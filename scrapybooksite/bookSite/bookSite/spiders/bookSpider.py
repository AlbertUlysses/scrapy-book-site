import scrapy
import os.path
from booksite.items import BookSiteMainItem 

class BookSpider(scrapy.Spider):
    name = "books"
        
    def start_requests(self):
        yield scrapy.Request(url = 'http://books.toscrape.com/', callback = self.parse)
    
    def parse(self, response):
        # Saves the main webpage to an html file and folder.
        html_path = r"C:\Users\alber\Desktop\myWork\projects\scrapy-book-site\scrapybooksite\booksite\booksite\spiders\htmlfiles"
        main_html_name = "booksToScrapeMain.html"
        filename = os.path.join( html_path, main_html_name ) 
        with open( filename, 'wb') as f:
            f.write(response.body)
        
        item = BookSiteMainItem()
        next_page = []
        
        # Enumerates is necessary to prevent yielding the same value 50 times.        
        for index, book in enumerate(response.xpath('//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul/li/a')):
            item['category_name'] = book.xpath('//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul/li/a/text()')[index].get().strip()
            item['category_link'] = book.xpath('//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul/li/a/@href')[index].get()
            next_page.append(book.xpath('//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul/li/a/@href')[index].get())
            yield item
                
        for type in next_page:
            if type is not None:
                type = response.urljoin(type)
            yield scrapy.Request(type, self.bookpage_parse, dont_filter = True)
            yield scrapy.Request(type, self.category_html)
        
    def category_html(self, response):   
        # Saves webpages for future access.
        page = response.url.split("/")[-2]
        html_name = "%s.html" % page
        html_path = r"C:\Users\alber\Desktop\myWork\projects\scrapy-book-site\scrapybooksite\booksite\booksite\spiders\htmlfiles\categories"
        filename = os.path.join( html_path, html_name)        
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

    def bookpage_parse(self, response):    
        item = BookSiteMainItem()
        book_page = []
        for index, book in enumerate(response.xpath('//*[@id="default"]/div/div/div/div/section/div[2]/ol/li/article/h3/a')):
            item['book_name'] = book.xpath('//*[@id="default"]/div/div/div/div/section/div[2]/ol/li/article/h3/a/text()')[index].get().strip()
            item['book_link'] = book.xpath('//*[@id="default"]/div/div/div/div/section/div[2]/ol/li/article/h3/a/@href')[index].get()
            book_page.append(book.xpath('//*[@id="default"]/div/div/div/div/section/div[2]/ol/li/article/h3/a/@href')[index].get())
            yield item

        for type in book_page:
            if type is not None:
                type = response.urljoin(type)
            yield scrapy.Request(type, self.bookpage_html, dont_filter = True)
            yield scrapy.Request(type, self.book_pare)
    
    def bookpage_html(self, response):
        page = response.url.split("/")[-2]
        html_name = "%s.html" % page
        html_path = r"C:\Users\alber\Desktop\myWork\projects\scrapy-book-site\scrapybooksite\booksite\booksite\spiders\htmlfiles\books"
        filename = os.path.join( html_path, html_name)        
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
    
    def book_pare(self, response):
        item = BookSiteMainItem()        
        for path in response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]'):
            item['full_bookname'] = path.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/h1/text()').get()
            item['priceinpounds'] = path.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/p[1]/text()').get()
            item['rating'] = path.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/p[3]/@class').get()
            item['upc'] = path.xpath('//*[@id="content_inner"]/article/table[@class="table table-striped"]//tr/td')[0].get().split()[0]
            item['producttype'] = path.xpath('//*[@id="content_inner"]/article/table[@class="table table-striped"]//tr/td')[1].get().split()[0]
            item['priceexcludetax'] = path.xpath('//*[@id="content_inner"]/article/table[@class="table table-striped"]//tr/td')[2].get().split()[0]
            item['priceincludetax'] = path.xpath('//*[@id="content_inner"]/article/table[@class="table table-striped"]//tr/td')[3].get().split()[0]
            item['tax'] = path.xpath('//*[@id="content_inner"]/article/table[@class="table table-striped"]//tr/td')[4].get().split()[0]
            item['availability'] = path.xpath('//*[@id="content_inner"]/article/table[@class="table table-striped"]//tr/td')[5].get().split()[0:2]
            item['numberavailable'] = path.xpath('//*[@id="content_inner"]/article/table[@class="table table-striped"]//tr/td')[5].get().split()[2:]
            item['numberofreviews'] = path.xpath('//*[@id="content_inner"]/article/table[@class="table table-striped"]//tr/td')[6].get().split()[0]
            yield item

