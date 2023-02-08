# to run 
# scrapy crawl tmdb_spider -o movies.csv

import scrapy
from scrapy.http import Request

class TmdbSpider(scrapy.Spider):
    name = 'tmdb_spider'
    
    start_urls = ['https://www.themoviedb.org/tv/63247-westworld/']

    def parse(self, response):
        """
        This method finds the hyperlink to the next webpage and 
        passes it to another parser function.
        """

        # this command finds the url to the next page
        next_page = response.css('#media_v4 .new_button a::attr(href)').get()
        # joins the initial link to the url found above
        yield response.follow(next_page, callback=self.parse_full_credit)

    def parse_full_credit(self, response):
        """
        This function extracts the links to each cast member and 
        calls parse_actor_page function for further parsing.
        """
        # gets the links to the cast members
        cast_links=response.css('.panel.pad > ol > li > a::attr(href)').getall()

        # makes a full url link
        next_pages = ["https://www.themoviedb.org" + link for link in cast_links]

        # loops over actor pages
        for next_page in next_pages:
            yield Request(next_page, callback = self.parse_actor_page)

    def parse_actor_page(self, response):
        pass
        