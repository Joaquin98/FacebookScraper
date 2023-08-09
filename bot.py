import undetected_chromedriver as uc
from fp.fp import FreeProxy
import driver_module
from selenium.webdriver.common.by import By
import time


class Bot:

    base_url = 'https://www.facebook.com/'

    browser = driver_module.get_driver()

    def get_posts_urls(self, profile):
        self.browser.get(self.base_url + profile)
        # self.browser.find_element(
        #    By.XPATH, "//div[@aria-label='Cerrar']").click()

        urls = set()

        while True:
            links = self.browser.find_elements(
                By.XPATH, '//a[contains(@href,"https://www.facebook.com/CFKArgentina/posts/") and @role = "link"]')

            for link in links:
                url = link.get_attribute('href')
                urls.add(url)

            print(urls)

        input()


bot = Bot()
bot.get_posts_urls('CFKArgentina')
