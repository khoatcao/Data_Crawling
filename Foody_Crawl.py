from selenium import webdriver
import time
import pandas
import csv
import json
class get_content:
    def __init__(self):
        # set my driver path
        self.driver = webdriver.Chrome(executable_path= 'D:\My AI\Chrome\Chromedriver.exe')
    # navigate and crawl data from web
    def navigate_and_crawl(self):
        driver = self.driver
        driver.get("https://www.foody.vn/ho-chi-minh/nha-hang-san-fu-lou")
        time.sleep(5)
    # find_list_img
    def get_page_source(self):
        return self.driver.page_source
    # get title
    def get_title(self):
            return self.driver.title
    # get the current url
    def get_current_url(self):
           return self.driver.current_url
    # get address
    def get_address(self):
        return self.driver.find_element_by_xpath('//span[@itemprop="streetAddress"]').text
    # get Category
    def get_category(self):
        return self.driver.find_element_by_xpath('//div[@class = "category"]/div[@class = "category-items"]').text,self.driver.find_element_by_xpath('//div[@class = "category"]/div[@class = "category-cuisines"]').text
    def get_time(self):
        return self.driver.find_element_by_xpath('//div[@class = "res-common-price"]/div[@class = "micro-timesopen"]').text
    def get_price(self):
        return self.driver.find_element_by_xpath('//div[@class = "res-common-price"]/div[@class ="res-common-minmaxprice"]').text
    def get_quality(self):
        return self.driver.find_element_by_xpath('//*[@id="res-summary-point"]').text
    def get_list_img(self):
        imagines = self.driver.find_elements_by_tag_name('img')
        for imagine in imagines :
            scr = imagine.get_attribute('src')
            print(scr)

# enable objects
Crawling = get_content()
# get the driver path
print(Crawling.navigate_and_crawl())
# enable to see full page source code
#print(Crawling.get_page_source())
# display the title
print(Crawling.get_title())
# display the current url
print(Crawling.get_current_url())
print(Crawling.get_address())
print(Crawling.get_category())
print(Crawling.get_time())
print(Crawling.get_price())
print(Crawling.get_quality())
print(Crawling.get_list_img())