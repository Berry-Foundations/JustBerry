# JustBerry

import discord
import os
import server

client = discord.Client()

@client.event
async def on_ready():
	print(f"{client.user} ready!")
	try:
		await client.change_presence(activity=discord.Game("Nothing"))
	except Exception as error:
		print(error)
	server.super_run()

@client.event
async def on_message(ctx):
	embed = discord.Embed(
		title = "JustBerry",
		description = "Just A Berry Bot!",
		color = 0xffffff
	)
	embed.set_image(url=client.user.avatar_url)
	embed.set_footer(
		text = "Berry Foundations - Attachment Studios",
		icon_url = "https://images-ext-1.discordapp.net/external/x_dF_ppBthHmRPQi75iuRXLMfK0wuAW2sBLTdtNlXAc/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/894098855220617216/d9b9a3b48a054b9847401bb9178ed438.webp"
	)
	if ctx.content.lower().split(" ")[0] in ["justberry", "<@915973222229504001>", "<@!915973222229504001>", "jb"]:
		await ctx.channel.send(embed=embed)

try:
	token = os.getenv("token")
	client.run(token)
except Exception as error:
	print(error)

