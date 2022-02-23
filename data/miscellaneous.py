import requests 
import json 
from datetime import datetime 

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

end_time = datetime.fromisoformat('2022-04-03 13:00:00.283-03:00')
