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
import psutil


#activity
from discord_together import DiscordTogether

#traduttore
from deep_translator import GoogleTranslator

#music-bot
import pytube
import asyncio
import os



#config
with open("config.json") as f:
    try:
        data = json.load(f)
    except json.decoder.JSONDecodeError as e:
        print("Errore in config.json")
        print(e)
        exit(1)

	
my_id = 598119406731657216
beta_list = [598119406731657216, 829022689338851389]


is_me = commands.check(lambda ctx: ctx.author.id == my_id) 

is_beta = commands.check(lambda ctx: ctx.author.id in beta_list )

#is_beta = str(message.author.id) in [str(id) for id in beta_list]
#if not is_beta:
#    await message.author.send("Non sei ancora autorizzato ad accedere alla funzionalità beta.")

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

#discord
footer_testo = data["footer_embed"]
stalkid = 1045020366751404172
errorchannel = 1046796347870826496
statuschannel = 1129639048735117342





@client.event
async def on_ready():
	try:
		change_status.cancel()
	except:
		return
	print(f"Bot logged into {client.user}.")
	channel = client.get_channel(statuschannel)
	embed = discord.Embed(title=f"**Bot Online 🟢 - Start d'avvio**", color=discord.Color.green())
	await channel.send(embed=embed)
	#slash_sync = await client.tree.sync()
	#print(f"Synced app command (tree) {len(slash_sync)}.")
	token_json = data["discord_token"]
	client.togetherControl = await DiscordTogether(token_json) #activity command - old 
	await asyncio.sleep(20)
	change_status.start()


#-----------Stalker--------------#

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
	
	



'''
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
'''

@client.event
async def on_voice_state_update(member, before, after):
	if before.channel is None and after.channel is not None:
		await asyncio.sleep(20)
		channel = client.get_channel(stalkid)
		embed = discord.Embed(title=f"**[Stalker]**\nUtente in Chat vocale\nUtente: `{member.display_name}#{member.discriminator}`\nServer: `{member.guild.name}`", color=discord.Color.blue())
		embed.add_field(name = 'Canale:', value=f"<#{after.channel}>", inline = True)
		await channel.send(embed=embed)
	if before.channel is not None and after.channel is None:
		await asyncio.sleep(20)
		channel = client.get_channel(stalkid)
		embed = discord.Embed(title=f"**[Stalker]**\nUtente in Chat vocale\nUtente: `{member.display_name}#{member.discriminator}`\nServer: `{member.guild.name}`", color=discord.Color.red())
		embed.add_field(name = 'Canale:', value=f"<#{before.channel}>", inline = True)
		await channel.send(embed=embed)
	

#ruoli

@client.event
async def on_guild_role_delete(role):
	await asyncio.sleep(20)
	channel = client.get_channel(stalkid)
	embed = discord.Embed(title=f"**[Stalker]**\nRuolo eliminato\nServer: `{role.guild.name}`", color=discord.Color.red())
	embed.add_field(name = 'Nome:', value=f"`{role.name}`", inline = True)
'''
@client.event
async def on_guild_role_update(before, after):
	await asyncio.sleep(20)
	channel = client.get_channel(stalkid)
	embed = discord.Embed(title=f"**[Stalker]**\nUpdate ruolo\nServer: `{before.guild.name}`", color=discord.Color.gold())
	embed.add_field(name = 'Nome:', value=f"Prima: `{before.name}` Dopo:  `{after.name}`", inline = False)
	embed.add_field(name = 'Avvertenza:', value=f":warning: se il nome non cambio sono i permessi :warning:\n:warning: per mancata voglia non sono stati inseriti :warning:", inline = True)
	await channel.send(embed=embed)
'''

@client.event
async def on_guild_role_create(role):
	await asyncio.sleep(20)
	channel = client.get_channel(stalkid)
	embed = discord.Embed(title=f"**[Stalker]**\nRuolo creato\nServer: `{role.guild.name}`", color=discord.Color.green())
	embed.add_field(name = 'Nome:', value=f"`{role.name}`", inline = True)
	await channel.send(embed=embed)

#----------Commands--------#



@client.command()
@commands.guild_only()
async def userinfo(ctx, *, user: discord.Member = None):
	voice_state = None if not user.voice else user.voice.channel
	role = user.top_role.name
	if role == "@everyone":
		role = "N/A"
	embed = discord.Embed(title=f"***User*** - Info", color=discord.Colour.blue())
	embed.add_field(name=':id: - User ID', value=f"{user.id}", inline=False)
	embed.add_field(name=':bust_in_silhouette: - UserName', value=f"<@{user.id}>", inline=False)
	embed.add_field(name=':bust_in_silhouette: - Old - User Name', value=f"{user.name}#{user.discriminator}", inline=False)
	#embed.add_field(name=':bust_in_silhouette: - User Nick', value=f"{user.display_name}", inline=False)
	#embed.add_field(name=':radio_button: - User Status', value=f"**{user.status}**", inline=False)
	#embed.add_field(name=':video_game: - User Game', value=f"**{user.activity}**", inline=False)
	embed.add_field(name=':robot: - Robot?', value=f"**{user.bot}**", inline=False)
	embed.add_field(name=':loud_sound:  - Is in voice', value=f"**In:** **{voice_state}**", inline=False)
	embed.add_field(name=':radio_button:  - Highest Role', value=f"**{role}**", inline=False)
	embed.add_field(name=':calendar: - Account Created', value=user.created_at.__format__('***Date:*** %A, %d. %B %Y ***Time:*** %H:%M:%S'), inline=False)
	embed.add_field(name=':calendar: - Join Server Date', value=user.joined_at.__format__('***Date:*** %A, %d. %B %Y ***Time:*** %H:%M:%S'), inline=False)
	embed.set_thumbnail(url=user.avatar)
	embed.set_footer(text=footer_testo)
	await ctx.send(embed=embed)







@client.command()
@commands.guild_only()
@commands.cooldown(1, 20, commands.BucketType.user)
@commands.has_permissions(manage_channels = True)
async def lockdown(ctx):
	await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False, view_channel=False)
	await ctx.send(ctx.channel.mention + " ***is now in lockdown.*** :lock:")   
    #embed = discord.Embed(title=ctx.channel.mention + " ***is now in lockdown.*** :lock:", color=discord.Color.red())
    #await ctx.send(embed)

@client.command()
@commands.guild_only()
@commands.cooldown(1, 10, commands.BucketType.user)
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
	await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True, view_channel=True)
	await ctx.send(ctx.channel.mention + " ***has been unlocked.*** :unlock:")   
	#embed = discord.Embed(title=ctx.channel.mention + " ***has been unlocked.*** :unlock:", color=discord.Color.red())
	#await ctx.send(embed)




@client.command()
@commands.guild_only()
@commands.has_permissions(manage_messages=True)
@commands.cooldown(1, 20, commands.BucketType.user)
async def nuke(ctx, amount: int = 100):
	if amount < 500:
        	embed = discord.Embed(title=f"{amount} messages deleted", color=discord.Color.red())
        	embed.set_image(url="https://www.19fortyfive.com/wp-content/uploads/2021/10/Nuclear-Weapons-Test.jpg")
        	await ctx.channel.purge(limit=amount + 1)
        	embed.set_footer(text=footer_testo)  
        	await ctx.send(embed=embed, delete_after=4)
	else:
        	embed = discord.Embed(title=f"Unable to delete messages, maximum is 450", color=discord.Color.red())
        	embed.set_footer(text=footer_testo)  
        	await ctx.send(embed=embed, delete_after=4)




@client.command()
@commands.guild_only()
async def serverinfo(ctx):
	#check_forum = discord.utils.get(ctx.guild.forum_channels)
	check_text = discord.utils.get(ctx.guild.text_channels)
	check_voice = discord.utils.get(ctx.guild.voice_channels)
	check_category = discord.utils.get(ctx.guild.categories)
	embed = discord.Embed(title=f"***{ctx.guild.name}*** - Info", description="Information of this Server", color=discord.Colour.blue())
	embed.add_field(name=':page_facing_up: - Name', value=f'{str(ctx.guild.name)} Server Name', inline=False)
	embed.add_field(name=':bookmark_tabs: - Description', value=f'{str(ctx.guild.description)} Server Description', inline=False)
	embed.add_field(name=':id: - Server ID', value=f"{ctx.guild.id}", inline=False)
	embed.add_field(name=':calendar: - Created On', value=ctx.guild.created_at.strftime("%b %d %Y"), inline=False)
	embed.add_field(name=':crown: - Owner', value=f"<@{ctx.guild.owner_id}>", inline=False)
	embed.add_field(name=':busts_in_silhouette: - Members', value=f'{ctx.guild.member_count} Members', inline=False)
	#if check_forum is not None:
	#	embed.add_field(name=f':speech_left: - Forum {len(ctx.guild.forum_channels)}', inline=False)
	if check_text is not None:
		embed.add_field(name=f':speech_balloon: - Text ', value=f'{len(ctx.guild.text_channels)}', inline=False)
	if check_voice is not None:
		embed.add_field(name=f':speaker: - Voice ', value=f'{len(ctx.guild.voice_channels)}', inline=False)
	if check_category is not None:
		embed.add_field(name=':open_file_folder: - Category', value=f'{len(ctx.guild.categories)}', inline=False)
	embed.add_field(name=':bust_in_silhouette: - Role', value=f'{len(ctx.guild.roles)} Role count', inline=False)
	embed.set_footer(text=footer_testo)    
	await ctx.send(embed=embed)

 

@client.command()
@commands.guild_only()
async def meme(ctx):
		embed = discord.Embed(title="Meme", color=discord.Colour.green())
		async with aiohttp.ClientSession() as cs:
			async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
				res = await r.json()
				embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
				embed.set_footer(text=footer_testo)  
				await ctx.send(embed=embed)



@client.command()
@commands.guild_only()
async def unmute(ctx, user: discord.Member = None):
	if ctx.message.author.guild_permissions.administrator:
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
	else:
		embed = discord.Embed(title="Error: You need the permission to use this command", color=discord.Color.red())
		embed.set_footer(text=footer_testo)
		await ctx.send(embed=embed, delete_after=4)

@client.command()
@commands.guild_only() 
async def mute(ctx, user: discord.Member = None, reason = None):
	if ctx.message.author.guild_permissions.administrator:
		#channel1 = ctx.guild.channels
		permissions = discord.Permissions(send_messages=False, read_messages=True, speak=False)
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
					else:
						return
					try:
						await user.send(f"You have been muted in the server: **{name}**")
					except:
						pass
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
					else:
						return
					try:
						await user.send(f"You have been muted in the server: **{name}** because:\n{reason}")
					except:
						pass
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
	else:
		embed = discord.Embed(title="Error: You need the permission to use this command", color=discord.Color.red())
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
				await ctx.send(embed=embed)
		else:
			#embed2 = discord.Embed(title=f"You have been banned from the server: {ctx.guild.name}/nFor: '{reason}'", color=discord.Color.red())
			#embed2.set_footer(text=footer_testo)
			#await member.send(embed2)
			#await member.send(f"You have been banned from the server: {ctx.guild.name}/nFor: '{reason}'")
			await member.ban(reason=f"You have been banned from the server: {ctx.guild.name}, For: '{reason}'")
			embed = discord.Embed(title=":warning: Member was banned :warning:", color=discord.Color.red())
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
@commands.has_permissions(manage_messages=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def slowmode(ctx, seconds: int):
	await ctx.channel.edit(slowmode_delay=seconds)
	slowmode_embed = discord.Embed(title="Slowmode", description="A slowmode was set for this channel", colour=discord.Colour.green())
	slowmode_embed.set_footer(text=footer_testo)
	await ctx.send(embed=slowmode_embed, delete_after=10)




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
@has_permissions(administrator = True)
@commands.cooldown(1, 60, commands.BucketType.user)
async def delchannel(ctx):
    for c in ctx.guild.channels: # iterating through each guild channel
        await c.delete()

@client.command()
@commands.guild_only()
@has_permissions(ban_members=True)
async def unban(ctx, user: discord.User):
	try:
		if member == None:
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
	embed = discord.Embed(title = 'System Resource Usage', description = 'See CPU and memory usage of the system.', color=discord.Color.blue())
	embed.add_field(name = ':computer: **CPU Usage**', value = f'{psutil.cpu_percent()}%', inline = False)
	embed.add_field(name = ':floppy_disk: **Memory Usage**', value = f'{psutil.virtual_memory().percent}%', inline = False)
	embed.add_field(name = ':floppy_disk: **Available Memory**', value = f'{psutil.virtual_memory().available * 100 / psutil.virtual_memory().total}%', inline = False)
	embed.add_field(name = ':globe_with_meridians: **Ping**', value = f'{round(client.latency * 1000)}ms')
	embed.set_footer(text=footer_testo)
	await ctx.send(embed = embed)

	

		

@client.command()
@commands.guild_only()
@commands.cooldown(1, 10, commands.BucketType.user)
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
		embed.set_footer(text=footer_testo)
		await ctx.send(embed=embed)





@client.command()
@commands.guild_only()
@commands.has_permissions(manage_messages=True)
@commands.cooldown(1, 15, commands.BucketType.user)
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
		embed = discord.Embed(title="Emoji_Info", colour=discord.Colour.blue())
		embed.add_field(name="Name", value=f"{name}", inline=False)
		embed.add_field(name="Id", value=f"{id_emoji}", inline=False)
		embed.add_field(name="Url", value=f"[Emoji Url]({response_emoji.url})", inline=False)
		embed.add_field(name="Author", value=f"{response_emoji.user.name}", inline=False)
		embed.add_field(name="Time Created", value=f"{creation_time}", inline=False)
		embed.add_field(name="Usable by", value=f"{can_use_emoji}", inline=False)
		embed.add_field(name="Animated", value=f"{is_animated}", inline=False)
		embed.add_field(name="Managed", value=f"{is_managed}", inline=False)
		embed.add_field(name="Requires colons", value=f"{requires_colons}", inline=False)
		embed.add_field(name="Guild name", value=f"{response_emoji.guild.name}", inline=False)
		embed.set_footer(text=footer_testo)
		embed.set_thumbnail(url=response_emoji.url)
		await ctx.send(embed=embed)
	
#-------------Ui----------#

from discord import ui
from discord import app_commands


#-ReportBug

class BugModal(ui.Modal, title='Report Bug'):
    bug_name = ui.TextInput(label='Bugged Command name')
    #options = [discord.SelectOption(label='Option 1', value='1'), discord.SelectOption(label='Option 2', value='2'), discord.SelectOption(label='Option 3', value='3')]
    #type_of_bug = ui.Select(placeholder="Bug Type", min_values=1, max_values=1, options=options)
    answer = ui.TextInput(label='Description of the bug', style=discord.TextStyle.paragraph)

    async def on_submit(self, interaction: discord.Interaction):
        channel = client.get_channel(1043931423360430190)
        embed = discord.Embed(title=":bug: Bug report :bug:")
        embed.add_field(name="Bugged Command name", value=self.children[0].value)
        #embed.add_field(name="Type of bug", value=self.children[1].value)
        embed.add_field(name="Description of the bug", value=self.children[1].value)
        embed.add_field(name="User:", value=f"`{interaction.user}`")
        await channel.send(embed=embed)
        embed1 = discord.Embed(title="Bug report sent", color=discord.Color.red())
        embed1.set_footer(text=footer_testo)
        await interaction.response.send_message(embeds=[embed1], ephemeral=True)


#-Verify
	
class Button(discord.ui.View):
	def __init__(self):
		super().__init__()
		self.value = None

	@discord.ui.button(label="Verify", style=discord.ButtonStyle.green)
	async def Button1(self, interaction: discord.Interaction, button: discord.ui.Button):
		ctx=interaction
		if discord.utils.get(ctx.guild.roles, name="verify"):
			#if get(message.guild.roles, name="verify"):
			role = discord.utils.get(ctx.guild.roles, name="verify")
			pearson = interaction.user
			await pearson.add_roles(role)
			embed_verify=discord.Embed(title=f"You are now verify", color=discord.Color.green())
			embed_verify.set_footer(text=footer_testo)  
			await interaction.response.send_message(embed=embed_verify, ephemeral=True)
		else:
			permissions = discord.Permissions(send_messages=True, read_messages=True)
			guild = interaction.guild
			await guild.create_role(name="verify", colour=discord.Colour(0x00ff00), permissions=permissions)
			role = discord.utils.get(ctx.guild.roles, name="verify")
			for channel in ctx.guild.channels:
				permissions = discord.PermissionOverwrite(send_messages=True, read_messages=True, speak=True)
				await channel.set_permissions(role, overwrite=permissions)
				role1 = discord.utils.get(ctx.guild.roles, name="@everyone")
				permissions1 = discord.PermissionOverwrite(send_messages=False, read_messages=True, speak=False)
				await channel.set_permissions(role1, overwrite=permissions1)
			await ctx.user.add_roles(role)
			

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


#-Help
		
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
			embed.add_field(name=f"{prefix}lockdown", value=f"Lockdown all channel", inline=True)
			embed.add_field(name=f"{prefix}unlock", value=f"Unlock channel", inline=True)
			embed.add_field(name=f"{prefix}mute `user_id`", value=f"Mute a member", inline=True)
			embed.add_field(name=f"{prefix}unmute `user_id`", value=f"Unmute a member", inline=True)
			embed.add_field(name=f"{prefix}slowmode `seconds`", value=f"Unmute a member", inline=True)
			embed.set_footer(text=footer_testo)
			await interaction.response.send_message(embed=embed, ephemeral=True)
		elif self.values[0] == "Utilty Commands":
			embedt = discord.Embed(title="Utilty :chart_with_downwards_trend:", color=discord.Color.green())
			embedt.add_field(name=f"{prefix}infobot", value="Send the bot stats (cpu, memory, ping)", inline=True)
			embedt.add_field(name=f"{prefix}chat `request`", value="Answer your questions using Openai", inline=True)
			embedt.add_field(name=f"{prefix}serverinfo", value="Send the server info", inline=True)
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
			embedd.add_field(name=f"{prefix}generate_image `request`", value="Generate image using Openai", inline=True)
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
			embed.set_footer(text=footer_testo)
			await interaction.response.send_message(embed=embed, ephemeral=True)

		

#-Manutenzione
		
class Admin_Button_View(discord.ui.View):
	def __init__(self):
		super().__init__()
		self.value = None

	@discord.ui.button(label="Off", style=discord.ButtonStyle.red)
	async def Off_Amin_Button(self, interaction: discord.Interaction, button: discord.ui.Button):
		if interaction.user.id == my_id:
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
		if interaction.user.id == my_id:
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
async def play(interaction: discord.Interaction, url: str):
	global filename
	if interaction.user.voice is None:
		embed = discord.Embed(title="*** You are not currently in a voice channel. ***", color=discord.Colour.red())
		embed.set_footer(text=footer_testo)
		await interaction.response.send_message(embed=embed, ephemeral=True)
	else:
		if interaction.guild.voice_client is not None and interaction.guild.voice_client.is_playing():
			no_music_embed = discord.Embed(title="*** Please wait until the song is finished to start another one, If you want to stop the song you can use </stop:1114604126861525132> ***", color=discord.Colour.red())
			no_music_embed.set_footer(text=footer_testo)
			await interaction.response.send_message(embed=no_music_embed, ephemeral=True)
		else:
			#else:
			try:
				if url.startswith("https://youtu.be/"):
					share_video_id = url.replace("https://youtu.be/", "")
					share_video_url = "youtube.com/watch?v=" + f"{share_video_id}"
					loading_embed = discord.Embed(title=":arrows_clockwise: Downloading song :musical_note:", color=discord.Colour.blue())
					loading_embed.set_footer(text=footer_testo)
					await interaction.response.send_message(embed=loading_embed, ephemeral=True)
					
					#find-video
					video = pytube.YouTube(share_video_url)
					
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
					
					filename = f"{file_name}"
	
					#video-info-embed
					title_embed = discord.Embed(color=discord.Colour.blue())
					title_embed.set_image(url=video.thumbnail_url)
					title_embed.description = f"***Now playing:*** \n\n***Title: ***`{video.title}`\n\n`{artist}` \n\n `{minutes}:{seconds}` ** :arrow_backward:     :pause_button:     :arrow_forward: **"
					title_embed.set_footer(text=footer_testo)
					await interaction.edit_original_response(embed=title_embed)
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
					voice_channel = interaction.user.voice.channel
					voice = await voice_channel.connect()
					voice.play(source)
		
					#volume fix
					volume = 0.4
					voice_client = interaction.guild.voice_client
					voice_client.source.volume = volume
	
					# Wait for the video to finish playing
					while voice.is_playing():
						await asyncio.sleep(1)
	
					# Disconnect from the voice channel
					await voice.disconnect()
	
					# Delete the video file
					os.remove(f"{file_name}")
					end_embed = discord.Embed(title="***:cd: The song is ended***", color=discord.Colour.red())
					end_embed.set_footer(text=footer_testo)
					await interaction.edit_original_response(embed=end_embed)
					#pass
					#return
				else:
					#loading embed
					loading_embed = discord.Embed(title=":arrows_clockwise: Downloading song :musical_note:", color=discord.Colour.blue())
					loading_embed.set_footer(text=footer_testo)
					await interaction.response.send_message(embed=loading_embed, ephemeral=True)
					
					#find-video
					video = pytube.YouTube(url)
					
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
					
					filename = f"{file_name}"
	
					#video-info-embed
					title_embed = discord.Embed(color=discord.Colour.blue())
					title_embed.set_image(url=video.thumbnail_url)
					title_embed.description = f"***Now playing:*** \n\n***Title: ***`{video.title}`\n\n`{artist}` \n\n `{minutes}:{seconds}` ** :arrow_backward:     :pause_button:     :arrow_forward: **"
					title_embed.set_footer(text=footer_testo)
					await interaction.edit_original_response(embed=title_embed)
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
					voice_channel = interaction.user.voice.channel
					voice = await voice_channel.connect()
					voice.play(source)
		
					#volume fix
					volume = 0.4
					voice_client = interaction.guild.voice_client
					voice_client.source.volume = volume
	
					# Wait for the video to finish playing
					while voice.is_playing():
						await asyncio.sleep(1)
	
					# Disconnect from the voice channel
					await voice.disconnect()
	
					# Delete the video file
					os.remove(f"{file_name}")
					end_embed = discord.Embed(title="***:cd: The song is ended***", color=discord.Colour.red())
					end_embed.set_footer(text=footer_testo)
					await interaction.edit_original_response(embed=end_embed)
					#pass
					#return
					#error
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
	global filename #global
	
	voice_client = interaction.guild.voice_client
	if voice_client and voice_client.is_connected():
		if voice_client.is_playing():
			try:
				embed = discord.Embed(title=':cd: The song has been stopped', color=discord.Colour.red())
				embed.set_footer(text=footer_testo)
				await interaction.response.send_message(embed=embed, ephemeral=True)
				voice_client.stop()
				await voice_client.disconnect()
				#await asyncio.sleep(2)
				os.remove(f"{filename}") #global
			except Exception as e:
				pass
		else:
			try:
				embed = discord.Embed(title=':x: The bot has been disconnected', color=discord.Colour.red())
				embed.set_footer(text=footer_testo)
				await interaction.response.send_message(embed=embed, ephemeral=True)
				os.remove(f"{filename}") #global
				await voice_client.disconnect()
			except Exception as e:
				try:
					os.remove(f"{filename}")
				except Exception:
					pass
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
@client.command()
async def meme(ctx):
    data = requests.get('https://meme-api.herokuapp.com/gimme').json()
    meme = discord.Embed(title=f"{data['title']}", Color = discord.Colour.green().set_image(url=f"{data['url']}"))
    await ctx.send(embed=meme)
'''
'''
@client.event
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
'''



'''
@client.command()
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
'''	

		

'''

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
'''

'''
    @commands.command(name="testautomod")
    async def automod(self, ctx: commands.Context):
        auto_mod_trigger = discord.AutoModTrigger(
            type= discord.AutoModRuleTriggerType.keyword_preset,
            presets=discord.AutoModPresets(profanity=True))
        a_single_object_for_this = discord.AutoModRuleAction(custom_message=f"Profanity is not allowed for this server!")
        actions_list = [a_single_object_for_this]
        auto_mod_event = discord.AutoModRuleEventType.message_send
        await ctx.guild.create_automod_rule(name="Profanity Filter By Me lol", trigger=auto_mod_trigger, actions=actions_list, event_type=auto_mod_event)
'''

'''
#openai
import openai


@is_me
@client.command()
@commands.guild_only()
async def chat(ctx, *, request):
	async with ctx.typing():
		response = openai.Completion.create(
			engine="text-davinci-003", 
			prompt=request,
			temperature=0.7, #creativita' coerenza
			max_tokens=1000, #max parole
			top_p=0.85, #considera le possibilita' di risposta
			frequency_penalty=0.75, #penalizza uso parole comuni
			presence_penalty=0.6 #uso di parole specifiche(specializzate)
		)
		embed = discord.Embed(title=f"Request: ```{request}```", colour=discord.Color.blue())
		embed.set_footer(text=footer_testo)
		await ctx.send(embed=embed, content=f"```{response.choices[0].text}```")	

'''

'''
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
 
'''
#---------Test------------#
from bardapi import Bard

token = data["access_token"]
bard = Bard(token=token)


@is_beta
@client.command()
async def bard(ctx, message):
	out = bard.get_answer(message)['content']
	await ctx.send(out)






@is_beta
@client.command()
async def download(ctx, url):
		try:
			
			# Find the video
			video = pytube.YouTube(url)
			
			#loading embed
			loading_embed = discord.Embed(title=":arrows_clockwise: Downloading song :musical_note:", color=discord.Colour.blue())
			loading_embed.set_footer(text=footer_testo)
			loading = await ctx.send(embed=loading_embed)
			
			#title-file
			number = random.randint(110000, 100000000)
			extension = "mp4"
			file_name = f"{number}.{extension}"
			#video.streams.get_highest_resolution().download(filename=file_name)
			
			#download
			video.streams.first().download(filename=file_name)
			
			#info
			video_length = video.length
			minutes, seconds = divmod(video_length, 60)
			
			artist = video.author
			
			#loading delete
			await asyncio.sleep(0.5)
			await loading.delete()
			await asyncio.sleep(1)
			#video-info-embed
			title_embed = discord.Embed(color=discord.Colour.blue())
			title_embed.set_image(url=video.thumbnail_url)
			title_embed.description = f"***I have downloaded:*** \n\n***Title: ***`{video.title}`\n\n`{artist}` \n\n `{minutes}:{seconds}`"
			title_embed.set_footer(text=footer_testo)
			
			title_embed = await ctx.send(embed=title_embed, file=discord.File(f"{file_name}"))

			await asyncio.sleep(20)
				
			# Delete the video file
			os.remove(f"{file_name}")
			await title_embed.delete()
			#pass
			#return
			#error
		except pytube.exceptions.PytubeError as e:
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
				error_embed_4 = discord.Embed(title="***An error occurred while downloading the video.***", color=discord.Colour.red())
				error_embed_4.set_footer(text=footer_testo)
				await ctx.send(embed=error_embed_4, delete_after=5)
				await asyncio.sleep(0.5)
				#stalk
				channel = client.get_channel(errorchannel)
				await channel.send(f"**[Errore]** \naudio isinstance: (pytube) ```{e}```")



@is_beta
@client.command()
async def automod2(ctx):
	await ctx.guild.create_automod_rule(name="Spam Block",
					    event_type=AutoModRuleEventType.message_send,
					    trigger=AutomodTrigger.spam,
					    actions=[AutoModRuleActionType.block_message], enabled=True)




@is_beta
@client.command()
async def automod(ctx):
    # Crea un trigger personalizzato per la parola "spam"
    trigger = discord.AutoModTrigger(
        type=discord.AutoModRuleTriggerType.keyword,
        keyword_filter=["spam"]
    )

    # Crea un'azione personalizzata per bloccare i messaggi contenenti la parola "spam"
    action = discord.AutoModRuleAction(
        action_type=discord.AutoModRuleActionType.block_message,
        custom_message="Messaggi contenenti la parola 'spam' non sono ammessi in questo canale."
    )

    # Crea una regola di AutoMod personalizzata utilizzando il trigger e l'azione creati
    rule = discord.AutoModRule(
        name="spam_filter",
        event_type=discord.AutoModRuleEventType.message_send,
        trigger=trigger,
        actions=[action]
    )

    # Aggiungi la regola di AutoMod personalizzata al canale corrente
    await ctx.channel.create_automod_rule(rule=rule)

    # Invia un messaggio di conferma al canale
    await ctx.send("Regola di AutoMod creata con successo!")

	
@is_beta
@client.command()
async def verify(ctx):
	#reactions = ['✅'] # add more later if u want idk
	embed = discord.Embed(title="Click the button to verify", color=discord.Color.green())
	embed.set_footer(text=footer_testo)
	#View=VerifyButton()
	await ctx.send(embed=embed, view=Button())
	#await message.add_reaction("<:checkmark_2714fe0f:1073342463995023433>")

	


#----------Admin---------------#
import base64
from io import BytesIO
import io

@commands.cooldown(1, 10, commands.BucketType.user)
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



'''
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
'''

@client.command()
@commands.guild_only()
async def chat(ctx):
	embed = discord.Embed(title="`?chat` has been disabled\nTry to check announcements to know when the command will be reactivated", color=discord.Color.greyple())
	embed.set_footer(text=footer_testo)
	await ctx.send(embed=embed, delete_after=20)	


@commands.cooldown(1, 5, commands.BucketType.user)
@client.command()
@commands.guild_only()
async def help(ctx):
	embed = discord.Embed(title="`?help` has been disabled\nTry using </help:1094994368445816934>", color=discord.Color.greyple())
	embed.set_footer(text=footer_testo)
	await ctx.send(embed=embed, delete_after=20)


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
@commands.guild_only()
async def servers(ctx):
	try:
		message = "I server in cui sono stato invitato sono:\n\n"
		for guild in client.guilds:
			channel = guild.text_channels[0]
			#invite = await channel.create_invite()
			#message += f"*** `{guild.name}` (id: `{guild.id}`) membri: `{guild.member_count}`\n Link invito: ***[Url]({invite.url}) \n\n"
			message += f"*** `{guild.name}` (id: `{guild.id}`) membri: `{guild.member_count}`\n  *** \n"
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
	exit(1)

	

@client.command()
@is_me
async def manutenzione(ctx):
	embed = discord.Embed(title="Click the button to start or stop maintenance mode\nThis message would be deleted in 20 seconds", color=discord.Color.red())
	embed.set_footer(text=footer_testo)
	await ctx.send(embed=embed, view=Admin_Button_View(),delete_after=20)	

	
	

#return await ctx.invoke(client.bot_get_command("help"), entity="commandname")


#--------Presence------------#

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
		embed = discord.Embed(title="Error", color=discord.Color.red())
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
