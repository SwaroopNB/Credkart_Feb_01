import allure
import pytest
from faker import Faker  # New# New# New
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.Login_Page import Login_Page_Class                ## For login
from pageObjects.Registration_Page import Registration_Page_Class  ## For Registration
from utilities.XLUtils import Excel_methods
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
    excel_path = ".\\Test_Data\\Credkart_Test_Data.xlsx"
    sheet_name = "login_data"

#pytest -v -s -n=auto --html=Html_Reports\my_report_24th_Jan_26.html

    ## We can customize this by using allure decorator
    @allure.title("test_Credkart_login_excel_ddt_004")  # if u want to change title only for allure report
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.epic("Epic : UserProfile : Excel ddt ")
    @allure.description("This testcases is validate Credkart website login_excel_ddt")
    @allure.link(login_url)
    @allure.issue("Excel Verification")
    @allure.story("Credkart User login_excel_ddt Verification")

    @pytest.mark.smoke
    @pytest.mark.flaky(reruns=1, reruns_delay=1)
    #@pytest.mark.dependency(depends=["test_verify_Credkart_url_001"])
    @pytest.mark.order(4)
    def test_Credkart_login_excel_ddt_004(self):

        self.log.info("TestCase test_Credkart_login_excel_ddt_004 is started")

        self.lp = Login_Page_Class(self.driver) # login page class object& now we can access the methods
        self.rows = Excel_methods.get_count_rows(self.excel_path, self.sheet_name)
        self.log.info(f"Number of rows in excel is {self.rows}")

        result_list = []
        for i in range(2,self.rows+1):
            self.driver.get(self.login_url)
            self.log.info(f"Opening Browser and getting {self.login_url}")
            self.email = Excel_methods.read_data_from_excel(self.excel_path , self.sheet_name, i ,2)
            self.password =  Excel_methods.read_data_from_excel(self.excel_path , self.sheet_name, i ,3)

            self.expected_result = Excel_methods.read_data_from_excel(self.excel_path , self.sheet_name, i ,4)

            # Enter Username
            self.log.info(f"Entering the Email address {self.email}")
            self.lp.Enter_Email(self.email)

            # Enter Password
            self.log.info(f"Entering the Password")
            self.lp.Enter_Password(self.password)

            # Click on Login button
            self.log.info(f"Click on the login button")
            self.lp.Click_Login_Register_Button()


            self.log.info(f"Checking the login status")
            if self.lp.verify_menu_button_visibility() == "pass":
                self.log.info(f"User login Successful and Taking Screenshot")
                self.driver.save_screenshot(f".\\Screenshots\\User Login Successful_{self.email}.png")
                allure.attach.file(f".\\Screenshots\\User Login Successful_{self.email}.png")   ###---
                self.log.info(f"Clicking on the Menu button")
                self.lp.Click_Menu_Button()
                self.log.info(f"Clicking on the logout button")
                self.lp.Click_Logout_Button()
                actual_result = "login_pass"
                Excel_methods.write_data_to_excel(self.excel_path, self.sheet_name, i, 5, actual_result)

            else:
                self.log.info(f"User login Failed and Taking Screenshot")
                self.driver.save_screenshot(f".\\Screenshots\\User Login Fail_{self.email}.png")
                allure.attach.file(f".\\Screenshots\\User Login Fail_{self.email}.png")   ###---
                actual_result = "login_fail"
                Excel_methods.write_data_to_excel(self.excel_path, self.sheet_name, i, 5, actual_result)

            if self.expected_result == actual_result:
                Test_Case_Status = "Pass"
                Excel_methods.write_data_to_excel(self.excel_path, self.sheet_name, i, 6, Test_Case_Status)
            else:
                Test_Case_Status = "Fail"
                Excel_methods.write_data_to_excel(self.excel_path, self.sheet_name, i, 6, Test_Case_Status)
                result_list.append(Test_Case_Status)

        if "Fail" not in result_list:
            self.log.info("All the testcases are Passed")
        else:
            self.log.info("All testcases are Failed")
            assert False

        self.log.info("TestCase test_Credkart_login_excel_ddt_004 is Completed")




