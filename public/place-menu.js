/* ══════════════════════════════════════════════════════════════
   PLACE MENU — Horizontal scrollable location navigation
   ══════════════════════════════════════════════════════════════ */

const PlaceMenu = (() => {
  let el = null;
  let track = null;

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

    track = document.createElement('div');
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
    if (!track) track = el?.querySelector('.pm-track');
    if (!track) return;

    const items = track.querySelectorAll('.pm-item');
    const target = items[index];
    if (!target) return;

    if (track.scrollWidth <= track.clientWidth) return;

    let left = 0;
    const gap = 8;
    for (let i = 0; i < index; i++) {
      left += items[i].offsetWidth + gap;
    }
    left += target.offsetWidth / 2;
    left -= track.clientWidth / 2;

    const max = track.scrollWidth - track.clientWidth;
    track.scrollLeft = Math.max(0, Math.min(left, max));
  }

  return { build, update, highlight, scrollTo };
})();
