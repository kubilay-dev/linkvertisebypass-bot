from cgitb import text
from pydoc import describe
from time import sleep
from turtle import color
from aiohttp import request
import discord
from discord.ext import commands
import datetime
import json
import _json
import requests

# Definiert Cog Klasse.
class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Bypass Command
    @commands.command()
    async def bypass(self, ctx, url):
        message = await ctx.send("bypassing linkvertise link...")
        # Sendet GET Anfrage an die API mit der Linkvertise URL.
        req = requests.get("https://vacant-curtly-composure.herokuapp.com/bypass2?url="+url)
        # Wandelt die Anfrage in ein JSON Format um.
        data = req.json()
        # Wenn Anfrage nicht erfolgreich, dann...
        if data["success"] == False:
            await message.delete()
            await ctx.send("error. link is invalid.")
        # Ansonsten...
        else:
            await message.delete()
            await ctx.send("successfully bypassed link!\n```\n"+data["destination"]+"\n```")
    
    @bypass.error
    async def ban_error(self, ctx, error):
        # Wenn URL Argument fehlt, dann...
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("error. syntax: ?bypass <link>")

# Fügt den Cog hinzu.
def setup(bot):
    bot.add_cog(Commands(bot))