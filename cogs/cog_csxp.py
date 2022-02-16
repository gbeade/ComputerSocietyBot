import discord.ext.commands as commands
import data.csxp as data
import random 

"""Commands for administrating CSXP."""
class Csxp(commands.Cog):
    def __init__(self, bot: commands.Bot):
      self.bot = bot

    @commands.group(name="csxp", invoke_without_command=True) 
    async def csxp(self, ctx: commands.Context, msg = ""): 
      await ctx.send("Root command: csxp")
 
    @csxp.command(name="leaderboard")  # subcommand
    async def leaderboard(self, ctx: commands.Context):
      strn = "🏆 CSXP Leaderboard 🏆\n"
      strn += "---------------------------------\n"
      # TODO: ordenar por cantidad de puntos y poner emojis del podio 
      for x in ctx.guild.members: 
        strn += "[@{0}]: {1} CSXP\n".format(
          x.name, 
          data.fetch_csxp(x.name)
        )
      await ctx.send(strn)

    def coinflip(self):
        return 
      
    @csxp.command(name="gamble")  # subcommand
    async def gamble(self, ctx: commands.Context, q: int):
      if q is None: 
        return
      x = ctx.author
      p = int(data.fetch_csxp(x.name))
      if q > p: 
        await ctx.send("You can't bet more CSXP than what you have!")
      elif p == 0: 
        await ctx.send("You can't bet if you don't have CSXP!")
      else:
        coin = random.randint(0, 1)
        if coin == 1: 
          t = data.inc_csxp(ctx.author.name, q)
          await ctx.send(
            "You won "+
            str(q)+
            " CSXP! Congrats!\nYour balance is now: "+
            str(t)+
            " CSXP"
          )
        else: 
          t = data.dec_csxp(ctx.author.name, q)
          await ctx.send(
            "You lost "+
            str(q)+
            " CSXP!\nYour new balance is now: "+
            str(t)+
            " CSXP"
          )

        
            
        


      



def setup(bot: commands.Bot):
    print("> Setting up CSXP module")
    bot.add_cog(Csxp(bot))