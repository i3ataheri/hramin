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
        highlight();
        renderSlide();
        requestAnimationFrame(() => scrollToItem(i));
      });
      list.appendChild(btn);
    });

    el.appendChild(list);
    highlight();
    requestAnimationFrame(() => scrollToItem(currentPlaceIndex));
  }

  function update() {
    if (!el) { build(); return; }
    const items = el.querySelectorAll('.pm-item');
    const places = getPlaces();
    if (items.length !== places.length) { build(); return; }
    items.forEach((item, i) => { item.textContent = getTitle(places[i]); });
    highlight();
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

    const itemLeft = item.offsetLeft;
    const itemWidth = item.offsetWidth;
    const containerWidth = el.clientWidth;
    const scrollTarget = itemLeft - (containerWidth / 2) + (itemWidth / 2);

    el.scrollTo({ left: Math.max(0, scrollTarget), behavior: 'smooth' });
  }

  return { build, update, highlight };
})();
