from src.judoka import Judoka; Judoka()
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains 
import pytube

# open browser
def init_browser(path="chromedriver"):
    browser = webdriver.Chrome(path)
    browser.maximize_window()
    return browser

# download the video at a given url
def download_video(url, location=None):
    youtube = pytube.YouTube(url)
    video = youtube.streams.first()
    video.download(location)


url = "https://www.ijf.org/judoka?name=&nation=FRA&gender=both&category=sen"
browser = init_browser()
browser.get(url)
judokas = browser.find_elements_by_class_name("judoka")
judoka_card = judokas[0]
judoka_info = judoka_card.find_element_by_class_name("judoka__info")
family_name = judoka_info.find_element_by_class_name("family_name").text
given_name = judoka_info.find_element_by_class_name("given_name").text
country = judoka_info.find_element_by_class_name("country").text
judoka = Judoka(family_name, given_name, country)
browser.get(judoka_card.get_attribute("href") + '/videos')