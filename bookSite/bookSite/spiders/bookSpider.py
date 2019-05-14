import scrapy


class BookSpider(scrapy.Spider):
    name= "books"


"""
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
"""