import discord
from discord.ext import commands
from discord import Intents
import random
import time
import kick
import errors
import ban
import msuic
import coinflip
import RussianRoulette
import help

client = commands.Bot(command_prefix = '!', intents = Intents.all()) 


token = open('token.txt', 'r').readline()
client.run(token)