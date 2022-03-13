# Importiert Librarys damit der Bot funktioniert.
from cgitb import text
from tkinter import E
from turtle import color, title
import discord
from discord.ext import commands
import json
import asyncio
import datetime

# Importiert die Config.json damit der Token und der Prefix abgelesen werden kann.
with open('config/conf.json', 'r') as cjson:
    config = json.load(cjson)

## Aktiviert die Intents und definiert den Bot als "client".
intents = discord.Intents.all()
intents.reactions = True
client = commands.Bot(command_prefix=config["prefix"], intents=intents)
client.remove_command("help")

# Alle Cogs die existieren und geladen werden sollen.
extensions = ['cogs.commands']

# Cogs werden geladen.
for extension in extensions:
    client.load_extension(extension)

# Wenn der Bot on ist, bla bla bla.
@client.event
async def on_ready():
    print("linkvertise bot started at " + str(datetime.datetime.now()))
    await client.change_presence(activity=discord.Game(name="linkvertise yes."))

# Help Command.
@client.command()
async def help(ctx):
    embed = discord.Embed(title="Alle Commands",
    description="hier ist noch nichts :<",
    color=0x9E34EB)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=str(ctx.author))
    await ctx.send(embed=embed)

# Starte Bot.
client.run(config["token"])