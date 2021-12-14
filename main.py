from typing import List
import discord
from discord.ext import commands
import logging

logging.basicConfig(level=logging.INFO)
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="$", description="Test bot", intents=intents)

@bot.event
async def on_ready():
    print("We have logged in as", bot.user)

@bot.command()
async def hello(ctx):
    await ctx.send('Hello')

@bot.command()
async def list_members(ctx):
    members = bot.get_all_members()
    # This line removes the repited members
    filtered_members = list(set(members))
    for x in filtered_members:
        await ctx.send(x)

@bot.command()
async def member_counter(ctx):
    members = bot.get_all_members()
    filtered_members = list(set(members))
    counter = len(filtered_members)
    message_to_send = "There is " + str(counter) + " members"
    await ctx.send(message_to_send)

bot.run('Your token goes here')
