from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.Login_Page import Login_Page_Class


class Registration_Page_Class(Login_Page_Class):

    text_name_xpath = "//input[@id='name']"

    # text_email_id = "email"                                             # already created in Loing
    # text_password_id = "password"                                       # already created in Loing

    text_confirm_password_xpath = "//input[@id='password-confirm']"

    # click_login_Register_button_Xpath = "//button[@type='submit']"      # already created in Loing
    # click_menu_button_Xpath = "//a[@role='button']"                     # already created in Loing
    # click_logout_button_Xpath = "//a[normalize-space()='Logout']"       # already created in Loing



    def Enter_Name(self,name):
        self.driver.find_element(By.XPATH, self.text_name_xpath).send_keys(name)


    def Enter_Confirm_Password(self,password):
        self.driver.find_element(By.XPATH, self.text_confirm_password_xpath).send_keys(password)




### pytest -v -s -n=auto --html=Html_Reports\my_report_24th_Jan_26.html
