import discum, json, time, asyncio
with open("data/config.json") as f: config = json.load(f) # load cfg file and store it as config variable to access later

class bumper: # create a class to store functions and have an initilizer in
    def __init__(self) -> None: # initilizer
        self.bot = discum.Client(token=config["DISCORD_TOKEN"], log=False) # create a client instance and access our config file to get the token
        self.channels = config["DISCORD_CHANNELS"] # store channels to bump in as a variable
    
    async def bump(self): # function to bump the x channels in the channels variable
        while True: # constantly run
            for channel in self.channels: # iterate over all the channels
                time.sleep(config["DELAY_IN_SECONDS"]) # wait for the bump interval
                self.bot.sendMessage(str(channel), config["DISCORD_MESSAGE"]) # send the bump message

    def run(self): # function to run the bot
        asyncio.run(self.bump()) # run the bump function
        self.bot.gateway.run(auto_reconnect=True) # run the gateway & auto reconnect if it disconnects

if __name__ == "__main__": # if the file is ran directly
    bot = bumper() # create a instance of the class
    bot.run() # run the bot