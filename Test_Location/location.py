class Location():
    url = "https://demoqa.com/automation-practice-form"
    #xpath locator
    #forms = '//*[@id="app"]/div/div/div/div[1]/div/div/div[2]/span/div/div[2]/div[2]/svg/g/path[2]'
    #practice_form = "//*[contains(text(),'Practice Form')]"
    first_name = "//input[@id='firstName']"
    last_name = "//input[@id='lastName']"
    #id locator
    user_email = "userEmail"
    female = "gender-radio-2"
    number = "userNumber"
    dob= "dateOfBirthInput"
    #xpath locator
    month_drpdwn = "//*[@id='dateOfBirth']/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/select"
    year_drpdwn = '//*[@id="dateOfBirth"]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/select'
    date = "//*[@id='dateOfBirth']/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div[7]"
    subject = '//*[@id="subjectsContainer"]/div/div[1]'
    #id
    hobbies = "hobbies-checkbox-2"
    uploadpic="uploadPicture"
    address = "currentAddress"
    #xpath
    state_drpdwn = '//*[@id="state"]/div/div[1]/div[1]'
    city_drpdwn = '//*[@id="city"]/div/div[1]/div[1]'
    ncr = '//*[contains(text(),"NCR")]'
    delhi='//*[contains(text(),"Delhi")]'
    #id
    submit = 'submit'


    #ALERT
    alert_url = "https://demoqa.com/alerts"
    alert_btn = '//button[@id="alertButton"]'
    timer_alert = '//button[@id="timerAlertButton"]'
    confirm_box = '//button[@id="confirmButton"]'
    prompt_box = '//button[@id="promtButton"]'
    msg_display='//span[@id="confirmResult"]'


