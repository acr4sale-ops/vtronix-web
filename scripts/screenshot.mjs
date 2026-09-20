import { chromium } from 'playwright-core';
import fs from 'fs';

const base = process.argv[2]; // e.g. http://localhost:8123
const outDir = process.argv[3]; // e.g. /path/to/review/before
const pages = [
  ['/', 'home'],
  ['/factory.html', 'factory'],
  ['/about.html', 'about'],
  ['/links.html', 'links'],
  ['/contact-us.html', 'contact-us'],
  ['/products.html', 'all-products'],
  ['/products.html?cat=control-boards', 'category-control-boards'],
  ['/products/w100-1.html', 'product-detail'],
  ['/products/th6210u2001.html', 'product-detail-honeywell'],
  ['/products/econo3-001-obsolete.html', 'product-detail-discontinued'],
  ['/custom-controls.html', 'custom-controls'],
  ['/applications.html', 'applications'],
  ['/applications/air-handlers.html', 'application-detail'],
  ['/documentation.html', 'documentation'],
  ['/request-a-quote.html', 'request-a-quote'],
  ['/capabilities.html', 'capabilities'],
  ['/brands.html', 'brands'],
  ['/certifications.html', 'certifications'],
  ['/warranty-returns.html', 'warranty-returns'],
];
const widths = [1440, 390];

fs.mkdirSync(outDir, { recursive: true });

const browser = await chromium.launch();
for (const width of widths) {
  const page = await browser.newPage({ viewport: { width, height: 1000 } });
  for (const [path, name] of pages) {
    await page.goto(base + path, { waitUntil: 'networkidle' });
    await page.waitForTimeout(300);
    // Trigger scroll-reveal animations by walking down the page first.
    const height = await page.evaluate(() => document.body.scrollHeight);
    for (let y = 0; y < height; y += 400) {
      await page.evaluate((y) => window.scrollTo(0, y), y);
      await page.waitForTimeout(60);
    }
    await page.evaluate(() => window.scrollTo(0, 0));
    await page.waitForTimeout(300);
    const file = `${outDir}/${name}-${width}.png`;
    await page.screenshot({ path: file, fullPage: true });
    console.log('saved', file);
  }
  await page.close();
}
await browser.close();
