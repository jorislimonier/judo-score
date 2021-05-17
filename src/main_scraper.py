from src.scraper import Scraper

scr = Scraper()
judokas = scr.scrape_judokas()
for judoka in judokas:
    print(vars(judoka))
