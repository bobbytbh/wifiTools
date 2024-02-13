import subprocess
import re 
import os

def getWLAN():
    def get_wifi_profiles():
        try:
            # Ottieni l'output di 'netsh wlan show profiles'
            result = os.popen('netsh wlan show profiles').read()
            
            # Trova tutti i nomi dei profili WiFi nell'output
            profile_names = re.findall(r'Tutti i profili utente\s*:\s*(.*)', result)
            return profile_names

        except Exception as e:
            print(f"Errore durante l'esecuzione del comando: {e}")
            return []

    def get_wifi_password(profile_name):
        try:
            # Ottieni l'output di 'netsh wlan show profile name="profile_name" key=clear'
            result = os.popen(f'netsh wlan show profile name="{profile_name}" key=clear').read()

            # Estrai la password dalla riga che contiene 'Contenuto chiave'
            password_match = re.search(r'Contenuto chiave\s*:\s*(.*)', result)
            password = password_match.group(1) if password_match else None
            return password

        except Exception as e:
            print(f"Errore durante l'esecuzione del comando: {e}")
            return None

    # Ottieni tutti i profili WiFi
    profile_names = get_wifi_profiles()
    
    # Creiamo una lista di stringhe per memorizzare i profili e le relative password
    wifi_profiles = []

    # Per ogni profilo, ottieni la password corrispondente
    for profile_name in profile_names:
        password = get_wifi_password(profile_name)

        # Formatta il nome del profilo e la password e aggiungilo alla lista
        profile_info = f"{profile_name}: {password}" if password else f"{profile_name}: Assente"
        wifi_profiles.append(profile_info)
    
    # Unisci tutte le stringhe della lista in un'unica stringa separata da newline
    return '\n'.join(wifi_profiles)

def getLAN():
    try:
        output = os.popen("netsh interface show interface").read()
    #    print("LAN Output:")
    except Exception as e:
        print("Errore durante l'esecuzione di 'netsh interface show interface':", e)
        return []

    interfaces = []
    for line in output.split('\n'):
        if line.startswith("Connessione"):
            interface = line.split()[-1]
            interfaces.append(interface)

    return interfaces

def getIP():
    try:
        output = os.popen("ipconfig").read()
    #    print("IPConfig Output:")
    except Exception as e:
        print("Errore durante l'esecuzione di 'ipconfig':", e)
        return {}

    ipv4 = ""
    subnet_mask = "" 
    gateway = ""

    # Utilizziamo le espressioni regolari per cercare i pattern corrispondenti
    ipv4_pattern = re.compile(r'Indirizzo IPv4[ .]+: ([0-9.]+)')
    subnet_mask_pattern = re.compile(r'Subnet mask[ .]+: ([0-9.]+)')
    gateway_pattern = re.compile(r'Gateway predefinito[ .]+: ([0-9.]+)')

    # Cerchiamo le corrispondenze nei dati di output
    ipv4_match = ipv4_pattern.search(output)
    subnet_mask_match = subnet_mask_pattern.search(output)
    gateway_match = gateway_pattern.search(output)

    # Estraiamo i valori corrispondenti se trovati
    if ipv4_match:
        ipv4 = ipv4_match.group(1)
    if subnet_mask_match:
        subnet_mask = subnet_mask_match.group(1)
    if gateway_match:
        gateway = gateway_match.group(1)

    freturn = f"IPv4: {ipv4}\nSubnet mask: {subnet_mask}\nDefault gateway: {gateway}"

    return freturn

def getDNS():
    try:
        output = subprocess.getoutput("ipconfig /displaydns")
    #    print("DNS Output:")
    except Exception as e:
        print("Error executing 'ipconfig /displaydns':", e)
        return []

    return output

def getMAC():
    try:
        output = subprocess.getoutput("getmac")
    #    print("MAC Output:")
    except Exception as e:
        print("Error executing 'getmac':", e)
        return []

    adapters = []
    adapter = {}
    for line in output.split('\n'):
        if "Physical Address" in line:
            if adapter:
                adapters.append(adapter)
            adapter = {}
            adapter["Physical Address"] = line.split()[0]
            adapter["Name"] = line.split()[1]

    if adapter:
        adapters.append(adapter)

    return adapters

def getNET():
    return f"\n\n\n\nWLAN:\n{getWLAN()}\n\n\nLAN:\n{getLAN()}\n\n\nIP:\n{getIP()}\n\n\nDNS:\n{getDNS()}\n\n\nMAC:\n{getMAC()}"