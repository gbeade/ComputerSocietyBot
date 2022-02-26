from replit import db 

def _val_db(category, difficulty): 
  if "ctf" not in db.keys():
    db["ctf"] = {}
  if category not in db["ctf"].keys(): 
    db["ctf"][category] = {}
  if difficulty not in db["ctf"][category].keys():
    for dif in range(1, 11):
      db["ctf"][category][] = []


def push_challenge(cat, code, chllg, desc, flag, diff):
  _val_db(cat, diff)
  chllgs= db["ctf"][cat][diff]
  chllgs[code] = [chllg, desc, flag]


def get_challenges_by_cat(cat):
  res = ""
  for dif in range(1, 11):
    chllgs = db["ctf"][cat][str(dif)]
    
    for c in chllgs.keys():
      res += "\t"+c+" - " +chllgs[c][0]+"\n"

  return res 

def get_categories():
  return db["ctf"].keys()

def del_challenge(category, difficulty, code): 
  del db["ctf"][category][difficulty][code]
  if len(db["ctf"][category][difficulty].keys()) < 1: 
    db["ctf"][category][difficulty] = {}
  
  
def solve()