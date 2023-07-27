import pandas as pd
from scrappy import Scrapper

url = 'https://fbref.com/en/comps/Big5/stats/players/Big-5-European-Leagues-Stats'
headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

players = Scrapper(url, headers)



dicionario = players.createDict(0,3004)
df = pd.DataFrame(dicionario)

df.drop(['xG', 'npxG', 'xAG', 'npxG+xAG', 'PrgC', 'PrgP', 'PrgR',
       'G+A-PK', 'xG+xAG'], inplace= True, axis= 1)
df.to_csv('C:\\Users\\alexa\\OneDrive\\Documents\\a_soccer_table_scrapper\\output\\2022-2023_footbal_players_status.csv')