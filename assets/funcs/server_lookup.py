import os
import requests
import datetime
from time import sleep
from colorama import Fore, init

def menu():
    print(f"""
                                {Fore.RED}[{Fore.RED}{Fore.LIGHTBLACK_EX}1{Fore.LIGHTBLACK_EX}{Fore.RED}{Fore.LIGHTBLACK_EX}{Fore.RED}]{Fore.RED} {Fore.RED} Server Lookup 
                                {Fore.RED}[{Fore.RED}{Fore.LIGHTBLACK_EX}2{Fore.LIGHTBLACK_EX}{Fore.RED}{Fore.LIGHTBLACK_EX}{Fore.RED}]{Fore.RED} {Fore.RED} Go Back 
""")

def fetch_data():
    menu()

menu()

option = int(input(f"                                {Fore.RED}[{Fore.RED}{Fore.LIGHTBLACK_EX}Input{Fore.LIGHTBLACK_EX}{Fore.RED}{Fore.LIGHTBLACK_EX}{Fore.RED}]{Fore.RED} {Fore.LIGHTBLACK_EX}~> {Fore.RESET}"))

if option == 1:
    os.system('cls'); print (banner)
    sleep(1)

    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Authorization' : input(f"{datetime.datetime.now().strftime(f'                                {Fore.RED}[{Fore.RED}{Fore.LIGHTBLACK_EX}%H:%M:%S{Fore.LIGHTBLACK_EX}{Fore.RED}]')}{Fore.RED} {Fore.RED}[Token]{Fore.RED} {Fore.LIGHTBLACK_EX}[INPUT HIDDEN]{Fore.LIGHTBLACK_EX} {Fore.RED}> {s}")
    }

    guildId = str(input(f"{datetime.datetime.now().strftime(f'                                {Fore.RED}[{Fore.RED}{Fore.LIGHTBLACK_EX}%H:%M:%S{Fore.LIGHTBLACK_EX}{Fore.RED}]')}{Fore.RED} {Fore.RED}[Guild Id]{Fore.RED} {Fore.RED}> {Fore.RESET}"))

    response = requests.get(
        f"https://discord.com/api/guilds/{guildId}",
        headers=headers,
        params={"with_counts": True}
    ).json()

    owner = requests.get(
        f"https://discord.com/api/guilds/{guildId}/members/{response['owner_id']}",
        headers=headers,
        params={"with_counts": True}
    ).json()

    os.system('cls'); print (banner)
    print(f"""
              {Fore.RESET}{Fore.RED}#######{Fore.RED} {Fore.RED}Server{Fore.RED} {Fore.RESET}Information{Fore.RESET} {Fore.RED}#######{Fore.RED}
              {Fore.RESET}[{Fore.RESET}{Fore.RED}Name{Fore.RESET}]      $   {response['name']} 
              {Fore.RESET}[{Fore.RESET}{Fore.RED}ID{Fore.RESET}]        $   {response['id']}
              {Fore.RESET}[{Fore.RESET}{Fore.RED}Owner{Fore.RESET}]     $   {owner['user']['username']}#{owner['user']['discriminator']} 
              {Fore.RESET}[{Fore.RESET}{Fore.RED}Owner ID{Fore.RESET}]  $   {response['owner_id']}
              {Fore.RESET}[{Fore.RESET}{Fore.RED}Members{Fore.RESET}]   $   {response['approximate_member_count']}
              {Fore.RESET}[{Fore.RESET}{Fore.RED}Region{Fore.RESET}]    $   {response['region']}
              {Fore.RESET}[{Fore.RESET}{Fore.RED}Icon URL{Fore.RESET}]  $   https://cdn.discordapp.com/icons/{guildId}/{response['icon']}.webp?size=256
""")
    sleep(6)
    menu()

elif option == 2:
    os.system('cls')
    menu()