from scraper import Scraper

scrp = Scraper()
judokas = scrp.scrape_judokas()
for judoka in judokas[:5]:
    fght = scrp.scrape_fights(judoka)