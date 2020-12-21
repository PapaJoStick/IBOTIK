import discord
from discord.ext import commands
from discord import Intents

client = commands.Bot(command_prefix = '!', intents = Intents.all()) 


@client.event # @client.vent - декоратор, указывающий на то, что fun = client.event(fun)
async def on_ready():
	'''
	асинхр функция, запускающаяся, когда запускается бот.
	class disord.client - класс discord.py, представляющий собой клиентское соединение, которое подключается к Discord
	class discord.Game - класс discord.py, частный случай класса Activity, отображающий в статусе "играет в..."
	class discord.Activity - класс discord.py, отвечающий за отображение активности в статусе
	class discord.Embed - класс discord.py, отвечающий за embed'ы (другой способ красивого вывода текста)
	'''
	print('Bot is active') # принты - для вывода информации на консоль
	ch = client.get_channel(771035973990481964) # получение канала, в который потом будет отправленно сообщение
	game = discord.Game('в крутого разраба') # задаем кастомную активность 'играю в ...'
	await client.change_presence(status = discord.Status.idle, activity = game) # выставляем активность, заданную выше, причем отображается, когда бот просто в сети (не стримит, не играет)
	emb = discord.Embed(title = f'Я к Вашим услугам', colour = discord.Color.orange()) # создаем Embed, title - текст заголовка, colour - цвет Embed
	await ch.send(embed = emb) # отправка эмбеда в заранее обозначенный канал