import discord
from discord.ext import commands
from discord import Intents
import random
import time
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