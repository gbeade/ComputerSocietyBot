import discord.ext.commands as commands
import data.miscellaneous as misc

"""A couple of simple commands."""
class Greetings(commands.Cog):
    def __init__(self, bot: commands.Bot):
      self.bot = bot

    @commands.command(name="hey")
    async def hey(self, ctx: commands.Context):
      await ctx.send("Hey, "+ctx.author.name+"!")

    @commands.command(name="inspire")
    async def inspire(self, ctx: commands.Context): 
      await ctx.send(misc.get_quote())

def setup(bot: commands.Bot):
    print("> Setting up Greetings module")
    bot.add_cog(Greetings(bot))

  