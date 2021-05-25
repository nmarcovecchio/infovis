import pandas as pd
from bs4 import BeautifulSoup
import re

# List to store the stats.
ls_all = []
ls_player = []
ls_score = []
ls_ping = []
ls_kill = []
ls_assist = []
ls_death = []
ls_mvp = []
ls_hsp = []
ls_match_score = []
ls_score = []

ls_map = []
ls_date = []
ls_waittime= []
ls_duration= []
ls_i = []

ls_team=[]

map = []
date = []
waittime= []
duration= []


def get_match_details():
  match_data = []
  with open('/content/drive/MyDrive/ITBA/Visualizacion de datos/Datos Personales/personal_data/Comunidad Steam __ Counter-Strike_ Global Offensive __ Datos de juego personales.html', encoding='utf8') as file:
    # Parse.
    soup = BeautifulSoup(file, 'html.parser')
    # Find main class.
    table_ = soup.find(class_='generic_kv_table csgo_scoreboard_root')
    # Find sub class.
    table = table_.find_all(class_='csgo_scoreboard_inner_left')
    # Get data for each match.
    for i in range(0, len(table)):
        #print(i)
        for row in table[i].find_all('td'):
          if 'Download'  in row.get_text().strip():
            continue 
          if 'Viewers' in row.get_text().strip():
            continue
          #print(row.get_text().strip())
          match_data.append(row.get_text().strip())

  # Appending individual stats of all players.
  for i in range(0, len(match_data),4):
      map.append(match_data[i])
      date.append(match_data[i + 1])
      waittime.append(match_data[i + 2])
      duration.append(match_data[i +3 ])
  return
  
#csgo_scoreboard_inner_left
get_match_details()

# Open the page.
with open('/content/drive/MyDrive/ITBA/Visualizacion de datos/Datos Personales/personal_data/Comunidad Steam __ Counter-Strike_ Global Offensive __ Datos de juego personales.html', encoding='utf8') as file:
    # Parse.
    soup = BeautifulSoup(file, 'html.parser')
    # Find main class.
    table_ = soup.find(class_='generic_kv_table csgo_scoreboard_root')
    # Find sub class.
    table = table_.find_all(class_='csgo_scoreboard_inner_right')
    # Get data for each match.
    for i in range(0, len(table)):
        for row in table[i].find_all('td'):
            if row.find('a'):
                name = row.get_text().strip()
                # Append name of the players.
                ls_player.append(name)
            # Match Score
            elif "colspan" in row.attrs:
                # print(row.get_text())
                ls_match_score.append(row.get_text().strip())
            # Game stats.
            else:
                # print(row.get_text())
                ls_all.append(row.get_text().strip())
LS_matchscore = []
#print(map)
n=0
k=0
# Appending individual stats of all players.
for i in range(0, len(ls_all), 7):
    

    ls_ping.append(ls_all[i])
    ls_kill.append(ls_all[i + 1])
    ls_assist.append(ls_all[i + 2])
    ls_death.append(ls_all[i + 3])
    ls_all[i+4] = ls_all[i+4].replace('★', '')
    ls_mvp.append(ls_all[i + 4])
    ls_all[i + 5] = ls_all[i + 5].replace('%', '')
    ls_hsp.append(ls_all[i + 5])
    ls_score.append(ls_all[i + 6])
    
    
for n in range(0,40):
    for k in range(0,10):
      if(k>=5):
        ls_team.append(1)
      else:
        ls_team.append(0)
      ls_i.append(n)
      ls_map.append(map[n])
      ls_date.append(date[n])
      ls_waittime.append(waittime[n])
      ls_duration.append(duration[n])
      LS_matchscore.append(ls_match_score[n])



# Created a DataFrame for easy manipulation.
df = pd.DataFrame()

df['Match index'] = ls_i
df['Team'] = ls_team
df['Player Name'] = ls_player
df['Ping'] = ls_ping
df['Kills'] = ls_kill
df['Assists'] = ls_assist
df['Deaths'] = ls_death
df['MVP'] = ls_mvp
df['HSP'] = ls_hsp
df['Score'] = ls_score
df['Map'] = ls_map
df['Duration'] = ls_duration
df['Wait time'] = ls_waittime
df['Date'] = ls_date
df['Match Score'] = LS_matchscore

# Replace blank space with zero.
df = df.replace(r'^\s*$', 0, regex=True)
print(df)
# Save the data to a CSV file.
df.to_csv('CSGO_Data.csv')
