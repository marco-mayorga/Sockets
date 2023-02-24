import socket

# Get Private IP address (192.168.1.238)
HOST = "192.168.1.238"
# Port to connect to. I just picked a random one
PORT = 9999

# TCP socket hence the stream. This socket is only to running server,
# listening for connections and accepting them
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

# this returns a new socket in which we can communicate and the address of the connection
address = socket.getsockname()
print(f"Connected to {address}")

while True:

    sMessage = input("Message To Server: ")
    socket.send(sMessage.encode("utf-8"))

    # Recive and decode message because it is sent as a bitstream
    rMessage = socket.recv(1024).decode("utf-8")
    print(f"Message from server is: {rMessage}")
