from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve


#page=urlopen("http://www.klasyfikacje.gofin.pl/pkwiu/1,2,2,produkty-rolnictwa-i-lowiectwa-oraz-uslugi-wspomagajace.html#D01").read().decode('ISO-8859-2')
page = open("klasyfikacja.html")
#print(_(page))
soup=BeautifulSoup(page)
spis = soup.findAll("table", { "class" : "spis" })
table_body = spis[0].find('tbody')
if table_body is None:
    print("table_body is none!")
else:
    rows = table_body.find_all('tr')
    data=[]
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele]) # Get rid of empty values

    print(data)