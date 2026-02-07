import allure
import pytest
from faker import Faker  # New# New# New
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.Login_Page import Login_Page_Class                ## For login
from pageObjects.Registration_Page import Registration_Page_Class  ## For Registration
from utilities.logger import log_generator_Class
from utilities.readConfig import ReadConfigClass




@pytest.mark.usefixtures("browser_setup")   # ----New
class Test_User_Profile :
    driver = None
    email = ReadConfigClass.get_data_for_email()
    password = ReadConfigClass.get_data_for_password()
    login_url = ReadConfigClass.get_data_for_login_url()
    registration_url = ReadConfigClass.get_data_for_registration_url()
    log = log_generator_Class.log_gen_method()

    ## We can customize this by using allure decorator
    @allure.title("test_verify_Credkart_url_001")   # if u want to change title only for allure report
    @allure.severity(allure.severity_level.MINOR)
    @allure.epic("Epic : User profile")
    @allure.description("This testcases is validate Credkart website title")
    @allure.link(login_url)
    @allure.issue("Title Verification")
    @allure.story("Credkart : User Page Verification")

    @pytest.mark.smoke
    @pytest.mark.flaky(reruns=1, reruns_delay = 1)
    @pytest.mark.dependency(name = "test_verify_Credkart_url_001")
    @pytest.mark.order(1)
    def test_verify_Credkart_url_001(self):

        # self.log.debug("This is debug log")
        # self.log.info("This is info log")
        # self.log.warning("This is warning log")
        # self.log.error("This is error log")
        # self.log.critical("This is critical log")
        self.log.info("TestCase test_verify_Credkart_url_001 is started")
        self.driver.get(self.login_url)
        self.log.info(f"Opening Browser and getting {self.login_url}")
        self.driver.get(self.login_url)

        self.log.info(f"Checking driver title")
        if self.driver.title == "CredKart" :
            self.log.info("TestCase test_verify_Credkart_url_001 is Passed")
            # driver.save_Screenshot(r"C:\Users\intel\04.Credkart_Pytest_Framework\Screenshots.png")
            self.log.info(f"Taking Screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_verify_Credkart_url_001_Pass.png")
            allure.attach.file(".\\Screenshots\\test_verify_Credkart_url_001_Pass.png",attachment_type=allure.attachment_type.PNG)
            print(f"driver title is {self.driver.title}")
        else:
            self.log.info("TestCase test_verify_Credkart_url_001 is Failed")
            self.log.info(f"Taking Screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_verify_Credkart_url_001_fail.png")
            allure.attach.file(".\\Screenshots\\test_verify_Credkart_url_001_fail.png",attachment_type=allure.attachment_type.PNG)
            assert False
        self.log.info("TestCase test_verify_Credkart_url_001 is Completed")

#pytest -v -s -n=auto --html=Html_Reports\my_report_24th_Jan_26.html

    ## We can customize this by using allure decorator
    @allure.title("test_Credkart_login_002")  # if u want to change title only for allure report
    @allure.severity(allure.severity_level.NORMAL)
    @allure.epic("Epic : User Login profile")
    @allure.description("This testcases is validate Credkart website Login")
    @allure.link(login_url)
    @allure.issue("Login Verification")
    @allure.story("Credkart : User Login")

    @pytest.mark.smoke
    @pytest.mark.flaky(reruns=1, reruns_delay=1)
    @pytest.mark.order(2)
    def test_Credkart_login_002(self):

        self.log.info("TestCase test_Credkart_login_002 is started")
        self.driver.get(self.login_url)
        self.log.info(f"Opening Browser and getting {self.login_url}")

        # email_id = "Credencetest@test.com"
        # pass_word = "Credence@123"
        self.lp = Login_Page_Class(self.driver) # login page class object& now we can access the methods


        # Enter Username

        # email = self.driver.find_element(By.XPATH, "//input[@id='email']")
        # email.send_keys(email_id)
        self.log.info(f"Entering the Email address {self.email}")
        self.lp.Enter_Email(self.email)

        # Enter Password
        # password = self.driver.find_element(By.XPATH, "//input[@id='password']")
        # password.send_keys(pass_word)
        self.log.info(f"Entering the Password")
        self.lp.Enter_Password(self.password)

        # Click on Login button
        # login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        # login_button.click()
        self.log.info(f"Click on the login button")
        self.lp.Click_Login_Register_Button()

        # wait = WebDriverWait(self.driver, 5)
        # try:
        #     wait.until(
        #         expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div[1]/p[1]")))
        #     element = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/p[1]")
        #     print("User Login Successful")
        #     # driver.save_screenshot(f"User Login Successful_{email_id}.png")
        #     menu = self.driver.find_element(By.XPATH, "//a[@role='button']")
        #     menu.click()
        #     logout = self.driver.find_element(By.XPATH, "//a[normalize-space()='Logout']")
        #     logout.click()
        #
        # except:
        #     print("User Login Fail")
        #     # driver.save_screenshot(f"User Login Fail_{email_id}.png")
        #     assert False, "User Login Fail"

        self.log.info(f"Checking the login status")
        if self.lp.verify_menu_button_visibility() == "pass":
            self.log.info(f"User login Successful and Taking Screenshot")
            self.driver.save_screenshot(f".\\Screenshots\\User Login Successful_{self.email}.png")
            allure.attach.file(f".\\Screenshots\\User Login Successful_{self.email}.png")   ####---
            self.log.info(f"Clicking on the Menu button")
            self.lp.Click_Menu_Button()
            self.log.info(f"Clicking on the logout button")
            self.lp.Click_Logout_Button()
        else:
            self.log.info(f"User login Failed and Taking Screenshot")
            self.driver.save_screenshot(f".\\Screenshots\\User Login Fail_{self.email}.png")
            allure.attach.file(f".\\Screenshots\\User Login Fail_{self.email}.png")     ####---
            assert False, "User Login Fail"
        self.log.info("TestCase test_Credkart_login_002 is Completed")


    ## We can customize this by using allure decorator
    @allure.title("test_Credkart_Registration_003")  # if u want to change title only for allure report
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.epic("Epic : User_Profile : User Registration")
    @allure.description("This testcases is validate Credkart website Registration")
    @allure.link(registration_url)
    @allure.issue("Registration Verification")
    @allure.story("Credkart : User Registration Verification")


    @pytest.mark.smoke
    @pytest.mark.flaky(reruns=1, reruns_delay=1)
    @pytest.mark.order(3)
    def test_Credkart_Registration_003(self):
        import time
        self.log.info("TestCase test_Credkart_Registration_003 is started")
        self.driver.get(self.registration_url)
        self.log.info(f"Opening Browser and getting {self.registration_url}")


        fake_username = Faker().user_name()  # New
        fake_email = Faker().email()  # New
        self.log.info(f"Generated the fake data for username--> {fake_username} And for email{fake_email}")
        password_data = "Credence_user_101@123"
        # print(f"fake_username--> {fake_username}")  # New
        # print(f"fake_email--> {fake_email}")  # New

        self.rp = Registration_Page_Class(self.driver)  # Registration page class object& now we can access the methods

        # Enter Username
        self.log.info(f"Entering the Username--> {fake_username}")
        self.rp.Enter_Name(fake_username)

        # Enter Email
        self.log.info(f"Entering the Email Address--> {fake_email}")
        self.rp.Enter_Email(fake_email)

        # Enter Password
        self.log.info("Entering the Password")
        self.rp.Enter_Password(password_data)

        # Enter  Confirm Password
        self.log.info("Entering the Confirm Password")
        self.rp.Enter_Confirm_Password(password_data)

        # time.sleep(2)
        # Click on register button
        self.log.info("Clicking on the Registration button")
        self.rp.Click_Login_Register_Button()

        # time.sleep(1)

        wait = WebDriverWait(self.driver, 0.5)
        self.log.info(f"Checking the Registration status")
        if self.rp.verify_menu_button_visibility() == "pass":
            self.log.info(f"User Registration Successful and Taking Screenshot")
            self.driver.save_screenshot(f".\\Screenshots\\User Registration Successful_{fake_username}.png")
            allure.attach.file(f".\\Screenshots\\User Registration Successful_{fake_username}.png") ####---
            self.log.info(f"Clicking on the Menu button")
            self.rp.Click_Menu_Button()
            self.log.info(f"Clicking on the Logout button")
            self.rp.Click_Logout_Button()
        else:
            self.log.info(f"User Registration Failed and Taking Screenshot")
            self.driver.save_screenshot(f".\\Screenshots\\User Registration Fail_{fake_username}.png")
            allure.attach.file(f".\\Screenshots\\User Registration Fail_{fake_username}.png")   ####---
            assert False, "User Login Fail"
        self.log.info("TestCase test_Credkart_Registration_003 is Completed")



