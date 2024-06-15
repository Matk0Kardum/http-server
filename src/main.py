import socket
import threading
from handle_client import handle_client


# @TODO ADD HTTP COMPRESSION
# @TODO CONVERT HEADERS TO LOWERCASE BEFORE COMPARISON
def main():
    print("Logging...")

    try:
        # Creating the server
        server_socket = socket.create_server(("localhost", 8080), reuse_port=True)
        while True:
            # Waiting for connection
            client_socket, client_address = server_socket.accept()
            print(f"Client address: {client_address}")

            # Creating the thread for concurrent connections
            client_thread = threading.Thread(target=handle_client, args=(client_socket,))
            # Starting the thread
            client_thread.start()
    except KeyboardInterrupt:
        print("\nLogging interrupted, stopping now...")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Check if those sockets are defined in local scope and close their connection if they are
        if "server_socket" in locals():
            server_socket.close()
        if "client_socket" in locals():
            client_socket.close()


if __name__ == "__main__":
    main()
