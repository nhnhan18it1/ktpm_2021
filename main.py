from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome("./chromedriver.exe")

web = driver.get("https://demo.openmrs.org/openmrs/login.htm")

ID = ""
Name = "Nhan Hai Nguyen"
lname = Name.split(" ")
#"TC1 - Verify User is able to login with CORRECT User Id and Password and choose Location is Inpatient Ward"
def login():
    driver.find_element_by_xpath('//*[@id="username"]').send_keys("Admin")
    driver.find_element_by_xpath('//*[@id="password"]').send_keys("Admin123")
    driver.find_element_by_xpath('//*[@id="Inpatient Ward"]').click()
    driver.find_element_by_xpath('//*[@id="loginButton"]').submit()
#"TC3-Verify User is able to login with CORRECT User Id and Password and choose Location is Inpatient Ward"
def loginFail():
    driver.find_element_by_xpath('//*[@id="username"]').send_keys("Admin")
    driver.find_element_by_xpath('//*[@id="password"]').send_keys("Admin12")
    driver.find_element_by_xpath('//*[@id="Inpatient Ward"]').click()
    driver.find_element_by_xpath('//*[@id="loginButton"]').submit()
    rs = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="error-message"]')))
    print("TC3-login-Fail",rs.text)
#TC2
def loginFail_nochoose():
    driver.find_element_by_xpath('//*[@id="username"]').send_keys("Admin")
    driver.find_element_by_xpath('//*[@id="password"]').send_keys("Admin12")
    # driver.find_element_by_xpath('//*[@id="Inpatient Ward"]').click()
    driver.find_element_by_xpath('//*[@id="loginButton"]').submit()
    rs = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="error-message"]')))
    print("TC2-login-Fail-no-choose-location",rs.text)
#TC5
def registPartient():
    home = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/ html / body / header / nav / div[1] / a')))
    driver.execute_script("arguments[0].click();", home)
    gotoregispage = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="referenceapplication-registrationapp-registerPatient-homepageLink-referenceapplication-registrationapp-registerPatient-homepageLink-extension"]'))).click()
    driver.implicitly_wait(5)
    givennameE = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div/div[3]/form/section[1]/div/fieldset[1]/div[1]/p[1]/input'))).send_keys(lname[0])

    midlenameE = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div/div[3]/form/section[1]/div/fieldset[1]/div[1]/p[2]/input')))
    midlenameE.send_keys(lname[1])
    familynameE = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[3]/form/section[1]/div/fieldset[1]/div[1]/p[3]/input')))
    familynameE.send_keys(lname[2])
    btnnextE = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="next-button"]')))
    btnnextE.click()

    selectSexE = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="gender-field"]/option[2]')))
    selectSexE.click()
    btnnextE.click()
    dayE = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="birthdateDay-field"]')))
    btnnextE.click()
    month = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="birthdateMonth-field"]/option[7]')))
    month.click()

    year = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="birthdateYear-field"]')))
    year.send_keys("2000")
    dayE.send_keys("03")
    btnnextE.click()

    address1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="address1"]')))
    address2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="address2"]')))
    city = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cityVillage"]')))
    province = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stateProvince"]')))
    country = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="country"]')))
    postcode = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="postalCode"]')))
    address1.send_keys("KTX Dai Hoc CNTT va TT Viet HAn")
    address2.send_keys("KTX Dai Hoc CNTT va TT Viet HAn")
    city.send_keys("Da Nang")
    province.send_keys("Ngu Hanh SOn")
    country.send_keys("Viet Nam")
    postcode.send_keys("50000")
    btnnextE.click()
    phone = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[3]/form/section[2]/div/fieldset[2]/p/input')))
    phone.send_keys("0339898222")
    btnnextE.click()
    relationship = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '// *[ @ id = "relationship_type"] / option[4]')))
    perName =  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="relationship"]/p[2]/input[1]')))
    relationship.click()
    perName.send_keys("abc")
    btnnextE.click()
    # givennameE.
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '// *[ @ id = "submit"]'))).click()
    ID = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '// *[ @ id = "content"] / div[6] / div[2] / div / span'))).text

    print("Page is ready!")

#TC-7 Find record by Name when that Name available.
def search_byName():
    home = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/ html / body / header / nav / div[1] / a')))
    driver.execute_script("arguments[0].click();", home)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '// *[ @ id = "coreapps-activeVisitsHomepageLink-coreapps-activeVisitsHomepageLink-extension"]'))).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/div/div[3]/div[1]/div/form/input'))).send_keys(Name)
    table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        '//*[@id="patient-search-results-table"]/tbody')))
    time.sleep(3)
    tr = table.find_element_by_xpath('// *[ @ id = "patient-search-results-table"] / tbody / tr')
    td = driver.find_element_by_xpath('// *[ @ id = "patient-search-results-table"] / tbody / tr[1] / td[1]')
    print("TC-7",td.text)
    if(td.text!="No matching records found"):
        td.click()
    else:
        print("TC-7","No record")
    # driver.find_element_by_xpath()
    pass
#TC6-Find record by ID when that ID available.
def search_byID():
    home = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/ html / body / header / nav / div[1] / a')))
    driver.execute_script("arguments[0].click();", home)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '// *[ @ id = "coreapps-activeVisitsHomepageLink-coreapps-activeVisitsHomepageLink-extension"]'))).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/div/div[3]/div[1]/div/form/input'))).send_keys('100')
    table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        '//*[@id="patient-search-results-table"]/tbody')))
    time.sleep(3)
    tr = table.find_element_by_xpath('// *[ @ id = "patient-search-results-table"] / tbody / tr')
    td = driver.find_element_by_xpath('// *[ @ id = "patient-search-results-table"] / tbody / tr[1] / td[1]')
    print("TC6-",td.text)
    if(td.text!="No matching records found"):
        td.click()
    else:
        print("No record")
    # driver.find_element_by_xpath()
    pass
#TC4
def logOut():

    el = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/header/nav/div[2]/ul/li[3]/a')))
    if el.is_displayed():
        el.click()
    else:
        driver.find_element_by_xpath('/ html / body / header / nav / button').click()
        # WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[3]/a'))).click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul/li[3]/a').click()

#TC-9 Booking an Appointment is Succesfully.
def booking():
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/ html / body / header / nav / div[1] / a'))).click()
    el = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="appointmentschedulingui-homeAppLink-appointmentschedulingui-homeAppLink-extension"]'))).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        '// *[ @ id = "appointmentschedulingui-scheduleProviders-app"]'))).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        '// *[ @ id = "calendar"] / div / div / table / tbody / tr[1] / td[1] / div'))).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        '//*[@id="select-location"]/select/option[3]'))).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        '//*[@id="select-provider"]/input'))).send_keys("abc")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        '// *[ @ id = "appointment-block-form"] / selectmultipleappointmenttypes / div / div[1] / div[2] / a'))).click()
    time.sleep(2)

    all = driver.find_element_by_xpath('// *[ @ id = "allAppointmentTypesModal"] / div[2]')
    driver.execute_script("arguments[0].click();",all)
    item = driver.find_element_by_xpath('//*[@id="allAppointmentTypesModal"]/div[2]/div[1]/a')
    driver.execute_script("arguments[0].click();", item)
    submit = driver.find_element_by_xpath('// *[ @ id = "appointment-block-form-buttons"] / button[2]')
    driver.execute_script("arguments[0].click();", submit)

if __name__ == '__main__':
    loginFail()
    loginFail_nochoose()
    login()
    booking()
    registPartient()
    search_byID()
    search_byName()
    logOut()