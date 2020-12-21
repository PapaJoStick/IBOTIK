import discord
import random
client = discord.Client()

class MyClient(discord.Client):
    async def on_ready(self):
        print('Ya prosnylsa {0}!'.format(self.user))

@client.event
async def on_message(message):
    if message.content.startswith('монетка!'):
        rand = random.randint(0,1)

        if(rand == 0):
            await message.channel.send('Орел')

        else:
            await message.channel.send('Не орел')

client.run('')