from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import InvalidArgumentException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test_Data import data
from Test_Location import location


class demoform():
    def __init__(self,url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def form_data(self):
        #form details
        #first name
        fname = self.driver.find_element(by=By.XPATH, value=location.Location().first_name)
        self.driver.execute_script("arguments[0].scrollIntoView();",fname)
        if fname.is_displayed():
              fname.click()
              fname.send_keys(data.Data().fname)
        #last name
        self.driver.find_element(by=By.XPATH,value=location.Location().last_name).send_keys(data.Data().lname)
        #email
        self.driver.find_element(by=By.ID, value= location.Location().user_email).send_keys(data.Data().email)
        #mobile number
        self.driver.find_element(by=By.ID, value=location.Location().number).send_keys(data.Data().number_inputbox)
        #D.O.B
        self.driver.find_element(by=By.ID,value=location.Location().dob).click()
        #month and year selection
        month=WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='dateOfBirth']/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/select")))
        if month:
            mon=self.driver.find_element(by=By.XPATH,value=location.Location().month_drpdwn)
            month_dropdown = Select(mon)
            month_dropdown.select_by_visible_text("March")

        year= WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="dateOfBirth"]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/select')))
        if year:
            yearvalue = self.driver.find_element(by=By.XPATH,value=location.Location().year_drpdwn)
            year_dropdown= Select(yearvalue)
            year_dropdown.select_by_value("1998")
        dateval=WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.XPATH,"//*[@id='dateOfBirth']/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div[7]")))
        if dateval:
            dateval.click()
        #subject is not visible so we have to scroll upto state
        state=self.driver.find_element(by=By.XPATH,value=location.Location().state_drpdwn)
        self.driver.execute_script("arguments[0].scrollIntoView();",state)
        #subject
        subject_box= self.driver.find_element(by=By.XPATH,value=location.Location().subject)

        if subject_box.is_displayed():
            print("subject_inputbox is displayed")
        #hobbies
        reading=self.driver.find_element(by=By.ID,value=location.Location().hobbies)
        act=ActionChains(self.driver)
        act.click(on_element=reading).perform()

        #upload picture
        try:
           self.driver.find_element(By.ID,"uploadPicture").send_keys("C:/Users/USER/Desktop/workspace/demoqa/pic.png")
        except InvalidArgumentException as e:
            print(e)
        if self.driver.current_url != "https://demoqa.com/automation-practice-form":
              print(self.driver.title)
              self.driver.quit()
        #address
        self.driver.find_element(by=By.ID, value=location.Location().address).send_keys(data.Data().current_address)
        #state
        self.driver.find_element(by=By.XPATH, value=location.Location().state_drpdwn).click()

        ncr_state=self.driver.find_element(by=By.XPATH, value=location.Location().ncr)
        act=ActionChains(self.driver)
        act.click(on_element=ncr_state).perform()

        # city
        city=self.driver.find_element(by=By.XPATH, value=location.Location().city_drpdwn)
        city.click()
        delhi_city=self.driver.find_element(by=By.XPATH,value=location.Location().delhi)
        act = ActionChains(self.driver)
        act.click(on_element=delhi_city).perform()
        #submit
        sub = self.driver.find_element(by=By.ID,value=location.Location().submit)
        ans = sub.click()
        print("submit button is clicked")
        self.driver.get_screenshot_as_file("form_screenshot.png")

    def quit_page(self):
        self.driver.quit()


object1 = demoform(location.Location().url)
object1.form_data()
object1.quit_page()