import sys
from ftplib import FTP

port = int(sys.argv[1])
my_ftp = FTP()
my_ftp.connect('localhost',port)
