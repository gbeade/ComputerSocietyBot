import discord.ext.commands as commands
import data.csxp as data
import random 

"""Commands for administrating CSXP."""
class Csxp(commands.Cog):
    def __init__(self, bot: commands.Bot):
      self.bot = bot

    def getScore(self,member):
      return data.fetch_csxp(member.name)
              
    @commands.group(name="csxp", invoke_without_command=True) 
    async def csxp(self, ctx: commands.Context, msg = ""): 
      await ctx.send(
        "<@{0}> You have {1} CSXP.".format(
          ctx.author.id, 
          self.getScore(ctx.author)
        ))
 
    @csxp.command(name="leaderboard")  # subcommand
    async def leaderboard(self, ctx: commands.Context):
      strn = "🏆 CSXP Leaderboard 🏆\n"
      strn += "---------------------------------\n"
      medals = ["🥇","🥈","🥉"]
      idAndScore = list(map(lambda x: [x.id,self.getScore(x)],ctx.guild.members))
      for idx,[id,score] in enumerate(sorted(idAndScore,key=lambda x: x[1], reverse=True)): 
        strn += "[<@{0}>]: {1} CSXP {2}\n".format(
          id, 
          score,
          medals[idx] if idx <= 2 else ""
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
      elif q > 10: 
        await ctx.send("You can't bet more than 10 CSXP.")
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

    @csxp.command(name="faucet")
    async def faucet(self, ctx: commands.Context): 
      t = data.inc_csxp(ctx.author.name, 1) 
      await ctx.send("Here's 1 CSXP! Your current balance is now: "+ str(t))

      



def setup(bot: commands.Bot):
    print("> Setting up CSXP module")
    bot.add_cog(Csxp(bot))