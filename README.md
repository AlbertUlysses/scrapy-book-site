# scrapy-book-site
This is a web scrapper built in Python with the Scrapy Library. The website scrapped is "books.toscrape.com" a website built to practice web scrapping.
## Installation
First you will want to create your virtual environment, then run `pip install -r requirements.txt` 
To run the spider you will enter `scrapy crawl books` 
## How the Spider Moves:
Spider starts on the main page and moves into the category links that are listed on the side. From there the spider moves into each book webpage.
There is one pipeline that saves all the data gethered into a json line file inside a json folder. Each webpage is saved as an html file on a local folder
to ensure the orginal data is never lost. The html files are divided into the categories and the book folders to make searching them easy.


## Data Dictionary:
Below I have a data dictionary for the project. 

Data Dictionary:
-Main Page
	category_name - category names
	category_link - links for category pages
-Category pages
	book_name - book names 
	book_link - links that take you to the book's page
-book page
	full_bookname - book name
	priceinpounds - price
	rating - rating
	product information:
		upc - UPC
		producttype - Product type
		priceexcludetax -price excl. tax in lbs
		priceincludetax - price incl. tax in lbs
		tax - tax in lbs
		availability - availability
		numberavailable - number of avilable books
		numberofreviews - number of reviews


