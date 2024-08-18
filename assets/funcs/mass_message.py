from assets import *

r = Fore.RESET
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

banner = f"""
                 
                                \033[31m _____ _____ _____ _____ _____ _____ _____ 
                                |     |   __| __  |     |  |  | __  |   __|
                                | | | |   __|    -|   --|  |  |    -|   __|
                                \033[90m|_|_|_|_____|__|__|_____|_____|__|__|_____|
"""

timestamp = datetime.datetime.now().strftime(f'{c}[{g}%H:%M:%S{c}]{c}')

async def send_message_to_channel(session, token, guild_id, channel_id, message):
    url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    data = {
        'content': message
    }
    async with session.post(url, headers=headers, json=data) as response:
        if response.status == 200:
            print(f"                                {Fore.RED}Message sent to channel {channel_id} in guild {guild_id}.{Fore.RESET}")

async def send_messages_to_channels(token, message):
    url = 'https://discord.com/api/v9/users/@me/guilds'
    headers = {
        'Authorization': token
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status != 200:
                print(f"                               {timestamp} {Fore.RED}Failed to fetch guilds. Make sure the token is correct.{Fore.RESET}")
                return
            guilds = await response.json()
            tasks = []
            for guild in guilds:
                guild_id = guild['id']
                async with session.get(f'https://discord.com/api/v9/guilds/{guild_id}/channels', headers=headers) as channels_response:
                    if channels_response.status != 200:
                        continue
                    channels = await channels_response.json()
                    for channel in channels:
                        channel_id = channel['id']
                        channel_type = channel['type']
                        if channel_type != 0: 
                            continue
                        task = send_message_to_channel(session, token, guild_id, channel_id, message)
                        tasks.append(task)
                        if len(tasks) >= 15:
                            await asyncio.gather(*tasks)
                            tasks = []
            if tasks:  
                await asyncio.gather(*tasks)

def read_tokens_from_file():
    try:
        with open('assets/input/tokens.txt', 'r') as file:
            tokens = file.read().strip().splitlines()
            return tokens
    except FileNotFoundError:
        print(f"                                {timestamp} {Fore.RED}tokens.txt file not found.{Fore.RESET}")
        return []

def meessage_everywhere_spam():
    use_tokens_from_file = input(f"                                {timestamp} {Fore.RED}Do you want to use tokens from assets/input/tokens.txt? (y/n) > {Fore.RESET}").strip().lower()
    
    if use_tokens_from_file == 'y':
        os.system('cls'); print (banner)
        tokens = read_tokens_from_file()
        if not tokens:
            print(f"                                {Fore.RED}No tokens found in tokens.txt. Exiting.{Fore.RESET}")
            return
        message = input(f"                                {timestamp} {Fore.RED}[Message] > {Fore.RESET}")
        for token in tokens:
            asyncio.run(send_messages_to_channels(token, message))
    else:
        os.system('cls'); print (banner)
        token = input(f"                                {timestamp} {c}[{c}{r}?{r}{c}]{c} {Fore.RED}[Token] > {Fore.RESET}")
        message = input(f"                                {timestamp} {c}[{c}{r}?{r}{c}]{c} {Fore.RED}[Message] > {Fore.RESET}")
        asyncio.run(send_messages_to_channels(token, message))

    input(f"                                {timestamp} {Fore.RED}Press Enter To continue...{Fore.RESET}")
    main()