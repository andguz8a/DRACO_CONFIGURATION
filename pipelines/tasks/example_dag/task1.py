import socket

def get_server_info():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)

    message = f"Hola mundo desde {hostname} con IP {ip}"
    print(message)

    return message