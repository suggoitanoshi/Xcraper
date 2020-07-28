import scrapy

class Kurikulum(scrapy.Spider):
  name = "kurikulum"

  def start_requests(self):
    nim = 00000000
    cookies = {
      "uitb": "sesuatu",
      "_auth": "ina",
      "khongguan": "sesuatu"
    }
    urls = [
      f"https://akademik.itb.ac.id/app/mahasiswa:{nim}/kurikulum/struktur?fakultas=&th_kur=2019"
    ]
    yield scrapy.Request(url=urls[0], cookies=cookies, callback=self.parse)
  def parse(self, response):
    for fak in response.css("#prodi optgroup"):
      yield {
        "fakultas": fak.css("::attr(label)").extract()[0],
        "prodi": fak.css("option::attr(value)").extract()[0]
      }
    # do something