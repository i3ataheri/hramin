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

    const track = document.createElement('div');
    track.className = 'pm-track';

    getPlaces().forEach((place, i) => {
      const btn = document.createElement('button');
      btn.className = 'pm-item';
      btn.textContent = getTitle(place);
      btn.addEventListener('click', () => {
        currentPlaceIndex = i;
        currentPhotoIndex = 0;
        renderSlide();
        highlight();
        requestAnimationFrame(() => scrollToItem(i));
      });
      track.appendChild(btn);
    });

    el.appendChild(track);
    highlight();
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

  function scrollToItem(index) {
    const track = el?.querySelector('.pm-track');
    const items = el?.querySelectorAll('.pm-item');
    if (!track || !items || !items[index]) return;

    const item = items[index];
    const trackRect = track.getBoundingClientRect();
    const itemRect = item.getBoundingClientRect();

    const scrollTarget =
      track.scrollLeft + itemRect.left - trackRect.left - (track.clientWidth / 2) + (itemRect.width / 2);

    track.scrollTo({ left: Math.max(0, scrollTarget), behavior: 'smooth' });
  }

  return { build, update, highlight, scrollToItem };
})();
