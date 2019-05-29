import scrapy
import os.path
from booksite.items import BookSiteMainItem # BookSiteCategoryItem

class BookSpider(scrapy.Spider):
    name = "books"
        
    def start_requests(self):
        yield scrapy.Request(url = 'http://books.toscrape.com/', callback = self.parse)
    
    def parse(self, response):

        # Saves the main webpage to an html file and folder so the data is never lost.

        html_path = r"C:\Users\alber\Desktop\myWork\projects\scrapy-book-site\scrapybooksite\booksite\booksite\spiders\htmlfiles"
        main_html_name = "booksToScrapeMain.html"
        filename = os.path.join( html_path, main_html_name ) 
        with open( filename, 'wb') as f:
            f.write(response.body)
        
        item = BookSiteMainItem()
        
        next_page = []
        
        # Enumerates to prevent yielding the same value 50 times.item = BookSiteMainItem()        
        for index, book in enumerate(response.xpath('//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul/li/a')):
            item['category_name'] = book.xpath('//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul/li/a/text()')[index].get().strip()
            item['category_link'] = book.xpath('//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul/li/a/@href')[index].get()
            next_page.append(book.xpath('//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul/li/a/@href')[index].get())
            yield item
                
        for type in next_page:
            if type is not None:
                type = response.urljoin(type)
            yield scrapy.Request(type, self.bookpage_parse, dont_filter = True)
            yield scrapy.Request(type, self.html_parse)
        
    def html_parse(self, response):   
        # Saves all the webpages for future access.
        page = response.url.split("/")[-2]
        html_name = "books-%s.html" % page
        html_path = r"C:\Users\alber\Desktop\myWork\projects\scrapy-book-site\scrapybooksite\booksite\booksite\spiders\htmlfiles"
        filename = os.path.join( html_path, html_name)        
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

    def bookpage_parse(self, response):    
        item = BookSiteMainItem()
        for index, book in enumerate(response.xpath('//*[@id="default"]/div/div/div/div/section/div[2]/ol/li/article/h3/a')):
            item['book_name'] = book.xpath('//*[@id="default"]/div/div/div/div/section/div[2]/ol/li/article/h3/a/text()')[index].get().strip(),
            item['book_link'] = book.xpath('//*[@id="default"]/div/div/div/div/section/div[2]/ol/li/article/h3/a/@href')[index].get()
            yield item


"""
    def html_request(self):
        yield scrapy.Request(url = "http://books.toscrape.com/", callback = self.html)
        
    def html(self, response):
        # This empty list will be used to gather the links.
        next_page = []
        # Enumerates to prevent yielding the same value 50 times.
        for index, book in enumerate(response.xpath('//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul/li/a')):
            next_page.append(book.xpath('//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul/li/a/@href')[index].get())
        print(next_page)       
        for type in next_page:
            if type is not None:
                type = response.urljoin(type)
            yield scrapy.Request(type, callback = self.htmlparse)

    def htmlparse(self, response):    
        page = response.url.split("/")[-2]
        book_html = 'books-%s.html' % page
        html_path = r
        filename = os.path.join(html_path, book_html)
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

"""
"""
    def parse(self, response):
        # Saves the main webpage to an html file and folder so the data is never lost.
        html_path = 
        main_html_name = "booksToScrapeMain.html"
        filename = os.path.join( html_path, main_html_name ) 
        with open( filename, 'wb') as f:
            f.write(response.body)
        
        item = BookSiteMainItem()        
        for index, book in enumerate(response.xpath('//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul/li/a')):
                    item['category'] = book.xpath('//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul/li/a/text()')[index].get().strip()
                    item['link'] = book.xpath('//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul/li/a/@href')[index].get()
                    yield item
"""
"""
    def booktypes(self, response):
        item = BookCategoryItem
        for index, book in enumerate(response.xpath('//*[@id="default"]/div/div/div/div/section/div[2]/ol/li/article/h3/a')):
            item['name'] = book.xpath('//*[@id="default"]/div/div/div/div/section/div[2]/ol/li/article/h3/a/text()')[index].get().strip(),
            item['link'] = book.xpath('//*[@id="default"]/div/div/div/div/section/div[2]/ol/li/article/h3/a/@href')[index].get()
            yield item
"""

"""

        # This empty list will be used to gather the links.
        next_page = []
        # Enumerates to prevent yielding the same value 50 times. 
        for index, book in enumerate(response.xpath('//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul/li/a')):
            yield {
                    'category': book.xpath('//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul/li/a/text()')[index].get().strip(),
                    'link': book.xpath('//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul/li/a/@href')[index].get()
                }
        
            next_page.append(book.xpath('//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul/li/a/@href')[index].get())
        # The program loops over the list to create functional urls that we can save to HTML files.
        for type in next_page:
                    if type is not None:
                        type = response.urljoin(type)
                        yield scrapy.Request(type, callback = self.parse)
        
        # The next few lines of code save the web pages as an HTML file in the current folder.
        # We are saving the web pages to avoid losing the original source.
        page = response.url.split("/")[-2]
        filename = 'books-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        

        
        # This code is to have the spider crawl from page to page.
        # This code is blocked out to help troubleshoot the above code. 
        next_page = response.xpath('//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul/li/a//@href').get()
        
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
        




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