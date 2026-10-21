"""Regenerate the five HTML pages from shared pieces.  Run: python tools/build_pages.py"""
import os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
MAPS = 'https://www.google.com/maps/search/?api=1&query=848+E+Ridgewood+Ave+Ridgewood+NJ+07450'

HEAD = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<meta name="robots" content="noindex, nofollow"><!-- prototype stage: remove this line when the site goes live -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Jost:wght@400;500;600&family=Zen+Kaku+Gothic+New:wght@400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>
'''

def header(cur):
    def a(href, label):
        c = ' aria-current="page"' if href == cur else ''
        return '<li><a href="%s"%s>%s</a></li>' % (href, c, label)
    return '''<header class="top">
  <div class="wrap info-row">
    <a class="info-box" href="tel:+12014937575">Call for takeout <span class="num">201-493-7575</span></a>
    <a class="info-box" href="%s" target="_blank" rel="noopener">848 E. Ridgewood Ave<br>Ridgewood, NJ 07450</a>
  </div>
  <div class="navbar">
    <div class="wrap">
      <a class="logo" href="index.html" aria-label="Wasabi Japanese Restaurant - Home"><img src="images/logo-round.png" alt="Wasabi Japanese Restaurant"></a>
      <button class="menu-btn" type="button" aria-label="Menu" aria-expanded="false" aria-controls="site-nav">&#8801;</button>
      <ul class="nav" id="site-nav">
        %s
        %s
        <li class="spacer" aria-hidden="true"></li>
        %s
        %s
        %s
      </ul>
    </div>
  </div>
''' % (MAPS, a('lunch-menu.html', 'Lunch Menu'), a('dinner-menu.html', 'Dinner Menu'),
       a('about.html', 'About Us'), a('contact.html', 'Contact Us'),
       a('index.html', 'Home').replace('<li>', '<li class="home-li">'))

def banner(name, cls=''):
    return '''  <div class="wrap banner %s">
    <div class="frame"><picture><source media="(max-width:820px)" srcset="images/banner-%s-m.jpg"><img src="images/banner-%s.jpg" alt=""></picture></div>
  </div>
</header>
''' % (cls, name, name)

FOOT = '''
<footer>
  <div class="wrap">
    <nav>
      <a href="index.html">Home</a><a href="lunch-menu.html">Lunch Menu</a><a href="dinner-menu.html">Dinner Menu</a><a href="about.html">About Us</a><a href="contact.html">Contact Us</a>
    </nav>
    <span>&copy; 2026 Wasabi Japanese Restaurant</span>
  </div>
</footer>

<div class="dock">
  <a class="d-call" href="tel:+12014937575"><span>Call</span> <strong>201-493-7575</strong></a>
  <a class="d-map" href="%s" target="_blank" rel="noopener" aria-label="Directions on Google Maps"><strong>Map</strong></a>
</div>

%%s<script src="script.js"></script>
</body>
</html>
''' % MAPS

HOURS = '''<div class="hours">
        <h3>Restaurant Hours</h3>
        <p><strong>Lunch</strong> 12:00pm - 2:30pm<br><strong>Dinner</strong> 5:00pm - 9:00pm</p>
        <p class="closed">Closed on Tuesdays</p>
      </div>'''

PAGES = []

def write(fn, title, desc, cur, top, body, scripts=''):
    PAGES.append(dict(fn=fn, cur=cur, html=header(cur) + top + '\n<main>\n' + body + '</main>\n' + (FOOT % '').split('<script')[0]))
    html = HEAD % dict(title=title, desc=desc) + header(cur) + top + '\n<main>\n' + body + '</main>\n' + FOOT % scripts
    with open(os.path.join(ROOT, fn), 'w', encoding='utf8') as f:
        f.write(html)

# ---- home
HERO = '''  <div class="wrap banner hero">
    <div class="frame">
      <img src="images/hero-sushi.jpg" alt="Assorted sushi and sashimi on a black plate">
      <div class="hero-text">
        <p class="eyebrow">Try our</p>
        <h1>Sushi Sashimi Combo</h1>
      </div>
    </div>
  </div>
</header>
'''

write('index.html', 'Wasabi Japanese Restaurant | Ridgewood, NJ',
      'Authentic Japanese cuisine in Ridgewood, NJ. Lunch and dinner, closed Tuesdays. Call 201-493-7575.',
      'index.html', HERO, '''  <div class="wrap home-top">
    ''' + HOURS + '''
  </div>

  <section class="boxes">
    <div class="wrap box-grid">
      <div class="box">
        <a class="pic" href="lunch-menu.html#c-lunch-combination"><img src="images/combo-a.jpg" alt="Lunch combination meal"></a>
        <p class="tag">Most popular</p>
        <h3>Lunch Combination Meal</h3>
        <a class="btn" href="lunch-menu.html#c-lunch-combination">View Lunch Menu</a>
      </div>
      <div class="box">
        <a class="pic" href="dinner-menu.html#c-dinner-wasabi-original-roll"><img src="images/dinner-box.jpg" alt="Special rolls"></a>
        <p class="tag">Wasabi originals</p>
        <h3>Special Rolls</h3>
        <a class="btn" href="dinner-menu.html#c-dinner-wasabi-original-roll">View Dinner Menu</a>
      </div>
    </div>
  </section>

  <div class="wrap intro">
    <section class="intro-main">
      <h2><em>Wasabi:</em> Authentic Japanese Cuisine in Ridgewood, NJ</h2>
      <div class="photo-row">
        <div class="photo"><img src="images/interior.jpg" alt="Inside Wasabi Japanese Restaurant"></div>
        <p>For the best sushi and Japanese cuisine in Bergen County, come to Wasabi Japanese Restaurant. Located on E. Ridgewood Ave, just a few blocks outside of downtown Ridgewood, New Jersey, Wasabi is a perfect place to sit back, relax and enjoy a delicious meal. We offer full lunch and dinner menus six days a week.</p>
      </div>
      <p>For lunch, try any one of our tasty combination platters, noodle dishes, rice bowls, or Sushi Sashimi. For dinner, choose from an assortment of sushi rolls, hot and cold appetizers, teriyaki, tempura or Donburi entrees. You won't find a better selection of Authentic Japanese Cuisine in the Ridgewood area.</p>
    </section>
  </div>
''')

# ---- menus
def menu_page(fn, kind, label, other_fn, other_label, meal_line):
    body = '''  <div class="wrap menu-wrap">
    <h1 class="page-title">Wasabi's %s Menu</h1>
    <p class="menu-sub">%s &middot; <strong>Closed on Tuesdays</strong></p>
    <p class="price-note">Prices will be added here.</p>
    <div class="menu-actions">
      <a class="btn ghost" href="%s">View %s Menu</a>
      <button class="btn ghost" id="print-btn" type="button">Print this menu</button>
    </div>
    <nav class="chips" id="chips" aria-label="Menu categories"></nav>
    <div id="menu-root" data-menu="%s" data-chips="chips" data-print="print-btn"></div>
  </div>
''' % (label.upper(), meal_line, other_fn, other_label, kind)
    write(fn, '%s Menu | Wasabi Japanese Restaurant' % label,
          'Wasabi %s menu with prices. Ridgewood, NJ.' % label.lower(), fn,
          banner(kind, 'menu-banner'), body, '<script src="menu-data.js"></script>\n')

menu_page('lunch-menu.html', 'lunch', 'Lunch', 'dinner-menu.html', 'Dinner', 'Lunch 12:00pm - 2:30pm')
menu_page('dinner-menu.html', 'dinner', 'Dinner', 'lunch-menu.html', 'Lunch', 'Dinner 5:00pm - 9:00pm')

# ---- about
write('about.html', 'About Us | Wasabi Japanese Restaurant', 'About Wasabi Japanese Restaurant in Ridgewood, NJ.',
      'about.html', '  <div class="strip"></div>\n</header>\n', '''  <div class="wrap about">
    <div class="about-text">
      <h1 class="h-left">About Wasabi Japanese Restaurant</h1>
      <p>Wasabi opened its doors in 2000 and has become one of the premier Japanese restaurants in Ridgewood, New Jersey.</p>
      <!-- TODO: add the owner's story here -->
    </div>
    <div class="about-photo"><img src="images/interior.jpg" alt="Inside Wasabi Japanese Restaurant"></div>
  </div>
''')

# ---- contact
write('contact.html', 'Contact Us | Wasabi Japanese Restaurant',
      'Call 201-493-7575. 848 E. Ridgewood Ave, Ridgewood, NJ. Lunch 12:00pm-2:30pm, Dinner 5:00pm-9:00pm, closed Tuesdays.',
      'contact.html', banner('contact', 'menu-banner'), '''  <div class="wrap contact">
    <h1 class="h-left">Contact Ridgewood's Premiere Japanese Restaurant</h1>
    <div class="contact-grid">
      <div class="contact-info">
        ''' + HOURS + '''
        <a class="call-btn" href="tel:+12014937575" style="margin-top:24px"><span>Call for takeout</span><strong>201-493-7575</strong></a>
        <h2>Address</h2>
        <p><a class="addr-link" href="''' + MAPS + '''" target="_blank" rel="noopener">848 E. Ridgewood Ave<br>Ridgewood, NJ 07450</a></p>
        <a class="btn ghost" href="''' + MAPS + '''" target="_blank" rel="noopener">Open in Google Maps</a>
      </div>
      <div class="map">
        <iframe title="Map to Wasabi Japanese Restaurant" src="https://www.google.com/maps?q=848+E+Ridgewood+Ave+Ridgewood+NJ+07450&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
      </div>
    </div>
  </div>
''')
print('pages built')


# ---------------- single-file preview (for the private cloud preview) ----------------
import re
ROUTES = {'index.html': 'home', 'lunch-menu.html': 'lunch', 'dinner-menu.html': 'dinner', 'about.html': 'about', 'contact.html': 'contact'}
def rd(n):
    return open(os.path.join(ROOT, n), encoding='utf8').read()
views = []
for pg in PAGES:
    r = ROUTES[pg['fn']]
    h = pg['html']
    h = h.replace('lunch-menu.html#c-lunch-combination', 'lunch-menu.html').replace('dinner-menu.html#c-dinner-wasabi-original-roll', 'dinner-menu.html')
    for fn, rt in ROUTES.items():
        h = h.replace('href="%s"' % fn, 'href="#%s"' % rt)
    h = h.replace('id="chips"', 'id="chips-%s"' % r).replace('data-chips="chips"', 'data-chips="chips-%s"' % r)
    h = h.replace('id="print-btn"', 'id="print-%s"' % r).replace('data-print="print-btn"', 'data-print="print-%s"' % r)
    h = re.sub(r'<div class="map">.*?</div>', '<div class="map"><p style="padding:24px;background:#f1f1f1;border-radius:8px;color:#666">The Google map is shown here on the live site.</p></div>', h, flags=re.S)
    views.append('<div class="view" id="v-%s" hidden>\n%s</div>' % (r, h))
css = rd('style.css').replace('@media print{', '@media print{.view[hidden]{display:none}')
router = """
(function(){
  var routes={home:1,lunch:1,dinner:1,about:1,contact:1};
  function show(){
    var r=location.hash.slice(1);
    if(!routes[r]){ if(!document.querySelector('.view:not([hidden])')) r='home'; else return; }
    document.querySelectorAll('.view').forEach(function(v){ v.hidden = v.id!=='v-'+r; });
    document.querySelectorAll('.nav a, footer nav a').forEach(function(a){
      if(a.getAttribute('href')==='#'+r) a.setAttribute('aria-current','page'); else a.removeAttribute('aria-current');
    });
    window.scrollTo(0,0);
  }
  window.addEventListener('hashchange',show); show();
})();
"""
out = ('<title>Wasabi Site Prototype</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n'
       '<link href="https://fonts.googleapis.com/css2?family=Jost:wght@400;500;600&family=Zen+Kaku+Gothic+New:wght@400&display=swap" rel="stylesheet">\n'
       '<style>\n' + css + '\n</style>\n' + '\n'.join(views) +
       '\n<script>\n' + rd('menu-data.js') + '\n</script>\n<script>\n' + rd('script.js') + '\n</script>\n<script>' + router + '</script>\n')
os.makedirs(os.path.join(ROOT, 'preview'), exist_ok=True)
open(os.path.join(ROOT, 'preview', 'prototype.html'), 'w', encoding='utf8').write(out)
print('preview built')
