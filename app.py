from flask import Flask, render_template
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

app = Flask(__name__)

# URL of the main page
main_page_url = "https://megapersonals.eu/users/posts/list"

# URL of the login page
login_page_url = "https://megapersonals.eu/login"

# Set this variable to True for testing mode, False for production mode
testing_mode = True

# Function to perform the automation actions
def automate_process():
    output = ""  # Initialize the output variable
    current_page = ""  # Initialize the current_page variable

    # Set up Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Open the main page
        driver.get(main_page_url)

        # Interactive step: Bump to Top command
        if testing_mode:
            input("Press Enter to execute the Bump to Top command...")

        output += "Executing Bump to Top command...\n"

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

        output += "Executing My Posts command...\n"

        my_posts_button.click()

        # Wait for the "My Posts" page to load (adjust the timeout as needed)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "post_header")))

        # Get the current page URL
        current_page = driver.current_url

    except Exception as e:
        output += f"Error: {e}\n"

    finally:
        # Close the browser
        driver.quit()

    return output, current_page

# Route for the main page
@app.route('/')
def main_page():
    output, current_page = automate_process()
    return render_template('index.html', output=output, current_page=current_page, login_page_url=login_page_url, main_page_url=main_page_url)

if __name__ == '__main__':
    app.run(debug=True)
