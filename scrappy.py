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
        cols = titulos[1].find_all('th')
        cols.pop()
        cols.pop(0)
        num_cols = len(cols)


        list_columns =[]
        for a in range(0, num_cols):
            status = cols[a].get_text().strip()
            list_columns.append(status)

        return  list_columns
    

    def makeContent(self, num_inicial, num_final):

        players_list = []
        table = self.soup.find('tbody')
        rows = table.find_all('tr')
        num = len(self.makeCols())
        

        for number in range(25, 2775, 25):
            rows.pop(number)
        
        for i in range(num_inicial, num_final):
            jogador = rows[i].find_all('td')
            
            for j in range(0, num):
                player_stats = jogador[j].get_text().strip()
                players_list.append(player_stats)

        return players_list
    
    def createDict(self, num_inicial, num_final):
        columns = self.makeCols()
        rows = self.makeContent(num_inicial, num_final) 
        dicionario = {}
        n = len(columns)

        splited = [rows[i::n] for i in range(n)]

        for i in range(0, n):
            dicionario[columns[i]] = splited[i]

        return dicionario   