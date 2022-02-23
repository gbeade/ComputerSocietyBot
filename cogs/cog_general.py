import discord.ext.commands as commands
from data.miscellaneous import end_time
from datetime import datetime, timezone

"""General commands."""
class General(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot
    
  @commands.command(name="time")
  async def time(self, ctx: commands.Context):
    now = datetime.now(timezone.utc) 
    await ctx.send(str(end_time-now).split(".")[0] + " left until its over! ⏱")

def setup(bot: commands.Bot):
    print("> Setting up General module")
    bot.add_cog(General(bot))