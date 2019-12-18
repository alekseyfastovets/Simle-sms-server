from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("headless")
driver = webdriver.Chrome(chrome_options = chrome_options)
driver.implicitly_wait(10)
driver.get("http://10.3.0.81:8888")
element = driver.find_element_by_xpath('//*[@id="block-desktop"]/div[2]/div/div[4]/div[4]').click()
elem = driver.find_element_by_xpath('//*[@id="block-desktop"]/div[1]/div/div[16]/div[1]/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div/div/div[1]/table/tbody/tr/td[2]/div/div/input')
elem.send_keys("0990000000")
elem.send_keys("0990000000")
elem2 = driver.find_element_by_xpath('//*[@id="block-desktop"]/div[1]/div/div[16]/div[1]/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div/div/div[4]/div/div[1]')
elem2.send_keys("Другое сообщение",Keys.ENTER)
qqq = driver.find_element_by_xpath('//*[@id="block-desktop"]/div[1]/div/div[16]/div[1]/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div/div/div[5]/button[2]')
time.sleep(5)
#qqq.click()
#driver.close()


