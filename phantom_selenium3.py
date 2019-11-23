from selenium import webdriver
import time

driver = webdriver.PhantomJS()
driver.get("http://www.baidu.com/")
kw = driver.find_element_by_id("kw")
kw.send_keys("朱一龙")
su = driver.find_element_by_id("su")
su.click()
time.sleep(1)
driver.save_screenshot("zhuyil.png")
driver.quit()