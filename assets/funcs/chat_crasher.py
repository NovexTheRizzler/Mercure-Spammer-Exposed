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

banner = f"""
                                \033[31m _____ _____ _____ _____ _____ _____ _____ 
                                |     |   __| __  |     |  |  | __  |   __|
                                | | | |   __|    -|   --|  |  |    -|   __|
                                \033[90m|_|_|_|_____|__|__|_____|_____|__|__|_____|
"""

def read_tokens_from_file(filename):
    with open(filename, "r") as file:
        tokens = file.read().splitlines()
    return tokens

async def emojisend_message(token, channel_id):
    async with aiohttp.ClientSession() as session:
        emojis = "🥵🤮😹🤭😫😋😏🤡💀☠👻😱😷😛😡😈🙈😜🤗😂🤨😔😯🤯🤤🤤🤢🤫👿🧐👽👾🤓😇🤧🤭☠😹😼😻😽🙀😿😺💩👺👹👿😈🤥🤡👺😺😾😿😿😾🐱‍👤🐻🦊🙉🐱‍🚀🐱‍🐉🐱‍🏍🐵🦝🐨🐨🐾🐽🦍🦧🦮🐕‍🦺🐩🐲🐔🦄🦓🐗🐸🐸🐇🦎🐊🐢🐋🐳🦅🦃🐡🦅🦜🦜🦀🧞‍♂️🦴⛷🤼‍♂️👥👀👁🐢💙✝☪💤"
        while True:
            num_emojis = min(150, len(emojis))  
            random_emojis = ''.join(random.sample(emojis, num_emojis))
            
            payload = {
                'content': random_emojis,
                'tts': False
            }
            async with session.post(f"https://canary.discordapp.com/api/v6/channels/{channel_id}/messages", headers={'Authorization': token}, json=payload) as response:
                if response.status == 429:
                    try:
                        ratelimit = await response.json()
                        print(f'                                {timestamp} {k}{k}[{k}{r}#{r}{c}]{k}{k} Ratelimited')
                    except Exception as e:
                        print(f"                                {timestamp} {c}{c}[{c}{r}#{r}{c}]{k}{c} Error")
                elif response.status == 200:
                    print(f'                                {timestamp} {c}{c}[{c}{r}#{r}{c}]{c}{x} Message Sent Successfully')
                else:
                    print(f'                                {timestamp} {c}{c}[{c}{r}#{r}{c}]{c}{k} Error')
                
                await asyncio.sleep(0.5)  

async def chat_crasher():
    tokens = read_tokens_from_file("assets/input/tokens.txt")
    channel_id = input(f"{dark_red_color}                                {timestamp} {c}[{r}?{c}]{c} [Channel ID]{c} {c}>{c} {c}")
    os.system('cls' if os.name == 'nt' else 'clear')  
    print(banner)
    tasks = [emojisend_message(token, channel_id) for token in tokens]
    await asyncio.gather(*tasks)
