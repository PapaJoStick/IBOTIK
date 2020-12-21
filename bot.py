import discord
from discord.ext import commands
from discord import Intents
import random
import time
from kick import kick, kick_error
from roll import roll
from errors import on_command_error
from msuic import play, stop, skip
from coinflip import coin
from rr import rr
from helptable import help
from clear import clear, clear_error
from ban import ban, ban_error, unban, on_member_ban, on_member_unban
from roles_help import roles_help
from roll import roll
from on_member_join import on_member_join
from on_ready import on_ready
from roles import roles

client = commands.Bot(command_prefix = '!', intents = Intents.all()) 

client.remove_command('help')


token = open('token.txt', 'r').readline()
client.run(token)