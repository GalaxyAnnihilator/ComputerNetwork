import socket

def main():
    # Replace with the server's IP address on your network (e.g., 172.16.0.194)
    host = "127.0.0.1"
    port = 51717

    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Get message from the user and send it to the server
    message = input("Please enter your message: ")
    client_socket.sendall(message.encode())

    # Receive the server's response
    data = client_socket.recv(1024)
    print("Received from server:", data.decode())

    # Close the connection
    client_socket.close()

if __name__ == '__main__':
    main()
