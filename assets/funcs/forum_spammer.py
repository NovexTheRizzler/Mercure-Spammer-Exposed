from assets import *

c = Fore.RED
r = '\033[90m'
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

class Output:
    @staticmethod
    def log(msg, token=None):
        if token:
            print(f"                                {timestamp} {c}{c}[{c}{r}#{r}{c}]{c}{x} [CREATED]")
        else:
            print(f"                                {timestamp} {c}{c}[{c}{r}#{r}{c}]{c}{c} [FAILED CREATING] {msg}")

    @staticmethod
    def set_title(title):
        print(f"                                {timestamp} {c}{title}{c}")

class Client:
    @staticmethod
    def get_session(token):
        session = requests.Session()
        session.headers.update({
            "Authorization": token,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
        })
        return session

def send(guild_id, channel_id, message, title, token):  
    try:
        session = Client.get_session(token)
        session.headers.update({"referer": f"https://discord.com/channels/{guild_id}/{channel_id}"})
        while True:
            try:
                data = {
                    "name": title,
                    "applied_tags": [],
                    "auto_archive_duration": 4320,
                    "message": {
                        "content": message
                    },
                }
                req = session.post(f"https://discord.com/api/v9/channels/{channel_id}/threads?use_nested_fields=true", json=data)
                
                if req.status_code == 201:
                    result = session.post(
                        f"https://discord.com/api/v9/channels/{req.json()['id']}/messages",
                        json={
                            "content": secrets.token_urlsafe(16),
                            "nonce": str(Decimal(time.time() * 1000 - 1420070400000) * 4194304).split(".")[0],
                            "tts": False
                        }
                    )
                    if result.status_code == 200:
                        Output.log("Success", token)
                    elif result.status_code == 429:
                        pass
                    else:
                        Output.log("                                {timestamp} {c}{c}[{c}{r}#{r}{c}]{c}{c} Error Creating Thread", token)
                elif req.status_code == 429:
                    Output.log("                                {timestamp} {k}{k}[{k}{r}#{r}{k}]{k}{k} Rate Limited", token)
                    time.sleep(float(req.json()['retry_after']))
                else:
                    Output.log("                                {timestamp} {c}{c}[{c}{r}#{r}{c}]{c}{c} Error Creating Thread", token)
            except Exception as e:
                Output.log(str(e))
    except Exception as e:
        Output.log(str(e))

def forum_spammer():
    guild_id = input(f"                                {timestamp} {c}[{c}{r}?{r}{c}]{c} {c}[Guild ID] {c}> {c}")
    channel_id = input(f"                                {timestamp} {c}[{c}{r}?{r}{c}]{c} {c}[Channel ID] {c}> {c}")
    title = input(f"                                {timestamp} {c}[{c}{r}?{r}{c}]{c} {c}[Title] {c}> {c}")
    message = input(f"                                {timestamp} {c}[{c}{r}?{r}{c}]{c} {c}[Message] {c}> {c}")
    max_threads = int(input(f"                                {timestamp} {c}[{c}{r}?{r}{c}]{c} {c}[Thread Count] {c}> {c}"))
    os.system('cls'); print (banner) 
  
    with open("assets/input/tokens.txt", "r") as f:
        tokens = [line.strip() for line in f]

    for token in tokens:
        threading.Thread(target=send, args=(guild_id, channel_id, message, title, token)).start()

if __name__ == "__main__":
    forum_spammer()