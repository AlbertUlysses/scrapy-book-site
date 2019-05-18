Spider plan:
-create a new spider that will crawl one of the links
-try to merge the spiders so it will move to the next page and yield different data
-create a spider that calls the urls and names
-then extract the real data

The data gethered:
** All webpages should be saved**
-Main Page
** This data is only gathered from side panel**
	-Category name
	-links for category page
-Category pages
	-book name 
	-links that take you to the book's page
-book page
	-book name: response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/h1/text()').get()
	-price: response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/p[1]/text()').get()
	-rating: response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/p[3]/@class').get()
	-prodcut information:
		-UPC: response.xpath('//*[@id="content_inner"]/article/table[@class="table table-striped"]//tr/td')[0].get().split()[0]
		-Product type: response.xpath('//*[@id="content_inner"]/article/table[@class="table table-striped"]//tr/td')[1].get().split()[0]
		-price excl. tax in lbs: response.xpath('//*[@id="content_inner"]/article/table[@class="table table-striped"]//tr/td')[2].get().split()[0]
		-price incl. tax in lbs: response.xpath('//*[@id="content_inner"]/article/table[@class="table table-striped"]//tr/td')[3].get().split()[0]
		-tax in lbs: response.xpath('//*[@id="content_inner"]/article/table[@class="table table-striped"]//tr/td')[4].get().split()[0]
		-availability and number available: response.xpath('//*[@id="content_inner"]/article/table[@class="table table-striped"]//tr/td')[5].get().split()
		-number of reviews: response.xpath('//*[@id="content_inner"]/article/table[@class="table table-striped"]//tr/td')[6].get().split()[0]

Goal:
-The spider will move to multiple pages and gather different data
-I will create a pipline to move the data to json files
-ontop of the json and html data I will need to save each html page incase the data was\
not processed correctly, the data will not be lost


---------------------------
BRAINSTORMING AREA:
Currently I can scrap the first page for both the html and the data I am looking for.
I want to be able to save the yielded data seperately, the -o books.json technique doesn't allow for me to seperate the \
data I want. I will start looking into a pipeline to save the data at each step.


To me a cleaner looking code will be seperate functions that will handle different things

Having multiple spiders may not be necessary
I will create mutliple spiders later if the code looks cleaner


python recursion by also help!


