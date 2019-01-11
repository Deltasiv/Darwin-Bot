# import standard libraries
from discord.ext import commands
import discord
import asyncio
import sqlite3
import time
import os, sys

# token key for logging the bot
token = 'token here'
userid = 'user id here'

# creates alias instance of the sub-class discord.Bot()
client = commands.Bot(command_prefix='$', pm_help=True)

# connects to virus.db
conn = sqlite3.connect('resources/virus.db')
cur = conn.cursor()

# when bot iniates
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    # displays Python and Discord.py version
    print(f'Using discord.py {discord.__version__} and Python {sys.version}')
    game = discord.Game(f"""Use $help for help commands,
                        Discord.py version: {discord.__version__}""") # message to display when change status
    await client.change_presence(status=discord.Status.online, activity=game) # changes Bot() status

# Bot() commands

# pings bot for response time
@client.command()
async def ping(ctx):
    start = time.process_time()
    ping = await ctx.channel.send(':ping_pong: Ping!')
    end = time.process_time()
    # calculate delay
    await ping.edit(content=f':ping_pong: Pong! {format(end - start, "5f")}/ms')

# purge amount of messages appended to list
@client.command(pass_context = True)
async def purge(ctx, msgs):
    mgs = []
    number = int(msgs)
    try:
        async for x in ctx.message.channel.history(limit = number):
            mgs.append(x)
        await ctx.message.channel.delete_messages(mgs)
    except ValueError as e:
        await ctx.message.channel.send(f'Due to error: {e}, bot won\'t execute command!')
        print(f'Err: {e}, wrong value!')
        raise SystemExit
    finally:
        await ctx.message.channel.send(f':boom: Deleted {number} messages!', delete_after = 2.0)

# execute logout() function if message.author == Hydra's ID
@client.command()
async def logout(ctx):
    # check if message.author.id is equal to entity.Hydra(x) id
    if ctx.message.author.id == userid:
        print(f'{ctx.message.author}, closed connection!')
        await client.logout()
    else:
        await ctx.message.channel.send(':no_entry_sign: You don\'t have permission to execute this command!')
        print(f'Warning: {ctx.message.author} tried closing your connection!')

# fetch all viruses
@client.command(pass_context=True)
async def virus(ctx, virus):
    cur.execute(f'SELECT name, description FROM main WHERE name LIKE "%{virus}%"')
    rows = cur.fetchall()
    for row, desc in rows:
        row = str(row)
        desc = str(desc)
        desc = desc.strip("(',)")
        row = row.strip("(',)")
        embed = discord.Embed(title=row, description=desc, color=0x00ffbb)
        embed.set_footer(text='Darwin, version 0.0.1')
        await ctx.message.channel.send(embed = embed)

# executes the discord.Bot() sub-class
client.run(token)

