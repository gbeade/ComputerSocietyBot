from replit import db

def fetch_csxp(username): 
  if "csxp" not in db.keys():
    db["csxp"] = {}

  if username not in db["csxp"].keys(): 
    db["csxp"][username] = 0
    
  return db["csxp"][username]

def inc_csxp(username, csxp): 
  if "csxp" not in db.keys():
    db["csxp"] = {}

  if username not in db["csxp"].keys(): 
    db["csxp"][username] = 0

  db["csxp"][username] += csxp
  return db["csxp"][username]

def dec_csxp(username, csxp): 
  if "csxp" not in db.keys():
    db["csxp"] = {}

  if username not in db["csxp"].keys() or db["csxp"][username] == 0 : 
    db["csxp"][username] = 0
    return 

  db["csxp"][username] -= csxp
  return db["csxp"][username]

