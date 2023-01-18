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
        time.sleep(1)
        
        
        response_message = driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div.error-message-container.error > h3")
        self.assertEqual(response_message,"Epic sadface: Username and password do not match any user in this service")
        
    def tes_login_positif(self)
        browser = self.browser
        browser.get("https://www.saucedemo.com/")
        time.sleep(3)
        browser.find_element(By.ID,"user-name").send_keys("standard_user")
        time.sleep(3)
        browser.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click()
        time.sleep(1)
        
        
        response_message_1 = driver.find_element(By.CSS_SELECTOR,"#header_container > div.header_secondary_container > span").text
        self.assertEqual(response_message_1,"Products")                                    
        
    def tes_logout(self)
        browser = self.browser
        browser.get("https://www.saucedemo.com/")
        time.sleep(3)
        browser.find_element(By.ID,"user-name").send_keys("standard_user")
        time.sleep(3)
        browser.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click()
        time.sleep(1)
        browser.find_element(By.ID,"logout_sidebar_link").click()
        time.sleep(1)
        
        response_message_2 = driver.find_element(By.ID,"user-names").text
                                                                                          
        self.assertEqual(response_message_2,"") 
                
                                                 
unittest.main()
