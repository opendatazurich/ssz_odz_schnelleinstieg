/*
 * Kiosk-Modus — nur aktiv, wenn die Seite mit ?kiosk=1 aufgerufen wird.
 *
 * Im Normalbetrieb passiert hier nichts: kein Reset-Overlay, keine
 * Auswahlsperre. Für Messen und Anlässe wird die Startseite mit
 * "?kiosk=1" geöffnet; der Modus setzt sich dann über die internen Links
 * automatisch auf allen Unterseiten fort.
 *
 *   chrome.exe --kiosk --noerrdialogs "http://localhost:8080/?kiosk=1"
 */

const IDLE_TIMEOUT_MS = 3 * 60 * 1000;
let idleTimer;

function isKioskMode() {
  return new URLSearchParams(window.location.search).get('kiosk') === '1';
}

function resetIdleTimer() {
  const overlay = document.getElementById('resetOverlay');
  if (overlay && overlay.classList.contains('visible')) {
    overlay.classList.remove('visible');
  }
  clearTimeout(idleTimer);
  idleTimer = setTimeout(showResetOverlay, IDLE_TIMEOUT_MS);
}

function showResetOverlay() {
  const overlay = document.getElementById('resetOverlay');
  if (overlay) {
    overlay.classList.add('visible');
  }
}

/* Interne Links den Kiosk-Parameter mitgeben, damit der Modus beim
   Navigieren zwischen den Seiten erhalten bleibt. Externe Links,
   Anker und mailto-Links bleiben unangetastet. */
function propagateKioskParam() {
  document.querySelectorAll('a[href]').forEach(function(link) {
    const href = link.getAttribute('href');
    if (!href || /^(https?:|mailto:|#)/.test(href)) return;
    link.setAttribute('href', href + (href.includes('?') ? '&' : '?') + 'kiosk=1');
  });
}

function initKiosk() {
  document.body.classList.add('kiosk');
  propagateKioskParam();

  ['mousemove', 'mousedown', 'keydown', 'touchstart', 'scroll'].forEach(function(evt) {
    document.addEventListener(evt, resetIdleTimer);
  });

  resetIdleTimer();
}

if (isKioskMode()) {
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initKiosk);
  } else {
    initKiosk();
  }
}
