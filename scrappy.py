import requests
from bs4 import BeautifulSoup


class Scrapper():

    def __init__(self, link, headers):
        self.link = link
        self.headers = headers 
        self.site = requests.get(self.link, headers = self.headers)
        self.soup = BeautifulSoup(self.site.content, 'html.parser')
    

    def makeCols(self) :

        header = self.soup.find('thead')
        titles = header.find_all('tr')
        cols = titles[1].find_all('th')
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
        content_rows = [tr_tag for tr_tag in rows if 'class="thead"' not in tr_tag]

        
        for i in range(num_inicial, num_final):
            player = content_rows[i].find_all('td')
            if len(player) > 0:
                player.pop()
            num = len(player)
            
            for j in range(0, num):
                player_stats = player[j].get_text().strip()
                players_list.append(player_stats)

        return players_list
    
    def createDict(self, first_row, last_row):
        columns = self.makeCols()
        rows = self.makeContent(first_row, last_row)
        data = {}
        n = len(columns)

        splited = [rows[i::n] for i in range(n)]

        for i in range(0, n):
            data[columns[i]] = splited[i]

        return data   