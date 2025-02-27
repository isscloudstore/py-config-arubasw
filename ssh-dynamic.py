import argparse
from netmiko import ConnectHandler

# Server SSH details
server = {
    "device_type": "linux",
    "host": "192.168.147.130",  # Change to your server's IP
    "username": "ladmin",
    "password": "P@ssw0rd",
    "port": 22,  # Default SSH port
}

# Set up argument parser
parser = argparse.ArgumentParser(description="Send command to server via SSH")
parser.add_argument("ip", type=str, help="Ip address")
parsed_args = parser.parse_args()

try:
    # Connect to the server via SSH
    connection = ConnectHandler(**server)

    commands = f"ping -c 5 {parsed_args.ip}"
    output = connection.send_command(commands)
    print(output)

    #commands_check = 'hostnamectl'
    #output_check = connection.send_command(commands_check)
    #print(output_check)

    # Close connection
    connection.disconnect()

except Exception as e:
    print(f"Error: {e}")
