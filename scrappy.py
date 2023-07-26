import requests
from bs4 import BeautifulSoup
import pandas as pd


class Scrapper():

    def __init__(self, link, headers):
        self.link = link
        self.headers = headers 
        self.site = requests.get(self.link, headers = self.headers)
        self.soup = BeautifulSoup(self.site.content, 'html.parser')
    

    def makeCols(self) :

        header = self.soup.find('thead')
        titulos = header.find_all('tr')
        Titulos = titulos[1].find_all('th')


        list_columns =[]
        for a in range(1, 36):
            status = Titulos[a].get_text().strip()
            list_columns.append(status)

        return  list_columns
    

    def makeContent(self, num_inicial, num_final):

        players_list = []
        table = self.soup.find('tbody')
        rows = table.find_all('tr')
        

        for number in range(25, 2775, 25):
            rows.pop(number)
        
        for i in range(num_inicial, num_final):
            jogador = rows[i].find_all('td')
            
            for j in range(0, 35):
                player_stats = jogador[j].get_text().strip()
                players_list.append(player_stats)

        return players_list
    
    