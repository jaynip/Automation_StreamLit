#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install selenium


# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# List of phone numbers (including country code)
phone_numbers = [
    "+91 ",
    "+91 "
]

# The message you want to send
message = "Hello! This is an automated message using Selenium."

# Set up the WebDriver
driver = webdriver.Chrome()  # Ensure that you have the ChromeDriver installed and in your PATH

# Open WhatsApp Web
driver.get("https://web.whatsapp.com")
input("Press ENTER after scanning the QR code")  # Wait for the user to scan the QR code

# Iterate through the phone numbers
for number in phone_numbers:
    # Open the chat for the specific contact
    url = f"https://web.whatsapp.com/send?phone={number}"
    driver.get(url)

    try:
        # Wait until the message input box is visible
        input_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true' and @data-tab='10']"))
        )

        # Send the message
        input_box.send_keys(message + Keys.ENTER)
        time.sleep(2)  # Wait for the message to send

    except Exception as e:
        print(f"Failed to send message to {number}: {str(e)}")

# Close the browser
driver.quit()


# In[ ]:




