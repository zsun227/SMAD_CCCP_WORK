from selenium import webdriver
import selenium
import os
import requests
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import zipfile
import io
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "/Users/sunzhongkai/Downloads/chromedriver")
def build_driver():
    wd = webdriver.Chrome(executable_path=DRIVER_BIN)
    url = 'https://signin.lexisnexis.com/lnaccess/app/signin?aci=ls&back=https%3A%2F%2Fwww.lexisnexis.com%3A443%2Flawschool'
    wd.get(url)
    wd.find_element_by_id('userid').send_keys('jlukito_cccp')
    wd.find_element_by_id('password').send_keys('sjmc_cccp1')
    wd.find_element_by_id('signInSbmtBtn').submit()  # 若是表单
    return wd
link = 'https://advance.lexis.com/search/?pdmfid=1000516&crid=eec67e61-14a7-4ddd-8ee5-719a0958b37b&pdsearchterms=(%22Nancy+VanderMeer%22+OR+%22Beth+Meyers%22+OR+%22Romaine+Quinn%22+OR+%22Lisa+Subeck%22+OR+%22Dave+Considine%22+OR+%22Chuck+Wichgers%22+OR+%22Patrick+Snyder%22+OR+%22James+Edming%22+OR+%22John+Macco%22+OR+%22Treig+Pronschinske%22+OR+%22Scott+Allen%22+OR+%22Cindi+Duchow%22+OR+%22Rebecca+Bradley%22+OR+%22Annette+Ziegler%22+OR+%22Shirley+Abrahamson%22+OR+%22Patience+D.+Roggensack%22+OR+%22Patience+Roggensack%22+OR+%22Ann+Walsh+Bradley%22+OR+%22Michael+Gableman%22+OR+%22Daniel+Kelly%22+OR+%22Patrick+Crooks%22+OR+%22Louis+Butler%22+OR+%22David+Prosser%22+OR+%22Rebecaa+Dallett%22+OR+romney+OR+obama+OR+clinton+OR+trump+OR+%22Marquette+University+Law+School+poll%E2%80%9D+OR+%22Marquette+Law+School+Poll%E2%80%9D+OR+%E2%80%9CMLSP%E2%80%9D+OR+%E2%80%9CDNR%22+OR+%22Department+of+Natural+Resources%E2%80%9D+OR+%E2%80%9CDPI%22+OR+%22Department+of+Public+Instruction%E2%80%9D+OR+%E2%80%9CGAB%22+OR+%22Government+Accountability+Board%E2%80%9D+OR+%22UW+Chancellor%22+OR+%22Kevin+Reilly%22+OR+%22Ray+Cross%22+OR+%22David+Ward%22+OR+%22John+Wiley%22+OR+%22Rebecca+Blank%22+OR+%22Biddy+Martin%22+OR+%22Tommy+Thompson%22+OR+%22Mark+Miller%22+OR+%22Van+Wanggaard%22+OR+%22Louis+Molepske%22)+AND+publication(Green+Bay+Press-Gazette)&pdstartin=hlct%3A1%3A8&pdtypeofsearch=searchboxclick&pdtimeline=Jan+01%2C+2010+to+Jul+31%2C+2018%7Cbetween&pdsearchtype=SearchBox&pdqttype=or&pdpsf=date&pdquerytemplateid=&ecomp=5pfLk&earg=pdpsf&prid=1c516f0a-4c64-4ef5-97c7-d8c2ebf288d5'

wd = build_driver()
wd.get(link)
previous_count = 257
total_count = 283
filename = '_outlet_2_6_'
sleep(5)
if previous_count != 0:
    for k in range(previous_count):
        sleep(3)
        wd.refresh()
        sleep(3)
        wd.find_element_by_xpath("//a[@href='#'][@data-action='nextpage']").click()
        sleep(3)

def download(driver,filename,ind):
    dd = driver
    try:
        sleep(5)
        dd.refresh()
        dd.find_element_by_xpath("//input[@type='checkbox'][@data-action='selectall']").click()
        dd.find_element_by_xpath("//span[@class='icon la-Download']").click()
        dd.implicitly_wait(15)
        name = filename + str(ind)
        dd.implicitly_wait(15)
        dd.find_element_by_id('FileName').send_keys(name)
        dd.implicitly_wait(15)
        dd.find_element_by_xpath("//input[@type='submit'][@data-action='download']").click()
        sleep(15)
        dd.find_element_by_xpath("//a[@href='#'][@data-action='nextpage']").click()
        sleep(5)
        return dd
    except (ConnectionResetError,selenium.common.exceptions.NoSuchElementException,selenium.common.exceptions.WebDriverException):
        dd.quit()
        newd = webdriver.Chrome(executable_path=DRIVER_BIN)
        url = 'https://signin.lexisnexis.com/lnaccess/app/signin?aci=ls&back=https%3A%2F%2Fwww.lexisnexis.com%3A443%2Flawschool'
        newd.get(url)
        newd.find_element_by_id('userid').send_keys('jlukito_cccp')
        newd.find_element_by_id('password').send_keys('sjmc_cccp1')
        newd.find_element_by_id('signInSbmtBtn').submit()  # 若是表单
        newd.get(link)
        sleep(5)
        for k in range(ind):
            sleep(3)
            newd.refresh()
            sleep(3)
            newd.find_element_by_xpath("//a[@href='#'][@data-action='nextpage']").click()
            sleep(5)
        download(newd, filename, ind)
        return newd

p_driver = wd
for i in range(previous_count,total_count):
    p_driver = download(p_driver,filename,i)







