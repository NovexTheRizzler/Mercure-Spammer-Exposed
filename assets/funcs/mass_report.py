import os
import datetime
import requests
import time
from threading import Thread
from colorama import Fore, init

# Initialize colorama
init()

# Color definitions
r = Fore.RESET
c = Fore.RED
g = Fore.LIGHTBLACK_EX
s = Fore.BLACK
x = Fore.GREEN
a = Fore.YELLOW

dark_red_color = '\033[31m'
light_green_color = '\033[92m'
grey_color = '\033[90m'
reset_color = '\033[0m'

os.system('cls' if os.name == 'nt' else 'clear')
os.system('mode con: cols=115 lines=20')

banner1 = '''     
                                \033[31m _____ _____ _____ _____ _____ _____ _____ 
                                |     |   __| __  |     |  |  | __  |   __|
                                | | | |   __|    -|   --|  |  |    -|   __|
                                \033[90m|_|_|_|_____|__|__|_____|_____|__|__|_____|
        [1] Illegal Content | [2] Harassment | [3] Spam or phishing links | [4] Self Harm | [5] NSFW Content'''

print(banner1)

use_file = input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r} {c}{r}{c}[{c}{r}?{r}{c}]{c}{r} {c}[Use assets/input/tokens.txt ? y/n]{c} > {c}{Fore.RESET}").strip().lower()

if use_file == 'y':
    token_file_path = 'assets/input/tokens.txt'
    try:
        with open(token_file_path, 'r') as file:
            tokens = [line.strip() for line in file if line.strip()]
        if not tokens:
            print(f"{c} > No tokens found in {token_file_path}. Please add tokens to the file.")
            exit()
        else:
            print(f"{x} > {len(tokens)} tokens loaded from {token_file_path}.")
    except FileNotFoundError:
        print(f"{c} > Token file not found at {token_file_path}.")
        exit()
elif use_file == 'n':
    token = input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r} {c}{r}{c}[{c}{r}?{r}{c}]{c}{r} {c}[Token] {g}[INPUT HIDDEN]{g}{c} > {s}")
    tokens = [token]
else:
    print(f"{c} > Invalid input. Please enter 'y' or 'n'.")
    exit()

guild_id1 = input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r} {c}{r}{c}[{c}{r}?{r}{c}]{c}{r} {c}[Server Id]{c} > {c}{Fore.RESET} ")
channel_id1 = input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r} {c}{r}{c}[{c}{r}?{r}{c}]{c}{r} {c}[Channel Id]{c} > {c}{Fore.RESET} ")
message_id1 = input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r} {c}{r}{c}[{c}{r}?{r}{c}]{c}{r} {c}[Message Id]{c} > {c}{Fore.RESET} ")
reason1 = input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r} {c}{r}{c}[{c}{r}?{r}{c}]{c}{r} {c}[Reason]{c} > {c}{Fore.RESET} ")
delay = float(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r} {c}{r}{c}[{c}{r}?{r}{c}]{c}{r} {c}[Delay]{c} > {c}{Fore.RESET} "))

def Main(token, count):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36',
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    payload = {
        'channel_id': channel_id1,
        'guild_id': guild_id1,
        'message_id': message_id1,
        'reason': reason1
    }

    while True:
        response = requests.post('https://discord.com/api/v6/report', headers=headers, json=payload)
        if response.status_code == 201:
            count += 1
            print(f"{x} > Report sent successfully ({count})")
        elif response.status_code == 401:
            print(f"{c} > Unauthorized: Invalid token or token expired")
            return
        else:
            print(f"{c} > Failed to send report: {response.status_code}")
        time.sleep(delay)

threads = []
for token in tokens:
    thread = Thread(target=Main, args=(token, 0))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()