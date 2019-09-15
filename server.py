import socket

# Creating a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding the socket to the port
host = 'localhost'
port = 9500
print('Now Connecting to {} port: {}'.format(host,port))
sock.bind((host,port))


# Listening for incoming connections
sock.listen(1)

# Waiting for a connection
while True:
    print('Waiting for a connection...')
    connection, client_address = sock.accept()
    print('Connected to:', client_address)
    print('Waiting to receive data...')


#Receiving Data
    data = connection.recv(100)
    print('Server has received:', data.decode())

    if data.decode() == 'Hello':
        print('Sending: Hi')
        output = 'Hi'
        connection.sendall(output.encode('utf-8'))

    else:
        print('Sending: Goodbye')
        output = 'Goodbye'
        connection.sendall(output.encode('utf-8'))

# Closing the connection
print('Closing connection')
connection.close()