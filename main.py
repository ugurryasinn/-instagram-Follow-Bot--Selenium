from selenium import webdriver
import time
from selenium.common.exceptions import ElementClickInterceptedException

chrome_path = ""
USERNAME = ""
PASSWORD = ""
SIMILAR_ACCOUNT = ""

class InstaFollower:

	def __init__(self, driver):
		self.driver = webdriver.Chrome(executable_path=driver)

	def login(self):
		self.driver.get("https://www.instagram.com/")
		time.sleep(5)
		self.driver.find_element_by_name("username").send_keys(USERNAME)
		self.driver.find_element_by_name("password").send_keys(PASSWORD)
		self.driver.find_element_by_class_name("y3zKF").click()
		time.sleep(5)
		self.find_followers()

	def find_followers(self):
		print("find followers is working")
		search = self.driver.find_element_by_class_name("d_djL")
		search.send_keys(SIMILAR_ACCOUNT)
		time.sleep(5)
		account = self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a")
		account.click()
		time.sleep(5)
		self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a").click()
		time.sleep(2)
		self.follow()

	def follow(self):
		follow_num = 0
		print("follow is working")
		a=3
		for i in range (1,250):
			try:
				button = self.driver.find_element_by_xpath(f"/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/ul/div/li[{i}]/div/div[{a}]/button/div/div")

				button.click()
				follow_num+=1
				time.sleep(3)

			except :
				cancel_button = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]')
				cancel_button.click()
				time.sleep(2)

			if follow_num%12==0:
				a=2
				time.sleep(5)



insta_class = InstaFollower(chrome_path)
insta_class.login()
