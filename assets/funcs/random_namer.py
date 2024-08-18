from assets import *

r = '\033[90m'
c = Fore.RED
g = Fore.LIGHTBLACK_EX
s = Fore.BLACK
x = Fore.GREEN
k = Fore.YELLOW

banner = f"""
                 
                                \033[31m _____ _____ _____ _____ _____ _____ _____ 
                                |     |   __| __  |     |  |  | __  |   __|
                                | | | |   __|    -|   --|  |  |    -|   __|
                                \033[90m|_|_|_|_____|__|__|_____|_____|__|__|_____|
"""

timestamp = datetime.datetime.now().strftime(f'{c}[{g}%H:%M:%S{c}]{c}')


def send_request(nicks, guild_id, token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    nick = random.choice(nicks)
    data = {
        'nick': nick
    }
    response = requests.patch(f"https://discord.com/api/v9/guilds/{guild_id}/members/@me", json=data, headers=headers)
    if response.status_code == 200:
        print(f"                                {timestamp} {c}{c}[{c}{r}#{r}{c}]{c}{x} Changed Nickname Successfully")
    else:
        print(f"                                {timestamp} {c}{c}[{c}{r}#{r}{c}]{c}{k} Error")

def server_nicker():
    guild_id = input(f"                                {timestamp} {c}[{c}{r}?{r}{c}]{c} {c}[Guild ID] {c}> {c}")
    nicknames_input = input(f"                                {timestamp} {c}[{c}{r}?{r}{c}]{c} {c}[Nicknames Separated by a | ] {c}> {c}")
    nicknames = [nick.strip() for nick in nicknames_input.split('|')]
    max_threads = int(input(f"                                {timestamp} {c}[{c}{r}?{r}{c}]{c} {c}[Thread Count] {c}> {c}")) 
    os.system('cls'); print (banner)    
    
    with open("assets/input/tokens.txt", "r") as file:
        for line in file:
            token = line.strip()
            thread = Thread(target=send_request, args=(nicknames, guild_id, token))
            thread.start()
            thread.join()