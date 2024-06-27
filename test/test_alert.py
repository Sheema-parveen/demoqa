import pytest
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


class Test_alert_practice():
     @pytest.fixture
     def startup(self):
         self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
         yield
         self.driver.close()

     def test_alert_btn(self,startup):
         self.driver.get(location.Location().alert_url)
         self.driver.maximize_window()
         self.driver.implicitly_wait(10)
         alertbtn = self.driver.find_element(by=By.XPATH,value = location.Location().alert_btn)
         self.driver.execute_script("arguments[0].scrollIntoView();",alertbtn)
         alertbtn.click()
         print("btn clicked")
         time.sleep(3)
         alertmsg =self.driver.switch_to.alert
         text_msg = alertmsg.text
         alertmsg.accept()
         assert "You clicked a button" == text_msg
         print("ok button clicked")

     def test_timer_alert(self,startup):
         self.driver.get(location.Location().alert_url)
         self.driver.maximize_window()
         self.driver.implicitly_wait(10)
         timerbtn= self.driver.find_element(by=By.XPATH,value = location.Location().timer_alert)
         self.driver.execute_script("arguments[0].scrollIntoView();", timerbtn)
         timerbtn.click()
         time.sleep(6)
         alertbox=self.driver.switch_to.alert
         ans= alertbox.text # It returns alertbox text
         alertbox.accept()
         assert ans == "This alert appeared after 5 seconds"
         print("Timer alert clicked")

     def test_confirm(self,startup):
         self.driver.get(location.Location().alert_url)
         self.driver.maximize_window()
         self.driver.implicitly_wait(10)
         confirmbtn = self.driver.find_element(by=By.XPATH, value=location.Location().confirm_box)
         self.driver.execute_script("arguments[0].scrollIntoView();", confirmbtn)
         confirmbtn.click()
         time.sleep(2)
         
         # Click on ok button
         self.driver.switch_to.alert.accept()
         result= self.driver.find_element(by=By.XPATH,value='//*[@id="confirmResult"]')
         res= result.text
         assert res == "You selected Ok"
         print ("ok button clicked")

     def test_confirm_cancel(self, startup):
         self.driver.get(location.Location().alert_url)
         self.driver.maximize_window()
         self.driver.implicitly_wait(10)
         confirmbtn = self.driver.find_element(by=By.XPATH, value=location.Location().confirm_box)
         self.driver.execute_script("arguments[0].scrollIntoView();", confirmbtn)
         confirmbtn.click()
         time.sleep(2)

         # click on cancel button
         self.driver.switch_to.alert.dismiss()
         result1 = self.driver.find_element(by=By.XPATH, value='//*[@id="confirmResult"]')
         res1=result1.text
         assert res1 == "You selected Cancel"
         print("Cancel button clicked")

     def test_prompt(self,startup):
         self.driver.get(location.Location().alert_url)
         self.driver.maximize_window()
         self.driver.implicitly_wait(10)
         promp=self.driver.find_element(by=By.XPATH,value= location.Location().prompt_box)
         self.driver.execute_script("arguments[0].scrollIntoView();", promp)
         promp.click()
         time.sleep(2)
         #enter text in prompt box and click ok
         promptbox = self.driver.switch_to.alert
         promptbox.send_keys("shahiq")
         promptbox.accept()
         time.sleep(2)
         answer= self.driver.find_element(by=By.XPATH, value= '//*[@id="promptResult"]')
         name=answer.text
         assert name == "You entered shahiq"
         print("In promptbox name entered and ok clicked")
         print("Name entered click ok ")
         #enter text in prompt box and click cancel
         #promptbox.dismiss()

