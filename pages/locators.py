from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary")
    BOOK_TITLE_ON_PAGE = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_TITLE_IN_BASKET = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success .alertinner strong")
    BOOK_PRICE_ON_PAGE = (By.CSS_SELECTOR, "h1 + .price_color")
    BOOK_PRICE_IN_BASKET = (By.CSS_SELECTOR, "div.alertinner > p > strong ")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success .alertinner strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")    