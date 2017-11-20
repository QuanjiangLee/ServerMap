import socket

HOST = '127.0.0.1'
PORT = 5555
ADDR = (HOST, PORT)
BUF_SIZE = 1024
sdata = 'client says: hello'
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
client.send(sdata.encode('utf-8'))
data = client.recv(BUF_SIZE)
if data:
	print('client recieved :', data.decode('utf-8'))
#client.close()