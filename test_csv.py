import requests
import csv
from bs4 import BeautifulSoup as bs4

url=requests.get("http://quirky-lichterman-ddef4e.netlify.app/")
print(url)

soup=bs4(url.content,"html.parser")
filename='test.csv'
csv_writer=csv.writer(open(filename,'w'))
heading=soup.find('h1')
print(heading.text)

#run a for loop  to extract the table data and store it in a cvs file
for tr in soup.find_all("tr"):
    data=[]

#Extracting the table heading which will only execute once
for th in tr.find_all('th'):
    data.append(th.text)

    if data:
        print("Display headers:{}".format(','.join(data)))
        csv_writer.writerow(data)
        continue

        #for scraping the actual table data valuea

for td in tr.find_all('td'):
    data.append(td.text.strip())

    if data:
        print("Display data:{}".format(','.join(data)))
        csv_writer.writerow(data)        


