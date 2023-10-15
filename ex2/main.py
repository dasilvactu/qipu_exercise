from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
def get_info(value):
    url = 'https://aisweb.decea.mil.br/?i=aerodromos&codigo={codigo}'
    try:
        html = urlopen(url.format(codigo=value))
    except HTTPError as e:
        print('Error code: ', e.code)
        return
    except URLError as e:
        print('Reason: ', e.reason)
        return    
    soup = bs(html, 'html.parser')
    error = soup.findAll('div',{'class':'alert-danger'})
    if len(error)> 0:
        print ("ICAO inválido")
        return
    sunset = soup.find('sunset').text
    sunrise = soup.find('sunrise').text
    taf_h5 = soup.find('h5', string="TAF")
    taf = taf_h5.findNext('p').get_text()
    metar_h5 = soup.find('h5', string="METAR")
    metar = metar_h5.findNext('p').get_text()
    hr_cartas = soup.find('hr', id='cartas')
    print ('Cartas:')
    for carta in hr_cartas.findAllNext('h4', attrs={'class':None}):
        nome = carta.getText()
        lista = carta.findNext('ul')
        links = []
        for itens in lista.findChildren('li', attrs={'class':None}):
            links.append(itens.findNext('a',attrs={'href':True})['href'])
        print (f"{nome} => {', '.join(links)}")
    print(f"Nascer do sol: {sunrise}h")
    print(f"Por do sol: {sunset}h")
    print(f"TAF: {taf}")
    print(f"METAR: {metar}")

if __name__ == "__main__":
    
    value = input("Digite o código ICAO:\n");
    get_info(value)

    