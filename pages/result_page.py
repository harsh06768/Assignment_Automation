from selenium.webdriver.common.by import By

class ResultPage:
    def __init__(self, driver):
        self.driver = driver

    output_text = (By.XPATH, "//div[contains(text(),'Output is:')]/div")

    def get_output(self):
        return self.driver.find_element(*self.output_text).text.strip()
