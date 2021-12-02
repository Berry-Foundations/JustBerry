# JustBerry

import discord
import os

client = discord.Client()

@client.event
async def on_ready():
	client.change_presence(activity=discord.Game("Nothing"))

try:
	token = os.getenv("token")
	client.run(token)
except Exception as error:
	print(error)

