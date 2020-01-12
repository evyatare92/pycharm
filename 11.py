from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from time import sleep

my_driver = webdriver.Chrome(executable_path='C:/Temp/chromedriver.exe')
def find_by_id(my_driver, element_id):
    try:
        return my_driver.find_element_by_id(element_id)
    except TypeError as e:
        return None

def find_by_xpath(my_driver, xpath):
    try:
        return my_driver.find_element_by_xpath(xpath)
    except TypeError as e:
        return None

def check_tip_calculation(my_driver):
    my_driver.get("file://C:/PycharmProjects/DevOps/tip_calc/index.html")
    find_by_id(my_driver, "billamt").send_keys("100")
    find_by_id(my_driver, "peopleamt").send_keys("5")
    find_by_xpath(my_driver, '//*[@id="serviceQual"]/option[3]').click()
    find_by_xpath(my_driver, '//*[@id="musicQual"]/option[4]').click()
    find_by_id(my_driver, "calculate").click()
    res = find_by_id(my_driver, "tip").text
    my_driver.close()
    if res == "4.60":
        return 0

my_driver.get("file://C:/PycharmProjects/DevOps/tip_calc/index.html")
my_driver.implicitly_wait(5)
my_driver.find_element_by_id("billamt").send_keys("100" + Keys.TAB + Keys.ARROW_DOWN*3 + Keys.SPACE)

print("1111")