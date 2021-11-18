from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class amazon_bot():
    def __init__(self, usernm, pswd, prod_url):
        self.usernm = usernm
        self.pswd = pswd
        self.prod_url = prod_url
        self.driver = webdriver.Safari()

    # def login_amazon():
#     driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')
#     # driver.get('https://www.amazon.com/AmazonBasics-Performance-Alkaline-Batteries-8-Pack/dp/B00O869QUC?ref_=ast_sto_dp&th=1&psc=1')

#     # input email into the field and submit
#     with open('email.txt') as f:
#         email = f.read()

#     driver.find_element(By.XPATH, '//*[@id="ap_email"]').send_keys(email, Keys.RETURN)
#     time.sleep(5)

#     # input password into field and submit
#     with open('password.txt') as f:
#         password = f.read()
    
#     driver.find_element(By.XPATH, '//*[@id="ap_password"]').send_keys(password, Keys.RETURN)

    def add_product_to_cart(self):
    # link to AAA batteries
        self.driver.get(self.prod_url)
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-button"]').click()    
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="hlb-ptc-btn-native"]').click()
        time.sleep(5)
        self.driver.close()
    
    def checkout(self):
        pass

    

