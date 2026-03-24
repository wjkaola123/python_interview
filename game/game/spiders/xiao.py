import scrapy


class XiaoSpider(scrapy.Spider):
    name = "xiao"
    allowed_domains = ["4399.com"]
    start_urls = ["https://www.4399.com/flash"]

    def parse(self, response, *args, **kwargs):
        game_items = response.css('ul.n-game.cf li')

        for item in game_items:
            game_name = item.css('b::text').get()
            game_link = item.css('a::attr(href)').get()
            game_category = item.css('em a::text').get()
            game_date = item.css('em::text').get()

            if game_name:
                yield {
                    'game_name': game_name.strip(),
                    'game_link': game_link,
                    'game_category': game_category.strip() if game_category else None,
                    'game_date': game_date.strip() if game_date else None
                }
