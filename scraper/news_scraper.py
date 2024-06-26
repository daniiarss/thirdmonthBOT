import requests
from parsel import Selector


class NewsScraper:
    URL = "https://ru.sputnik.kg/Kyrgyzstan/"
    HEADERS = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
"Accept-Encoding":"gzip, deflate, br, zstd",
"Accept-Language":"en-US,en;q=0.8",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0"
    }
    TITLE_XPATH = '//div[@class="list__content"]/a/text()'
    IMG_XPATH = '//div[@class="list__image"]/a/picture/img/@src'
    DESCRIPTION_XPATH = '//div[@class="article__text"]/text()'

    def scrape_data(self):
        response = requests.get(self.URL, headers=self.HEADERS)
        # print(response.text)
        tree = Selector(text=response.text)
        title = tree.xpath(self.TITLE_XPATH).getall()
        images = tree.xpath(self.IMG_XPATH).getall()
        descs = tree.xpath(self.DESCRIPTION_XPATH).getall()

        for i in descs:
            print(i)
    

if __name__ == "__main__":
    scraper = NewsScraper()
    scraper.scrape_data()