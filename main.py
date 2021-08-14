#--- CONFIG ---
token = "YOUR_DISCORD_BOT_TOKEN"
prefix = "YOUR_PREFIX"

#--- DEPENDENCIAS ---
from keep_alive import keep_alive
import discord
from discord.ext import commands
from discord import Member
import requests
import json
import os
import re
from datetime import datetime
import urllib

print("[Ultra's Bot] Carregado todas as dependencias!")

#--- BOT ---

bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help")


@bot.event
async def on_ready():
	print("\n\n[Ultra's Bot] Pronto! Estou a espera de comandos..")
	print(f"[Ultra's Bot] Logado em: {bot.user.name}")
	print(f"[Ultra's Bot] ID: {bot.user.id}\n\n")
	await bot.change_presence(
	    activity=discord.Streaming(name='Biana di Drill by sandrini9k',
	                               url='https://www.twitch.tv/Ultra_Somat27'))


#--- COMANDOS ---

from CMDS import music, info, hacking, mod

cogs = [music, info, hacking, mod]

for i in range(len(cogs)):
	cogs[i].setup(bot)

#--- MANTER O BOT 24/7 ---

keep_alive()
bot.run(token)
