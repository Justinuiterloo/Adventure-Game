function sendCommand() {
    const command = document.getElementById("command").value;

    fetch("/command", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ command: command }),
    })
      .then((response) => response.json())
      .then((data) => {
        typeText("\n> You said: " + command + "!\n> " + data.response);
        document.getElementById("command").value = "";
      });
  }