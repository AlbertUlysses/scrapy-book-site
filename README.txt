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



Creating functions for each step is the best way to move around in the code

the pipeline is a little difficult, I want to work on the html code first then move on to the other data pipelines