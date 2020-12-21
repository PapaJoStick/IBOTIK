import discord
from discord.ext import commands
from discord import Intents
import random
import time
client = commands.Bot(command_prefix = '!', intents = Intents.all()) # установка префикса для команд и намерений бота (то, с чем он может взаимодействовать), discord.Intents - класс,
																	 # отвечающий за область действия бота (намерения)

client.remove_command('help') # удаление дефолтной команды !help для ее последующей замены,
# class discord.client класс discord.py, представляющий собой клиентское соединение, которое подключается к Discord


@client.command(pass_context = True) # pass_context = True - разрешает команде использовать контекст
async def roles_help(ctx):
	'''
	функция для показа возможных к получению ролей
	аргумент ctx - контекст
	class discord.Embed - класс discord.py, отвечающий за embed'ы (другой способ красивого вывода текста)
	class discord.Color - стандартная библиотека цветов discord.py
	class discord.client - класс discord.py, представляющий собой клиентское соединение, которое подключается к Discord
	'''
	roles_ch = client.get_channel(778260081879416842)
	emb = discord.Embed(title = 'Роли', colour = discord.Color.green()) # создание Embed
	emb.add_field(name = 'WoW', value = '"!roles 1" - для получения роли WoW и доступа к закрытым каналам игры (код - 1)', inline = False)
	emb.add_field(name = 'SC2', value = '"!roles 2" - для получения роли SC2 и доступа к каналам (код - 2)', inline = False)
	emb.add_field(name = 'Python', value = '"!roles 3" - для получения роли Python и доступа к канал для программистов (код - 3)', inline = False)
	emb.add_field(name = 'Java', value = '"!role 4" - для получения роли Java и доступа к каналам (код - 4)', inline = False)
	emb.add_field(name = 'Комбинации ролей', value = 'Например, "!roles 1234" - выдаст все доступные пока что роли', inline = False)
	await roles_ch.send(embed = emb)


'''инициализация бота'''
token = open('token.txt', 'r').readline() # открытие .txt файла, где лежит токен бота
client.run(token) #инициализация бота