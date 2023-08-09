import undetected_chromedriver as uc
from fp.fp import FreeProxy


def get_driver():
    options = uc.ChromeOptions()
    proxy_server_url = FreeProxy(timeout=1).get()
    options.add_argument(f"--proxy-server={proxy_server_url}")
    driver = uc.Chrome(options=options)
    return driver
