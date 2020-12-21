import discord
from discord.ext import commands
from discord import Intents
import random

client = commands.Bot(command_prefix = '!', intents = Intents.all()) 


@client.command(pass_context = True) # pass_context = True - разрешает команде использовать контекст
async def coin(ctx, opponent: discord.Member):
	'''
	функция для разрешение споров между двумя пользователями при помощи подбрасывания монетки
	аргумент ctx - контекст
	аргумент opponent : str - id оппонента
	class discord.Member - класс discord.py, отвечающий за взаимодействие с участниками сервера и их данными
	'''
	author = ctx.message.author # указание автора команды
	results = ['орел', 'решка'] # возможные результаты броска
	author_choice = random.choice(results) # случайный выбор винкондишна автора команды
	await ctx.channel.send(f'Благодаря случаю {author.name} достается {author_choice}...') # оповещение какая сторона монеты является винкондишном автора команды
	result = random.choice(results) # случайный выбор результата броска
	await ctx.channel.send(f'{author.name} и {opponent.name} бросают монетку... Выпадает {result}') # отправка информации о результате броска в канал, где отдали команду
	if result == author_choice: # проверка выиграл ли автор
		await ctx.channel.send(f'Выиграл {author.mention}') # отправка сообщения о победе автора
	else: # если не, тогда выиграл оппонент
		await ctx.channel.send(f'Выиграл {opponent.mention}') # отправка сообщения о победе оппонента
	print(f'подбросилась монетка') # отчет в консоль

