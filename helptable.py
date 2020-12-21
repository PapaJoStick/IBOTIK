import discord
from discord.ext import commands
from discord import Intents

client = commands.Bot(command_prefix = '!', intents = Intents.all()) 

client.remove_command('help')


@client.command(pass_context = True) # pass_context = True - разрешает команде использовать контекст
async def help(ctx):
	'''
	функция для показа доступных реалтзованных команд
	аргумент ctx - контекст
	class discord.Embed - класс discord.py, отвечающий за embed'ы (другой способ красивого вывода текста)
	class discord.Color - стандартная библиотека цветов discord.py
	'''
	emb = discord.Embed(title = 'Реализованные команды', colour = discord.Color.green()) # создание Embed
	emb.add_field(name = '!clear', value = '"!clear n удаляет n" последних сообщений из чата (n = 0 очищает весь чат)', inline = False) # добавление поля, name - подзаголовок,
	emb.add_field(name = '!kick', value = '"!kick @участник причина" кикает члена)', inline = False) # value - содержание поля Embed, inline - будут ли подзаголовок и содержание в одной строке
	emb.add_field(name = '!ban', value = '"!ban @участник причина" банит участника на 5 минут', inline = False) 
	emb.add_field(name = '!roll', value = '"!roll число" роллит число от 0 до указаного (отсутсвие числа роллит от 0 до 100', inline = False) 
	emb.add_field(name = '!rr', value = '"!rr @участник" начинает игру в русскую рулетку с указанным участником на бан на 5 минут', inline = False) 
	emb.add_field(name = '!coin', value = '"!coin @участник" разрешает спор между юзерами монеткой', inline = False) 
	emb.add_field(name = '!play', value = '"!play ссылка" проигрывает музыку с youtube (в разработке, пока приглашает бота в голосовой канал)', inline = False) 
	emb.add_field(name = '!skip', value = '"!skip" пропускает песню в очереди (в разработке, пока не делает ничего)', inline = False) #
	emb.add_field(name = '!stop', value = '"!stop" останавливает воспроизведение музыки (в разработке, пока заставляет бота покинуть голосовой канал', inline = False)
	emb.add_field(name = '!roles', value = '"!roles коды ролей" выдает пользователю выбранные роли (больше информацией по "!roles_help")', inline = False)
	emb.add_field(name = '!roles_help', value = '"!roles_help" помогает выбрать нужные роли', inline = False)
	# emb.add_field(name = '', value = '""', inline = False)
	await ctx.channel.send(embed = emb) # вывод Embed в контекстный канал