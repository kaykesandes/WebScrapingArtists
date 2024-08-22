import requests
import csv
from bs4 import BeautifulSoup


#criando um arquivo para gravar, adicionar linha de cabeçalhos
f = csv.writer(open('z-artist-names.csv', 'w'))
f.writerow(['Name', 'Link'])

pages = []

for x in range(1,5):
    url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ' + str(x) + '.htm'
    pages.append(url)

#Coletar a primeira pagina da lista de artistas
#page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')

#Criar o objeto BeautifulSoup

for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')

    #Remover links inferiores
    lastLink = soup.find(class_ = 'AlphaNav')
    lastLink.decompose()

    #Pegar todo o texto da div BodyText
    artistNameList = soup.find(class_='BodyText')
    artistNameListItems = artistNameList.find_all('a')

    #cria loop para imprimir todos os nomes de artistas
    for artistName in artistNameListItems:
        names = artistName.contents[0]
        links = 'https://web.archive.org' + artistName.get('href')
        f.writerow([names, links])