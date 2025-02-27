import argparse
from netmiko import ConnectHandler

# Set up argument parser
parser = argparse.ArgumentParser(description="Send command to server via SSH")
parser.add_argument("device_ip", type=str, help="Device Ip address")
parser.add_argument("dest_ip", type=str, help="Destination Ip address")
parsed_args = parser.parse_args()

# Server SSH details
server = {
    "device_type": "linux",
    "host": parsed_args.device_ip,  # Change to your server's IP
    "username": "ladmin",
    "password": "P@ssw0rd",
    "port": 22,  # Default SSH port
}

try:
    # Connect to the server via SSH
    connection = ConnectHandler(**server)

    commands = f"ping -c 5 {parsed_args.dest_ip}"
    output = connection.send_command(commands)
    print(output)

    #commands_check = 'hostnamectl'
    #output_check = connection.send_command(commands_check)
    #print(output_check)

    # Close connection
    connection.disconnect()

except Exception as e:
    print(f"Error: {e}")
