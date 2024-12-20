from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time  # For pauses
import random  # For randomized pauses
import pandas as pd
from config import app, db
from models import Movie

class LetterboxdScraper:
    def __init__(self, username, driver_path, browser_binary = None, headless = False):
        self.username = username
        self.driver_path = driver_path
        self.browser_binary = browser_binary
        self.headless = headless
    
    def set_up_driver(self):
        options = Options()
        options.headless = self.headless
        options.add_argument('window_size=1920x1080')
        if self.browser_binary:
            options.binary_location = self.browser_binary

        service = Service(self.driver_path)
        self.driver = webdriver.Chrome(service=service, options=options)

    def scrape_movies(self):
        if not self.driver:
            raise RuntimeError("Driver is not set up. Call set_up_driver() first.")
        website = f'https://letterboxd.com/{self.username}/watchlist/'

        self.driver.get(website)

        def check_next_page_exists(xpath):
            try:
                self.driver.find_element(By.XPATH, xpath)
            except:
                return False
            return True
        
        xpath = '//div[@class="pagination"]'

        if check_next_page_exists(xpath):
        #setting up variables for pagination
            pagination = self.driver.find_element(By.XPATH, '//div[@class="pagination"]')
            pages = pagination.find_elements(By.XPATH, './/li')
            next_page = pagination.find_element(By.XPATH, './/a[@class="next"]')
            last_page = int(pages[-1].text)
        else:
            next_page = 1 # goes into while loop once just for the one page

        movie_title = []
        movie_release = []
        movie_img_url = []
        movie_url = []
        current_page = 1

        while next_page:

            if check_next_page_exists(xpath):
                pagination = self.driver.find_element(By.XPATH, '//div[@class="pagination"]')

            # container = self.driver.find_element(By.XPATH, '//ul[contains(@class , "poster-list")]')
            container = WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.XPATH, '//ul[contains(@class , "poster-list")]')))

            movies = WebDriverWait(container,5).until(EC.presence_of_all_elements_located((By.XPATH, './li')))
            for movie in movies:

                title_element = WebDriverWait(movie,5).until(EC.presence_of_element_located((By.XPATH, './/div[@data-film-name]'))).get_attribute('data-film-name')
                year_element = WebDriverWait(movie,5).until(EC.presence_of_element_located((By.XPATH, './/div[@data-film-release-year]'))).get_attribute('data-film-release-year')
                img_url_element = WebDriverWait(movie,5).until(EC.presence_of_element_located((By.XPATH, './/img[@src]'))).get_attribute('src')
                url_element = WebDriverWait(movie,5).until(EC.presence_of_element_located((By.XPATH, './/a[@href]'))).get_attribute('href')

                movie_title.append(title_element)
                movie_release.append(year_element)
                movie_img_url.append(img_url_element)
                movie_url.append(url_element)
            try:
                next_page = WebDriverWait(pagination, 10).until(EC.element_to_be_clickable((By.XPATH, './/a[@class="next"]')))
                next_page.click()
                current_page += 1
            except:
                next_page = None

        movies = [{'title': movie_title, 
                   'releaseYear': movie_release, 
                   'imgUrl': movie_img_url,
                   'movieUrl': movie_url
                   } for movie_title, movie_release, movie_img_url, movie_url in zip(movie_title, movie_release, movie_img_url, movie_url)
        ]
        
        return movies
    
    def quit_driver(self):
        if self.driver:
            self.driver.quit()
            self.driver = None

def add_movies_to_database(movies):
    with app.app_context():
        for movie in movies:
            existing_movie = Movie.query.filter_by(title = movie['title'], release_year=movie['releaseYear']).first()
            if not existing_movie:
                new_movie = Movie(title = movie['title'],
                                  release_year = movie['releaseYear'],
                                  img_url = movie['imgUrl'],
                                  movie_url = movie['movieUrl'])
                db.session.add(new_movie)
        db.session.commit()


if __name__ == "__main__":
    username = 'mowiah' # filler until I build input alg
    driver_path = '/Users/drewgoldstein/workspace/github.com/ultraluckyclover/fullstack_letterboxd_scraper/backend/chromedriver-mac-arm64/chromedriver'
    browser_binary = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'


    scraper = LetterboxdScraper(username, driver_path, browser_binary, headless = False)
    start = time.time()
    try:
        scraper.set_up_driver()
        movies = scraper.scrape_movies()
        add_movies_to_database(movies) # SQLite database

        # pandas dataframe for easy testing
        df_movies = pd.DataFrame({
            "movieTitle": movie['title'],
            "year": movie['releaseYear'],
            "imageUrl": movie['imgUrl'],
            "url": movie['movieUrl']
        } for movie in movies)

        df_movies.to_csv('movies.csv', index = True)
    finally:
        scraper.quit_driver()

    end = time.time()

    print(f'Runtime: { end - start } seconds')