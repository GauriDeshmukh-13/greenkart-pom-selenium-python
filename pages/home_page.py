from selenium.webdriver.common.by import By


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

    def search_product(self, text):
        self.driver.find_element(*self.search_box).send_keys(text)

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
