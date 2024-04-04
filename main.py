from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import controllPannel




driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
url = "https://discord.com/settings/lootboxes"

try:
    driver.get(url)
    controllPannel.controllWindow(driver)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()






