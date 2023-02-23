import scrapy


class ImdbSpider(scrapy.Spider):
    name = "imdb"
    start_urls = ["https://www.imdb.com/chart/top?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=470df400-70d9-4f35-bb05-8646a1195842&pf_rd_r=9KG6HNKADZ9RE62M18RZ&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=moviemeter&ref_=chtmvm_ql_3"]

    def parse(self, response):
        for filmes in response.css('.titleColumn'):
            yield{
                'titulo': filmes.css('.titleColumn a::text').get(),
                'ano': filmes.css('.secondaryInfo ::text').get()[1:-1],
                'nota': response.css('strong ::text').get()
            }