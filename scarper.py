from bs4 import BeautifulSoup
import requests
import csv

url="https://quotes.toscrape.com/"

website= requests.get(url)
soup= BeautifulSoup(website.text, 'html.parser')
quotes= soup.find_all(class_="text")
authors= soup.find_all(class_="author")

file = open("quotes.csv", "w", newline='', encoding='utf-8')
writer = csv.writer(file)

writer.writerow(["Quote", "Author"])

for quote, author in zip(quotes, authors):
    print(f"{quote.get_text()} - {author.get_text()}")
    writer.writerow([quote.get_text(), author.get_text()])
file.close()   

    
