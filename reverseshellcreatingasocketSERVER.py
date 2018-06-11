import socket #connect 2 machine
import sys #command line

#create socket allows two computers to connect
def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket creatin erro:" + str(msg))


# bind socket to pport and wait for connection from client
def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port:" + str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("Socket binding erro:"+str(msg) + "\n" + "retring...")

# Establish a connection with client (socket must be listining for them)
def socket_accept():
    conn, address = s.accept()
    print("Connection has been established |" + "IP " + address[0]+ "| Port " + str(address[1]))
    send_commands(conn)
    conn.close()

def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0: #verify if type something
            conn.send(str.encode(cmd)) #necessary convert to str because it will be in bit
            client_response = str(conn.recv(1024), 'utf-8')
            print(client_response, end="") #move cursor to new line


def main():
    socket_create()
    socket_bind()
    socket_accept()

main()


