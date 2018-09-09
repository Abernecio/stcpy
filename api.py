import urllib
from urllib.request import urlopen
import urllib.error
from bs4 import BeautifulSoup


def getbuses(code):
    try:
        html = urlopen("http://www.stcp.pt/pt/itinerarium/soapclient.php?codigo=" + code)
        soup = BeautifulSoup(html, 'html.parser')

        data = []
        table = soup.find(id='smsBusResults')

        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])

        cars = data[1][0], data[2][0]
        time = data[1][1], data[2][1]
        awaittime = data[1][2], data[2][2]

        print("carros:\n")
        print(cars)

        print("\nhora:\n")
        print(time)

        print("\ntempo de espera:\n")
        print(awaittime)

    except urllib.error as e:
        print("Codigo de Paragem invalido. Mais info:\n")
        print(e)


user_input = input("Codigo da paragem: \n")
getbuses(user_input)