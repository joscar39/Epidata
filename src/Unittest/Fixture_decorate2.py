# import allure
# import pytest
# import time
#
# from allure_commons.types import AttachmentType
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import TimeoutException
# from Funciones import Funciones_Globales
# from Page_Login import Funciones_Login
# from selenium.webdriver import ActionChains
# t=.8
#
# #Para imagenes de Error
#
# @pytest.fixture()
# def log_on_failure(request):
#     yield
#     item = request.node
#     if item.rep_call.failed:
#         allure.attach(driver.get_screenshot_as_png(), name="Error", attachment_type=AttachmentType.PNG)
#
#
# @pytest.fixture(scope='module')
# def setup_login_uno():
#     global driver, f
#     driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
#     driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
#     driver.maximize_window()
#     driver.implicitly_wait(20)
#     f = Funciones_Globales(driver)
#     f.Texto_Mixto("id", "Email", "admin@yourstore.com", t)
#     f.Texto_Mixto("id", "Password", "admin", t)
#     f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", t)
#     print("Entrando al sistema")
#     yield
#     print("Salida del login uno")
#     driver.close()
#
# @pytest.fixture(scope='module')
# def setup_Login_dos():
#     global driver, f
#     driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
#     driver.get("https://opensource-demo.orangehrmlive.com/")
#     driver.maximize_window()
#     driver.implicitly_wait(20)
#     f = Funciones_Globales(driver)
#     f.Texto_Mixto("id", "txtUsername", "Admin", t)
#     f.Texto_Mixto("id", "txtPassword", "admin123", t)
#     f.Click_Mixto("id", "btnLogin", t)
#     print("Entrando al sistema")
#     yield
#     print("Salida del login uno")
#     #driver.close()
#
#
# @pytest.mark.usefixtures("log_on_failure")
# @pytest.mark.usefixtures("setup_login_uno")
# def test_uno():
#     print("Entrando el sistema uno")
#     f.Click_Mixto("xpath","(//p[contains(.,'Customers')])[1]",t)
#     f.Click_Mixto("xpath","(//p[contains(.,'Customers')])[2]",t)
#     f.Texto_Mixto("xpath","//input[contains(@id,'SearchFirstName')]","victoria",t)
#     allure.attach(driver.get_screenshot_as_png(), name="buscando_nombre", attachment_type=AttachmentType.PNG)
#     f.Click_Mixto("xpath","//button[contains(@id,'search-customers')]",t)
#     allure.attach(driver.get_screenshot_as_png(),name="customers",attachment_type=AttachmentType.PNG)
#     #Creando un nuevo usuario
#     f.Click_Mixto("xpath","//a[@href='/Admin/Customer/Create']",t)
#     email=driver.find_element_by_xpath("//input[contains(@id,'Email')]")
#     email.send_keys("juan@gmail.com"+Keys.TAB+"12345"+Keys.TAB+"Juan"+Keys.TAB+"Perez")
#     time.sleep(3)
#     allure.attach(driver.get_screenshot_as_png(), name="datos", attachment_type=AttachmentType.PNG)
#     f.Click_Mixto("xpath","//input[contains(@id,'Gender_Male')]",t)
#     f.Texto_Mixto("xpath","//input[contains(@id,'DateOfBirth')]","2/20/2019",t)
#     allure.attach(driver.get_screenshot_as_png(), name="fecha", attachment_type=AttachmentType.PNG)
#     assert 1==2
#     driver.close()
#
#
# @pytest.mark.usefixtures("log_on_failure")
# @pytest.mark.usefixtures("setup_Login_dos")
# def test_dos():
#     print("Entrando el sistema dos")
#     f.Click_Mixto("xpath","//b[contains(.,'Admin')]",t)
#     f.Click_Mixto("xpath","//a[contains(@id,'menu_admin_UserManagement')]",t)
#     allure.attach(driver.get_screenshot_as_png(), name="Menu_admin", attachment_type=AttachmentType.PNG)
#     f.Texto_Mixto("xpath","//input[contains(@id,'searchSystemUser_userName')]","ananya Dash",t)
#     f.Click_Mixto("xpath","//input[contains(@id,'searchBtn')]",t)
#     allure.attach(driver.get_screenshot_as_png(), name="buscando", attachment_type=AttachmentType.PNG)
#     f.Click_Mixto("xpath","//input[contains(@id,'btnAdd')]",t)
#     allure.attach(driver.get_screenshot_as_png(), name="Agregando", attachment_type=AttachmentType.PNG)
#     f.Select_Xpath_Type("//select[contains(@id,'systemUser_userType')]","index",0,t)
#     assert 1 == 2
#     driver.close()
#
#

