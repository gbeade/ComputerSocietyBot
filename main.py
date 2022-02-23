import os
import csbot
import discord 


def main():
  intents = discord.Intents.default()
  intents.members = True
  bot = csbot.ComputerSocietyBot(
    command_prefix='$', 
    intents=intents
  )
  bot.load_extension("cogs.cog_greetings")
  bot.load_extension("cogs.cog_csxp") 
  bot.load_extension("cogs.cog_teams") 
  bot.load_extension("cogs.cog_general") 
  bot.run(os.environ['TOKEN'])

if __name__ == '__main__':
    main()