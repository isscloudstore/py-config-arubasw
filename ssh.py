from netmiko import ConnectHandler

# Server SSH details
server = {
    "device_type": "linux",
    "host": "192.168.147.130",  # Change to your server's IP
    "username": "ladmin",
    "password": "P@ssw0rd",
    "port": 22,  # Default SSH port
}

# Argument to pass into command
directory = "/var/log"

try:
    # Connect to the server via SSH
    connection = ConnectHandler(**server)

    # Run a command on the server
    output = connection.send_command("uname -a")  # Check OS info
    print(output)

    # Run multiple commands
    commands_static = [
        "uptime",         # Show system uptime
        "df -h",          # Show disk usage
        "whoami"          # Show current user
    ]
    
    commands_dynamic = f"ls -l {directory}"

    for cmd in commands_static:
        response = connection.send_command(cmd)
        print(f"\nOutput of '{cmd}':\n{response}")
    
    output = connection.send_command(commands_dynamic)
    print(f"Output of '{commands_dynamic}':\n{output}")
    # Close connection
    connection.disconnect()

except Exception as e:
    print(f"Error: {e}")
