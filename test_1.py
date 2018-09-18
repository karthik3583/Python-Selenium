import BaseTest


# You can copy credentials from here:

# - Valid email : jack.sparrow@thepiratebay.se
# - Valid password : blackpearl

# - Invalid email : will.turner@gentlemen.com
# - Invalid password : savoirvivre

class LoginPageTest(BaseTest.BaseTest):

    def LoginPageTest1(self):
        login = self.driver.find_element_by_id('email-input')
        password = self.driver.find_element_by_id('password-input')
        submit = self.driver.find_element_by_id('login-button')

        self.assertTrue(login != None)
        self.assertTrue(password != None)
        self.assertTrue(submit != None)


    # example how to use the driver :
    def LoginPageTest2(self):#email and password field checking
        login = self.driver.find_element_by_id('email-input')
        password = self.driver.find_element_by_id('password-input')
        submit = self.driver.find_element_by_id('login-button')

        login.send_keys("jack.sparrow@thepiratebay.se")
        password.send_keys("blackpearl")
        submit.click()
        msg = self.driver.find_element_by_class_name('message success')
        self.assertIn("Welcome to The Pirate Bay!", msg)
        self.driver.delete_all_cookies()

    def LoginPageTest3(self):#valid login
        login = self.driver.find_element_by_id('email-input')
        password = self.driver.find_element_by_id('password-input')
        submit = self.driver.find_element_by_id('login-button')

        login.send_keys("will.turner@gentlemen.com")
        password.send_keys("savoirvivre")
        submit.click()
        msg = self.driver.find_element_by_class_name('message error')
        self.assertIn("You shall not pass! Arr!", msg)
        self.driver.delete_all_cookies()

    def LoginPageTest4(self):#invalid email
        login = self.driver.find_element_by_id('email-input')
        password = self.driver.find_element_by_id('password-input')
        submit = self.driver.find_element_by_id('login-button')

        login.send_keys("will.turner@gentlemen.com")
        password.send_keys("savoirvivre")
        submit.click()
        msg = self.driver.find_element_by_class_name('message error')
        self.assertIn("You shall not pass! Arr!", msg)
        self.driver.delete_all_cookies()

    def LoginPageTest5(self):#try to login with empty fields
        login = self.driver.find_element_by_id('email-input')
        password = self.driver.find_element_by_id('password-input')
        submit = self.driver.find_element_by_id('login-button')

        login.send_keys("")
        password.send_keys("")
        submit.click()
        msg = self.driver.find_element_by_class_name('message error')
        self.assertIn("You shall not pass! Arr!", msg)
        self.driver.delete_all_cookies()
