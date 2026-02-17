import pytest
from pages.home_page import HomePage
from pages.checkout_page import CheckoutPage


@pytest.mark.usefixtures("setup")
class TestGreenKart:

    def test_e2e_order(self):

        # open site
        self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

        # Home Page actions
        home = HomePage(self.driver)
        home.search_product("ber")
        home.add_product_to_cart("Cucumber")
        home.proceed_to_checkout_page()

        # Checkout Page actions
        checkout = CheckoutPage(self.driver)
        products = checkout.get_cart_product_names()

        # Validation
        assert any("Cucumber" in item for item in products)
