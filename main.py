from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep

CHROMEDRIVER_PATH='D:/Bot Twitch/chromedriver.exe' # local aonde esta o chromedriver baixado

options = webdriver.ChromeOptions()
service = ChromeService(executable_path=CHROMEDRIVER_PATH)
driver1 = webdriver.Chrome(service=service, options=options)
driver2 = webdriver.Chrome(service=service, options=options)
driver3 = webdriver.Chrome(service=service, options=options)
driver4 = webdriver.Chrome(service=service, options=options)
driver5 = webdriver.Chrome(service=service, options=options)

#Você pode aumentar ou diminuir a quantidade de abas
driver1.get("https://www.twitch.tv/nome do seu canal") # seu nome de usuario do seu canal ex: faide, (https://www.twitch.tv/faide)
driver2.get("https://www.twitch.tv/nome do seu canal")
driver3.get("https://www.twitch.tv/nome do seu canal")
driver4.get("https://www.twitch.tv/nome do seu canal")
driver5.get("https://www.twitch.tv/nome do seu canal")


while True:
    sleep(300) # Auto refresh/tempo por segundos (a cada 5 minutos ele atualiza sozinho)
    driver1.refresh()
    driver2.refresh()
    driver3.refresh()
    driver4.refresh()
    driver5.refresh()
  
  