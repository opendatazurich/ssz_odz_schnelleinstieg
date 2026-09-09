const IDLE_TIMEOUT_MS = 3 * 60 * 1000;
let idleTimer;

function resetIdleTimer() {
  const overlay = document.getElementById('resetOverlay');
  if (overlay.classList.contains('visible')) {
    overlay.classList.remove('visible');
  }
  clearTimeout(idleTimer);
  idleTimer = setTimeout(showResetOverlay, IDLE_TIMEOUT_MS);
}

function showResetOverlay() {
  document.getElementById('resetOverlay').classList.add('visible');
}

document.addEventListener('mousemove', resetIdleTimer);
document.addEventListener('mousedown', resetIdleTimer);
document.addEventListener('keydown', resetIdleTimer);
document.addEventListener('touchstart', resetIdleTimer);
document.addEventListener('scroll', resetIdleTimer);

resetIdleTimer();
