import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException




def mainfn():
    
    def formfiller(link,i):
        try:
            driver.get(link)
            roll = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/input')
            emailad = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/input')
            time.sleep(3)
            roll.send_keys('19223032')
            time.sleep(3)
            emailad.send_keys('gunik.maliwal@gmail.com')
            time.sleep(3)
            driver.find_element_by_xpath("//*[contains(text(), 'Submit')]").click()
            time.sleep(3)
            print("Filled " + i + "Form")
            i+=1
        except:
            return

    options = webdriver.ChromeOptions() 
    options.add_argument(r"user-data-dir=C:\Users\GunikthegEEk\AppData\Local\Google\Chrome\User Data") #Path to your chrome profile
    driver = webdriver.Chrome(executable_path=r"C:\Users\GunikthegEEk\Documents\AutoAttendance nitrr teams\chromedriver.exe", chrome_options=options)
    driver.set_page_load_timeout(10)

    driver.get("https://teams.microsoft.com/_#/conversations/General?threadId=19:7d69bec3918a43f08dce8d248b0dd030@thread.tacv2&ctx=channel")

    time.sleep(10)
    elems = driver.find_elements_by_xpath("//a[@href]")
    for elem in elems:
        print(elem.get_attribute("href"))

    try:
        for _ in range (5):
            repl1 = driver.find_element_by_partial_link_text("2 replies from")
            print("element is: ")
            print(repl1)
            repl1.click()
            time.sleep(2)
    except NoSuchElementException:  #no error
        pass

    #getting docs links
    print("new links")
    elems = driver.find_elements_by_xpath('//a[contains(@href,"/docs.google.com")]')
    for elem in elems:
        print(elem.get_attribute("href"))

    links=[]
    for elem in elems:
        txt = elem.text
        if 'docs' in txt:
            links.append(txt)
    
    #test form - last link    
    links.append('https://docs.google.com/forms/d/e/1FAIpQLSfol4lDXXrjAqzLqGvdfBpiCocqYLHT7pBADjkgtLkoIJzp6A/viewform')
    
    print("new links:")
    print(links)
    i=0
    for link in links:
        i+=1
        formfiller(link,i)

        
    print("hi")
    driver.quit()
    return


for _ in  range (25):
    mainfn()
    time.sleep(600)