from jira_connector import get_jira_issue
from prompt_loader import load_prompt
from ollama_client import generate_test_cases


def get_automation_prompt(description: str) -> str:
    return load_prompt("prompts/automation_prompt.txt", description)
def get_manual_prompt(description: str) -> str:
    return load_prompt("prompts/manual_prompt.txt", description)

def main(issue_id):
    # Step 1: Fetch Jira issue data
    issue_data = get_jira_issue(issue_id)
    if not issue_data:
        print(f"Could not fetch data for issue {issue_id}")
        return

    description = issue_data.get('description', '')

    # Step 2: Prepare prompts for manual and automation test cases
    manual_prompt = get_manual_prompt(description)
    automation_prompt = get_automation_prompt(description)

    # Step 3: Generate test cases using Ollama
    print("Generating Manual Test Cases...")
    manual_test_cases = generate_test_cases(manual_prompt)
    print(manual_test_cases)

    print("\nGenerating Automation Test Cases...")
    automation_test_cases = generate_test_cases(automation_prompt)
    print(automation_test_cases)

    with open("manual_test_cases.txt", "w", encoding="utf-8") as f:
        f.write(manual_test_cases)

    with open("automation_test_cases.py", "w", encoding="utf-8") as f:
        f.write(automation_test_cases)

    print("\n Test cases saved to 'manual_test_cases.txt' and 'automation_test_cases.py'")

