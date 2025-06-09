Sbit_auto_testcase_generator


Overview


A Python-based automation tool that generates manual and automated test cases from Jira issue descriptions using Ollama LLM and provides a simple web interface to download the generated test cases.

Features:

* Fetch Jira issue details automatically.
* Generate test cases (manual and automation) using AI prompts.
* Display a web interface to download the generated testcases.
* Easily extensible for adding more features.

Installation
Clone the repository:

git clone https://github.com/your-username/Sbit_auto_testcase_generator.git

cd Sbit_auto_testcase_generator

Install dependencies:

pip install -r requirements.txt

Windows users:

Download and install Ollama LLM for Windows.
After installation, download the recommended model:

ollama pull llama2

Configuration
Update your Jira credentials or API tokens securely (make sure NOT to commit secrets!).

Configure Ollama API client if necessary.

Usage
Run the main script to generate test cases and start the web server:
python main.py

Then open your browser at http://localhost:5000 to download the test cases.


Folder Structure
* jira_connector.py — Handles Jira API interaction.
* generate_testcases.py — Logic for test case generation.
* web_server.py — Flask web server to download test cases.
* prompts/ — Contains prompt templates for AI.
* main.py — Main entry point script.

Contributing
Feel free to open issues or submit pull requests to improve this project.


Example-

Jira ticket
![Screenshot 2025-06-09 131344](https://github.com/user-attachments/assets/7da670aa-3e7e-4de9-a0e2-0727f910b79d)



Manual Test cases

Title: Logging In and Logging Out as a Registered User

Test Case 1: Successful Logging In with Valid Email and Password

Test Steps:

1. Go to the web application's login page and enter a valid email address in the "Email" field.
2. Enter a valid password in the "Password" field.
3. Click on the "Log In" button.
4. Verify that the user is successfully logged in by checking the following:
	* The user is redirected to their dashboard after logging in.
	* The user's name is displayed in the top right corner of the page.
	* The user has access to all features and functionality on their dashboard.

Expected Result:
The user should be able to log in successfully with a valid email address and password, and be redirected to their dashboard.

Test Case 2: Failure to Log In with Invalid Email or Password

Test Steps:

1. Go to the web application's login page and enter an invalid email address in the "Email" field.
2. Enter an invalid password in the "Password" field.
3. Click on the "Log In" button.
4. Verify that the user is not logged in by checking the following:
	* The user is redirected to the login page after clicking the "Log In" button.
	* An error message indicating that the email or password is invalid is displayed.

Expected Result:
The user should not be able to log in with an invalid email address or password, and should be redirected to the login page with an error message.

Test Case 3: Successful Logging Out

Test Steps:

1. Log in to the web application using a valid email address and password.
2. Click on the "Log Out" button located in the top right corner of the page.
3. Verify that the user is logged out by checking the following:
	* The user's name is no longer displayed in the top right corner of the page.
	* The user is redirected to the login page after clicking the "Log Out" button.

Expected Result:
The user should be able to log out successfully, and be redirected to the login page after clicking the "Log Out" button.

Test Case 4: Failure to Log Out

Test Steps:

1. Log in to the web application using a valid email address and password.
2. Click on the "Log Out" button located in the top right corner of the page.
3. Verify that the user is still logged in by checking the following:
	* The user's name is still displayed in the top right corner of the page.
	* The user has access to all features and functionality on their dashboard.

Expected Result:
The user should not be able to log out successfully, and should still be logged in after clicking the "Log Out" button.



Automation Test case

Here are two Python test functions using the Selenium framework to check the main functionality of logging in and out of a web application:
```python
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Function to log in to the application
def login_to_application():
    # Create a new instance of the webdriver
    driver = webdriver.Chrome()
    
    # Navigate to the login page
    driver.get("http://www.example.com/login")
    
    # Fill in the email and password fields
    driver.find_element_by(By.NAME, "email").send_keys("myemail@example.com")
    driver.find_element_by(By.NAME, "password").send_keys("mypassword")
    
    # Click the login button
    driver.find_element_by(By.XPATH, "/html/body/form/div[2]/button").click()
    
    # Wait for the login to complete
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".logged-in")))
    
    # Close the webdriver
    driver.quit()
    
# Function to log out of the application
def log_out_of_application():
    # Create a new instance of the webdriver
    driver = webdriver.Chrome()
    
    # Navigate to the login page
    driver.get("http://www.example.com/login")
    
    # Click the log out button
    driver.find_element_by(By.XPATH, "/html/body/form/div[3]/button").click()
    
    # Wait for the log out to complete
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".logged-out")))
    
    # Close the webdriver
    driver.quit()
```
In these functions, we use the `WebDriverWait` class from the Selenium framework to wait for the login or log out process to complete before closing the webdriver. We also use the `find_element_by` method to locate and interact with the email and password fields, and the login and log out buttons on the page.

Note that you will need to have the latest version of Chrome installed on your machine in order for these tests to work. You can install the latest version of Chrome using the following command:
```
chromedriver --version
```
You will also need to have the `selenium` and ` selenium-support` packages installed in your Python environment in order to use the Selenium framework. You can install these packages using the following command:
```
pip install selenium selenium-support
```

