from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Test_Data import data
from Test_Location import location
import time

class alert_practice():
     def __init__(self,alert_url):
         self.url = alert_url
         self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
         self.driver.get(self.url)
         self.driver.maximize_window()
         self.driver.implicitly_wait(10)

     def alert_btn(self):
         alertbtn = self.driver.find_element(by=By.XPATH,value = location.Location().alert_btn)
         self.driver.execute_script("arguments[0].scrollIntoView();",alertbtn)
         alertbtn.click()
         print("btn clicked")
         time.sleep(3)
         self.driver.switch_to.alert.accept()
         print("clicked ok button")

     def timer_alert(self):
         timerbtn= self.driver.find_element(by=By.XPATH,value = location.Location().timer_alert)
         self.driver.execute_script("arguments[0].scrollIntoView();", timerbtn)
         timerbtn.click()
         time.sleep(6)
         alertbox=self.driver.switch_to.alert
         print(alertbox.text) # It returns alertbox text
         alertbox.accept()

     def confirm(self):
         confirmbtn = self.driver.find_element(by=By.XPATH, value=location.Location().confirm_box)
         self.driver.execute_script("arguments[0].scrollIntoView();", confirmbtn)
         confirmbtn.click()
         time.sleep(2)

         # Click on ok button
         self.driver.switch_to.alert.accept()
         result = self.driver.find_element(by=By.XPATH, value='//*[@id="confirmResult"]')
         res= result.text
         print(res)
         print("click ok button")
     """
         #click on cancel button
         self.driver.switch_to.alert.dismiss()
         result1 = self.driver.find_element(by=By.XPATH, value='//*[@id="confirmResult"]')
         res1= result1.text
         print(res1)
         print("click on cancel button")
     """
     def prompt(self):
         promp=self.driver.find_element(by=By.XPATH,value= location.Location().prompt_box)
         self.driver.execute_script("arguments[0].scrollIntoView();", promp)
         promp.click()
         time.sleep(2)
         #enter text in prompt box and click ok
         promptbox = self.driver.switch_to.alert
         #promptbox.send_keys("shahiq")
         #print(promptbox.text)
         #promptbox.accept()
         print("Name entered click ok ")
         #enter text in prompt box and click cancel
         promptbox.dismiss()

a = alert_practice(location.Location().alert_url)
#a.alert_btn()
#a.timer_alert()
a.confirm()
#a.prompt()

