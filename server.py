import socket

def main():
    host = ''  # Empty string means bind to all interfaces
    port = 51717  # Use any available port (ensure it is the same on client)

    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on port {port}...")

    # Wait for a connection
    conn, addr = server_socket.accept()
    print("Connected by", addr)

    # Receive data from the client
    data = conn.recv(1024)
    if data:
        print("Received:", data.decode())
        # Send an acknowledgement back to the client
        conn.sendall(b"I got your message")
    
    # Close the connection
    conn.close()
    server_socket.close()

if __name__ == '__main__':
    main()
