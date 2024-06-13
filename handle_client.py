from process_request import process_request
from create_response import create_response


def handle_client(client_socket):
    while True:
        # Receiving user's request and decoding it
        client_request = client_socket.recv(1024).decode()

        # If there isn't client request break the loop and close the socket connection
        if not client_request:
            break

        # Separate object with status, headers and the body of the request
        processed_request = process_request(client_request)
        print(f"Status: {processed_request.get_status()}")
        print(f"Headers: {processed_request.get_headers()}")
        print(f"Body: {processed_request.get_body()}")

        # Create a response from the request
        response = create_response(processed_request)

        # Send encoded response to the client
        client_socket.sendall(response.encode())

    # Close the socket connection
    client_socket.close()
