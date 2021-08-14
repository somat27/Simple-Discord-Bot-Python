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
import time

class hacking(commands.Cog):
    def _init_(self, bot):
        self.bot = bot

    @commands.command()
    async def ip(self, ctx, arg):
        res = requests.get(f"https://ipinfo.io/{arg}")
        data = res.json()
        pretty_data = json.dumps(data, indent=4)
        await ctx.send(f"```json\n{pretty_data}\n```")


    @commands.command()
    async def ping(self, ctx):
        before = time.monotonic()
        message = await ctx.send("Pong!")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"Pong!  `{int(ping)} ms`")

def setup(bot):
    bot.add_cog(hacking(bot))