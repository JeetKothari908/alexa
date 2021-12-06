import time
from selenium import webdriver


#idk what this does, just DONT TOUCH IT
driver = webdriver.Chrome(executable_path=r'C:\Users\jeetd\downloads\chromedriver')
#opens google
driver.get('http://www.google.com/');

time.sleep(5) # Let the user actually see something!

search_box = driver.find_element_by_name('q')

search_box.send_keys('ChromeDriver')

search_box.submit()

time.sleep(5) # Let the user actually see something!

driver.quit()
