from jira_connector import JiraClient
from prompt_loader import load_prompt
from ollama_client import OllamaClient

class TestCaseGenerator:
    def __init__(self):
        self.ollama = OllamaClient(model_name="llama2:7b")
        self.jira = JiraClient()

    def get_automation_prompt(self, description: str) -> str:
        return load_prompt("prompts/automation_prompt.txt", description)

    def get_manual_prompt(self, description: str) -> str:
        return load_prompt("prompts/manual_prompt.txt", description)

    def generate(self, issue_id: str):
        # Step 1: Fetch Jira issue
        issue_data = self.jira.get_issue(issue_id)
        if not issue_data:
            print(f" Could not fetch data for issue {issue_id}")
            return

        description = issue_data.get('description', '')

        # Step 2: Prepare prompts
        manual_prompt = self.get_manual_prompt(description)
        automation_prompt = self.get_automation_prompt(description)

        # Step 3: Generate test cases
        print("📝 Generating Manual Test Cases...")
        manual_test_cases = self.ollama.generate_test_cases(manual_prompt)
        print(manual_test_cases)

        print("\n Generating Automation Test Cases...")
        automation_test_cases = self.ollama.generate_test_cases(automation_prompt)
        print(automation_test_cases)

        # Step 4: Save to files
        with open("manual_test_cases.txt", "w", encoding="utf-8") as f:
            f.write(manual_test_cases)

        with open("automation_test_cases.py", "w", encoding="utf-8") as f:
            f.write(automation_test_cases)

        print("\n Test cases saved to 'manual_test_cases.txt' and 'automation_test_cases.py'")
