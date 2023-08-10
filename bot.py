import undetected_chromedriver as uc
from fp.fp import FreeProxy
import driver_module
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import codecs
import csv


class Bot:

    selectors_dict = {
        'post_link': '//a[contains(@href,"https://www.facebook.com/CFKArgentina/posts/") and @role = "link"]',
        'close_login': '//div[@aria-label="Cerrar"]'
    }

    base_url = 'https://www.facebook.com/'
    __WAIT_FOR_ELEMENT_TIMEOUT = 10
    new_posts = set()
    all_posts = set()
    results_filename = "posts.csv"

    browser = driver_module.get_driver()

    def __init__(self) -> None:
        self.read_scraped_posts()

    def get_posts_urls(self, profile):
        self.browser.get(self.base_url + profile)
        WebDriverWait(self.browser, self.__WAIT_FOR_ELEMENT_TIMEOUT).until(
            EC.presence_of_element_located(
                (By.XPATH, self.selectors_dict['close_login']))
        )
        self.browser.find_element(
            By.XPATH, self.selectors_dict['close_login']).click()

        urls = set()

        while True:

            self.browser.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            links = self.browser.find_elements(
                By.XPATH, self.selectors_dict['post_link'])

            for link in links:
                url = link.get_attribute('href')
                if url not in self.all_posts:
                    self.new_posts.add(url)

            self.save_new_scraped_posts()
            time.sleep(10)

    def save_new_scraped_posts(self):
        posts_txt = ""
        for user in self.new_posts:
            posts_txt += user + "\n"
        file_obj = codecs.open(self.results_filename, 'a+', "utf-8")
        file_obj.write(posts_txt)
        file_obj.close()

    def read_scraped_posts(self):
        if not os.path.exists(self.results_filename):
            file = codecs.open(self.results_filename, 'a+', 'utf8')
            file.close()

        with codecs.open(self.results_filename, 'r+', "utf-8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                self.all_posts.add(
                    (row[0].strip()))
        return self.all_posts


bot = Bot()
bot.get_posts_urls('CFKArgentina')
