from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import json
class Bot:
    def __init__(self):
        self.driversLst = []
        self._countDrivers = 1

    @property
    def countDrivers(self):
        return self._countDrivers

    @countDrivers.setter
    def countDrivers(self, value):
        self._countDrivers = value

    def CreateDrivers(self):
        url = "https://discord.com/settings/lootboxes"
        for i in range(self.countDrivers):
            self.driversLst.append(webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())))
        for driver in self.driversLst:
            driver.get(url)

    def LogIn(self):
        with open("config.json", 'r') as json_file:
            # Завантажити дані з JSON-файлу у словник
            data = json.load(json_file)
        for driver in self.driversLst:
            try:
                driver.find_element(By.NAME, "email").send_keys(data["login"])
                driver.find_element(By.NAME, "password").send_keys(data["password"])
            except:
                pass
            try:
                driver.find_element(By.XPATH, "//button[@type='submit']").click()
            except:
                pass
    def TryAgain(self):
        for driver in self.driversLst:
            try:
                driver.find_element(By.XPATH, "//button[@type='submit']").click()
            except:
                pass

    def OpenBox(self):
        for driver in self.driversLst:
            try:
                driver.find_element(By.XPATH, '//button[contains(@class, "shinyButton")]').click()
            except:
                pass
            try:
                driver.find_element(By.XPATH, '//*[name()="svg"][@height="1080"]').click()
            except:
                pass

    def AutoOpen(self):
        self.OpenBox()

    def End(self):
        for driver in self.driversLst:
            driver.close()
            driver.quit()
