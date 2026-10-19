// The overview's dashboard: totals for the chosen dandisets, a running total of one measure, and the outcomes
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
  var state = { subset: "all", metric: "dandisets" };
  var root = document.querySelector(".progress");
  var line = document.getElementById("progress-line"), cols = document.getElementById("progress-outcomes");
  var outcomeKeys = Object.keys(P.outcomes);

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

  function drawLine() {
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

  function drawColumns() {
    var rows = P.series[state.subset], n = rows.length, f = frame(cols, 230);
    var sums = rows.map(function (r) { return outcomeKeys.reduce(function (s, k) { return s + r[k]; }, 0); });
    var top = Math.max.apply(null, sums.concat([1])), step = niceStep(top, 4), yMax = Math.ceil(top / step) * step;
    var band = (f.w - f.left - f.right) / n, bw = Math.min(24, band * 0.7);
    var x = function (i) { return f.left + band * (i + 0.5); };
    var y = function (v) { return f.top + (f.h - f.top - f.bottom) * (1 - v / yMax); };
    axes(f, yMax, step, n, x);
    rows.forEach(function (r, i) {
      var base = 0, g = el("g", {}, f.svg), drawn = outcomeKeys.filter(function (k) { return r[k]; });
      drawn.forEach(function (k, j) {
        var y0 = y(base), y1 = y(base + r[k]), hgt = Math.max(y0 - y1 - (j < drawn.length - 1 ? 2 : 0), 1);
        var isTop = j === drawn.length - 1, rx = Math.min(4, bw / 2, hgt / 2);
        var d = isTop
          ? "M" + (x(i) - bw / 2) + "," + y0 + "V" + (y0 - hgt + rx) + "Q" + (x(i) - bw / 2) + "," + (y0 - hgt) + " " + (x(i) - bw / 2 + rx) + "," + (y0 - hgt) +
            "H" + (x(i) + bw / 2 - rx) + "Q" + (x(i) + bw / 2) + "," + (y0 - hgt) + " " + (x(i) + bw / 2) + "," + (y0 - hgt + rx) + "V" + y0 + "Z"
          : "M" + (x(i) - bw / 2) + "," + y0 + "V" + (y0 - hgt) + "H" + (x(i) + bw / 2) + "V" + y0 + "Z";
        el("path", { "class": "seg-" + P.outcomes[k].css, d: d }, g);
        base += r[k];
      });
      var hit = el("rect", { "class": "hit", x: f.left + band * i, y: f.top, width: band, height: f.h - f.top - f.bottom }, f.svg);
      var show = function () {
        var parts = outcomeKeys.filter(function (k) { return r[k]; })
          .map(function (k) { return r[k] + " " + P.outcomes[k].label.toLowerCase(); });
        place(f, x(i), y(sums[i]), day(P.days[i], true) + ": " + (parts.length ? parts.join(", ") : "no claims"));
      };
      hit.addEventListener("mouseenter", show); hit.addEventListener("touchstart", show, { passive: true });
    });
    f.svg.addEventListener("mouseleave", function () { f.tip.hidden = true; });
    f.svg.setAttribute("role", "img");
    f.svg.setAttribute("aria-label", "Outcomes of claims tested, by day");
    var totals = {};
    outcomeKeys.forEach(function (k) { totals[k] = rows.reduce(function (s, r) { return s + r[k]; }, 0); });
    document.getElementById("progress-legend").innerHTML = '<ul class="legend compact" style="margin-top:8px">' +
      outcomeKeys.map(function (k) {
        return '<li><span class="swatch ' + P.outcomes[k].css + '" aria-hidden="true"></span><strong>' +
          totals[k].toLocaleString() + "</strong> " + P.outcomes[k].label.toLowerCase() + "</li>";
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
