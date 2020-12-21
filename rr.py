import discord
from discord.ext import commands
from discord import Intents
import random
import time


client = commands.Bot(command_prefix = '!', intents = Intents.all()) 

client.remove_command('help')


@client.command(pass_context = True) # pass_context = True - разрешает команде использовать контекст
async def rr(ctx, opponent: discord.Member):
	'''
	функция игры в русскую рулетку, на кону - смена ника на Лузер ;)
	аргумент ctx - контекст
	аргумент opponent - оппонент участника, отдавшего командку
	class discord.Member - класс discord.py, отвечающий за взаимодействие с участниками сервера и их данными 
	class discord.Embed - класс discord.py, отвечающий за embed'ы (другой способ красивого вывода текста)
	class discord.Color - стандартная библиотека цветов discord.py
	'''
	author = ctx.message.author # указание автора команды
	await ctx.channel.send(f'Дамы и господа, {author.name} предлагает {opponent.mention} сыграть в русскую рулетку в русскую рулетку.') # оповещение о начале игры в канал контекста
	parts = [author, opponent] # список участников для дальнейшего выбора того, кто начинает
	first = random.choice(parts) # слчуайный выбор начинающего
	if first == author: # если начинает автор
		second = opponent # то второй - оппонент
	else: # если начинает оппонент
		second = author # то второй - автор
	await ctx.channel.send(f'Случай решил, что первым стреляет {first.name}') # опопвещение об очередности стрельбы
	len_seq = 0 # количсетво выстрелов, в дальнейшем для красивого оформления
	drum = [0]*6 # у нашего револьвера 6-ти зарядный барабан
	drum[random.randint(0,5)] = [1] # заряжаем один патрон в барабан (меняем один 0 на 1)
	for i in range(len(drum)): # запускаем цикл стрельбы
		if i % 2 == 0: # если очередь стрелять first
			await ctx.channel.send(f'{first.name} медленно нажимает на курок...') # оповещение о подготовке к первому выстрелу
			time.sleep(1) # задержка для создания интриги
			if drum[i] == 0: # если пули в яйчеке барабана не оказалост
				await ctx.channel.purge(limit = 1) # очищаем уведомление о подготовке
				await ctx.channel.send('Осечка') # выводим инфо об осечке
				len_seq += 1 # добавляем к количсетву спусков крючка 1
			else: # если пуля была
				await ctx.channel.purge(limit = 1) # очищение инфо о подготовке
				await ctx.channel.send(f'{first.name} становится Лузером') # вывод оповещения о проигрыше первого игрока
				await first.edit(nick = 'Лузер') # изменение никнейма первого игрока
				len_seq += 1 # добавление количества спусков
				break # выход из цикла стрельбы
		else: # если очередь стрелять второго игрока
			await ctx.channel.send(f'{second.name} потихоньку давит на спусковой крючок...') # оповещение о подготовке
			time.sleep(1) # задержка для интриги
			if drum[i] == 0: # если пули нет
				await ctx.channel.purge(limit = 1) # удаление инфо о подготовке
				await ctx.channel.send('Осечка') # отправка инфо об осечке
				len_seq += 1 # добавление количства спусков
			else: # если пуля была
				await ctx.channel.purge(limit = 1) # удаление инфо о подготовке
				await ctx.channel.send(f'{second.name} становится Лузером') # вывод инфо о проигравшем
				await second.edit(nick = 'Лузер') # изменение никнейма
				len_seq += 1 # прибавление кол-ва спусков
				break # выход из цикла
	print(f'сыграли в РР') # отчет в консоль
    


client = commands.Bot(command_prefix = '!', intents = Intents.all()) 

client.remove_command('help')