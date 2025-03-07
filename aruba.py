from netmiko import ConnectHandler
import re
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description="Send command to server via SSH")
parser.add_argument("device_ip", type=str, help="Device Ip address")
parsed_args = parser.parse_args()



# Aruba switch details
device = {
    "device_type": "aruba_os",
    "host": parsed_args.device_ip,  # Replace with your switch IP using argparse
    "username": "admin",
    "password": "aruba",
}

try:
    # Connect to the switch
    connection = ConnectHandler(**device)

    # Get Product Name for load configuration
    output_connection=connection.send_command(f"show system\n")
    pattern_pn = r"Product Name\s+\:\s+(.*?)\s"
    matches_pn = re.findall(pattern_pn, output_connection) # Extract Product Name
    print(matches_pn)

    # Load configuration from tftp server
    connection.send_command("copy tftp://192.168.10.1/{matches_pn[0]}.cfg running-config", expect_string=r"#")
    connection.send_command("copy running-config startup-config", expect_string=r"#")


    # Get IP Address for change ip of vlan 1021
    output_ip_vlan1=connection.send_command(f"show ip int brief\n")
    pattern_ip_vlan1 = r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/"
    matches_ip_vlan1 = re.findall(pattern_ip_vlan1, output_ip_vlan1) #Extract IP address of vlan 1
    print(matches_ip_vlan1)

    # Change IP address off vlan 1021
    output_change_ip=connection.send_command(f"config\nint vlan 1021\nip addr 10.102.{matches_ip_vlan1[0][2]}.{matches_ip_vlan1[0][3]}/24\nend", expect_string=r"#")


    print("Configuration changed successfully!")
    
    # Disconnect from the switch
    connection.disconnect()

except Exception as e:
    print(f"Failed to change config: {e}")
