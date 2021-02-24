#UPDATING IT REGURARLY

'''
very basic discord bot being developed by me
currently I'm just learning, so it doesn't have 
any purpose, but I'm opened for suggestions!
'''

import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello')

    if message.content.startswith('$info'):
        await message.channel.send('Discord BOT, coded by PADi\n(https://github.com/padi48)')


client.run(os.getenv('TOKEN'))
