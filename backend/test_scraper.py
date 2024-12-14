import unittest
from unittest.mock import patch, MagicMock
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from LetterboxdScraper import LetterboxdScraper
import pandas as pd
import time


class TestScraperObject(unittest.TestCase):
    def setUp(self):
        print("Setting up test...")
        self.username = 'mowiah'
        self.driver_path = '/Users/drewgoldstein/workspace/github.com/ultraluckyclover/fullstack_letterboxd_scraper/backend/chromedriver-mac-arm64/chromedriver'
        self.browser_binary = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

        self.scraper = LetterboxdScraper(username = self.username, 
                                         driver_path = self.driver_path, 
                                         browser_binary = self.browser_binary, 
                                         headless = False)
    @patch("selenium.webdriver.Chrome")
    def test_set_up_driver(self, mock_chrome):

        mock_driver = MagicMock()
        mock_chrome.return_value = mock_driver
        
        self.scraper.set_up_driver()

        mock_chrome.assert_called_once()
        self.assertIsNotNone(self.scraper.driver)

    
    # @patch(webdriver.Chrome)
    # def test_scrape_movies(self, mock_chrome):

    #     mock_driver = MagicMock()
    #     mock_chrome.return_value = mock_driver

    #     self.scraper.set_up_driver()
    
    @patch("selenium.webdriver.Chrome")
    def test_quit_scraper(self, mock_chrome):
        mock_driver = MagicMock()
        mock_chrome.return_value = mock_driver
        self.scraper.set_up_driver()

        self.scraper.quit_driver()
        self.assertIsNone(self.scraper.driver)

    def tearDown(self):
        if self.scraper:
            self.scraper.quit_driver()
        self.scraper = None




#     def setUp(self):
#         options = Options()
#         options.headless = False
#         options.add_argument('window_size=1920x1080')
#         options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
#         PATH = '/Users/drewgoldstein/workspace/github.com/ultraluckyclover/fullstack_letterboxd_scraper/backend/chromedriver-mac-arm64/chromedriver'
#         service = Service(PATH)
#         driver = webdriver.Chrome(service=service, options=options)

#         username = 'mowiah' # This is a placeholder
#         website = f'https://letterboxd.com/{username}/watchlist/'

#         self.driver.get(website)

#     def test_scrape_movies(self):

#         movie_title, movie_release, movie_img_url, movie_url = scrape_movies()

#         df_movies = pd.DataFrame({'title': movie_title, 'year': movie_release})
#         df_movies.to_csv('movies.csv', index=False)


# testing browser set up

# class TestBrowserSetup(unittest.TestCase):

#     def setUp(self):
#         # Set up Chrome options
#         self.options = Options()
#         self.options.headless = False  # Set to False to see the browser
#         self.options.add_argument('window_size=1920x1080')
#         self.options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
#         self.PATH = './chromedriver-mac-arm64/chromedriver'
#         self.service = Service(self.PATH)
        
#     def test_browser_initialization(self):
#         # Initialize WebDriver with options and Service
#         driver = webdriver.Chrome(service=self.service, options=self.options)

#         driver.get("https://letterboxd.com")

#         # Assert that the title of the page is correct to confirm page is loaded
#         self.assertIn("Letterboxd • Social film discovery.", driver.title)
#         time.sleep(3)

#         try:
#             driver.find_element(By.ID, "search-q")
#             element_found = True
#         except:
#             element_found = False

#         self.assertTrue(element_found, "Search bar found on the page")

#         # Close the driver
#         driver.quit()


# testing scraper        

# class TestScraper(unittest.TestCase):

#     def setUp(self):
#         # Set up Chrome options
#         self.options = Options()
#         self.options.headless = False  # Set to False to see the browser
#         self.options.add_argument('window_size=1920x1080')
#         self.options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
#         self.PATH = './chromedriver-mac-arm64/chromedriver'
#         self.service = Service(self.PATH)

#     def test_scrape_watchlist(self):

#         # testing with my watchlist

#         driver = webdriver.Chrome(service=self.service, options=self.options)
#         driver.get('https://letterboxd.com/drewiepiebear/watchlist/')


#         # Assert that the title of the page is correct to confirm page is loaded
#         self.assertIn("Drew's Watchlist • Letterboxd", driver.title)
#         time.sleep(3)

#         try:
#             driver.find_element(By.XPATH, "//li[@class = 'poster-container']" )
#             element_found = True
#         except: 
#             element_found = False
        
#         self.assertTrue(element_found, "Movie found on the page")

#         driver.quit()


# class TestScraperFunction(unittest.TestCase):

    
if __name__ == "__main__":
    unittest.main()

