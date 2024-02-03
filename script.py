from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# URL of the main page
url = "https://megapersonals.eu/users/posts/list"

# Set this variable to True for testing mode, False for production mode
testing_mode = True

# Function to perform the automation actions
def automate_process():
    # Set up Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Open the main page
        driver.get(url)

        # Interactive step: Bump to Top command
        if testing_mode:
            input("Press Enter to execute the Bump to Top command...")

        # Find and click the "Bump To Top" button
        bump_button = driver.find_element_by_id("managePublishAd")
        bump_button.click()

        # Wait for the confirmation modal to appear (adjust the timeout as needed)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "success")))

        # You can add additional steps here for handling the confirmation modal if needed
        # For example, check if the modal is displayed and click "OK"

        # Navigate to "My Posts" page
        my_posts_button = driver.find_element_by_link_text("My Posts")

        # Interactive step: My Posts command
        if testing_mode:
            input("Press Enter to execute the My Posts command...")
        my_posts_button.click()

        # Wait for the "My Posts" page to load (adjust the timeout as needed)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "post_header")))

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the browser
        driver.quit()

# Main loop
while True:
    automate_process()

    # Interactive step: Wait 15 mins command
    if testing_mode:
        input("Press Enter to start the 15-minute countdown...")

    # Countdown
    for remaining_time in range(900, 0, -1):
        print(f"Time remaining: {remaining_time} seconds", end="\r")
        time.sleep(1)

    print("\nPress Enter to end/exit the sequence.")
    if testing_mode:
        input()
