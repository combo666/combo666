import socket
import threading
import os

def handle_request(client_socket):
    request = client_socket.recv(1024).decode('utf-8')
    request_method, file_path = parse_request(request)

    if request_method == 'GET':
        response = handle_get_request(file_path)
    elif request_method == 'POST':
        response = handle_post_request(request)
    else:
        response = generate_error_response(400, "Bad Request")

    client_socket.sendall(response)
    client_socket.close()

def parse_request(request):
    parts = request.split(' ')
    request_method = parts[0]
    file_path = parts[1][1:]  # Remove the leading slash (/) from the file path
    return request_method, file_path

def handle_get_request(file_path):
    if file_path == "":
        file_path = "index.html"

    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
        response_body = content.encode('utf-8')
        response_header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
        return response_header.encode('utf-8') + response_body
    else:
        return generate_error_response(404, "Not Found")

def handle_post_request(request):
    # Handle POST request data here (e.g., store in a database)
    response_body = "POST request received".encode('utf-8')
    response_header = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\n"
    return response_header.encode('utf-8') + response_body

def generate_error_response(status_code, message):
    response_body = f"{status_code} {message}".encode('utf-8')
    response_header = f"HTTP/1.1 {status_code} {message}\r\nContent-Type: text/plain\r\n\r\n"
    return response_header.encode('utf-8') + response_body

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8000))
    server_socket.listen(5)
    print("Server listening on port 8000")

    while True:
        client_socket, client_addr = server_socket.accept()
        print(f"Connection from {client_addr[0]}:{client_addr[1]}")
        client_thread = threading.Thread(target=handle_request, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    main()
