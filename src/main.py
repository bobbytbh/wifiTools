import functions.GetNet as gn

def main():
    print("Icons by: https://icons8.com/")
    while True:
        scelta = input("Inserisci '1' per WLAN, '2' per LAN, '3' per IP, '4' per DNS, '5' per MAC, '6' per WLAN, LAN, IP, DNS, MAC, '7' per Esci: ")
        if scelta == '1':
            print("Please wait while we try to retrive informations about your WLAN")
            a = gn.getWLAN()
            print(a)            
        elif scelta == '2':
            print("Please wait while we try to retrive informations about your LAN")
            a = gn.getLAN()
            print(a)
        elif scelta == '3':
            print("Please wait while we try to retrive informations about your IP")
            a = gn.getIP()
            print(a)
        elif scelta == '4':
            print("Please wait while we try to retrive informations about your DNS")
            a = gn.getDNS()
            print(a)
        elif scelta == '5':
            print("Please wait while we try to retrive informations about your MAC")
            a = gn.getMAC()
            print(a)
        elif scelta == '6':
            print("Please wait while we try to retrive informations")
            a = gn.getNET()
            print(a)
        elif scelta == '4':
            break

if __name__ == '__main__':
    main()