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

async def send_message(token, channel_id, message_content):
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    payload = {
        "content": message_content
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200 or response.status_code == 201:
            message_id = response.json()['id']
            print(f"                                {timestamp} {c}{c}[{c}{r}#{r}{c}]{c}{x} Message Sent Successfully")
            return message_id
        else:
            print(f"                                {timestamp} {c}{c}[{c}{r}#{r}{c}]{c}{c} Failed Sending Message")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error occurred with token ending in {token[-4:]}: {e}")
        return None

async def pin_message(token, channel_id, message_id):
    url = f"https://discord.com/api/v9/channels/{channel_id}/pins/{message_id}"
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }

    try:
        response = requests.put(url, headers=headers)
        if response.status_code == 204:
            print(f"                                {timestamp} {c}{c}[{c}{r}#{r}{c}]{c}{x} Message Pinned")
        else:
            print(f"                                {timestamp} {c}{c}[{c}{r}#{r}{c}]{c}{c} Pin Failed")
    except requests.exceptions.RequestException as e:
        print(f"                                {timestamp} {c}{c}[{c}{r}#{r}{c}]{c}{c} Error")

async def send_and_pin_message(token, channel_id, message_content):
    message_id = await send_message(token, channel_id, message_content)
    if message_id:
        await pin_message(token, channel_id, message_id)

async def message_spammer():
    with open("assets/input/tokens.txt", "r") as file:
        tokens = [line.strip() for line in file]

    channel_id = input(f"                                {timestamp} {c}[{c}{r}?{r}{c}]{c} {c}[Channel ID] {c}> {c}")
    base_message_content = input(f"                                {timestamp} {c}[{c}{r}?{r}{c}]{c} {c}[Message] {c}> {c}")
    os.system('cls'); print (banner)

    with ThreadPoolExecutor(max_workers=10) as executor:
        while True:
            futures = []
            for token in tokens:
                message_content = f"{base_message_content} - {random.randint(1000, 9999)}"
                futures.append(executor.submit(asyncio.run, send_and_pin_message(token, channel_id, message_content)))
            for future in futures:
                await asyncio.sleep(0.5)