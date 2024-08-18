from assets import *

r = Fore.RESET
c = Fore.RED
g = Fore.LIGHTBLACK_EX
s = Fore.BLACK
x = Fore.GREEN
k = Fore.YELLOW

dark_red_color = '\033[31m'
light_green_color = '\033[92m'
grey_color = '\033[90m'
reset_color = '\033[0m'

RED = Fore.LIGHTRED_EX
RESET = "\033[0m"

def get_ip_info(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        print(f"                                discord.gg/mercureraider")
        print(f"                                {g}[{g}{c}Ip{c}{g}] > {ip}")
        print(f"                                {g}[{g}{c}Country{c}{g}] > " + data.get('country', 'N/A'))
        print(f"                                {g}[{g}{c}City{c}{g}] > " + data.get('city', 'N/A'))
        print(f"                                {g}[{g}{c}Region{c}{g}] > " + data.get('regionName', 'N/A'))
        print(f"                                {g}[{g}{c}ISP{c}{g}] > " + data.get('isp', 'N/A'))
    except Exception as e:
        print("Error:", e)