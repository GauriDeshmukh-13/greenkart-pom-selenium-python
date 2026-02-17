from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    # ---------------- LOCATORS ----------------
    cart_products = (By.CSS_SELECTOR, "p.product-name")
    promo_code_input = (By.CSS_SELECTOR, ".promoCode")
    apply_button = (By.CSS_SELECTOR, ".promoBtn")
    place_order_button = (By.XPATH, "//button[text()='Place Order']")

    # ---------------- ACTIONS ----------------

    def get_cart_product_names(self):
        products = self.driver.find_elements(*self.cart_products)
        return [product.text for product in products]

    def enter_promo_code(self, code):
        self.driver.find_element(*self.promo_code_input).send_keys(code)

    def apply_promo_code(self):
        self.driver.find_element(*self.apply_button).click()

    def place_order(self):
        self.driver.find_element(*self.place_order_button).click()
