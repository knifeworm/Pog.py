import discord
from discord.ext import commands
import os

TOKEN = 'C:/users/progr/desktop/token.json'

bot = commands.Bot(command_prefix = "!")

@bot.event
async def on_ready():
    print("Pog.py is online!")


@bot.command()
@commands.has_guild_permissions(administrator=True)
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f"Cog {extension} has been loaded! :white_check_mark:")


@bot.command()
@commands.has_guild_permissions(administrator=True)
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f"Cog {extension} has been unloaded! :white_check_mark:")

@bot.command()
@commands.has_guild_permissions(administrator=True)
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f"Cog {extension} has been reloaded! :white_check_mark:")


bot.run(TOKEN)