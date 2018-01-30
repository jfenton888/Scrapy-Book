import scrapy


# class BrickSetSpider(scrapy.Spider):
#     name = 'brick_spider'
#     start_urls = ['http://brickset.com/sets/year-2016']

#     def parse(self, response):
#         SET_SELECTOR = '.set'
#         for brickset in response.css(SET_SELECTOR):
#         	NAME_SELECTOR = 'h1 ::text'
#         	SET_NUMBER = 'h1 a ::text' 
#             PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
#             MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
#             IMAGE_SELECTOR = 'img ::attr(src)'
#             SET_PRICE = './/dl[dt/text() = "RRP"]/dd[3]/a/text()'
#             yield {
#             	'set #' : brickset.css(SET_NUMBER).extract_first(),
#                 'name': brickset.css(NAME_SELECTOR).extract_first(),
#                 'pieces': brickset.xpath(PIECES_SELECTOR).extract_first(),
#                 'minifigs': brickset.xpath(MINIFIGS_SELECTOR).extract_first(),
#                 'image': brickset.css(IMAGE_SELECTOR).extract_first(),
#             }

#         NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
#         next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
#         if next_page:
#             yield scrapy.Request(
#                 response.urljoin(next_page),
#                 callback=self.parse
#             )


class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ['https://brickset.com/sets/theme-Star-Wars']

    def parse(self, response):
        SET_SELECTOR = '.set'
        for brickset in response.css(SET_SELECTOR):

            NAME_SELECTOR = 'h1 a ::text'
            PIECES_SELECTOR = 'a.//dl[dt/text() = "Pieces"]/dd/a/text()'
            MINIFIGS_SELECTOR = 'a.//dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
            IMAGE_SELECTOR = 'img ::attr(src)'
            SET_PRICE = 'a.//dl[dt/text() = "RRP"]/text()'
            yield {
                'number': (brickset.css(NAME_SELECTOR).extract())[0],
                'name': (brickset.css(NAME_SELECTOR).extract())[0],
                'pieces': brickset.xpath(PIECES_SELECTOR).extract_first(),
                'minifigs': brickset.xpath(MINIFIGS_SELECTOR).extract_first(),
                'price' : brickset.xpath(SET_PRICE).extract_first(),
                'image': brickset.css(IMAGE_SELECTOR).extract_first(),
            }
        NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )




