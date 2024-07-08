from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.amazon.in/')

# get cookie
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

# add cookies
cookies = {'name': 'mycookie', 'value': '1234567890'}

driver.add_cookie(cookies)
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

# delete cokkies
cookies=driver.delete_cookie('1234567890')
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)
