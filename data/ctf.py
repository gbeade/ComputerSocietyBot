from replit import db 

def add_category(category, prefix): 
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
    
  if "ctf_challs" not in db.keys(): 
    db["ctf_challs"] = {}

  if cat_code not in db["ctf_challs"].keys(): 
    db["ctf_challs"][cat_code] = {}

  # esto es medio JS, deberia hacer una clase Challenge? 
  id = str(len(db["ctf_challs"][cat_code]))
  db["ctf_challs"][cat_code]["diff"] = diff
  db["ctf_challs"][cat_code]["name"] = name
  db["ctf_challs"][cat_code]["desc"] = desc
  db["ctf_challs"][cat_code]["flag"] = flag
  db["ctf_challs"][cat_code]["id"] = id
  
  return cat_code+str(diff)+"0"+id

def get_challenges(cat_code):
  if "ctf_challs" not in db.keys() or \
    cat_code not in db["ctf_challs"].keys(): 
      return None 

  return db["ctf_challs"][cat_code]
  



  
