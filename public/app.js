/* ══════════════════════════════════════════════════════════════
   HARAMAIN GALLERY - Core Logic
   ══════════════════════════════════════════════════════════════ */

let placesData = {};
let translations = {};
let currentLang = 'ar';
let currentCity = 'makkah';
let currentIndex = 0;

const allLangs = [
  { code: 'ar', label: 'AR', dir: 'rtl', font: 'Vazirmatn', native: 'العربية' },
  { code: 'fa', label: 'FA', dir: 'rtl', font: 'Vazirmatn', native: 'فارسی' },
  { code: 'en', label: 'EN', dir: 'ltr', font: 'Inter', native: 'English' },
  { code: 'ur', label: 'UR', dir: 'rtl', font: 'Gulzar', native: 'اردو' },
  { code: 'id', label: 'ID', dir: 'ltr', font: 'Inter', native: 'Indonesia' },
  { code: 'bn', label: 'ব', dir: 'ltr', font: 'Noto Sans Bengali', native: 'বাংলা' },
  { code: 'tr', label: 'TR', dir: 'ltr', font: 'Inter', native: 'Türkçe' },
  { code: 'ms', label: 'MS', dir: 'ltr', font: 'Inter', native: 'Melayu' },
  { code: 'fr', label: 'FR', dir: 'ltr', font: 'Inter', native: 'Français' },
  { code: 'sw', label: 'SW', dir: 'ltr', font: 'Inter', native: 'Kiswahili' },
  { code: 'ha', label: 'HA', dir: 'ltr', font: 'Inter', native: 'Hausa' },
  { code: 'ps', label: 'PS', dir: 'rtl', font: 'Vazirmatn', native: 'پښتو' },
  { code: 'uz', label: 'UZ', dir: 'ltr', font: 'Inter', native: 'Oʻzbek' },
  { code: 'ru', label: 'RU', dir: 'ltr', font: 'Inter', native: 'Русский' },
  { code: 'zh', label: '中', dir: 'ltr', font: 'Noto Sans SC', native: '中文' },
  { code: 'az', label: 'AZ', dir: 'ltr', font: 'Inter', native: 'Azərbaycan' },
  { code: 'ku', label: 'KU', dir: 'ltr', font: 'Inter', native: 'Kurdî' },
  { code: 'so', label: 'SO', dir: 'ltr', font: 'Inter', native: 'Soomaali' },
  { code: 'bs', label: 'BS', dir: 'ltr', font: 'Inter', native: 'Bosanski' },
  { code: 'tg', label: 'ТЈ', dir: 'ltr', font: 'Inter', native: 'Тоҷикӣ' }
];

const bgImages = {
  makkah: '/images/makkah/haram/1.jpg',
  madinah: '/images/madinah/nabawi/1.jpg'
};

// ──── INIT ────
async function init() {
  try {
    const placesRes = await fetch('/data/places.json');
    placesData = await placesRes.json();

    // Load current language file
    await loadLang(currentLang);

    setupListeners();
    createTooltip();
    setBgImage('makkah');
    renderApp();
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

// ═══════ LISTENERS ═══════
function setupListeners() {
  // Info button
  document.getElementById('info-btn').addEventListener('click', (e) => {
    e.stopPropagation();
    document.getElementById('desc-overlay').classList.toggle('active');
  });

  // Close button
  document.getElementById('close-desc').addEventListener('click', (e) => {
    e.stopPropagation();
    document.getElementById('desc-overlay').classList.remove('active');
  });

  // Click on empty top area closes overlay
  document.getElementById('app-container').addEventListener('click', (e) => {
    if (!document.getElementById('desc-overlay').classList.contains('active')) return;
    const rect = e.currentTarget.getBoundingClientRect();
    const clickY = e.clientY - rect.top;
    if (clickY < rect.height * 0.2) {
      document.getElementById('desc-overlay').classList.remove('active');
    }
  });

  // City buttons
  document.getElementById('btn-makkah').addEventListener('click', () => switchCity('makkah'));
  document.getElementById('btn-madinah').addEventListener('click', () => switchCity('madinah'));

  // Language sidebar - hover (desktop)
  document.getElementById('lang-sidebar').addEventListener('mouseover', (e) => {
    const item = e.target.closest('.lang-item');
    if (item) showTooltip(item);
  });

  document.getElementById('lang-sidebar').addEventListener('mouseout', () => {
    hideTooltip();
  });

  // Language sidebar - click
  document.getElementById('lang-sidebar').addEventListener('click', async (e) => {
    const item = e.target.closest('.lang-item');
    if (!item) return;
    currentLang = item.dataset.lang;
    applyDir();
    syncLangSidebar();

    // Show tooltip on mobile for 3 seconds
    showTooltip(item);
    setTimeout(hideTooltip, 3000);

    // Scroll selected language to center of sidebar
    const scroll = document.querySelector('.lang-scroll');
    const itemTop = item.offsetTop;
    const itemHeight = item.offsetHeight;
    const scrollHeight = scroll.clientHeight;
    scroll.scrollTo({
      top: itemTop - scrollHeight / 2 + itemHeight / 2,
      behavior: 'smooth'
    });

    await renderApp();
  });
}

// ═══════ HELPERS ═══════
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
  tooltipEl.style.top = (rect.top + rect.height / 2 - 20) + 'px';
  tooltipEl.style.right = 'auto';
  tooltipEl.style.left = (rect.left - tooltipEl.offsetWidth - 10) + 'px';
  tooltipEl.classList.add('show');
}

function hideTooltip() {
  if (tooltipEl) tooltipEl.classList.remove('show');
}

function applyDir() {
  const langInfo = allLangs.find(l => l.code === currentLang);
  document.body.setAttribute('data-lang', currentLang);
}

function syncLangSidebar() {
  document.querySelectorAll('.lang-item').forEach(el => {
    el.classList.toggle('active', el.dataset.lang === currentLang);
  });
}

function setBgImage(city) {
  const scene = document.getElementById('phone-scene');
  scene.style.backgroundImage = `url('${bgImages[city]}')`;
}

function switchCity(city) {
  currentCity = city;
  currentIndex = 0;
  setBgImage(city);

  document.getElementById('btn-makkah').className = `city-btn ${city === 'makkah' ? 'active-makkah' : ''}`;
  document.getElementById('btn-madinah').className = `city-btn ${city === 'madinah' ? 'active-madinah' : ''}`;

  renderApp();
}

// ═══════ RENDER ═══════
async function renderApp() {
  // Load language if not loaded yet
  if (!translations[currentLang]) {
    await loadLang(currentLang);
  }
  
  const lang = translations[currentLang];
  if (!lang) return;

  applyDir();
  renderBottomMenu();
  showPlace(currentIndex);
}

function renderBottomMenu() {
  const list = document.getElementById('places-list');
  list.innerHTML = '';
  const lang = translations[currentLang];
  if (!placesData[currentCity] || !lang) return;

  placesData[currentCity].forEach((place, index) => {
    const info = lang.places[place.id];
    if (!info) return;

    const item = document.createElement('div');
    item.className = `nav-item ${index === currentIndex ? 'active' : ''}`;
    item.id = `nav-${currentCity}-${index}`;
    item.innerHTML = `
      <div class="icon-box">${place.icon}</div>
      <span>${info.title}</span>
    `;
    item.addEventListener('click', () => showPlace(index));
    list.appendChild(item);
  });
}

function showPlace(index) {
  currentIndex = index;
  const place = placesData[currentCity]?.[index];
  const lang = translations[currentLang];
  if (!place || !lang) return;

  const info = lang.places[place.id];
  if (!info) return;

  document.getElementById('app-title').textContent = info.title;
  document.getElementById('app-short').textContent = info.short;
  document.getElementById('modal-title').textContent = info.title;
  document.getElementById('modal-description').innerHTML = info.full.split('\n\n').filter(p => p.trim()).map(p => `<p>${p.trim()}</p>`).join('');

  const track = document.getElementById('image-track');
  track.innerHTML = '';
  place.images.forEach(src => {
    const slide = document.createElement('div');
    slide.className = 'slide';
    slide.innerHTML = `<img src="${src}" alt="${info.title}" loading="lazy" onerror="this.style.background='#222'">`;
    track.appendChild(slide);
  });
  track.scrollLeft = 0;

  document.querySelectorAll('.nav-item').forEach((el, i) => {
    el.classList.toggle('active', i === index);
  });

  const activeItem = document.getElementById(`nav-${currentCity}-${index}`);
  if (activeItem) {
    activeItem.scrollIntoView({ behavior: 'smooth', inline: 'center', block: 'nearest' });
  }
}

// ──── Start ────
window.addEventListener('DOMContentLoaded', init);
