from netmiko import ConnectHandler

# Server SSH details
server = {
    "device_type": "linux",
    "host": "192.168.147.130",  # Change to your server's IP
    "username": "ladmin",
    "password": "P@ssw0rd",
    "port": 22,  # Default SSH port
}

try:
    # Connect to the server via SSH
    connection = ConnectHandler(**server)

    # Run a command on the server
    output = connection.send_command("uname -a")  # Check OS info
    print(output)

    # Run multiple commands
    commands = [
        "uptime",         # Show system uptime
        "df -h",          # Show disk usage
        "whoami"          # Show current user
    ]
    
    for cmd in commands:
        response = connection.send_command(cmd)
        print(f"\nOutput of '{cmd}':\n{response}")

    # Close connection
    connection.disconnect()

except Exception as e:
    print(f"Error: {e}")
