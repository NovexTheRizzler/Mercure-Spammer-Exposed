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

def delete(webhook):
    try:
        requests.delete(webhook)
        check = requests.get(webhook)
        if check.status_code == 404:
            print(f"{datetime.datetime.now().strftime(f'                      {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r}  {c}{x}({x}+{x}){x}  {x}[SUCCESS]{x}   {g}~>   {x}Successfully Deleted Webhook | [404]")
            time.sleep(2)
            main()
        elif check.status_code == 200:
            print(f"{datetime.datetime.now().strftime(f'                      {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r}  {c}{c}({c}+{c}){c}  {c}[FAILED]{c}   {g}~>   {x}Failed to delete webhook | [200]")
            time.sleep(2)
            main()
        else:
            print(f"{datetime.datetime.now().strftime(f'                      {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r}  {c}{x}({x}+{x}){x}  {x}[ERROR]{x}   {g}~>   {x}Unexpected status code: {check.status_code}")
            time.sleep(2)
            main()
    except requests.RequestException as e:
        print(f"{datetime.datetime.now().strftime(f'                      {c}[{c}{g}%H:%M:%S{g}{c}]{c}')}{r}  {c}{x}({x}+{x}){x}  {x}[EXCEPTION]{x}   {g}~>   {x}Exception occurred: {e}")
        time.sleep(2)
        main()