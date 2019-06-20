import unittest
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

class cariQA(unittest.TestCase):

	def setUp(self):
		binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')
		self.browser = webdriver.Firefox()

	def test_cari_QA(self):
		browser = self.browser
		browser.get("https://kasirpintar.co.id/")
		self.assertIn("Kasir Pintar",browser.title)
		#karir_link = browser.find_elements_by_xpath("//*[text(text(), 'Karir')]")
		karir_link = browser.find_element_by_xpath("//a[.='Karir']")
		#print(karir_link.text())
		karir_link.click()
		pagekarir_url = "https://kasirpintar.co.id/careers"
		if (browser.current_url == pagekarir_url):
			posisi_textbox = browser.find_element_by_id("posisi")
			posisi_textbox.send_keys("Quality Assurance Engineer")
			divisi_dropdown = browser.find_element_by_id("divisi")
			divisi_dropdown.send_keys("Technology")
			wait = WebDriverWait(browser,15)
			cari_button = browser.find_element_by_id("cari")
			cari_button.click()
			wait = WebDriverWait(browser,15)
			

	def tearDown(self):
		self.browser.close()

if __name__ == "__main__":
	suite = unittest.TestLoader().loadTestsFromTestCase(cariQA)
	unittest.TextTestRunner(verbosity=2).run(suite)
