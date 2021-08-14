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

launch_time = datetime.utcnow()

class info(commands.Cog):
    def _init_(self, bot):
        self.bot = bot

    @commands.command()
    async def uptime(self, ctx):
        delta_uptime = datetime.utcnow() - launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        await ctx.send(
            f"Estou online à {days} dias, {hours} horas, {minutes} minutos e {seconds} segundos!"
        )
        print(f"Comando [UPTIME] Executado no Canal: {ctx.channel}")
    
    @commands.command()
    async def btc(self, ctx):
        url = f"https://api.coindesk.com/v1/bpi/currentprice.json"
        r = requests.get(url)
        re = r.json()
        price_usd = re["bpi"]["USD"]["rate"]
        price_eur = re["bpi"]["EUR"]["rate"]
        disclaimer = re["disclaimer"]
        update = re["time"]["updated"]
        embed = discord.Embed(title=f"Preço da **Bitcoin**",
                            description=disclaimer,
                            color=0xffff00)
        embed.add_field(name="USD", value=f"** {price_usd} $**")
        embed.add_field(name="EUR", value=f"** {price_eur} €**")
        embed.set_footer(text=f"Data: {update}")
        await ctx.send(embed=embed)
        print(f"Comando [BTC] Executado no Canal: {ctx.channel}")

    @commands.command()
    async def user_info(self, ctx, member: Member = None):
        member = ctx.author if not member else member
        roles = [role for role in member.roles]
        embed = discord.Embed(colour=member.colour,
                            timestamp=ctx.message.created_at)
        embed.set_author(name=f"Imformaçao Do Usuario - {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Comando por {ctx.author}",
                        icon_url=ctx.author.avatar_url)
        embed.add_field(name="ID: ", value=member.id)
        embed.add_field(name="Nome no servidor: ", value=member.display_name)
        embed.add_field(name="Conta Criada a: ",
                        value=member.created_at.strftime("%a, %#d/%m/%Y, %X UTC"))
        embed.add_field(name="Entrou no Servidor a: ",
                        value=member.joined_at.strftime("%a, %#d/%m/%Y, %X UTC"))
        embed.add_field(name=f"Cargos: ({len(roles)})",
                        value=" ".join({role.mention
                                        for role in roles}))
        embed.add_field(name="Cargo mais Alto:", value=member.top_role.mention)
        embed.add_field(name="Bot?", value=member.bot)
        await ctx.send(embed=embed)
        print(f"Comando [USER_INFO] Executado no Canal: {ctx.channel}")


def setup(bot):
    bot.add_cog(info(bot))