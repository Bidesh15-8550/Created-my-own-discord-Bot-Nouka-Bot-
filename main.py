import discord
import os
import requests
import json
import random

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable","depressing"]

starter_encouragements = [
  "Cheer Up!",
  "I am sad too",
  "You are a great person!"
]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -"+ json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  msg = message.content

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')
  if message.content.startswith('$:3'):
    await message.channel.send('🥴🥴')
  if message.content.startswith('$you are smart'):
    await message.channel.send('I know 😜')
  if message.content.startswith('$halar po'):
    await message.channel.send('Fuck You')
  if message.content.startswith('$fuck you'):
    await message.channel.send('Fuck You Too ❤️‍🔥')
  if message.content.startswith('$shit'):
    await message.channel.send("😈😈")
  if message.content.startswith('$uninspire'):
    await message.channel.send("Die! You're good for nothing")

  if msg.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)
  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encouragements))

client.run(os.getenv('TOKEN'))
