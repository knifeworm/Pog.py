import discord
from discord.ext import commands
import os
import json
from se import TOKEN

def get_prefix(bot, message):

    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

bot = commands.Bot(command_prefix = get_prefix)

@bot.event
async def on_ready():
    print("Pog.py is online!")


@bot.event
async def on_guild_join(guild):


    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = "!"

    with open("prefixes.json", "w") as f:
        json.dump(prefixes,f)


@bot.command()
@commands.has_guild_permissions(administrator = True)
async def changeprefix(ctx, prefix):

    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open("prefixes.json", "w") as f:
        json.dump(prefixes,f)


@bot.event
async def on_message(msg):

    if msg.mentions[0] == bot.user:

        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)

        pre = prefixes[str(msg.guild.id)]

        await msg.channel.send(f"My prefix for this server is {pre}") 

    await bot.process_commands(msg)

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