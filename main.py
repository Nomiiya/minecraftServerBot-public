import discord # For Discord
from discord.utils import get  # For Discord Utils
from discord.ext import commands # For Discord Extensions
import asyncio
import logging # For Logging
from pathlib import Path # For Pathing
import json

#Def import
import serverUtilities

#Bot Configs
cwd = Path(__file__).parents[0]
cwd = str(cwd)
#print(f"{cwd}\n-----")

#Both Definitions
secret_file = json.load(open(cwd+'/bot_config/secrets.json'))
bot = commands.Bot(command_prefix='!!', case_insenstive=True)
bot.config_token = secret_file['token']
logging.basicConfig(level=logging.INFO)

@bot.command(name='hello')
async def _hello(ctx):
    msg = await ctx.send("Hello World")

@bot.command(name='restart')
async def _restart(ctx):
    serverUtilities.server_restart()
    msg = await ctx.send("Server has been restarted. Please wait a few minutes.")

@bot.command(name='botOFF')
async def _botOFF(ctx):
    await ctx.bot.logout()

bot.run(bot.config_token)