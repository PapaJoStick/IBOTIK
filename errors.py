import discord
from discord.ext import commands
from discord import Intents
import random
import time
client = commands.Bot(command_prefix = '!', intents = Intents.all()) # установка префикса для команд и намерений бота (то, с чем он может взаимодействовать), discord.Intents - класс,
																	 # отвечающий за область действия бота (намерения)

client.remove_command('help')

@client.event
async def on_command_error(ctx, error):
	''' 
	функция инициализации обработки ошибок при исполнении команд
	аргумент ctx - контекст, т. е. чат, в котором писалась команда, автор команды и т. д.
	аргумент error - сама ошибка, требующая обработки
	'''
	pass # ничего не делает, т к функция нужна лишь для инициализации ошибки на дальнейшую обработку
	print(f'обрабатываю {error}') # отчет в консоль


@kick.error # обработка ошибки функции кика
async def kick_error(ctx, error):
	'''
	функция обработки ошибки недостатка прав функции кика
	аргумент ctx - контекст 
	error - код ошибки
	class discord.Embed - класс discord.py, отвечающий за embed'ы (другой способ красивого вывода текста)
	class discord.Color - стандартная библиотека цветов discord.py
	class discord.Member - класс discord.py, отвечающий за взаимодействие с участниками сервера и их данными
	'''
	if isinstance(error, commands.MissingPermissions): # проверка наличия ошибки и подохдит ли ошибка под искомую категорию
		author = ctx.message.author # указание автора команды, при исполнении которой произошла ошибка
		emb = discord.Embed(title = f'{author.name}, у вас недостаточно прав', colour = discord.Color.red()) # создание информации о причине ошибки
		await ctx.channel.send(embed = emb) # вывод инфо о проблеме
 

@ban.error # обарботка ошибки функции бана
async def ban_error(ctx, error):
	'''
	функция обработки ошибок недостатка прав функции бана
	аргумент ctx - контекст
	аргумент error - код ошибки
	class discord.Embed - класс discord.py, отвечающий за embed'ы (другой способ красивого вывода текста)
	class discord.Color - стандартная библиотека цветов discord.py
	class discord.Member - класс discord.py, отвечающий за взаимодействие с участниками сервера и их данными
	'''
	if isinstance(error, commands.MissingPermissions): # проверка наличия ошибки и подходит ли ошибка под искомую категорию
		author = ctx.message.author # указание автора команды с ошибкой
		emb = discord.Embed(title = f'{author.name}, у вас недостаточно прав', colour = discord.Color.red()) # создания Embed с инфой о причине ошибки
		await ctx.channel.send(embed = emb) # оправка инфо о причине ошибки


@clear.error # обработка ошибки функции очистки
async def clear_error(ctx, error):
	'''
	функция обработки ошибок недостатка прав функции очистки
	аргумент ctx - контекст
	аргумент error - код ошибки
	class discord.Embed - класс discord.py, отвечающий за embed'ы (другой способ красивого вывода текста)
	class discrod.Color - стандартная библиотека цветов discord.py
	class discord.Member - класс discord.py, отвечающий за взаимодействие с участниками сервера и их данными
	'''
	if isinstance(error, commands.MissingPermissions): # проверка наличия ошибки и подходит ли ошиба под искомую ктегорию
		author = ctx.message.author # указание автора команды с ошибкой
		emb = discord.Embed(title = f'{author.mention}, у вас недостаточно прав', colour = discord.Color.red()) # создание поля Embed дл информирования о причине ошибки 
		await ctx.channel.send(embed = emb) # отправка инфо о причине