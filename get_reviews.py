import requests
from bs4 import BeautifulSoup
import json
import csv

data = {"storefrontId":"1",
		"culture":"tr-TR",
		"order":"5",
		"searchValue":"",
		"onlySellerReviews":"false",
		"tagValue":"tümü",
		"ratingValue": "", # this is rating param
		"page":"0"}

# read the csv for product ids

ids = []
with open('raw_data_tyol.csv', 'r') as f:
	csv_reader = csv.reader(f)
	for line in csv_reader:
		ids.append(line[2])
del ids[0]

reviews = [['product_id', 'review', 'rating']]

# for each product id send a get request for each one of five ratings
# get the comments on the first page
for count, product_id in enumerate(ids):
	url = "https://public-mdc.trendyol.com/discovery-web-socialgw-service/api/review/"+product_id
	for i in range(1, 6):
		data['ratingValue'] = str(i)
		page = requests.get(url, params=data)
		content = page.json()
		#total_pages = content['result']['productReviews']['totalPages']
		length = len(content['result']['productReviews']['content'])
		for item in range(length):
			reviews.append([ids[count], content['result']['productReviews']['content'][item]['comment'], content['result']['productReviews']['content'][item]['rate']])
		

# Create a new csv file to save the raw reviews	

with open('rev2.csv', 'w') as f:
	csv_writer = csv.writer(f, delimiter=",")
	for row in reviews:
		csv_writer.writerow(row)





