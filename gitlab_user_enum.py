#!/usr/bin/env python3

# Modified from https://github.com/dpgg101/GitLabUserEnum. Added Threading, Colored output, a result file, and ASCII art.
import requests
import argparse
from termcolor import cprint
from concurrent.futures import ThreadPoolExecutor

def check_username(url, username):
    http_code = requests.head(f'{url}/{username}').status_code
    if http_code == 200:
        cprint(f'[+] The username {username} exists!', "green", attrs=['bold'])
        with open("result.txt", "a") as result_file:
            result_file.write(username + "\n")
    elif http_code == 0:
        print('[!] The target is unreachable.')
    else:
        cprint(f"[*] Testing: {username}", "yellow", attrs=['bold'])

def main():
    parser = argparse.ArgumentParser(description='GitLab User Enumeration')
    parser.add_argument('--url', '-u', type=str, required=True, help='The URL of the GitLab\'s instance')
    parser.add_argument('--wordlist', '-w', type=str, required=True, help='Path to the username wordlist')
    args = parser.parse_args()

    print(r"""

          ____
          \__/        @ @@     gitlab enummmmmmmeration
         `(  `^=_ p _@@@_      gitlab enummmmmmmeration
          c   /  )  |   /      gitlab enummmmmmmeration
   _____- //^---~  _c  3       gitlab enummmmmmmeration
 /  ----^\ /^_\   / --,-       gitlab enummmmmmmeration
(   |  |  O_| \\_/  ,/         gitlab enummmmmmmeration
|   |  | / \|  `-- /           gitlab enummmmmmmeration
(((G   |-----|                 gitlab enummmmmmmeration
      //-----\\                gitlab enummmmmmmeration
     //       \\               gitlab enummmmmmmeration
   /   |     |  ^|             gitlab enummmmmmmeration
   |   |     |   |             gitlab enummmmmmmeration
   |____|    |____|            gitlab enummmmmmmeration
  /______)   (_____\           gitlab enummmmmmmeration
          """)

    with open(args.wordlist, 'r') as f:
        usernames = [line.strip() for line in f]

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(check_username, args.url, username) for username in usernames]

    # Wait for all tasks to complete (optional, you can remove this if you want to exit immediately)
    for future in futures:
        future.result()

if __name__ == '__main__':
    main()
