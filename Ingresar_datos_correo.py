from selenium import webdriver
from selenium.webdriver.common.keys import Keys # Keys to use in the keyboard
from selenium.webdriver.common.by import By
import time


driver= webdriver.Chrome(executable_path=r"D:\Descargas\chromedriver_win32\chromedriver.exe") # executable_path=  driver root
driver.get("https://www.facebook.com") # Open facebook 

usuario = driver.find_element(By.ID,"email")
usuario.send_keys("correo@hotmail.com")

time.sleep(5)

clave= driver.find_element(By.ID,"pass")
clave.send_keys("password")
clave.send_keys(Keys.ENTER)