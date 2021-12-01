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

    def login_amazon(self):
        """Logs into your Amazon account.
        """
        #login to Amazon account with email/passwrd
        # print(f'Login: {self.driver.session_id}')
        self.driver.find_element(By.XPATH, '//*[@id="ap_email"]').send_keys(self.usernm, Keys.RETURN)
        time.sleep(4)
        self.driver.find_element(By.XPATH, '//*[@id="ap_password"]').send_keys(self.pswd, Keys.RETURN)
        # had to increase wait time because it asks for approval now....they're on to me
        time.sleep(10)

    def add_product_to_cart(self):
        """Adds a product to your cart based on the url you input. Clicks the add to cart and checkout buttons.
        """
        # add some error handling for different product links
        # print(f'Add product to cart: {self.driver.session_id}')
        self.driver.get(self.prod_url)
        try:
            if self.driver.find_element(By.XPATH, '//*[@id="newAccordionCaption_feature_div"]/div').is_enabled():
                self.driver.find_element(By.XPATH, '//*[@id="newAccordionRow"]/div/div[1]/a').click()
                time.sleep(6)
                self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-button"]').click()    
                time.sleep(4)
                self.driver.find_element(By.XPATH, '//*[@id="hlb-ptc-btn-native"]').click()
                time.sleep(4)
            else:
                self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-button"]').click()    
                time.sleep(4)
                self.driver.find_element(By.XPATH, '//*[@id="hlb-ptc-btn-native"]').click()
                time.sleep(4)
        except:
            self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-button"]').click()    
            time.sleep(4)
            self.driver.find_element(By.XPATH, '//*[@id="hlb-ptc-btn-native"]').click()
            time.sleep(4)

    # if you want to actually buy something then replace the print statement with .click() on the same 
    # XPATH as the conditional statement.
    def checkout(self):
        """Checks to see if the place order button can be clicked (if the bot was successful)
        """
        # print(f'Checkout: {self.driver.session_id}')
        if self.driver.find_element(By.XPATH, '//*[@id="placeYourOrder"]/span/input').is_enabled():
            print("Order was able to be purchased....but was not purchased in order to save your wallet!")

    def shipping(self):
        """Selects the default shipping methood from the list on the amazon checkout page.
        """
        # click the button to change shipping address, click the default address
        # print(f'Shipping: {self.driver.session_id}')
        self.driver.find_element(By.XPATH, '//*[@id="spc-top"]/div/div[1]/div[1]/div[1]/span/a').click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, '//*[@id="shipping-address-popover"]/div[1]/div[2]/div/div[2]/div[3]/span[1]/span/a').click()
        time.sleep(4)

    def payment(self):
        """Selects the default payment methood from the list of payments on the amazon checkout page.
        """
        # print(f'Payment: {self.driver.session_id}')
        # click the change payment button
        self.driver.find_element(By.XPATH, '//*[@id="payment-change-link"]').click()
        time.sleep(4)

        # check the default card payment option, if it already selected then press continue, this will remove the use of gift cards
        if not self.driver.find_element(By.XPATH, '//*[@id="pp-pJ7Tjx-69"]').is_selected():
            self.driver.find_element(By.XPATH, '//*[@id="pp-pJ7Tjx-69"]').click()
        else:
            self.driver.find_element(By.XPATH, '//*[@id="pp-pJ7Tjx-91"]/span/input').click()
            time.sleep(4)

    def close_session(self):
        """Quits the current webdriver session
        """
        # print(f'Close session: {self.driver.session_id}')
        time.sleep(5)
        self.driver.quit()
        
    def get_url(self):
        """This function is a getter function to return the current url of the webdriver

        Returns:
            String: current webdriver url
        """
        return self.driver.current_url