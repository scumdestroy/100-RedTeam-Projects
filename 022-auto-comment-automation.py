from selenium import webdriver

# init, change if you use chromium or otherwise
driver = webdriver.Firefox()

driver.get("https://www.babyboys.com")

# Will need to update here based on whether the id is "comment_box", "comment_field" or otherwise
comment_section = driver.find_element_by_id("comments")
comment_field = comment_section.find_element_by_tag_name("textarea")

comment_field.send_keys("scumdestroy wuz here xoxo")

# Find submit button and smash dat
submit_button = comment_section.find_element_by_tag_name("button")
submit_button.click()
