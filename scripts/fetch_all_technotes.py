# -*- coding: utf-8 -*-
"""
Rebuild the master list of ALL Tech Notes on kb.4d.com using the site's
internal search API (not by guessing asset-ID ranges).

kb.4d.com is a single-page app backed by a REST-like search endpoint:

  POST https://kb.4d.com/search
    body: mode=rest&query=&type=Tech Notes&version=&product=&time=&pp=20&cc=
    -> JSON: {"__COUNT": N, "__SENT": 20, "__FIRST": 1, "__ASSETS": [...]}

  POST https://kb.4d.com/result
    body: mode=rest&nav=pnext&pos=<N>
    -> next page of 20, following the same session

Pagination requires session-cookie continuity: the server sets a `qstring`
cookie on the /search call that must be echoed back on every /result call,
in addition to the static 4DSID_KBv20 auth cookie. This script uses
Python's http.cookiejar to handle that automatically.

Usage:
    export KB4D_COOKIE="4DSID_KBv20=<value>"
    python3 scripts/fetch_all_technotes.py > technotes/all_technotes.json

Output: a JSON array of {recnum, assetid, title, publishedDate, productName,
productVersion, ...} for every Tech Note currently listed on kb.4d.com,
sorted as returned by the API (newest first).
"""
import http.cookiejar
import json
import sys
import urllib.request

from common import KB_BASE, get_cookie

STATIC_COOKIE_NAME = "4DSID_KBv20"


def make_opener():
    cookie = get_cookie()
    jar = http.cookiejar.CookieJar()
    # Seed the static auth cookie into the jar so it survives redirects
    # and merges correctly with the server-set dynamic `qstring` cookie.
    name, _, value = cookie.partition("=")
    c = http.cookiejar.Cookie(
        version=0, name=name.strip(), value=value.strip(),
        port=None, port_specified=False,
        domain="kb.4d.com", domain_specified=True, domain_initial_dot=False,
        path="/", path_specified=True,
        secure=False, expires=None, discard=True,
        comment=None, comment_url=None, rest={},
    )
    jar.set_cookie(c)
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
    opener.addheaders = [("User-Agent", "Mozilla/5.0")]
    return opener


def post(opener, path, body):
    data = body.encode("utf-8")
    req = urllib.request.Request(
        f"{KB_BASE}{path}", data=data,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    with opener.open(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def fetch_all():
    opener = make_opener()
    body = "mode=rest&query=&type=Tech Notes&version=&product=&time=&pp=20&cc="
    result = post(opener, "/search", body)
    assets = list(result.get("__ASSETS", []))
    total = result.get("__COUNT", 0)
    pos = result.get("__FIRST", 1) + result.get("__SENT", 0) - 1

    while len(assets) < total:
        body = f"mode=rest&nav=pnext&pos={pos}"
        result = post(opener, "/result", body)
        batch = result.get("__ASSETS", [])
        if not batch:
            break
        assets.extend(batch)
        pos = result.get("__FIRST", pos) + result.get("__SENT", 0) - 1
        print(f"  fetched {len(assets)}/{total}", file=sys.stderr)

    return assets


if __name__ == "__main__":
    assets = fetch_all()
    print(f"Total Tech Notes found: {len(assets)}", file=sys.stderr)
    json.dump(assets, sys.stdout, indent=2)
