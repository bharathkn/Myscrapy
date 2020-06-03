import scrapy

class WikiSpider(scrapy.Spider):
    name ="wiki_univ"
    start_urls =["https://en.wikipedia.org/wiki/List_of_universities_in_England"]

    def parse(self,response):
        content = response.xpath('//*[@id="mw-content-text"]/div/table/tbody/tr')
        for data in content:

            yield{
                'University':data.xpath('./td[1]/a/text()').extract(),
            'Location':data.xpath('./td[2]/a/text()').extract(),
            'Established':data.xpath('./td[3]/text()').extract(),
            'Number_of_Students':data.xpath('./td[4]/text()').extract(),
            'Tuition_fee':data.xpath('./td[5]/text()').extract(),
            'Degree_powers':data.xpath('./td[6]/text()').extract(),
            'Url_links': data.css('tr td:nth-child(1) a::attr(href)').extract()
        }

        univ_url = response.css('tr td:nth-child(1) a::attr(href)').extract()
        self.logger.info('Get individual college information from this block')
        yield response.follow(univ_url,callback=self.parse_univ_details)

    def parse_univ_details(self,response):
        yield{

      #  }