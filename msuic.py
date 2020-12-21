import discord
from discord.ext import commands
from discord import Intents


@client.command(pass_context = True) # pass_context = True - разрешает команде использовать контекст
async def play(ctx):
	'''
	функция подключения к голосовому каналу, проигрывания мцзыки (музыка еще не реализованна)
	аргумент ctx - контекст
	class discord.client - класс discord.py, представляющий собой клиентское соединение, которое подключается к Discord
	class discord.Embed - класс discord.py, отвечающий за embed'ы (другой способ красивого вывода текста)
	class discord.utils - класс discord.py, содержащий в себе функциональные методы, например - get
	class discord.Color - стандартная библиотека цветов discord.py
	'''
	global voice # указание глобальной переменной voice 
	music_text_ch = client.get_channel(773264803211771985) # указание канала для отправки инфо о музыке
	channel = ctx.message.author.voice.channel # указание канала, в котором сидит желающий послушать музыку
	voice = discord.utils.get(client.voice_clients, guild = ctx.guild) # получение списка голосовых каналов сервера
	if voice and voice.is_connected(): # проверка находится ли бот в каком-то голосовм канале
		await voice.move_to(channel) # переход из канала, к которому подключен бот, к указанному голосовому каналу
	else: # если бот не находится в голосовом канале
		voice = await channel.connect() # присоединение к каналу запросившего музыку
	emb = discord.Embed(title = f'Присоединяюсь к {channel.name}', colour = discord.Color.purple()) # создание Embed о присоединении к каналу, в дальнейшем - инфо о играющей музыке
	await music_text_ch.send(embed = emb) # присоединение к каналу
	print('запуск музыки') # отчет в консоль


@client.command(pass_context = True) # pass_context = True - разрешает команде использовать контекст
async def skip(ctx):
	'''
	функция пропуска текущей песни, переход к следующей
	для реализации необходима реализация очереди прослушивания
	пока не доступна
	аргумент ctx - контекст
	'''
	print("музыка пропущена") # отчет в консоль


@client.command(pass_context = True) # pass_context = True - разрешает команде использовать контекст
async def stop(ctx):
	'''
	функция отключения от голосового канала
	аргумент ctx - контекст
	class discord.client - класс discord.py, представляющий собой клиентское соединение, которое подключается к Discord
	class discord.Embed - класс discord.py, отвечающий за embed'ы (другой способ красивого вывода текста)
	class discord.Color - стандартная библиотека цветов discord.py
	class discord.Member - класс discord.py, отвечающий за взаимодействие с участниками сервера и их данными
	'''
	music_text_ch = client.get_channel(773264803211771985) # указание текстового чата для музыки
	channel = ctx.message.author.voice.channel # указание голосового канала, в котором сидит юзер, отдавший команду
	emb = discord.Embed(title = f'Отключаюсь от {channel.name}', colour = discord.Color.purple()) #создание оповещение в виде Embed об отключении
	await music_text_ch.send(embed = emb) # вывод оповещения об отключении
	await voice.disconnect() # отключение от голосового канала
	print('музыка остановилась') # отчет в консоль


client = commands.Bot(command_prefix = '!', intents = Intents.all()) 

client.remove_command('help')