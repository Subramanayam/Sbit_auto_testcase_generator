from jira_connector import get_jira_issue
from generate_testcases import main
from web_server import app
import os

if __name__ == '__main__':
    issue_id = "SCRUM-1"

    # Run generation only on initial start, not on reload
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        main(issue_id)

    app.run(port=5000, debug=True)

