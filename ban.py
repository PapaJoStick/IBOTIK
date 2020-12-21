import discord
from discord.ext import commands
from discord import Intents
import random
import time

client = commands.Bot(command_prefix = '!', intents = Intents.all()) 

client.remove_command('help')

@client.command(pass_context = True) # pass_context = True - разрешает команде использовать контекст
@commands.has_permissions(administrator = True) # разрешает выполнять команду только администраторам
async def ban(ctx, member: discord.Member, reason):
	'''
	функция, предназначенная для бана участников
	аргумент ctx - контекст
	аргумент member : str - участник, которого надо забанить
	аргемент reason : str - причина бана
	class discord.embed - класс discord.py, отвечающий за embed'ы (другой способ красивого вывода текста)
	class discord.Color - стандартная библиотека цветов discord.py
	class discord.member - класс discord.py, отвечающий за взаимодействие с участниками сервера и их данными
	метод purge - очистка
	метод send - отправка
	метод ban - бан
	'''
	await ctx.channel.purge(limit = 1) # ctx.channel - канал, в котором отдана команда, тут удаляется сточка с командой ban
	emb = discord.Embed(title = f'{member.name} был исключен за {reason}', colour = discord.Color.red()) # создание Embed, title - текст в Embed, color - цвет Embed
	await ctx.channel.send(embed = emb) # отправка Embed в канал, в котором была задана команда (контекстный)
	await member.send(f'Вы были забанены за {reason}.') # отправка оповещения забаненному в ЛС
	await member.ban(reason = reason, delete_message_days = 7) # бан, reason - причина бана, delete_message_days - удаляет все сообщения забаненного пользователя (1-7)
	print(f'{member.name} забанен') # отчет в консоль


@client.command(pass_context = True) # pass_context = True - разрешает команде использовать контекст
@commands.has_permissions(administrator = True) #
async def unban(ctx): 
	'''
	функция разбана, для реализации требуется организовать стабильный бан-лист
	аргумент ctx - контекст
	'''
	print(f' разбанен') #отчет в консоль


@client.event
async def on_member_ban():
	'''
	функция, активирующаяся при бане
	в разработке, планируется добавить бан-лист до вывода бота на хостинг и реализация фич, связанных с бан-листом
	'''
	print(f'кого-то забанили') # отчет в консоль


@client.event
async def on_member_unban():
	'''
	функция, активирующаяся при разбане
	как и on_member_ban, пока в разработке
	'''
	print(f'кого-то разбанили') # отчет в консоль


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