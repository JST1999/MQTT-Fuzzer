import socket

HOST = '127.0.0.1'
PORT = 9998

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

client.send(b'Hi')
response = client.recv(4096)
print(response.decode('utf-8'))

client.close()
