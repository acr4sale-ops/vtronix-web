document.addEventListener("DOMContentLoaded", function () {
  var grid = document.getElementById("productGrid");
  var countEl = document.getElementById("resultCount");
  var searchInput = document.getElementById("productSearch");
  var catLinks = document.querySelectorAll(".shop-categories a");

  var params = new URLSearchParams(window.location.search);
  var pathMatch = window.location.pathname.match(/^\/category\/([^/]+)\/?$/);
  var activeCat = (pathMatch && pathMatch[1]) || params.get("cat") || "all-products";

  var icon =
    '<svg viewBox="0 0 24 24" fill="none" stroke="#5b6b78" stroke-width="1.4"><rect x="4" y="4" width="16" height="16" rx="2"/><circle cx="12" cy="12" r="3.2"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M5 5l1.4 1.4M17.6 17.6L19 19M19 5l-1.4 1.4M6.4 17.6L5 19"/></svg>';

  var categoryLabels = {};
  (window.VTRONIX_CATEGORIES || []).forEach(function (c) {
    categoryLabels[c.slug] = c.label;
  });

  var productsBySku = {};
  VTRONIX_PRODUCTS.forEach(function (p) {
    productsBySku[p.sku] = p;
  });

  var categoryOrder = window.VTRONIX_CATEGORY_ORDER || {};
  var brandFilter = "all";
  var brandButtons = document.querySelectorAll(".filter-toggle button");
  var paginationEl = document.getElementById("pagination");
  var PAGE_SIZE = 20;
  var currentPage = 1;

  function isHoneywell(p) {
    return p.brand === "Honeywell";
  }

  function matchesBrandFilter(p) {
    if (brandFilter === "vtronix") return !isHoneywell(p);
    if (brandFilter === "honeywell") return isHoneywell(p);
    return true;
  }

  function setActiveCategoryLink() {
    catLinks.forEach(function (a) {
      a.classList.toggle("active", a.dataset.cat === activeCat);
    });
  }

  function setCategory(cat) {
    activeCat = cat;
    currentPage = 1;
    window.history.replaceState({}, "", "/category/" + activeCat);
    setActiveCategoryLink();
  }

  function matchesQuery(p, q) {
    return !q || p.sku.toLowerCase().indexOf(q) !== -1 || p.brand.toLowerCase().indexOf(q) !== -1;
  }

  function productsInCategory(cat) {
    return (categoryOrder[cat] || [])
      .map(function (sku) {
        return productsBySku[sku];
      })
      .filter(Boolean);
  }

  function filterByCategory(cat, q) {
    return productsInCategory(cat).filter(function (p) {
      return matchesQuery(p, q) && matchesBrandFilter(p);
    });
  }

  function renderCards(items) {
    grid.innerHTML = items
      .map(function (p) {
        var detail = (window.VTRONIX_PRODUCT_DETAILS || {})[p.sku];
        var tag = detail ? "a" : "div";
        var href = detail ? ' href="/product-page/' + detail.slug + '"' : "";
        var media = detail && detail.image
          ? '<img src="' + detail.image + '" alt="' + p.sku + ' product photo" loading="lazy" decoding="async" />'
          : icon;
        return (
          "<" + tag + ' class="product-card' + (isHoneywell(p) ? " product-card--resale" : "") + '"' + href + ">" +
          '<div class="product-thumb">' +
          '<span class="product-tag' + (p.discontinued ? " discontinued" : "") + '">' +
          p.brand +
          "</span>" +
          media +
          "</div>" +
          '<div class="product-info">' +
          '<div class="sku">' + p.sku + (p.discontinued ? " (Discontinued)" : "") + "</div>" +
          '<div class="rule"></div>' +
          "</div>" +
          "</" + tag + ">"
        );
      })
      .join("");

    if (items.length === 0) {
      grid.innerHTML = '<p style="grid-column:1/-1; color:#777;">No products match your search.</p>';
    }
  }

  function renderPagination(total) {
    var totalPages = Math.ceil(total / PAGE_SIZE);
    if (totalPages <= 1) {
      paginationEl.innerHTML = "";
      return;
    }
    if (currentPage > totalPages) currentPage = totalPages;
    var links = [];
    for (var i = 1; i <= totalPages; i++) {
      links.push(
        '<a href="#" data-page="' + i + '"' + (i === currentPage ? ' class="current"' : "") + ">" + i + "</a>"
      );
    }
    paginationEl.innerHTML = links.join("");
    paginationEl.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function (e) {
        e.preventDefault();
        currentPage = parseInt(a.getAttribute("data-page"), 10);
        render();
        grid.scrollIntoView({ behavior: "smooth", block: "start" });
      });
    });
  }

  // Live filtering within the currently selected category. No category switching here —
  // that only happens on an explicit search (Enter / search button), see performSearch().
  function render(items, note) {
    if (!items) items = filterByCategory(activeCat, currentQuery());
    var countText = items.length + (items.length === 1 ? " product" : " products");
    if (note) {
      countText += ' <span style="color:var(--blue-dim); font-weight:600;">— ' + note + "</span>";
    }
    countEl.innerHTML = countText;
    var start = (currentPage - 1) * PAGE_SIZE;
    renderCards(items.slice(start, start + PAGE_SIZE));
    renderPagination(items.length);
  }

  function currentQuery() {
    return (searchInput.value || "").trim().toLowerCase();
  }

  // Explicit search: if nothing matches in the current category, search every category and
  // jump to wherever the match actually lives.
  function performSearch() {
    var q = currentQuery();
    var items = filterByCategory(activeCat, q);

    if (items.length === 0 && q && activeCat !== "all-products") {
      var allMatches = filterByCategory("all-products", q);
      if (allMatches.length > 0) {
        var cats = [];
        allMatches.forEach(function (p) {
          VTRONIX_CATEGORIES.forEach(function (c) {
            if (c.slug === "all-products" || c.slug === "discontinued") return;
            if ((categoryOrder[c.slug] || []).indexOf(p.sku) !== -1 && cats.indexOf(c.slug) === -1) {
              cats.push(c.slug);
            }
          });
        });

        var fromLabel = categoryLabels[activeCat] || activeCat;
        setCategory(cats.length === 1 ? cats[0] : "all-products");
        var toLabel = categoryLabels[activeCat] || "All Products";
        render(allMatches, "no matches in " + fromLabel + ", showing results from " + toLabel);
        return;
      }
    }

    render(items);
  }

  brandButtons.forEach(function (btn) {
    btn.addEventListener("click", function () {
      brandFilter = btn.getAttribute("data-brand");
      currentPage = 1;
      brandButtons.forEach(function (b) { b.classList.toggle("active", b === btn); });
      render();
    });
  });

  catLinks.forEach(function (a) {
    a.addEventListener("click", function (e) {
      e.preventDefault();
      setCategory(a.dataset.cat);
      render();
    });
  });

  searchInput.addEventListener("input", function () {
    currentPage = 1;
    render();
  });

  searchInput.addEventListener("keydown", function (e) {
    if (e.key === "Enter") {
      e.preventDefault();
      performSearch();
    }
  });

  document.getElementById("searchBtn").addEventListener("click", function (e) {
    e.preventDefault();
    performSearch();
  });

  setActiveCategoryLink();
  render();
});
