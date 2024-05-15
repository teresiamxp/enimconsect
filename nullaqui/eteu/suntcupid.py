from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Assuming 'driver' is already defined
# Replace 'your_xpath_here' with the actual XPath
xpath = "your_xpath_here"
wait = WebDriverWait(driver, 10)

try:
    # Wait until the element to be clickable
    remove_button = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    remove_button.click()
except Exception as e:
    print(f"An error occurred: {e}")
