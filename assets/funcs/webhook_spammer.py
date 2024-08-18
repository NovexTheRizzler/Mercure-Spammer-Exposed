from assets import *

def WebhookSpammer(WebHook, Message):
    print("                                ctrl+c if u wanna stop")
    time.sleep(1.5)
    while True:
        response = requests.post(
            WebHook,
            json={"content": Message},
            params={'wait': True}
        )
        try:
            if response.status_code in (200, 204):
                print(f"                                                {Fore.RED}Message sent{Fore.RED}")
            elif response.status_code == 429:
                retry_after = response.json().get('retry_after', 0)
                print(f"                                                 {Fore.RED}Rate limited ({retry_after}ms){Fore.RED}")
                time.sleep(retry_after / 1000)
            else:
                print(f"                                                 {Fore.RED}Error: {response.status_code}{Fore.RESET}")

            time.sleep(0.01)
        except KeyboardInterrupt:
            break

    print(f'                                                              {Fore.RED}Spammed Webhook Successfully!{Fore.RED}')
    input("Enter anything to continue. . . ")
    main()