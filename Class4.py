from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.chrome.options
import selenium.webdriver.firefox.options
import selenium.webdriver.ie.options

chrome_driver = webdriver.Chrome(executable_path='C:/Temp/chromedriver.exe')
firefox_driver = webdriver.Firefox(executable_path='C:/Temp/geckodriver.exe')

# 1
chrome_driver.get("https://www.walla.co.il")
firefox_driver.get("https://www.ynet.co.il")

# 2
title = chrome_driver.title
print(title)
chrome_driver.refresh()
if(title == chrome_driver.title):
    print("Equals!")

# 3 - yes the element has the same location in any browser

# 4
chrome_driver.get("https://translate.google.co.il/#view=home&op=translate&sl=auto&tl=en")
chrome_driver.find_element_by_id("source").send_keys("כלב")

# 5 + 6
chrome_driver.get("https://youtube.com")
chrome_driver.find_element_by_id("search").send_keys("liar")
chrome_driver.find_element_by_id("search-icon-legacy").click()

# 7
chrome_driver.get("https://facebook.com")
chrome_driver.find_element_by_id("email").send_keys("aaa@aaa.aaa")
chrome_driver.find_element_by_id("pass").send_keys("bbbbb")
chrome_driver.find_element_by_id("u_0_2").click()

# 8
chrome_driver.get("https://facebook.com")
chrome_driver.delete_all_cookies()
print(chrome_driver.get_cookies())

# 9
chrome_driver.get("https://github.com")
chrome_driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/div/div/div/form/label/input[1]").send_keys("Selenium" + Keys.ENTER)

# 10
chrome_options = selenium.webdriver.chrome.options.Options()
chrome_options.add_argument("--disable-extensions")
chrome_browser = webdriver.Chrome(executable_path='C:/Temp/chromedriver.exe',options=chrome_options)

firefox_options = selenium.webdriver.firefox.options.Options()
firefox_options.add_argument("--disable-extensions")
firefox_options = webdriver.Firefox(executable_path='C:/Temp/geckodriver.exe',options=firefox_options)

ie_options = selenium.webdriver.ie.options.Options()
ie_options.add_argument("--disable-extensions")
ie_options = webdriver.Ie(executable_path='C:/Temp/IEDriverServer.exe',options=ie_options)

