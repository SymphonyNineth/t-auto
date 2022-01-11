from termcolor import colored
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains

errors = []

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

tumo = "https://360.am.tumo.world/site/login"
currentStudent = ""

driver.get(tumo)

login_field = driver.find_element(By.ID, "loginform-username")
password_field = driver.find_element(By.ID, "loginform-password")
submit = driver.find_element(By.ID, "login-button")
login_field.send_keys("login")
password_field.send_keys("password")
submit.click()
try:
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            By.CLASS_NAME, 'user-image')
    )
    print(colored("Authorized succesfully", "green"))

    # email = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "element_css"))).get_attribute("value")

except:
    # driver.quit()
    print(colored("Authorization error", "red"))
driver.get(currentStudent)
# try:
#     oneTime = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located(
#             By.XPATH, '//button[text()="Onetime schedule"]')
#     )
#     oneTime.click()
#     # email = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "element_css"))).get_attribute("value")

# except:
#     driver.quit()
#     print(colored("Error", "red"))


# oneTime = driver.find_element(By.XPATH, '//button[text()="Onetime schedule"]')


# try:
#     main = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "main"))
#     )

#     articles = main.find_elements(By.TAG_NAME,"article")

#     for article in articles:
#         header = article.find_element(By.CSS_SELECTOR,".entry-summary")
#         print(header.text)
# except:
#     driver.quit()
# finally:
#     time.sleep(5)
#     driver.quit()
