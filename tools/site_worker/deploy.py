"""Deploy the Worker that serves encorescience.org from the R2 bucket encore-site.

    CLOUDFLARE_API_TOKEN=... python tools/site_worker/deploy.py

The Worker (site.js) is attached to encorescience.org, www.encorescience.org and next.encorescience.org as custom
domains, on the CatalystNeuro Cloudflare account. It changes rarely, so it is deployed by hand: this uploads site.js
with the bucket bound as SITE. The token needs Workers Scripts: Edit on the account.
"""

from __future__ import annotations

import json
import os
import sys
import urllib.request
import uuid
from pathlib import Path

ACCOUNT = "008449f3dd09bf4fea5f86ee82695b6e"
SCRIPT, BUCKET = "encore-site", "encore-site"


def main() -> int:
    source = (Path(__file__).parent / "site.js").read_bytes()
    meta = {"main_module": "site.js", "compatibility_date": "2026-11-01",
            "bindings": [{"type": "r2_bucket", "name": "SITE", "bucket_name": BUCKET}]}
    b = "----encore" + uuid.uuid4().hex
    body = (f'--{b}\r\nContent-Disposition: form-data; name="metadata"\r\nContent-Type: application/json\r\n\r\n'
            + json.dumps(meta) + f'\r\n--{b}\r\nContent-Disposition: form-data; name="site.js"; filename="site.js"'
            '\r\nContent-Type: application/javascript+module\r\n\r\n').encode() + source + f"\r\n--{b}--\r\n".encode()
    req = urllib.request.Request(
        f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/workers/scripts/{SCRIPT}", method="PUT", data=body,
        headers={"Authorization": f"Bearer {os.environ['CLOUDFLARE_API_TOKEN']}",
                 "Content-Type": f"multipart/form-data; boundary={b}"})
    with urllib.request.urlopen(req, timeout=120) as r:
        ok = json.load(r).get("success")
    print("deployed" if ok else "not deployed")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
