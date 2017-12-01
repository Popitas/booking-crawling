import scrapy


class RoomSpider(scrapy.Spider):
    name = "roomSpider"
    start_urls = ['https://www.booking.com/hotel/es/cordial-mogan-playa.en-gb.html?label=gen173nr-1DCAsoRkIdYXBhcnRhbWVudG9zLXB1ZXJ0by1kZS1tb2dhLW5ICVgEaEaIAQGYAS64AQbIAQzYAQPoAQH4AQKSAgF5qAID;sid=ff9a183fbe9fa83431649d942c63c25f;all_sr_blocks=9756806_102858594_0_17_0;bshb=2;checkin=2018-01-13;checkout=2018-01-19;dest_id=-387820;dest_type=city;dist=0;group_adults=2;hapos=2;highlighted_blocks=9756806_102858594_0_17_0;hpos=2;room1=A%2CA;sb_price_type=total;srepoch=1512136644;srfid=e8aec5c65d79399a5d79e665be6b7cf18fbf9a87X2;srpvid=4f6962218c1801f6;type=total;ucfs=1&#hotelTmpl']
    
    def parse(self, response):
        roomSelector = '.room_loop_counter1'

        for room in response.css(roomSelector):
            nameSelector = '.roomType span a ::text'
            occupancySelector = '.roomMaxPersons ::attr(data-occupancy-for-tracking)'
            priceSelector = '.roomPrice .roomDefaultUse strong ::text'

            yield {
                'name': room.css(nameSelector).extract_first(),
                'occupancy': room.css(nameSelector).extract_first(),
                'price': room.css(nameSelector).extract_first()
            }


