from src.judoka import Judoka
from src.fight import Fight
from selenium import webdriver


class Scraper:
    def __init__(
        self, url="https://www.ijf.org/judoka?name=&nation=FRA&gender=both&category=sen"
    ):
        self.url = url  # change later. Now only going through french athletes

    @staticmethod
    def init_browser(url, path="chromedriver"):
        """open browser"""
        driver = webdriver.Chrome(path)
        driver.maximize_window()
        driver.get(url)
        return driver

    @staticmethod
    def init_judoka(judoka_card):
        """create instance of the Judoka class
        with family_name, given_name and country"""
        profile_url = judoka_card.get_attribute("href")
        judoka_info = judoka_card.find_element_by_class_name("judoka__info")
        family_name = judoka_info.find_element_by_class_name("family_name").text
        given_name = judoka_info.find_element_by_class_name("given_name").text
        country = judoka_info.find_element_by_class_name("country").text
        return Judoka(
            profile_url=profile_url,
            family_name=family_name,
            given_name=given_name,
            country=country,
        )

    def scrape_judokas(self):
        driver = self.init_browser(self.url)
        judoka_cards = driver.find_elements_by_class_name("judoka")
        init_judokas = [self.init_judoka(judoka_card) for judoka_card in judoka_cards]
        driver.quit()
        return init_judokas

    def scrape_fights(self, judoka):
        driver = self.init_browser(self.url)
        driver.get(judoka.profile_url + "/contests")
        driver.find_elements_by_class_name("opt")[1].click()  # click table view
        table_rows = driver.find_elements_by_class_name("contest-table__contest")
        for table_row in table_rows[0:1]:
            table_row_white = table_row.find_element_by_class_name("judoka--white")
            family_name = table_row_white.find_element_by_class_name(
                "judoka__name"
            ).text
            country = table_row_white.find_element_by_class_name("country").text


scrp = Scraper()
judokas = scrp.scrape_judokas()
judoka = judokas[1]

driver = scrp.init_browser(judoka.profile_url + "/contests")

# Accept cookies
driver.find_element_by_class_name("btn--red").click()

# Click table view
driver.find_elements_by_class_name("opt")[1].click()

# Scrape information from contest tile
table_rows = driver.find_elements_by_class_name("contest-table__contest--has-media")
for row_nb in [0, *range(len(table_rows))]:
    table_rows = driver.find_elements_by_class_name("contest-table__contest--has-media")
    table_row = table_rows[row_nb]
    row_cells = table_row.find_elements_by_tag_name("td")
    competition = row_cells[10].text
    date = row_cells[12].text
    # print("before click")
    row_cells[0].click()
    # print("after click")

    white, blue = driver.find_elements_by_class_name("judoka-info")
    family_name = white.find_element_by_class_name("family-name").text
    given_name = white.find_element_by_class_name("given-name").text
    country = white.find_element_by_class_name("country").text
    profile_url = white.get_attribute("href")
    white_athlete = Judoka(family_name, given_name, country, profile_url)

    family_name = blue.find_element_by_class_name("family-name").text
    given_name = blue.find_element_by_class_name("given-name").text
    country = blue.find_element_by_class_name("country").text
    profile_url = blue.get_attribute("href")
    blue_athlete = Judoka(family_name, given_name, country, profile_url)

    scores = driver.find_element_by_class_name("scores")
    score_title = scores.find_element_by_class_name("title").text
    round_cat = score_title

    fght = Fight(white=white_athlete, blue=blue_athlete, competition=competition, date=date, round_cat=round_cat) 

    vars(fght.blue)
    vars(fght.white)
    vars(fght)
    # if row_nb == 3:
    #     break
    print("==========")

row_nb