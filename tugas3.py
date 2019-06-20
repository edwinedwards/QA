import unittest,time,os
from appium import webdriver
from time import sleep

class Android_Kasir_Pintar(unittest.TestCase):
	"class to run test against Kasir Pintar app"
	def setUp(self):
		"Setup for the test"
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '8.0.0'
		#desired_caps['automationName'] = 'uiautomator2'
		desired_caps['deviceName'] = 'a4f6cbcc'
		#youtube
		#desired_caps['appPackage'] = 'com.google.android.youtube'
		#desired_caps['appActivity'] = 'com.google.android.youtube.HomeActivity'

		desired_caps['appPackage'] = 'org.owline.kasirpintar'
		desired_caps['appActivity'] = 'org.owline.kasirpintar.SplashScreen'
		#desired_caps['appWaitActivity'] = 'org.owline.kasirpintar/org.owline.kasirpintar.SplashScreen'
		self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

	def tearDown(self):
		"Tear down the test"
		self.driver.quit()

	def pilih_bahasa(self):
		#pilih bahasa indonesia
		self.driver.implicitly_wait(30)
		#time.sleep(5)
		bahasa_spinner = self.driver.find_element_by_id('org.owline.kasirpintar:id/select_language')
		bahasa_spinner.click()
		bahasa_indonesia = self.driver.find_element_by_android_uiautomator('new UiSelector().text("Indonesia")')
		bahasa_indonesia.click()
		next_button = self.driver.find_element_by_id('org.owline.kasirpintar:id/fab')
		next_button.click()

	def login(self):
		#login username password
		self.driver.implicitly_wait(30)
		#time.sleep(5)
		email_text = self.driver.find_element_by_id('org.owline.kasirpintar:id/editEmail')
		email_text.send_keys('buangbuangan.1@gmail.com')
		password_text = self.driver.find_element_by_id('org.owline.kasirpintar:id/editPassword')
		password_text.send_keys('pass1234')
		login_button = self.driver.find_element_by_id('org.owline.kasirpintar:id/buttLogin')
		login_button.click()

	def isibiodata(self):
		self.driver.implicitly_wait(30)
		time.sleep(5)

	def test_kasir_pintar(self):
		#Testing kasir pintar app
		self.pilih_bahasa()
		self.login()
		self.isibiodata()


if __name__ == '__main__':
		suite = unittest.TestLoader().loadTestsFromTestCase(Android_Kasir_Pintar)
		unittest.TextTestRunner(verbosity=2).run(suite)
