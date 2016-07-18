import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = 'satish'
port = 12345
s.bind((host,port))
s.connect(('satish',80))
s.sendall('hi! from client')












