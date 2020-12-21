import discord
from discord.ext import commands
from discord import Intents
import random
import time
client = commands.Bot(command_prefix = '!', intents = Intents.all()) # установка префикса для команд и намерений бота (то, с чем он может взаимодействовать), discord.Intents - класс,
																	 # отвечающий за область действия бота (намерения)

client.remove_command('help') # удаление дефолтной команды !help для ее последующей замены,
# class discord.client класс discord.py, представляющий собой клиентское соединение, которое подключается к Discord


@client.event
async def on_member_join(member):
	'''
	асинхр функция, запускающаяся, когда кто-то заходит на сервер. Выдает новопришедшим роль Newbee
	аргумент member : str - id участника, зашедшего на сервер
	class discord.utils - класс discord.py, содержащий в себе функциональные методы, например - get
	class discord.Member - класс discord.py, отвечающий за взаимодействие с участниками сервера и их данными
	class discord.Guild - класс discord.py, отвечающий за взаимодействие бота с информацией о сервере
	'''
	role = discord.utils.get(member.guild.roles, id = 778259400644231168) # получаем id роли Newbee
	await member.add_roles(role) #выдача роли 
	print(f'{member.name} зашел на сервер') # отчет в консоль


'''инициализация бота'''
token = open('token.txt', 'r').readline() # открытие .txt файла, где лежит токен бота
client.run(token) #инициализация бота