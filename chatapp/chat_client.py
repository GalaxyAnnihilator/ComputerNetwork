import socket
import threading
import sys

def receive_messages(sock):
    """Continuously listen for messages from the server and print them."""
    while True:
        try:
            message = sock.recv(1024)
            if not message:
                print("Disconnected from server.")
                break
            print("\r" + message.decode().strip() + "\n> ", end='')
        except Exception as e:
            print("Error receiving message:", e)
            break
    sock.close()
    sys.exit()

def send_messages(sock):
    """Read user input from the terminal and send it to the server."""
    while True:
        try:
            message = input("> ")
            if message.lower() == "quit":
                sock.close()
                sys.exit()
            sock.sendall(message.encode())
        except Exception as e:
            print("Error sending message:", e)
            break

def main():
    # Replace 'server_ip_address' with the actual IP of the machine running the server.
    server_ip = "172.16.0.194"  # Example: update with your server's IP address
    port = 5000  # Must match the port used by the server

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((server_ip, port))
    except Exception as e:
        print("Unable to connect to the server:", e)
        return

    print("Connected to chat server. Type 'quit' to exit.")

    # Start a thread to listen for messages from the server
    thread_recv = threading.Thread(target=receive_messages, args=(client_socket,))
    thread_recv.daemon = True
    thread_recv.start()

    # Main thread for sending messages
    send_messages(client_socket)

if __name__ == '__main__':
    main()
