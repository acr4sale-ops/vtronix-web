# Vtronix V2 launch checklist

1. Lower web-record DNS TTL one day before cutover. Leave MX and all mail records unchanged.
2. Set `www.vtronix.com` as the Vercel primary domain and redirect the apex host to `www`.
3. Verify SSL and every mapped Wix URL returns either 200 or one 301 followed by 200.
4. Confirm `robots.txt`, `sitemap.xml`, canonical tags and analytics are production-ready.
5. Submit the production sitemap through Google Search Console.
