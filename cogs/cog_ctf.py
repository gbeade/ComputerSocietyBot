import discord.ext.commands as commands
import data.ctf as data


"""CTF commands."""
class Ctf(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot
    
  @commands.group(name="ctf", invoke_without_command=True)
  async def ctf(self, ctx: commands.Context):
    res = "🚩 **Computer Society's Capture The Flag** 🚩\n\n"
    for prefix, category in data.get_categories().items():
      res += "\t{0} [{1}]\n".format(
        category, prefix
      )
      for chllg_code, chllg_data in data.get_challenges(prefix).items():
        if chllg_data["solved_by"] is not None: 
          icon, solve = "✅", " - 🏆<@{0}>".format(chllg_data["solved_by"])
        else:
          icon, solve = "❌", ""
        res += "\t\t{0} [{1}] {2} {3}\n".format(
          icon, chllg_code, chllg_data["name"], solve
        )
      res += "\n"
        
    await ctx.send(res)

  @ctf.command(name="newcat")
  async def newcat(self, ctx: commands.Context, category: str, prefix:str):
    data.add_category(category, prefix)
    await ctx.send("Category [{0}] created! \n".format(prefix))

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


  @ctf.command(name="solve")
  async def try_solve(self, ctx: commands.Context, chllg_code: str, flag:str):
    author, diff = data.try_solve(ctx.author.id, chllg_code, flag)
    if author == "": 
      await ctx.send("You solved challenge [{0}]! You won {1} CSXP".format(chllg_code, int(diff)*100))
    elif author == None: 
      await ctx.send("Challenge [{0}] does not exist!".format(chllg_code))
    else: 
      await ctx.send("Challenge [{0}] has already been solved by @<{0}>".format(author))

  @ctf.command(name="more")
  async def more(self, ctx: commands.Context, chllg_code: str):
    chllg = data.get_challenge_data(chllg_code)
    res = "**Challenge {}**\n*{}* ({} CSXP)\n------------\n".format(chllg_code, chllg["name"].upper(), chllg["diff"]*100)
    res += "*Solved by*: {0}\n".format(
      None if chllg["solved_by"] is None else "<@"+str(chllg["solved_by"])+">"
    )
    res += "*How to find the flag:*\n" 
    res += chllg["desc"]
    await ctx.send(res)

      

      



def setup(bot: commands.Bot):
    print("> Setting up CTF module")
    bot.add_cog(Ctf(bot))