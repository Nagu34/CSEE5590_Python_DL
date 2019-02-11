import csv
import requests
from bs4 import BeautifulSoup
url='https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States'
page=requests.get(url)
words=BeautifulSoup(page.text,"html.parser")
rows=words.find(class_='wikitable sortable plainrowheaders')
with open('scrape_results.csv', 'w', newline='') as scrape_results:
    csvwriter = csv.writer(scrape_results)
    for td in rows.find_all("td"):
        for t in td.find_all("a"):
            x=t.get('title')
            csvwriter.writerow([x])
