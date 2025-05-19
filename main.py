import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

def fetch_bgp_sessions(router_ip, username, password):
    url = f"http://{router_ip}/rest/routing/bgp/session"
    response = requests.get(url, auth=HTTPBasicAuth(username, password))

    if response.status_code == 200:
        sessions = response.json()
        print(f"\nRouter: {router_ip}\n")
        for session in sessions:
            print(f"Name: {session.get('name', 'N/A')}")
            print(f"Remote ID: {session.get('remote.id', 'N/A')}")
            print(f"Uptime: {session.get('uptime', 'N/A')}")
            print(f"Established: {session.get('state', 'N/A')}")
            print("-" * 30)
    else:
        print(f"Error connecting to {router_ip}: HTTP {response.status_code}")

if __name__ == "__main__":
    routers = os.getenv("ROUTERS", "")
    username = os.getenv("ROUTER_USER", "")
    passwords = os.getenv("PASSWORDS", "")

    if not routers or not username or not passwords:
        print("Please set ROUTERS, ROUTER_USER, and PASSWORDS in your .env file.")
        exit(1)

    router_list = [ip.strip() for ip in routers.split(",") if ip.strip()]
    password_list = [p.strip() for p in passwords.split(",") if p.strip()]

    if len(router_list) != len(password_list):
        print("The number of routers and passwords must be the same.")
        exit(1)

    for ip, pwd in zip(router_list, password_list):
        fetch_bgp_sessions(ip, username, pwd)
