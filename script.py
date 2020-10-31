from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("https://www.tumblr.com/")
        driver.find_element_by_xpath("//button[@id='signup_login_button']/span").click()
        driver.find_element_by_id("signup_determine_email").click()
        driver.find_element_by_id("signup_determine_email").clear()
        # Email here!
        driver.find_element_by_id("signup_determine_email").send_keys("email@email.com")
        driver.find_element_by_xpath("//button[@id='signup_forms_submit']/span[2]").click()
        driver.find_element_by_link_text(u"Use sua senha para iniciar a sessão").click()
        time.sleep(1)
        driver.find_element_by_id("signup_password").clear()
        # Password here!
        driver.find_element_by_id("signup_password").send_keys("password")
        time.sleep(3)       
        driver.find_element_by_xpath("//button[@id='signup_forms_submit']/span[6]").click()
        # Blog here!
        driver.get("https://www.tumblr.com/blog/bloghere/followers")
        print("loop to remove")
        while True:
            # Blog here!
            driver.get("https://www.tumblr.com/blog/bloghere/followers")
            time.sleep(2)
            driver.find_element_by_css_selector("span.Jnotm > svg").click()
            driver.find_element_by_xpath("//div[@id='base-container']/div/div[2]/div/main/section/div/div[2]/div/span/div/div/div/button").click()
            driver.find_element_by_xpath("//div[@id='glass-container']/div/div[2]/div[2]/button[2]/span").click()
            time.sleep(2)

if __name__ == "__main__":
    unittest.main()
