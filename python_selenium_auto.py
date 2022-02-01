###########################################################
#           MADE WITH LOVE BY CRISTIAN SOARE              #
# --------------------------------------------------------#             
# PLEASE DO NOT ABUSE THE NHS LATERAL FLOW SERVICE USING  #
# THIS SOFTWARE. I AM NOT RESPONSIBLE FOR THE ACTIONS OF  #
#                        OTHERS!                          #
###########################################################

from selenium import webdriver #IMPORT WEBDRIVER
import time, warnings
import getpass
warnings.filterwarnings("ignore", category=DeprecationWarning)
print('''
      _  _____  _____ _________   ___     ____  _____ ____  ____  ______   
     / \|_   _||_   _|  _   _  |.'   `.  |_   \|_   _|_   ||   _.' ____ \  
    / _ \ | |    | | |_/ | | \_/  .-.  \   |   \ | |   | |__| | | (___ \_| 
   / ___ \| '    ' |     | |   | |   | |   | |\ \| |   |  __  |  _.____`.  
 _/ /   \ \\ \__/ /     _| |_  \  `-'  /  _| |_\   |_ _| |  | |_| \____) | 
|____| |____`.__.'     |_____|  `.___.'  |_____|\____|____||____|\______.'
\n''')
first_name = input('First name: ')  # REQUESTS DATA NEEDED FOR THE AUTOMATED DATA INPUT
last_name = input('Last name: ')
emailAddress= input('Email address (Tutanota): ')

while '@tutanota' not in emailAddress:
    emailAddress = input('Please enter a Tutanota email address: ')  # VERIFIES EMAIL SUBMITTED IS FROM THE TUTANOTA EMAIL SERVICE

emailAddressPass= getpass.getpass(prompt='Email address password (Tutanota): ') # HIDDEN PASSWORD INPUT
day= input('Day of birth (dd): ')
month= input('Month of birth (mm): ')
year= input('Year of birth (yyyy): ')
POAdd=input('Post code: ')
print('Please wait...')
driver = webdriver.Firefox(executable_path=r'./geckodriver.exe')  #SELECTS THE DRIVER WITHIN THE FOLDER
driver.implicitly_wait(30)  # IMPLICIT WAITING FOR WEB ELEMENTS TO LOAD DEPENDING ON NETWORK SPEED OF CLIENT
driver.get('https://www.gov.uk/order-coronavirus-rapid-lateral-flow-tests')
first_tab=driver.window_handles[0]  # TELLS DRIVER THIS IS THE FIRST TAB
driver.find_element_by_class_name('govuk-button--start').click()
driver.find_element_by_id('condition-2').click()
driver.find_element_by_xpath('//*[@id="main-content"]/div/div/form/button').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/main/div/div/a').click()
driver.find_element_by_id('first-name').send_keys(first_name)
driver.find_element_by_xpath('//*[@id="last-name"]').send_keys(last_name)
driver.find_element_by_xpath('//*[@id="main-content"]/div/div/form/fieldset/button').click()
driver.find_element_by_id('email-available').click()
driver.find_element_by_id('email').send_keys(emailAddress)
driver.find_element_by_id('email-confirmation').send_keys(emailAddress)
driver.find_element_by_xpath('//*[@id="main-content"]/div/div/form/button').click()
driver.find_element_by_id('mobile-available-2').click()
driver.find_element_by_xpath('//*[@id="main-content"]/div/div/form/fieldset/button').click()
driver.find_element_by_id('date-of-birth-day').send_keys(day)
driver.find_element_by_id('date-of-birth-month').send_keys(month)
driver.find_element_by_id('date-of-birth-year').send_keys(year)
driver.find_element_by_xpath('//*[@id="main-content"]/div/div/form/button').click()
driver.find_element_by_id('country').click()
driver.find_element_by_xpath('//*[@id="main-content"]/div/div/form/button').click()
driver.find_element_by_id('nhs-staff-2').click()
driver.find_element_by_xpath('//*[@id="main-content"]/div/div/form/button').click()
driver.find_element_by_xpath('//*[@id="main-content"]/div/div/button').click()
driver.find_element_by_id('submit-delivery-information').click() 
driver.find_element_by_xpath('//*[@id="postcode--62"]/input').send_keys(POAdd)
driver.find_element_by_xpath('//*[@id="submit-postcode-home"]').click()
driver.find_element_by_xpath('//*[@id="home-address-select-list"]').click()
driver.find_element_by_xpath('/html/body/div/main/div/div/div[2]/div/div/form/div/select/option[15]').click()
driver.find_element_by_xpath('//*[@id="home-address-submit"]').click()
driver.find_element_by_xpath('//*[@id="x-same-address"]').click()
driver.find_element_by_xpath('//*[@id="x-address-check-next"]').click()
driver.find_element_by_xpath('//*[@id="3-send-code"]').click() # DATA INPUT ALL ABOVE
driver.execute_script("window.open('https://mail.tutanota.com/login');") # OPENS NEW TAB USING JS
second_tab=driver.window_handles[1] # TELLS DRIVER THIS IS SECOND TAB
driver.switch_to.window(second_tab) # SWITCHES DRIVER TO SECOND TAB
driver.find_element_by_xpath('//*[@id="login-view"]/div[2]/div/div[1]/form/div[1]/div/div/div/div/div/input').send_keys(emailAddress)
driver.find_element_by_xpath('//*[@id="login-view"]/div[2]/div/div[1]/form/div[2]/div/div/div/div/div/input').send_keys(emailAddressPass)
driver.find_element_by_xpath('//*[@id="login-view"]/div[2]/div/div[1]/form/div[4]/button/div').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div/div[3]/div/div[2]/div[2]/div/div/div/ul/li[1]').click()
code = driver.find_element_by_xpath('/html/body/div/div[3]/div/div[2]/div[3]/div/div/div[2]/div/table[3]/tbody/tr[2]/td[2]/blockquote/p').text # FETCHES THE OTP FROM THE EMAIL
print('OTP code is: '+code) # PRINTS OTP FOR REFERENCE
driver.switch_to.window(first_tab) # SWITCHES DRIVER BACK TO INITIAL TAB
driver.find_element_by_xpath('//*[@id="main-content"]/div/div/h2/div/label/input').send_keys(code) # INPUTS OTP
driver.find_element_by_xpath('//*[@id="4-confirm-code"]').click()
driver.find_element_by_xpath('/html/body/div/main/div/div/div[2]/div/div/label/label/input').click()
driver.find_element_by_xpath('//*[@id="7-submit-order"]').click() # CONFIRMS AND SUBMITS
time.sleep(5)
driver.close() # CLOSES DRIVER
driver.close()

# TO REITERATE: I AM NOT RESPONSIBLE FOR WHAT PEOPLE CHOSE TO DO WITH THIS SOFTWARE. IT'S INTENDED PURPOSE WAS
# TO HELP PEOPLE WITH NO KNOWLEDGE OF TECHNOLOGY ORDER A LATERAL FLOW TEST ONLINE FROM THE GOVERNMENT SERVICE
# WITHOUT CLOGGING UP THE NHS HELPLINE.