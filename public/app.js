/* ══════════════════════════════════════════════════════════════
   HARAMAIN GALLERY - Stories Mode
   ══════════════════════════════════════════════════════════════ */

let placesData = {};
let translations = {};
let currentLang = localStorage.getItem('haramain_lang') || 'ar';
let currentCity = 'makkah';
let currentPlaceIndex = 0;
let currentPhotoIndex = 0;
let autoTimer = null;
let autoDelay = 5000;
let isPaused = false;

const allLangs = [
  { code: 'ar', label: 'AR', dir: 'rtl', font: 'Vazirmatn', native: 'العربية' },
  { code: 'fa', label: 'FA', dir: 'rtl', font: 'Vazirmatn', native: 'فارسی' },
  { code: 'en', label: 'EN', dir: 'ltr', font: 'Inter', native: 'English' },
  { code: 'ur', label: 'UR', dir: 'rtl', font: 'Vazirmatn', native: 'اردو' },
  { code: 'id', label: 'ID', dir: 'ltr', font: 'Inter', native: 'Indonesia' },
  { code: 'bn', label: 'বা', dir: 'ltr', font: 'Noto Sans Bengali', native: 'বাংলা' },
  { code: 'tr', label: 'TR', dir: 'ltr', font: 'Inter', native: 'Türkçe' },
  { code: 'ms', label: 'MS', dir: 'ltr', font: 'Inter', native: 'Melayu' },
  { code: 'fr', label: 'FR', dir: 'ltr', font: 'Inter', native: 'Français' },
  { code: 'sw', label: 'SW', dir: 'ltr', font: 'Inter', native: 'Kiswahili' },
  { code: 'ha', label: 'HA', dir: 'ltr', font: 'Inter', native: 'Hausa' },
  { code: 'ps', label: 'PS', dir: 'rtl', font: 'Vazirmatn', native: 'پښتو' },
  { code: 'uz', label: 'UZ', dir: 'ltr', font: 'Inter', native: "O'zbek" },
  { code: 'ru', label: 'RU', dir: 'ltr', font: 'Inter', native: 'Русский' },
  { code: 'zh', label: '中', dir: 'ltr', font: 'Noto Sans SC', native: '中文' },
  { code: 'az', label: 'AZ', dir: 'ltr', font: 'Inter', native: 'Azərbaycan' },
  { code: 'ku', label: 'KU', dir: 'ltr', font: 'Inter', native: 'Kurdî' },
  { code: 'so', label: 'SO', dir: 'ltr', font: 'Inter', native: 'Soomaali' },
  { code: 'bs', label: 'BS', dir: 'ltr', font: 'Inter', native: 'Bosanski' },
  { code: 'tg', label: 'ТЈ', dir: 'ltr', font: 'Inter', native: 'Тоҷикӣ' }
];

/* ═══════ INIT ═══════ */
async function init() {
  try {
    const placesRes = await fetch('/data/places.json');
    placesData = await placesRes.json();
    await loadLang(currentLang);
    setupListeners();
    createTooltip();
    setFont();
    renderSlide();
  } catch (e) {
    console.error('Init error:', e);
  }
}

async function loadLang(code) {
  try {
    const res = await fetch(`/lang/${code}.json`);
    if (!res.ok) throw new Error(`Lang ${code} not found`);
    translations[code] = await res.json();
  } catch (e) {
    console.error(`Failed to load lang ${code}:`, e);
  }
}

/* ═══════ FONT ═══════ */
function setFont() {
  const fontMap = {
    ar: 'Vazirmatn', fa: 'Vazirmatn', ur: 'Vazirmatn', ps: 'Vazirmatn',
    bn: 'Noto Sans Bengali', zh: 'Noto Sans SC',
    en: 'Inter', id: 'Inter', tr: 'Inter', ms: 'Inter', fr: 'Inter',
    sw: 'Inter', ha: 'Inter', uz: 'Inter', ru: 'Inter', az: 'Inter',
    ku: 'Inter', so: 'Inter', bs: 'Inter', tg: 'Inter'
  };
  const font = fontMap[currentLang] || 'Inter';
  document.documentElement.style.setProperty('--page-font', `'${font}', sans-serif`);
  document.body.setAttribute('data-lang', currentLang);
}

/* ═══════ PLACES HELPERS ═══════ */
function getPlaces() {
  return placesData[currentCity] || [];
}

function getCurrentPlace() {
  return getPlaces()[currentPlaceIndex];
}

function getTranslation() {
  const lang = translations[currentLang];
  const place = getCurrentPlace();
  if (!lang || !place) return null;
  return lang.places[place.id] || null;
}

function getPhotoCount() {
  const place = getCurrentPlace();
  return place ? place.images.length : 0;
}

/* ═══════ RENDER SLIDE ═══════ */
function renderSlide() {
  const place = getCurrentPlace();
  const info = getTranslation();
  if (!place || !info) return;

  clearAutoTimer();

  const viewport = document.getElementById('stories-viewport');
  viewport.innerHTML = '';

  const slide = document.createElement('div');
  slide.className = 'story-slide active';
  slide.innerHTML = `<img src="${place.images[currentPhotoIndex]}" alt="${info.title}" draggable="false">`;
  viewport.appendChild(slide);

  document.getElementById('story-title').textContent = info.title;
  document.getElementById('story-short').textContent = info.short;

  document.getElementById('modal-title').textContent = info.title;
  document.getElementById('modal-description').innerHTML = info.full
    .split('\n\n')
    .filter(p => p.trim())
    .map(p => `<p>${p.trim()}</p>`)
    .join('');

  renderProgress();
  renderDots();
  renderCityLabels();
  startAutoTimer();
}

/* ═══════ PROGRESS BARS ═══════ */
function renderProgress() {
  const bar = document.getElementById('progress-bar');
  const count = getPhotoCount();
  bar.innerHTML = '';

  for (let i = 0; i < count; i++) {
    const seg = document.createElement('div');
    seg.className = 'progress-segment';
    const fill = document.createElement('div');
    fill.className = 'progress-fill';

    if (i < currentPhotoIndex) {
      fill.classList.add('done');
    } else if (i === currentPhotoIndex) {
      fill.classList.add('active');
    }

    seg.appendChild(fill);
    bar.appendChild(seg);
  }
}

/* ═══════ CITY LABELS ═══════ */
function renderCityLabels() {
  const lang = translations[currentLang];
  if (!lang || !lang.ui) return;
  document.getElementById('btn-makkah').textContent = lang.ui.makkah_label || 'مكة المكرمة';
  document.getElementById('btn-madinah').textContent = lang.ui.madinah_label || 'المدينة المنورة';
}

/* ═══════ STORY DOTS ═══════ */
function renderDots() {
  const dots = document.getElementById('story-dots');
  const places = getPlaces();
  dots.innerHTML = '';

  places.forEach((_, i) => {
    const dot = document.createElement('div');
    dot.className = `dot ${i === currentPlaceIndex ? 'active' : ''}`;
    dot.addEventListener('click', () => goToPlace(i));
    dots.appendChild(dot);
  });
}

/* ═══════ NAVIGATION ═══════ */
function nextPhoto() {
  const count = getPhotoCount();
  if (currentPhotoIndex < count - 1) {
    currentPhotoIndex++;
    renderSlide();
  } else {
    nextPlace();
  }
}

function prevPhoto() {
  if (currentPhotoIndex > 0) {
    currentPhotoIndex--;
    renderSlide();
  }
}

function nextPlace() {
  const places = getPlaces();
  if (currentPlaceIndex < places.length - 1) {
    currentPlaceIndex++;
    currentPhotoIndex = 0;
    renderSlide();
  }
}

function prevPlace() {
  if (currentPlaceIndex > 0) {
    currentPlaceIndex--;
    currentPhotoIndex = 0;
    renderSlide();
  }
}

function goToPlace(index) {
  currentPlaceIndex = index;
  currentPhotoIndex = 0;
  renderSlide();
}

/* ═══════ AUTO TIMER ═══════ */
function startAutoTimer() {
  clearAutoTimer();
  autoTimer = setTimeout(() => {
    if (!isPaused) nextPhoto();
  }, autoDelay);
}

function clearAutoTimer() {
  if (autoTimer) {
    clearTimeout(autoTimer);
    autoTimer = null;
  }
}

function pauseAuto() {
  isPaused = true;
  clearAutoTimer();
  const activeFill = document.querySelector('.progress-fill.active');
  if (activeFill) activeFill.style.animationPlayState = 'paused';
}

function resumeAuto() {
  isPaused = false;
  const activeFill = document.querySelector('.progress-fill.active');
  if (activeFill) {
    activeFill.style.animationPlayState = 'running';
    const computed = getComputedStyle(activeFill);
    const matrix = computed.transform;
    let currentScale = 0;
    if (matrix && matrix !== 'none') {
      const values = matrix.split('(')[1]?.split(')')[0]?.split(',');
      if (values) currentScale = parseFloat(values[0]) || 0;
    }
    const remaining = (1 - currentScale) * autoDelay;
    autoTimer = setTimeout(() => {
      if (!isPaused) nextPhoto();
    }, Math.max(remaining, 500));
  } else {
    startAutoTimer();
  }
}

/* ═══════ TOUCH HANDLING ═══════ */
function setupTouchHandlers() {
  const viewport = document.getElementById('stories-viewport');
  let startX = 0, startY = 0, startTime = 0;
  let dx = 0, dy = 0;
  let isDragging = false;

  viewport.addEventListener('touchstart', (e) => {
    startX = e.touches[0].clientX;
    startY = e.touches[0].clientY;
    startTime = Date.now();
    isDragging = true;
    dx = 0;
    dy = 0;
    pauseAuto();
  }, { passive: true });

  viewport.addEventListener('touchmove', (e) => {
    if (!isDragging) return;
    dx = e.touches[0].clientX - startX;
    dy = e.touches[0].clientY - startY;
  }, { passive: true });

  viewport.addEventListener('touchend', () => {
    if (!isDragging) return;
    isDragging = false;

    const absDx = Math.abs(dx);
    const absDy = Math.abs(dy);
    const elapsed = Date.now() - startTime;
    const velocity = Math.max(absDx, absDy) / elapsed;

    const threshold = velocity > 0.5 ? 20 : 60;

    if (absDx > absDy && absDx > threshold) {
      if (dx < 0) {
        nextPlace();
      } else {
        prevPlace();
      }
    } else if (absDy > absDx && absDy > threshold) {
      if (dy < 0) {
        nextPhoto();
      } else {
        if (document.getElementById('desc-panel').classList.contains('active')) {
          closeDesc();
        } else {
          prevPhoto();
        }
      }
    } else {
      const vw = window.innerWidth;
      if (startX > vw * 0.6) {
        nextPhoto();
      } else if (startX < vw * 0.4) {
        prevPhoto();
      } else {
        nextPhoto();
      }
    }

    resumeAuto();
  }, { passive: true });
}

/* ═══════ DESCRIPTION PANEL ═══════ */
function openDesc() {
  document.getElementById('desc-panel').classList.add('active');
  pauseAuto();
}

function closeDesc() {
  document.getElementById('desc-panel').classList.remove('active');
  resumeAuto();
}

/* ═══════ CITY SWITCH ═══════ */
function switchCity(city) {
  currentCity = city;
  currentPlaceIndex = 0;
  currentPhotoIndex = 0;

  document.getElementById('btn-makkah').classList.toggle('active', city === 'makkah');
  document.getElementById('btn-madinah').classList.toggle('active', city === 'madinah');

  renderSlide();
}

/* ═══════ LANGUAGE ═══════ */
function syncLangSidebar() {
  document.querySelectorAll('.lang-item').forEach(el => {
    el.classList.toggle('active', el.dataset.lang === currentLang);
  });
}

/* ═══════ TOOLTIP ═══════ */
let tooltipEl = null;

function createTooltip() {
  tooltipEl = document.createElement('div');
  tooltipEl.className = 'lang-tooltip';
  document.body.appendChild(tooltipEl);
}

function showTooltip(langItem) {
  const lang = allLangs.find(l => l.code === langItem.dataset.lang);
  if (!lang || !tooltipEl) return;
  tooltipEl.textContent = lang.native;
  tooltipEl.style.fontFamily = `'${lang.font}', sans-serif`;
  const rect = langItem.getBoundingClientRect();
  tooltipEl.style.top = (rect.top + rect.height / 2 - 16) + 'px';
  tooltipEl.style.right = 'auto';
  tooltipEl.style.left = (rect.left - tooltipEl.offsetWidth - 8) + 'px';
  tooltipEl.classList.add('show');
}

function hideTooltip() {
  if (tooltipEl) tooltipEl.classList.remove('show');
}

/* ═══════ LISTENERS ═══════ */
function setupListeners() {
  setupTouchHandlers();

  document.getElementById('btn-makkah').addEventListener('click', () => switchCity('makkah'));
  document.getElementById('btn-madinah').addEventListener('click', () => switchCity('madinah'));

  document.getElementById('info-btn').addEventListener('click', (e) => {
    e.stopPropagation();
    openDesc();
  });

  document.getElementById('close-desc').addEventListener('click', (e) => {
    e.stopPropagation();
    closeDesc();
  });

  document.getElementById('desc-panel').addEventListener('touchstart', (e) => {
    e.stopPropagation();
  }, { passive: true });

  const changeLangBtn = document.getElementById('change-lang-btn');
  if (changeLangBtn) {
    changeLangBtn.addEventListener('click', () => {
      localStorage.removeItem('haramain_lang');
      localStorage.removeItem('haramain_dir');
      window.location.href = '/';
    });
  }

}

/* ═══════ START ═══════ */
window.addEventListener('DOMContentLoaded', () => {
  syncLangSidebar();
  init();
});
