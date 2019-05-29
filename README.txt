Spider plan:
Spider starts on the main page and moves into the category links that are listed on the side. From there the spider moves into each book webpage.
There is one pipeline that saves all the data gethered into a json line file inside a json folder. Each webpage is saved as an html file on a local folder
to ensure the orginal data is never lost. The html files are divided into the categories and the book folders to make searching them easy.



Simple Data Dictionary:
-Main Page
	category_name - category names
	category_link - links for category pages
-Category pages
	book_name - book names 
	book_link - links that take you to the book's page
-book page
	full_bookname - book name: response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/h1/text()').get()
	priceinpounds - price: response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/p[1]/text()').get()
	rating - rating: response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/p[3]/@class').get()
	prodcut information:
		upc - UPC: response.xpath('//*[@id="content_inner"]/article/table[@class="table table-striped"]//tr/td')[0].get().split()[0]
		producttype - Product type: response.xpath('//*[@id="content_inner"]/article/table[@class="table table-striped"]//tr/td')[1].get().split()[0]
		priceexcludetax -price excl. tax in lbs: response.xpath('//*[@id="content_inner"]/article/table[@class="table table-striped"]//tr/td')[2].get().split()[0]
		priceincludetax - price incl. tax in lbs: response.xpath('//*[@id="content_inner"]/article/table[@class="table table-striped"]//tr/td')[3].get().split()[0]
		tax - tax in lbs: response.xpath('//*[@id="content_inner"]/article/table[@class="table table-striped"]//tr/td')[4].get().split()[0]
		availability - availability: path.xpath('//*[@id="content_inner"]/article/table[@class="table table-striped"]//tr/td')[5].get().split()[0:2]
		numberavailable - number of avilable books: path.xpath('//*[@id="content_inner"]/article/table[@class="table table-striped"]//tr/td')[5].get().split()[2:]
		numberofreviews - number of reviews: response.xpath('//*[@id="content_inner"]/article/table[@class="table table-striped"]//tr/td')[6].get().split()[0]


