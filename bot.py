import discord
from discord.ext import commands
from discord import Intents
import random
import time
import kick
import errors
import ban
import msuic


client = commands.Bot(command_prefix = '!', intents = Intents.all()) 

client.remove_command('help')


token = open('token.txt', 'r').readline()
client.run(token)