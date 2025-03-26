import requests
import json
import urllib3
import time
import argparse
import getpass

# Disable cert warnings
urllib3.disable_warnings()

parser = argparse.ArgumentParser(description="Program to send CLI commands to Lenovo ThinkSystem storage arrays")
parser.add_argument("-u", "--username", type=str, default="monitor", help='Username for authentication, defaults to "monitor"')
parser.add_argument("-p", "--password", type=str, help="Password for authentication (will prompt if not provided)")
parser.add_argument("-c", "--command", type=str, required=True, help="Command to run")
parser.add_argument("-H", "--host", type=str, required=True, help="Target host address or IP")
args = parser.parse_args()
# Prompt for password if not provided
if args.password is None:
    args.password = getpass.getpass("Password: ")

# Define constants
HOST = f"https://{args.host}"
LOGIN_URL = f"{HOST}/devmgr/utils/login"
COMMAND_URL = f"{HOST}/devmgr/internal/storage-systems/1/cli/command"
LOGOUT_URL = f"{HOST}/devmgr/utils/login"

# User credentials
payload = {"userId": args.username, "password": args.password}

# Create a session to persist cookies
session = requests.Session()

# Authenticate
login_response = session.post(LOGIN_URL, json=payload, verify=False)
if login_response.status_code != 200:
    print("Login failed!")
    print(login_response.text)
    exit(1)

# Command payload. The storage array expects the command to end with a semicolon
if args.command.endswith(";"):
    command = args.command
else:
    command = args.command + ";"
timestamp = int(time.time() * 1000)
command_payload = {
    "timestamp": f"{timestamp}",  # I suspect this doesn't matter
    "command": {
        "command": command
    },
    "clientVersion": "01.00"
}

# Send command request
command_response = session.post(COMMAND_URL, json=command_payload, verify=False)
if command_response.status_code == 200:
    json_data = json.loads(command_response.text)
    print(json_data["outputValue"])

# Logout to clean up session
session.delete(LOGOUT_URL, verify=False)