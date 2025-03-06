from netmiko import ConnectHandler
import re

# Server SSH details
server = {
    "device_type": "linux",
    "host": "192.168.10.11",  # Change to your server's IP
    "username": "admin",
    "password": "",
    "port": 22,  # Default SSH port
}

try:
    # Connect to the server via SSH
    connection = ConnectHandler(**server)

    # Run multiple commands
    commands_static = [
#       "uptime",         # Show system uptime
#      "df -h",          # Show disk usage
#       "whoami"          # Show current user
        "show system"
    ]
    
#    commands_dynamic = f"ls -l {directory}"

    for cmd in commands_static:
        response = connection.send_command(cmd)
        print(f"\nOutput of '{cmd}':\n{response}")
    
#    output = connection.send_command(commands_dynamic)
#    print(f"Output of '{commands_dynamic}':\n{output}")
    # Close connection
#    connection.disconnect()

        # Regex pattern to match interface name and IP
#        pattern = r"inet\s(\d+)\.(\d+)\.(\d+)\.(\d+)"
#        matches = re.findall(pattern, response)

#        print(matches[0][1])

except Exception as e:
    print(f"Error: {e}")
