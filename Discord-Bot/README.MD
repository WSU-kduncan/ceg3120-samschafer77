Setup
* how to get an API:
    - discord development portal under bot to get the token.
* where to put it to work with the code dependencies (what packages need to be installed to run the code)
    - add DISCORD_TOKEN= {TOKENKEY} to a .env file inside of the Discord-Bot folder. 
    - the package needed to be installed to link the .env to the python script is load_dotenv. The discord package must be installed to connect to the discord api to have the bot up and running.

* Commands
    - python3: This is the python interpreter used for run the python code.
    - python3-pip: this is the python package management system used to install new packages and manage existing ones.
    - pip3 install -U python-dotenv: installs python-dotenv using pip
    - pip3 install discord.py: install the discord package to connect to the discord api.

Usage
* with your changes to the code in place, describe what commands you can type in your Discord server what response this will provide (from your bot)
    - my discord bot outputs text into my discord server using the !ring command, this will output a random lord of the rings quote.
    
Research
* you may have realized that it is lame that it only runs when you run the program. In the real world, things are "always on", not waiting for Bob to turn his PC on and make sure the program is running. Research some possible solutions that would solve this, and discuss why you think it would work.
    - The solution to having a program "always on" is to run the program on a server that is online 24/7 so that the program will be up and running 24/7.