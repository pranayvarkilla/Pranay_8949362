from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.youtube.com")
time.sleep(3)

search_bar = driver.find_element("name", "search_query")
search_bar.send_keys("music videos")

search_bar.send_keys(Keys.RETURN)

time.sleep(3)

assert "music videos" in driver.title

first_video = driver.find_element("xpath", "//a[@id='video-title']")
first_video.click()

time.sleep(10)

pause_button = driver.find_element("xpath", "//button[@class='ytp-play-button ytp-button']")
pause_button.click()

volume_button = driver.find_element("xpath", "//button[@class='ytp-mute-button ytp-button']")
volume_button.click()

youtube_logo = driver.find_element("xpath", "//a[@id='logo-icon-container']")
youtube_logo.click()

time.sleep(3)

assert "YouTube" in driver.title

driver.quit()
