from selenium import webdriver
from time import sleep
import random

class InstaBot:
    def __init__(self, username, pw):
        self.username = username
        self.pw = pw
        
    def login(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input").click()
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input").send_keys(self.username)
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input").send_keys(self.pw)
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div").click()
        print('Logging in')
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()

    def findPage(self):
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div/div/span[2]").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys("mathmatics_lover")
        print('Typed in page')
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div/div[2]/div/span").click()
        print('Clicked on page in search results')
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span").click()
        print('Clicked on followers')
        sleep(2)

    def scroll(self):
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        scrollCount = 0
        followerNum = 0
        self.driver.execute_script('arguments[0].scrollIntoView()', scroll_box)
        sleep(1)
        last_ht, ht = 0, 1
        print("while")
        while last_ht != ht:
            last_ht = ht
            sleep(2)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """, scroll_box)
            scrollCount += 1
            randomNum = int(12*random.random() + followerNum)
            print(randomNum)
            sleep(2)
            self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/ul/div/li["+str(randomNum)+"]/div/div[2]/button").click()
            randomNum += 1
            sleep (1)
            self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/ul/div/li["+str(randomNum)+"]/div/div[2]/button").click()
            randomNum += 1
            sleep (1)
            self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/ul/div/li["+str(randomNum)+"]/div/div[2]/button").click()
            followerNum += 12
bot1 = InstaBot('USERNAME', 'PASSWORD')
bot1.login()
bot1.findPage()
bot1.scroll()

