import scrapy

class User_data(scrapy.Item):
    accountId = scrapy.Field()
    level = scrapy.Field()
    platformId = scrapy.Field()
    queueid = scrapy.Field()
    timestamp = scrapy.Field()
    game_duration = scrapy.Field()
    partecipantsList = scrapy.Field()