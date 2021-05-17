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
        return [self.init_judoka(judoka_card) for judoka_card in judoka_cards]

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
            # white =
            # blue =
            # competition =
            # date =
            # winner =
            # category =
            # comp_round =
