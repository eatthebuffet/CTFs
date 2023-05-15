import socket
import threading
import os


# filepath, remove if old result file is there.
cwd = os.getcwd()
error_fileName = "vrfy_errors.txt"
errors_path = cwd + "/" + error_fileName

result_fileName = "vrfy_result.txt"
result_path = cwd + "/" + result_fileName

if os.path.isfile(result_path):
    os.remove(result_path)

if os.path.isfile(errors_path):
    os.remove(errors_path)

# IP address of the SMTP server
SMTP_SERVER = 'IP'

# Port number to connect
SMTP_PORT = 25

# File containing list of usernames to bruteforce
#USERNAME_FILE = '/usr/share/seclists/Usernames/Names/names.txt'
USERNAME_FILE = cwd + '/wordlist.txt'
def closeFiles(username):
    if username:
        result_file = open(result_path, mode="a")
        result_file.write(username + '\n')
        result_file.close()

    file = open(USERNAME_FILE, mode="r")
    file.close()

    file_errors = open(errors_path, mode="a")
    file_errors.close()

def bruteforce():
    # Open the file containing the usernames
    with open(USERNAME_FILE, 'r') as file:
        # Loop through each line in the file
        for username in file:
            # Strip any whitespace characters
            username = username.strip()

            # Create a socket object
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Connect to the SMTP server over nc
            s.connect((SMTP_SERVER, SMTP_PORT))

            # Receive the banner message from the server
            banner = s.recv(1024)
            print(banner.decode())

            # Send the HELO command to the server
            helo_command = 'HELO test\r\n'
            s.send(helo_command.encode())
            response = s.recv(1024)
            print(response.decode())

            # Send the VRFY command to the server with the current username
            vrfy_command = 'VRFY {}\r\n'.format(username)
            s.send(vrfy_command.encode())
            response = s.recv(1024)

            # Check if the username was found
            if '252' in response.decode():
                print('Found username: {}'.format(username))
                closeFiles(username)

            # Close the socket connection
            s.close()


#program go vrooooom
threads = []

for i in range(50):
    t = threading.Thread(target=bruteforce)
    t.daemon=True
    threads.append(t)

for i in range(50):
    threads[i].start()

for i in range(50):
    threads[i].join()

if __name__ == '__main__':
    bruteforce()
