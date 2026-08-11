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

async function loadTextFile(filePath, contentId, containerId) {
  const container = document.getElementById(containerId);
  const contentEl = document.getElementById(contentId);

  try {
    const response = await fetch(filePath);
    if (!response.ok) throw new Error("File not found");

    const text = (await response.text()).trim();

    if (text.length > 0) {
      contentEl.textContent = text;
    } else {
      container.style.display = "none";
    }
  } catch (err) {
    container.style.display = "none";
  }
}

loadTextFile("instruct.txt", "instructions-content", "instructions-box");
loadTextFile("notes.txt", "notes-content", "notes-box");
