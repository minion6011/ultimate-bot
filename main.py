#needed for start the bot
import discord
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure, NoPrivateMessage
from discord.utils import get

from discord import app_commands #disord slash

import random #random exractor
from random import choice #random exractor

import asyncio #time

import os #botinfo

import aiohttp #https
import requests #https
from requests import get #https
import json #htpps

#system-info
import psutil, datetime


#activity
from discord_together import DiscordTogether

#traduttore
from deep_translator import GoogleTranslator

#music-bot
import pytube
from pytube import YouTube
from pytube import Search
import asyncio
import os

#generate image
import base64
from io import BytesIO
import io

#verifydelete - captcha - setupverify
import random #captcha-image-text
from PIL import Image, ImageDraw, ImageFont #captcha-image
import io #captcha-image

#automod
from typing import Literal #slash preset-option
from datetime import timedelta #timeout time

#discord-ui
from discord import ui
from discord import app_commands


#config
with open("config.json") as f:
    try:
        data = json.load(f)
    except json.decoder.JSONDecodeError as e:
        print("Errore in config.json")
        print(e)
        exit(1)


#intent
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True
intents.reactions = True


pre = data["command_prefix"]
client = commands.Bot(command_prefix=(pre), intents=intents, case_insensitive=True)
client.remove_command('help')



#dati generali

my_id = [598119406731657216, 1181630796759564358]
beta_list = [598119406731657216, 829022689338851389, 1181630796759564358]

footer_testo = data["footer_embed"]
stalkid = 1045020366751404172
errorchannel = 1046796347870826496
statuschannel = 1129639048735117342




is_me = commands.check(lambda ctx: ctx.author.id in my_id )
is_beta = commands.check(lambda ctx: ctx.author.id in beta_list )





#-----------Events--------------#

@client.event
async def on_ready():
	try:
		change_status.cancel()
	except:
		pass
	print(f"Bot logged into {client.user}.")
	channel = client.get_channel(statuschannel)
	embed = discord.Embed(title=f"**Bot Online 🟢 - Start d'avvio**", color=discord.Color.green())
	await channel.send(embed=embed)
	#slash_sync = await client.tree.sync()
	#print(f"Synced app command (tree) {len(slash_sync)}.")
	#token_json = data["discord_token"]
	#client.togetherControl = await DiscordTogether(token_json) #activity command - old 
	await asyncio.sleep(10)
	change_status.start()



@client.event
async def on_voice_state_update(member, before, after):
	voice_client = member.guild.voice_client
	if member.display_name == client.user:
		if voice_client.is_playing():
			voice_client.stop()   	


@client.event
async def on_message_edit(before, after):
	if after.author.bot:
		return
	elif before.author.bot:
		return
	else:
		await client.process_commands(after)


'''

#-----------Stalker_old--------------#

@client.event
async def on_message(message):
	if message.author.bot:
		return
	if len(message.content) > 1800:
		return
	if message.channel.type == discord.ChannelType.private:
		await client.process_commands(message) 
		await asyncio.sleep(20)
		channel = client.get_channel(stalkid)
		if message.attachments:
			image_links = [attachment.url for attachment in message.attachments]
			embed = discord.Embed(title=f"**[Stalker]**\nImmagine inviata\nUtente: `{message.author.display_name}#{message.author.discriminator}`\nDm: `Yes`", color=discord.Color.green())
			message_c = f"> Url: \n>>> {', '.join(image_links)}"
			await channel.send(embed=embed)
			await channel.send(message_c)
		else:
			embed = discord.Embed(title=f"**[Stalker]**\nMessagio inviato\nUtente: `{message.author.display_name}#{message.author.discriminator}`\nDm: `Yes`", color=discord.Color.green())
			embed.add_field(name = 'Contenuto:', value=f"`{message.content}`", inline = True)
			await channel.send(embed=embed)
	else:
		await client.process_commands(message)
		await asyncio.sleep(20)
		channel = client.get_channel(stalkid)
		if message.attachments:
			image_links = [attachment.url for attachment in message.attachments]
			embed = discord.Embed(title=f"**[Stalker]**\nImmagine inviata\nUtente: `{message.author.display_name}#{message.author.discriminator}`\n Server: `{message.guild.name}`", color=discord.Color.green())
			embed.add_field(name = 'Canale:', value=f"<#{message.channel.id}>", inline = True)
			message_c = f"> Url: \n>>> {', '.join(image_links)} "
			await channel.send(embed=embed)
			await channel.send(message_c)
		else:
			embed = discord.Embed(title=f"**[Stalker]**\nMessagio inviato\nUtente: `{message.author.display_name}#{message.author.discriminator}`\n Server: `{message.guild.name}`", color=discord.Color.green())
			embed.add_field(name = 'Contenuto:', value=f"`{message.content}`", inline = True)
			embed.add_field(name = 'Canale:', value=f"<#{message.channel.id}>", inline = True)
			await channel.send(embed=embed)


@client.event
async def on_message_delete(message):
	if message.author.bot:
		return
	if len(message.content) > 1908:
		return
	if message.channel.type == discord.ChannelType.private:
		await asyncio.sleep(20)
		channel = client.get_channel(stalkid)
		if message.attachments:
			image_links = [attachment.url for attachment in message.attachments]
			embed = discord.Embed(title=f"**[Stalker]**\nImmagine eliminata\nUtente: `{message.author.display_name}#{message.author.discriminator}`\n Server: `{message.guild.name}`", color=discord.Color.red())
			message_c = f"> Url: \n>>> {', '.join(image_links)} "
			await channel.send(embed=embed)
			await channel.send(message_c)
		else:
			embed = discord.Embed(title=f"**[Stalker]**\nMessagio Eliminato\nUtente: `{message.author.display_name}#{message.author.discriminator}`\n Dm: `Yes`", color=discord.Color.red())
			embed.add_field(name = 'Contenuto:', value=f"`{message.content}`", inline = True)
			await channel.send(embed=embed)
	else:
		await asyncio.sleep(20)
		channel = client.get_channel(stalkid)
		if message.attachments:
			image_links = [attachment.url for attachment in message.attachments]
			embed = discord.Embed(title=f"**[Stalker]**\nImmagine eliminata\nUtente: `{message.author.display_name}#{message.author.discriminator}`\n Server: `{message.guild.name}`", color=discord.Color.red())
			embed.add_field(name = 'Canale:', value=f"<#{message.channel.id}>", inline = True)
			message_c = f"> Url: \n>>> {', '.join(image_links)} "
			await channel.send(embed=embed)
			await channel.send(message_c)
		else:
			embed = discord.Embed(title=f"**[Stalker]**\nMessagio Eliminato\nUtente: `{message.author.display_name}#{message.author.discriminator}`\n Server: `{message.guild.name}`", color=discord.Color.red())
			embed.add_field(name = 'Contenuto:', value=f"`{message.content}`", inline = True)
			embed.add_field(name = 'Canale:', value=f"<#{message.channel.id}>", inline = True)
			await channel.send(embed=embed)

@client.event
async def on_message_edit(before, after):
	if after.author.bot:
		return
	if len(after.content) > 1000:
		return
	if len(before.content) > 1000:
		return
	if after.channel.type == discord.ChannelType.private:
		await client.process_commands(after)
		await asyncio.sleep(20)
		channel = client.get_channel(stalkid)
		embed = discord.Embed(title=f"**[Stalker]**\nMessagio Editato\nUtente: `{after.author.display_name}#{after.author.discriminator}`\nDm: `Yes`", color=discord.Color.gold())
		embed.add_field(name = 'Contenuto:', value=f"Prima: `{before.content}`, Dopo: `{after.content}`", inline = True)
		await channel.send(embed=embed)
	else:
		await client.process_commands(after)
		await asyncio.sleep(20)
		channel = client.get_channel(stalkid)
		embed = discord.Embed(title=f"**[Stalker]**\nMessagio Editato\nUtente: `{after.author.display_name}#{after.author.discriminator}`\n Server: `{after.guild.name}`", color=discord.Color.gold())
		embed.add_field(name = 'Contenuto:', value=f"Prima: `{before.content}`, Dopo: `{after.content}`", inline = True)
		embed.add_field(name = 'Canale:', value=f"<#{after.channel.id}>", inline = True)
		await channel.send(embed=embed)

@client.event
async def on_member_join(member):
	try:
		await asyncio.sleep(20)
		channel = client.get_channel(stalkid)
		embed = discord.Embed(title=f"**[Stalker]**\nNuovo utente nel server\nUtente: `{member.display_name}#{member.discriminator}`\n Server: `{member.guild.name}`", color=discord.Color.orange())
		await channel.send(embed=embed)
		if member.guild.id == "1043925344312381550":
			await member.create_dm()
			embed = discord.Embed(title=f"Hi {member.name}, welcome to {member.guild}!", color=discord.Color.orange())
			await member.dm_channel.send(embed=embed)
	except:
		await asyncio.sleep(20)
		channel = client.get_channel(errorchannel)
		embed = discord.Embed(title=f"**[Errore]**\nOn_Member_Join error (private user)", color=discord.Color.red())
		await channel.send(embed=embed)
	
@client.event
async def on_member_ban(guild, user):
	await asyncio.sleep(20)
	channel = client.get_channel(stalkid)
	embed = discord.Embed(title=f"**[Stalker]**\nUtente bannato\nUtente: `{user.display_name}#{user.discriminator}`\n Server: `{guild.name}`", color=discord.Color.red())


@client.event
async def on_member_unban(guild, user):
	await asyncio.sleep(20)
	channel = client.get_channel(stalkid)
	embed = discord.Embed(title=f"**[Stalker]**\nUtente sbannato\nUtente: `{user.display_name}#{user.discriminator}`\n Server: `{guild.name}`", color=discord.Color.red())

@client.event
async def on_member_remove(member):
	await asyncio.sleep(20)
	guild = member.guild
	channel = client.get_channel(stalkid)
	embed = discord.Embed(title=f"**[Stalker]**\nMembro rimosso / quit\nUtente: `{member.display_name}#{member.discriminator}`\n Server: `{member.guild.name}`", color=discord.Color.red())
	await channel.send(embed=embed)

@client.event
async def on_member_update(before, after):
	await asyncio.sleep(20)
	channel = client.get_channel(stalkid)
	embed = discord.Embed(title=f"**[Stalker]**\n Server: `{after.guild.name}`", color=discord.Color.purple())
	embed.add_field(name = 'Status:', value=f"Prima: `{before.status}`, Dopo: `{after.status}`", inline = False)
	embed.add_field(name = 'Nome:', value=f"Prima: `{before.name}`, Dopo: `{after.name}`", inline = False)
	embed.add_field(name = 'Avatar:', value=f"Prima: [Url]({before.avatar}), Dopo: [Url]({after.avatar})", inline = False) 
	embed.add_field(name = 'Attività:', value=f"Prima: `{before.activity}`, Dopo: `{after.activity}`", inline = False)
	embed.add_field(name = 'Avvertenza:', value=f":warning: se Alcune informazioni non cambiano :warning:\n:warning: Significa che sono le stesse :warning:", inline = False)
	await channel.send(embed=embed)

@client.event
async def on_voice_state_update(member, before, after):
	voice_client = member.guild.voice_client
	if member.display_name == client.user:
		if voice_client.is_playing():
			voice_client.stop()   	
	if before.channel is None and after.channel is not None:
		await asyncio.sleep(20)
		channel = client.get_channel(stalkid)
		embed = discord.Embed(title=f"**[Stalker]**\nUtente in Chat vocale\nUtente: `{member.display_name}#{member.discriminator}`\nServer: `{member.guild.name}`", color=discord.Color.blue())
		embed.add_field(name = 'Canale:', value=f"<#{after.channel}>", inline = True)
		await channel.send(embed=embed)
	if before.channel is not None and after.channel is None:
		await asyncio.sleep(20)
		channel = client.get_channel(stalkid)
		embed = discord.Embed(title=f"**[Stalker]**\nUtente uscito dalla Chat vocale\nUtente: `{member.display_name}#{member.discriminator}`\nServer: `{member.guild.name}`", color=discord.Color.red())
		embed.add_field(name = 'Canale:', value=f"<#{before.channel}>", inline = True)
		await channel.send(embed=embed)

#ruoli

@client.event
async def on_guild_role_delete(role):
	await asyncio.sleep(20)
	channel = client.get_channel(stalkid)
	embed = discord.Embed(title=f"**[Stalker]**\nRuolo eliminato\nServer: `{role.guild.name}`", color=discord.Color.red())
	embed.add_field(name = 'Nome:', value=f"`{role.name}`", inline = True)
 
@client.event
async def on_guild_role_update(before, after):
	await asyncio.sleep(20)
	channel = client.get_channel(stalkid)
	embed = discord.Embed(title=f"**[Stalker]**\nUpdate ruolo\nServer: `{before.guild.name}`", color=discord.Color.gold())
	embed.add_field(name = 'Nome:', value=f"Prima: `{before.name}` Dopo:  `{after.name}`", inline = False)
	embed.add_field(name = 'Avvertenza:', value=f":warning: se il nome non cambio sono i permessi :warning:\n:warning: per mancata voglia non sono stati inseriti :warning:", inline = True)
	await channel.send(embed=embed)

@client.event
async def on_guild_role_create(role):
	await asyncio.sleep(20)
	channel = client.get_channel(stalkid)
	embed = discord.Embed(title=f"**[Stalker]**\nRuolo creato\nServer: `{role.guild.name}`", color=discord.Color.green())
	embed.add_field(name = 'Nome:', value=f"`{role.name}`", inline = True)
	await channel.send(embed=embed)
'''



#----------Commands--------#



@commands.cooldown(1, 5, commands.BucketType.user)
@client.command()
@commands.guild_only()
async def help(ctx):
	embed = discord.Embed(title="`?help` has been disabled\nTry using </help:1094994368445816934>", color=discord.Color.greyple())
	embed.set_footer(text=footer_testo)
	await ctx.send(embed=embed, delete_after=10)

#--Mod command


@client.command()
@commands.guild_only()
@commands.has_permissions(manage_messages=True)
@commands.cooldown(1, 20, commands.BucketType.user)
async def nuke(ctx, amount: int = 50):
	if amount == 0:
		embed = discord.Embed(title=f"Unable to delete messages, you must select a number between 1 and 450", color=discord.Color.red())
		embed.set_footer(text=footer_testo)  
		await ctx.send(embed=embed, delete_after=4)
		return
	if amount < 400:
		embed = discord.Embed(title=f"{amount} messages deleted", color=discord.Color.red())
		embed.set_image(url="https://www.19fortyfive.com/wp-content/uploads/2021/10/Nuclear-Weapons-Test.jpg")
		await ctx.channel.purge(limit=amount)
		embed.set_footer(text=footer_testo)  
		await ctx.send(embed=embed, delete_after=4)
	else:
		embed = discord.Embed(title=f"Unable to delete messages, the maximum is 450", color=discord.Color.red())
		embed.set_footer(text=footer_testo)  
		await ctx.send(embed=embed, delete_after=4)




@client.command()
@commands.guild_only()
@has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason = None):
	try:
		if member == None:
			embed = discord.Embed(title=":warning: Please write the member's ID :warning:", color=discord.Color.red())
			embed.set_footer(text=footer_testo)  
			await ctx.send(embed=embed)
		elif reason == None:
			if member == None:
				embed = discord.Embed(title=":warning: Please write the member's ID :warning:", color=discord.Color.red())
				embed.set_footer(text=footer_testo)  
				await ctx.send(embed=embed)
			else:
				#embed2 = discord.Embed(title=f"You have been kicked from the server: {ctx.guild.name}", color=discord.Color.red())
				#embed2.set_footer(text=footer_testo)
				#await member.send(embed2)
				#await member.send(f"You have been kicked from the server: {ctx.guild.name}")
				embed = discord.Embed(title=":warning: Member was kicked :warning:", color=discord.Color.red())
				embed.set_footer(text=footer_testo)  
				await ctx.send(embed=embed)
				await member.kick(reason=f"You have been banned from the server: {ctx.guild.name}")
		else:
			#embed2 = discord.Embed(title=f"You have been kicked from the server: {ctx.guild.name}, For: '{reason}'", color=discord.Color.red())
			#embed2.set_footer(text=footer_testo)
			#await member.send(embed2)
			#await member.send(f"You have been kicked from the server: {ctx.guild.name}, For: '{reason}'")
			embed = discord.Embed(title=":warning: Member was kicked :warning:", color=discord.Color.red())
			embed.set_footer(text=footer_testo)  
			await ctx.send(embed=embed)
			await member.kick(reason=f"You have been kicked from the server: {ctx.guild.name}, For: '{reason}'")
	except Exception as e:
		if 'error code: 50013' in str(e):
			embed = discord.Embed(title="Error: I don't have permission to kick this user", color=discord.Color.red())
			embed.set_footer(text=footer_testo)
			await ctx.send(embed=embed, delete_after=4)
		else:
			channel = client.get_channel(errorchannel)
			await channel.send(f"**[Errore]** \nisinstance: ```{e}```\nerror: ```{str(e)}```")
			raise e




@client.command()
@commands.guild_only()
@has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason = None):
	try:
		if member == None:
			embed = discord.Embed(title=":warning: Please write the member's ID :warning:", color=discord.Color.red())
			embed.set_footer(text=footer_testo)  
			await ctx.send(embed=embed)
		elif reason == None:
			if member == None:
				embed = discord.Embed(title=":warning: Please write the member's ID :warning:", color=discord.Color.red())
				embed.set_footer(text=footer_testo)  
				await ctx.send(embed=embed)
			else:
				#embed2 = discord.Embed(title=f"You have been banned from the server: {ctx.guild.name}", color=discord.Color.red())
				#embed2.set_footer(text=footer_testo)
				#await member.send(embed2)
				#await member.send(f"You have been banned from the server: {ctx.guild.name}")
				await member.ban(reason=f"You have been banned from the server: {ctx.guild.name}")
				embed = discord.Embed(title=":warning: Member was banned :warning:", color=discord.Color.red())
				embed.set_footer(text=footer_testo)  
				await ctx.send(embed=embed,delete_after=10)
		else:
			#embed2 = discord.Embed(title=f"You have been banned from the server: {ctx.guild.name}/nFor: '{reason}'", color=discord.Color.red())
			#embed2.set_footer(text=footer_testo)
			#await member.send(embed2)
			#await member.send(f"You have been banned from the server: {ctx.guild.name}/nFor: '{reason}'")
			await member.ban(reason=f"You have been banned from the server: {ctx.guild.name}, For: '{reason}'")
			embed = discord.Embed(title=":warning: Member was banned :warning:", color=discord.Color.red())
			embed.set_footer(text=footer_testo)  
			await ctx.send(embed=embed,delete_after=10)
	except Exception as e:
		if 'error code: 50013' in str(e):
			embed = discord.Embed(title="Error: I don't have permission to ban this user", color=discord.Color.red())
			embed.set_footer(text=footer_testo)
			await ctx.send(embed=embed, delete_after=4)
		else:
			channel = client.get_channel(errorchannel)
			await channel.send(f"**[Errore]** \nisinstance: ```{e}```\nerror: ```{str(e)}```")
			raise e





@client.command()
@commands.guild_only()
@has_permissions(ban_members=True)
async def unban(ctx, user: discord.User):
	try:
		if user == None:
			embed = discord.Embed(title=":warning: Please write the member's ID :warning:", color=discord.Color.red())
			embed.set_footer(text=footer_testo)  
			await ctx.send(embed=embed)
		else:
			await ctx.guild.unban(user)
			embed = discord.Embed(title=f":warning: `{user}` has been unbanned :warning:", color=discord.Color.red())
			embed.set_footer(text=footer_testo)  
			await ctx.send(embed=embed)
	except Exception as e:
		if 'error code: 50013' in str(e):
			embed = discord.Embed(title="Error: I don't have permission to ban this user", color=discord.Color.red())
			embed.set_footer(text=footer_testo)
			await ctx.send(embed=embed, delete_after=4)
		else:
			channel = client.get_channel(errorchannel)
			await channel.send(f"**[Errore]** \nisinstance: ```{e}```\nerror: ```{str(e)}```")
			raise e



@client.command()
@commands.guild_only()
@has_permissions(administrator = True)
@commands.cooldown(1, 60, commands.BucketType.user)
async def delchannel(ctx):
    for c in ctx.guild.channels: # iterating through each guild channel
        await c.delete()



@client.command()
@commands.guild_only()
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.has_permissions(manage_channels = True)
async def lockdown(ctx):
	await ctx.message.delete()
	for role in ctx.guild.roles:
		if role.permissions.manage_channels:
			await ctx.channel.set_permissions(role, attach_files=True, send_messages=True, read_messages=True, read_message_history=True, add_reactions=True)
	await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False, view_channel=False)
	embed = discord.Embed(title=f"***{ctx.channel.mention} is now in lockdown.*** :lock:", color=discord.Color.yellow())
	await ctx.send(embed=embed, delete_after=5)

@client.command()
@commands.guild_only()
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
	await ctx.message.delete()
	await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True, view_channel=True)
	embed = discord.Embed(title=f"***{ctx.channel.mention} has been unlocked.*** :unlock:", color=discord.Color.yellow())
	await ctx.send(embed=embed, delete_after=5)



@client.command()
@commands.guild_only()
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.has_permissions(moderate_members=True)
async def mute(ctx, user: discord.Member = None, reason = None):
		try:
			if user == None:
				embed = discord.Embed(title="Please send the user id", color=discord.Color.red())
				embed.set_footer(text=footer_testo)
				await ctx.send(embed=embed, delete_after=4)
			else:
				guild = ctx.guild
				if discord.utils.get(ctx.guild.roles, name="mute"):
					if reason == None:
						role = discord.utils.get(ctx.guild.roles, name="mute")
						guild = ctx.guild
						for channel in ctx.guild.channels:
							permissions = discord.PermissionOverwrite(send_messages=False, read_messages=True, speak=False)
							await channel.set_permissions(role, overwrite=permissions)
						await user.add_roles(role)
						embed = discord.Embed(title = 'I muted', description = f'{user}', color=discord.Color.blue())
						embed.set_footer(text=footer_testo)
						await ctx.send(embed=embed, delete_after=7)
						name = str(ctx.guild.name)
						check_voice_member = ctx.guild.get_member(int(user.id))
						if check_voice_member and check_voice_member.voice:
							await check_voice_member.move_to(None)
						try:
							await user.send(f"You have been muted in the server: **{name}**")
						except:
							return
					else:
						role = discord.utils.get(ctx.guild.roles, name="mute")
						guild = ctx.guild
						for channel in ctx.guild.channels:
							permissions = discord.PermissionOverwrite(send_messages=False, read_messages=True, speak=False)
							await channel.set_permissions(role, overwrite=permissions)
						await user.add_roles(role)
						embed = discord.Embed(title = f'I muted {user}', description = f'For reason: {reason}', color=discord.Color.blue())
						embed.set_footer(text=footer_testo)
						await ctx.send(embed=embed, delete_after=7)
						name = str(ctx.guild.name)
						check_voice_member = ctx.guild.get_member(int(user.id))
						if check_voice_member and check_voice_member.voice:
							await check_voice_member.move_to(None)
						try:
							await user.send(f"You have been muted in the server: **{name}** because:\n{reason}")
						except:
							return
				else:
					if reason == None:
						role = discord.utils.get(ctx.guild.roles, name="mute")
						permissions = discord.Permissions(send_messages=False, read_messages=True, speak=False)
						await guild.create_role(name="mute", colour=discord.Colour(0x444949), permissions=permissions)
						guild = ctx.guild
						for channel in ctx.guild.channels:
							permissions = discord.PermissionOverwrite(send_messages=False, read_messages=True, speak=False)
							await channel.set_permissions(role, overwrite=permissions)
						await user.add_roles(role)
						embed = discord.Embed(title = 'I muted', description = f'{user}', color=discord.Color.blue())
						embed.set_footer(text=footer_testo)
						await ctx.send(embed=embed, delete_after=7)
						name = str(ctx.guild.name)
						check_voice_member = ctx.guild.get_member(int(user.id))
						if check_voice_member and check_voice_member.voice:
							await check_voice_member.move_to(None)
						else:
							return
						try:
							await user.send(f"You have been muted in the server: **{name}**")
						except:
							pass
					else:
						role = discord.utils.get(ctx.guild.roles, name="mute")
						permissions = discord.Permissions(send_messages=False, read_messages=True, speak=False)
						await guild.create_role(name="mute", colour=discord.Colour(0x444949), permissions=permissions)
						for channel in ctx.guild.channels:
							permissions = discord.PermissionOverwrite(send_messages=False, read_messages=True, speak=False)
							await channel.set_permissions(role, overwrite=permissions)
						await user.add_roles(role)
						embed = discord.Embed(title = f'I muted {user}', description = f'For reason: {reason}', color=discord.Color.blue())	
						embed.set_footer(text=footer_testo)
						await ctx.send(embed=embed, delete_after=7)
						name = str(ctx.guild.name)
						check_voice_member = ctx.guild.get_member(int(user.id))
						if check_voice_member and check_voice_member.voice:
							await check_voice_member.move_to(None)
						else:
							return
						try:
							await user.send(f"You have been muted in the server: **{name}** because:\n{reason}")
						except:
							pass
		except Exception as e:
			if "target parameter must be either Member or Role" in str(e):
				embed = discord.Embed(title="Error: You need to ping the user to mute it", color=discord.Color.red())
				embed.set_footer(text=footer_testo)
				await ctx.send(embed=embed, delete_after=4)
			else:
				channel = client.get_channel(errorchannel)
				await channel.send(f"**[Errore]** \nisinstance: ```{isinstance}```\nerror: ```{str(e)}```")
				raise e

@client.command()
@commands.guild_only()
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.has_permissions(moderate_members=True)
async def unmute(ctx, user: discord.Member = None):
	try:
			if user == None:
				embed = discord.Embed(title="Please send the user id", color=discord.Color.red())
				embed.set_footer(text=footer_testo)
				await ctx.send(embed=embed)
			else:
				role = discord.utils.get(ctx.guild.roles, name="mute")
				await user.remove_roles(role)
				check_voice_member = ctx.guild.get_member(int(user.id))
				if check_voice_member and check_voice_member.voice:
					await check_voice_member.move_to(None)
				else:
					return
				embed = discord.Embed(title = 'I unmuted', description = f'{user}', color=discord.Color.blue())
				embed.set_footer(text=footer_testo)
				await ctx.send(embed=embed)
	except Exception as e:
			if "target parameter must be either Member or Role" in str(e):
				embed = discord.Embed(title="Error: You need to ping the user to mute it", color=discord.Color.red())
				embed.set_footer(text=footer_testo)
				await ctx.send(embed=embed, delete_after=4)
			else:
				channel = client.get_channel(errorchannel)
				await channel.send(f"**[Errore]** \nisinstance: ```{isinstance}```\nerror: ```{str(e)}```")
				raise e




@client.command()
@commands.guild_only()
@commands.has_permissions(manage_channels=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def slowmode(ctx, seconds: int):
	await ctx.channel.edit(slowmode_delay=seconds)
	slowmode_embed = discord.Embed(title="Slowmode", description="A slowmode was set for this channel", colour=discord.Colour.green())
	slowmode_embed.set_footer(text=footer_testo)
	await ctx.send(embed=slowmode_embed, delete_after=10)

#--


@client.command()
@commands.guild_only()
@commands.cooldown(1, 5, commands.BucketType.user)
async def userinfo(ctx, *, user: discord.Member = None):
	voice_state = None if not user.voice else user.voice.channel
	#role = user.top_role.name
	role = user.top_role.name
	acc_created = user.created_at.__format__('Date: %A, %d. %B %Y Time: %H:%M:%S')
	server_join = user.joined_at.__format__('Date: %A, %d. %B %Y Time: %H:%M:%S')
	if role == "@everyone":
		role = None
	embed = discord.Embed(title=f"**User Info**", color=discord.Colour.blue())
	embed.add_field(name=':id: - User ID', value=f"`{user.id}`", inline=True)
	embed.add_field(name=":bust_in_silhouette: - Displayed Server Name", value=user.mention, inline=True)
	embed.add_field(name=':bust_in_silhouette: - User Name', value=f"`{user.name}`", inline=True)
	#embed.add_field(name=':video_game: - User Game', value=f"**{user.activity}**", inline=False)
	embed.add_field(name=':robot: - Robot?', value=f"`{user.bot}`", inline=True)
	embed.add_field(name=':loud_sound:  - Is in voice', value=f"**In:** `{voice_state}`", inline=True)
	embed.add_field(name=':radio_button:  - Highest Role', value=f"`{role}`", inline=True)
	embed.add_field(name=':calendar: - Account Created', value=f"`{acc_created}`", inline=True)
	embed.add_field(name=':calendar: - Join Server Date', value=f"`{server_join}`", inline=True)
	embed.set_thumbnail(url=user.avatar)
	embed.set_footer(text=footer_testo)
	await ctx.send(embed=embed)














@client.command()
@commands.guild_only()
@commands.cooldown(1, 5, commands.BucketType.user)
async def serverinfo(ctx):
	guild_create = ctx.guild.created_at.strftime("%d-%m-%Y")
	check_text = discord.utils.get(ctx.guild.text_channels)
	check_voice = discord.utils.get(ctx.guild.voice_channels)
	check_category = discord.utils.get(ctx.guild.categories)
	
	voice_state = None if not user.voice else user.voice.channel
	#role = user.top_role.name
	role = user.top_role.name
	acc_created = user.created_at.__format__('Date: %A, %d. %B %Y Time: %H:%M:%S')
	server_join = user.joined_at.__format__('Date: %A, %d. %B %Y Time: %H:%M:%S')
	if role == "@everyone":
		role = None
	embed = discord.Embed(title=f"***{ctx.guild.name}*** - Info", color=discord.Colour.blue())
	embed.add_field(name=':page_facing_up: - Nome del Server', value=f'**`{str(ctx.guild.name)}`**', inline=True)
	embed.add_field(name=':bookmark_tabs: -  Descrizione del Server', value=f'**`{str(ctx.guild.description)}`**', inline=True)
	embed.add_field(name=':id: - ID del Server', value=f"`{ctx.guild.id}`", inline=True)
	embed.add_field(name=':busts_in_silhouette: - Membri', value=f'**`{ctx.guild.member_count}` Membri**', inline=True)
	embed.add_field(name=':crown: - Creatore del Server', value=f"<@{ctx.guild.owner_id}>", inline=True)
	embed.add_field(name=':bust_in_silhouette: - Numero Ruoli', value=f'**`{len(ctx.guild.roles)}` Ruoli**', inline=True)
	#if check_forum is not None:
	#	embed.add_field(name=f':speech_left: - Forum {len(ctx.guild.forum_channels)}', inline=False)
	if check_text is not None:
		embed.add_field(name=f':speech_balloon: - Canali Testuali ', value=f'**`{len(ctx.guild.text_channels)}`**', inline=True)
	if check_voice is not None:
		embed.add_field(name=f':speaker: - Canali Vocali ', value=f'**`{len(ctx.guild.voice_channels)}`**', inline=True)
	if check_category is not None:
		embed.add_field(name=':open_file_folder: - Categorie ', value=f'**`{len(ctx.guild.categories)}`**', inline=True)
	embed.add_field(name=':calendar: - Server creato il:', value=f"**`{guild_create}`**", inline=False)
	embed.set_thumbnail(url=user.avatar)
	embed.set_footer(text=footer_testo)
	await ctx.send(embed=embed)

 

@client.command()
@commands.guild_only()
@commands.cooldown(1, 5, commands.BucketType.user)
async def meme(ctx):
		link_list = [
			"https://www.reddit.com/r/memes/new.json",
			"https://www.reddit.com/r/dankmemes/new.json",
			"https://www.reddit.com/r/meme/new.json",
		]
		link = random.choice(link_list)
		embed = discord.Embed(title="Meme", color=discord.Colour.green())
		async with aiohttp.ClientSession() as cs:
			async with cs.get(link) as r:
				res = await r.json()
				embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
				embed.set_footer(text=footer_testo)  
				await ctx.send(embed=embed)







@client.command()
@commands.guild_only()
@commands.cooldown(1, 5, commands.BucketType.user)
async def translate(ctx, language, *, request):
	text = request
	lang = language
	try:
		if len(text) > 1998:
			embed = discord.Embed(title="Error: The text is too long must not exceed 1998 characters", color=discord.Color.red())
			embed.set_footer(text=footer_testo)
			await ctx.send(embed=embed, delete_after=4)
		else:
			if len(text) > 1024:
				traduttore = GoogleTranslator(source='auto', target=lang)
				risultato = traduttore.translate(text)
				await ctx.send(f"```{risultato}```")
			else:
				traduttore = GoogleTranslator(source='auto', target=lang)
				risultato = traduttore.translate(text)
				embed=discord.Embed(color=discord.Color.green())
				embed.add_field(name=":earth_americas: Request:", value=f"{request}")
				embed.set_footer(text=footer_testo)
				await ctx.send(embed=embed, content=f"```{risultato}```")
	except Exception as e:
		embed=discord.Embed(title=f"The language {lang} is not supported.\nTo see the supported languages press the button.", color=discord.Color.green())
		embed.set_footer(text=footer_testo)
		await ctx.send(embed=embed, view=TraslateButton())





@client.command()
@commands.guild_only()
@commands.cooldown(1, 5, commands.BucketType.user)
async def casual(ctx):
	list1 = ["yes", "no"]
	r = random.choice(list1)
	embed = discord.Embed(title=f"{r}", color=discord.Color.blue())
	embed.set_footer(text=footer_testo)  
	await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
@commands.cooldown(1, 5, commands.BucketType.user)
async def coinflip(ctx):
	coin = ['heads  :coin:','tails  :coin:']
	r = random.choice(coin)
	link = 'https://i.pinimg.com/originals/d7/49/06/d74906d39a1964e7d07555e7601b06ad.gif'
	#link = 'https://cdn-icons-png.flaticon.com/512/1540/1540515.png'
	embed = discord.Embed(title=f"It came up {r}", color=discord.Color.gold())
	embed.set_image(url=link)
	embed.set_footer(text=footer_testo)  
	await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
@commands.cooldown(1, 5, commands.BucketType.user)
async def num_extractor(ctx):
	number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	r = random.choice(number)
	embed = discord.Embed(title=f"Is out", color=discord.Color.blue())
	embed.add_field(name = 'Number', value = f'{r}')
	embed.set_footer(text=footer_testo)  
	await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
@commands.cooldown(1, 25, commands.BucketType.user)
async def infobot(ctx):
	time_boot = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("**Date: `%Y-%m-%d`  Time: `%H:%M:%S`**")
	embed = discord.Embed(title = 'System Resource Usage', description = 'See CPU and memory usage of the system.', color=discord.Color.blue())
	embed.add_field(name = ':computer: **CPU Usage**', value = f'{psutil.cpu_percent()}%', inline = False)
	embed.add_field(name = ':floppy_disk: **Memory Usage**', value = f'{psutil.virtual_memory().percent}%', inline = False)
	embed.add_field(name = ':floppy_disk: **Available Memory**', value = f'{psutil.virtual_memory().available * 100 / psutil.virtual_memory().total}%', inline = False)
	embed.add_field(name = ':globe_with_meridians: **Ping**', value = f'{round(client.latency * 1000)}ms')
	embed.add_field(name = ':timer: **Last Boot**', value =time_boot)
	embed.set_footer(text=footer_testo)
	await ctx.send(embed = embed)

	

		

@client.command()
@commands.guild_only()
@commands.cooldown(1, 5, commands.BucketType.user)
async def dictionary(ctx, term):
	url = f"https://api.urbandictionary.com/v0/define?term={term}"
	response = requests.get(url).json()
	if "list" in response:
		if response["list"]:
			definition = response["list"][0]["definition"]
			example = response["list"][0]["example"]
			
			#await ctx.send(f"**{term}**:\n\n{definition}\n\n*Esempio:* {example}")
			embed = discord.Embed(title=" :notebook_with_decorative_cover: Dictionary :notebook_with_decorative_cover: ", colour=discord.Colour.green())
			embed.add_field(name="Definition", value=f"{definition}", inline=False)
			embed.add_field(name="Example", value=f"{example}", inline=False)
			embed.set_footer(text=footer_testo)
			await ctx.send(embed=embed)
		else:
			embed = discord.Embed(title="Error: No definitions found for the specified word or phrase", color=discord.Color.red())
			embed.set_footer(text=footer_testo)
			await ctx.send(embed=embed)
	else:
		embed = discord.Embed(title="Error: An error occurred while searching for the definition", color=discord.Color.red())
		embed.add_field(name="Please report the bug using:", value="</reportbug:1093483925533368361>", inline=True)
		embed.set_footer(text=footer_testo)
		await ctx.send(embed=embed)





@client.command()
@commands.guild_only()
@commands.cooldown(1, 5, commands.BucketType.user)
async def custom_emoji_info(ctx, emoji: discord.Emoji = None):
	if not emoji:
		embed = discord.Embed(title="Error\nPlease send a valid emoji", colour=discord.Colour.red())
		embed.set_footer(text=footer_testo)
		await ctx.send(embed=embed)
	else:
		response_emoji = await emoji.guild.fetch_emoji(emoji.id)
		
		is_managed = "Yes" if response_emoji.managed else "No" 
		is_animated = "Yes" if response_emoji.animated else "No"
		requires_colons = "Yes" if response_emoji.require_colons else "No"
		creation_time = response_emoji.created_at.strftime("%b %d %Y")
		can_use_emoji = "Everyone" if not response_emoji.roles else "".join(role.name for role in response_emoji.roles)
		name = response_emoji.name
		id_emoji = response_emoji.id

		embed = discord.Embed(title="Emoji - Info", colour=discord.Colour.blue())
		embed.add_field(name=":scroll: Name", value=f"`{name}`", inline=True)
		embed.add_field(name=":id: Id", value=f"`{id_emoji}`", inline=True)
		embed.add_field(name=":camera: Url", value=f"[Emoji Url]({response_emoji.url})", inline=True)

		embed.add_field(name=":page_facing_up: Guild name", value=f"`{response_emoji.guild.name}`", inline=True)
		embed.add_field(name=":busts_in_silhouette: Author", value=f"`{response_emoji.user.name}`", inline=True)
		embed.add_field(name=":calendar: Time Created", value=f"`{creation_time}`", inline=True)

		embed.add_field(name="Animated", value=f"`{is_animated}`", inline=True)
		embed.add_field(name="Managed", value=f"`{is_managed}`", inline=True)
		embed.add_field(name="Requires colons", value=f"`{requires_colons}`", inline=True)

		embed.add_field(name=":busts_in_silhouette: Usable by", value=f"`{can_use_emoji}`", inline=False)

		embed.set_footer(text=footer_testo)
		embed.set_thumbnail(url=response_emoji.url)
		await ctx.send(embed=embed)
		

@commands.cooldown(1, 20, commands.BucketType.user)
@commands.guild_only()
@client.command()
async def generate_image(ctx, *, request: str):
	#ETA = int(time.time() + 60)
	embed = discord.Embed(title=f"Loading the image...", colour=discord.Color.blue())
	embed.set_footer(text=footer_testo)
	msg = await ctx.send(embed=embed)
	async with ctx.typing():
		try:
			seed = random.randint(1, 1000)
			image_url = f"https://image.pollinations.ai/prompt/{request}?seed={seed}"
			async with aiohttp.ClientSession() as session:
				async with session.get(image_url) as response:
					if response.status == 200:
						image_data = await response.read()
						image_io = io.BytesIO(image_data)
						await msg.delete()
						file = discord.File(image_io, "generatedImage.png")
						#file = discord.File(resp, "generatedImage.png")
						image_embed = discord.Embed(title=f"Request: ```{request}```", colour=discord.Color.green())
						image_embed.set_image(url="attachment://generatedImage.png")
						image_embed.set_footer(text=footer_testo)
						await ctx.send(file=file, embed=image_embed)
						#await ctx.send("Here's the generated image:", file=discord.File(image, "generatedImage.png"))
					else:
						response_text = await resp.text()
						embed = discord.Embed(title="Error: Unknow", color=discord.Color.red())
						embed.set_footer(text=footer_testo)
						await ctx.send(embed=embed, delete_after=4)
						#error-chat
						channel = client.get_channel(errorchannel)
						response_text = await resp.text()
						embed = discord.Embed(title=f"**[Errore]** \nisinstance:\nText: {response_text}", color=discord.Color.red())
						await channel.send(embed=embed)
		except aiohttp.ContentTypeError as e:
				embed = discord.Embed(title="Error: Unknow", color=discord.Color.red())
				embed.set_footer(text=footer_testo)
				await ctx.send(embed=embed, delete_after=4)
				#error-chat
				channel = client.get_channel(errorchannel)
				response_text = await resp.text()
				embed = discord.Embed(title=f"**[Errore]** \nisinstance: ```{e}```\nerror: ```{str(e)}```\nText: {response_text}", color=discord.Color.red())
				await channel.send(embed=embed)


#------------Verify-------#

@client.tree.command(name="verifydelete", description = "Delete the verification system in the server") #slash command
async def delverify(interaction: discord.Interaction):
	if interaction.user.guild_permissions.manage_roles:
		if not discord.utils.get(interaction.guild.roles, name="verify"):
			embed2 = discord.Embed(title="The verify role does not exist on this server", color=discord.Color.blue())
			embed2.set_footer(text=footer_testo)
			await interaction.response.send_message(embed=embed2, ephemeral=True)
		elif discord.utils.get(interaction.guild.roles, name="verify"):
			embed = discord.Embed(title="I deleted the verify role", color=discord.Color.blue())
			embed.set_footer(text=footer_testo)
			await interaction.response.send_message(embed=embed, ephemeral=True)
			#role delete
			role = discord.utils.get(interaction.guild.roles, name="verify")
			everyone_role = interaction.guild.default_role
			for channel in interaction.guild.channels:
				overwrites = channel.overwrites_for(role)
				if overwrites.view_channel is True:
					await channel.set_permissions(everyone_role, view_channel=True)
					await channel.set_permissions(role, view_channel=None)
			# del the role
			for channel in interaction.guild.channels:
				overwrites = channel.overwrites_for(role)
				if overwrites.view_channel is True:
					return
			await role.delete()
			def check(msg):
				return msg.author == client.user
			await interaction.channel.purge(limit=100, check=check)
	else:
		embed_e = discord.Embed(title='Error: You need the permission to use this command `"manage roles"`', color=discord.Color.red())
		embed_e.set_footer(text=footer_testo)
		await interaction.response.send_message(embed=embed_e, ephemeral=True)




@client.tree.command(name="verifysetup", description = "Set up the system for verification on the server") #slash command
async def verify(interaction: discord.Interaction):
	if interaction.user.guild_permissions.manage_roles:
		embed = discord.Embed(title="Setup Verify", description="You need to press the first two buttons if you have never set up this verification system on your server", color=discord.Color.blue())
		embed.add_field(name="Press the green button to add the verify role in the server\nand set this channel as verify channel", value=":green_circle:",inline=True)
		#embed.add_field(name="Press the blue button to send the message to verify", value=":blue_circle:",inline=True)
		embed.add_field(name="\n\nUse this command to delete the Verify system in the server:", value="/verifydelete",inline=False)
		embed.set_footer(text=footer_testo)
		await interaction.response.send_message(embed=embed, ephemeral=True, view=Verify_Button())
	else:
		embed = discord.Embed(title='Error: You need the permission to use this command `"manage roles"`', color=discord.Color.red())
		embed.set_footer(text=footer_testo)
		await interaction.response.send_message(embed=embed, ephemeral=True)

	



@client.command()
async def captcha(ctx):
	if not discord.utils.get(ctx.guild.roles, name="verify"):
		await ctx.message.delete()
		i_e_embed = discord.Embed(title=" :no_entry_sign: Error: Verify has not been set :no_entry_sign: ", colour=discord.Color.red())
		if ctx.author.guild_permissions.manage_roles:
			i_e_embed.add_field(name="Set up Verify using:", value="</verifysetup:0000>", inline=True) #verifysetup id
		i_e_embed.set_footer(text=footer_testo)
		await ctx.send(embed=i_e_embed, delete_after=4)
		return
	if discord.utils.get(ctx.guild.roles, name="verify") in ctx.author.roles:
		await ctx.message.delete()
		v_e_embed = discord.Embed(title=" :x: You have already been verified :x: ", colour=discord.Color.red())
		v_e_embed.set_footer(text=footer_testo)
		await ctx.send(embed=v_e_embed, delete_after=4)
		return
	image = Image.new('RGB', (350, 100), (255, 255, 255))
	draw = ImageDraw.Draw(image)
	text = random.choice(["J3PKL2", "8QGT2V", "T3FWR6", "VF7NY2", "UPA2XZ", "I5CYWJ", "BVT6NC"])
	font = ImageFont.truetype("captcha.ttf", 60)
	draw.text((80, 25), text, font=font, fill=(0, 0, 0))
	buffer = io.BytesIO()
	image.save(buffer, format='PNG')
	buffer.seek(0)
	file = discord.File(buffer, filename='captcha.png')
	#file = discord.File(resp, "generatedImage.png")
	image_embed = discord.Embed(title=" :robot: Captcha :white_check_mark: ", colour=discord.Color.green())
	image_embed.add_field(name=" :warning: Warning :warning: ", value="All characters must be written in capital letters", inline=True)
	image_embed.set_image(url="attachment://captcha.png")
	image_embed.set_footer(text="Write the characters in the image")
	start_embed = await ctx.send(file=file, embed=image_embed)
	await asyncio.sleep(1)
	await ctx.message.delete()

	def check(m: discord.Message):
		return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id
	
	try:
		response = await client.wait_for('message', check=check, timeout=15.0)
		#print(response.content)
		#print(text)
		if response.content == text:
			await response.delete()
			await start_embed.delete()
			c_embed = discord.Embed(title=" :white_check_mark: Correct CAPTCHA :white_check_mark: ", colour=discord.Color.green())
			c_embed.set_footer(text=footer_testo)
			c_edit = await ctx.send(embed=c_embed, delete_after=2)
			await asyncio.sleep(3)
			if discord.utils.get(ctx.guild.roles, name="verify"):
				if not discord.utils.get(ctx.guild.roles, name="verify") in ctx.author.roles:
					role = discord.utils.get(ctx.guild.roles, name="verify")
					await ctx.author.add_roles(role)
				else:
					error1_embed = discord.Embed(title="Error: Unknown", color=discord.Color.red())
					error1_embed.add_field(name="Please report the bug using:", value="</reportbug:1093483925533368361>", inline=True)
					error1_embed.set_footer(text=footer_testo)
					await c_edit.edit(embed=error1_embed, delete_after=3)
			else:
				error2_embed = discord.Embed(title="Error: Verify has not been set", color=discord.Color.red())
				error2_embed.add_field(name="Set up Verify using:", value="</verifysetup:0000>", inline=True) #verifysetup id
				error2_embed.set_footer(text=footer_testo)
				await c_edit.edit(embed=error2_embed, delete_after=3)
		else:
			await response.delete()
			await start_embed.delete()
			w_embed = discord.Embed(title=" :x: Wrong CAPTCHA :x: ", colour=discord.Color.red())
			w_embed.set_footer(text=footer_testo)
			await ctx.send(embed=w_embed, delete_after=5)
	except asyncio.TimeoutError:
			await start_embed.delete()
			t_embed = discord.Embed(title=f" :clock2: You have run out of time to answer the CAPTCHA.\nPlease try again :clock2: ", colour=discord.Color.gold())
			t_embed.set_footer(text=footer_testo)
			await ctx.send(embed=t_embed, delete_after=5)
	except Exception as e:
			error3_embed = discord.Embed(title="Error: Unknown", color=discord.Color.red())
			error3_embed.add_field(name="Set up Verify using:", value="</verifysetup:0000>", inline=True) #verifysetup id
			error3_embed.set_footer(text=footer_testo)
			await ctx.send(embed=error3_embed, delete_after=4)
			channel = client.get_channel(errorchannel)
			await channel.send(f"**[Errore]** captcha/verify \nisinstance: ```{e}```\nerror: ```{str(e)}```")
			raise e



#-------------Ui----------#

#-verify-setup-confierm-button

class Verify_Button(discord.ui.View):
	def __init__(self):
		super().__init__()
		self.value = None

	@discord.ui.button(label="Verify", style=discord.ButtonStyle.green)
	async def Verify_Button1(self, interaction: discord.Interaction, button: discord.ui.Button):
		ctx=interaction
		if discord.utils.get(ctx.guild.roles, name="verify"):
			#if get(message.guild.roles, name="verify"):
			embed_ex=discord.Embed(title="The role already exists on the server", color=discord.Color.red())
			embed_ex.set_footer(text=footer_testo)  
			await interaction.response.send_message(embed=embed_ex, ephemeral=True)
		else:
			permissions = discord.Permissions(send_messages=True, read_messages=True) #da-cambiare
			guild = interaction.guild
			await guild.create_role(name="verify", colour=discord.Colour(0x00ff00), permissions=permissions)
			role = discord.utils.get(ctx.guild.roles, name="verify")
			#all channel no-private set verify can see - everyone
			#message ephereal
			embed_m_f=discord.Embed(title="I have set up the Verify role on the server.\nI set this channel to be the one where people can Verify", color=discord.Color.green())
			embed_m_f.set_footer(text=footer_testo)
			await interaction.response.send_message(embed=embed_m_f, ephemeral=True)
			await asyncio.sleep(2)
			#message visible
			embed_ex=discord.Embed(title="To become verified run the `?captcha` command", color=discord.Color.green())
			embed_ex.set_footer(text=footer_testo) 
			channel = interaction.channel
			await channel.send(embed=embed_ex)
			await asyncio.sleep(0.5)
			#set role
			for channel in ctx.guild.channels:
				overwrites = channel.overwrites_for(ctx.guild.default_role)
				if overwrites.is_empty() or overwrites.view_channel is None or overwrites.view_channel:
					role_overwrites = channel.overwrites_for(role)
					role_overwrites.view_channel = True
					await channel.set_permissions(role, overwrite=role_overwrites)
					everyone_overwrites = channel.overwrites_for(ctx.guild.default_role)
					everyone_overwrites.view_channel = False
					await channel.set_permissions(ctx.guild.default_role, overwrite=everyone_overwrites)
					#verify_channel can be seen
					channel_v = interaction.channel
					role_v_e = discord.utils.get(ctx.guild.roles, name="@everyone")
					role_v_v = discord.utils.get(ctx.guild.roles, name="verify")
					permissions_v_e = discord.PermissionOverwrite(view_channel=True)
					permissions_v_v = discord.PermissionOverwrite(view_channel=False)
					await channel_v.set_permissions(role_v_e, overwrite=permissions_v_e)
					await channel_v.set_permissions(role_v_v, overwrite=permissions_v_v)



#-ReportBug

class BugModal(ui.Modal, title='Report Bug'):
    bug_name = ui.TextInput(label='Bugged Command name',required=True,placeholder='Bugged command name...', max_length=50)
    #options = [discord.SelectOption(label='Option 1', value='1'), discord.SelectOption(label='Option 2', value='2')]
    #type_of_bug = ui.Select(placeholder="Bug Type", min_values=1, max_values=1, options=options)
    answer = ui.TextInput(label='Description of the bug', style=discord.TextStyle.paragraph, max_length=300,placeholder='Bug description...')

    async def on_submit(self, interaction: discord.Interaction):
        channel = client.get_channel(1043931423360430190)
        embed = discord.Embed(title=":bug: Bug report :bug:")
        embed.add_field(name="Bugged Command name", value=self.children[0].value)
        #embed.add_field(name="Type of bug", value=self.children[1].value)
        embed.add_field(name="Description of the bug", value=self.children[1].value)
        embed.add_field(name="User:", value=f"`{interaction.user}`")
        await channel.send(embed=embed)
        embed1 = discord.Embed(title="Bug report sent", color=discord.Color.green())
        embed1.set_footer(text=footer_testo)
        await interaction.response.send_message(embeds=[embed1], ephemeral=True)


			

#-Suggestion
	
class SuggestionModal(ui.Modal, title='Suggest a command'):
    name = ui.TextInput(label='Command name')
    answer = ui.TextInput(label='Description of the command / its functions', style=discord.TextStyle.paragraph)

    async def on_submit(self, interaction: discord.Interaction):
        channel = client.get_channel(1079859774344134686)
        embed = discord.Embed(title="Suggestion Modal Results")
        embed.add_field(name="Command name", value=self.children[0].value)
        embed.add_field(name="Description of the command / its functions", value=self.children[1].value)
        embed.add_field(name="Utente:", value=f"`{interaction.user}`")
        await channel.send(embed=embed)
        embed1 = discord.Embed(title="Suggestion sent", color=discord.Color.green())
        embed1.set_footer(text=footer_testo)
        await interaction.response.send_message(embeds=[embed1], ephemeral=True)


#-Help-
		
class HelpDropdownView(discord.ui.View):
	def __init__(self):
		super().__init__()
		self.add_item(HelpDropdown())
		
class HelpDropdown(discord.ui.Select):
	def __init__(self):
		options = [discord.SelectOption(label='Mod Commands', emoji='🔐'), discord.SelectOption(label='Utilty Commands', emoji='📉'), discord.SelectOption(label='Fun Commands', emoji='🎉'), discord.SelectOption(label='Slash Commands', emoji='💻')]
		
		super().__init__(placeholder='Choose help section...', min_values=1, max_values=1, options=options)

	async def callback(self, interaction: discord.Interaction):
		prefix = data["command_prefix"]
		if self.values[0] == "Mod Commands":
			embed = discord.Embed(title="Mod Commands :closed_lock_with_key:", color=discord.Color.gold())
			embed.add_field(name=f"{prefix}nuke", value=f"Delete messages in the chat where it is used", inline=True)
			embed.add_field(name=f"{prefix}kick `user_id` `reason`", value=f"Kick a member from the server", inline=True)
			embed.add_field(name=f"{prefix}ban `user_id` `reason`", value=f"Ban a member from the server", inline=True)
			embed.add_field(name=f"{prefix}unban `user_id`", value=f"Unban a member from the server", inline=True)
			embed.add_field(name=f"{prefix}delchannel", value=f"Delete all channel", inline=True)
			embed.add_field(name=f"{prefix}lockdown", value=f"Lockdown the channel", inline=True)
			embed.add_field(name=f"{prefix}unlock", value=f"Unlock the channel", inline=True)
			embed.add_field(name=f"{prefix}mute `user_id`", value=f"Mute a member", inline=True)
			embed.add_field(name=f"{prefix}unmute `user_id`", value=f"Unmute a member", inline=True)
			embed.add_field(name=f"{prefix}slowmode `seconds`", value=f"Set the slowmode of the channel", inline=True)
			embed.set_footer(text=footer_testo)
			await interaction.response.send_message(embed=embed, ephemeral=True)
		elif self.values[0] == "Utilty Commands":
			embedt = discord.Embed(title="Utilty :chart_with_downwards_trend:", color=discord.Color.green())
			embedt.add_field(name=f"{prefix}infobot", value="Send the bot stats (cpu, memory, ping)", inline=True)
			embedt.add_field(name=f"{prefix}serverinfo", value="Send the Server info", inline=True)
			embedt.add_field(name=f"{prefix}userinfo `user_id`", value="Send the User info", inline=True)
			embedt.add_field(name=f"{prefix}translate `language` `text`", value="Translates text into any supported language", inline=True)
			embedt.add_field(name=f"{prefix}custom_emoji_info `custom_emoji`", value="Tells you the information of a custom emoji", inline=True)
			embedt.add_field(name=f"{prefix}dictionary `word`", value="Tells you the meaning of a word", inline=True)
			embedt.set_footer(text=footer_testo)
			await interaction.response.send_message(embed=embedt, ephemeral=True)
		elif self.values[0] == "Fun Commands":
			embedd = discord.Embed(title="Fun Commands :tada:", color=discord.Color.blurple())
			embedd.add_field(name=f"{prefix}meme", value="Send a random meme", inline=True)
			embedd.add_field(name=f"{prefix}casual", value="Extracts Yes or No", inline=True)
			embedd.add_field(name=f"{prefix}coinflip", value="Extracts heads or tails", inline=True)
			embedd.add_field(name=f"{prefix}num_extractor", value="Extracts a number from 1 to 10", inline=True)
			embedd.add_field(name=f"{prefix}generate_image `request`", value="Generate an image", inline=True)
			#embedd.add_field(name=f"{prefix}activity", value="Send the No-Nitro and the Nitro Activity", inline=True)
			embedd.set_footer(text=footer_testo)
			await interaction.response.send_message(embed=embedd, ephemeral=True)
		elif self.values[0] == "Slash Commands":
			embed = discord.Embed(title="Slash command :computer:", color=discord.Color.blurple())
			embed.add_field(name="</help:1094994368445816934>", value="This command", inline=True)
			embed.add_field(name="</reportbug:1093483925533368361>", value="Report a Ultimate-Bot Bug", inline=True)
			embed.add_field(name="</suggestion:1079857792095105044>", value="Send a suggestion for Ultimate-Bot", inline=True)
			embed.add_field(name="</giveaway:1096547565601828946>", value="Make a giveaway for all member in a server", inline=True)
			embed.add_field(name="</play:1114559886995509268>", value="Play a song", inline=True)
			embed.add_field(name="</stop:1114604126861525132>", value="Stop a song", inline=True)
			embed.add_field(name="</volume:1114604126861525133>", value="Set the volume of a song", inline=True)
			embed.add_field(name="</verifydelete:1165565902633324545>", value="Delete the verification system in the server", inline=True)
			embed.add_field(name="</verifysetup:1165565902633324546>", value="Create the verification system in the server", inline=True)
			embed.set_footer(text=footer_testo)
			await interaction.response.send_message(embed=embed, ephemeral=True)

		

#-Manutenzione
		
class Admin_Button_View(discord.ui.View):
	def __init__(self):
		super().__init__()
		self.value = None

	@discord.ui.button(label="Off", style=discord.ButtonStyle.red)
	async def Off_Amin_Button(self, interaction: discord.Interaction, button: discord.ui.Button):
		if interaction.user.id in my_id:
			change_status.start()
			embed = discord.Embed(title="Maintenance Mod Off", color=discord.Color.red())
			embed.set_footer(text=footer_testo)
			await interaction.response.send_message(embed=embed, ephemeral=True)
		else:
			embed = discord.Embed(title=f"Error\nYou are not Admin", color=discord.Color.red())
			embed.set_footer(text=footer_testo)
			await interaction.response.send_message(embed=embed, ephemeral=True)
			
	@discord.ui.button(label="On", style=discord.ButtonStyle.green)
	async def On_Amin_Button(self, interaction: discord.Interaction, button: discord.ui.Button):
		if interaction.user.id in my_id:
			change_status.cancel()
			await asyncio.sleep(2)
			await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name=f"maintenance"))
			embed = discord.Embed(title="Maintenance Mod On", color=discord.Color.red())
			embed.set_footer(text=footer_testo)
			await interaction.response.send_message(embed=embed, ephemeral=True)
		else:
			embed = discord.Embed(title=f"Error\nYou are not Admin", color=discord.Color.red())
			embed.set_footer(text=footer_testo)
			await interaction.response.send_message(embed=embed, ephemeral=True)


#-Traslate	
		
class TraslateButton(discord.ui.View):
	def __init__(self):
		super().__init__()
		self.value = None

	@discord.ui.button(label="List of language", style=discord.ButtonStyle.red)
	async def TraslateButton(self, interaction: discord.Interaction, button: discord.ui.Button):
		lingue_supportate = GoogleTranslator().get_supported_languages()
		#embed_traslate=discord.Embed(title=f"***```{lingue_supportate}```***", color=discord.Color.green())
		#embed_traslate.set_footer(text=footer_testo)
		await interaction.response.send_message(f"***```{lingue_supportate}```***", ephemeral=True)
		
		

#------------Slash------------#




@client.tree.command(name="help", description = "Show the list of command for Ultimate-Bot")
async def help(interaction: discord.Interaction):
	if interaction.user.id == my_id:
		prefix = data["command_prefix"]
		admin_embed = discord.Embed(title="Admin Command :money_with_wings:", color=discord.Color.blue())
		admin_embed.add_field(name=f"{prefix}update", value="Update Bot code", inline=True)
		admin_embed.add_field(name=f"{prefix}slash_sync", value="Sync tree command", inline=True)
		admin_embed.add_field(name=f"{prefix}verify", value="In test", inline=True)
		admin_embed.add_field(name=f"{prefix}manutenzione", value="Cambia status al bot", inline=True)
		admin_embed.set_footer(text=footer_testo)
		command_list = []
		for command in client.commands:
			command_list.append(f"Nome: {command.name} - Descrizione: {command.description} - Utilizzo: {command.usage}")
		message = "\n".join(command_list)
		await interaction.response.send_message(f'{message}\n\nSelect the help command section:', view=HelpDropdownView(), embed=admin_embed, ephemeral=True)
	else:
		#view = HelpDropdownView()
		await interaction.response.send_message( view=HelpDropdownView(), ephemeral=True)

#----Ticket---start


class TicketModal(ui.Modal, title='Ticket message'):
	title_name = ui.TextInput(label='Message Title',required=True,placeholder='Message title...', max_length=50)
	description_name = ui.TextInput(label='Message Description',required=True, style=discord.TextStyle.paragraph, max_length=300,placeholder='Use ?ticket to use a ticket...')
	async def on_submit(self, interaction: discord.Interaction):
		channel = interaction.channel
		embed = discord.Embed(title=f"{self.children[0].value}",description=f"{self.children[1].value}", color=discord.Color.green())
		await channel.send(embed=embed)
		channel_id = interaction.channel.id
		with open('ticket_channels.json', 'r') as f:
			channels = json.load(f)
		channels[str(channel_id)] = True
		with open('ticket_channels.json', 'w') as f:
			json.dump(channels, f)
		embed_r = discord.Embed(title='The verification system has been set up', color=discord.Color.green())
		embed_r.set_footer(text=footer_testo)
		await interaction.response.send_message(embed=embed_r, ephemeral=True)


class Ticket_Button(discord.ui.View):
	def __init__(self):
		super().__init__()
		self.value = None

	@discord.ui.button(label="Add", emoji="➕", style=discord.ButtonStyle.green)
	async def Ticket_add(self, interaction: discord.Interaction, button: discord.ui.Button):
		await interaction.response.send_modal(TicketModal())



	@discord.ui.button(label="Remove",emoji="➖", style=discord.ButtonStyle.red)
	async def Ticket_remove(self, interaction: discord.Interaction, button: discord.ui.Button):
		channel_id = interaction.channel.id
		with open('ticket_channels.json', 'r') as f:
			channels = json.load(f)
		if str(channel_id) in channels:
			del channels[str(channel_id)]
		with open('ticket_channels.json', 'w') as f:
			json.dump(channels, f)
		embed = discord.Embed(title=f'The verification system in the channel: <#{channel_id}> as been removed', color=discord.Color.red())
		embed.set_footer(text=footer_testo)
		await interaction.response.send_message(embed=embed, ephemeral=True)
		def check(msg):
			return msg.author == client.user
		await interaction.channel.purge(limit=100, check=check)


@client.tree.command(name="ticketsetup", description = "Set up the ticket system on the server") #slash command
async def ticketsetup(interaction: discord.Interaction):
	if interaction.user.guild_permissions.manage_roles:
		embed = discord.Embed(title="Ticket System Setup", color=discord.Color.blue())
		embed.add_field(name="Press add to add the Ticket system in this channel", value=":green_circle:",inline=True)
		embed.add_field(name="\nPress remove to remove the Ticket system from this channel", value=":red_circle:",inline=True)
		embed.set_footer(text=footer_testo)
		await interaction.response.send_message(embed=embed, ephemeral=True, view=Ticket_Button())
	else:
		embed = discord.Embed(title='Error: You need the permission to use this command `"manage roles"`', color=discord.Color.red())
		embed.set_footer(text=footer_testo)
		await interaction.response.send_message(embed=embed, ephemeral=True)
          



@client.command()
async def ticket(ctx):
	await ctx.message.delete()
	with open('ticket_channels.json', 'r') as f:
		channels = json.load(f)

	if str(ctx.channel.id) in channels:
		guild = ctx.guild
		ticket_channel = await guild.create_text_channel(name=f'ticket-{ctx.author.name}')
		await ticket_channel.set_permissions(guild.get_role(guild.id), send_messages=False, read_messages=False)
		await ticket_channel.set_permissions(ctx.author, attach_files=True, send_messages=True, read_messages=True, read_message_history=True, add_reactions=True)
		for role in guild.roles:
			if role.permissions.manage_roles:
				await ticket_channel.set_permissions(role, attach_files=True, send_messages=True, read_messages=True, read_message_history=True, add_reactions=True)
		embed = discord.Embed(title=f'`{ctx.author.name}` ***Ticket***\n\nFor the admin: Use ?close to close the ticket', color=discord.Color.blue())
		embed.set_footer(text=footer_testo)
		await ticket_channel.send(embed=embed)
	else:
		embed = discord.Embed(title=f'Error: This channel has not been set to initiate tickets', color=discord.Color.red())
		embed.set_footer(text=footer_testo)
		await ctx.send(embed=embed,delete_after=5)


		
@client.command()
async def close(ctx):
	if ctx.author.guild_permissions.manage_roles:
		if 'ticket-' in ctx.channel.name:
			embed = discord.Embed(title='The ticket will be closed in 5 seconds', color=discord.Color.dark_blue())
			await ctx.send(embed=embed)
			await asyncio.sleep(5)
			await ctx.channel.delete()
		else:
			await ctx.message.delete()
			embed = discord.Embed(title=f'Error: This channel is not a ticket', color=discord.Color.red())
			embed.set_footer(text=footer_testo)
			await ctx.send(embed=embed,delete_after=5)
	else:
		await ctx.message.delete()
		embed = discord.Embed(title='Error: You need the permission to use this command `"manage roles"`', color=discord.Color.red())
		embed.set_footer(text=footer_testo)
		await ctx.send(embed=embed,delete_after=5)    

		embed = discord.Embed(title='Error: You need the permission to use this command `"manage roles"`', color=discord.Color.red())
		embed.set_footer(text=footer_testo)


#----Ticket---stop

#----Automod---start


#automod d



@client.tree.command(name="automod_delete", description = "Delete an AutoMod rule from the server")
async def automod_delete(interaction: discord.Interaction):
	try:
		rules = await interaction.guild.fetch_automod_rules()
		rule_opf = []
		for rule in rules:
			rule_op = discord.SelectOption(label=str(rule.name))  # Convert rule.name to string
			rule_opf.append(rule_op)
		view = Automod_D_Dropdown_View(rule_opf)
		embed = discord.Embed(title='Choose the Automod rule to delete', color=discord.Color.red())
		await interaction.response.send_message(embed=embed, view=view, ephemeral=True)
	except Exception as e:
		if "In data.components.0.components.0.options:" in str(e):
			embed = discord.Embed(title="Error: There are no automod rules in the server", color=discord.Color.red())
			embed.set_footer(text=footer_testo)
			await interaction.response.send_message(embed=embed, ephemeral=True)
		else:
			embed = discord.Embed(title="Error: Unknown", color=discord.Color.red())
			embed.add_field(name="Please report the bug using:", value="</reportbug:1093483925533368361>", inline=True)
			embed.set_footer(text=footer_testo)
			await interaction.response.send_message(embed=embed, ephemeral=True)
			#error-chat
			channel = client.get_channel(errorchannel)
			await channel.send(f"**[Errore]** \nisinstance: ```{isinstance}```\nerror: ```{str(e)}```")
			raise e



class Automod_D_Dropdown_View(discord.ui.View):
	def __init__(self, options):
		super().__init__()
		self.add_item(Automod_D_Dropdown(options))


class Automod_D_Dropdown(discord.ui.Select):
	def __init__(self, options):
		super().__init__(placeholder='Choose the Automod rule...', min_values=1, max_values=1, options=options)

	async def callback(self, interaction: discord.Interaction):
		try:
			rules = await interaction.guild.fetch_automod_rules()
			for rule in rules:
				if self.values[0] == rule.name:
					await rule.delete()
					embed = discord.Embed(title=f'I deleted `{rule.name}`', color=discord.Color.red())
					await interaction.response.edit_message(embed=embed, view=None)
		except Exception as e:
			if "In data.components.0.components.0.options:" in str(e):
				embed = discord.Embed(title="Error: There are no automod rules in the server", color=discord.Color.red())
				embed.set_footer(text=footer_testo)
				await interaction.response.send_message(embed=embed, ephemeral=True)
			else:
				embed = discord.Embed(title="Error: Unknown", color=discord.Color.red())
				embed.add_field(name="Please report the bug using:", value="</reportbug:1093483925533368361>", inline=True)
				embed.set_footer(text=footer_testo)
				await interaction.response.send_message(embed=embed, ephemeral=True)
				#error-chat
				channel = client.get_channel(errorchannel)
				await channel.send(f"**[Errore]** \nisinstance: ```{isinstance}```\nerror: ```{str(e)}```")
				raise e



#automod c

@client.tree.command(name="automod_create", description = "Adds AutoMod rules to the server")
@app_commands.describe(type='The type of rule you want', timeout_time='The time the person violating the rule will be put in timeout', log_channel="The channel where alerts will be sent when someone violates a rule")
async def automod_create(interaction: discord.Interaction, type: Literal['Spam', 'Mention Spam', 'Custom Keyword', 'Keyword Preset'], timeout_time: Literal['60 sec', '5 min.','10 min.', '1 hour', '1 day', '1 week'], log_channel: discord.TextChannel):
	if interaction.user.guild_permissions.manage_messages:
		time_value = {
			"60 sec": timedelta(seconds=60),
			"5 min.": timedelta(minutes=5),
			"10 min.": timedelta(minutes=10),
			"1 hour": timedelta(hours=1),
			"1 day": timedelta(days=1),
			"1 week": timedelta(weeks=1)
		}
		embed = discord.Embed(title=f'I created a `{type}` rule in automod, the timeout time is `{timeout_time}` , the log channel is `#{log_channel}`', color=discord.Color.green())
		embed.set_footer(text=footer_testo)
		if timeout_time in time_value:
			time = time_value[timeout_time]
			try:
				if type == 'Custom Keyword':
					global timeout_time_f
					global time_f
					global log_channel_f
					timeout_time_f = timeout_time
					time_f = time
					log_channel_f = log_channel
					await interaction.response.send_modal(AutomodCustom_Keyword_Modal())
				elif type == 'Spam':
					actions = [
						discord.AutoModRuleAction(),
						discord.AutoModRuleAction(channel_id=log_channel.id),
						]
					await interaction.guild.create_automod_rule(
						name="Spam Rule",
						event_type=discord.AutoModRuleEventType.message_send,
						trigger=discord.AutoModTrigger(
						type=discord.AutoModRuleTriggerType.spam
						),
						enabled=True,
						actions=actions
					)
					await interaction.response.send_message(embed=embed, ephemeral=True)
				elif type == 'Mention Spam':
					actions = [
						discord.AutoModRuleAction(),
						discord.AutoModRuleAction(channel_id=log_channel.id),
						discord.AutoModRuleAction(duration=time),
						discord.AutoModRuleAction(custom_message=">>> **You are sending too many mentions**")
						]
					await interaction.guild.create_automod_rule(
						name="Mention Spam Rule",
						event_type=discord.AutoModRuleEventType.message_send,
						trigger=discord.AutoModTrigger(
						type=discord.AutoModRuleTriggerType.mention_spam, mention_limit=5
						),
						enabled=True,
						actions=actions
					)
					await interaction.response.send_message(embed=embed, ephemeral=True)
				elif type == 'Keyword Preset':
					global timeout_time_d
					global time_d
					global log_channel_d
					timeout_time_d = timeout_time
					time_d = time
					log_channel_d = log_channel
					embed_key = discord.Embed(title=f'Select a Keyword preset for the rule', color=discord.Color.blue())
					embed_key.set_footer(text="\nWarning:\nIn the Keyword preset the isn't a timeout time because the message will be blocked")
					await interaction.response.send_message(embed=embed_key, view=AutomodKeyword_Preset_Dropdown_View(), ephemeral=True)
			except Exception as e:
				if "AUTO_MODERATION_MAX_RULES_OF_TYPE_EXCEEDED" in str(e):
					embed = discord.Embed(title="Error: Auto-mod Max Rules of this type\n\nYou have reached the maximum number of rules of this type", color=discord.Color.red())
					embed.set_footer(text=footer_testo)
					await interaction.response.send_message(embed=embed, ephemeral=True)
				else:
					embed = discord.Embed(title="Error: Unknown", color=discord.Color.red())
					embed.add_field(name="Please report the bug using:", value="</reportbug:1093483925533368361>", inline=True)
					embed.set_footer(text=footer_testo)
					await interaction.response.send_message(embed=embed, ephemeral=True)
					#error-chat
					channel = client.get_channel(errorchannel)
					await channel.send(f"**[Errore]** \nisinstance: ```{isinstance}```\nerror: ```{str(e)}```")
					raise e
	else:
		embed = discord.Embed(title="Error: You need the permission to use this command (`manage_messages`)", color=discord.Color.red())
		embed.set_footer(text=footer_testo)
		await interaction.response.send_message(embed=embed, ephemeral=True)
		



class AutomodCustom_Keyword_Modal(ui.Modal, title='AutoMod Customod Keyword'):
	w1 = ui.TextInput(label='First word',required=True,placeholder='A bad word...', max_length=50)
	w2 = ui.TextInput(label='Second word',required=False,placeholder='A bad word...', max_length=50)
	w3 = ui.TextInput(label='Third word',required=False,placeholder='A bad word...', max_length=50)
	w4 = ui.TextInput(label='Fourth word',required=False,placeholder='A bad word...', max_length=50)
	w5 = ui.TextInput(label='Fifth word',required=False,placeholder='A bad word...', max_length=50)

	async def on_submit(self, interaction: discord.Interaction):
		try:
			global timeout_time_f
			global time_f
			global log_channel_f
			timeout_time = timeout_time_f
			time = time_f
			log_channel = log_channel_f
			type = "Custom Keyword"

			w1_f = self.children[0].value
			w2_f = self.children[1].value
			w3_f = self.children[2].value
			w4_f = self.children[3].value
			w5_f = self.children[4].value
			w_c_d = [f"{w1_f}" if w1_f is not None else None,
				f"{w2_f}" if w2_f is not None else None,
				f"{w3_f}" if w3_f is not None else None,
				f"{w4_f}" if w4_f is not None else None,
				f"{w5_f}" if w5_f is not None else None]

			# Rimuovi gli elementi None da w_c
			w_c = [f"*{item}*" if item is not None else None for item in w_c_d]
			time_value = {
				w1_f: timedelta(seconds=60),
				w2_f: timedelta(minutes=5),
				w3_f: timedelta(minutes=10),
				w4_f: timedelta(hours=1),
				w5_f: timedelta(days=1)
			}
			print(w_c)
			actions = [
				discord.AutoModRuleAction(),
				discord.AutoModRuleAction(channel_id=log_channel.id),
				discord.AutoModRuleAction(duration=time),
				]
			await interaction.guild.create_automod_rule(
				name="Custom Keywords Rule",
				event_type=discord.AutoModRuleEventType.message_send,
				trigger=discord.AutoModTrigger(
				type=discord.AutoModRuleTriggerType.keyword, keyword_filter=w_c
				),
				enabled=True,
				actions=actions
			)

			embed = discord.Embed(title=f'I created a `{type}` rule in automod, the timeout time is `{timeout_time}` , the log channel is `#{log_channel}`', color=discord.Color.green())
			embed.set_footer(text=footer_testo)

			await interaction.response.send_message(embed=embed, ephemeral=True)
		except Exception as e:
			if "AUTO_MODERATION_MAX_RULES_OF_TYPE_EXCEEDED" in str(e):
				embed = discord.Embed(title="Error: Auto-mod Max Rules of this type\n\nYou have reached the maximum number of rules of this type", color=discord.Color.red())
				embed.set_footer(text=footer_testo)
				await interaction.response.send_message(embed=embed, ephemeral=True)
			else:
				embed = discord.Embed(title="Error: Unknown", color=discord.Color.red())
				embed.add_field(name="Please report the bug using:", value="</reportbug:1093483925533368361>", inline=True)
				embed.set_footer(text=footer_testo)
				await interaction.response.send_message(embed=embed, ephemeral=True)
				#error-chat
				channel = client.get_channel(errorchannel)
				await channel.send(f"**[Errore]** \nisinstance: ```{isinstance}```\nerror: ```{str(e)}```")
				raise e




class AutomodKeyword_Preset_Dropdown_View(discord.ui.View):
	def __init__(self):
		super().__init__()
		self.add_item(AutomodKeyword_Preset_Dropdown())


class AutomodKeyword_Preset_Dropdown(discord.ui.Select):
	def __init__(self):
		options = [discord.SelectOption(label='Profanity', emoji='🗣️'), discord.SelectOption(label='Sexual content', emoji='💋'), discord.SelectOption(label='Slurs', emoji='🗨️'), discord.SelectOption(label='All', emoji='📁')]
		super().__init__(placeholder='Choose the automod preset for the keyword...', min_values=1, max_values=1, options=options)

	async def callback(self, interaction: discord.Interaction):
		try:
			type = f"{self.values[0]} keyword preset rule"

			#global -- info
			global timeout_time_d
			global time_d
			global log_channel_d
			timeout_time = timeout_time_d
			time = time_d
			log_channel = log_channel_d

			embed = discord.Embed(title=f"I created a `{type}` rule in automod, there isn't a timeout time for this rule, the log channel is `#{log_channel}`", color=discord.Color.green())
			embed.set_footer(text=footer_testo)
			if self.values[0] == "Profanity":
				actions = [
					discord.AutoModRuleAction(),
					discord.AutoModRuleAction(channel_id=log_channel.id),
					discord.AutoModRuleAction(custom_message=">>> **Profanity messages are not allowed**")
					]
				await interaction.guild.create_automod_rule(
					name="Profanity Rule",
					event_type=discord.AutoModRuleEventType.message_send,
					trigger=discord.AutoModTrigger(
					type=discord.AutoModRuleTriggerType.keyword_preset, presets = discord.AutoModPresets(profanity=True)
					),
					enabled=True,
					actions=actions
				)
				await interaction.response.send_message(embed=embed, ephemeral=True)
			elif self.values[0] == "Sexual content":
				actions = [
					discord.AutoModRuleAction(),
					discord.AutoModRuleAction(channel_id=log_channel.id),
					discord.AutoModRuleAction(custom_message=">>> **Sexual content messages are not allowed**")
					]
				await interaction.guild.create_automod_rule(
					name="Sexual content Rule",
					event_type=discord.AutoModRuleEventType.message_send,
					trigger=discord.AutoModTrigger(
					type=discord.AutoModRuleTriggerType.keyword_preset, presets = discord.AutoModPresets(sexual_content=True)
					),
					enabled=True,
					actions=actions
				)
				await interaction.response.send_message(embed=embed, ephemeral=True)
			elif self.values[0] == "Slurs":
				actions = [
					discord.AutoModRuleAction(),
					discord.AutoModRuleAction(channel_id=log_channel.id),
					discord.AutoModRuleAction(custom_message=">>> **Slurs messages are not allowed**")
					]
				await interaction.guild.create_automod_rule(
					name="Slurs Rule",
					event_type=discord.AutoModRuleEventType.message_send,
					trigger=discord.AutoModTrigger(
					type=discord.AutoModRuleTriggerType.keyword_preset, presets = discord.AutoModPresets(slurs=True)
					),
					enabled=True,
					actions=actions
				)
				await interaction.response.send_message(embed=embed, ephemeral=True)
			elif self.values[0] == "All":
				actions = [
					discord.AutoModRuleAction(),
					discord.AutoModRuleAction(channel_id=log_channel.id),
					discord.AutoModRuleAction(custom_message=">>> **Slurs, Profanity and Sexual content messages are not allowed**")
					]
				await interaction.guild.create_automod_rule(
					name="All Keywords Presets Rule",
					event_type=discord.AutoModRuleEventType.message_send,
					trigger=discord.AutoModTrigger(
					type=discord.AutoModRuleTriggerType.keyword_preset, presets = discord.AutoModPresets.all()
					),
					enabled=True,
					actions=actions
				)
				embed_a = discord.Embed(title=f"I created a rule in automod with all of keywords presets, there isn't a timeout time for this rule, the log channel is `#{log_channel}`", color=discord.Color.green())
				embed_a.set_footer(text=footer_testo)
				await interaction.response.send_message(embed=embed_a, ephemeral=True)
		except Exception as e:
			if "AUTO_MODERATION_MAX_RULES_OF_TYPE_EXCEEDED" in str(e):
				embed = discord.Embed(title="Error: Auto-mod Max Rules of this type\n\nYou have reached the maximum number of rules of this type", color=discord.Color.red())
				embed.set_footer(text=footer_testo)
				await interaction.response.send_message(embed=embed, ephemeral=True)
			else:
				embed = discord.Embed(title="Error: Unknown", color=discord.Color.red())
				embed.add_field(name="Please report the bug using:", value="</reportbug:1093483925533368361>", inline=True)
				embed.set_footer(text=footer_testo)
				await interaction.response.send_message(embed=embed, ephemeral=True)
				#error-chat
				channel = client.get_channel(errorchannel)
				await channel.send(f"**[Errore]** \nisinstance: ```{isinstance}```\nerror: ```{str(e)}```")
				raise e





#----Automod---stop





@client.tree.command(name="reportbug", description="Report a bug of a Ultimate-Bot command") #slash command
async def report_bug(interaction: discord.Interaction):
	modal = BugModal
	await interaction.response.send_modal(BugModal())



@client.tree.context_menu(name="Get Message ID") #message contex command
async def getmessageid(interaction: discord.Interaction, message: discord.Message):
	await interaction.response.send_message(f"***Message ID: ***`{message.id}`", ephemeral=True)


@client.tree.command(name = "suggestion", description = "Suggest a command for Ultimate-Bot") #slash command
async def suggestion(interaction: discord.Interaction):
	#modal = SuggestionModal
	await interaction.response.send_modal(SuggestionModal())

@client.tree.command(name="giveaway", description = "Make a giveaway") #slash command
@app_commands.describe(prize='The prize that you wanna give in giveaway')
async def giveaway(interaction: discord.Interaction, seconds: int, prize: str):
		time = seconds
		if time > 500:
			warning_embed = discord.Embed(title="Error: The max of seconds is 500 (for now)", color=discord.Color.red())
			warning_embed.set_footer(text=footer_testo)
			await interaction.response.send_message(embed=warning_embed, ephemeral=True)
		else:
			if interaction.user.guild_permissions.administrator:
				start_embed = discord.Embed(title=f":tada: Giveaway start in {time} seconds :tada:\nThe prize is `{prize}` :moneybag:", color=0xe91e63)
				await interaction.response.send_message(embed=start_embed)
				await asyncio.sleep(time)
				results = [member for member in interaction.guild.members if not member.bot]
				winner = random.choice(results)
				win_embed = discord.Embed(title=":tada: Giveaway :tada:", color=0xe91e63)
				win_embed.add_field(name="Winner user:", value=f":confetti_ball: `{winner}` :confetti_ball:")
				win_embed.add_field(name="Prize", value=f":gift: ***`{prize}`*** :gift:")
				win_embed.set_footer(text=footer_testo)
				await interaction.edit_original_response(embed=win_embed)
			else:
				embed = discord.Embed(title="Error: You need the permission to use this command", color=discord.Color.red())
				embed.set_footer(text=footer_testo)
				await interaction.response.send_message(embed=embed, ephemeral=True)


@client.tree.context_menu(name="Ban User") #message contex command
async def ban(interaction: discord.Interaction, message: discord.Message):
	if interaction.user.guild_permissions.administrator:
		try:
			target = message.author
		
			# Banna l'utente
			await interaction.guild.ban(target)
		
			# Invia un messaggio di conferma
			embed = discord.Embed(title="The user has been banned!", color=discord.Color.red())
			embed.set_footer(text=footer_testo)
			await interaction.response.send_message(embed=embed, ephemeral=True)
			
		except Exception as e:
			if 'error code: 50013' in str(e):
				embed = discord.Embed(title="Error: I don't have permission to ban this user", color=discord.Color.red())
				embed.set_footer(text=footer_testo)
				await interaction.response.send_message(embed=embed, ephemeral=True)
			else:
				embed = discord.Embed(title="Error: Unknown", color=discord.Color.red())
				embed.add_field(name="Please report the bug using:", value="</reportbug:1093483925533368361>", inline=True)
				embed.set_footer(text=footer_testo)
				await interaction.response.send_message(embed=embed, ephemeral=True)
				channel = client.get_channel(errorchannel)
				await channel.send(f"**[Errore]** \nisinstance: ```{e}```\nerror: ```{str(e)}```")
				raise e
		except discord.ext.commands.errors.MissingPermissions as e:
			embed = discord.Embed(title="Error: I don't have permission to ban", color=discord.Color.red())
			embed.set_footer(text=footer_testo)
			await interaction.response.send_message(embed=embed, ephemeral=True)
	else:
		embed = discord.Embed(title="Error: You need the permission to use this command", color=discord.Color.red())
		embed.set_footer(text=footer_testo)
		await interaction.response.send_message(embed=embed, ephemeral=True)
		
		

@client.tree.context_menu(name="Traslate message") #message contex command
async def traslate(interaction: discord.Interaction, message: discord.Message):
	text = message.content
	lang = "en"
	try:
		if len(text) > 1998:
			embed = discord.Embed(title="Error: The text is too long must not exceed 1998 characters", color=discord.Color.red())
			embed.set_footer(text=footer_testo)
			await interaction.response.send_message(embed=embed, ephemeral=True)
			#await ctx.send(embed=embed, delete_after=4)
		else:
			if len(text) > 1024:
				traduttore = GoogleTranslator(source='auto', target=lang)
				risultato = traduttore.translate(text)
				await interaction.response.send_message(f"```{risultato}```", ephemeral=True)
				#await ctx.send(f"```{risultato}```")
			else:
				traduttore = GoogleTranslator(source='auto', target=lang)
				risultato = traduttore.translate(text)
				embed=discord.Embed(color=discord.Color.green())
				embed.set_footer(text=footer_testo)
				await interaction.response.send_message(embed=embed, content=f"```{risultato}```", ephemeral=True)
	except Exception as e:
		embed = discord.Embed(title="Error: Unknown", color=discord.Color.red())
		embed.set_footer(text=footer_testo)
		await interaction.response.send_message(embed=embed, ephemeral=True)
		#error-chat
		channel = client.get_channel(errorchannel)
		await channel.send(f"**[Errore]** \nisinstance: ```{e}```\nerror: ```{str(e)}```")
		print(e)



@client.tree.command(name="play", description = "Play a song") #slash command
async def play(interaction: discord.Interaction, name: str):
	url = name
	if interaction.user.voice is None:
		embed = discord.Embed(title="*** You are not currently in a voice channel. ***", color=discord.Colour.red())
		embed.set_footer(text=footer_testo)
		await interaction.response.send_message(embed=embed, ephemeral=True)
	else:
		if interaction.guild.voice_client is not None and interaction.guild.voice_client.is_playing():
			no_music_embed = discord.Embed(title="*** Please wait until the song is finished to start another one, If you want to stop the song you can use </stop:1114604126861525132> ***", color=discord.Colour.red())
			no_music_embed.set_footer(text=footer_testo)
			await interaction.response.send_message(embed=no_music_embed, ephemeral=True)
			await asyncio.sleep(0.5)
		else:
			#else:
			try:
				loading_embed = discord.Embed(title=":arrows_clockwise: Downloading song :musical_note:", color=discord.Colour.blue())
				loading_embed.set_footer(text=footer_testo)
				await interaction.response.send_message(embed=loading_embed, ephemeral=True)
				if "playlist?list=" in url:
					error_embed = discord.Embed(title="***Playlists cannot be played***", color=discord.Colour.red())
					error_embed.set_footer(text=footer_testo)
					await interaction.edit_original_response(embed=error_embed)
				else:
					if url.startswith("https://"):
						if url.startswith("https://youtu.be/"):
							share_video_id = url.replace("https://youtu.be/", "")
							share_video_url = "youtube.com/watch?v=" + f"{share_video_id}"



							# Scarica l'audio da YouTube
							yt = pytube.YouTube(share_video_url)
							stream = yt.streams.get_audio_only() #w
							stream_url = stream.url

							channel = interaction.user.voice.channel
							voice_channel = await channel.connect()

							#----FFMPEG_OPTION
			
							#permette la canzone di essere completata quando si ha un delay nell'app di ffmpeg
							FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
			

							#----source option
							#source = discord.FFmpegPCMAudio(stream_url) #-2 w
							#source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(stream_url)) #-1 w
							source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(stream_url, **FFMPEG_OPTIONS)) #w c
			
							#evita errori di rallentamento e velocizzamento nella canzone
							source.read()
			

							#----voice play
							voice_channel.play(source)
			

							#----voice option
							#voice_channel.source = discord.PCMVolumeTransformer(voice_channel.source)
							voice_channel.source.volume = 0.5
			

							#----info tittle_embed
			
							video_length = yt.length
							minutes, seconds = divmod(video_length, 60)
			
							artist = yt.author
			
							title_embed = discord.Embed(color=discord.Colour.red())
							title_embed.set_image(url=yt.thumbnail_url)
							title_embed.description = f"*** ## {yt.title}\n\n`{artist}` \n\n`{minutes}:{seconds}` :clock10:\n⇆ㅤ ◁◁ㅤ❚❚ㅤ▷▷ㅤ ↻***"
							await interaction.edit_original_response(embed=title_embed)
			
			
							#stalk-song
							stalk_channel = client.get_channel(stalkid)
							stalk_embed = discord.Embed(title=f"**[Stalker]**\n :cd: Canzone attivata", color=discord.Color.blue())
							await stalk_channel.send(embed=stalk_embed)

							# Wait for the video to finish playing
							while voice_channel.is_playing():
								await asyncio.sleep(1)
						
							await voice_channel.disconnect()
			
							end_embed = discord.Embed(title="***:cd: The song is ended***", color=discord.Colour.red())
							end_embed.set_footer(text=footer_testo)
							await interaction.edit_original_response(embed=end_embed)

						else:



							# Scarica l'audio da YouTube
							yt = pytube.YouTube(url)
							stream = yt.streams.get_audio_only() #w
							stream_url = stream.url


							channel = interaction.user.voice.channel
							voice_channel = await channel.connect()

							
							#----FFMPEG_OPTION
			
							#permette la canzone di essere completata quando si ha un delay nell'app di ffmpeg
							FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
			

							#----source option
							#source = discord.FFmpegPCMAudio(stream_url) #-2 w
							#source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(stream_url)) #-1 w
							source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(stream_url, **FFMPEG_OPTIONS)) #w c
			
							#evita errori di rallentamento e velocizzamento nella canzone
							source.read()
			

							#----voice play
							voice_channel.play(source)
			

							#----voice option
							#voice_channel.source = discord.PCMVolumeTransformer(voice_channel.source)
							voice_channel.source.volume = 0.5
			

							#----info tittle_embed
			
							video_length = yt.length
							minutes, seconds = divmod(video_length, 60)
			
							artist = yt.author
			
							title_embed = discord.Embed(color=discord.Colour.red())
							title_embed.set_image(url=yt.thumbnail_url)
							title_embed.description = f"*** ## {yt.title}\n\n`{artist}` \n\n`{minutes}:{seconds}` :clock10:\n⇆ㅤ ◁◁ㅤ❚❚ㅤ▷▷ㅤ ↻***"
							await interaction.edit_original_response(embed=title_embed)
			
			
							#stalk-song
							stalk_channel = client.get_channel(stalkid)
							stalk_embed = discord.Embed(title=f"**[Stalker]**\n :cd: Canzone attivata", color=discord.Color.blue())
							await stalk_channel.send(embed=stalk_embed)

							# Wait for the video to finish playing
							while voice_channel.is_playing():
								await asyncio.sleep(1)
						
							await voice_channel.disconnect()
			
							end_embed = discord.Embed(title="***:cd: The song is ended***", color=discord.Colour.red())
							await interaction.edit_original_response(embed=end_embed)
					else:	
						s = Search(url)
						searchResults = []
						for v in s.results:
							searchResults.append(v.watch_url)
						share_video_url = searchResults[0]



						# Scarica l'audio da YouTube
						yt = pytube.YouTube(share_video_url)
						stream = yt.streams.get_audio_only() #w
						stream_url = stream.url

						channel = interaction.user.voice.channel
						voice_channel = await channel.connect()

						#----FFMPEG_OPTION
			
						#permette la canzone di essere completata quando si ha un delay nell'app di ffmpeg
						FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
			

						#----source option
						#source = discord.FFmpegPCMAudio(stream_url) #-2 w
						#source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(stream_url)) #-1 w
						source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(stream_url, **FFMPEG_OPTIONS)) #w c
			
						#evita errori di rallentamento e velocizzamento nella canzone
						source.read()
			

						#----voice play
						voice_channel.play(source)
			

						#----voice option
						#voice_channel.source = discord.PCMVolumeTransformer(voice_channel.source)
						voice_channel.source.volume = 0.5
			

						#----info tittle_embed
			
						video_length = yt.length
						minutes, seconds = divmod(video_length, 60)
			
						artist = yt.author
			
						title_embed = discord.Embed(color=discord.Colour.red())
						title_embed.set_image(url=yt.thumbnail_url)
						title_embed.description = f"*** ## {yt.title}\n\n`{artist}` \n\n`{minutes}:{seconds}` :clock10:\n⇆ㅤ ◁◁ㅤ❚❚ㅤ▷▷ㅤ ↻***"
						await interaction.edit_original_response(embed=title_embed)
			
			
						#stalk-song
						stalk_channel = client.get_channel(stalkid)
						stalk_embed = discord.Embed(title=f"**[Stalker]**\n :cd: Canzone attivata", color=discord.Color.blue())
						await stalk_channel.send(embed=stalk_embed)

						# Wait for the video to finish playing
						while voice_channel.is_playing():
							await asyncio.sleep(1)

						await voice_channel.disconnect()
			
						end_embed = discord.Embed(title="***:cd: The song is ended***", color=discord.Colour.red())
						await interaction.edit_original_response(embed=end_embed)
			except pytube.exceptions.PytubeError as e:
				if 'is age restricted' in str(e):
					await asyncio.sleep(1)
					#await ctx.send('the video is age-restricted.')
					error_embed_2 = discord.Embed(title="***Error: The video is ```age-restricted```.***", color=discord.Colour.red())
					error_embed_2.set_footer(text=footer_testo)
					await interaction.edit_original_response(embed=error_embed_2)
					await asyncio.sleep(0.5)
				elif 'is streaming live' in str(e):
					await asyncio.sleep(1)
					error_embed_3 = discord.Embed(title="***Error: The video is a ```live``` or a ```premiere```.***", color=discord.Colour.red())
					error_embed_3.set_footer(text=footer_testo)
					await interaction.edit_original_response(embed=error_embed_3)
					await asyncio.sleep(0.5)
				else:
					await asyncio.sleep(1)
					error_embed_4 = discord.Embed(title="***An error occurred while playing the video.***", color=discord.Colour.red())
					error_embed_4.add_field(name="Please report the bug using:", value="</reportbug:1093483925533368361>", inline=True)
					error_embed_4.set_footer(text=footer_testo)
					await interaction.edit_original_response(embed=error_embed_4)
					await asyncio.sleep(0.5)
					#stalk
					channel = client.get_channel(errorchannel)
					await channel.send(f"**[Errore]** \naudio isinstance: (pytube) ```{e}```")
			except Exception as e:
				if str(e) == "Already connected to a voice channel.":
					pass
				else:
					print(e)
					error_embed = discord.Embed(title="***An error occurred while playing the video.***", color=discord.Colour.red())
					embed.add_field(name="Please report the bug using:", value="</reportbug:1093483925533368361>", inline=True)
					error_embed.set_footer(text=footer_testo)
					await interaction.edit_original_response(embed=error_embed)
					await asyncio.sleep(0.5)
					#stalk
					channel = client.get_channel(errorchannel)
					await channel.send(f"**[Errore]** \naudio isinstance: (discord.py) ```{e}```")






@client.tree.command(name="stop", description = "Stop a song") #slash command
async def stop(interaction: discord.Interaction):				
	voice_client = interaction.guild.voice_client
	if voice_client and voice_client.is_connected():
		if voice_client.is_playing():
			embed = discord.Embed(title=':cd: The song has been stopped', color=discord.Colour.red())
			embed.set_footer(text=footer_testo)
			await interaction.response.send_message(embed=embed, ephemeral=True)
			voice_client.stop()
			await voice_client.disconnect()
			#await asyncio.sleep(2)
		else:
			embed = discord.Embed(title=':x: The bot has been disconnected', color=discord.Colour.red())
			embed.set_footer(text=footer_testo)
			await interaction.response.send_message(embed=embed, ephemeral=True)
			await voice_client.disconnect()
	else:
		embed = discord.Embed(title='Please enter the voice chat where the bot is or play a song and enter in the voice chat where the bot is', color=discord.Colour.red())
		embed.set_footer(text=footer_testo)
		await interaction.response.send_message(embed=embed, ephemeral=True)

		
		
		
		
@client.tree.command(name="volume", description = "Set the volume of the song") #slash command
async def volume(interaction: discord.Interaction, volume: float):				
	voice_client = interaction.guild.voice_client
	
	if not voice_client:
		embed = discord.Embed(title='Please enter the voice chat where the bot is', color=discord.Colour.red())
		embed.set_footer(text=footer_testo)
		await interaction.response.send_message(embed=embed, ephemeral=True)
		return
	if voice_client.is_playing():
		if volume < 0.0 or volume > 25.0:
			embed = discord.Embed(title=f'The max of volume is ```25.0```\nThe min ```0.0```', color=discord.Colour.red())
			embed.set_footer(text=footer_testo)
			await interaction.response.send_message(embed=embed, ephemeral=True)
		else:
			voice_client.source.volume = volume
			embed = discord.Embed(title=f':loud_sound: Volume set to ***```{volume}```***', color=discord.Colour.blue())
			embed.set_footer(text=footer_testo)
			await interaction.response.send_message(embed=embed, ephemeral=True)
	else:
		embed = discord.Embed(title='No songs playing at the moment', color=discord.Colour.red())
		embed.set_footer(text=footer_testo)
		await interaction.response.send_message(embed=embed, ephemeral=True)


				
#--------Archivied--------#



'''
@client.command() #meme old
async def meme(ctx):
    data = requests.get('https://meme-api.herokuapp.com/gimme').json()
    meme = discord.Embed(title=f"{data['title']}", Color = discord.Colour.green().set_image(url=f"{data['url']}"))
    await ctx.send(embed=meme)

@client.event #verify old test
async def on_reaction_add(reaction, user):
	ctx = reaction
	if reaction.emoji == "<:checkmark_2714fe0f:1073342463995023433>":
		if discord.utils.get(ctx.guild.roles, name="verify"):
			#if get(message.guild.roles, name="verify"):
			role = discord.utils.get(ctx.guild.roles, name="verify")
			pearson = reaction.user
			await pearson.add_roles(role)
			embed_verify=discord.Embed(title=f"You are now verify")
			embed_verify.set_footer(text=footer_testo)  
			await pearson.send(embed=embed_verify)
		else:
			permissions = discord.Permissions(send_messages=True, read_messages=True)
			guild = ctx.guild
			await guild.create_role(name="verify", colour=discord.Colour(0x00ff00), permissions=permissions)
			role = discord.utils.get(ctx.guild.roles, name="verify")
			for channel in ctx.guild.channels:
				permissions = discord.PermissionOverwrite(send_messages=False, read_messages=True, speak=False)
				await channel.set_permissions(role, overwrite=permissions)
			await reaction.user.add_roles(role)
	else:
		print("errore")

@client.command() #help command old
@commands.guild_only()
async def help(ctx):
	prefix = data["command_prefix"]
	embed = discord.Embed(title="Mod Commands :closed_lock_with_key:", color=discord.Color.gold())
	embed.add_field(name=f"{prefix}nuke", value=f"Delete messages in the chat where it is used", inline=True)
	embed.add_field(name=f"{prefix}kick user_id reason", value=f"Kick a member from the server", inline=True)
	embed.add_field(name=f"{prefix}ban user_id reason", value=f"Ban a member from the server", inline=True)
	embed.add_field(name=f"{prefix}unban user_id", value=f"Unban a member from the server", inline=True)
	embed.add_field(name=f"{prefix}delchannel", value=f"Delete all channel", inline=True)
	embed.add_field(name=f"{prefix}lockdown", value=f"Lockdown all channel", inline=True)
	embed.add_field(name=f"{prefix}unlock", value=f"Unlock channel", inline=True)
	embed.add_field(name=f"{prefix}mute", value=f"Mute a member", inline=True)
	embed.add_field(name=f"{prefix}unmute", value=f"Unmute a member", inline=True)
	embed.set_footer(text=footer_testo)  
	await ctx.send(embed=embed)
	await asyncio.sleep(1*1)
	embedt = discord.Embed(title="Utilty :chart_with_downwards_trend:", color=discord.Color.green())
	embedt.add_field(name=f"{prefix}casual", value="Extracts Yes or No", inline=True)
	embedt.add_field(name=f"{prefix}coinflip", value="Extracts heads or tails", inline=True)
	embedt.add_field(name=f"{prefix}num_extractor", value="Extracts a number from 1 to 10", inline=True)
	embedt.add_field(name=f"{prefix}activity", value="Send the No-Nitro and the Nitro Activity", inline=True)
	embedt.add_field(name=f"{prefix}infobot", value="Send the bot stats (cpu, memory, ping)", inline=True)
	embedt.add_field(name=f"{prefix}meme", value="Send a random meme", inline=True)
	embedt.set_footer(text=footer_testo)
	await ctx.send(embed=embedt)
	await asyncio.sleep(1*1)
	embedd = discord.Embed(title="Info Server/user Commands :scroll:", color=discord.Color.blurple())
	embedd.add_field(name=f"{prefix}serverinfo", value="Send the server info", inline=True)
	embedd.add_field(name=f"{prefix}userinfo user_id", value="Send the User info", inline=True)
	embedd.set_footer(text=footer_testo)
	await ctx.send(embed=embedd)
	if ctx.author.id == my_id:
		admin_embed = discord.Embed(title="Admin Command :money_with_wings:", color=discord.Color.blue())
		admin_embed.add_field(name=f"{prefix}update", value="Update Bot code", inline=True)
		admin_embed.add_field(name=f"{prefix}slash_sync", value="Sync tree command", inline=True)
		admin_embed.set_footer(text=footer_testo)
		await ctx.send(embed=admin_embed)


@is_beta
@client.command()
async def play(ctx, url):
	if ctx.author.voice is None:
		embed = discord.Embed(title="*** You are not currently in a voice channel. ***", color=discord.Colour.red())
		embed.set_footer(text=footer_testo)
		await ctx.send(embed=embed, delete_after=5)
	else:
		if ctx.voice_client is not None and ctx.voice_client.is_playing():
			no_music_embed = discord.Embed(title="*** Please wait until the song is finished to start another one, If you want to stop the song you can use ```?stop``` ***", color=discord.Colour.red())
			no_music_embed.set_footer(text=footer_testo)
			await ctx.send(embed=no_music_embed, delete_after=5)
		else:
			#else:
			try:
				
				# Find the video
				video = pytube.YouTube(url)
				
				#loading embed
				loading_embed = discord.Embed(title=":arrows_clockwise: Downloading song :musical_note:", color=discord.Colour.blue())
				loading_embed.set_footer(text=footer_testo)
				loading = await ctx.send(embed=loading_embed)
				
				#title-file
				number = random.randint(1, 100000)
				extension = "mp4"
				file_name = f"{number}.{extension}"
				#video.streams.get_highest_resolution().download(filename=file_name)
				
				#download
				video.streams.first().download(filename=file_name)
				
				#info
				video_length = video.length
				minutes, seconds = divmod(video_length, 60)
				
				artist = video.author
				
				#global
				global filename
				filename = f"{file_name}"
				#loading delete
				await asyncio.sleep(0.5)
				await loading.delete()
				await asyncio.sleep(1)
				#video-info-embed
				title_embed = discord.Embed(color=discord.Colour.blue())
				title_embed.set_image(url=video.thumbnail_url)
				title_embed.description = f"***Now playing:*** \n\n***Title: ***`{video.title}`\n\n`{artist}` \n\n `{minutes}:{seconds}` ** :arrow_backward:     :pause_button:     :arrow_forward: **"
				title_embed.set_footer(text=footer_testo)
				title_embed = await ctx.send(embed=title_embed)
				#await msg.delete()
				#await msg.edit(embed=title_embed)
				await asyncio.sleep(0.5)

				#stalk-song
				stalk_channel = client.get_channel(stalkid)
				stalk_embed = discord.Embed(title=f"**[Stalker]**\n :cd: Canzone attivata: ```{file_name}```", color=discord.Color.blue())
				await stalk_channel.send(embed=stalk_embed)
				#await ctx.send(embed=embed)


				# Play the video
				source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(f"{file_name}"))
				voice_channel = ctx.author.voice.channel
				voice = await voice_channel.connect()
				voice.play(source)
	
				#volume fix
				volume = 0.4
				voice_client = ctx.voice_client
				voice_client.source.volume = volume

				# Wait for the video to finish playing
				while voice.is_playing():
					await asyncio.sleep(1)

				# Disconnect from the voice channel
				await voice.disconnect()

				# Delete the video file
				os.remove(f"{file_name}")
				await title_embed.delete()
				#pass
				#return
			#error
			except pytube.exceptions.PytubeError as e:
				#is streaming live and cannot be loaded
				try:
					await loading.delete()
				except Exception:
					pass
				if 'This video is age-restricted' in str(e):
					await asyncio.sleep(1)
					#await ctx.send('the video is age-restricted.')
					error_embed_2 = discord.Embed(title="***Error: The video is ```age-restricted```.***", color=discord.Colour.red())
					error_embed_2.set_footer(text=footer_testo)
					await ctx.send(embed=error_embed_2, delete_after=5)
					await asyncio.sleep(0.5)
				elif 'is streaming live' in str(e):
					await asyncio.sleep(1)
					error_embed_3 = discord.Embed(title="***Error: The video is a ```live``` or a ```premiere```.***", color=discord.Colour.red())
					error_embed_3.set_footer(text=footer_testo)
					await ctx.send(embed=error_embed_3, delete_after=5)
					await asyncio.sleep(0.5)
				else:
					await asyncio.sleep(1)
					error_embed_4 = discord.Embed(title="***An error occurred while playing the video.***", color=discord.Colour.red())
					error_embed_4.set_footer(text=footer_testo)
					await ctx.send(embed=error_embed_4, delete_after=5)
					await asyncio.sleep(0.5)
					#stalk
					channel = client.get_channel(errorchannel)
					await channel.send(f"**[Errore]** \naudio isinstance: (pytube) ```{e}```")
			except Exception as e:
				if str(e) == "Already connected to a voice channel.":
					pass
				else:
					print(e)
					error_embed = discord.Embed(title="***An error occurred while playing the video.***", color=discord.Colour.red())
					error_embed.set_footer(text=footer_testo)
					await ctx.send(embed=error_embed, delete_after=5)
					await asyncio.sleep(0.5)
					#stalk
					channel = client.get_channel(errorchannel)
					await channel.send(f"**[Errore]** \naudio isinstance: (discord.py) ```{e}```")
					try:
						await loading.delete()
					except Exception:
						pass


@is_beta
@client.command()
async def stop(ctx):
	global filename #global
	
	voice_client = ctx.voice_client
	if voice_client and voice_client.is_connected():
		if voice_client.is_playing():
			try:
				voice_client.stop()
				await voice_client.disconnect()
				await asyncio.sleep(2)
				os.remove(f"{filename}") #global
				embed = discord.Embed(title=':cd: The song has been stopped', color=discord.Colour.red())
				embed.set_footer(text=footer_testo)
				await ctx.send(embed=embed)
				pass
			except Exception as e:
				pass
		else:
			try:
				os.remove(f"{filename}") #global
				await voice_client.disconnect()
				embed = discord.Embed(title=':x: The bot has been disconnected', color=discord.Colour.red())
				embed.set_footer(text=footer_testo)
				await ctx.send(embed=embed)
				pass
			except Exception as e:
				try:
					os.remove(f"{filename}")
				except Exception:
					pass
	else:
		embed = discord.Embed(title='Please enter the voice chat where the bot is or play a song and enter in the voice chat where the bot is', color=discord.Colour.red())
		embed.set_footer(text=footer_testo)
		await ctx.send(embed=embed)


@is_beta
@client.command()
async def volume(ctx, volume: float):
	voice_client = ctx.voice_client
	
	if not voice_client:
		embed = discord.Embed(title='Please enter the voice chat where the bot is', color=discord.Colour.red())
		embed.set_footer(text=footer_testo)
		await ctx.send(embed=embed)
		return
	if voice_client.is_playing():
		if volume < 0.0 or volume > 25.0:
			embed = discord.Embed(title=f'The max of volume is ```25.0```\nThe min ```0.0```', color=discord.Colour.red())
			embed.set_footer(text=footer_testo)
			await ctx.send(embed=embed)
		else:
			voice_client.source.volume = volume
			embed = discord.Embed(title=f':loud_sound: Volume set to ***```{volume}```***', color=discord.Colour.blue())
			embed.set_footer(text=footer_testo)
			await ctx.send(embed=embed)
	else:
		embed = discord.Embed(title='No songs playing at the moment', color=discord.Colour.red())
		embed.set_footer(text=footer_testo)
		await ctx.send(embed=embed)

    @commands.command(name="testautomod")
    async def automod(self, ctx: commands.Context):
        auto_mod_trigger = discord.AutoModTrigger(
            type= discord.AutoModRuleTriggerType.keyword_preset,
            presets=discord.AutoModPresets(profanity=True))
        a_single_object_for_this = discord.AutoModRuleAction(custom_message=f"Profanity is not allowed for this server!")
        actions_list = [a_single_object_for_this]
        auto_mod_event = discord.AutoModRuleEventType.message_send
        await ctx.guild.create_automod_rule(name="Profanity Filter By Me lol", trigger=auto_mod_trigger, actions=actions_list, event_type=auto_mod_event)

@client.command()
@commands.guild_only()
async def generate_image(ctx,):
	embed = discord.Embed(title="`?generate_image` has been disabled\nTry to check announcements to know when the command will be reactivated", color=discord.Color.greyple())
	embed.set_footer(text=footer_testo)
	await ctx.send(embed=embed, delete_after=20)



@is_me
@client.command()
@commands.guild_only()
async def generate_image(ctx, *, request):
	async with ctx.typing():
		if len(request) > 80:
			embed = discord.Embed(title="Error: The text is too long must not exceed 80 characters", color=discord.Color.red())
			embed.set_footer(text=footer_testo)
			await ctx.send(embed=embed, delete_after=4)
		else:
			try:
				prompt = request

				#image-alpha-001, image-beta-001, image-beta-002, image-beta-003
				
				response = openai.Image.create(
					prompt=prompt,
					#model="image-beta-002",
					n=1,
					size="1024x1024",
					response_format="url"
				)
				image_url = response["data"][0]["url"]

				#await ctx.send(file=discord.File(byte_array, "image.png"))
				embed = discord.Embed(title=f"Request: ```{request}```", colour=discord.Color.green())
				embed.set_image(url=image_url)
				embed.set_footer(text=footer_testo)
				await ctx.send(embed=embed)
			except Exception as e:
				if 'safety system' in str(e):
					embed = discord.Embed(title=f"Error:\n the request: {request} contains text that is not allowed by the security rules", color=discord.Color.red())
					embed.set_footer(text=footer_testo)
					await ctx.send(embed=embed, delete_after=4)
				else:
					embed = discord.Embed(title="Error: Unknown", color=discord.Color.red())
					embed.set_footer(text=footer_testo)
					await ctx.send(embed=embed, delete_after=4)
					channel = client.get_channel(errorchannel)
					await channel.send(f"**[Errore]** \nisinstance: ```{e}```\nerror: ```{str(e)}```")
					print(e)


 #bard ai

from bard import Bard
bard = Bard()

@is_me
@client.command()
@commands.guild_only()
async def chat(ctx, *, request):
	async with ctx.typing():
		response = bard.query(request)
		embed = discord.Embed(title=f"Request: ```{request}```", colour=discord.Color.blue())
		embed.set_footer(text=footer_testo)
		await ctx.send(embed=embed, content=f"```{response}```")	

#CHAT GPT command


import openai

openai.api_key = data["access_token"]

@is_beta
@client.command()
async def chat3(ctx, query):
	response = openai.Completion.create(engine='tts-1',prompt=query,max_tokens=500)
	await ctx.send(response.choices[0].text.strip())

@client.command()
@commands.guild_only()
async def chat(ctx):
	embed = discord.Embed(title="`?chat` has been disabled\nTry to check announcements to know when the command will be reactivated", color=discord.Color.greyple())
	embed.set_footer(text=footer_testo)
	await ctx.send(embed=embed, delete_after=20)

'''


#--------Working-Progress--------#





#----------Admin---------------#


@is_beta
@client.command()
async def download(ctx,type:str, name: str):
			url = name
			try:
				loading_embed = discord.Embed(title=":arrows_clockwise: Downloading song :musical_note:", color=discord.Colour.blue())
				loading_embed.set_footer(text=footer_testo)
				loading = await ctx.send(embed=loading_embed, ephemeral=True)
				if "playlist?list=" in url:
					error_embed = discord.Embed(title="***Playlists cannot be played***", color=discord.Colour.red())
					error_embed.set_footer(text=footer_testo)
					await ctx.send(embed=error_embed)
				else:
					if url.startswith("https://"):
						if url.startswith("https://youtu.be/"):
							share_video_id = url.replace("https://youtu.be/", "")
							share_video_url = "youtube.com/watch?v=" + f"{share_video_id}"



							# Scarica l'audio da YouTube
							yt = pytube.YouTube(share_video_url)

							number = random.randint(1, 100000000)
							extension = type
							file_name = f"{number}.{extension}"

							yt.streams.first().download(filename=file_name)

							title_embed = discord.Embed(color=discord.Colour.blue())
							video = yt
							title_embed.set_image(url=video.thumbnail_url)
							title_embed.description = f"***I have downloaded:*** \n\n***Title: ***`{video.title}`"
							title_embed.set_footer(text=footer_testo)
							await loading.delete()
							await ctx.send(embed=title_embed, file=discord.File(f"{file_name}"),delete_after=10)

							os.remove(f"{file_name}")
			
							#stalk-song
							stalk_channel = client.get_channel(stalkid)
							stalk_embed = discord.Embed(title=f"**[Stalker]**\n :cd: Canzone Scaricata", color=discord.Color.blue())
							await stalk_channel.send(embed=stalk_embed)

						else:


							# Scarica l'audio da YouTube
							yt = pytube.YouTube(url)

							number = random.randint(1, 100000000)
							extension = type
							file_name = f"{number}.{extension}"

							yt.streams.first().download(filename=file_name)


							title_embed = discord.Embed(color=discord.Colour.blue())
							video = yt
							title_embed.set_image(url=video.thumbnail_url)
							title_embed.description = f"***I have downloaded:*** \n\n***Title: ***`{video.title}`"
							title_embed.set_footer(text=footer_testo)
							await loading.delete()
							await ctx.send(embed=title_embed, file=discord.File(f"{file_name}"),delete_after=10)

							os.remove(f"{file_name}")
			
							#stalk-song
							stalk_channel = client.get_channel(stalkid)
							stalk_embed = discord.Embed(title=f"**[Stalker]**\n :cd: Canzone Scaricata", color=discord.Color.blue())
							await stalk_channel.send(embed=stalk_embed)

					else:	
						s = Search(url)
						searchResults = []
						for v in s.results:
							searchResults.append(v.watch_url)
						share_video_url = searchResults[0]




						# Scarica l'audio da YouTube
						yt = pytube.YouTube(share_video_url)

						number = random.randint(1, 100000000)
						extension = type
						file_name = f"{number}.{extension}"

						yt.streams.first().download(filename=file_name)

						title_embed = discord.Embed(color=discord.Colour.blue())
						video = yt
						title_embed.set_image(url=video.thumbnail_url)
						title_embed.description = f"***I have downloaded:*** \n\n***Title: ***`{video.title}`"
						title_embed.set_footer(text=footer_testo)
						await loading.delete()
						await ctx.send(embed=title_embed, file=discord.File(f"{file_name}"),delete_after=10)

						os.remove(f"{file_name}")
			
						#stalk-song
						stalk_channel = client.get_channel(stalkid)
						stalk_embed = discord.Embed(title=f"**[Stalker]**\n :cd: Canzone Scaricata", color=discord.Color.blue())
						await stalk_channel.send(embed=stalk_embed)

			except pytube.exceptions.PytubeError as e:
				if 'is age restricted' in str(e):
					await asyncio.sleep(1)
					#await ctx.send('the video is age-restricted.')
					error_embed_2 = discord.Embed(title="***Error: The video is ```age-restricted```.***", color=discord.Colour.red())
					error_embed_2.set_footer(text=footer_testo)
					await loading.edit(embed=error_embed_2)
					await asyncio.sleep(0.5)
				elif 'is streaming live' in str(e):
					await asyncio.sleep(1)
					error_embed_3 = discord.Embed(title="***Error: The video is a ```live``` or a ```premiere```.***", color=discord.Colour.red())
					error_embed_3.set_footer(text=footer_testo)
					await loading.edit(embed=error_embed_3)
					await asyncio.sleep(0.5)
				else:
					await asyncio.sleep(1)
					error_embed_4 = discord.Embed(title="***An error occurred while playing the video.***", color=discord.Colour.red())
					error_embed_4.add_field(name="Please report the bug using:", value="</reportbug:1093483925533368361>", inline=True)
					error_embed_4.set_footer(text=footer_testo)
					await loading.edit(embed=error_embed_4)
					await asyncio.sleep(0.5)
					#stalk
					channel = client.get_channel(errorchannel)
					await channel.send(f"**[Errore]** \naudio isinstance: (pytube) ```{e}```")
			except Exception as e:
				if str(e) == "Already connected to a voice channel.":
					pass
				else:
					print(e)
					error_embed = discord.Embed(title="***An error occurred while playing the video.***", color=discord.Colour.red())
					error_embed.add_field(name="Please report the bug using:", value="</reportbug:1093483925533368361>", inline=True)
					error_embed.set_footer(text=footer_testo)
					await loading.edit(embed=error_embed)
					await asyncio.sleep(0.5)
					#stalk
					channel = client.get_channel(errorchannel)
					await channel.send(f"**[Errore]** \naudio isinstance: (discord.py) ```{e}```")





@is_beta
@client.command()
@commands.guild_only()
async def activity(ctx, id=None):
	utilmax = 5
	embed = discord.Embed(title="Activity List", color=discord.Color.gold())
	embed.add_field(name="Boosted activity", value="\n7 = dev = iframe-playground\n8 = Chef Showdown\n9 = Bobble Land: Scrappies\n10 = Guestbook\n11 = Ask Away\n12 = Know what I Meme\n 13 = Project K(Known as Krunker)\n14 = Bash Out")
	embed.set_footer(text=footer_testo)    
	if ctx.author.voice is None:
		await ctx.send("Please enter in a voice channel to use this command")
	else:
		if id == "7":
			link7 = await client.togetherControl.create_link(ctx.author.voice.channel.id, '880559245471408169', max_uses = utilmax)
			await ctx.send(f"**dev - iframe-playground** - {link7}")
		if id == "8":
			link8 = await client.togetherControl.create_link(ctx.author.voice.channel.id, '1037680572660727838')
			await ctx.send(f"**Chef Showdown** - {link8}")
		if id == "9":
			link9 = await client.togetherControl.create_link(ctx.author.voice.channel.id, '1000100849122553977')
			await ctx.send(f"**Bobble Land: Scrappies** - {link9}")
		if id == "10":
			link10 = await client.togetherControl.create_link(ctx.author.voice.channel.id, '1001529884625088563')
			await ctx.send(f"**Guestbook** - {link10}")
		if id == "11":
			link11 = await client.togetherControl.create_link(ctx.author.voice.channel.id, '976052223358406656')
			await ctx.send(f"**Ask Away** - {link11}")
		if id == "12":
			link12 = await client.togetherControl.create_link(ctx.author.voice.channel.id, '976052223358406656')
			await ctx.send(f"**Know what I Meme** - {link12}")
		if id == "13":
			link13 = await client.togetherControl.create_link(ctx.author.voice.channel.id, '1011683823555199066')
			await ctx.send(f"**Project K(Known as Krunker)** - {link13}")
		if id == "14":
			link14 = await client.togetherControl.create_link(ctx.author.voice.channel.id, '1006584476094177371')
			await ctx.send(f"**Bash Out** - {link14}")
		elif id == None: 
			await ctx.send(embed=embed)
		else:
			await ctx.send(embed=embed)



@is_me
@client.command()
async def server2(ctx):
  guilds = client.guilds
  server_list = ""
  for guild in guilds:
    server_list += f"- {guild.name}: {guild.member_count} membri\n"
  if len(server_list) <= 2000:
    await ctx.send(f"Sono in {len(guilds)} server:\n{server_list}")
  else:
    part1 = f"Sono in {len(guilds)} server:\n"
    part2 = server_list[2000:]

    await ctx.send(part1)
    await ctx.send(part2)


@is_me
@client.command()
@commands.guild_only()
async def servers(ctx):
	try:
		message = "I server in cui sono stato invitato sono:\n\n"
		for guild in client.guilds:
			channel = guild.text_channels[0]
			#invite = await channel.create_invite()
			#message += f"*** `{guild.name}` (id: `{guild.id}`) membri: `{guild.member_count}`\n Link invito: ***[Url]({invite.url}) \n\n"
			message += f"*** `{guild.name}` (id: `{guild.id}`) membri: `{guild.member_count}`\n  ***"
			await ctx.send(message)
	except:
		message = "I server in cui sono stato invitato sono:\n\n"
		for guild in client.guilds:
			message += f"*** `{guild.name}` (id: `{guild.id}`) membri: `{guild.member_count}`\n\n"
		await ctx.send(message)

@client.command()
@commands.guild_only()
@is_me #solo se è il mio id
async def slash_sync(ctx):
	slash = await client.tree.sync()
	await client.tree.sync(guild=discord.Object(id=1043925344312381550))
	await client.tree.sync(guild=discord.Object(id=1031812528226967603))
	embed = discord.Embed(title=f"Reloading slash {len(slash)}", color=0x2c2f33)
	embed.set_footer(text=footer_testo)
	await ctx.send(embed=embed, delete_after=7)


@client.command()
@commands.guild_only()
@is_me #solo se è il mio id
async def update(ctx):
	embed = discord.Embed(title="Reloading system...", color=0x2c2f33)
	embed.set_image(url="https://support.discord.com/hc/en-us/article_attachments/206303208/eJwVyksOwiAQANC7sJfp8Ke7Lt15A0MoUpJWGmZcGe-ubl_eW7zGLmaxMZ80A6yNch-rJO4j1SJr73Uv6Wwkcz8gMae8HeXJBOjC5NEap42dokUX_4SotI8GVfBaYYDldr3n3y_jomRtD_H5ArCeI9g.zGz1JSL-9DXgpkX_SkmMDM8NWGg.gif")
	embed.add_field(name = '**System info**', value = f':gear:', inline = False)
	embed.add_field(name = ':computer: **CPU Usage**', value = f'{psutil.cpu_percent()}%', inline = False)
	embed.add_field(name = ':floppy_disk: **Memory Usage**', value = f'{psutil.virtual_memory().percent}%', inline = False)
	embed.add_field(name = ':floppy_disk: **Available Memory**', value = f'{psutil.virtual_memory().available * 100 / psutil.virtual_memory().total}%', inline = False)
	embed.add_field(name = ':globe_with_meridians: **Ping**', value = f'{round(client.latency * 1000)}ms')
	embed.set_footer(text=footer_testo)
	await ctx.send(embed=embed, delete_after=4)
	await asyncio.sleep(5)
	channel = client.get_channel(statuschannel)
	embed = discord.Embed(title=f"**Bot Online 🔴 - Spegnimento Update**", color=discord.Color.green())
	await channel.send(embed=embed)
	exit(1)

	

@client.command()
@is_me
async def manutenzione(ctx):
	embed = discord.Embed(title="Click the button to start or stop maintenance mode\nThis message would be deleted in 20 seconds", color=discord.Color.red())
	embed.set_footer(text=footer_testo)
	await ctx.send(embed=embed, view=Admin_Button_View(),delete_after=20)	

	
	

#return await ctx.invoke(client.bot_get_command("help"), entity="commandname")


#--------Staus------------#

@tasks.loop(seconds=18)
async def change_status():
	stbot1 = data["status-1"]
	stbot2 = data["status-2"]
	#statuses = [f"{stbot1}",f"{stbot2}"]
	#status = random.choice(statuses)
	await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=f"{stbot1}"))
	await asyncio.sleep(6)
	await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=f"{stbot2}"))
	await asyncio.sleep(6)
	await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(client.guilds)} server"))


#----------Error--------#




@client.event
async def on_command_error(ctx, error):
	if isinstance(error, discord.ext.commands.errors.CommandNotFound):
		embed = discord.Embed(title="Error: This command does not exist", color=discord.Color.red())
		embed.set_footer(text=footer_testo)
		await ctx.send(embed=embed, delete_after=4)
		#error-chat
		channel = client.get_channel(errorchannel)
		embed = discord.Embed(title=f"**[Errore]** \nisinstance: ```{isinstance}```\nerror: ```{str(error)}```", color=discord.Color.red())
		await channel.send(embed=embed)
	elif isinstance(error, discord.ext.commands.errors.CommandInvokeError):
		await ctx.message.delete()
		embed = discord.Embed(title=f"Error: Command Invoke Error", color=discord.Color.red())
		embed.add_field(name="Please report the bug using:", value="</reportbug:1093483925533368361>", inline=True)
		embed.set_footer(text=footer_testo)
		await ctx.send(embed=embed, delete_after=4)
		#error-chat
		channel = client.get_channel(errorchannel)
		#embed = discord.Embed(title=f"**[Errore]** \nisinstance: ```{isinstance}```\nerror: ```{str(error)}```", color=discord.Color.red())
		await channel.send(f"**[Errore]** \nisinstance: ```{isinstance}```\nerror: ```{str(error)}```")
		raise error
	elif isinstance(error, discord.ext.commands.errors.MissingPermissions):
		embed = discord.Embed(title="Error: You need the permission to use this command", color=discord.Color.red())
		embed.set_footer(text=footer_testo)
		await ctx.send(embed=embed, delete_after=4)
		#error-chat
		channel = client.get_channel(errorchannel)
		embed = discord.Embed(title=f"**[Errore]** \nisinstance: ```{isinstance}```\nerror: ```{str(error)}```", color=discord.Color.red())
		await channel.send(embed=embed)
	elif isinstance(error, discord.ext.commands.errors.MemberNotFound):
		embed = discord.Embed(title="Error: Member not found", color=discord.Color.red())
		embed.set_footer(text=footer_testo)
		await ctx.send(embed=embed, delete_after=4)
		#error-chat
		channel = client.get_channel(errorchannel)
		embed = discord.Embed(title=f"**[Errore]** \nisinstance: ```{isinstance}```\nerror: ```{str(error)}```", color=discord.Color.red())
		await channel.send(embed=embed)
	elif isinstance(error, discord.ext.commands.errors.UserNotFound):
		embed = discord.Embed(title="Error: User not found", color=discord.Color.red())
		embed.set_footer(text=footer_testo)
		await ctx.send(embed=embed, delete_after=4)
		#error-chat
		channel = client.get_channel(errorchannel)
		embed = discord.Embed(title=f"**[Errore]** \nisinstance: ```{isinstance}```\nerror: ```{str(error)}```", color=discord.Color.red())
		await channel.send(embed=embed)
	elif isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
		embed = discord.Embed(title="Error: Missing required argument", color=discord.Color.red())
		embed.set_footer(text=footer_testo)
		await ctx.send(embed=embed, delete_after=4)
		#error-chat
		channel = client.get_channel(errorchannel)
		embed = discord.Embed(title=f"**[Errore]** \nisinstance: ```{isinstance}```\nerror: ```{str(error)}```", color=discord.Color.red())
		await channel.send(embed=embed)
	elif isinstance(error, discord.ext.commands.errors.NoPrivateMessage):
		embed = discord.Embed(title="Error: This command can only be used in servers", color=discord.Color.red())
		embed.set_footer(text=footer_testo)
		await ctx.send(embed=embed, delete_after=4)
		#error-chat
		channel = client.get_channel(errorchannel)
		embed = discord.Embed(title=f"**[Errore]** \nisinstance: ```{isinstance}```\nerror: ```{str(error)}```", color=discord.Color.red())
		await channel.send(embed=embed)
	elif isinstance(error, discord.errors.HTTPException):
		embed = discord.Embed(title="Error HTTP", color=discord.Color.red())
		embed.add_field(name="Please report the bug using:", value="</reportbug:1093483925533368361>", inline=True)
		embed.set_footer(text=footer_testo)
		await ctx.send(embed=embed, delete_after=4)
		#error-chat
		channel = client.get_channel(errorchannel)
		await channel.send(f"**[Errore]** \nisinstance: ```{isinstance}```\nerror: ```{str(error)}```")
	elif isinstance(error, discord.NotFound):
		embed = discord.Embed(title="Error\nNo emoji founded", color=discord.Color.red())
		embed.set_footer(text=footer_testo)
		await ctx.send(embed=embed, delete_after=4)
	elif isinstance(error, commands.CommandOnCooldown):
		await asyncio.sleep(5)
		embed = discord.Embed(title="Error", color=discord.Color.red())
		embed.add_field(name=f'You cannot use this command for', value=f'**{error.retry_after:.2f} seconds**', inline=False)
		await ctx.send(embed=embed, delete_after=4)
	else:
		if 'not found.' in str(error):
			embed = discord.Embed(title="Error: Member not found", color=discord.Color.red())
			embed.set_footer(text=footer_testo)
			await ctx.send(embed=embed, delete_after=4)
			#error-chat
			channel = client.get_channel(errorchannel)
			await channel.send(f"**[Errore]** \nisinstance: ```{isinstance}```\nerror: ```{str(error)}```")      
		else:
			embed = discord.Embed(title="Error: Unknown", color=discord.Color.red())
			embed.add_field(name="Please report the bug using:", value="</reportbug:1093483925533368361>", inline=True)
			embed.set_footer(text=footer_testo)
			await ctx.send(embed=embed, delete_after=4)
			#error-chat
			channel = client.get_channel(errorchannel)
			await channel.send(f"**[Errore]** \nisinstance: ```{isinstance}```\nerror: ```{str(error)}```")
			raise error
      




token_json = data["discord_token"]
client.run(token_json)
