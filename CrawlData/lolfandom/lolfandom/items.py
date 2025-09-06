
import scrapy


class LolfandomItem(scrapy.Item):
    date = scrapy.Field()
    tournament = scrapy.Field()
    tournament_type = scrapy.Field()  # International or Domestic
    patch = scrapy.Field()
    enemy = scrapy.Field()
    side = scrapy.Field()
    result = scrapy.Field()

    # Bans
    ban1_1 = scrapy.Field()
    ban1_2 = scrapy.Field()
    ban1_3 = scrapy.Field()
    ban1_4 = scrapy.Field()
    ban1_5 = scrapy.Field()

    # Bans enemy
    ban2_1 = scrapy.Field()
    ban2_2 = scrapy.Field()
    ban2_3 = scrapy.Field()
    ban2_4 = scrapy.Field()
    ban2_5 = scrapy.Field()

    # Picks
    pick1_top = scrapy.Field()
    pick1_jungle = scrapy.Field()
    pick1_mid = scrapy.Field()
    pick1_ad = scrapy.Field()
    pick1_support = scrapy.Field()

    # Picks enemy

    pick2_top = scrapy.Field()
    pick2_jungle = scrapy.Field()
    pick2_mid = scrapy.Field()
    pick2_ad = scrapy.Field()
    pick2_support = scrapy.Field()

    # Players
    player_top = scrapy.Field()
    player_jungle = scrapy.Field()
    player_mid = scrapy.Field()
    player_ad = scrapy.Field()
    player_support = scrapy.Field()

    pass
