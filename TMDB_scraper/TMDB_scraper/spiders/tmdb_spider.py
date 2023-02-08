# to run 
# scrapy crawl tmdb_spider -o movies.csv

import scrapy

class TmdbSpider(scrapy.Spider):
    name = 'tmdb_spider'
    
    start_urls = ['https://www.themoviedb.org/tv/63247-westworld/']

    def parse(self, response):
        """
        This method finds the hyperlink to the next webpage and 
        passes it to another parser function.
        """

        next_page = response.css('#media_v4.new_button a::attr(href)').get()
        yield response.follow(next_page, callback=parse_full_credit)

    def parse_full_credit(self, response):
        pass