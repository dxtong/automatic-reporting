import time
import os
import glob
import shutil
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoAlertPresentException

class WMS():
    def __init__(self, loginid, userpassword):
        self.loginid = loginid
        self.userpassword = userpassword
        self.driver = webdriver.Chrome()
        self.options = webdriver.ChromeOptions()
        self.filepath = os.path.join(os.sep, os.path.dirname(__file__),'temp')
        self.prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': self.filepath}
        self.options.add_experimental_option('prefs', self.prefs)
        self.driver = webdriver.Chrome(chrome_options=self.options)
        self.wait = WebDriverWait(self.driver, 120)

    def get_login(self):
        self.driver.maximize_window()
        self.driver.get('https://account.baozun.com/person/login?appkey=WMSHK')
        self.driver.find_element(By.ID, 'loginid').send_keys(self.loginid)
        self.driver.find_element(By.ID, 'userpassword').send_keys(self.userpassword)
        self.driver.find_element(By.ID, 'for_login_sunbmit').click()

    def get_roleCode(self, role_name):
        self.role_name = role_name
        if self.role_name == 'SwireHK':
            self.role_id = 'Swire Resources香港专用仓'
        elif self.role_name == 'NbaHK':
            self.role_id = 'NBA香港仓'
        elif self.role_name == 'NikeHK':
            self.role_id = 'NIKE倉'
        elif self.role_name == 'PumaHK':
            self.role_id = 'puma香港仓'
        elif self.role_name == 'MicrosoftHK':
            self.role_id ='MICROSOFT倉'
        elif self.role_name == 'AdidasHK':
            self.role_id = 'adidas 香港仓'
        elif self.role_name == 'ReebokHK':
            self.role_id = 'Reebok 香港仓'

    def change_role(self):
        self.wait.until(ec.visibility_of_element_located((By.ID, 'rolename'))).click()
        self.wait.until(ec.visibility_of_element_located((By.XPATH, '//td[contains(.,"'+ self.role_id +'")]'))).click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'确定')]").click()

    def get_log(self):
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get('https://scmhk.baozun.com/scm/warehouse/inventorylogquery.do')
        self.wait.until(ec.visibility_of_element_located((By.NAME, 'stock.stockStartTime1'))).send_keys(datetime.datetime.now().strftime('%Y-%m-%d 00:00:00'))
        self.wait.until(ec.visibility_of_element_located((By.NAME, 'stock.stockEndTime1'))).send_keys(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@id='query']/span").click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, '.ui-icon-comment').click()
        try:
            self.driver.switch_to.alert.dismiss()
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.switch_to_default_content()
        except NoAlertPresentException:
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.switch_to_default_content()
            time.sleep(6)
            filename = max([i for i in glob.glob('temp/'+ '*.xls')], key=os.path.getmtime)
            new_filename = datetime.datetime.now().strftime('%Y%m%d') + self.role_name + 'Log.xls'
            shutil.move(filename,os.path.join(self.filepath, new_filename))

    def get_quit(self):
        self.driver.quit()