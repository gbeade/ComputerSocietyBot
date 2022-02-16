from discord.ext import commands


# Actions that depend on events and not on commands should be described
# in the ComputerSocietyBot class
class ComputerSocietyBot(commands.Bot):
  
    async def on_ready(self):
      print(f'{self.user} bot user is ready to rumble!')
      
