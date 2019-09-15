import socket

# Creating a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecting the socket to the port where the server is listening
host = 'localhost'
port = 9500
print('Now Connecting to {} port: {}'.format(host,port))
sock.connect((host,port))

# Sending the inputed data
output = input('What do you want to send? ')
print('Sending:', output)
sock.sendall(output.encode('utf-8'))

# Getting a response
data = sock.recv(100)
print('Received from server:', data.decode())

# Closing socket
print('Closing socket')
sock.close()