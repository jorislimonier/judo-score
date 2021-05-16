import os
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains 
import pytube
import subprocess

# open browser
def open_browser(path="chromedriver"):
    browser = webdriver.Chrome(path)
    browser.maximize_window()
    return browser


# download the video at a given url
def download_video(url, location=None):
    youtube = pytube.YouTube(url)
    video = youtube.streams.first()
    video.download(location)

def free_up_space(path):
    file_paths = [path + '\\' + file_path for file_path in os.listdir(path)]
    # Open files in fight_videos
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            # Free up space (OneDrive) after usage
            subprocess.run('attrib +U -P "' + file_path + '"')
    
# scrape ijf website
def download_fight_videos():
    start_time = time.time()
    browser = open_browser()
    # open ranking list
    browser.get('https://www.ijf.org/wrl?category=all')
    browser.find_element_by_css_selector('.btn.btn--red').click()
    print('Clicked ok on cookie button')
    time.sleep(1)
    # get judoka <td>
    judokas = browser.find_elements_by_css_selector('.name >a')
    # get judokas' link to profile
    judokas_video_section = [name.get_attribute('href') + '/videos' for name in judokas]
    # get judokas' name
    judokas_name = [jn.text for jn in judokas]
    # iterate over judokas
    for judoka_i in range(44, 47):
        try:
            name = judokas_name[judoka_i]
            fighter_subfolder_name = './fight_videos/' +  name.lower().replace(' ', '_')
            video_section_link = judokas_video_section[judoka_i]
            print(f'\n----- {judoka_i} - {name} -----')
            # open video section
            profile = browser.get(video_section_link)
            time.sleep(5)
            judoka_videos = browser.find_elements_by_css_selector('.video-list-thumb')
            for video in judoka_videos[6:8]:
                print(f'\nTrying to download video {judoka_videos.index(video)} . . .')
                for _ in range(3):
                    try:
                        print('...moving to video')
                        time.sleep(3)
                        actions = ActionChains(browser)
                        actions.move_to_element(video).perform()
                        video.click()

                        # get url of fight
                        print('......getting url of fight')
                        iframe = browser.find_element_by_css_selector('iframe')
                        browser.switch_to.frame(iframe)
                        fight_url = browser.find_element_by_css_selector('.ytp-title-link.yt-uix-sessionlink').get_attribute('href')
                        # download fight video
                        print('............trying to download fight videos')
                        download_video(fight_url, location=fighter_subfolder_name)
                        print(f'..............................ok download {judoka_videos.index(video)}')
                        browser.switch_to.default_content()
                        break
                    except:
                        print('/!\ There has been a problem while trying to download the video')
                        time.sleep(2)
                        browser.switch_to.default_content()
            free_up_space(fighter_subfolder_name)
        except:
            print(f'/!\ There has been a problem while reaching the profile of {name}')
    browser.quit()
    print(int(time.time() - start_time), 'seconds')
    
download_fight_videos()

