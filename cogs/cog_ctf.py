import discord.ext.commands as commands
import data.ctf as data


"""CTF commands."""
class Ctf(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot
    
  @commands.group(name="ctf", invoke_without_command=True)
  async def ctf(self, ctx: commands.Context):
    res = "Categories\n"
    for prefix, category in data.get_categories().items():
      res += "\t{0} [{1}]\n".format(
        category, prefix
      )
    await ctx.send(res)

  @ctf.command(name="newcat")
  async def newcat(self, ctx: commands.Context, category: str, prefix:str):
    data.add_category(category, prefix)

  @ctf.command(name="push")
  async def push(
    self, ctx: commands.Context, 
    cat_code: str, 
    name: str, 
    desc: str, 
    flag: str, 
    diff: int
  ):
    m = data.push_challenge(
      cat_code=cat_code, 
      name=name, 
      desc=desc, 
      flag=flag, 
      diff=diff
    )

    if m is not None: 
      await ctx.send("Challenge [{0}] pushed".format(m))
    else: 
      await ctx.send("There was an error pushing the challenge")


    
      



def setup(bot: commands.Bot):
    print("> Setting up CTF module")
    bot.add_cog(Ctf(bot))