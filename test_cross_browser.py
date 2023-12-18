import pytest
from selenium import webdriver

# Define the list of browsers to test
browsers = ["chrome", "firefox", "safari"]

# Test case
@pytest.mark.parametrize("browser", browsers)
def test_cross_browser_compatibility(browser):
    # Initialize the WebDriver based on the specified browser
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path="C:/Users/Ms.Sanskriti/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path="c:/Users/Ms.Sanskriti/Downloads/geckodriver-v0.33.0-win64/geckodriver.exe")
    elif browser == "safari":
        driver = webdriver.Safari()

    try:
        # Navigate to the URL of your web application
        driver.get("https://your-web-application-url.com")

        # Add your test logic here (interact with elements, perform actions, etc.)

        # Example: Check the title of the page
        assert "Your Web App Title" in driver.title

    finally:
        # Close the browser window``
        driver.quit()

# Run the tests
if __name__ == "__main__":
    pytest.main(["-v", "test_cross_browser.py"])