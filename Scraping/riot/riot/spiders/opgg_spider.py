
import scrapy


class OPGGSpider(scrapy.Spider):
    name = 'opgg'
    start_urls = ['https://euw.op.gg/summoner/userName=ScarletBloody']

    def parse(self, response):
        level = response.css("span.Level::text").get()
        for match in response.css('div.GameItemWrap'):
            print("x")
            yield{
                "type": match.css("div.GameItemWrap div.GameType::text").get().strip(),
                "timestamp": match.css("div.GameItemWrap span._timeago::attr(data-datetime)").get(),
                "duration": match.css("div.GameItemWrap div.GameLength::text").get(),
                "level": level,
                "list_players": match.css("div.GameItemWrap div.FollowPlayers div.SummonerName a::attr(href)").getall()
           }
