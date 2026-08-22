# -*- coding: utf-8 -*-
"""
Shared helpers for the 4D Tech Notes archival scripts.

Requires a valid kb.4d.com session cookie. Get one by:
  1. Log in (or just visit) https://kb.4d.com/ in a browser.
  2. Open DevTools > Application/Storage > Cookies for kb.4d.com.
  3. Copy the value of the `4DSID_KBv20` cookie.
  4. Export it as an environment variable before running any script:
       export KB4D_COOKIE="4DSID_KBv20=<value>"

All scripts in this folder read the cookie from the KB4D_COOKIE env var.
"""
import os
import re
import html as htmllib
import urllib.request
from urllib.parse import quote

KB_BASE = "https://kb.4d.com"


def get_cookie():
    cookie = os.environ.get("KB4D_COOKIE")
    if not cookie:
        raise SystemExit(
            "ERROR: KB4D_COOKIE environment variable not set.\n"
            "Set it with: export KB4D_COOKIE=\"4DSID_KBv20=<your-cookie-value>\"\n"
            "See scripts/common.py docstring for how to obtain the cookie."
        )
    return cookie


def fetch_url(url, timeout=60):
    """GET a URL with the KB session cookie. Returns bytes."""
    safe_url = quote(url, safe=":/?#[]@!$&'()*+,;=%")
    req = urllib.request.Request(
        safe_url,
        headers={"Cookie": get_cookie(), "User-Agent": "Mozilla/5.0"},
    )
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def fetch_asset_page(assetid):
    """Fetch the raw HTML of a kb.4d.com asset detail page."""
    url = f"{KB_BASE}/assetid={assetid}"
    return fetch_url(url, timeout=30).decode("utf-8", errors="replace")


def is_valid_technote(html_body):
    if "Requested asset cannot be found" in html_body:
        return False
    if "Tech Note" not in html_body and "Technical Note" not in html_body:
        return False
    return True


def parse_asset_page(assetid, html_body):
    """Extract metadata + a best-guess download link from an asset page's HTML.

    Returns a dict: id, title, meta, date, link, all_links
    or None if the page is not a valid Tech Note.
    """
    if not is_valid_technote(html_body):
        return None

    title_m = re.search(r'<div class="detailtitle">(.*?)</div>', html_body, re.S)
    meta_m = re.search(r'<div class="detailtitle2">(.*?)</div>', html_body, re.S)
    date_m = re.search(r'<div class="detailtitle3">(.*?)</div>', html_body, re.S)

    title = htmllib.unescape(title_m.group(1).strip()) if title_m else None
    meta = htmllib.unescape(meta_m.group(1).strip()) if meta_m else ""
    date = htmllib.unescape(date_m.group(1).strip()) if date_m else ""

    # Every download-ish href on the page, in rough preference order.
    all_links = re.findall(
        r'href="([^"]+\.(?:zip|pdf|exe|hqx|sit|sea|doc))"', html_body, re.I
    )
    # Normalize protocol-relative / bare-path hrefs seen in some old pages.
    all_links = [KB_BASE + l if l.startswith("/") else l for l in all_links]

    pref_order = ["zip", "pdf", "exe", "sit", "hqx", "sea", "doc"]

    def ext_of(u):
        return u.rsplit(".", 1)[-1].lower()

    best = None
    for ext in pref_order:
        for l in all_links:
            if ext_of(l) == ext:
                best = l
                break
        if best:
            break

    teaser = ""
    body_m = re.search(r'<div class="detailbody">(.*?)</div>', html_body, re.S)
    if body_m:
        t = re.sub(r"<br\s*/?>", "\n", body_m.group(1))
        t = re.sub(r"<[^>]+>", "", t)
        teaser = htmllib.unescape(t).strip()

    return {
        "id": assetid,
        "type": "technote",
        "title": title,
        "meta": meta,
        "date": date,
        "link": best,
        "all_links": all_links,
        "teaser": teaser,
    }
