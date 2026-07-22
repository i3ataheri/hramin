/* ══════════════════════════════════════════════════════════════
   PLACE MENU — Horizontal scrollable location navigation
   ══════════════════════════════════════════════════════════════ */

const PlaceMenu = (() => {
  let el = null;

  function getPlaces() {
    return placesData[currentCity] || [];
  }

  function getTitle(place) {
    return translations[currentLang]?.places?.[place.id]?.title || place.id;
  }

  function build() {
    el = document.getElementById('place-menu');
    if (!el) return;
    el.innerHTML = '';

    const list = document.createElement('div');
    list.className = 'pm-list';

    getPlaces().forEach((place, i) => {
      const btn = document.createElement('button');
      btn.className = 'pm-item';
      btn.textContent = getTitle(place);
      btn.addEventListener('click', () => {
        currentPlaceIndex = i;
        currentPhotoIndex = 0;
        renderSlide();
        highlight();
        scrollToItem(i);
      });
      list.appendChild(btn);
    });

    el.appendChild(list);
    highlight();
    scrollToItem(currentPlaceIndex);
  }

  function update() {
    if (!el) { build(); return; }

    const items = el.querySelectorAll('.pm-item');
    const places = getPlaces();

    if (items.length !== places.length) { build(); return; }

    items.forEach((item, i) => {
      item.textContent = getTitle(places[i]);
    });
    
    highlight();
    // این خط اضافه شد تا در صورت تغییر خودکار مکان، منو هم اسکرول شود
    scrollToItem(currentPlaceIndex); 
  }

  function highlight() {
    if (!el) return;
    el.querySelectorAll('.pm-item').forEach((item, i) => {
      item.classList.toggle('active', i === currentPlaceIndex);
    });
  }

  function scrollToItem(index) {
    if (!el) return;
    const item = el.querySelectorAll('.pm-item')?.[index];
    if (!item) return;

    // متد مدرن و نیتیو مرورگر که با صفحات RTL (راست‌چین) کاملاً سازگار است
    // و آیتم را به نرمی دقیقاً در مرکز قرار می‌دهد
    item.scrollIntoView({ 
      behavior: 'smooth', 
      inline: 'center', 
      block: 'nearest' 
    });
  }

  return { build, update, highlight };
})();