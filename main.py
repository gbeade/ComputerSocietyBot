# Mirar el video para ver que esta pasando:
# https://www.youtube.com/watch?v=SPTfmiYiuok

import os
import discord
import requests
import json
import random
from replit import db
import csxp
# from keep_alive import keep_alive
# TODO: implement keep_alive 

intents = discord.Intents().all()
client = discord.Client(prefix = '', intents=intents)

def fetch_csxp(username): 
  if "csxp" not in db.keys():
    db["csxp"] = {}

  if username not in db["csxp"].keys(): 
    db["csxp"][username] = 0
    
  return db["csxp"][username]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)
 
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  msg_ary = message.content.split() 
  cmd = msg_ary[0]

  if cmd == '$hello':
    await message.channel.send("Hello "+message.author.name+"!")

  if cmd == '$inspire':
    quote = get_quote()
    await message.channel.send(quote)

  if cmd == "$csxp":
    if (len(msg_ary)) == 1:
      await message.channel.send(
        "[@{0}]: {1} CSXP".format(message.author.name, 
        fetch_csxp(message.author.name) )
      )
    elif msg_ary[1] == "leaderboard": 
      str = "🏆 CSXP Leaderboard 🏆\n"
      str += "------------------------\n"
      for x in message.guild.members: 
        str += "[@{0}]: {1} CSXP\n".format(x.name,fetch_csxp(x.name))
      await message.channel.send(str)
      
# keep_alive()
client.run(os.environ['TOKEN'])


