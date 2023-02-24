import socket

# Get Private IP address (192.168.1.238)
HOST = "192.168.1.238"
# Port to connect to. I just picked a random one
PORT = 9999

# TCP socket hence the stream. This socket is only to connect
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))  # binds server to that port

# Accepts connections
server.listen(5)

# this returns a new socket in which we can communicate and the address of the connection
communication_socket, address = server.accept()
print(f"Connected to {address}")

while True:

    # Recive and decode message because it is sent as a bitstream
    rMessage = communication_socket.recv(1024).decode("utf-8")
    print(f"Message from client is: {rMessage}")

    # send message
    sMessage = input("Message to client: ")
    communication_socket.send(sMessage.encode("utf-8"))
