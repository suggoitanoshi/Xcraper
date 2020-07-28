import scrapy

class Kanji(scrapy.Spider):
  name = "kanji"
  def start_requests(self):
    url = 'http://www.studykanji.net/kanjilist?JLPTLevel='
    for i in range(1,6):
      yield scrapy.Request(url=f'{url}N{i}', callback=self.get_list)
  def get_list(self, request):
    detail_url = 'http://www.studykanji.net/kanjidetail/index'
    for kanji in request.css('.kanji-detail'):
      yield scrapy.FormRequest(url=detail_url, method='POST', formdata={'KanjiId':kanji.css("a::attr(id)").get()}, callback=self.get_details)
  def get_details(self, request):
    yield {
      "kanji": request.css("#kanji p::text").get(),
      "details": {
        "meaning": request.css("#english::text").get(),
        "onyomi": request.css("#on-yomi::text").get(),
        "kunyomi": request.css("#kun-yomi::text").get()
      }
    }