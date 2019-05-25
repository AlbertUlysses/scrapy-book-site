Spider plan:
- create a new spider that will crawl one of the links
- Use the item module as a simple container to save scraped data
- Create an feeder export to export the data onto my local machine


- try to merge the spiders so it will move to the next page and yield different data
- create a spider that calls the urls and names
- then extract the real data

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


---------------------------
BRAINSTORMING AREA:

First pipeline is complete, I have created a pipeline for the first page
next I want to create a pipeline for html
but also create a list of those html pages so I can then create a parse function similar to the one in the begining of the tutorial
then I would repeat these steps for the last tree


I have the html files saved however a recursion has occured and now it is spitting out the same information for all the html files

what I can do is create an item for it and attempt to redo the process with a pipeline