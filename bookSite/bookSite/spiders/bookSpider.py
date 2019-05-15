import scrapy


class BookSpider(scrapy.Spider):
    name= "books"

    #firts page code, json file produces the categories and links provided on the side bar
    start_urls = ["http://books.toscrape.com/"]


    #spider that yields the book categories and links from the mainpage    
    def parse(self, response):
        #saves html
        filename = 'booksToScrapeMain.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

        #enumerates using index to prevent yielding the same value 50 times 
        for index, book in enumerate(response.xpath('//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul/li/a')):
            yield {
                    'category': book.xpath('//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul/li/a/text()')[index].get().strip(),
                    'link': book.xpath('//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul/li/a/@href')[index].get()
                }
"""        
        next_page = response.xpath('//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul/li/a//@href').get()
        
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
        
        page = response.url.split("/")[-2]
        filename = 'books-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)




"""



"""
    #the first link provided by the side column of main page provides the name and link
    start_urls = ["http://books.toscrape.com/catalogue/category/books/travel_2/index.html"]

    def parse(self, response):
        #saves html file
        page = response.url.split("/")[-2]
        filename = 'category-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

        #enumerates using index to prevent yielding the same value 11 times

        for index, book in enumerate(response.xpath('//*[@id="default"]/div/div/div/div/section/div[2]/ol/li/article/h3/a')):
            yield {
                    'Name': book.xpath('//*[@id="default"]/div/div/div/div/section/div[2]/ol/li/article/h3/a/text()')[index].get().strip(),
                    'link': book.xpath('//*[@id="default"]/div/div/div/div/section/div[2]/ol/li/article/h3/a/@href')[index].get()
                }

    #first link provided by travel. it's a webpage that has the standard layout of the webpages \
    # for books

    start_urls = ["http://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html"]

    def parse(self, response):
        #saves html
        filename = 'its-only-the-himalayas.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

        for path in response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]'):
            yield {
                    "book name": path.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/h1/text()').get(),
                    "listed price in pounds": path.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/p[1]/text()').get(),
                    "rating": path.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/p[3]/@class').get(),
                    "UPC": path.xpath('//*[@id="content_inner"]/article/table[@class="table table-striped"]//tr/td')[0].get().split()[0],
                    "Product type": path.xpath('//*[@id="content_inner"]/article/table[@class="table table-striped"]//tr/td')[1].get().split()[0],
                    "price excl. tax in lbs": path.xpath('//*[@id="content_inner"]/article/table[@class="table table-striped"]//tr/td')[2].get().split()[0],
                    "price incl. tax in lbs": path.xpath('//*[@id="content_inner"]/article/table[@class="table table-striped"]//tr/td')[3].get().split()[0],
                    "tax in lbs": path.xpath('//*[@id="content_inner"]/article/table[@class="table table-striped"]//tr/td')[4].get().split()[0],
                    "availability": path.xpath('//*[@id="content_inner"]/article/table[@class="table table-striped"]//tr/td')[5].get().split()[0:2],
                    "number available": path.xpath('//*[@id="content_inner"]/article/table[@class="table table-striped"]//tr/td')[5].get().split()[2:],
                    "number of reviews": path.xpath('//*[@id="content_inner"]/article/table[@class="table table-striped"]//tr/td')[6].get().split()[0],
                }

"""