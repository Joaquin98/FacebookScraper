import undetected_chromedriver as uc
from fp.fp import FreeProxy


def set_proxy(options):
    proxy_server_url = FreeProxy(timeout=1).get()
    options.add_argument(f"--proxy-server={proxy_server_url}")


def get_driver():
    options = uc.ChromeOptions()
    # set_proxy(options)
    driver = uc.Chrome(options=options)
    return driver
