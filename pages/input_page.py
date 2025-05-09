from selenium.webdriver.common.by import By

class InputPage:
    def __init__(self, driver):
        self.driver = driver

    input_field = (By.XPATH, "//input[@placeholder='Enter String Input...']")
    submit_button = (By.XPATH, "//button[text()='Submit']")

    def enter_input(self, input_text):
        self.driver.find_element(*self.input_field).clear()
        self.driver.find_element(*self.input_field).send_keys(input_text)

    def click_submit(self):
        self.driver.find_element(*self.submit_button).click()
