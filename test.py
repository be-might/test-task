from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.get("https://mathguru.live/?source=test")

element = driver.find_element(By.XPATH, "//div[@class='col-7']//a[@class='btn btn-outline-black w-100 font-weight-bold'][contains(text(),'I’ll send it later')]")
#
# actions = ActionChains(driver)
# actions.move_to_element(element).perform()


driver.execute_script("arguments[0].scrollIntoView();", element)
sleep(5)
driver.implicitly_wait(50)
