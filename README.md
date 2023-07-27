# Web Scraping de Página de Futebol

Este é um projeto de web scraping em Python para extrair dados de uma página de futebol. Ele utiliza as bibliotecas `requests` e `BeautifulSoup` para obter e analisar o conteúdo HTML da página.

## Como usar

1. Instalação das bibliotecas necessárias:

   Para executar este projeto, certifique-se de ter as bibliotecas `requests` e `BeautifulSoup` instaladas. Caso ainda não tenha instalado, você pode instalar as bibliotecas utilizando o seguinte comando:
    pip install requests
    pip install beautifulsoup4

2. Utilizando a classe `Scrapper`:

    Para começar, importe a classe `Scrapper` para o seu código Python e instancie-a com o link da página de futebol que você deseja fazer o web scraping. Certifique-se de fornecer também os headers necessários, caso a página os exija para a requisição. Por exemplo:

```python
import requests
from bs4 import BeautifulSoup
from scrapper import Scrapper

link = 'https://fbref.com/en/comps/Big5/stats/players/Big-5-European-Leagues-Stats'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

scrapper = Scrapper(link, headers) 
```


## Obtendo os dados:

Utilize os métodos makeCols(), makeContent() e createDict() para obter os dados desejados da página. Por exemplo:  
  
### Obter as colunas
    colunas = scrapper.makeCols()

### Obter os dados de uma faixa de linhas
    dados_dict = scrapper.createDict(first_row=0, last_row=100)

### Imprimir o dicionário com os dados
    print(dados_dict)

#### Funcionalidades

    makeCols(): Extrai os nomes das colunas da tabela da página de futebol.

    makeContent(num_inicial, num_final): Extrai os dados das células da tabela, entre as linhas num_inicial e num_final.

    createDict(first_row, last_row): Cria um dicionário a partir dos dados extraídos da tabela, com as colunas como chaves e os valores como listas contendo os dados de cada coluna.

# Contribuição

Contribuições para aprimorar este projeto são bem-vindas! Sinta-se à vontade para abrir problemas (issues) ou enviar pull requests.  