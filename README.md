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


