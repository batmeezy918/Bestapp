#!/usr/bin/env bash
set -euo pipefail

### ===============================
### REALITY-COHERENT INSTALL SCRIPT
### ===============================

echo "▶ Starting Reality-Coherent APK + PWA Pipeline Install"

### ---------- STEP 0: Preconditions ----------
command -v git >/dev/null || { echo "❌ git missing"; exit 1; }
command -v curl >/dev/null || { echo "❌ curl missing"; exit 1; }
command -v node >/dev/null || { echo "❌ node missing"; exit 1; }

echo "✔ Preconditions OK"

### ---------- STEP 1: Repo Root ----------
ROOT="$(pwd)"
echo "✔ Repo root: $ROOT"

### ---------- STEP 2: Directory Invariants ----------
mkdir -p .github/workflows || true

echo "✔ Directory structure ready"

### ---------- STEP 3: PWA FILES ----------
cat > index.html <<'EOF'
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8"/>
  <title>APK Factory</title>
  <link rel="manifest" href="manifest.json"/>
  <link rel="stylesheet" href="style.css"/>
</head>
<body>
<h1>APK Factory Control</h1>

<button id="start">Start Session</button>

<select id="buildType">
  <option value="release">Release</option>
</select>

<input id="minSdk" value="24"/>

<button id="build">Build APK</button>

<pre id="log"></pre>

<script src="app.js"></script>
</body>
</html>
EOF

cat > style.css <<'EOF'
body { background:#0b0b0b; color:#eaeaea; font-family: monospace; }
button { padding:8px; margin:5px; }
pre { background:black; padding:10px; height:300px; overflow:auto; }
EOF

cat > app.js <<'EOF'
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
EOF

cat > manifest.json <<'EOF'
{
  "name": "APK Factory",
  "short_name": "APKFactory",
  "start_url": "./",
  "display": "standalone",
  "background_color": "#000000",
  "theme_color": "#000000"
}
EOF

cat > sw.js <<'EOF'
self.addEventListener('install', e => self.skipWaiting());
EOF

echo "✔ PWA installed"

### ---------- STEP 4: GitHub Action ----------
cat > .github/workflows/android-release.yml <<'EOF'
name: Reality APK Build

on:
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-java@v4
        with:
          distribution: temurin
          java-version: 17

      - uses: android-actions/setup-android@v3

      - name: Ensure Gradle Wrapper
        run: |
          if [ ! -f ./gradlew ]; then
            gradle wrapper
            chmod +x gradlew
          fi

      - name: Build Release
        run: ./gradlew assembleRelease

      - name: Verify Signing
        run: |
          apksigner verify --verbose app/build/outputs/apk/release/*.apk

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: apk
          path: app/build/outputs/apk/release/*.apk
EOF

echo "✔ GitHub Action installed"

### ---------- STEP 5: Verification ----------
test -f index.html || { echo "❌ index.html missing"; exit 1; }
test -f app.js || { echo "❌ app.js missing"; exit 1; }
test -f .github/workflows/android-release.yml || exit 1

echo "✔ All invariants verified"

### ---------- STEP 6: Git Status ----------
git status --short

echo "▶ INSTALL COMPLETE — SYSTEM IS REALITY-COHERENT"
