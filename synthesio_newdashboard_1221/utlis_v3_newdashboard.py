import time
import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os


def openweb(firefox_profile, executable_path, url = "https://app.synthesio.com/dashboard/#home/workspace/35944/projects/dashboard"):
    driver = webdriver.Firefox(firefox_profile = firefox_profile, 
    							executable_path = executable_path)
    driver.get(url)
    time.sleep(2)
    return driver
def data_tab(driver):
	data = driver.find_element_by_xpath('/html/body/div/div/nav/div[1]/a[4]')
	data.click()
	time.sleep(2)
	return 
def login(driver, username, pw):
    #username
    login = driver.find_element_by_id('login')
    login.click()
    login.send_keys(username) #input your username here

    #password
    login = driver.find_element_by_id('password')
    login.click()
    login.send_keys(pw) #input your password here

    #log in
    LoginButton = driver.find_element_by_id('connectBtn')
    LoginButton.click()
    time.sleep(5)

    #close the pop-up message; sometimes it doesn't exist
    #PopButton = driver.find_element_by_class_name('Modal_closeButton__8C_Tm')
    #PopButton.click()
    #time.sleep(3)

    #Switch back to old dashboard
    # SwitchButton = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/button')
    # SwitchButton.click()
    # time.sleep(3)

    # driver.refresh()



def relogin(driver, username, pw):
    #username
    login = driver.find_element_by_id('login')
    login.click()
    login.send_keys(username) #input your username here

    #password
    login = driver.find_element_by_id('password')
    login.click()
    login.send_keys(pw) #input your password here

    #log in
    LoginButton = driver.find_element_by_id('connectBtn')
    LoginButton.click()
    time.sleep(5)


def selectdashboard(driver, dashboard = "XXX"): # Replace with your own dashboard name
    #step1: Check the total amount and order of dashboards we currently have
    Dashboards = []
    DashElements = driver.find_elements_by_class_name('gb-dashboard-card-title')
    Dashboards = [DashElements[i].text for i in range(len(DashElements))]

    print("We currently have ", len(Dashboards), " Dashboards: ", Dashboards)
    print("The location of the dashboard we are seeking for is: Index[", Dashboards.index(dashboard),"].")


    #step2: Enter a specific dashboard

    DashButton = driver.find_elements_by_class_name('gb-dashboard-card-title')[Dashboards.index(dashboard)]
    DashButton.click()
    time.sleep(6)


def changeiframe(driver, mode = "Default"):
    # Raise Error meesage if can not connect server in five minutes
    total_num_try = 5
    total_num_fre = 3

    num_try = 0
    num_fre = 0

    # Ensure Selenium can change the iframe
    while num_try <= total_num_try:
        print('Change iframe: Try', num_try, '. Refresh', num_fre, '.')
        num_try += 1
        try:
            if mode == "Default":
            # Change iframe
                iframe = driver.find_elements_by_tag_name('iframe')[0]
                driver.switch_to.frame(iframe)
            elif mode == "Retrieve":
                driver.switch_to.default_content()
                driver.switch_to.frame(0)

            break
        except Exception as e:
            print(e)
            time.sleep(6)

            if num_try == total_num_try:
                num_try = 0
                num_fre += 1
                driver.refresh()
                if num_fre == total_num_fre:
                    #raise Exception("Not Connected to Server!")
                    return False
    return True

def checkiframe(driver, mode = "Default"):

    if changeiframe(driver, mode = mode):

        # Raise Error meesage if can not connect server in five minutes
        total_num_try = 5
        total_num_fre = 3

        # Ensure Selenium can load the content of iframe
        num_try = 0
        num_fre = 0

        while num_try <= total_num_try:
            print('Find Indicator: Try', num_try, '. Refresh', num_fre, '.')
            num_try += 1
            try:
                # Find indicator
                ExportButton = driver.find_element_by_class_name("gb-export-btn") # indicator
                break
            except Exception as e:
                print(e)
                time.sleep(6)

                if num_try == total_num_try:
                    num_try = 0
                    num_fre += 1
                    driver.refresh()
                    time.sleep(5)
                    changeiframe(driver)
                    if num_fre == total_num_fre:
                        #raise Exception("Cannot Find Iframe!")
                        return False
        return True




def select_all_topic(driver):
    #---- Media Type ----#
    topic = driver.find_element_by_xpath('//*[@data-tracker-id="filters-button-subtopic"]')
    topic.click()
    time.sleep(2)
    # svg-inline--fa fa-square fa-w-14 Checkbox_checkbox__Lzga_

    # all_topic = driver.find_elements_by_xpath('//*[@class="svg-inline--fa fa-square fa-w-14 Checkbox_checkbox__Lzga_"]')
    all_topic = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/header/div[2]/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/header/section[2]/div[2]/div/span')
    all_topic.click()
    time.sleep(2)

def empty_click(driver):
    # breadcrumb_breadcrumb__3FyJh
    empty = driver.find_element_by_xpath('//*[@class="TopBar_topBarHeader__2orqh"]')
    empty.click()
    time.sleep(2)
    return



def select_language(driver, language_inputs):
    #---- Language ----#
    language_box =  driver.find_element_by_xpath('//*[@data-tracker-id="filters-button-language"]')
    language_box.click()
    time.sleep(2)

    try:
        for language_input in language_inputs:
            chosen_language = driver.find_element_by_xpath('//*[@title="' + language_input + '"]')
            chosen_language.click()
            time.sleep(2)
        empty_click(driver)
    except:
    	print ('Can not find this language')










def setup(Language_list, account, password, executable_path, firefox_profile, dashboard_name):
    driver = openweb(firefox_profile, executable_path)
    login(driver, account, password) #Replace with your own UserName and Paddword
    selectdashboard(driver, dashboard_name)
    # checkiframe(driver)
    #selectalltopics(driver) #uncomment if select all topics
    data_tab(driver)
    empty_click(driver)

    # selectallmedia(driver)
    #selectallcountries(driver) #uncomment if select all countries
    #selectcountry(driver)
    # selectlanguage(driver, Language_list)

    return driver

def run_interval( store_folder_path, driver,cur_year, cur_month, 
                 cur_day, cur_hour, interval_hour_len,
                 language_list = None, all_media = True ):


    timebox = driver.find_element_by_xpath('//*[@data-tracker-id="filters-button-date"]')
    timebox.click()
    time.sleep(2)

    date1 = driver.find_element_by_xpath('//*[@id="date-begin"]')
    hour1 = driver.find_elements_by_xpath('//*[@class="DatePicker_timeInput__1cNsX"]')[0]
    # hour1.clear()

    date2 = driver.find_element_by_xpath('//*[@id="date-end"]')
    hour2 = driver.find_elements_by_xpath('//*[@class="DatePicker_timeInput__1cNsX"]')[1]
    # date2.clear()
    cur_date = str(cur_year) + '/' + str(cur_month) + '/' + str(cur_day)
    if int(cur_hour) >= 10:
        cur_hour_start = str(cur_hour) + ':00'

        cur_hour_end = str(int(cur_hour) + interval_hour_len) + ':00'
    else:
        cur_hour_start = '0' + str(cur_hour) + ':00'
        if (int(cur_hour) + interval_hour_len) >= 10:
            cur_hour_end = str(int(cur_hour) + interval_hour_len) + ':00'
        else:
            cur_hour_end = '0' + str(int(cur_hour) + interval_hour_len) + ':00'
    # print (cur_hour_start, cur_hour_end)
    date1.send_keys(cur_date)
    hour1.clear()

    hour1.send_keys(cur_hour_start)
    date2.send_keys(cur_date)
    hour2.clear()
    if ( int(cur_hour) + interval_hour_len)== 24:
        cur_hour_end = '23:59'
    hour2.send_keys(cur_hour_end)
    
    empty_click(driver)
    time.sleep(2)
    
    if all_media:
        # select_all_topic(driver)
        # empty_click(driver)
        try:
            select_all_topic(driver)
            empty_click(driver)
        except:
            print ('cannot select all media')
    time.sleep(1)
 
    if language_list:
        # try:
        select_language(driver, language_list)
        empty_click(driver)
        # except:
        #     print ('cannot select language')
    time.sleep(1)
   
    try:
        span_element = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/div[1]/div/div/div[1]/div/span')
    except:
        print ('cannot find data for this time')
    if 'K' in span_element.text:
        volume = float(span_element.text.split('K')[0])
        n_volume = str(volume) + 'K' 
        if volume > 50:
            print("Date: " + cur_date + ' Hour: ' + cur_hour_start + '-' +  cur_hour_end + 
                  "    The total Volume " + str(volume) + "K is larger than the cap!")
        else:
            print("Date: " + cur_date + ' Hour: ' + cur_hour_start + '-' +  cur_hour_end + 
                   "   The total Volume is " + str(volume)+  "K Data is ready to download.")
    elif 'M' in span_element.text:
        volume = float(span_element.text.split('M')[0])
        n_volume = str(volume) + 'M'
        print("Date: " + cur_date + ' Hour: ' + cur_hour_start + '-' +  cur_hour_end + 
                  "    The total Volume " + str(volume) + "M is larger than the cap!")
    else:
        volume = float(span_element.text)
        n_volume = str(volume)
        print("Date: " + cur_date + ' Hour: ' + cur_hour_start + '-' +  cur_hour_end + 
                   "   The total Volume is " + str(volume)+  " Data is ready to download.")
    time.sleep(5)
    sett = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/header/div[1]/div/div[2]/nav/div[3]/div/button')
    sett.click()
    
    time.sleep(1)
    export_button = driver.find_element_by_xpath('//*[@data-tracker-id="toggle-export-modal"]')
    export_button.click()
 
    time.sleep(2)

    csv_choice = driver.find_elements_by_xpath("//*[contains(text(), 'CSV')]")[0]
    csv_choice.click()
    time.sleep(2)
    
    random = driver.find_element_by_xpath('//*[@title="Export a random sample up to 50,000 mentions "]')
    random.click()
    time.sleep(2)
    
    cur_len = len(os.listdir(store_folder_path))
    download_button =  driver.find_element_by_xpath('//*[@data-tracker-id="mention-modal-export-export-mention"]')
    download_button.click()

    while len(os.listdir(store_folder_path)) == cur_len:
        time.sleep(15)
    # print (len(os.listdir(store_folder_path)))
    print ('Download ready')
    return n_volume

def clear(driver):
    clear = driver.find_element_by_xpath('//*[@data-tracker-id="filters-clear-filters"]')
    clear.click()
    return 
    
    

def resetup(driver, Language_input):
    driver.get("https://app.synthesio.com/dashboard/#home/workspace/35944/projects/dashboard")
    time.sleep(10)
    try:
        relogin(driver, 'TypeinUserName', 'TypeinPassword') #Replace with your own UserName and Paddword
    #except:
        #pass
    except Exception as e:
        print(e)
    selectdashboard(driver)
    checkiframe(driver)

    # Raise Error meesage if can not connect server in five minutes
    total_num_try = 10
    total_num_fre = 3

    # Ensure Selenium can load the content of iframe
    num_try = 0
    num_fre = 0

    while num_try <= total_num_try:
        print('Find Elements: Try', num_try, '. Refresh', num_fre, '.')
        num_try += 1
        try:
            # Find element
            #selectalltopics(driver)
            selectallmedia(driver)
            #selectallcountries(driver)
            selectlanguage(driver, Language_input)
            break
        except Exception as e:
            print(e)
            time.sleep(6)

            if num_try == total_num_try:
                num_try = 0
                num_fre += 1
                driver.refresh()
                time.sleep(5)
                checkiframe(driver)
                if num_fre == total_num_fre:
                    #raise Exception("Cannot Find Iframe!")
                    return False




