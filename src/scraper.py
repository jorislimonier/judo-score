from .judoka import Judoka
import os
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains 
import pytube
import subprocess

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
judokas[0].get_attribute("href")

Judoka()