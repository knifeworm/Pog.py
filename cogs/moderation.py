import discord
from discord.ext import commands
import os
import json


class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_guild_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        embed = discord.Embed(title="Ban")
        embed.add_field(name="Member Banned", value=f"{member}", inline=False)
        embed.add_field(name="Staff Member", value=f"{ctx.author}", inline=False)
        embed.add_field(name="Reason", value=f"{reason}", inline=False)
        await ctx.send(embed=embed)
        mem = discord.Embed(title="Ban")
        mem.add_field(name="Staff Member", value=f"{ctx.author}", inline=False)
        mem.add_field(name="Reason", value=f"{reason}", inline=False)
        mem.add_field(name="Server", value=f"{ctx.guild.name}", inline=False)
        await member.send(embed=mem)
        await member.ban(reason=reason)

    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error,commands.MissingPermissions):
            await ctx.send("You do not have permission to run this command! :x:")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("The command is missing a arg.")
    
    @commands.command()
    @commands.has_guild_permissions(kick_members=True)
    async def kick(self, ct, member : discord.Member, *, reason=None):
        embed = discord.Embed(title="Kick")
        embed.add_field(name="Member Kicked", value=f"{member}", inline=False)
        embed.add_field(name="Staff Member", value=f"{ctx.author}", inline=False)
        embed.add_field(name="Reason", value=f"{reason}", inline=False)
        await ctx.send(embed=embed)
        mem = discord.Embed(title="Kick")
        mem.add_field(name="Staff Member", value=f"{ctx.author}", inline=False)
        mem.add_field(name="Reason", value=f"{reason}", inline=False)
        mem.add_field(name="Server", value=f"{ctx.guild.name}", inline=False)
        await member.send(embed=mem)
        await member.kick(reason=reason)


def setup(bot):
    bot.add_cog(moderation(bot))