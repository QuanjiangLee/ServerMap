import socket
import select
import threading
import os

HOST ='127.0.0.1'
PORT = 5555
ADDR = (HOST, PORT)
BUF_SIZE = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen(1)
#simple socket
'''
conn, addr = server.accept()
print('server is connected by ', addr)
while True:
	data = conn.recv(BUF_SIZE)
	sdata = 'server recived success'
	if not data:
		break;
	print('server recv:', data.decode('utf-8'))
	conn.send(sdata.encode('utf-8'))
conn.close()
'''
#sync single socket
server.setblocking(0)
def process_conn(conn, addr):
    print('server is connected by:', addr)
    while True:
        data = conn.recv(BUF_SIZE)
        sdata = 'server is recieved success'
        if not data:
            break
        print('server recived:',data.decode('utf-8'))
        conn.send(sdata.encode('utf-8'))
    conn.close()
TreadNum = 0
while True:
	print('loop connection')
	r,w,e = select.select([server], [], [], 5)
	if server in r:
		conn,addr = server.accept()
		TreadNum = TreadNum + 1
		print('TreadNum:',TreadNum)
		#process_conn(conn, addr)
		t = threading.Thread(target=process_conn,name='server tread'+ str(TreadNum),args = (conn,addr))
		t.start() 
