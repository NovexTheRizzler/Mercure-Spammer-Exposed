from assets import *

r = Fore.RESET
c = Fore.RED
g = Fore.LIGHTBLACK_EX
x = Fore.GREEN

dark_red_color = '\033[31m'
light_green_color = '\033[92m'
grey_color = '\033[90m'
reset_color = '\033[0m'

print("""      
                                \033[31m _____ _____ _____ _____ _____ _____ _____ 
                                |     |   __| __  |     |  |  | __  |   __|
                                | | | |   __|    -|   --|  |  |    -|   __|
                                \033[90m|_|_|_|_____|__|__|_____|_____|__|__|_____|
""")
time.sleep(0.3)

try:
    num = int(input(f"{datetime.datetime.now().strftime(f'                                {c}[{g}%H:%M:%S{c}]')}{r} {c}[?]{r} {c}[How Many Codes?]{c} > {Fore.RESET}").strip().lower())
    os.system('cls'); print (banner)
except ValueError:
    print(f"{c}Invalid input! Please enter a valid number.{r}")
    exit()

output_file = "assets/output/nitro_codes.txt"
valid_codes_file = "assets/output/valid_codes.txt"

with open(output_file, "w", encoding='utf-8') as file:

    start = time.time()

    for _ in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k=16
        ))
        file.write(f"https://discord.gift/{code}\n")

with open(output_file, "r") as file, open(valid_codes_file, "w") as valid_file:
    for line in file:
        nitro = line.strip("\n")

        url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro.split('/')[-1]}?with_application=false&with_subscription_plan=true"

        try:
            r = requests.get(url)
            if r.status_code == 200:
                print(f"                                {x}Valid ~> {nitro} ")
                valid_file.write(f"{nitro}\n")
                break
            else:
                print(f"                                {g}Invalid{g} {c}~> {nitro} ")
        except requests.RequestException as e:
            print(f"                                {c}Error checking code {nitro}: {e}{r}")

time.sleep(0.2)
