from judoka import Judoka, Fight
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
        """ iterate over judokas from the IJF list of judokas to get
        their given_name, family_name, country and profile_url"""
        driver = self.init_browser(self.url)
        judoka_cards = driver.find_elements_by_class_name("judoka")
        init_judokas = [self.init_judoka(judoka_card) for judoka_card in judoka_cards]
        driver.quit()
        return init_judokas

    def scrape_fights(self, judoka):
        """ iterate over the fights of one judoka on their IJF contest page"""
        driver = self.init_browser(judoka.profile_url + "/contests")

        # Accept cookies
        driver.find_element_by_class_name("btn--red").click()

        # Click table view
        driver.find_elements_by_class_name("opt")[1].click()

        # Scrape information from contest tile
        table_rows = driver.find_elements_by_class_name("contest-table__contest--has-media")

        fights_info = []
        for row_nb in [0, *range(len(table_rows)-1)]:
            print(f"=== {row_nb} ===")

            # get info from row header
            table_rows = driver.find_elements_by_class_name("contest-table__contest--has-media")
            table_row = table_rows[row_nb]
            row_cells = table_row.find_elements_by_tag_name("td")
            competition = row_cells[10].text
            date = row_cells[12].text

            # open video and score sections below row header
            row_cells[0].click()

            # get both judokas' info
            white, blue = driver.find_elements_by_class_name("judoka-info")
            colors = [white, blue]
            family_name = [color.find_element_by_class_name("family-name").text  for color in colors]
            given_name = [color.find_element_by_class_name("given-name").text  for color in colors]
            country = [color.find_element_by_class_name("country").text  for color in colors]
            profile_url = [color.get_attribute("href")  for color in colors]
            white_athlete, blue_athlete = [Judoka(family_name[i], given_name[i], country[i], profile_url[i]) for i in range(2)]

            # get score
            scores = driver.find_element_by_class_name("scores")
            category_and_round = scores.find_element_by_class_name("title").text

            fight_info = Fight(
                white=white_athlete,
                blue=blue_athlete,
                competition=competition,
                date=date,
                category_and_round=category_and_round,
            )

            print(vars(fight_info.blue))
            print(vars(fight_info.white))
            print(vars(fight_info))

            fights_info.append(fight_info)
        return fights_info






