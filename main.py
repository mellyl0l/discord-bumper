import discum, json, time, asyncio, colorama, requests
from colorama import Fore; colorama.init(autoreset=True)

with open("data/config.json") as f: config = json.load(f)
[print(f"{Fore.RED}Please fill out the {Fore.YELLOW}{key}{Fore.RED} value in the config.") for key in config if not config[key]]; exit() if not all(config.values()) else None

# check if this is the latest version
if requests.get(config["URL"]).text != open("main.py").read():
    print(f"{Fore.RED}Please update the script to the latest version: {Fore.YELLOW}")

class bumper:
    def __init__(self) -> None:
        self.bot = discum.Client(token=config["DISCORD_TOKEN"], log=False)
        self.channels = config["DISCORD_CHANNELS"]
    
    async def bump(self):
        while True:
            try:
                print(f"{Fore.GREEN}Bumping")
                [self.bot.sendMessage(str(channel), config["DISCORD_MESSAGE"]) for channel in self.channels]; time.sleep(config["DELAY_IN_SECONDS"])
            except Exception as e:
                print(f"{Fore.RED}Error: {Fore.WHITE}{e}")
                pass

    def run(self):
        print(f"{Fore.GREEN}Bumping {Fore.YELLOW}{len(self.channels)}{Fore.GREEN} channels every {Fore.YELLOW}{config['DELAY_IN_SECONDS']}{Fore.GREEN} seconds")
        asyncio.run(self.bump())
        self.bot.gateway.run(auto_reconnect=True)

if __name__ == "__main__":
    #print(requests.get("https://raw.githubusercontent.com/mellyl0l/discord-bumper/main/main.py").text)
    ...
    #bot = bumper()
    #bot.run()