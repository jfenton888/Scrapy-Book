
import scrapy

# most basic spider in scrapy
# whole spiders are organized within a class


# class BrickSetSpider(scrapy.Spider):
#     name = "demo_spider" 
#     start_urls = ['http://brickset.com/sets/year-2016'] #website that will be scraped

#     def parse(self, response): #this function controls what the code does with the website
#         SET_SELECTOR = '.set' #defines the place in the code that information will start being taken from
#         for brickset in response.css(SET_SELECTOR):
#             pass



# class BrickSetSpider(scrapy.Spider):
#     name = "demo_spider"
#     start_urls = ['http://brickset.com/sets/year-2016']

#     def parse(self, response):
#         page = response.url.split("/")[-2]
#         filename = 'quotes-%s.html' % page 
#         with open(filename, 'wb') as f:
#             f.write(response.body)




# class BrickSetSpider(scrapy.Spider):
#     name = "demo_spider"
#     start_urls = ['http://brickset.com/sets/year-2016']

#     def parse(self, response):
#         SET_SELECTOR = '.set' #all the information being taken is under the heading of set, meaning it is information about a specific set
#         for brickset in response.css(SET_SELECTOR): # loop that will grab the information for every '.set' on the page

#             NAME_SELECTOR = 'h1 ::text' #goes to the path using css that contians the name of each set and saves all the information in that path
#             yield {
#                 'name': brickset.css(NAME_SELECTOR).extract_first(), #takes only the first picece of information 
#             }






class BrickSetSpider(scrapy.Spider):
    name = 'demo_spider'
    start_urls = ['http://brickset.com/sets/year-2016']

    def parse(self, response):
        SET_SELECTOR = '.set'
        for brickset in response.css(SET_SELECTOR):

            NAME_SELECTOR = 'h1 a ::text'
            PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()' #relative path using xpath to where number of the pieces is stored
            MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()' #relative path using xpath
            IMAGE_SELECTOR = 'img ::attr(src)' #using css again for path to image of set
            yield {
                'name': (brickset.css(NAME_SELECTOR).extract())[1],
                'number': (brickset.css(NAME_SELECTOR).extract())[0],
                'pieces': brickset.xpath(PIECES_SELECTOR).extract_first(), # takes only the first element of the extracted data with xpath
                'minifigs': brickset.xpath(MINIFIGS_SELECTOR).extract_first(), 
                'image': brickset.css(IMAGE_SELECTOR).extract_first(), # takes only the first element of the extracted data with css
            }




# class BrickSetSpider(scrapy.Spider):
#     name = "demo_spider"
#     start_urls = ['https://brickset.com/sets/year-2016']

#     def parse(self, response):
#         SET_SELECTOR = '.set'
#         for brickset in response.css(SET_SELECTOR):

#             NAME_SELECTOR = 'h1 a ::text'
#             NUMBER_SELECTOR = 'h1 a ::text'
#             PIECES_SELECTOR = 'a.//dl[dt/text() = "Pieces"]/dd/a/text()'
#             MINIFIGS_SELECTOR = 'a.//dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
#             SET_PRICE = 'a.//dl[dt/text() = "RRP"]/text()' # takes only the first element of the extracted data with xpath
#             IMAGE_SELECTOR = 'img ::attr(src)'
#             yield {
#                 'number': (brickset.css(NAME_SELECTOR).extract_first())[0],
#                 'name': (brickset.css(NAME_SELECTOR).extract())[1],
#                 'pieces': brickset.xpath(PIECES_SELECTOR).extract_first(),
#                 'minifigs': brickset.xpath(MINIFIGS_SELECTOR).extract_first(),
#                 'price' : brickset.xpath(SET_PRICE).extract_first(),
#                 'image': brickset.css(IMAGE_SELECTOR).extract_first(),
#             }
            # loops through each page included in the catagory 
#         NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
#         next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
#         if next_page:
#             yield scrapy.Request(
#                 response.urljoin(next_page),
#                 callback=self.parse
#             )















