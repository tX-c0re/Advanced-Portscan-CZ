import os
import socket
import subprocess
import sys
from tqdm import tqdm
import getpass  # Import knihovny pro skrytí hesla

def vytvor_logo():
 
    logo = """
    
\x1b[31m
**********************************************************************************************************                                  
                                                                                                   
\x1b[32m\x1b[5m
			   __          ___       ___     __                  ___ ___ 
		|__|  /\  /  ` |__/     |  |__| |__     |__) |     /\  |\ | |__   |  
		|  | /~~\ \__, |  \     |  |  | |___    |    |___ /~~\ | \| |___  |
				⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣶⠖⠀⠀⠲⣶⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
				⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠋⠀⠀⠀⠀⠀⠀⠙⢿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀
				⠀⠀⠀⠀⠀⠀⢀⣾⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣷⡀⠀⠀⠀⠀⠀⠀
				⠀⠀⠀⠀⠀⠀⣾⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣷⠀⠀⠀⠀⠀⠀
				⠀⠀⠀⠀⠀⠀⣿⣿⣿⣇⣤⠶⠛⣛⣉⣙⡛⠛⢶⣄⣸⣿⣿⣿⠀⠀⠀⠀⠀⠀
				⠀⠀⠀⠀⢀⣀⣿⣿⣿⡟⢁⣴⣿⣿⣿⣿⣿⣿⣦⡈⢿⣿⣿⣿⣀⡀⠀⠀⠀⠀
				⠀⠀⢠⣴⣿⣿⣿⣿⡟⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡌⢿⣿⣿⣿⣿⣦⡄⠀⠀
				⠀⣴⣿⣿⡿⠿⢛⣻⡇⢸⡟⠻⣿⣿⣿⣿⣿⡿⠟⢻⡇⣸⣛⡛⠿⣿⣿⣿⣦⠀
				⢸⣿⡿⠋⠀⠀⢸⣿⣿⡜⢧⣄⣀⣉⡿⣿⣉⣀⣠⣼⢁⣿⣿⡇⠀⠀⠙⢿⣿⡆
				⣿⣿⠁⠀⠀⠀⠈⣿⣿⡇⣿⡿⠛⣿⣵⣮⣿⡟⢻⡿⢨⣿⣿⠀⠀⠀⠀⠈⣿⣿
				⢿⡟⠀⠀⠀⠀⠀⠘⣿⣷⣤⣄⡀⣿⣿⣿⣿⢁⣤⣶⣿⣿⠃⠀⠀⠀⠀⠀⣿⡟
				⠘⠇⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡇⢿⣿⣿⣿⢸⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠻⠃
				⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⢩⣦⣘⡘⠋⣛⣸⡍⠁⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀
				⠀⠀⠘⢿⣷⣤⣤⣄⣤⣤⣶⣿⣿⣿⡿⢿⣿⣿⣿⣷⣤⣤⣠⣤⣴⣾⡿⠁⠀⠀
		                     ⠉⠛⠿⠿⠿⡿⠿⠿⠛⠉⠀⠀⠉⠛⠿⠿⣿⠿⠿⠿⠛⠉⠀⠀⠀⠀
                                				©copyright by tX-c0re                                                               
\x1b[0m                                                                                                             
\x1b[31m
**********************************************************************************************************                                                                                                                                           
\x1b[1m
\x1b[33m    !!!DISCLAIMER!!!  DISCLAIMER!!!  DISCLAIMER!!!  DISCLAIMER!!!  DISCLAIMER!!!  DISCLAIMER!!!\x1b[0m
				
\x1b[96m\x1b[3m
	Port scan se sběrem bannerů (PORT GRABBING) Vyrobeno pro účely penetračního testování verze (0.9)			
	Program slouží výhradně pro testování sítě nebo adresy ke které máte opravávnění od správce sítě
	nebo jiné pověřené osoby.
					
\x1b[31m		Mějte na paměti že autor nenese žádnou zodpovědnost za způsobené škody!\x1b[0m
    """

    print(logo)

if __name__ == '__main__':
    vytvor_logo()
    

class PortScanner:
    def __init__(self, target_ports=None):
        if target_ports is None:
            self.target_ports = range(1, 1025)  # Výchozí rozsah skenovaných portů (1-1024)
        elif isinstance(target_ports, list):
            self.target_ports = target_ports
        else:
            raise ValueError("Neplatný argument target_ports. Měl by být seznam portů.")

    def scan(self, host, start_port=1, end_port=1024):
        open_ports = []
        total_ports = end_port - start_port + 1
        
        # Vlastní formátovací řetězec pro červený ukazatel pokroku
        custom_bar_format = "{l_bar}%s{bar}%s{r_bar}" % ("\x1b[32m" , "\x1b[3m\x1b[1m")  # Červený bar (ANSI escape kód)
        
        for port in tqdm(range(start_port, end_port + 1), total=total_ports, desc="\x1b[32mSkenování portů\x1b[3m", bar_format=custom_bar_format):
            if self.__scan_port(host, port):
                open_ports.append(port)
        
        # Získání banneru pro otevřené porty
        banners = {}
        for port in open_ports:
            banner = self.__get_banner(host, port)
            if banner:
                banners[port] = banner
        return banners

    def __scan_port(self, host, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)  # Nastavit timeout pro pokus o připojení
                result = sock.connect_ex((host, port))
                return result == 0  # Port je otevřený, pokud vrátí hodnotu 0 (nula)
        except (socket.timeout, ConnectionRefusedError):
            return False
        except Exception as e:
            return False

    def __get_banner(self, host, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)  # Nastavit timeout pro pokus o připojení
                sock.connect((host, port))
                banner = sock.recv(1024)  # Přijměte několik bytů banneru (změňte podle potřeby)
                return banner.decode('utf-8')  # Dekódovat banner na řetězec
        except (socket.timeout, ConnectionRefusedError):
            return None
        except Exception as e:
            return None

def spustit_skenovani():
    host_to_scan = input("\x1b[31mZadejte název hostitele nebo IP adresu ke skenování: \x1b[0m")
    scanner = PortScanner()
    print(f"\x1b[31mProbíhá skenování portů na {host_to_scan}...\x1b[0m")
    banners = scanner.scan(host_to_scan)

    if banners:
        for port, banner in banners.items():
            print(f"Port {port}: {banner}")

        # Uložení výsledků do souboru
        with open("skenovani_vysledek.txt", "w") as file:
            for port, banner in banners.items():
                file.write(f"Port {port}: {banner}\n")

        print("Výsledky byly uloženy do souboru 'skenovani_vysledek.txt'.")
    else:
        print("Nebyly nalezeny žádné otevřené porty s bannerem.")
if __name__ == '__main__':
    spustit_skenovani() 
