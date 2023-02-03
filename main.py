import discum, json, time, asyncio, colorama
from colorama import Fore, Style; colorama.init(autoreset=True)

with open("data/config.json") as f: config = json.load(f) # load cfg file and store it as config variable to access later

if not config["DISCORD_TOKEN"]: print(f"{Fore.RED}Please fill out the config file with your token"); exit()
if not config["DISCORD_CHANNELS"]: print(f"{Fore.RED}Please fill out the config file with the channels you want to bump in"); exit()
if not config["DISCORD_MESSAGE"]: print(f"{Fore.RED}Please fill out the config file with the message you want to send"); exit()
if not config["DELAY_IN_SECONDS"]: print(f"{Fore.RED}Please fill out the config file with the delay in seconds"); exit()

class bumper: # create a class to store functions and have an initilizer in
    def __init__(self) -> None: # initilizer
        self.bot = discum.Client(token=config["DISCORD_TOKEN"], log=False) # create a client instance and access our config file to get the token
        self.channels = config["DISCORD_CHANNELS"] # store channels to bump in as a variable
    
    async def bump(self): # function to bump the x channels in the channels variable
        while True: # constantly run
            try:
                print(f"{Fore.GREEN}Bumping") # print bumping to the console
                [self.bot.sendMessage(str(channel), config["DISCORD_MESSAGE"]) for channel in self.channels]; time.sleep(config["DELAY_IN_SECONDS"]) # send the message to the channels and wait the delay in seconds
            except Exception as e:
                print(f"{Fore.RED}Error: {Fore.WHITE}{e}") # if there is an error print it to the console
                pass # pass and continue

    def run(self): # function to run the bot
        print(f"{Fore.GREEN}Bumping {Fore.YELLOW}{len(self.channels)}{Fore.GREEN} channels every {Fore.YELLOW}{config['DELAY_IN_SECONDS']}{Fore.GREEN} seconds")
        asyncio.run(self.bump()) # run the bump function
        self.bot.gateway.run(auto_reconnect=True) # run the gateway & auto reconnect if it disconnects

if __name__ == "__main__": # if the file is ran directly
    bot = bumper() # create a instance of the class
    bot.run() # run the bot