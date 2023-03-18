import time
import pytest
from selenium.webdriver.chrome import webdriver

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def setup_function(function, email="consola@habitsqa.ai", password="Aa123456."):
    global driver
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-features=NetworkService')
    path = Service("../Resources/chromedriver.exe")
    driver = webdriver.Chrome(service=path, options=options)
    web = "http://consoledesarrollo.habits.ai/"
    driver.get(web)
    driver.maximize_window()
    mail = driver.find_element(By.ID, "mail")
    mail.send_keys(email)
    passw = driver.find_element(By.ID, "password")
    passw.send_keys(password)
    login = driver.find_element(By.ID, "login_button")
    login.click()
    time.sleep(15)


def teardown_function(function):
    driver.quit()


def test_login_uno():
    # Acceder a modulo operaciones
    operations = driver.find_element(By.XPATH, "//p[contains(text(), 'Operaciones')]")
    operations.click()
    time.sleep(10)
    challenge_module = driver.find_element(By.XPATH, "//p[contains(text(), 'Retos')]")
    challenge_module.click()
    time.sleep(10)
    # @pytest.fixture()
    # def log_on_failure_firefox(request, setup_Login):
    #     yield
    #     item = request.node
    #     driver = setup_Login
    #     if item.rep_call.failed:
    #         allure.attach(driver.get_screenshot_as_png(), name="Error, Fallo la prueba", attachment_type=AttachmentType.PNG)
    #
    # @pytest.fixture(scope="function")
    # def setup_Login():
    #     # Inicializacion de selenium
    #     global driver, f
    #     path = Service("../recursos/chromedriver.exe")
    #     driver = webdriver.Chrome(service=path)
    #     driver.implicitly_wait(20)
    #     web = "http://consoledesarrollo.habits.ai/"
    #     driver.get(web)
    #     driver.maximize_window()
    #     f = Funciones_Globales(driver)
    #     yield driver
    #     driver.quit()
    #
    # @pytest.mark.usefixtures("log_on_failure_chrome")
    # @pytest.mark.usefixtures("setup_Login")
    # def test_REG01(email="consola@habitsqa.ai", password="Aa123456."):
    #     time.sleep(2)
    #     f.Texto_Mixto("id", "mail", email, 0.5)
    #     f.Texto_Mixto("id", "password", password, 0.5)
    #     time.sleep(3)

    print("Prueba uno")
