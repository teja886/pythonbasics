from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Path to your ChromeDriver
# Replace this with your actual path
chromedriver_path = "/path/to/chromedriver"

# Set up Chrome service
service = Service(chromedriver_path)

# Launch Chrome
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open YouTube
driver.get("https://www.youtube.com")

# Wait for 10 seconds
time.sleep(10)

# Close the browser
driver.quit()
