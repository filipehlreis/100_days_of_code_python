from dataentryjobautomation import DataEntryJobAutomation


if __name__ == "__main__":
    URL_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSdlKRUNFP8H4AkrUDVXc"\
        "jrgfQCXe9HkrlV0_mSg1Ec1SpRE8Q/viewform?usp=sf_link"

    # URL_ZILLOW = 'https://www.zillow.com/los-angeles-ca/rentals/2-_beds/'\
    #     '1.0-_baths/?searchQueryState=%7B"pagination"%3A%7B%7D%2C"usersSearc'\
    #     'hTerm"%3A"Los%20Angeles%2C%20CA"%2C"mapBounds"%3A%7B"west"%3A-119.'\
    #     '49827532003042%2C"east"%3A-117.06755022237417%2C"south"%3A33.550031'\
    #     '085151616%2C"north"%3A34.46529184425745%7D%2C"regionSelection"%3A%5'\
    #     'B%7B"regionId"%3A12447%2C"regionType"%3A6%7D%5D%2C"isMapVisible"%3A'\
    #     'true%2C"filterState"%3A%7B"price"%3A%7B"min"%3A0%2C"max"%3A537712%'\
    #     '7D%2C"mp"%3A%7B"min"%3A0%2C"max"%3A2000%7D%2C"beds"%3A%7B"min"%3A2'\
    #     '%7D%2C"ah"%3A%7B"value"%3Atrue%7D%2C"fr"%3A%7B"value"%3Atrue%7D%2C"'\
    #     'fsba"%3A%7B"value"%3Afalse%7D%2C"nc"%3A%7B"value"%3Afalse%7D%2C"cms'\
    #     'n"%3A%7B"value"%3Afalse%7D%2C"fore"%3A%7B"value"%3Afalse%7D%2C"bath'\
    #     's"%3A%7B"min"%3A1%7D%7D%2C"isListVisible"%3Atrue%7D'

    URL_ZILLOW = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'

    dtja = DataEntryJobAutomation()

    dtja.get_research_houses(URL_ZILLOW)
    dtja.send_forms(URL_FORM)
