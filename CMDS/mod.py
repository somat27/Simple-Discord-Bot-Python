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

class mod(commands.Cog):
    def _init_(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=200):
        if amount > 200:
            await ctx.send(
                f"{ctx.author.mention} So podes apagar até 200 mensagens!")
            return
        else:
            await ctx.channel.purge(limit=amount)
            await ctx.send(f"Limpaste {amount} mensagens!", delete_after=5)


    @commands.command()
    async def avatar(self, ctx, member: Member = None):
        if not member:
            member = ctx.author
        await ctx.send('Logo de: ' + member.name)
        await ctx.send(member.avatar_url)

def setup(bot):
    bot.add_cog(mod(bot))