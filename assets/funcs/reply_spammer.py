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

banner = f"""
                 
                                \033[31m _____ _____ _____ _____ _____ _____ _____ 
                                |     |   __| __  |     |  |  | __  |   __|
                                | | | |   __|    -|   --|  |  |    -|   __|
                                \033[90m|_|_|_|_____|__|__|_____|_____|__|__|_____|
"""

timestamp = datetime.datetime.now().strftime(f'{c}[{g}%H:%M:%S{c}]{c}')

async def reply_spammer():
    channel_id = input(f"{dark_red_color}                                {timestamp} {c}[{c}{r}{g}?{g}{c}]{c} [Channel ID] {c}>{c} ")
    message_id = input(f"{dark_red_color}                                {timestamp} {c}[{c}{r}{g}?{g}{c}]{c} [Message ID] {c}>{c} ")
    message = input(f"{dark_red_color}                                {timestamp} {c}[{c}{r}{g}?{g}{c}]{c} [Message] {c}>{c} ")
    amount = int(input(f"{dark_red_color}                                {timestamp} {c}[{c}{r}{g}?{g}{c}]{c} [Amount] {c}>{c} "))
    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner)

    with open('assets/input/tokens.txt', 'r') as file:
        tokens = file.read().splitlines()

    async with aiohttp.ClientSession() as session:
        tasks = []
        for token in tokens:
            task = spam_message(token, channel_id, message_id, message, amount, session)
            tasks.append(task)

        await asyncio.gather(*tasks)

async def spam_message(token, channel_id, message_id, message, amount, session):
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    headers = {
        'authorization': token,
        'content-type': 'application/json'
    }
    payload = {
        'content': message,
        'message_reference': {
            'channel_id': channel_id,
            'message_id': message_id
        }
    }
    for _ in range(amount):
        async with session.post(url, headers=headers, json=payload) as response:
            if response.status == 200:
                print(f"                                {timestamp} {c}[{c}{r}{g}#{g}{c}]{c} Message Sent Successfully")
            else:
                print(f"                                {timestamp} {c}[{c}{r}{g}?{g}{c}]{c} Failed Sending Message")
