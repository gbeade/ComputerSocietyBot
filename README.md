# ComputerSocietyBot
A Discord bot for IEEE's Computer Society chapter @ ITBA, Buenos Aires, Argentina. 

## Setting up the bot in a Discord server
Authorize the bot at https://discord.com/oauth2/authorize?client_id=943286355281207347&permissions=1249785670769&scope=bot and select a server. 

## Starting the bot 
Pull and and run main.py in https://replit.com/join/kbtdgynilq-gonzalomanuelma. A future version will allow the bot to run forever, but for now the bot must be manually booted after one hour of inactivity. The replit acts as a server so that it depends on no computer and can be turned on/off from anywhere. 

## Using the bot 
All commands are prefixed by a '$' symbol. 

### Debugging
- ``$inspire``: replies with a motivational phrase 

### CSXP 
CSXP refers to Computer Society's Experience Points. CSXP can be tracked by, awarded to or removed from any user in the server where the bot has been set up. 
- ``$csxp``: replies with the sender's current CSXP. 
- ``$csxp leaderboard``: replies with the server's members' CSXP.
- ``$csxp faucet``: gives the user 1 CSXP
- ``$csxp gamble <q>``: bets q units of CSXP with a .5 chance of doubling and a .5 chance of losing. 
  
### Teams 
Teams are member subgroups inside the Bot's scope in a server. A member can only belong to one team. 
 
- ``$teams``: replies with all teams and their members, if any. 
- ``$teams signup <team>``: signs a user to a team. If the team does not exist, the team may be created at runtime if it does not exist (if the supervisor allowed it)
- ``$teams quit``: removes the user from its current team, if any. 
- ``$teams mine``: replies with the user's current team, if any. 
  
  ####TODO: 
- ``$teams creat_runtime <boolean>`` (privileged): determines whether a team can be created at runtime by an ordinary member 
- ``$teams create <team>`` (privileged): creates a new empty team

### Trivia
Members can play a sequential trivia of increasing difficulty. The more questions correctly answered, the more difficult the next questions are. Tougher questions give out more CSXP. Trivia must be turned on and filled with questions by priviledged users. 

  ####TODO
- ``$trivia push <question> <answer> <difficulty>`` (privileged): pushes a question with a certain difficulty (1-10, where 1 is the easiest) and its answer to the database.
- ``$trivia``: replies with the next question in the queue. 
- ``$trivia <answer>``: submits and answer to the current active question. It is rejected if incorrect; CSXP is gained and next question is dequeued if correct. 

### Capture The Flag
Members are shown several challenges that are to be solved. Each challenge has a code and a flag that is to be found. The more difficult a challenge is, the more CSXO it returns. 

  ####TODO
- ``$ctf push <category_code> <name> <description> <flag> <difficulty>`` (privileged): pushes a challenge with a certain difficulty (1-10, where 1 is the easiest) and its flag to the database.
- ``$ctf``: replies with all challenges and their codes. 
- ``$ctf <code> <flag>``: submits the flag to a challenge. It is rejected if incorrect; CSXP is gained if correct. 





