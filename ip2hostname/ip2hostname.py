 #!/usr/bin/python3
import socket   
with open("ips.txt") as ips:
    for i in ips:
        i = i.replace("\n", "")
        print (i + " , " +socket.gethostbyaddr(i)[0])
