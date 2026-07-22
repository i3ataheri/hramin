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

    getPlaces().forEach((place, i) => {
      const btn = document.createElement('button');
      btn.className = 'pm-item';
      btn.textContent = getTitle(place);
      btn.addEventListener('click', () => select(i));
      el.appendChild(btn);
    });

    highlight();
    requestAnimationFrame(() => scrollToItem(currentPlaceIndex));
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
  }

  function highlight() {
    if (!el) return;
    el.querySelectorAll('.pm-item').forEach((item, i) => {
      item.classList.toggle('active', i === currentPlaceIndex);
    });
  }

  function select(index) {
    currentPlaceIndex = index;
    currentPhotoIndex = 0;
    renderSlide();
    highlight();
    scrollToItem(index);
  }

  function scrollToItem(index) {
    if (!el) return;
    const items = el.querySelectorAll('.pm-item');
    const item = items[index];
    if (!item) return;

    const scrollLeftTarget = item.offsetLeft - (el.offsetWidth / 2) + (item.offsetWidth / 2);
    el.scrollTo({ left: Math.max(0, scrollLeftTarget), behavior: 'smooth' });
  }

  return { build, update, highlight };
})();
