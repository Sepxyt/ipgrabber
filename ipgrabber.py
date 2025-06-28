import requests
import socket

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org')
        return response.text
    except requests.RequestException:
        return "Could not fetch public IP address"

def get_local_ip():
    try:
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)
    except socket.error:
        return "Could not fetch local IP address"

if __name__== "__main__":
    print("Public IP Address: ", get_public_ip())
    print("Local IP Address: ", get_local_ip())