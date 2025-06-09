from dotenv import load_dotenv
from generate_testcases import TestCaseGenerator
from web_server import TestCaseServer
import os

# Load environment variables from .env
load_dotenv()

if __name__ == '__main__':
    issue_id = "SCRUM-1"  # You can replace this or fetch from input/env

    # Prevent duplicate generation on Flask reload
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        print(f"Generating test cases for issue: {issue_id}")
        generator = TestCaseGenerator()
        generator.generate(issue_id)

    # Start Flask server
    server = TestCaseServer()
    server.run(port=5000, debug=True)
