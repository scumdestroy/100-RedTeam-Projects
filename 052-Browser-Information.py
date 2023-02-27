import os
from selenium import webdriver

# Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--disable-infobars')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--log-level=3')
chrome_options.add_argument('--silent')
chrome_options.add_argument('--user-data-dir=chrome_profile')
chrome_driver = webdriver.Chrome(options=chrome_options)
chrome_driver.get('chrome://version')
chrome_version = chrome_driver.find_element_by_xpath('//td[contains(text(),"Google Chrome")]/following-sibling::td[1]').text
chrome_user_agent = chrome_driver.execute_script("return navigator.userAgent;")
print('Chrome version:', chrome_version)
print('Chrome user agent:', chrome_user_agent)

chrome_profile_dir = os.path.join(os.getcwd(), 'chrome_profile')
if not os.path.exists(chrome_profile_dir):
    os.mkdir(chrome_profile_dir)
print('Chrome profile directory:', chrome_profile_dir)

chrome_driver.quit()

# Firefox
firefox_options = webdriver.FirefoxOptions()
firefox_options.headless = True
firefox_options.set_preference("dom.webdriver.enabled", False)
firefox_options.set_preference("privacy.trackingprotection.enabled", True)
firefox_options.set_preference("privacy.trackingprotection.socialtracking.enabled", True)
firefox_options.set_preference("privacy.trackingprotection.cryptomining.enabled", True)
firefox_options.set_preference("privacy.trackingprotection.fingerprinting.enabled", True)
firefox_options.set_preference("privacy.firstparty.isolate", True)
firefox_options.set_preference("privacy.resistFingerprinting", True)
firefox_driver = webdriver.Firefox(options=firefox_options)
firefox_driver.get('about:support')
firefox_version = firefox_driver.find_element_by_xpath('//td[text()="Version"]/following-sibling::td').text
firefox_user_agent = firefox_driver.execute_script("return navigator.userAgent;")
print('Firefox version:', firefox_version)
print('Firefox user agent:', firefox_user_agent)

firefox_profile_dir = firefox_driver.capabilities['moz:profile']
print('Firefox profile directory:', firefox_profile_dir)

firefox_driver.quit()

# Edge
edge_options = webdriver.EdgeOptions()
edge_options.use_chromium = True
edge_options.add_argument('--user-data-dir=edge_profile')
edge_driver = webdriver.Edge(options=edge_options)
edge_driver.get('edge://version')
edge_version = edge_driver.find_element_by_xpath('//td[text()="Microsoft Edge"]/following-sibling::td[1]').text
edge_user_agent = edge_driver.execute_script("return navigator.userAgent;")
print('Edge version:', edge_version)
print('Edge user agent:', edge_user_agent)

edge_profile_dir = os.path.join(os.getcwd(), 'edge_profile')
if not os.path.exists(edge_profile_dir):
    os.mkdir(edge_profile_dir)
print('Edge profile directory:', edge_profile_dir)

edge_driver.quit()
