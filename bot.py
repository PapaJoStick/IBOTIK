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
import rr
import helptable
import clear
import roles_help
import roll
import on_member_join
import on_ready
import roles

client = commands.Bot(command_prefix = '!', intents = Intents.all()) 


token = open('token.txt', 'r').readline()
client.run(token)