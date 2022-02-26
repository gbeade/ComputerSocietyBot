import discord.ext.commands as commands
import data.ctf as data


"""CTF commands."""
class Ctf(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot
    
  @commands.group(name="ctf", invoke_without_command=True)
  async def ctf(self, ctx: commands.Context):
    res = ""
    for x in data.get_categories():
      res += "Category: "+x+" ["+x[:5].upper()+"]\n"
      res += str(data.get_challenges_by_cat(x))+"\n"
    await ctx.send(res)

  @ctf.command(name="push")
  async def push(self, ctx: commands.Context, cat: str, chllg: str, dsc:str, flag:str, diff:str):
    data.push_challenge(cat, chllg, dsc, flag, diff)
    await ctx.send("Challenge ["+chllg+"] created!\n")


  @ctf.command(name="rmv")
  async def rmv(self, ctx: commands.Context, cat: str, chllg: str, diff:str):
    data.del_challenge(cat, diff, chllg)
    await ctx.send("Challenge ["+chllg+"] removed!\n")


def setup(bot: commands.Bot):
    print("> Setting up CTF module")
    bot.add_cog(Ctf(bot))