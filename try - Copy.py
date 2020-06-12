import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

options = webdriver.ChromeOptions() 
options.add_argument(r"user-data-dir=C:\Users\GunikthegEEk\AppData\Local\Google\Chrome\User Data") #Path to your chrome profile
driver = webdriver.Chrome(executable_path=r"C:\Users\GunikthegEEk\Documents\AutoAttendance nitrr teams\chromedriver.exe", chrome_options=options)
driver.set_page_load_timeout(10)
def formfiller(link,i):
    try:
        driver.get(link)
        roll = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/input')
        emailad = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/input')
        time.sleep(3)
        roll.send_keys('19667091')
        time.sleep(3)
        emailad.send_keys('smatyL@gmail.com')
        time.sleep(3)
        driver.find_element_by_xpath("//*[contains(text(), 'Submit')]").click()
        time.sleep(3)
        print("Filled " + i + "Form")
        i+=1
    except:
        return

i=0
links=['https://docs.google.com/forms/d/e/1FAIpQLSfol4lDXXrjAqzLqGvdfBpiCocqYLHT7pBADjkgtLkoIJzp6A/viewform','https://docs.google.com/forms/d/e/1FAIpQLScQdAprdvHbsl_iZbrr5n9-jdh5NjkLqKpiRGGwbRpC-xaIUg/viewform?usp=sf_link', 'https://docs.google.com/forms/d/e/1FAIpQLSfvDUaU_-jssm4fevHQwTDZjRZwO9bdHJZnkWb6m_kUzUW3Qw/viewform?usp=sf_link', 'https://docs.google.com/forms/d/e/1FAIpQLSdYyPvzYP38L5LoCJnrAKAx7ldyHvGM60TG23UGa8Y1q-mJGQ/viewform?usp=sf_link', 'https://docs.google.com/forms/d/e/1FAIpQLSfAB0vW70npC-9a8hbYBwQWYr4iHKmolhvTAxWlx74nbMA31w/viewform?usp=sf_link']
for link in links:
    i+=1
    formfiller(link,i)