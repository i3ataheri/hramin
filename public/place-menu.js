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
      btn.addEventListener('click', () => select(i));
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

  function select(index) {
    currentPlaceIndex = index;
    currentPhotoIndex = 0;
    renderSlide();
    scrollTo(index);
  }

  function scrollTo(index) {
    const track = el?.querySelector('.pm-track');
    const item = track?.querySelectorAll('.pm-item')?.[index];
    if (!track || !item) return;

    if (track.scrollWidth <= track.clientWidth) return;

    const pos = item.offsetLeft - track.clientWidth / 2 + item.offsetWidth / 2;
    const max = track.scrollWidth - track.clientWidth;
    track.scrollLeft = Math.max(0, Math.min(pos, max));
  }

  return { build, update, highlight, scrollTo };
})();
