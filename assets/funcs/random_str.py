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

def send_message(token, channel_id, message, delay):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    while True:
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))  
        payload = {
            "content": f"{message} | {random_string}"  
        }
        url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
        
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            print(f"                                {timestamp} {c}{c}[{c}{r}#{r}{c}]{c}{x} Message Sent Successfully")
        else:
            print(f"                                {timestamp} {c}{c}[{c}{r}#{r}{c}]{c}{c} Failed To Send Message")
        time.sleep(delay)

def random_string_spammer():
    tokens = open("assets/input/tokens.txt", "r", encoding="utf8").read().splitlines()
    message = input(f"                                {timestamp} {c}[{c}{r}?{r}{c}]{c} {c}[Message] {c}> {c}")
    channel_id = input(f"                                {timestamp} {c}[{c}{r}?{r}{c}]{c} {c}[Channel ID] {c}> {c}")
    delay = float(input(f"                                {timestamp} {c}[{c}{r}?{r}{c}]{c} {c}[Delay] {c}> {c}"))
    os.system('cls')
    print (banner)

    threads = []
    for token in tokens:
        thread = threading.Thread(target=send_message, args=(token, channel_id, message, delay))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    basic_spammer()
