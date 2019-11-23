from selenium import webdriver
from lxml import etree
import time
import csv

opt = webdriver.ChromeOptions()
opt.set_headless()

driver = webdriver.Chrome(options=opt)
driver.get("https://www.douyu.com/directory/all")
i = 1

while True:
    parseHtml = etree.HTML(driver.page_source)
    names = parseHtml.xpath('//div[@class="DyListCover-info"]/h2')
    numbers = parseHtml.xpath('//div[@class="DyListCover-info"]/span[@class="DyListCover-hot"]')
    for name,number in zip(names,numbers):
        print("\t主播名称:%s  \t观众人数:%s"%(name.text,number.text))
        with open("douyu.csv","a",newline="") as f:
            writer = csv.writer(f)
            L = [name.text,number.text]
            writer.writerow(L)
        print("第%d页爬取成功"%i)
        i += 1
        if driver.page_source.find('aria-disabled="true"') == -1:
            driver.find_element_by_class_name("dy-Pagination-item-custom").click()
            time.sleep(1)
        else:
            break
print("一个爬取了%d页"%i)