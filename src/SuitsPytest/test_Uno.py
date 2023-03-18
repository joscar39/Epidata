import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver



@pytest.fixture(autouse=True)
def start_automatic_fixture():
    print("Start Test With Automatic Fixture")


@pytest.fixture(scope="function")
def setup_login(web="http://consoledesarrollo.habits.ai/",
                email="consola@habitsqa.ai",
                password="Aa123456."):
    global driver
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-features=NetworkService')
    path = Service("../Resources/chromedriver.exe")
    driver = webdriver.Chrome(service=path, options=options)
    driver.get(web)
    driver.maximize_window()
    mail = driver.find_element(By.ID, "mail")
    mail.send_keys(email)
    passw = driver.find_element(By.ID, "password")
    passw.send_keys(password)
    login = driver.find_element(By.ID, "login_button")
    login.click()
    time.sleep(15)
    yield
    driver.quit()


@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="Error, Fallo la prueba", attachment_type=AttachmentType.PNG)


@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.usefixtures("setup_login")
def test_REG01():
    # Acceder a modulo operaciones
    operations = driver.find_element(By.XPATH, "//p[contains(text(), 'Operaciones')]")
    operations.click()
    time.sleep(10)
    challenge_module = driver.find_element(By.XPATH, "//p[contains(text(), 'Retos')]")
    challenge_module.click()
    time.sleep(10)


@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.usefixtures("setup_login")
def test_dos():

    mail = driver.find_element(By.XPATH, "//a[@id='menu_live_class']")
    mail.click()
    time.sleep(15)
    print("Prueba dos")


@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.usefixtures("setup_login")
def test_tres():

    mail = driver.find_element(By.XPATH, "//a[@id='menu_benefits']")
    mail.click()
    time.sleep(15)
    print("Prueba tres")
