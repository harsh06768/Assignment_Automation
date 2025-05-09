from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.input_page import InputPage
from pages.result_page import ResultPage
import time

@given("I launch the browser and open the input page")
def launch_browser(context):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    context.driver.get("https://agrichain.com/qa/input")

@when('I enter the string "{input_text}" and click submit')
def enter_input_and_submit(context, input_text):
    input_page = InputPage(context.driver)
    input_page.enter_input(input_text)
    input_page.click_submit()
   

@then("I switch to the result tab")
def switch_to_result_tab(context):
    context.driver.switch_to.window(context.driver.window_handles[1])

@then('I should see output "{expected_output}"')
def verify_output(context, expected_output):
    result_page = ResultPage(context.driver)
    actual_output = result_page.get_output()
    assert actual_output == expected_output, f"Expected: {expected_output}, but got: {actual_output}"
