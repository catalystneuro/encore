// One list component for the Datasets, Claims and Findings pages.
//
// The page embeds its configuration as JSON in #list-config:
//   { kind, root, data, facets: [{key, label}], sorts: [{key, label}],
//     labels: {facetKey: {value: text}}, outcomes: {key: [label, css, icon]} }
// Rows are fetched from `data`. Filters, search, sort, page and page size are
// kept in the URL query string, so every view is a link.
(async function () {
  const cfg = JSON.parse(document.getElementById('list-config').textContent);
  const root = cfg.root;
  const $ = (id) => document.getElementById(id);
  const esc = (s) => String(s == null ? '' : s).replace(/[&<>"']/g,
    (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const label = (facet, value) => (cfg.labels[facet] && cfg.labels[facet][value]) || value;
  const values = (row, key) => {
    const v = row[key];
    if (Array.isArray(v)) return v.length ? v : ['(none)'];
    return [v === null || v === undefined || v === '' ? '(none)' : String(v)];
  };

  // On a narrow screen the filters sit above the results: start them closed.
  if (matchMedia('(max-width: 820px)').matches) $('facets').open = false;

  let rows;
  try {
    rows = await (await fetch(root + cfg.data)).json();
  } catch (err) {
    $('results').innerHTML = '<p class="empty">The data could not be loaded.</p>';
    return;
  }
  rows.forEach((r) => { r._text = JSON.stringify(r).toLowerCase(); });

  // --- state <-> URL ---------------------------------------------------------
  const state = { q: '', sort: cfg.sorts[0].key, page: 1, size: 25, f: {} };
  function readUrl() {
    const p = new URLSearchParams(location.search);
    state.q = p.get('q') || '';
    state.sort = p.get('sort') || cfg.sorts[0].key;
    state.page = Math.max(1, parseInt(p.get('page') || '1', 10) || 1);
    state.size = [25, 50, 100].includes(+p.get('size')) ? +p.get('size') : 25;
    state.f = {};
    cfg.facets.forEach((f) => {
      const v = p.get(f.key);
      if (v) state.f[f.key] = new Set(v.split(',').filter(Boolean));
    });
  }
  function writeUrl(push) {
    const p = new URLSearchParams();
    cfg.facets.forEach((f) => {
      if (state.f[f.key] && state.f[f.key].size) p.set(f.key, [...state.f[f.key]].join(','));
    });
    if (state.q) p.set('q', state.q);
    if (state.sort !== cfg.sorts[0].key) p.set('sort', state.sort);
    if (state.page > 1) p.set('page', state.page);
    if (state.size !== 25) p.set('size', state.size);
    const url = location.pathname + (p.toString() ? '?' + p : '') + location.hash;
    history[push ? 'pushState' : 'replaceState'](null, '', url);
  }

  // --- filtering -------------------------------------------------------------
  function matches(row, skipFacet) {
    if (state.q && !row._text.includes(state.q.toLowerCase())) return false;
    for (const f of cfg.facets) {
      if (f.key === skipFacet) continue;
      const chosen = state.f[f.key];
      if (chosen && chosen.size && !values(row, f.key).some((v) => chosen.has(v))) return false;
    }
    return true;
  }
  function sorted(list) {
    const desc = state.sort.startsWith('-');
    const key = desc ? state.sort.slice(1) : state.sort;
    const dir = desc ? -1 : 1;
    return list.slice().sort((a, b) => {
      const x = a[key], y = b[key];
      if (x == null && y == null) return 0;
      if (x == null) return 1;            // missing values last, either direction
      if (y == null) return -1;
      return dir * (typeof x === 'number' && typeof y === 'number' ? x - y : String(x).localeCompare(String(y)));
    });
  }

  // --- rendering: one function per kind of row -------------------------------
  const chip = (outcome) => {
    const [text, css, icon] = cfg.outcomes[outcome];
    return `<span class="chip ${css}"><span class="icon" aria-hidden="true">${icon}</span>${esc(text)}</span>`;
  };
  const miniBar = (counts) => {
    const total = Object.values(counts).reduce((a, b) => a + b, 0);
    if (!total) return '';
    const segs = Object.keys(cfg.outcomes).filter((k) => counts[k]).map((k) =>
      `<span class="seg ${cfg.outcomes[k][1]}" style="flex:${counts[k]}" title="${esc(cfg.outcomes[k][0])}: ${counts[k]}"></span>`).join('');
    const text = Object.keys(cfg.outcomes).filter((k) => counts[k]).map((k) =>
      `${counts[k]} ${esc(cfg.outcomes[k][0].toLowerCase())}`).join(' · ');
    return `<div class="bar mini" role="img" aria-label="${text}">${segs}</div><span class="small muted">${text}</span>`;
  };
  // Claims on data outside the dataset are counted apart from the bar; a row whose claims are mostly
  // there would otherwise look empty.
  const elsewhere = (r) => r.elsewhere
    ? `<div class="small muted">${r.elsewhere} ${r.elsewhere === 1 ? 'claim' : 'claims'} on data outside the dataset, counted apart</div>`
    : '';
  const tier = (r) => r.tier
    ? `<span class="tier${r.tier === 'runs' ? ' pending' : ''}">${esc(r.tier === 'runs' ? 'Not yet verified' : '✓ ' + label('tier', r.tier))}</span>` : '';
  // 38464.5 GB reads better as 38.5 TB, and 40982 files as 41k files (exact figure on hover).
  const size = (gb) => {
    const [v, unit] = gb >= 1000 ? [gb / 1000, 'TB'] : gb >= 1 ? [gb, 'GB'] : [gb * 1000, 'MB'];
    const text = `${v >= 100 ? Math.round(v) : v >= 10 ? v.toFixed(1) : v.toFixed(v < 1 ? 2 : 1)} ${unit}`;
    return `<span title="${gb.toLocaleString()} GB">${text}</span>`;
  };
  const files = (n) => {
    const text = n >= 1e6 ? `${(n / 1e6).toFixed(1)}M` : n >= 1e4 ? `${Math.round(n / 1e3)}k` : n.toLocaleString();
    return `<span title="${n.toLocaleString()} files">${text} file${n === 1 ? '' : 's'}</span>`;
  };
  const tags = (list) => (list || []).map((t) => `<span class="tag">${esc(t)}</span>`).join(' ');

  const render = {
    datasets(r) {
      const href = r.page ? root + r.page : r.url;
      const right = r.status === 'attempted'
        ? `${tier(r)}<span class="small muted">${esc(r.date)}</span>`
        : `<span class="tag">${esc(label('status', r.status))}</span>`;
      return `<div class="row drow">
        <div class="id"><a href="${href}">${esc(r.label)}</a></div>
        <div><p class="title"><a href="${href}">${esc(r.name || r.paper_title)}</a></p>
          <div class="meta">${tags(r.technique)} ${tags(r.species)}
            ${size(r.size_gb)} ${files(r.files)}
            <a href="https://doi.org/${esc(r.paper)}" title="${esc(r.paper_title || r.paper)}">Paper</a>
            ${r.page ? `<a href="${root + r.page}#findings">Findings (${r.findings})</a>` : ''}</div>
          ${r.status === 'attempted' ? `<div class="meta" style="margin-top:6px">${miniBar(r.counts)}${elsewhere(r)}</div>` : ''}</div>
        <div class="right">${right}</div></div>`;
    },
  }[cfg.kind];

  function renderFacets() {
    const html = cfg.facets.map((f) => {
      const counts = new Map();
      rows.forEach((r) => { if (matches(r, f.key)) values(r, f.key).forEach((v) => counts.set(v, (counts.get(v) || 0) + 1)); });
      const chosen = state.f[f.key] || new Set();
      chosen.forEach((v) => { if (!counts.has(v)) counts.set(v, 0); });
      const order = cfg.order && cfg.order[f.key];
      const entries = [...counts.entries()].sort((a, b) => order
        ? (order.indexOf(a[0]) + 1 || 99) - (order.indexOf(b[0]) + 1 || 99)
        : b[1] - a[1] || a[0].localeCompare(b[0]));
      if (!entries.length) return '';
      const limit = 8;
      const items = entries.map(([v, n], i) => {
        const hide = i >= limit && !chosen.has(v) && !f._open;
        return `<label class="${n ? '' : 'zero'}"${hide ? ' hidden' : ''}><input type="checkbox" data-facet="${esc(f.key)}" value="${esc(v)}"${chosen.has(v) ? ' checked' : ''}>
          <span>${esc(label(f.key, v))}</span><span class="c">${n}</span></label>`;
      }).join('');
      const more = entries.length > limit && !f._open
        ? `<button type="button" class="showmore" data-more="${esc(f.key)}">Show all ${entries.length}</button>` : '';
      return `<fieldset class="facet"><legend>${esc(f.label)}</legend>${items}${more}</fieldset>`;
    }).join('');
    $('facet-list').innerHTML = html;
  }

  function renderActive() {
    const parts = [];
    cfg.facets.forEach((f) => (state.f[f.key] || []).forEach((v) =>
      parts.push(`<button type="button" data-drop="${esc(f.key)}" data-value="${esc(v)}">${esc(f.label)}: ${esc(label(f.key, v))}</button>`)));
    if (state.q) parts.push(`<button type="button" data-drop="q">Search: ${esc(state.q)}</button>`);
    $('active').innerHTML = parts.join('');
    $('clear').hidden = !parts.length;
  }

  let current = [];
  function update(push) {
    current = sorted(rows.filter((r) => matches(r)));
    const pages = Math.max(1, Math.ceil(current.length / state.size));
    state.page = Math.min(state.page, pages);
    const start = (state.page - 1) * state.size;
    const shown = current.slice(start, start + state.size);
    $('results').innerHTML = shown.length ? shown.map(render).join('')
      : '<p class="empty">Nothing matches these filters.</p>';
    $('count').textContent = current.length === rows.length
      ? `${rows.length.toLocaleString()} ${cfg.noun}`
      : `${current.length.toLocaleString()} of ${rows.length.toLocaleString()} ${cfg.noun}`;
    renderFacets();
    renderActive();
    renderPager(pages, start, shown.length);
    writeUrl(push);
  }

  function renderPager(pages, start, n) {
    const el = $('pager');
    if (!current.length) { el.innerHTML = ''; return; }
    const nums = new Set([1, pages, state.page - 1, state.page, state.page + 1].filter((p) => p >= 1 && p <= pages));
    let last = 0, buttons = '';
    [...nums].sort((a, b) => a - b).forEach((p) => {
      if (p - last > 1) buttons += '<span class="muted">…</span>';
      buttons += `<button type="button" data-page="${p}"${p === state.page ? ' aria-current="page"' : ''}>${p}</button>`;
      last = p;
    });
    el.innerHTML = `<span class="muted">${start + 1}–${start + n} of ${current.length.toLocaleString()}</span><span class="grow"></span>
      <button type="button" data-page="${state.page - 1}"${state.page === 1 ? ' disabled' : ''} aria-label="Previous page">‹</button>
      ${buttons}
      <button type="button" data-page="${state.page + 1}"${state.page === pages ? ' disabled' : ''} aria-label="Next page">›</button>
      <select class="ghost" id="size" aria-label="Rows per page">${[25, 50, 100].map((s) =>
        `<option value="${s}"${s === state.size ? ' selected' : ''}>${s} per page</option>`).join('')}</select>`;
  }

  // --- events ----------------------------------------------------------------
  $('sort').innerHTML = cfg.sorts.map((s) => `<option value="${esc(s.key)}">${esc(s.label)}</option>`).join('');
  function syncControls() { $('q').value = state.q; $('sort').value = state.sort; }

  $('facet-list').addEventListener('change', (ev) => {
    const box = ev.target.closest('input[data-facet]');
    if (!box) return;
    const set = state.f[box.dataset.facet] || (state.f[box.dataset.facet] = new Set());
    box.checked ? set.add(box.value) : set.delete(box.value);
    state.page = 1; update(true);
  });
  $('facet-list').addEventListener('click', (ev) => {
    const more = ev.target.closest('[data-more]');
    if (!more) return;
    cfg.facets.find((f) => f.key === more.dataset.more)._open = true;
    renderFacets();
  });
  $('active').addEventListener('click', (ev) => {
    const b = ev.target.closest('[data-drop]');
    if (!b) return;
    if (b.dataset.drop === 'q') state.q = '';
    else state.f[b.dataset.drop].delete(b.dataset.value);
    state.page = 1; syncControls(); update(true);
  });
  $('clear').addEventListener('click', () => { state.f = {}; state.q = ''; state.page = 1; syncControls(); update(true); });
  let timer;
  $('q').addEventListener('input', () => {
    clearTimeout(timer);
    timer = setTimeout(() => { state.q = $('q').value.trim(); state.page = 1; update(false); }, 120);
  });
  $('sort').addEventListener('change', () => { state.sort = $('sort').value; state.page = 1; update(true); });
  $('pager').addEventListener('click', (ev) => {
    const b = ev.target.closest('[data-page]');
    if (!b || b.disabled) return;
    state.page = +b.dataset.page; update(true);
    $('results').scrollIntoView({ block: 'start' });
  });
  $('pager').addEventListener('change', (ev) => {
    if (ev.target.id === 'size') { state.size = +ev.target.value; state.page = 1; update(true); }
  });
  const exportButton = $('export');
  if (exportButton) exportButton.addEventListener('click', () => {
    const cols = cfg.csv;
    const cell = (v) => `"${String(Array.isArray(v) ? v.join('; ') : v == null ? '' : v).replace(/"/g, '""')}"`;
    const csv = [cols.join(',')].concat(current.map((r) => cols.map((c) => cell(r[c])).join(','))).join('\n');
    const a = document.createElement('a');
    a.href = URL.createObjectURL(new Blob([csv], { type: 'text/csv' }));
    a.download = `${cfg.kind}.csv`;
    a.click();
    URL.revokeObjectURL(a.href);
  });
  addEventListener('popstate', () => { readUrl(); syncControls(); update(false); });

  readUrl(); syncControls(); update(false);
  document.documentElement.dataset.listReady = '1';
})();
