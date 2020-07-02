import  os
import discord
from discord.ext import commands

bot_token = os.getenv("TOKEN")
novel = commands.Bot(command_prefix = '~')

@novel.command()
async def ping(ctx):
  await ctx.send('Pong!')

novel.run(bot_token)