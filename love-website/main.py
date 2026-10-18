
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI(title="A Little Surprise for Sindhu")

PHOTO_DIR = Path("photos")
PHOTO_DIR.mkdir(exist_ok=True)
app.mount("/photos", StaticFiles(directory=str(PHOTO_DIR)), name="photos")

PAGE = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>For Sindhu ❤️</title>
<style>
:root {
  --pink: #ff65b5;
  --purple: #a78bfa;
  --white: #fff7ff;
}
* { box-sizing: border-box; }
body {
  margin: 0; min-height: 100vh; overflow-x: hidden;
  font-family: 'Segoe UI', sans-serif; color: var(--white);
  background: radial-gradient(ellipse at 50% 0%, #49216d 0%, #17112f 45%, #080817 100%);
}
#stars, #effects {
  position: fixed; inset: 0; width: 100%; height: 100%;
  pointer-events: none;
}
#stars { z-index: 0; }
#effects { z-index: 5; }
main {
  position: relative; z-index: 1; min-height: 100vh;
  display: flex; flex-direction: column; align-items: center;
  justify-content: center; text-align: center; padding: 35px 18px 60px;
}
.moon {
  position: fixed; top: 8%; right: 11%; width: 70px; height: 70px;
  border-radius: 50%; background: #fff4d2;
  box-shadow: 0 0 35px #ffdfb777, 0 0 90px #a78bfa55;
  animation: moonGlow 4s ease-in-out infinite alternate;
}
@keyframes moonGlow {
  from { box-shadow: 0 0 25px #ffdfb755; }
  to { box-shadow: 0 0 65px #ffdfbbaa, 0 0 120px #a78bfa77; }
}
.eyebrow {
  color: #ffd0ee; letter-spacing: 4px; text-transform: uppercase;
  font-size: 11px; animation: fadeUp 1s both;
}
h1 {
  margin: 17px 0; font-size: clamp(45px, 10vw, 88px);
  line-height: 1.05; letter-spacing: -3px;
  background: linear-gradient(100deg, #fff, #ff91cb, #c8b5ff, #fff);
  background-size: 250%; color: transparent; background-clip: text;
  animation: shine 5s linear infinite, fadeUp 1s both;
}
@keyframes shine { to { background-position: 250% center; } }
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(25px); }
  to { opacity: 1; transform: translateY(0); }
}
.subtitle {
  max-width: 490px; color: #ded0ef; line-height: 1.9;
  font-size: 15px; animation: fadeUp 1.5s both;
}
.heart-wrap {
  margin: 28px 0 22px; cursor: pointer; user-select: none;
  animation: float 3s ease-in-out infinite;
  filter: drop-shadow(0 0 25px #ff4fa5aa);
}
.heart {
  display: inline-block; font-size: clamp(85px, 19vw, 145px);
  line-height: 1; animation: beat 1.15s ease-in-out infinite;
}
@keyframes beat {
  0%,100% { transform: scale(1); }
  15% { transform: scale(1.14); }
  30% { transform: scale(1); }
  45% { transform: scale(1.09); }
}
@keyframes float { 50% { translate: 0 -12px; } }
button {
  border: 1px solid #ffffff45; color: white; cursor: pointer;
  padding: 14px 23px; border-radius: 999px; margin: 7px;
  font-size: 14px; letter-spacing: .3px;
  background: linear-gradient(120deg, #f052a3, #8955e9);
  box-shadow: 0 5px 30px #bc52d044;
  transition: transform .25s, box-shadow .25s;
}
button:hover { transform: translateY(-3px) scale(1.04); box-shadow: 0 8px 35px #ff65b577; }
.secondary { background: #ffffff10; backdrop-filter: blur(12px); }
.glass {
  max-width: 540px; width: 100%; margin-top: 25px; padding: 23px;
  border: 1px solid #ffffff20; border-radius: 22px;
  background: #ffffff09; backdrop-filter: blur(12px);
  box-shadow: 0 10px 50px #00000020;
}
#message {
  display: none; color: #ffe0f1; line-height: 1.9;
  animation: fadeUp .8s both;
}
#message.show { display: block; }
.photo-frame {
  display: none; width: min(300px, 80vw); margin: 22px auto;
  border-radius: 20px; padding: 7px;
  border: 1px solid #ff91cb99;
  background: linear-gradient(135deg, #ff65b5, #9e83ff);
  box-shadow: 0 0 35px #ff65b544;
}
.photo-frame img { display: block; width: 100%; border-radius: 15px; }
footer { margin-top: 35px; color: #b8a7ce; font-size: 11px; letter-spacing: 2px; }
.float-item {
  position: fixed; bottom: -40px; pointer-events: none;
  animation: rise linear forwards;
}
@keyframes rise {
  to { transform: translateY(-115vh) rotate(35deg); opacity: 0; }
}
#musicNote { color: #cbb8e9; font-size: 11px; margin-top: 8px; }
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: .01ms !important; }
}
</style>
</head>
<body>
<canvas id="stars"></canvas>
<canvas id="effects"></canvas>
<div class="moon"></div>

<main>
  <div class="eyebrow">A little universe, just for you</div>
  <h1>Hey, Sindhu ✨</h1>
  <p class="subtitle">
    In a sky full of stars, some people make the whole universe
    feel a little brighter. This little corner of the internet is for you. 💗
  </p>

  <div class="heart-wrap" id="heart" title="Tap the heart">
    <span class="heart">💖</span>
  </div>
  <div style="color:#ffb9df;font-size:12px;letter-spacing:2px">
    MADE WITH A LITTLE MAGIC
  </div>

  <div>
    <button id="surprise">Open your little surprise 💌</button>
    <button class="secondary" id="hearts">Send some hearts ✨</button>
  </div>

  <section class="glass">
    <div id="message">
      <div style="font-size:28px">🌙 💗 🌷</div>
      <h2 style="color:#ffacd8">A little note for you</h2>
      <p>
        Dear Sindhu,<br>
        Some people bring happiness without even trying.
        I hope this tiny surprise brings a smile to your face.
        May your days be full of beautiful moments, your dreams
        grow bigger, and your heart always find reasons to smile.
      </p>
      <p style="font-size:20px;color:#ff9bce">You deserve all the lovely things. ❤️</p>
    </div>
    <div id="photoArea">
      <div class="photo-frame" id="photoFrame">
        <img id="friendPhoto" src="" alt="A special memory">
      </div>
      <p style="font-size:12px;color:#c8b7dc;margin-bottom:0">
        A tiny surprise made just for you ✨
      </p>
    </div>
  </section>

  <footer>ONE LITTLE PAGE · A THOUSAND LITTLE SPARKS</footer>
</main>

<script>
// Twinkling star field
const canvas = document.getElementById("stars");
const ctx = canvas.getContext("2d");
let stars = [];
function resize() {
  const dpr = Math.min(window.devicePixelRatio || 1, 2);
  canvas.width = innerWidth * dpr;
  canvas.height = innerHeight * dpr;
  canvas.style.width = innerWidth + "px";
  canvas.style.height = innerHeight + "px";
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  stars = Array.from({length: Math.min(180, Math.floor(innerWidth / 5))}, () => ({
    x: Math.random() * innerWidth,
    y: Math.random() * innerHeight,
    r: Math.random() * 1.6 + .3,
    a: Math.random(),
    speed: Math.random() * .012 + .003
  }));
}
function drawStars() {
  ctx.clearRect(0, 0, innerWidth, innerHeight);
  stars.forEach(s => {
    s.a += s.speed;
    const opacity = .25 + (Math.sin(s.a) + 1) * .35;
    ctx.beginPath();
    ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
    ctx.fillStyle = `rgba(255,225,249,${opacity})`;
    ctx.fill();
  });
  requestAnimationFrame(drawStars);
}
window.addEventListener("resize", resize);
resize();
drawStars();

// Floating hearts and sparkles
function floatHeart(x = Math.random() * innerWidth) {
  const el = document.createElement("span");
  el.className = "float-item";
  el.textContent = ["💗","💖","💕","✨","💘","🌸"][Math.floor(Math.random()*6)];
  el.style.left = x + "px";
  el.style.fontSize = (15 + Math.random()*23) + "px";
  el.style.animationDuration = (4 + Math.random()*4) + "s";
  document.body.appendChild(el);
  setTimeout(() => el.remove(), 8500);
}
const heartTimer = setInterval(() => floatHeart(), 650);

// Click burst
function burst(x, y) {
  for (let i = 0; i < 18; i++) {
    const el = document.createElement("span");
    el.className = "float-item";
    el.textContent = ["💖","✨","💕","✦"][Math.floor(Math.random()*4)];
    el.style.left = (x + (Math.random()-.5)*170) + "px";
    el.style.top = y + "px";
    el.style.bottom = "auto";
    el.style.animationDuration = (1.4 + Math.random()*1.5) + "s";
    document.body.appendChild(el);
    setTimeout(() => el.remove(), 3200);
  }
}
document.getElementById("heart").addEventListener("click", e => {
  burst(e.clientX, e.clientY);
});
document.getElementById("hearts").addEventListener("click", e => {
  burst(e.clientX || innerWidth/2, e.clientY || innerHeight/2);
  for (let i=0;i<12;i++) setTimeout(() => floatHeart(), i*90);
});
document.getElementById("surprise").addEventListener("click", () => {
  document.getElementById("message").classList.toggle("show");
  document.getElementById("surprise").textContent =
    document.getElementById("message").classList.contains("show")
    ? "Hide the note 💌" : "Open your little surprise 💌";
  if (document.getElementById("message").classList.contains("show")) {
    burst(innerWidth/2, innerHeight/2);
  }
});

// Optional personal photo: place your image at photos/sindhu.jpg
fetch("/photos/sindhu.jpg", { method: "HEAD" }).then(res => {
  if (res.ok) {
    document.getElementById("friendPhoto").src = "/photos/sindhu.jpg";
    document.getElementById("photoFrame").style.display = "block";
  }
}).catch(() => {});

</script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def home():
    return HTMLResponse(PAGE)
