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
async def roll(ctx, number = 101):
	'''
	функция ролла (выбора случайног очисла от 0 до указанного, по умолчанию - 100)
	аргумент ctx - контекст
	аргумент number : int - число, до которого выбираются случайные числа
	class discord.Memeber - класс discord.py, отвечающий за взаимодействие с участниками сервера и их данными
	'''
	author = ctx.message.author # указание автора команды
	result = random.choice(range(0,number+1)) # получение случайного числа от 0 до number ввключительно
	await ctx.channel.send(f'{author.name} роллит (0, {number})... Выпадает {result}!') # отправка инфо о полученном числе
	print(f'{author.name} зароллил') # отчет в консоль