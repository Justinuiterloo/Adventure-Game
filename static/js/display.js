const audioElement = document.getElementById("bg-music");
audioElement.volume = 0.5; // Set volume (0.0 to 1.0)

function playSound() {
  const audioContext = new (window.AudioContext ||
    window.webkitAudioContext)();
  const oscillator = audioContext.createOscillator();
  oscillator.type = "square"; // Square wave for a classic 8-bit sound
  oscillator.frequency.setValueAtTime(440, audioContext.currentTime); // Frequency in Hz (440 is A4 pitch)

  // Optional: create a short envelope for the sound
  const gainNode = audioContext.createGain();
  gainNode.gain.setValueAtTime(1, audioContext.currentTime);
  gainNode.gain.linearRampToValueAtTime(
    0,
    audioContext.currentTime + 0.05
  ); // Fade out

  oscillator.connect(gainNode);
  gainNode.connect(audioContext.destination);

  oscillator.start();
  oscillator.stop(audioContext.currentTime + 0.05); // Duration in seconds
}

document.addEventListener("DOMContentLoaded", () => {
  fetch("/start")
    .then((response) => response.json())
    .then((data) => {
      typeText("> " + data.description);
      playSound();
    });
});

function typeText(text) {
  let i = 0;
  const output = document.getElementById("output");

  function type() {
    if (i < text.length) {
      if (text[i] === "\n") {
        output.innerHTML += "<br>";
      } else {
        output.innerHTML += text[i];
        playSound();
      }
      i++;
      setTimeout(type, 25);
      output.scrollTop = output.scrollHeight;
    }
  }

  type();
}