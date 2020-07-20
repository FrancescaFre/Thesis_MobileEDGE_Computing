#https://docs.scrapy.org/en/latest/topics/request-response.html#scrapy.http.Response


import scrapy


class RiotSpider(scrapy.Spider):
    name = 'riot'

    start_urls = ["https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/scarletbloody?api_key=RGAPI-cc34b06e-be77-4b02-acc5-a4d455c5123e"]

    '''
    def __init__ (self, *a, **kw): 
        super(RiotSpider, self).__init__(*a, **kw)
        self.key = "RGAPI-cc34b06e-be77-4b02-acc5-a4d455c5123e"
    
        self.api_url = {
                "data by_account" : lambda account_name : f"https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{account_name}?api_key={key}",
                "matches by accountID" : lambda accountID : f"https://euw1.api.riotgames.com/lol/match/v4/matchlists/by-account/{accountID}?api_key={key}",
                "match info by matchID" : lambda matchID : f"https://euw1.api.riotgames.com/lol/match/v4/matches/{matchID}?api_key={key}"
            }

        '''

#---------------------------------------- PARSE SUMMONER
    def parse(self, response):
        print("-----------------------------------------------------------------------------"+response.url)
       
        #trasformo in dict una stringa che contiene un dizionario/json
        summoner_data = eval(response.text)
        level = summoner_data['summonerLevel']
        accountId = summoner_data['accountId']

        print("-geturl- : "+self._getUrl(0,"ScarletBloody"))
        
        request_matches = scrapy.Request(
                #url = "https://euw1.api.riotgames.com/lol/match/v4/matchlists/by-account/HgoCSSbBOVNN8JP0StXL_72jqlfXU-cgSlx8uWY9EDWn-f4?api_key=RGAPI-cc34b06e-be77-4b02-acc5-a4d455c5123e",
                #url = self.api_url["matches by accountID"](accountId),
                url = self._getUrl(1, accountId),
                callback= self.parse_matches
            )
        yield request_matches

        yield{
            summoner_data, 
            level
        }

#---------------------------------------- PARSE LISTA MATCH
    def parse_matches(self, response): 
        print("-----------------------------------------------------------------------------"+response.url)
        summoner_matches = eval(response.text)['matches']

        
        for match in summoner_matches[:2]:
            platform = match['platformId']
            queueid = match['queue']
            timestamp = match['timestamp']

            request_match = scrapy.Request(
                #url = self.api_url["match info by matchID"](matchID))
                #url = "https://euw1.api.riotgames.com/lol/match/v4/matches/4713294703?api_key=RGAPI-cc34b06e-be77-4b02-acc5-a4d455c5123e",
                url = self._getUrl(2, match['gameId']),
                callback=self.parse_match)
            yield request_match
        
        yield{
            platform,
            queueid,
            timestamp
        }
        


#---------------------------------------- PARSE Singolo MATCH
    def parse_match(self, response): 
        print("\n-----------------------------------------------------------------------------\n"+response.url)
    
        single_match = eval(response.text.replace('true', 'True').replace('false', 'False'))
        game_duration = single_match['gameDuration']
        gamecreationTimeStamp = single_match['gameCreation']
        partecipantsList = single_match['participantIdentities']

        for accountId in [x['player']['accountId'] for x in partecipantsList]:
            request_matches = scrapy.Request(
                url = self._getUrl(1, accountId),
                callback= self.parse_matches
            )
            yield request_matches

        yield{
            game_duration,
            gamecreationTimeStamp,
            partecipantsList
        }



       

    def _getUrl(self, type, id):
        key = "RGAPI-cc34b06e-be77-4b02-acc5-a4d455c5123e"
        if type == 0: return f"https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{id}?api_key={key}"
        if type == 1: return f"https://euw1.api.riotgames.com/lol/match/v4/matchlists/by-account/{id}?api_key={key}"
        if type == 2: return f"https://euw1.api.riotgames.com/lol/match/v4/matches/{id}?api_key={key}"