import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = 'satish'
port = 2345
s.bind((host,port))
s.connect(('satish',80))
s.sendall('hi from client2')

