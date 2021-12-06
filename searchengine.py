import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

youtube = input("do you want to search things on youtube? ")
if youtube == 'yes':
    #dont touch this code idk what it does but it does something important
    driver = webdriver.Chrome(executable_path=r'C:\Users\jeetd\downloads\chromedriver')
    #opens youtube and waits for it to load
    driver.get('https://www.youtube.com/')
    #finds the search bar using its html dom thing idk just click on the element and inspect it
    search_bar = driver.find_element_by_name("search_query")
    #puts stuff in search bar
    search_bar.send_keys("getting started with python")
    #clicks return
    search_bar.send_keys(Keys.RETURN)
    #print current url
    print(driver.current_url)
    #closes browser
    driver.close()
text = input('what do you want to search?  ')
#googling the input text
webbrowser.open_new_tab("https://www.google.com/search?q=" + text + "&start=")
