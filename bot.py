import undetected_chromedriver as uc
from fp.fp import FreeProxy
import driver_module
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Bot:

    base_url = 'https://www.facebook.com/'
    __WAIT_FOR_ELEMENT_TIMEOUT = 10

    browser = driver_module.get_driver()

    def get_posts_urls(self, profile):
        self.browser.get(self.base_url + profile)
        WebDriverWait(self.browser, self.__WAIT_FOR_ELEMENT_TIMEOUT).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@aria-label='Cerrar']"))
        )
        self.browser.find_element(
            By.XPATH, "//div[@aria-label='Cerrar']").click()

        urls = set()

        while True:
            time.sleep(4)
            self.browser.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            links = self.browser.find_elements(
                By.XPATH, '//a[contains(@href,"https://www.facebook.com/CFKArgentina/posts/") and @role = "link"]')

            for link in links:
                url = link.get_attribute('href')
                urls.add(url)

            print(urls)

        input()


bot = Bot()
bot.get_posts_urls('CFKArgentina')
