import pytest
from pages.home_page import HomePage


@pytest.mark.usefixtures("setup")
class TestGreenKart:

    def test_search_and_add_product(self):
        self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

        home = HomePage(self.driver)
        home.search_product("ber")
        home.add_product_to_cart("Cucumber")
