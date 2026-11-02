// The overview's dashboard: totals for the chosen datasets, a running total of one measure, and the outcomes
// of the claims tested each day. Drawn from the JSON in #progress-data, at the width of its panel.
(function () {
  var node = document.getElementById("progress-data");
  if (!node) return;
  var P = JSON.parse(node.textContent), NS = "http://www.w3.org/2000/svg";
  // Each series arrives as one list per measure; the charts read it as one row per day.
  Object.keys(P.series).forEach(function (s) {
    var cols = P.series[s];
    P.series[s] = P.days.map(function (_, i) {
      var row = {};
      for (var k in cols) row[k] = cols[k][i];
      return row;
    });
  });
  var state = { subset: "all", metric: "datasets" };
  var root = document.querySelector(".progress");
  var line = document.getElementById("progress-line"), cols = document.getElementById("progress-outcomes");
  var outcomeKeys = Object.keys(P.outcomes), protocols = P.protocols || [];
  // Two measures are stacked: claims by outcome, and attempts by the protocol version they followed, shaded in
  // the bar colour from light (the oldest version) to dark (the newest), with attempts that recorded none in gray.
  function protocolFill(v) {
    if (v === "not recorded") return "var(--muted)";
    var known = protocols.filter(function (p) { return p !== "not recorded"; }), i = known.indexOf(v);
    var share = known.length > 1 ? 30 + 70 * i / (known.length - 1) : 100;
    return "color-mix(in srgb, var(--bar) " + share.toFixed(0) + "%, var(--surface))";
  }
  function stackOf(m) {
    if (m === "claims") return {
      keys: outcomeKeys, label: function (k) { return P.outcomes[k].label.toLowerCase(); },
      paint: function (node, k) { node.setAttribute("class", "seg-" + P.outcomes[k].css); },
      swatch: function (k) { return '<span class="swatch ' + P.outcomes[k].css + '" aria-hidden="true"></span>'; } };
    if (m === "attempts" && protocols.length) return {
      keys: protocols.map(function (v) { return "protocol:" + v; }),
      label: function (k) { var v = k.slice(9); return v === "not recorded" ? "protocol not recorded" : "protocol " + v; },
      // A thin line of the surface between versions, as their shades are close.
      paint: function (node, k) { node.setAttribute("style", "fill:" + protocolFill(k.slice(9)) + ";stroke:var(--surface);stroke-width:1"); },
      swatch: function (k) { return '<span class="swatch" style="background:' + protocolFill(k.slice(9)) + '" aria-hidden="true"></span>'; } };
    return null;
  }
  var DAY_NOTES = {
    datasets: "Each dataset on the date of its first attempt.",
    papers: "Each paper on the date of its first attempt.",
    attempts: "Each attempt on its own date, shaded by the protocol version it followed (the strongest colour is the newest).",
    claims: "Claims that rest on the dataset, on the date of their attempt.",
    findings: "Findings of the current attempts, on the date of their attempt."
  };

  function el(name, attrs, parent) {
    var n = document.createElementNS(NS, name);
    for (var k in attrs) n.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(n);
    return n;
  }
  function day(d, year) {
    var t = new Date(d + "T00:00:00Z");
    return t.toLocaleDateString("en-US", { month: "short", day: "numeric", year: year ? "numeric" : undefined, timeZone: "UTC" });
  }
  function niceStep(top, n) {
    var steps = [1, 2, 5, 10, 20, 25, 50, 100, 200, 250, 500, 1000, 2000, 2500, 5000, 10000];
    for (var i = 0; i < steps.length; i++) if (top / steps[i] <= n) return steps[i];
    return steps[steps.length - 1];
  }
  function frame(box, height) {
    box.innerHTML = "";
    var w = Math.max(box.clientWidth, 260), h = height;
    var svg = el("svg", { width: w, height: h, viewBox: "0 0 " + w + " " + h }, box);
    var tip = document.createElement("div"); tip.className = "tip"; tip.hidden = true; box.appendChild(tip);
    return { svg: svg, tip: tip, w: w, h: h, left: 38, right: 14, top: 18, bottom: 26 };
  }
  function axes(f, yMax, step, n, xAt) {
    for (var v = 0; v <= yMax; v += step) {
      var y = f.top + (f.h - f.top - f.bottom) * (1 - v / yMax);
      el("line", { "class": "grid", x1: f.left, x2: f.w - f.right, y1: y, y2: y }, f.svg);
      el("text", { "class": "tick", x: f.left - 6, y: y + 4, "text-anchor": "end" }, f.svg).textContent = v.toLocaleString();
    }
    var every = Math.max(1, Math.ceil(n / Math.max(2, Math.floor((f.w - f.left - f.right) / 70))));
    for (var i = 0; i < n; i++) {
      if (i % every && i !== n - 1) continue;
      if (i !== n - 1 && n - 1 - i < every && i % every === 0 && i !== 0) continue;
      el("text", { "class": "tick", x: xAt(i), y: f.h - 8,
        "text-anchor": i === 0 ? "start" : i === n - 1 ? "end" : "middle" }, f.svg).textContent = day(P.days[i]);
    }
  }
  function place(f, x, y, text) {
    f.tip.textContent = text; f.tip.hidden = false;
    f.tip.style.left = Math.min(Math.max(x - f.tip.offsetWidth / 2, 0), f.w - f.tip.offsetWidth) + "px";
    f.tip.style.top = Math.max(y - f.tip.offsetHeight - 12, 0) + "px";
  }

  // A stacked running total: claims by outcome (reproduced at the bottom, blocked on top), or attempts by
  // protocol version (the oldest at the bottom).
  function drawStacked(S) {
    var rows = P.series[state.subset], n = rows.length, run = {}, f = frame(line, 230), keys = S.keys;
    keys.forEach(function (k) { run[k] = 0; });
    var cum = rows.map(function (r) {
      var c = {}; keys.forEach(function (k) { run[k] += r[k]; c[k] = run[k]; }); return c;
    });
    var totals = cum.map(function (c) { return keys.reduce(function (s, k) { return s + c[k]; }, 0); });
    var top = Math.max(totals[n - 1], 1), step = niceStep(top, 4), yMax = Math.ceil(top / step) * step;
    var x = function (i) { return f.left + i * (f.w - f.left - f.right) / (n - 1); };
    var y = function (v) { return f.top + (f.h - f.top - f.bottom) * (1 - v / yMax); };
    axes(f, yMax, step, n, x);
    var below = cum.map(function () { return 0; });
    keys.forEach(function (k) {
      var upper = cum.map(function (c, i) { return below[i] + c[k]; });
      var pts = upper.map(function (v, i) { return x(i).toFixed(1) + "," + y(v).toFixed(1); });
      for (var i = n - 1; i >= 0; i--) pts.push(x(i).toFixed(1) + "," + y(below[i]).toFixed(1));
      S.paint(el("polygon", { points: pts.join(" ") }, f.svg), k);
      below = upper;
    });
    el("text", { "class": "end-label", x: x(n - 1) - 8, y: y(totals[n - 1]) - 9, "text-anchor": "end" }, f.svg)
      .textContent = totals[n - 1].toLocaleString();
    var cross = el("line", { "class": "cross", y1: f.top, y2: f.h - f.bottom, visibility: "hidden" }, f.svg);
    var half = (f.w - f.left - f.right) / (n - 1) / 2;
    cum.forEach(function (c, i) {
      var x0 = Math.max(f.left, x(i) - half), x1 = Math.min(f.w - f.right, x(i) + half);
      var hit = el("rect", { "class": "hit", x: x0, y: f.top, width: x1 - x0, height: f.h - f.top - f.bottom }, f.svg);
      var show = function () {
        cross.setAttribute("x1", x(i)); cross.setAttribute("x2", x(i)); cross.setAttribute("visibility", "visible");
        var parts = keys.filter(function (k) { return c[k]; })
          .map(function (k) { return c[k].toLocaleString() + " " + S.label(k); });
        place(f, x(i), y(totals[i]), day(P.days[i], true) + ": " + totals[i].toLocaleString() + " in all" +
          (parts.length ? " (" + parts.join(", ") + ")" : ""));
      };
      hit.addEventListener("mouseenter", show); hit.addEventListener("touchstart", show, { passive: true });
    });
    f.svg.addEventListener("mouseleave", function () { cross.setAttribute("visibility", "hidden"); f.tip.hidden = true; });
    f.svg.setAttribute("role", "img");
    f.svg.setAttribute("aria-label", P.metrics[state.metric] + ": " + totals[n - 1] + " by " + day(P.days[n - 1], true) + ", " +
      keys.filter(function (k) { return cum[n - 1][k]; })
        .map(function (k) { return cum[n - 1][k] + " " + S.label(k); }).join(", "));
    document.getElementById("progress-title").textContent = P.metrics[state.metric] + " over time";
  }

  function drawLine() {
    var S = stackOf(state.metric);
    if (S) return drawStacked(S);
    var rows = P.series[state.subset], m = state.metric, total = 0;
    var values = rows.map(function (r) { total += r[m]; return total; });
    var f = frame(line, 230), n = values.length, top = Math.max(values[n - 1], 1);
    var step = niceStep(top, 4), yMax = Math.ceil(top / step) * step;
    var x = function (i) { return f.left + i * (f.w - f.left - f.right) / (n - 1); };
    var y = function (v) { return f.top + (f.h - f.top - f.bottom) * (1 - v / yMax); };
    axes(f, yMax, step, n, x);
    var pts = values.map(function (v, i) { return x(i).toFixed(1) + "," + y(v).toFixed(1); }).join(" ");
    el("polygon", { "class": "wash", points: x(0) + "," + y(0) + " " + pts + " " + x(n - 1) + "," + y(0) }, f.svg);
    el("polyline", { "class": "line", points: pts }, f.svg);
    el("circle", { "class": "end", cx: x(n - 1), cy: y(values[n - 1]), r: 4 }, f.svg);
    el("text", { "class": "end-label", x: x(n - 1) - 8, y: y(values[n - 1]) - 9, "text-anchor": "end" }, f.svg)
      .textContent = values[n - 1].toLocaleString();
    var cross = el("line", { "class": "cross", y1: f.top, y2: f.h - f.bottom, visibility: "hidden" }, f.svg);
    var dot = el("circle", { "class": "focus", r: 4, visibility: "hidden" }, f.svg);
    var half = (f.w - f.left - f.right) / (n - 1) / 2;
    values.forEach(function (v, i) {
      var x0 = Math.max(f.left, x(i) - half), x1 = Math.min(f.w - f.right, x(i) + half);
      var hit = el("rect", { "class": "hit", x: x0, y: f.top, width: x1 - x0, height: f.h - f.top - f.bottom }, f.svg);
      var show = function () {
        cross.setAttribute("x1", x(i)); cross.setAttribute("x2", x(i)); cross.setAttribute("visibility", "visible");
        dot.setAttribute("cx", x(i)); dot.setAttribute("cy", y(v)); dot.setAttribute("visibility", "visible");
        place(f, x(i), y(v), day(P.days[i], true) + ": " + v.toLocaleString() + " in all, " +
          rows[i][m].toLocaleString() + " new that day");
      };
      hit.addEventListener("mouseenter", show); hit.addEventListener("touchstart", show, { passive: true });
    });
    f.svg.addEventListener("mouseleave", function () {
      cross.setAttribute("visibility", "hidden"); dot.setAttribute("visibility", "hidden"); f.tip.hidden = true;
    });
    f.svg.setAttribute("role", "img");
    f.svg.setAttribute("aria-label", P.metrics[m] + ": " + values[n - 1] + " by " + day(P.days[n - 1], true));
    document.getElementById("progress-title").textContent = P.metrics[m] + " over time";
  }

  // What is new each day in the chosen measure; claims are stacked by outcome, attempts by protocol version.
  function drawColumns() {
    var rows = P.series[state.subset], n = rows.length, f = frame(cols, 230), m = state.metric;
    var S = stackOf(m), stacked = !!S, keys = stacked ? S.keys : [m];
    var paint = function (node, k) { if (stacked) S.paint(node, k); else node.setAttribute("class", "seg-bar"); };
    var label = function (k) { return stacked ? S.label(k) : P.metrics[m].toLowerCase(); };
    var sums = rows.map(function (r) { return keys.reduce(function (s, k) { return s + r[k]; }, 0); });
    var top = Math.max.apply(null, sums.concat([1])), step = niceStep(top, 4), yMax = Math.ceil(top / step) * step;
    var band = (f.w - f.left - f.right) / n, bw = Math.min(24, band * 0.7);
    var x = function (i) { return f.left + band * (i + 0.5); };
    var y = function (v) { return f.top + (f.h - f.top - f.bottom) * (1 - v / yMax); };
    axes(f, yMax, step, n, x);
    rows.forEach(function (r, i) {
      var base = 0, g = el("g", {}, f.svg), drawn = keys.filter(function (k) { return r[k]; });
      drawn.forEach(function (k, j) {
        var y0 = y(base), y1 = y(base + r[k]), hgt = Math.max(y0 - y1 - (j < drawn.length - 1 ? 2 : 0), 1);
        var isTop = j === drawn.length - 1, rx = Math.min(4, bw / 2, hgt / 2);
        var d = isTop
          ? "M" + (x(i) - bw / 2) + "," + y0 + "V" + (y0 - hgt + rx) + "Q" + (x(i) - bw / 2) + "," + (y0 - hgt) + " " + (x(i) - bw / 2 + rx) + "," + (y0 - hgt) +
            "H" + (x(i) + bw / 2 - rx) + "Q" + (x(i) + bw / 2) + "," + (y0 - hgt) + " " + (x(i) + bw / 2) + "," + (y0 - hgt + rx) + "V" + y0 + "Z"
          : "M" + (x(i) - bw / 2) + "," + y0 + "V" + (y0 - hgt) + "H" + (x(i) + bw / 2) + "V" + y0 + "Z";
        paint(el("path", { d: d }, g), k);
        base += r[k];
      });
      var hit = el("rect", { "class": "hit", x: f.left + band * i, y: f.top, width: band, height: f.h - f.top - f.bottom }, f.svg);
      var show = function () {
        var parts = keys.filter(function (k) { return r[k]; })
          .map(function (k) { return r[k].toLocaleString() + " " + label(k); });
        place(f, x(i), y(sums[i]), day(P.days[i], true) + ": " + (parts.length ? parts.join(", ") : "none") +
          (stacked || !parts.length ? "" : " new"));
      };
      hit.addEventListener("mouseenter", show); hit.addEventListener("touchstart", show, { passive: true });
    });
    f.svg.addEventListener("mouseleave", function () { f.tip.hidden = true; });
    f.svg.setAttribute("role", "img");
    var title = m === "claims" ? "Outcomes of claims tested, by day"
      : stacked ? P.metrics[m] + " by protocol version, new each day" : P.metrics[m] + ", new each day";
    f.svg.setAttribute("aria-label", title);
    document.getElementById("progress-day-title").textContent = title;
    document.getElementById("progress-day-note").textContent = DAY_NOTES[m] || "";
    var totals = {};
    keys.forEach(function (k) { totals[k] = rows.reduce(function (s, r) { return s + r[k]; }, 0); });
    document.getElementById("progress-legend").innerHTML = !stacked ? "" : '<ul class="legend compact" style="margin-top:8px">' +
      keys.filter(function (k) { return totals[k]; }).map(function (k) {
        return "<li>" + S.swatch(k) + "<strong>" + totals[k].toLocaleString() + "</strong> " + S.label(k) + "</li>";
      }).join("") + "</ul>";
  }

  function drawTiles() {
    var rows = P.series[state.subset], recent = rows.slice(-7);
    root.querySelectorAll(".tile.metric").forEach(function (t) {
      var m = t.dataset.metric;
      var total = rows.reduce(function (s, r) { return s + r[m]; }, 0);
      var week = recent.reduce(function (s, r) { return s + r[m]; }, 0);
      t.querySelector(".n").textContent = total.toLocaleString();
      t.querySelector(".delta").textContent = week ? "+" + week.toLocaleString() + " in the last 7 days" : "none in the last 7 days";
      t.setAttribute("aria-pressed", String(m === state.metric));
    });
    root.querySelectorAll("[data-subset]").forEach(function (b) {
      b.setAttribute("aria-pressed", String(b.dataset.subset === state.subset));
    });
  }

  function draw() { drawTiles(); drawLine(); drawColumns(); }
  root.querySelectorAll(".tile.metric").forEach(function (t) {
    t.addEventListener("click", function () { state.metric = t.dataset.metric; draw(); });
  });
  root.querySelectorAll("[data-subset]").forEach(function (b) {
    b.addEventListener("click", function () { state.subset = b.dataset.subset; draw(); });
  });
  var timer;
  window.addEventListener("resize", function () { clearTimeout(timer); timer = setTimeout(draw, 120); });
  draw();
})();
