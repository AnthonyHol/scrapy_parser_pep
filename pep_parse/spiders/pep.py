import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ["https://peps.python.org/"]

    def parse(self, response):
        """Метод парсинга страницы со всеми PEP."""
        for pep in response.css("section#numerical-index tbody tr"):
            href = pep.css("td a::attr(href)").get()

            if href is not None:
                yield response.follow(href + "/", callback=self.parse_pep)

    def parse_pep(self, response):
        """Метод парсинга номера, названия и статуса со страницы PEP."""
        name = response.xpath('//*[@id="pep-content"]/h1/text()').get()

        data = {
            "number": name.split()[1],
            "name": name,
            "status": response.css("abbr::text").get(),
        }

        yield PepParseItem(data)
