import socket
import threading

# List to keep track of connected client sockets
clients = []
clients_lock = threading.Lock()

def broadcast(message, sender_socket):
    """Send a message to all clients except the sender."""
    with clients_lock:
        for client in clients:
            if client != sender_socket:
                try:
                    client.sendall(message)
                except Exception:
                    # Remove client if sending fails
                    clients.remove(client)

def handle_client(client_socket, addr):
    """Handle incoming messages from a single client."""
    print(f"New connection from {addr}")
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                print(f"Connection closed by {addr}")
                break
            # Print on server console
            print(f"{addr}: {message.decode().strip()}")
            broadcast(message, client_socket)
        except Exception as e:
            print(f"Error with {addr}: {e}")
            break
    with clients_lock:
        if client_socket in clients:
            clients.remove(client_socket)
    client_socket.close()

def main():
    host = ''  # Bind to all available interfaces
    port = 5000  # Change port if needed

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Chat server started on port {port}. Waiting for connections...")

    try:
        while True:
            client_socket, addr = server_socket.accept()
            with clients_lock:
                clients.append(client_socket)
            client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
            client_thread.daemon = True
            client_thread.start()
    except KeyboardInterrupt:
        print("Server shutting down...")
    finally:
        server_socket.close()

if __name__ == '__main__':
    main()
