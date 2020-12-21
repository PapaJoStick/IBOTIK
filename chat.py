import discord
client = discord.Client()

@client.event
async def on_ready():
    print('Ya prosnylsa {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return 
        
    if message.content.startswith('Привет'):
        await message.channel.send('ну здарова') 

client.run('')