#!/usr/bin/env python

###############################################
# Script de prueba. Si, ya se que esta feo xD #
###############################################

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import os, time

os.system("clear")

print("[+] Iniciando Bot...")

#browser = webdriver.Firefox()
browser = webdriver.Chrome(executable_path="./chromedriver")

print("[+] Navegador Listo.")

url = "http://demo.compropago.com/version/magento/1.9.2/"

print("[+] URL: {}".format(url))

browser.get(url)

print("[+] Hecho.")

page = BeautifulSoup(browser.page_source, 'html.parser')

links = page.find('a')

product = "http://demo.compropago.com/version/magento/1.9.2/index.php/chino-straight-fit-algodon.html"

qty = "3"

print("[+] Producto: {}".format(product))
print("[+] Cantidad: {}".format(qty))

browser.get(product)

qtyElement = browser.find_element_by_id("qty")

qtyElement.send_keys(Keys.BACKSPACE)

qtyElement.send_keys(qty)

button = browser.find_element_by_css_selector(".button.btn-cart")

button.submit()

button = browser.find_element_by_css_selector(".button.btn-proceed-checkout.btn-checkout")

button.click()

button = browser.find_element_by_id("onepage-guest-register-button")

button.click()

inputName = browser.find_element_by_id("billing:firstname")

inputName.send_keys("Luis Esteban")

inputLN = browser.find_element_by_id("billing:lastname")

inputLN.send_keys("Rodríguez")

inputMail = browser.find_element_by_id("billing:email")

inputMail.send_keys("esteban@compropago.com")

inputStreet = browser.find_element_by_id("billing:street1")

inputStreet.send_keys("qetgdfah")

inputCity = browser.find_element_by_id("billing:city")

inputCity.send_keys("Mexico")

browser.find_element_by_xpath("//select[@id='billing:region_id']/option[text()='Alaska']").click()

inputCity = browser.find_element_by_id("billing:postcode")

inputCity.send_keys("39393")

browser.find_element_by_xpath("//select[@id='billing:country_id']/option[text()='Estados Unidos']").click()

inputCity = browser.find_element_by_id("billing:telephone")

inputCity.send_keys("1234567890")

browser.find_element_by_xpath("//button[@title='Continue'][@type='button']").click()

#button = browser.find_element_by_xpath("//div[@id='shipping-method-buttons-container']/button")



try:
	
	button = WebDriverWait(browser, 5).until(
    	EC.presence_of_element_located((By.XPATH, "//div[@id='shipping-method-buttons-container']"))
    )
	
except Exception as e:

	print(e)

time.sleep(1)

button.submit()

try:
	
	button = WebDriverWait(browser, 5).until(
    	EC.presence_of_element_located((By.XPATH, "//select[@id='store_code_selected']/option[@value='COPPEL']"))

    )

	button.click()
	
except Exception as e:

	print(e)

time.sleep(1)

button.submit()

try:
	
	button = WebDriverWait(browser, 5).until(
    	EC.presence_of_element_located((By.XPATH, "//div[@id='review-buttons-container']/button[@title='Place Order']"))
    )
	
except Exception as e:

	print(e)

time.sleep(1)

button.click()

time.sleep(10)
"""
if browser.find_element_by_xpath("//h3[@]"):

¡FELICITACIONES! SU PEDIDO HA SIDO GENERADO CORRECTAMENTE.

	print("[+] Compra Exitosa.")

else:

	print("[-] Algo Fallo...")
"""
input()

browser.quit()