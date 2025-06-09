import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

class JiraClient:
    def __init__(self):
        load_dotenv()  # Load from .env
        self.base_url = os.getenv("JIRA_BASE_URL")
        self.email = os.getenv("JIRA_EMAIL")
        self.api_token = os.getenv("JIRA_API_TOKEN")
        self.auth = HTTPBasicAuth(self.email, self.api_token)
        self.headers = {"Accept": "application/json"}

    def extract_description_text(self, description_json):
        text_parts = []

        for block in description_json.get("content", []):
            if block.get("type") == "paragraph":
                for item in block.get("content", []):
                    if item.get("type") == "text":
                        text_parts.append(item.get("text", ""))
            elif block.get("type") == "bulletList":
                for bullet in block.get("content", []):
                    for item in bullet.get("content", []):
                        if item.get("type") == "paragraph":
                            for sub_item in item.get("content", []):
                                if sub_item.get("type") == "text":
                                    text_parts.append("- " + sub_item.get("text", ""))

        return "\n".join(text_parts)

    def get_issue(self, issue_id):
        url = f"{self.base_url}/rest/api/3/issue/{issue_id}"

        response = requests.get(url, headers=self.headers, auth=self.auth)

        if response.status_code == 200:
            data = response.json()
            description = self.extract_description_text(data['fields']['description']) if data['fields'].get('description') else ""
            return {
                "summary": data['fields']['summary'],
                "description": description,
                "issue_type": data['fields']['issuetype']['name'],
                "components": [c['name'] for c in data['fields']['components']],
                "labels": data['fields']['labels']
            }
        else:
            raise Exception(f"Failed to fetch JIRA issue {issue_id}: {response.status_code} - {response.text}")