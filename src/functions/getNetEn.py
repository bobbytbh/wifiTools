import re 
import os

def getWLAN():
    def get_wifi_profiles():
        try:
            result = os.popen('netsh wlan show profiles').read()
            profile_names = re.findall(r'All User Profile\s*:\s*(.*)', result)
            return profile_names
        except Exception as e:
            print(f"Error during the command execution: {e}")
            return []

    def get_wifi_password(profile_name):
        try:
            result = os.popen(f'netsh wlan show profile name="{profile_name}" key=clear').read()
            password_match = re.search(r'Key Content\s*:\s*(.*)', result)
            password = password_match.group(1) if password_match else None
            return password
        except Exception as e:
            print(f"Error during the command execution: {e}")
            return None

    profile_names = get_wifi_profiles()
    wifi_profiles = []

    for profile_name in profile_names:
        password = get_wifi_password(profile_name)
        profile_info = f"{profile_name}: {password}" if password else f"{profile_name}: Absent"
        wifi_profiles.append(profile_info)

    return '\n'.join(wifi_profiles)

def getLAN():
    try:
        output = os.popen("netsh interface show interface").read()
    except Exception as e:
        print("Error executing 'netsh interface show interface':", e)
        return []

    interfaces = []
    for line in output.split('\n'):
        if line.startswith("Connection"):
            interface = line.split()[-1]
            interfaces.append(interface)

    return interfaces

def getIP():
    try:
        output = os.popen("ipconfig").read()
    except Exception as e:
        print("Error executing 'ipconfig':", e)
        return {}

    ipv4 = ""
    subnet_mask = "" 
    gateway = ""

    ipv4_pattern = re.compile(r'IPv4 Address[ .]+: ([0-9.]+)')
    subnet_mask_pattern = re.compile(r'Subnet Mask[ .]+: ([0-9.]+)')
    gateway_pattern = re.compile(r'Default Gateway[ .]+: ([0-9.]+)')

    ipv4_match = ipv4_pattern.search(output)
    subnet_mask_match = subnet_mask_pattern.search(output)
    gateway_match = gateway_pattern.search(output)

    if ipv4_match:
        ipv4 = ipv4_match.group(1)
    if subnet_mask_match:
        subnet_mask = subnet_mask_match.group(1)
    if gateway_match:
        gateway = gateway_match.group(1)

    result = f"IPv4: {ipv4}\nSubnet Mask: {subnet_mask}\nDefault Gateway: {gateway}"

    return result

def getDNS():
    try:
        output = os.popen("ipconfig /displaydns").read()
    except Exception as e:
        print("Error executing 'ipconfig /displaydns':", e)
        return []

    return output

def getMAC():
    try:
        output = os.popen("getmac /fo table /nh").read()
    except Exception as e:
        print("Error executing 'getmac':", e)
        return "Error executing 'getmac': " + str(e)

    result = ""
    transport_pattern = re.compile(r"^(.*?)\s{2,}(.*?)$", re.IGNORECASE | re.MULTILINE)
    transport_matches = transport_pattern.findall(output)

    for transport_match in transport_matches:
        mac_address = transport_match[0].strip()
        transport_name = transport_match[1].strip()
        result += "\n\n"
        result += "Physical Address: " + mac_address + "\n"
        result += "Transport Name: " + transport_name + "\n"
        result += "\n"

    return result.strip()

def getNET():
    return f"\n\n\n\nWLAN:\n{getWLAN()}\n\n\nLAN:\n{getLAN()}\n\n\nIP:\n{getIP()}\n\n\nDNS:\n{getDNS()}\n\n\nMAC:\n{getMAC()}"