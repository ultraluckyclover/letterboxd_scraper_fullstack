from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time  # For pauses
import random  # For randomized pauses

options = Options()
options.headless = False
options.add_argument('window_size=1920x1080')
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

def scrape_movies():

    PATH = '/Users/drewgoldstein/workspace/github.com/ultraluckyclover/fullstack_letterboxd_scraper/backend/chromedriver-mac-arm64/chromedriver'
    service = Service(PATH)
    driver = webdriver.Chrome(service=service, options=options)


    username = 'drewiepiebear'
    website = f'https://letterboxd.com/{username}/watchlist/'

    driver.get(website)
      # Pause to keep the browser open for observation
    time.sleep(10)

    # Close the browser after the delay
    driver.quit()


if __name__ == "__main__":
    scrape_movies()