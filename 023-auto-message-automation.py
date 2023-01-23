from selenium import webdriver

# change browser if needed
driver = webdriver.Firefox()

driver.get("https://www.babymessageboys.com")

# change based on message field names 
message_section = driver.find_element_by_id("message_section")
to_field = message_section.find_element_by_name("to")
message_field = message_section.find_element_by_name("message")

# add your email and message
to_field.send_keys("recipient@example.com")
message_field.send_keys("?")

send_button = message_section.find_element_by_tag_name("button")
send_button.click()
