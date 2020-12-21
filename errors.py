import discord
from discord.ext import commands
from discord import Intents
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