import telnetlib
import argparse
import time

#parse the ip of devices
parser = argparse.ArgumentParser(description="Connect to a device via Telnet.")
parser.add_argument("device_ip", help="Aruba device hostname or IP address")
args = parser.parse_args()
device_ip = args.device_ip


# default credentials
username='root'
password='P@ssw0rd'

# command for initial configuration
command = ["ifconfig"]


try:

# connect to the device
    tn = telnetlib.Telnet(device_ip)

# login successfully
    tn.read_until(b"Login Username: ")
    tn.write(username.encode('ascii') + b"\n")
    tn.read_until(b"Login Password: ")
    tn.write(password.encode('ascii') + b"\n")

# Send configuration commands
    for command in command:
        tn.write(command.encode('ascii') + b"\n")
        time.sleep(1)  # Allow the command to execute
    output = tn.read_all().decode('ascii')
    print(output)

# Close the connection
    tn.close()
except Exception as e:
    print(f"Error: {e}")