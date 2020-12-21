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
async def roles(ctx, roles_wanted):
	'''
	функция для выдачи ролей по требованию, при получении роли открываются скрытые текстовые и голосовые команды, доступные данной роли
	аргумент ctx - контекст
	аргумент roles_wanted : str - желаемые роли (их численные коды)
	class discord.Member - класс discord.py, отвечающий за взаимодействие с участниками сервера и их данными
	class discord.utils - класс discord.py, содержащий в себе функциональные методы, например - get
	class discord.Guild - класс discord.py, отвечающий за взаимодействие бота с информацией о сервере
	'''
	author = ctx.message.author # указание id автора
	newbee = discord.utils.get(author.guild.roles, id = 778259400644231168) # получение роли Новичок с сервера
	if newbee in author.roles: # если у автора команды есть эта роль
		await author.remove_roles(newbee) # убираем роль Новичок
	roles_wanted = list(roles_wanted) # форматируем строку с цифрами в список
	roles_possible = { # создаем словарь соответствия ролей и их кодов
		'1':['WoW', 790186717616930836], # код 1 - игра World of Warcraft, id роли
		'2':['SC2', 790186752266600499], # код 2 - игра SC2, id роли
		'3':['Python', 790360677021515797], # код 3 - язык программирования Python, id роли
		'4':['Java', 790360742913245186] # код 4 - язык программирования Java, id роли
	}
	for role in roles_wanted: # пробегаем по кодам желаемых ролей
		if role in roles_possible: # если код роли есть в словаре
			r = discord.utils.get(author.guild.roles, id = roles_possible[role][1]) # получаем роль ко коду из словаря соотвествий
			await author.add_roles(r) #присваеваем роль
	await ctx.channel.purge(limit = 1) # удаление команды из чата после выдачи


'''инициализация бота'''
token = open('token.txt', 'r').readline() # открытие .txt файла, где лежит токен бота
client.run(token) #инициализация бота