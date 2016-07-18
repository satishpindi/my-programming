import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print socket.gethostname()
print socket.gethostbyname(socket.gethostname())
host = 'satish'
port = 80
s.bind((host,port))
s.listen(5)
while True:
     conn,address = s.accept()
     print 'got connected from',conn,address
     data = conn.recv(1024)
     print 'server recieved',repr(data)
     
     

     
     





