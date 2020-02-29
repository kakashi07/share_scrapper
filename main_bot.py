from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import os, sys,csv
import pandas as pd
import numpy as np

website_link  = 'https://www.sharesansar.com/today-share-price'

option = Options()
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2
})

def data_input_cleaner(x,volume_flg = False):
    x = x.replace(',','')
    if volume_flg == False:
        x = float(x)
    elif volume_flg == True:
        x = int(x)
    return x

class jordan():
    def __init__(self,data_list=[],dataset_date=None):
        self.driver = webdriver.Chrome(options=option)
        self.data_list = data_list

    def link_initiator(self):
        self.driver.get(website_link)
        time.sleep(5)
        self.dataset_date = self.driver.find_element_by_xpath('//*[@id="todayshareprice_data"]/h5/span').text
        # data = self.driver.find_element_by_xpath('//*[@id="headFixed_wrapper"]')

        # data = self.driver.find_element_by_xpath('//table/tbody/tr[1]/td[2]').text
        for i in range(1,179):
            temp = []
            date_of_scrap = self.dataset_date
            company_name = self.driver.find_element_by_xpath('//table/tbody/tr['+str(i)+']/td[2]').text
            closing_price =self.driver.find_element_by_xpath('//table/tbody/tr['+str(i)+']/td[7]').text
            volume_transacted = self.driver.find_element_by_xpath('//table/tbody/tr['+str(i)+']/td[9]').text
            TY_highest =self.driver.find_element_by_xpath('//table/tbody/tr['+str(i)+']/td[19]').text
            TY_lowest =self.driver.find_element_by_xpath('//table/tbody/tr['+str(i)+']/td[20]').text
            temp = [date_of_scrap,company_name,data_input_cleaner(closing_price),data_input_cleaner(volume_transacted,volume_flg=True),data_input_cleaner(TY_highest),data_input_cleaner(TY_lowest)]
            self.data_list.append(temp)

        return  self.data_list

    def csv_writer(self):
        output_filename = 'Share_Data_'+str(self.dataset_date)+'.csv'
        row_header = ['Date','Company','Closing Price','Volume Transacted','TY Highest','TY Lowest']
        with open(output_filename,'w',newline='') as file:
            writer = csv.writer(file,delimiter = '|')       # the | is system specific for \t in my old laptop. This might have to be changed in future.
            writer.writerows([row_header])
            for rows in self.data_list:
                writer.writerows([rows])

        return  True

x = jordan()
data  = x.link_initiator()
writing = x.csv_writer()
x.driver.close()

