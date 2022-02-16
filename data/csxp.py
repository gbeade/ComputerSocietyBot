from replit import db


def _val_db(member): 
  if "csxp" not in db.keys():
    db["csxp"] = {}
  if member not in db["csxp"].keys(): 
    db["csxp"][member] = 0
  
def fetch_csxp(member): 
  _val_db(member)  
  return db["csxp"][member]

def inc_csxp(member, csxp): 
  _val_db(member)
  db["csxp"][member] += csxp
  return db["csxp"][member]

def dec_csxp(member, csxp): 
  _val_db(member)
  r = db["csxp"][member] - csxp
  if r >= 0: 
    db["csxp"][member] -= csxp
  return db["csxp"][member]

