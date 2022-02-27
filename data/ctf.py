from replit import db 

def add_category(category, prefix): 
  if len(prefix) > 3: 
    return 
    
  if "ctf_cats" not in db.keys(): 
    db["ctf_cats"] = {} 
  
  db["ctf_cats"][prefix] = category

def rmv_category(prefix): 
  if "ctf_cats" not in db.keys(): 
    return
  del db["ctf_cats"][prefix]

def get_categories():
  if "ctf_cats" not in db.keys(): 
    return {}
  return db["ctf_cats"] # returns a map 

def push_challenge(cat_code=None, name=None, desc=None, flag=None, diff=1):

  if diff < 1 or diff > 9: 
    return None

  if db["ctf_cats"][cat_code] is None: 
    return None 
    
  if "ctf_challs" not in db.keys(): 
    db["ctf_challs"] = {}

  if cat_code not in db["ctf_challs"].keys(): 
    db["ctf_challs"][cat_code] = {}   


  # esto es medio JS, deberia hacer una clase Challenge? 
  id = str(len(db["ctf_challs"][cat_code]))
  chllg_code = cat_code+str(diff)+"0"+id
  db["ctf_challs"][cat_code][chllg_code] = {}
  chllg = db["ctf_challs"][cat_code][chllg_code]
  chllg["diff"] = diff
  chllg["name"] = name
  chllg["desc"] = desc
  chllg["flag"] = flag
  chllg["solved_by"] = None

  return chllg_code

''' Returns dict with each challenge code as key and a map with its data as value'''
def get_challenges(cat_code):
  if "ctf_challs" not in db.keys() or \
    cat_code not in db["ctf_challs"].keys(): 
      return {} 

  return db["ctf_challs"][cat_code]

def try_solve(author, chllg_code, flag):

  cat_code = chllg_code[:3]
  if "ctf_challs" not in db.keys() or \
    cat_code not in db["ctf_challs"].keys(): 
      return None, None

  chllg = db["ctf_challs"][cat_code][chllg_code]
  if chllg["solved_by"] is None and \
    chllg["flag"] == flag: 
      chllg["solved_by"] = author
      return "", chllg["diff"]


  return chllg["solved_by"], None


def get_challenge_data(chllg): 
  return db["ctf_challs"][chllg[:3]][chllg]
  
  



  
