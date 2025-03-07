# PenetationTestingToolkit
# Penetration Testing Toolkit

![Penetration Testing Toolkit](https://img.shields.io/badge/Penetration%20Testing-Toolkit-blue)

## 📌 Overview
This is a Python-based penetration testing toolkit that includes multiple security modules. The current version features:
- **🛠️ Port Scanner**: Checks for open ports on a target IP.
- **🔑 Brute Force Attack**: Attempts to guess login credentials using a wordlist.

## 🚀 Features
- 🛡️ Easy-to-use command-line interface
- 🚀 Fast and efficient scanning
- ✅ Validates IP addresses before scanning
- 🔍 Detects open ports on a target machine
- 🔑 Attempts login brute-force attacks on web forms

## 📦 Installation
To install this toolkit, clone the repository:

```bash
git clone https://github.com/Hipster2110/PenetationTestingToolkit.git
cd PenetationTestingToolkit
```

Ensure you have Python installed (Python 3.x recommended). Install dependencies using:

```bash
pip install requests
```
To use this toolkit, ensure you have Python installed (Python 3.x recommended). Install dependencies using:

```bash
pip install requests
```

## 🛠️ Usage
Run the script using:

```bash
python PenetrationTestingToolkit.py
```

### 1️⃣ Port Scanner
- Enter a valid target IP address.
- Provide ports to scan (comma-separated).
- The tool will check which ports are open.

### 2️⃣ Brute Force Attack
- Enter the target login page URL.
- Provide the username for login.
- Specify the path to a password wordlist.
- The tool will attempt to log in with different passwords.

## 🔍 Example Commands
#### Running Port Scanner
```bash
python PenetrationTestingToolkit.py
```
```plaintext
Choose an option (1/2): 1
Enter target IP address: 192.168.1.1
Enter ports to scan (comma-separated): 80,443,22
✅ Port 80 is open
❌ Port 443 is closed
✅ Port 22 is open
```

#### Running Brute Force Attack
```bash
python PenetrationTestingToolkit.py
```
```plaintext
Choose an option (1/2): 2
Enter login URL: http://example.com/login
Enter username: admin
Enter path to password wordlist: passwords.txt
🎉 Login successful: admin:123456
```

## 👨‍💻 Author
Developed by **Hipster2110**.

## ⚠️ Disclaimer
**This tool is for educational and ethical testing purposes only. Unauthorized use against systems without permission is illegal!**

## 🌟 Contributing
Pull requests are welcome! Feel free to submit bug reports or feature requests.

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

