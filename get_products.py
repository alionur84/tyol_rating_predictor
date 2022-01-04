import requests
from bs4 import BeautifulSoup
import csv

# scraps the url for best selling products on a given date
# saves links and product names to a csv file

links = [["Product_Name", "Link"]]

for i in range(1,6):
	url = "https://www.trendyol.com/sr/?fl=encoksatanurunler&pi="+str(i)
	#headers['pi'] = i
	page = requests.get(url)
	soup = BeautifulSoup(page.content, "html.parser")
	print(url)
	card = soup.findAll('div', class_="p-card-wrppr")
	for i in card:
		link = i.find_next("a", href=True)
		text = link.find("span", class_="prdct-desc-cntnr-name hasRatings")
		links.append([text.text, "https://www.trendyol.com"+link['href']])

with open('best_selling.csv', 'w') as f:
	csv_writer = csv.writer(f, delimiter=",")
	for row in links:
		csv_writer.writerow(row)

print(links)
print(len(links))

