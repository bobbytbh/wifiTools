import functions.GetNet as gn
import functions.getNetEn as gne
from langdetect import detect
import os

def main():
    print("Icons by: https://icons8.com/")
    # controlla la lingua del sistema operativo
    lang = detect(os.popen('ipconfig').read())
    
    if lang == "it":
        print("Lingua di sistema rilevata: Italiano")
        while True:
            scelta = input("Inserisci '1' per WLAN, '2' per LAN, '3' per IP, '4' per DNS, '5' per MAC, '6' per tutti, '7' per uscire: ")
            if scelta == '1':
                print("Attendere mentre proviamo a recuperare informazioni sulla WLAN")
                a = gn.getWLAN()
                print(a)            
            elif scelta == '2':
                print("Attendere mentre proviamo a recuperare informazioni sulla LAN")
                a = gn.getLAN()
                print(a)
            elif scelta == '3':
                print("Attendere mentre proviamo a recuperare informazioni sull'IP")
                a = gn.getIP()
                print(a)
            elif scelta == '4':
                print("Attendere mentre proviamo a recuperare informazioni sul DNS")
                a = gn.getDNS()
                print(a)
            elif scelta == '5':
                print("Attendere mentre proviamo a recuperare informazioni sul MAC")
                a = gn.getMAC()
                print(a)
            elif scelta == '6':
                print("Attendere mentre proviamo a recuperare tutte le informazioni")
                a = gn.getNET()
                print(a)
            elif scelta == '7':
                break

    elif lang == "en":
        print("Detected system language: English")
        
        while True:
            choice = input("Insert '1' for WLAN, '2' for LAN, '3' for IP, '4' for DNS, '5' for MAC, '6' for all, '7' to exit: ")
            if choice == '1':
                print("Please wait while we try to retrive informations about your WLAN")
                a = gne.getWLAN()
                print(a)            
            elif choice == '2':
                print("Please wait while we try to retrive informations about your LAN")
                a = gne.getLAN()
                print(a)
            elif choice == '3':
                print("Please wait while we try to retrive informations about your IP")
                a = gne.getIP()
                print(a)
            elif choice == '4':
                print("Please wait while we try to retrive informations about your DNS")
                a = gne.getDNS()
                print(a)
            elif choice == '5':
                print("Please wait while we try to retrive informations about your MAC")
                a = gne.getMAC()
                print(a)
            elif choice == '6':
                print("Please wait while we try to retrive informations")
                a = gne.getNET()
                print(a)
            elif choice == '7':
                break
        

if __name__ == '__main__':
    main()