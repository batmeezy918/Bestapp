let session = null;
const log = m => document.getElementById("log").textContent += m + "\n";

document.getElementById("start").onclick = () => {
  session = "session-" + Date.now();
  log("Session started: " + session);
};

document.getElementById("build").onclick = () => {
  if (!session) return log("ERROR: start session first");
  log("Intent locked");
  log("Dispatch build (GitHub Actions)");
};
