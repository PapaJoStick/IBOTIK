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
@commands.has_permissions (administrator = True) # разрешает выполнять команду только администраторам
async def clear(ctx, amount = 0):
	''' 
	функция для очистки чата
	аргумент ctx - контекст
	аргумент amount : int - количсетво желаемых удаленных сообщений, с последнего отправленного
	class discord.embed - класс discord.py, отвечающий за embed'ы (другой способ красивого вывода текста)
	class discord.Color - стандартная библиотека цветов discord.py
	class discord.Member - класс discord.py, отвечающий за взаимодействие с участниками сервера и их данными
	'''
	author = ctx.message.author # author указывает на автора, в данном случае сообщения
	await ctx.channel.purge(limit = 1) #удаляем команду !clear n
	if amount == 0: #если аргумент не задан - чистим весь канал
		await ctx.channel.purge(limit = 10000000) #непосредственно чистка
		await ctx.channel.send(embed = discord.Embed(description = f'``{author.name}`` очистил весь чат')) #оповещение об очистке
	else:
		await ctx.channel.purge(limit = amount) #непосредственно чистка
		await ctx.channel.send(embed = discord.Embed(description = f'``{author.name}`` очистил {amount} сообщений')) #оповещение об очистке
	print('чат очищен') #отчет в консоль

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

'''инициализация бота'''
token = open('token.txt', 'r').readline() # открытие .txt файла, где лежит токен бота
client.run(token) #инициализация бота