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
    async def kick(self, ctx, member : discord.Member, *, reason=None):
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

    @commands.command()
    @commands.has_guild_permissions(mute_members=True)
    async def mute(self, ctx, member : discord.Member, *, reason=None):
        role = discord.utils.get(ctx.guild.roles, name="Muted")

        if role is None:

            await ctx.send("Muted role not found i am creating the role for you!")
            create_role = await ctx.guild.create_role(name="Muted", reason = "Created for the mute command!")
            await ctx.send("Setting permissions!")

            for channel in ctx.guild.channels:
                role_channel = discord.utils.get(ctx.guild.roles, name="Muted")
                await channel.set_permissions(role_channel, speak=False, send_messages=False, read_message_history=True, read_messages=True)
                await ctx.send("Permissions set!")
                await ctx.send("Muteing!")
                await member.add_roles(role_channel)
                embed = discord.Embed(title = "Mute")
                embed.add_field(name = "Member Muted", value = f'{member}', inline=False)
                embed.add_field(name = "Staff Member", value = f'{ctx.author}', inline=False)
                embed.add_field(name = "Reason", value = f'{reason}', inline=False)
                await ctx.send(embed = embed)
                mem = discord.Embed(title = "Mute")
                mem.add_field(name = "Staff Member", value = f'{ctx.author}', inline=False)
                mem.add_field(name = "Reason", value = f'{reason}', inline=False)
                mem.add_field(name = "Server", value = f'{ctx.guild.name}', inline=False)
                await member.send(embed = mem)
                break
                if role_channel in member.roles:
                    await ctx.send(f"{member} is already muted :x:")
                    break
        else:
            role_channell = discord.utils.get(ctx.guild.roles, name="Muted")
            await member.add_roles(role_channell)
            embed = discord.Embed(title = "Mute")
            embed.add_field(name = "Member Muted", value = f'{member}', inline=False)
            embed.add_field(name = "Staff Member", value = f'{ctx.author}', inline=False)
            embed.add_field(name = "Reason", value = f'{reason}', inline=False)
            await ctx.send(embed = embed)
            mem = discord.Embed(title = "Mute")
            mem.add_field(name = "Staff Member", value = f'{ctx.author}', inline=False)
            mem.add_field(name = "Reason", value = f'{reason}', inline=False)
            mem.add_field(name = "Server", value = f'{ctx.guild.name}', inline=False)
            await member.send(embed = mem)


    @commands.command()
    @commands.has_guild_permissions(mute_members=True)
    async def unmute(self, ctx, member : discord.Member):
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        embed = discord.Embed(title = "Unmute")
        embed.add_field(name = "Member Unmuted", value = f'{member}', inline=False)
        embed.add_field(name = "Staff Member", value = f'{ctx.author}', inline=False)
        await ctx.send(embed = embed)
        mem = discord.Embed(tile = 'Unmute')
        mem.add_field(name = "Staff Member", value = f'{ctx.author}', inline=False)
        mem.add_field(name = "Server", value = f'{ctx.guild.name}', inline=False)
        await member.send(embed = mem)
        await member.remove_roles(role)
        if role not in member.roles:
            await ctx.send(f"{member} is not muted :x:")


    @commands.command()
    @commands.has_guild_permissions(ban_members=True)
    async def unban(self, *, member : discord.Member):
        banned_users = await ctx.guild.bans()
        member_name, member_disc = member.split('#')

        for banned_entry in banned_users:
            user = banned_entry.user

            if(user.name, user.discriminator) == (member_name,member_disc):

                await ctx.guild.unban(user)
                await ctx.send(member_name + "Has been unbanned and can join the server again!")
                return
        await ctx.send(member + "Was not found in the ban records!")




def setup(bot):
    bot.add_cog(moderation(bot))