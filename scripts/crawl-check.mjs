import { chromium } from 'playwright-core';

const base = process.argv[2] || 'http://localhost:3210';
const browser = await chromium.launch();
const page = await browser.newPage();

const seeds = [
  '/', '/factory', '/about', '/links', '/contact-us', '/category/all-products',
  '/custom-controls', '/capabilities', '/brands', '/certifications',
  '/applications', '/documentation', '/request-a-quote',
  '/warranty-returns', '/privacy', '/terms', '/accessibility',
  '/product-page/w100-1', '/product-page/th6210u2001', '/product-page/econo3-001-obsolete',
];

const allErrors = [];
const visitedLinks = new Set();

for (const seed of seeds) {
  const consoleErrors = [];
  page.removeAllListeners('console');
  page.removeAllListeners('pageerror');
  page.on('console', (msg) => { if (msg.type() === 'error') consoleErrors.push(msg.text()); });
  page.on('pageerror', (e) => consoleErrors.push(String(e)));

  const resp = await page.goto(base + seed, { waitUntil: 'networkidle' });
  const status = resp ? resp.status() : 'no response';
  if (status !== 200) allErrors.push(`${seed}: page itself returned ${status}`);

  // Collect internal links on this page
  const links = await page.$$eval('a[href]', (as) =>
    as.map((a) => a.getAttribute('href')).filter((h) => h && h.startsWith('/'))
  );
  links.forEach((l) => visitedLinks.add(l));

  if (consoleErrors.length) {
    allErrors.push(`${seed}: console/page errors: ${JSON.stringify(consoleErrors)}`);
  }
}

console.log('Seed pages checked:', seeds.length);
console.log('Unique internal links found:', visitedLinks.size);

// Now check every unique internal link resolves to 200 in <=1 hop.
// PDFs (and other downloads) are checked with a plain fetch, since headless
// Chromium's built-in viewer makes page.goto() navigation unreliable for them.
const linkErrors = [];
for (const link of visitedLinks) {
  const url = base + link;
  if (/\.(pdf|zip|jpg|jpeg|png)$/i.test(link)) {
    const resp = await fetch(url).catch(() => null);
    if (!resp || resp.status !== 200) linkErrors.push(`${link}: ${resp ? resp.status : 'ERR'}`);
    continue;
  }
  const resp = await page.goto(url, { waitUntil: 'domcontentloaded' }).catch((e) => null);
  const status = resp ? resp.status() : 'ERR';
  if (status !== 200) linkErrors.push(`${link}: ${status}`);
}

console.log('Broken links:', linkErrors.length);
linkErrors.forEach((e) => console.log(' -', e));

console.log('Page-level errors:', allErrors.length);
allErrors.forEach((e) => console.log(' -', e));

await browser.close();
