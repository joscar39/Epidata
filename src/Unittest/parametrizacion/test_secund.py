
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# class TestSecund(unittest.TestCase):
#
#     # def setUp(self):
#     # chrome_options = Options()
#     # chrome_options.add_argument("--headless")
#     # self.driver = webdriver.Chrome(
#     #     chrome_options=chrome_options, executable_path=r"C:\Users\user\Documents"
#     #                                                    r"\Habits.ai\Automatizacion\q"
#     #                                                    r"a_automation\recursos\chromedriver.exe")
#     def setUp(self):
path = Service("../maquina/Resources/chromedriver.exe")
driver = webdriver.Chrome(service=path)

    # def test_case1(self):
web = "https://www.lambdatest.com/"
# driver = self.driver
driver.get(web)
driver.maximize_window()
# Obtener el título de la página web
web_title = driver.title
result_test = False
# Comparar el título de la página web con el título dado
if web_title == "Most Powerful Cross Browser Testing Tool Online | LambdaTest":
    result_test = True
else:
    result_test = False
assert result_test is True, "El título de la página no coincide con el título dado."
print("El título de la página coincide con el título dado.")

# def tearDown(self):
driver.close()


# if __name__ == '__main__':
#     suite = unittest.TestLoader().loadTestsFromTestCase(TestSecund)
#     unittest.TextTestRunner(verbosity=2).run(suite)