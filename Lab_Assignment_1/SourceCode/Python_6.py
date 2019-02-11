'''6. Program a code which download a webpage contains a table using Request library, then parse the page using Beautiful soup library.
You should save the information about the states and their capitals in a file.
Sample input:https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_StatesSample
output:Save the table in this link into a file'''
#import csv library package to store data into csv file
import csv
#import requests library to get data from url
import requests
#import beautifulSoup pakagae to etract html content
from bs4 import BeautifulSoup
url='https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States'
page=requests.get(url)
words=BeautifulSoup(page.text,"html.parser")
#get the required table by using find()
rows=words.find(class_='wikitable sortable plainrowheaders')
#after finding out exact details then store each required row in csv file
with open('scrape_results.csv', 'w', newline='') as scrape_results:
    csvwriter = csv.writer(scrape_results)
    for td in rows.find_all("td"):
        for t in td.find_all("a"):
            x=t.get('title')
            csvwriter.writerow([x])
