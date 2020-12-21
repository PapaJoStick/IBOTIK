import discord
from discord.ext import commands
from discord import Intents
client = commands.Bot(command_prefix = '!', intents = Intents.all()) # установка префикса для команд и намерений бота (то, с чем он может взаимодействовать), discord.Intents - класс,
																	 # отвечающий за область действия бота (намерения)

client.remove_command('help')

@client.command(pass_context = True) # pass_context = True - разрешает команде использовать контекст
@commands.has_permissions (administrator = True) # разрешает выполнять команду только администраторам
async def kick(ctx, member: discord.Member, reason):
	'''
	функция кика
	аргумент ctx - контекст
	аргумент member : str - учатник, которого надо кикнуть
	аргумент reason : str - причина
	class discord.Embed - класс discord.py, отвечающий за embed'ы (другой способ красивого вывода текста)
	class discord.Member - класс discord.py, отвечающий за взаимодействие с участниками сервера и их данными
	class discord.Color - стандартная библиотека цветов discord.py
	'''
	await ctx.channel.purge(limit = 1)
	emb = discord.Embed(title = f'{member.name} был кикнут за {reason}', colour = discord.Color.red()) #выводит оповещение о кике в чат 
	await ctx.channel.send(embed = emb)
	await member.send(f'Вы были кикнуты за {reason}') #отправляет причину кика на сервере забаненному
	await member.kick(reason = reason) #кикает 
	print(f'{member.name} кикнут')


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