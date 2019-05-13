import scrapy


class BookSpider(scrapy.Spider):
    name= "books"

    start_urls = ["http://books.toscrape.com/"]

#spider that yields the book categories and links from the mainpage    
    def parse(self, response):
        #enumerates using index to prevent yielding the same value 50 times 
        for index, book in enumerate(response.xpath('//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul/li/a')):
            yield {
                    'category': book.xpath('//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul/li/a/text()')[index].get().strip(),
                    'link': book.xpath('//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul/li/a/@href')[index].get()
                }
        
