#--- CONFIG ---
token = "YOUR_DISCORD_BOT_TOKEN"
prefix = "YOUR_PREFIX"

#--- BOT ---
import keep_alive
import discord
from discord.ext import commands
from discord import Member
import requests
import json
import os
import re


print("[Ultra's Bot] Carregado todas as dependencias!")

bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help")

@bot.event
async def on_ready():
    print("\n\n[Ultra's Bot] Pronto! Estou a espera de comandos..")
    print(f"[Ultra's Bot] Logado em: {bot.user.name}")
    print(f"[Ultra's Bot] ID: {bot.user.id}\n\n")
    await bot.change_presence(
        activity=discord.Streaming(name='Biana di Drill by sandrini9k', url='https://www.twitch.tv/Ultra_Somat27'))

#--- COMANDOS ---

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=200):
    if amount > 200:
        await ctx.send(
            f"{ctx.author.mention} So podes apagar até 200 mensagens!")
        return
    else:
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"Limpaste {amount} mensagens!", delete_after=5)

@bot.command()
async def avatar(ctx, member: Member = None):
    if not member:
        member = ctx.author
    await ctx.send('Logo de: ' + member.name)
    await ctx.send(member.avatar_url)

@bot.command()
async def btc(ctx):
        url = f"https://api.coindesk.com/v1/bpi/currentprice.json"
        r = requests.get(url)
        re = r.json()
        price_usd = re["bpi"]["USD"]["rate"]
        price_eur = re["bpi"]["EUR"]["rate"]
        disclaimer = re["disclaimer"]
        update = re["time"]["updated"]
        embed = discord.Embed(title=f"Preço da **Bitcoin**", description=disclaimer, color=0xffff00)
        embed.add_field(name="USD", value=f"** {price_usd} $**")
        embed.add_field(name="EUR", value=f"** {price_eur} €**")
        embed.set_footer(text=f"Data: {update}")
        await ctx.send(embed=embed)

@bot.command()
async def ip(ctx, arg):
    res = requests.get(f"https://ipinfo.io/{arg}")
    data = res.json()
    pretty_data = json.dumps(data, indent=4)
    await ctx.send(f"```json\n{pretty_data}\n```")

#--- MANTER O BOT 24/7 ---

keep_alive.keep_alive()
bot.run(token)
