/* ══════════════════════════════════════════════════════════════
   PLACE MENU — Horizontal scrollable location navigation
   ══════════════════════════════════════════════════════════════ */

const PlaceMenu = {
  container: null,
  inner: null,

  init() {
    this.container = document.getElementById('place-menu');
    if (!this.container) return;
    this.build();
  },

  build() {
    if (!this.container) return;
    this.container.innerHTML = '';

    this.inner = document.createElement('div');
    this.inner.className = 'place-menu-inner';
    this.container.appendChild(this.inner);

    const places = getPlaces();
    const lang = translations[currentLang];

    places.forEach((place, i) => {
      const btn = document.createElement('button');
      btn.className = 'place-item';
      btn.textContent = lang?.places?.[place.id]?.title || place.id;
      btn.addEventListener('click', () => {
        currentPlaceIndex = i;
        currentPhotoIndex = 0;
        renderSlide();
        this.scrollTo(i);
      });
      this.inner.appendChild(btn);
    });

    this.updateActive();
  },

  update() {
    if (!this.inner) {
      this.build();
      return;
    }

    const places = getPlaces();
    const lang = translations[currentLang];
    const items = this.inner.querySelectorAll('.place-item');

    if (items.length !== places.length) {
      this.build();
      return;
    }

    items.forEach((item, i) => {
      item.textContent = lang?.places?.[places[i].id]?.title || places[i].id;
      item.classList.toggle('active', i === currentPlaceIndex);
    });
  },

  updateActive() {
    if (!this.inner) return;
    this.inner.querySelectorAll('.place-item').forEach((item, i) => {
      item.classList.toggle('active', i === currentPlaceIndex);
    });
  },

  scrollTo(index) {
    if (!this.inner) return;

    const items = this.inner.querySelectorAll('.place-item');
    const target = items[index];
    if (!target) return;

    if (this.inner.scrollWidth <= this.inner.clientWidth) return;

    const scrollPos = target.offsetLeft - this.inner.clientWidth / 2 + target.offsetWidth / 2;
    const maxScroll = this.inner.scrollWidth - this.inner.clientWidth;
    this.inner.scrollLeft = Math.max(0, Math.min(scrollPos, maxScroll));
  }
};
