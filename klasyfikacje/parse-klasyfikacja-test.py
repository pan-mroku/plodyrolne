from bs4 import BeautifulSoup


soup = BeautifulSoup(open("klasyfikacja.html"))

spis = soup.findAll("table", { "class" : "spis" })
table_body = spis[0].find('tbody')

rows = table_body.find_all('tr')
data=[]
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele]) # Get rid of empty values

print(data)