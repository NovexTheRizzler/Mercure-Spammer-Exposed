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

banner = f"""
                 
                                \033[31m _____ _____ _____ _____ _____ _____ _____ 
                                |     |   __| __  |     |  |  | __  |   __|
                                | | | |   __|    -|   --|  |  |    -|   __|
                                \033[90m|_|_|_|_____|__|__|_____|_____|__|__|_____|
"""

timestamp = datetime.datetime.now().strftime(f'{c}[{g}%H:%M:%S{c}]{c}')

class TokenManager:
    @staticmethod
    def get_tokens():
        with open("assets/input/tokens.txt", "r") as file:
            return [token.strip() for token in file.readlines()]

class Client:
    @staticmethod
    def get_session(token):
        session = requests.Session()
        session.headers.update({'authorization': token})
        return session

class Output:

    @staticmethod
    def log(message, token):
        print(f"                                {timestamp} {c}(x) Spammed Sound")

    @staticmethod
    def error_logger(token, response_text, status_code):
        print(f"                                {timestamp} {c}(x) ERROR {g}[{g}{c}{status_code}{c}{g}]{g}")

def send(channel_id: str, sounds: list[dict[str, typing.Union[str, int]]], tokens: list[str]):
    while True:
        for token in tokens:
            session = Client.get_session(token)
            sound = random.choice(sounds)
            data = {
                "sound_id": sound.get("sound_id"),
                "emoji_id": None,
                "emoji_name": sound.get("emoji_name"),
                "override_path": sound.get("override_path")
            }
            result = session.post(f"https://discord.com/api/v9/channels/{channel_id}/voice-channel-effects", json=data)
            if result.status_code == 204:
                Output.log("Success", token)
            elif result.status_code == 429:
                pass
            else:
                Output.error_logger(token, result.text, result.status_code)

def soundboard_spammer():
    channel_id = input(f"{dark_red_color}                                {timestamp} {c}[{r}?{c}]{c} [Channel ID]{c} >{c} {c}")
    max_threads = int(input(f"{dark_red_color}                                {timestamp} {c}[{r}?{c}]{c} [Thread Count]{c} >{c} {c}"))
    os.system('cls'); print (banner)
    
    tokens = TokenManager.get_tokens()
    session = Client.get_session(tokens[0])  
    headers = session.headers
    sounds = requests.get("https://discord.com/api/v9/soundboard-default-sounds", headers=headers).json()
    
    send(channel_id, sounds, tokens)