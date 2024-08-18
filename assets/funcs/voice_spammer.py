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

def voice_spammer():
    tokenlist = open('assets/input/tokens.txt', 'r').read().splitlines()
    channel = int(input(f"                                {timestamp} {c}[?] [Channel ID{Fore.RED}] {Fore.RED}> {Fore.RED}"))
    server = int(input(f"                                {timestamp} {c}[?] [Sever ID{Fore.RED}] {Fore.RED}> {Fore.RED}"))
    deaf = input(f"                                {timestamp} {c}[?] [Deafen? {g}(y/n) {Fore.RED}] {Fore.RED}> {Fore.RED}")
    deaf = True if deaf.lower() == "y" else False

    mute = input(f"                                {timestamp} {c}[?] [Mute? {g}(y/n) {Fore.RED}] {Fore.RED}> {Fore.RED}")
    mute = True if mute.lower() == "y" else False

    stream = input(f"                                {timestamp} {c}[?] [Stream? {g}(y/n) {Fore.RED}] {Fore.RED}> {Fore.RED}")
    stream = True if stream.lower() == "y" else False

    video = input(f"                                {timestamp} {c}[?] [Video? {g}(y/n) {Fore.RED}] {Fore.RED}> {Fore.RED}")
    video = True if video.lower() == "y" else False

    os.system('cls')
    print(banner)

    executor = ThreadPoolExecutor(max_workers=1000)

    def join_leave(token):
        while True:
            ws = WebSocket()
            ws.connect("wss://gateway.discord.gg/?v=8&encoding=json")
            hello = loads(ws.recv())
            heartbeat_interval = hello['d']['heartbeat_interval']
            ws.send(dumps({"op": 2, "d": {"token": token, "properties": {"$os": "windows", "$browser": "Discord",
                                                                          "$device": "desktop"}}}))
            ws.send(dumps({"op": 4, "d": {"guild_id": server, "channel_id": channel, "self_mute": mute,
                                           "self_deaf": deaf, "self_stream?": stream, "self_video": video}}))
            ws.send(dumps({"op": 18, "d": {"type": "guild", "guild_id": server, "channel_id": channel,
                                            "preferred_region": "singapore"}}))
            ws.send(dumps({"op": 1, "d": None}))
            print(f"                                {timestamp} {c}{x}(+){x} {c}Spammed VC{c}")
            time.sleep(0.5)
            ws.send(dumps({"op": 4, "d": {"guild_id": server, "channel_id": channel, "self_mute": mute,
                                           "self_deaf": deaf, "self_stream?": stream, "self_video": video}}))
            time.sleep(0.5)
            ws.send(dumps({"op": 4, "d": {"guild_id": server, "channel_id": channel, "self_mute": mute,
                                           "self_deaf": deaf, "self_stream?": stream, "self_video": video}}))
            ws.close()

    for token in tokenlist:
        executor.submit(join_leave, token)
