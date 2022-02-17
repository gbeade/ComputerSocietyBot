from replit import db

def _val_db(team): 
  if "teams" not in db.keys():
    db["teams"] = {}
  if team not in db["teams"].keys(): 
    db["teams"][team] = {}

def signup_to(team, member):
  _val_db(str(team))
  db["teams"][str(team)][str(member)] = ""

def quit(member):
  team = fetch_team_from_member(str(member))
  if team is not None: 
    del db["teams"][team][str(member)]

# improve! 
def fetch_team_from_member(member): 
  for x in db["teams"].keys():
    for y in db["teams"][x].keys():
      if y == str(member): 
        return x
  return None
  
def fetch_teams(): 
  return db["teams"].keys() 

def fetch_team_members(team): 
  return db["teams"][str(team)].keys() 

