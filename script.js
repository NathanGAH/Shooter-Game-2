const BASE_URL = "https://turbowarp.org/embed.html";

const playerSettings = {
  "auto-start": false,
  "addons": ["pause", "gamepad", "mute-project"].join(","),
  "settings-button": true,
  "interpolate": true,
  "fps": 60,
  "clones": "Infinity",
  "project_url": "https://raw.githubusercontent.com/nathangah/Shooter-Game-2/main/ShooterGame2.sb3"
};

const queryString = new URLSearchParams(playerSettings).toString();
document.getElementById("turbowarp-player").src = `${BASE_URL}?${queryString}`;
