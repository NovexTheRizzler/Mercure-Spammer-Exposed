from assets import *

r = '\033[90m'
c = Fore.RED
g = Fore.LIGHTBLACK_EX
s = Fore.BLACK
x = Fore.GREEN
k = Fore.YELLOW

dark_red_color = Fore.RED
light_green_color = '\033[92m'
grey_color = '\033[90m'
reset_color = '\033[0m'

RED = Fore.RED
RESET = "\033[0m"

timestamp = datetime.datetime.now().strftime(f'{c}[{g}%H:%M:%S{c}]{c}')

with open("assets/input/tokens.txt", "r") as f:
    tokens = f.read().strip().splitlines()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

print(f"""{Fore.RED}
                              
                                  
                                \033[31m _____ _____ _____ _____ _____ _____ _____ 
                                |     |   __| __  |     |  |  | __  |   __|
                                | | | |   __|    -|   --|  |  |    -|   __|
                                \033[90m|_|_|_|_____|__|__|_____|_____|__|__|_____|                             
""")

print("")

leave_servers = input(f"                                {timestamp} {c}[{c}?{c}]{c} {c}[Leave Servers?{c} {g}(y/n){g} {c}] {c}> {c}").lower() == "y"
delete_friends = input(f"                                {timestamp} {c}[{c}?{c}]{c} {c}[Delete Friends?{c} {g}(y/n){g} {c}] {c}> {c}").lower() == "y"
close_dms = input(f"                                {timestamp} {c}[{c}?{c}]{c} {c}[Close Direct Messages?{c} {g}(y/n){g} {c}] {c}> {c}").lower() == "y"
reset_avatar = input(f"                                {timestamp} {c}[{c}?{c}]{c} {c}[Reset PFP?{c} {g}(y/n){g} {c}] {c}> {c}").lower() == "y"
clean_pronouns = input(f"                                {timestamp} {c}[{c}?{c}]{c} {c}[Reset Pronouns{c} {g}(y/n){g}{c}] {c}> {c}").lower() == "y"
clean_bio = input(f"                                {timestamp} {c}[{c}?{c}]{c} {c}[Reset Bio?{c} {g}(y/n){g}{c}] {c}> {c}").lower() == "y"
clean_status = input(f"                                {timestamp} {c}[{c}?{c}]{c} {c}[Reset Status?{c} {g}(y/n){g}{c}] {c}> {c}").lower() == "y"

for token in tokens:
    headers = {"Authorization": token}
    response = requests.get("https://discord.com/api/v8/users/@me", headers=headers)

    if response.status_code == 200:
        user = response.json()
        print(f"                                {timestamp} > {user['username']}#{user['discriminator']}")

        servers_response = requests.get("https://discord.com/api/v8/users/@me/guilds", headers=headers)
        servers = servers_response.json()

        if leave_servers:
            time.sleep(1)
            for server in servers:
                try:
                    leave_response = requests.delete(f"https://discord.com/api/v8/users/@me/guilds/{server['id']}", headers=headers)
                    if leave_response.status_code == 204:
                        print(f"                                {timestamp} [+] Left server {server['name']}")
                    else:
                        print(f"                                {timestamp} [-] Error leaving server {server['name']}: {leave_response.status_code}")
                except Exception as e:
                    print(f"                                {timestamp} [+] Already left the server, skipping... Error: {str(e)}")
                time.sleep(1)  

        friends_response = requests.get("https://discord.com/api/v8/users/@me/relationships", headers=headers)
        friends = friends_response.json()

        if delete_friends:
            for friend in friends:
                try:
                    delete_response = requests.delete(f"https://discord.com/api/v8/users/@me/relationships/{friend['id']}", headers=headers)
                    if delete_response.status_code == 204:
                        print(f"                                {timestamp} Deleted friend {friend['user']['username']}#{friend['user']['discriminator']}")
                    else:
                        print(f"                                {timestamp} Error deleting friend {friend['user']['username']}#{friend['user']['discriminator']}: {delete_response.status_code}")
                except Exception as e:
                    print(f"                                {timestamp} Already deleted friend, skipping... Error: {str(e)}")

        dm_response = requests.get("https://discord.com/api/v8/users/@me/channels", headers=headers)
        dms = dm_response.json()

        if close_dms:
            time.sleep(1)
            for dm in dms:
                if dm["type"] == 1:  
                    close_response = requests.delete(f"https://discord.com/api/v8/channels/{dm['id']}", headers=headers)
                    if close_response.status_code in [200, 204]:
                        print(f"                                {timestamp} Closed direct message with {dm['recipients'][0]['username']}#{dm['recipients'][0]['discriminator']}")
                    else:
                        print(f"                                {timestamp} Error closing direct message with {dm['recipients'][0]['username']}#{dm['recipients'][0]['discriminator']}: {close_response.status_code}")
                    time.sleep(1)

        if reset_avatar:
            avatar_data = {"avatar": None}
            avatar_response = requests.patch("https://discord.com/api/v8/users/@me", headers=headers, json=avatar_data)
            if avatar_response.status_code == 200:
                print(f"                                {timestamp} Profile picture reset.")
            else:
                print(f"                                {timestamp} Error resetting profile picture or already done: {avatar_response.status_code}")

        if clean_pronouns:
            pronouns_data = {"pronouns": None}
            pronouns_response = requests.patch("https://discord.com/api/v8/users/@me/settings", headers=headers, json=pronouns_data)
            if pronouns_response.status_code == 200:
                print(f"                                {timestamp} Pronouns cleaned.")
            else:
                print(f"                                {timestamp} Error cleaning pronouns or already done: {pronouns_response.status_code}")

        if clean_bio:
            bio_data = {"bio": None}
            bio_response = requests.patch("https://discord.com/api/v8/users/@me", headers=headers, json=bio_data)
            if bio_response.status_code == 200:
                print(f"                                {timestamp} Bio cleaned.")
            else:
                print(f"                                {timestamp} Error cleaning bio or already done: {bio_response.status_code}")

        if clean_status:
            status_data = {"custom_status": None}
            status_response = requests.patch("https://discord.com/api/v8/users/@me/settings", headers=headers, json=status_data)
            if status_response.status_code == 200:
                print(f"                                {timestamp} Status cleaned.")
            else:
                print(f"                                {timestamp} Error cleaning status or already done: {status_response.status_code}")

print(f"                                {timestamp} Done")

exit_choice = input(f"                                {timestamp} {Fore.RED}Do you want to go back to menu ? (y/n): ")
if exit_choice.lower() == 'y':
    clear()
else:
    exit()