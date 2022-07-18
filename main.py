import discord
import os

disc_token = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as user {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$help'):
    await message.channel.send('WIP')

client.run(disc_token)
