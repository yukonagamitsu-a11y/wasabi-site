// Mobile menu toggle
document.querySelectorAll('.menu-btn').forEach(function (btn) {
  var nav = btn.parentNode.querySelector('.nav');
  if (!nav) return;
  function set(open) {
    nav.classList.toggle('open', open);
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    btn.textContent = open ? '×' : '≡';
  }
  btn.addEventListener('click', function () { set(!nav.classList.contains('open')); });
  nav.addEventListener('click', function (e) { if (e.target.tagName === 'A') set(false); });
});

// Menu pages: render from menu-data.js, build category chips
document.querySelectorAll('[data-menu]').forEach(function (root) {
  if (!window.WASABI_MENU) return;
  var cats = window.WASABI_MENU[root.getAttribute('data-menu')] || [];
  var chips = document.getElementById(root.getAttribute('data-chips') || 'chips');
  function slug(s) { return s.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, ''); }
  function el(tag, cls, text) { var e = document.createElement(tag); if (cls) e.className = cls; if (text) e.textContent = text; return e; }

  cats.forEach(function (c) {
    var id = 'c-' + root.getAttribute('data-menu') + '-' + slug(c.name);
    var sec = el('section', 'mcat'); sec.id = id;
    sec.appendChild(el('h2', '', c.name));
    var ul = el('ul', 'items');
    c.items.forEach(function (it) {
      var li = el('li', 'item');
      var row = el('div', 'row');
      var n = el('span', 'n', it.n);
      if (it.jp) n.appendChild(el('i', '', it.jp));
      var p = el('span', 'p');
      it.p.forEach(function (v) {
        var s = el('span');
        if (v.l) s.appendChild(el('small', '', v.l));
        if (v.v) s.appendChild(document.createTextNode(v.v));
        p.appendChild(s);
      });
      row.appendChild(n); row.appendChild(p); li.appendChild(row);
      if (it.d) li.appendChild(el('p', 'd', it.d));
      ul.appendChild(li);
    });
    sec.appendChild(ul);
    root.appendChild(sec);
    if (chips) {
      var a = el('a', '', c.name); a.href = '#' + id; chips.appendChild(a);
    }
  });

  // highlight the chip of the section being read
  if (chips && 'IntersectionObserver' in window) {
    var links = {};
    chips.querySelectorAll('a').forEach(function (a) { links[a.getAttribute('href').slice(1)] = a; });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        Object.keys(links).forEach(function (k) { links[k].classList.remove('on'); });
        var a = links[en.target.id]; if (!a) return;
        a.classList.add('on');
        var box = chips, l = a.offsetLeft - 16;
        if (l < box.scrollLeft || l + a.offsetWidth > box.scrollLeft + box.clientWidth) box.scrollTo({ left: l, behavior: 'smooth' });
      });
    }, { rootMargin: '-80px 0px -70% 0px' });
    root.querySelectorAll('.mcat').forEach(function (s) { io.observe(s); });
  }

  var pr = document.getElementById(root.getAttribute('data-print') || 'print-btn');
  if (pr) pr.addEventListener('click', function () { window.print(); });
});
