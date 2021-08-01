from _pytest import mark
from .pages.product_page import ProductPage
import pytest, time


@pytest.mark.parametrize('link', [#0, 1, 2, 3, 4, 5, 6,
                                  #pytest.param(7, marks=pytest.mark.xfail),
                                  8, 9])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.click_button_on_buccet()
    page.solve_quiz_and_get_code()
    page.test_guest_can_add_product_to_basket(link)
    #page.test_guest_cant_see_success_message_after_adding_product_to_basket()
    #page.test_guest_cant_see_success_message_after_adding_product_to_basket()
    #page.test_guest_cant_see_success_message()
    #page.test_message_disappeared_after_adding_product_to_basket()
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

