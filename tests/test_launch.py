import pytest
from pages.home_page import HomePage
from pages.checkout_page import CheckoutPage
from utils.data_reader import load_test_data


@pytest.mark.usefixtures("setup")
class TestGreenKart:

    def test_e2e_order(self):

        data = load_test_data()

        self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

        home = HomePage(self.driver)
        home.search_product(data["search_text"])
        home.add_product_to_cart(data["product_name"])
        home.proceed_to_checkout_page()

        checkout = CheckoutPage(self.driver)
        products = checkout.get_cart_product_names()

        assert any(data["product_name"] in item for item in products)
