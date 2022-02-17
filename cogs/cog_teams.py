import discord.ext.commands as commands
import data.teams as data

"""Commands for administrating teams."""
class Csxp(commands.Cog):
    def __init__(self, bot: commands.Bot):
      self.bot = bot

    @commands.group(name="teams", invoke_without_command=True) 
    async def teams(self, ctx: commands.Context, msg = ""): 
      t = "🤝 TEAMS 🤝\n"
      t += "-------------------------\n"
      for x in data.fetch_teams(): 
        t += (x+"\n")
        mems = ""
        for y in data.fetch_team_members(x):
          mems += ("\t\t⚬<@"+y+">\n")
        t += mems if mems else '\t\t(empty)\n'
      await ctx.send(t)
      return
     
    @teams.command(name="signup")  # subcommand
    async def signup(self, ctx: commands.Context, team):
      data.signup_to(team, ctx.author.id)
      await ctx.send("<@{0}>, welcome to [{1}]".format(
        ctx.author.id, 
        data.fetch_team_from_member(ctx.author.id)
      ))

    @teams.command(name="quit")  # subcommand
    async def quit(self, ctx: commands.Context):
      t = data.fetch_team_from_member(ctx.author.id)
      t = "<@{0}> quit [{1}]".format(ctx.author.id, t) if t else "No team to quit!"   
      await ctx.send(t)


    @teams.command(name="mine")  # subcommand
    async def mine(self, ctx: commands.Context):
      team = data.fetch_team_from_member(ctx.author.id)
      if team is None: 
        await ctx.send("<@{0}>, you don't belong to any team.".format(
          ctx.author.id
        )) 
      else: 
        await ctx.send("<@{0}>, you belong to team [{1}]".format(
          ctx.author.id,
          team
      ))

    


      
     
def setup(bot: commands.Bot):
    print("> Setting up Teams module")
    bot.add_cog(Csxp(bot))