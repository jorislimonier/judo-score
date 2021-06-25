from scraper import Scraper
import pandas as pd

scrp = Scraper()
judokas = scrp.scrape_judokas()
df_fights = pd.DataFrame()
for judoka in judokas[:3]:
    fights = scrp.scrape_fights(judoka)
    for fight in fights:
        white_name = " ".join([fight.white.family_name, fight.white.given_name])
        blue_name = " ".join([fight.blue.family_name, fight.blue.given_name])
        data = {"white": [white_name], "blue": [blue_name]}
        data.update({k: [v] for k,v in vars(fight).items() if k not in ["white", "blue"]})
        df_fight = pd.DataFrame(data=data)
        df_fights = df_fights.append(df_fight)

df_fights.to_csv("fights.csv")



