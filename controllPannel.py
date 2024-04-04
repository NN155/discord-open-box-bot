from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tkinter
import customtkinter
import json
import time
root_tk = tkinter.Tk()
root_tk.geometry("500x500")  # Розмір вікна
root_tk.title("Discord bot")  # Назва вінка
customtkinter.set_appearance_mode("System")
def controllWindow(driver):
    def signUp():
        with open("config.json", 'r') as json_file:
            # Завантажити дані з JSON-файлу у словник
            data = json.load(json_file)
        driver.find_element(By.NAME, "email").send_keys(data["login"])
        driver.find_element(By.NAME, "password").send_keys(data["password"])
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
    def button_event_open_box():
        try:
            buttonWeb = driver.find_element(By.XPATH, '//button[contains(@class, "shinyButton")]')
            buttonWeb.click()
        except:
            pass
        try:
            element = driver.find_element(By.XPATH, "(//*[name()='svg'])[63]")
            element.click()
        except:
            pass
        try:
            element = driver.find_element(By.XPATH, "(//*[name()='svg'])[64]")
            element.click()
        except:
            pass
    def autoOpen():
        while True:
            button_event_open_box()
            time.sleep(0.5)
    button = customtkinter.CTkButton(master=root_tk,
                                     text="Open Box",
                                     command=button_event_open_box,
                                     width=120,
                                     height=32,
                                     border_width=0,
                                     corner_radius=8)
    button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    button = customtkinter.CTkButton(master=root_tk,
                                     text="Sign Up",
                                     command=signUp,
                                     width=120,
                                     height=32,
                                     border_width=0,
                                     corner_radius=8)
    button.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
    button = customtkinter.CTkButton(master=root_tk,
                                     text="Auto open",
                                     command=autoOpen,
                                     width=120,
                                     height=32,
                                     border_width=0,
                                     corner_radius=8)
    button.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
    root_tk.mainloop()




