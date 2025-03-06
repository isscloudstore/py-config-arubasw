from netmiko import ConnectHandler
import re

# Aruba switch details
device = {
    "device_type": "aruba_os",
    "host": "192.168.10.11",  # Replace with your switch IP
    "username": "admin",
    "password": "aruba",
}

try:
    # Connect to the switch
    connection = ConnectHandler(**device)
    output=connection.send_command(f"show system\n")
    pattern = r"Product Name\s+\:\s+(.*?)\s"
    matches = re.findall(pattern, output)
    print(matches)

    # Output 1 change username
    connection.send_command(f"configure terminal\nuser admin group administrators password plaintext aruba\nexit", expect_string=r"#")
    output1 = connection.send_command(f"show user information", expect_string=r"#")
    print(output1)


    # Change hostname
    connection.send_command(f"configure terminal\nhostname {matches[0]}\nexit", expect_string=r"#")
    output2 = connection.send_command(f"show hostname", expect_string=r"#")
    print(output2)

#   # Exit config mode
#    connection.send_command("exit", expect_string=r"#")

    # Save configuration
    connection.send_command("copy running-config startup-config", expect_string=r"#")

    print("Hostname changed successfully!")
    
    # Disconnect from the switch
    connection.disconnect()

except Exception as e:
    print(f"Failed to change config: {e}")
