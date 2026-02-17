from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    # ---------------- LOCATORS ----------------
    search_box = (By.CSS_SELECTOR, "input.search-keyword")
    product_names = (By.CSS_SELECTOR, "h4.product-name")
    add_to_cart_buttons = (By.XPATH, "//div[@class='product-action']/button")
    cart_icon = (By.CSS_SELECTOR, "a.cart-icon")
    proceed_to_checkout = (By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")

    # ---------------- ACTIONS ----------------

    def wait_for_products(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(lambda d: len(d.find_elements(*self.product_names)) > 0)

    def search_product(self, text):
        wait = WebDriverWait(self.driver, 10)
        search = wait.until(EC.visibility_of_element_located(self.search_box))
        search.clear()
        search.send_keys(text)
        self.wait_for_products()

    def get_product_list(self):
        return self.driver.find_elements(*self.product_names)

    def add_product_to_cart(self, product_name):
        products = self.get_product_list()
        buttons = self.driver.find_elements(*self.add_to_cart_buttons)

        for i in range(len(products)):
            if product_name in products[i].text:
                buttons[i].click()
                break

    def open_cart(self):
        self.driver.find_element(*self.cart_icon).click()

    def proceed_to_checkout_page(self):
        self.open_cart()
        self.driver.find_element(*self.proceed_to_checkout).click()
