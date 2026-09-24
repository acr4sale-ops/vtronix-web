// Vercel serverless function: emails contact form submissions via Resend.
//
// Environment variables (Vercel → Project → Settings → Environment Variables):
//   RESEND_API_KEY  required  API key from resend.com
//   CONTACT_TO      optional  recipient, defaults to sales@vtronix.com
//   CONTACT_FROM    optional  sender on a Resend-verified domain,
//                             defaults to "Vtronix Website <website@vtronix.com>"

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

const LIMITS = { fname: 100, lname: 100, email: 254, message: 5000 };

function escapeHtml(value) {
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

function clean(value, max) {
  return typeof value === "string" ? value.trim().slice(0, max) : "";
}

module.exports = async function handler(req, res) {
  if (req.method !== "POST") {
    res.setHeader("Allow", "POST");
    return res.status(405).json({ ok: false, error: "Method not allowed" });
  }

  const body = req.body && typeof req.body === "object" ? req.body : {};

  // Honeypot: real visitors never see or fill this field. Pretend success so
  // bots get no signal.
  if (clean(body.website, 200)) {
    return res.status(200).json({ ok: true });
  }

  const fname = clean(body.fname, LIMITS.fname);
  const lname = clean(body.lname, LIMITS.lname);
  const email = clean(body.email, LIMITS.email);
  const message = clean(body.message, LIMITS.message);

  if (!EMAIL_RE.test(email)) {
    return res.status(400).json({ ok: false, error: "A valid email address is required." });
  }

  const apiKey = process.env.RESEND_API_KEY;
  if (!apiKey) {
    console.error("contact: RESEND_API_KEY is not set");
    return res.status(500).json({ ok: false, error: "Email is not configured." });
  }

  const to = process.env.CONTACT_TO || "sales@vtronix.com";
  const from = process.env.CONTACT_FROM || "Vtronix Website <website@vtronix.com>";
  const name = [fname, lname].filter(Boolean).join(" ") || "(not given)";

  const rows = [
    ["Name", name],
    ["Email", email],
    ["Message", message || "(no message)"]
  ];

  const html =
    '<h2 style="font-family:Arial,sans-serif;">New message from the Vtronix website</h2>' +
    '<table cellpadding="8" style="font-family:Arial,sans-serif;border-collapse:collapse;">' +
    rows
      .map(function (row) {
        return (
          '<tr><th align="left" valign="top" style="border-bottom:1px solid #ddd;">' +
          row[0] +
          '</th><td style="border-bottom:1px solid #ddd;white-space:pre-wrap;">' +
          escapeHtml(row[1]) +
          "</td></tr>"
        );
      })
      .join("") +
    "</table>";

  const text = rows
    .map(function (row) {
      return row[0] + ": " + row[1];
    })
    .join("\n\n");

  try {
    const response = await fetch("https://api.resend.com/emails", {
      method: "POST",
      headers: {
        Authorization: "Bearer " + apiKey,
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        from: from,
        to: [to],
        reply_to: email,
        subject: "New website message from " + name,
        html: html,
        text: text
      })
    });

    if (!response.ok) {
      console.error("contact: Resend error", response.status, await response.text());
      return res.status(502).json({ ok: false, error: "Could not send email." });
    }

    return res.status(200).json({ ok: true });
  } catch (err) {
    console.error("contact: request to Resend failed", err);
    return res.status(502).json({ ok: false, error: "Could not send email." });
  }
};
