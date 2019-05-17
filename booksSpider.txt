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

How I think I'll be able to move to the next website and gather the first \
yield
-see this webpage:https://docs.scrapy.org/en/latest/topics/spiders.html
-under the first spider type you'll see "let's see an example"
-The following code is from the second example, I believe we can call a second\
for loop that will yield different data, which means I can probably yield \
more than one for loop. 
-the only issue i can potentially see in getting the data onto a json file.


import scrapy

class MySpider(scrapy.Spider):
    name = 'example.com'
    allowed_domains = ['example.com']
    start_urls = [
        'http://www.example.com/1.html',
        'http://www.example.com/2.html',
        'http://www.example.com/3.html',
    ]

    def parse(self, response):
        for h3 in response.xpath('//h3').getall():
            yield {"title": h3}

        for href in response.xpath('//a/@href').getall():
            yield scrapy.Request(response.urljoin(href), self.parse)





---------------------------
BRAINSTORMING AREA:
so I think i have figured out how to go to the next page and save the html, 
I'll have to create a new function and it'll process after the first one has been processed
or i can yield the link in a different yield output and save it into a list, then use the orginal code to loop through those links like this:
**the only issue I can see right now is that the list is inside of the start_requests function, i'll have to look at the short cut and overwrite the\
start_urls variable**


import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)