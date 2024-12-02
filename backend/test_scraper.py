import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


# testing browser set up

class TestBrowserSetup(unittest.TestCase):

    def setUp(self):
        # Set up Chrome options
        self.options = Options()
        self.options.headless = False  # Set to False to see the browser
        self.options.add_argument('window_size=1920x1080')
        self.options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        self.PATH = './chromedriver-mac-arm64/chromedriver'
        self.service = Service(self.PATH)
        
    def test_browser_initialization(self):
        # Initialize WebDriver with options and Service
        driver = webdriver.Chrome(service=self.service, options=self.options)

        driver.get("https://letterboxd.com")

        # Assert that the title of the page is correct to confirm page is loaded
        self.assertIn("Letterboxd • Social film discovery.", driver.title)
        time.sleep(3)

        try:
            driver.find_element(By.ID, "search-q")
            element_found = True
        except:
            element_found = False

        self.assertTrue(element_found, "Search bar found on the page")

        # Close the driver
        driver.quit()


# testing scraper        

class TestScraper(unittest.TestCase):

    def setUp(self):
        # Set up Chrome options
        self.options = Options()
        self.options.headless = False  # Set to False to see the browser
        self.options.add_argument('window_size=1920x1080')
        self.options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        self.PATH = './chromedriver-mac-arm64/chromedriver'
        self.service = Service(self.PATH)

    def test_scrape_watchlist(self):


        # testing with my watchlist

        driver = webdriver.Chrome(service=self.service, options=self.options)
        driver.get('https://letterboxd.com/drewiepiebear/watchlist/')


        # Assert that the title of the page is correct to confirm page is loaded
        self.assertIn("Drew’s Watchlist • Letterboxd", driver.title)
        time.sleep(3)

        try:
            driver.find_element(By.XPATH, "//li[@class = 'poster-container']" )
            element_found = True
        except: 
            element_found = False
        
        self.assertTrue(element_found, "Movie found on the page")

        driver.quit()

if __name__ == "__main__":
    unittest.main()

