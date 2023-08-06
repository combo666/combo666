import socket
import threading
from pathlib import Path
from urllib.parse import urlparse

def get_file_content(filename):
   
    try:
        with open(filepath, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return None

def handle_client_connection(client_socket):
    request = client_socket.recv(1024).decode()

    
    path = urlparse(request).path or '/'

    if path == '/':
        filename = 'index.html'
    else:
        filename = path[1:]  # Remove the leading '/' from the path

    content = get_file_content(filename)

    if content is not None:
        response_status = 'HTTP/1.1 200 OK'
        content_length = len(content)
    else:
        content = '<h1>404 Not Found</h1>'
        response_status = 'HTTP/1.1 404 NOT FOUND'
        content_length = len(content)

    response_header = f'{response_status}\nContent-Type: text/html\nContent-Length: {content_length}\n\n'
    response = response_header + content
    client_socket.sendall(response.encode())
    client_socket.close()

def main():
    SERVER_HOST = '127.0.0.1'
    SERVER_PORT = 8080

    global htdocs_path
    htdocs_path = Path('htdocs').resolve()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(5)
    print(f'Listening on port {SERVER_PORT} ...')

    while True:
        client_connection, client_address = server_socket.accept()
        print(f'Accepted connection from {client_address[0]}:{client_address[1]}')

        
        client_thread = threading.Thread(target=handle_client_connection, args=(client_connection,))
        client_thread.start()

    server_socket.close()

if __name__ == "__main__":
    main()
