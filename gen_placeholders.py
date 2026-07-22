import os

locations = {
    'makkah': {
        'haram': {'ar': 'الحرم المكي', 'colors': ['#1a5276', '#2e86c1'], 'count': 8},
        'hira': {'ar': 'غار حراء', 'colors': ['#6c3483', '#8e44ad'], 'count': 5},
        'thawr': {'ar': 'جبل ثور', 'colors': ['#784212', '#b7950b'], 'count': 4},
        'arafat': {'ar': 'عرفات', 'colors': ['#1e8449', '#27ae60'], 'count': 6},
        'mina': {'ar': 'منى', 'colors': ['#922b21', '#c0392b'], 'count': 5},
        'muzdalifah': {'ar': 'المزدلفة', 'colors': ['#1b4f72', '#2980b9'], 'count': 3},
        'namirah': {'ar': 'نمرة', 'colors': ['#7d6608', '#d4ac0d'], 'count': 3},
        'khayf': {'ar': 'allee', 'colors': ['#4a235a', '#7d3c98'], 'count': 4},
        'birthplace': {'ar': 'مولد النبي', 'colors': ['#0e6655', '#1abc9c'], 'count': 3},
        'jin_mosque': {'ar': 'مسجد الجن', 'colors': ['#1a5276', '#5dade2'], 'count': 3},
    },
    'madinah': {
        'nabawi': {'ar': 'المسجد النبوي', 'colors': ['#1e8449', '#2ecc71'], 'count': 10},
        'baqi': {'ar': 'البقيع', 'colors': ['#6c3483', '#a569bd'], 'count': 5},
        'quba': {'ar': 'مسجد قباء', 'colors': ['#1a5276', '#3498db'], 'count': 6},
        'uhud': {'ar': 'جبل أحد', 'colors': ['#922b21', '#e74c3c'], 'count': 7},
        'qiblatayn': {'ar': 'القبلتين', 'colors': ['#7d6608', '#f1c40f'], 'count': 4},
        'sabah': {'ar': 'السبع مساجد', 'colors': ['#0e6655', '#16a085'], 'count': 3},
        'khandaq': {'ar': 'الخندق', 'colors': ['#784212', '#dc7633'], 'count': 4},
        'ghamamah': {'ar': 'مسجد الغمام', 'colors': ['#2c3e50', '#7f8c8d'], 'count': 3},
        'ijabah': {'ar': 'مسجد الإجابة', 'colors': ['#4a235a', '#8e44ad'], 'count': 3},
        'miqat': {'ar': 'الميقات', 'colors': ['#1b4f72', '#2e86c1'], 'count': 4},
        'jummah': {'ar': 'مسجد الجمعة', 'colors': ['#1e8449', '#27ae60'], 'count': 3},
        'ambariyah': {'ar': 'العمرية', 'colors': ['#922b21', '#c0392b'], 'count': 3},
    }
}

def make_geometric_pattern(color1, color2, name_ar, idx):
    """Generate Islamic geometric SVG"""
    hue_shift = (idx * 37) % 360
    angle = (idx * 15) % 360
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="600" viewBox="0 0 800 600">
  <defs>
    <linearGradient id="bg{idx}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{color1}"/>
      <stop offset="100%" stop-color="{color2}"/>
    </linearGradient>
    <pattern id="pat{idx}" width="60" height="60" patternUnits="userSpaceOnUse" patternTransform="rotate({angle})">
      <rect width="60" height="60" fill="none"/>
      <circle cx="30" cy="30" r="28" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
      <circle cx="30" cy="30" r="18" fill="none" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>
      <circle cx="30" cy="30" r="8" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
      <line x1="0" y1="30" x2="60" y2="30" stroke="rgba(255,255,255,0.04)" stroke-width="0.5"/>
      <line x1="30" y1="0" x2="30" y2="60" stroke="rgba(255,255,255,0.04)" stroke-width="0.5"/>
      <line x1="0" y1="0" x2="60" y2="60" stroke="rgba(255,255,255,0.03)" stroke-width="0.5"/>
      <line x1="60" y1="0" x2="0" y2="60" stroke="rgba(255,255,255,0.03)" stroke-width="0.5"/>
      <polygon points="30,2 58,30 30,58 2,30" fill="none" stroke="rgba(255,255,255,0.07)" stroke-width="0.8"/>
    </pattern>
    <radialGradient id="glow{idx}" cx="50%" cy="40%" r="60%">
      <stop offset="0%" stop-color="rgba(255,255,255,0.15)"/>
      <stop offset="100%" stop-color="rgba(255,255,255,0)"/>
    </radialGradient>
  </defs>
  <rect width="800" height="600" fill="url(#bg{idx})"/>
  <rect width="800" height="600" fill="url(#pat{idx})"/>
  <rect width="800" height="600" fill="url(#glow{idx})"/>
  <text x="400" y="280" text-anchor="middle" font-family="serif" font-size="48" fill="rgba(255,255,255,0.25)" direction="rtl">{name_ar}</text>
  <text x="400" y="340" text-anchor="middle" font-family="sans-serif" font-size="16" fill="rgba(255,255,255,0.15)">{idx + 1}</text>
</svg>'''
    return svg

idx = 0
for city, places in locations.items():
    for place_id, info in places.items():
        folder = f'public/images/{city}/{place_id}'
        os.makedirs(folder, exist_ok=True)
        for i in range(info['count']):
            svg = make_geometric_pattern(
                info['colors'][0], info['colors'][1],
                info['ar'], idx + i
            )
            filepath = f'{folder}/{i+1}.svg'
            with open(filepath, 'w') as f:
                f.write(svg)
        print(f'{city}/{place_id}: {info["count"]} images created')
        idx += info['count']

print(f'\nTotal: {idx} placeholder images created')
