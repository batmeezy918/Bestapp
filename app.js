cat > web/app.js <<'EOF'
const logEl = document.getElementById("log");
const startBtn = document.getElementById("start");
const stopBtn  = document.getElementById("stop");
const clearBtn = document.getElementById("clear");

let active = false;
let lastPrint = 0;
let handlerBound = false;

function write(line) {
  const ts = new Date().toISOString();
  logEl.textContent += `[${ts}] ${line}\n`;
  logEl.scrollTop = logEl.scrollHeight;
}

function onMotion(e) {
  if (!active) return;

  // Throttle prints (4 per second)
  const now = Date.now();
  if (now - lastPrint < 250) return;
  lastPrint = now;

  const a = e.accelerationIncludingGravity;
  if (!a) return;

  const x = (a.x ?? 0).toFixed(2);
  const y = (a.y ?? 0).toFixed(2);
  const z = (a.z ?? 0).toFixed(2);

  write(`Accel g: x=${x} y=${y} z=${z}`);
}

async function requestMotionPermissionIfNeeded() {
  // iOS needs explicit permission, Android usually doesn't.
  if (typeof DeviceMotionEvent !== "undefined" &&
      typeof DeviceMotionEvent.requestPermission === "function") {
    const res = await DeviceMotionEvent.requestPermission();
    if (res !== "granted") throw new Error("Motion permission denied");
  }
}

startBtn.onclick = async () => {
  if (active) return;

  try {
    await requestMotionPermissionIfNeeded();
    active = true;
    write("Sensors started");

    if (navigator.getBattery) {
      const battery = await navigator.getBattery();
      write(`Battery: ${(battery.level * 100).toFixed(0)}%`);
    } else {
      write("Battery API not available");
    }

    if (window.DeviceMotionEvent) {
      if (!handlerBound) {
        window.addEventListener("devicemotion", onMotion);
        handlerBound = true;
      }
      write("DeviceMotion listener active");
    } else {
      write("DeviceMotionEvent not supported");
    }
  } catch (err) {
    write(`ERROR: ${err.message || err}`);
  }
};

stopBtn.onclick = () => {
  if (!active) return;
  active = false;
  write("Sensors stopped");
};

clearBtn.onclick = () => {
  logEl.textContent = "";
  write("Log cleared");
};
EOF
