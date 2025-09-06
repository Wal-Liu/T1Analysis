import scrapy
from lolfandom.items import LolfandomItem
import json
import os
from datetime import datetime

STATE_FILE = 'max_date.json' # Lưu trữ ngày lớn nhất đã crawl

def parse_datetime(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d')

class LolfandomSpider(scrapy.Spider):
    name = 'lolfandom'
    allowed_domains = ['lolfandom.com']
    start_urls = [
        "https://lol.fandom.com/wiki/Special:RunQuery/MatchHistoryGame?MHG%5Bpreload%5D=Team&MHG%5Btournament%5D=&MHG%5Bteam%5D=T1&MHG%5Bteam1%5D=&MHG%5Bteam2%5D=&MHG%5Bban%5D=&MHG%5Brecord%5D=&MHG%5Bascending%5D%5Bis_checkbox%5D=true&MHG%5Blimit%5D=250&MHG%5Boffset%5D=&MHG%5Bregion%5D=&MHG%5Byear%5D=&MHG%5Bstartdate%5D=&MHG%5Benddate%5D=&MHG%5Bwhere%5D=&MHG%5Btextonly%5D%5Bis_checkbox%5D=true&_run=&pfRunQueryFormName=MatchHistoryGame&wpRunQuery=&pf_free_text=",
        "https://lol.fandom.com/wiki/Special:RunQuery/MatchHistoryGame?MHG%5Bpreload%5D=Team&MHG%5Btournament%5D=&MHG%5Bteam%5D=T1&MHG%5Bteam1%5D=&MHG%5Bteam2%5D=&MHG%5Bban%5D=&MHG%5Brecord%5D=&MHG%5Bascending%5D%5Bis_checkbox%5D=true&MHG%5Blimit%5D=250&MHG%5Boffset%5D=250&MHG%5Bregion%5D=&MHG%5Byear%5D=&MHG%5Bstartdate%5D=&MHG%5Benddate%5D=&MHG%5Bwhere%5D=&MHG%5Btextonly%5D%5Bis_checkbox%5D=true&_run=&pfRunQueryFormName=MatchHistoryGame&wpRunQuery=&pf_free_text=",
        "https://lol.fandom.com/wiki/Special:RunQuery/MatchHistoryGame?MHG%5Bpreload%5D=Team&MHG%5Btournament%5D=&MHG%5Bteam%5D=T1&MHG%5Bteam1%5D=&MHG%5Bteam2%5D=&MHG%5Bban%5D=&MHG%5Brecord%5D=&MHG%5Bascending%5D%5Bis_checkbox%5D=true&MHG%5Blimit%5D=250&MHG%5Boffset%5D=500&MHG%5Bregion%5D=&MHG%5Byear%5D=&MHG%5Bstartdate%5D=&MHG%5Benddate%5D=&MHG%5Bwhere%5D=&MHG%5Btextonly%5D%5Bis_checkbox%5D=true&_run=&pfRunQueryFormName=MatchHistoryGame&wpRunQuery=&pf_free_text=",
        "https://lol.fandom.com/wiki/Special:RunQuery/MatchHistoryGame?MHG%5Bpreload%5D=Team&MHG%5Btournament%5D=&MHG%5Bteam%5D=T1&MHG%5Bteam1%5D=&MHG%5Bteam2%5D=&MHG%5Bban%5D=&MHG%5Brecord%5D=&MHG%5Bascending%5D%5Bis_checkbox%5D=true&MHG%5Blimit%5D=250&MHG%5Boffset%5D=750&MHG%5Bregion%5D=&MHG%5Byear%5D=&MHG%5Bstartdate%5D=&MHG%5Benddate%5D=&MHG%5Bwhere%5D=&MHG%5Btextonly%5D%5Bis_checkbox%5D=true&_run=&pfRunQueryFormName=MatchHistoryGame&wpRunQuery=&pf_free_text="
        #"https://lol.fandom.com/wiki/Special:RunQuery/MatchHistoryGame?MHG%5Bpreload%5D=Team&MHG%5Btournament%5D=&MHG%5Bteam%5D=T1&MHG%5Bteam1%5D=&MHG%5Bteam2%5D=&MHG%5Bban%5D=&MHG%5Brecord%5D=&MHG%5Bascending%5D%5Bis_checkbox%5D=true&MHG%5Blimit%5D=250&MHG%5Boffset%5D=&MHG%5Bregion%5D=&MHG%5Byear%5D=&MHG%5Bstartdate%5D=&MHG%5Benddate%5D=&MHG%5Bwhere%5D=&MHG%5Btextonly%5D%5Bis_checkbox%5D=true&MHG%5Btextonly%5D%5Bvalue%5D=&_run=&pfRunQueryFormName=MatchHistoryGame&wpRunQuery=&pf_free_text=",
        #"https://lol.fandom.com/wiki/Special:RunQuery/MatchHistoryGame?MHG%5Bpreload%5D=Team&MHG%5Btournament%5D=&MHG%5Bteam%5D=T1&MHG%5Bteam1%5D=&MHG%5Bteam2%5D=&MHG%5Bban%5D=&MHG%5Brecord%5D=&MHG%5Bascending%5D%5Bis_checkbox%5D=true&MHG%5Blimit%5D=250&MHG%5Boffset%5D=250&MHG%5Bregion%5D=&MHG%5Byear%5D=&MHG%5Bstartdate%5D=&MHG%5Benddate%5D=&MHG%5Bwhere%5D=&MHG%5Btextonly%5D%5Bis_checkbox%5D=true&MHG%5Btextonly%5D%5Bvalue%5D=&_run=&pfRunQueryFormName=MatchHistoryGame&wpRunQuery=&pf_free_text=",
        #"https://lol.fandom.com/wiki/Special:RunQuery/MatchHistoryGame?MHG%5Bpreload%5D=Team&MHG%5Btournament%5D=&MHG%5Bteam%5D=T1&MHG%5Bteam1%5D=&MHG%5Bteam2%5D=&MHG%5Bban%5D=&MHG%5Brecord%5D=&MHG%5Bascending%5D%5Bis_checkbox%5D=true&MHG%5Blimit%5D=250&MHG%5Boffset%5D=500&MHG%5Bregion%5D=&MHG%5Byear%5D=&MHG%5Bstartdate%5D=&MHG%5Benddate%5D=&MHG%5Bwhere%5D=&MHG%5Btextonly%5D%5Bis_checkbox%5D=true&MHG%5Btextonly%5D%5Bvalue%5D=&_run=&pfRunQueryFormName=MatchHistoryGame&wpRunQuery=&pf_free_text=",
        #"https://lol.fandom.com/wiki/Special:RunQuery/MatchHistoryGame?MHG%5Bpreload%5D=Team&MHG%5Btournament%5D=&MHG%5Bteam%5D=T1&MHG%5Bteam1%5D=&MHG%5Bteam2%5D=&MHG%5Bban%5D=&MHG%5Brecord%5D=&MHG%5Bascending%5D%5Bis_checkbox%5D=true&MHG%5Blimit%5D=250&MHG%5Boffset%5D=750&MHG%5Bregion%5D=&MHG%5Byear%5D=&MHG%5Bstartdate%5D=&MHG%5Benddate%5D=&MHG%5Bwhere%5D=&MHG%5Btextonly%5D%5Bis_checkbox%5D=true&MHG%5Btextonly%5D%5Bvalue%5D=&_run=&pfRunQueryFormName=MatchHistoryGame&wpRunQuery=&pf_free_text="
        ]

    def __init__(self, *args, **kwargs):
        super(LolfandomSpider, self).__init__(*args, **kwargs)
        # Kiểm tra và đọc ngày lớn nhất đã crawl
        if os.path.exists(STATE_FILE):
            with open(STATE_FILE, 'r') as f:
                self.max_date =  parse_datetime(json.load(f).get('max_date', ''))
        else:
            self.max_date = ''

    def save_state(self, date):
        date_str = date.strftime('%Y-%m-%d') if isinstance(date, datetime) else date
        with open(STATE_FILE, 'w') as f:
            json.dump({'max_date': date_str}, f)
        self.logger.info(f"Saved max date: {date_str}")


    def parse(self, response):
      rows = response.xpath('//table//tr')
      new_max_date = self.max_date if self.max_date else None
      for row in rows:
            tds = row.xpath('./td')
            if len(tds) < 12:
                  continue
            

            date_text = parse_datetime(tds[0].xpath('text()').get())

            print(f"Extracted date: {date_text}")
            print(f"Current max date: {self.max_date}")
            if not date_text:
                continue

            # Nếu date_text <= max_date đã lưu thì bỏ qua (data cũ)
            if self.max_date and date_text <= self.max_date:
                continue
            
            # Nếu date_text mới hơn thì cập nhật giá trị max_date tạm thời để lưu lại sau
            if date_text > new_max_date:
                new_max_date = date_text


            item = LolfandomItem()

            # Lấy dữ liệu region và tên giải
            region = tds[1].xpath('.//div[@class="region-icon"]/text()').get()
            tournament_name = tds[1].xpath('.//a/text()').get()

            # Xử lý tách tên giải và loại giải
            if region == "INT":
                  item['tournament'] = tournament_name 
                  item['tournament_type'] = "International" 
            else:
                  item['tournament'] = tournament_name
                  item['tournament_type'] = "Domestic"

            item['date'] = tds[0].xpath('text()').get()
            region = tds[1].xpath('.//div[@class="region-icon"]/text()').get()
            item['patch'] = tds[2].xpath('.//a/text()').get()
            item['result'] = tds[3].xpath('text()').get()
            item['side'] = tds[4].xpath('text()').get()
            item['enemy'] = tds[5].xpath('.//a/@title').get()


            # Lấy bans đội mình
            bans1 = tds[6].xpath('.//span/@title').getall()
            # Lấy bans đội đối thủ 
            bans2 = tds[7].xpath('.//span/@title').getall()

            # Lấy picks đội mình
            picks1 = tds[8].xpath('.//span/@title').getall()
            # Lấy picks đội đối thủ
            picks2 = tds[9].xpath('.//span/@title').getall()

            # Lấy danh sách tuyển thủ đội mình
            players = tds[10].xpath('.//a/text()').getall()

            # --- Phân tách bans ---
            for i in range(5):
                item[f'ban1_{i+1}'] = bans1[i] if i < len(bans1) else None
                item[f'ban2_{i+1}'] = bans2[i] if i < len(bans2) else None

            # --- Phân tách picks theo vị trí ---
            positions = ['top', 'jungle', 'mid', 'ad', 'support']
            for i, pos in enumerate(positions):
                item[f'pick1_{pos}'] = picks1[i] if i < len(picks1) else None
                item[f'pick2_{pos}'] = picks2[i] if i < len(picks2) else None

            # --- Phân tách players theo vị trí ---
            for i, pos in enumerate(positions):
                item[f'player_{pos}'] = players[i] if i < len(players) else None


            yield item

            # Cập nhật ngày lớn nhất tạm thời
            if new_max_date != self.max_date:
                self.save_state(new_max_date)
                print(f"Updated max date to: {new_max_date}")
            