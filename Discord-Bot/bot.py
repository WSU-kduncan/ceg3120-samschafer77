import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return


    lotr_quotes = [
       'Not all those who wander are lost.',
       'Even the smallest person can change the course of the future',
       'You step into the Road, and if you dont keep your feet, there is no knowing where you might be swept off to.',
        'Its the job thats never started as takes longest to finish',
    ]

    if message.content == '!ring':

        response = random.choice(lotr_quotes)
        await message.channel.send(response)

client.run(TOKEN)