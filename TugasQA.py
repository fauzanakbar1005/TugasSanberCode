import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def tes_login_failed(self):
        browser = self.browser
        browser.get("https://www.saucedemo.com/")
        time.sleep(3)
        browser.find_element(By.ID,"user-name").send_keys("email_salah")
        time.sleep(3)
        browser.find_element(By.ID,"password").send_keys("pass_salah")
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click()
        
        
        response_message = driver
        
