import scrapy


class BookSpider(scrapy.Spider):
    name= "books"

    start_urls = ["http://books.toscrape.com/"]

    
    def parse(self, response):
        for index, book in enumerate(response.xpath('//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul/li/a')):
            yield {
                    'text': book.xpath('//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul/li/a/text()')[index].get().strip(),
                    'link': book.xpath('//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul/li/a/@href')[index].get()
                }
        #next_page = response.xpath('//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul/li[1]/a/@href').get()
