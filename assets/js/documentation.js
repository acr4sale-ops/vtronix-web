document.addEventListener("DOMContentLoaded", function () {
  var tbody = document.getElementById("docsTableBody");
  var countEl = document.getElementById("docsCount");
  var searchInput = document.getElementById("docsSearch");
  if (!tbody) return;

  var categoryLabels = {};
  (window.VTRONIX_CATEGORIES || []).forEach(function (c) {
    categoryLabels[c.slug] = c.label;
  });

  var categoriesBySku = {};
  Object.keys(window.VTRONIX_CATEGORY_ORDER || {}).forEach(function (catSlug) {
    (VTRONIX_CATEGORY_ORDER[catSlug] || []).forEach(function (sku) {
      categoriesBySku[sku] = categoriesBySku[sku] || [];
      if (categoriesBySku[sku].indexOf(catSlug) === -1) categoriesBySku[sku].push(catSlug);
    });
  });

  var pdfIcon =
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" style="width:14px;height:14px;"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/><line x1="9" y1="13" x2="15" y2="13"/><line x1="9" y1="17" x2="15" y2="17"/></svg>';

  var rows = VTRONIX_PRODUCTS.map(function (p) {
    var detail = (window.VTRONIX_PRODUCT_DETAILS || {})[p.sku];
    var docs = (window.VTRONIX_DOCS || {})[p.sku] || [];
    var cats = (categoriesBySku[p.sku] || []).filter(function (c) { return c !== "all-products"; });
    return {
      sku: p.sku,
      brand: p.brand,
      discontinued: !!p.discontinued,
      slug: detail ? detail.slug : null,
      categoryLabel: cats.map(function (c) { return categoryLabels[c] || c; }).join(", "),
      docs: docs,
    };
  });

  function renderRow(r) {
    var nameCell = r.slug
      ? '<a href="/product-page/' + r.slug + '">' + r.sku + "</a>"
      : r.sku;
    var statusBadge = r.discontinued
      ? '<span style="color:#9a2020; font-weight:600;">Discontinued</span>'
      : '<span style="color:#2a7d2a;">Active</span>';
    var docLinks = r.docs.length
      ? r.docs
          .map(function (d) {
            return '<a href="' + d.href + '" target="_blank" rel="noopener" style="display:inline-flex; align-items:center; gap:4px; margin:0 10px 4px 0; font-size:13px;">' + pdfIcon + " " + d.label + "</a>";
          })
          .join("")
      : '<span style="color:#999;">&ndash;</span>';
    return (
      "<tr>" +
      '<td data-label="Model" style="font-weight:600;">' + nameCell + "</td>" +
      '<td data-label="Brand">' + r.brand + "</td>" +
      '<td data-label="Category" style="color:#555;">' + (r.categoryLabel || "&ndash;") + "</td>" +
      '<td data-label="Status">' + statusBadge + "</td>" +
      '<td data-label="Documents">' + docLinks + "</td>" +
      "</tr>"
    );
  }

  function render() {
    var q = (searchInput.value || "").trim().toLowerCase();
    var filtered = rows.filter(function (r) {
      return !q || r.sku.toLowerCase().indexOf(q) !== -1 || r.brand.toLowerCase().indexOf(q) !== -1;
    });
    tbody.innerHTML = filtered.map(renderRow).join("");
    countEl.textContent = filtered.length + (filtered.length === 1 ? " product" : " products");
  }

  searchInput.addEventListener("input", render);
  render();
});
