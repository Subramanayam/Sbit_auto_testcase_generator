import requests
from requests.auth import HTTPBasicAuth

# Store your Jira credentials and API base here
JIRA_BASE_URL = "https://your-domain.atlassian.net"
JIRA_EMAIL = "your_email.com"
JIRA_API_TOKEN = "your-api-token"


def extract_description_text(description_json):
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



def get_jira_issue(issue_id):
    url = f"{JIRA_BASE_URL}/rest/api/3/issue/{issue_id}"
    auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)
    headers = {
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers, auth=auth)

    if response.status_code == 200:
        data = response.json()
        description = extract_description_text(data['fields']['description']) if data['fields'].get(
            'description') else ""
        return {
            "summary": data['fields']['summary'],
            "description": description,
            "issue_type": data['fields']['issuetype']['name'],
            "components": [c['name'] for c in data['fields']['components']],
            "labels": data['fields']['labels']
        }
    else:
        raise Exception(f"Failed to fetch Jira issue {issue_id}: {response.status_code} - {response.text}")