from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>Generated Test Cases</h2>
    <ul>
        <li><a href="/manual">Download Manual Test Cases</a></li>
        <li><a href="/automation">Download Automation Test Cases</a></li>
    </ul>
    """

@app.route("/manual")
def get_manual():
    return send_file("manual_test_cases.txt", as_attachment=True)

@app.route("/automation")
def get_automation():
    return send_file("automation_test_cases.py", as_attachment=True)

