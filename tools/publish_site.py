"""Publish the built dashboard to the R2 bucket that encorescience.org is served from (site.yml).

    python tools/publish_site.py SITE_DIR [--prefix pr-preview/pr-12/] [--dry-run]

Uploads every file of SITE_DIR whose MD5 differs from the bucket's copy, and deletes the bucket's files under the
prefix that the build no longer makes. Files under pr-preview/ are left alone unless the prefix is inside it, so that
publishing the site keeps the pull requests' previews. A Cloudflare Worker serves the bucket (folder/ is
folder/index.html, as GitHub Pages did).

R2 is reached through its S3-compatible API, with the access key in R2_ACCESS_KEY_ID and R2_SECRET_ACCESS_KEY and
the Cloudflare account in R2_ACCOUNT_ID. The bucket is R2_BUCKET, encore-site by default.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import mimetypes
import os
import sys
from pathlib import Path

TYPES = {".html": "text/html; charset=utf-8", ".css": "text/css; charset=utf-8", ".js": "text/javascript",
         ".json": "application/json", ".svg": "image/svg+xml", ".woff2": "font/woff2", ".png": "image/png",
         ".txt": "text/plain; charset=utf-8", ".xml": "application/xml", ".ipynb": "application/json"}
# Not part of the site: GitHub Pages' own files.
SKIP = {"CNAME", ".nojekyll"}
PREVIEWS = "pr-preview/"
# Uploads at once. A new preview uploads every file of the site, some 13,000 small ones, and at 16 at once that
# took six minutes; R2's S3 API sets no limit that this reaches.
UPLOADS = 64


def content_type(path: Path) -> str:
    return TYPES.get(path.suffix.lower()) or mimetypes.guess_type(path.name)[0] or "application/octet-stream"


def md5(path: Path) -> str:
    return hashlib.md5(path.read_bytes()).hexdigest()


def plan(local: dict[str, str], remote: dict[str, str], prefix: str) -> tuple[list[str], list[str]]:
    """The keys to upload (new or changed) and the keys to delete (in the bucket under the prefix, not in the
    build). Previews are kept unless the prefix is one of them."""
    upload = sorted(k for k, digest in local.items() if remote.get(k) != digest)
    keep_previews = not prefix.startswith(PREVIEWS)
    delete = sorted(k for k in remote if k.startswith(prefix) and k not in local
                    and not (keep_previews and k.startswith(PREVIEWS)))
    return upload, delete


def client():
    import boto3
    from botocore.config import Config
    account = os.environ["R2_ACCOUNT_ID"]
    return boto3.client("s3", endpoint_url=f"https://{account}.r2.cloudflarestorage.com",
                        aws_access_key_id=os.environ["R2_ACCESS_KEY_ID"],
                        aws_secret_access_key=os.environ["R2_SECRET_ACCESS_KEY"],
                        region_name="auto",
                        config=Config(retries={"max_attempts": 8, "mode": "adaptive"}, max_pool_connections=UPLOADS))


def listing(s3, bucket: str, prefix: str) -> dict[str, str]:
    """The bucket's keys under the prefix and their ETags, which are MD5s for files uploaded whole."""
    found = {}
    for page in s3.get_paginator("list_objects_v2").paginate(Bucket=bucket, Prefix=prefix):
        for o in page.get("Contents", []):
            found[o["Key"]] = o["ETag"].strip('"')
    return found


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("site", type=Path)
    ap.add_argument("--prefix", default="", help="publish under this folder of the bucket, such as pr-preview/pr-12/")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    prefix = args.prefix.strip("/") + "/" if args.prefix.strip("/") else ""
    files = {prefix + p.relative_to(args.site).as_posix(): p
             for p in sorted(args.site.rglob("*")) if p.is_file() and p.name not in SKIP}
    local = {k: md5(p) for k, p in files.items()}
    bucket = os.environ.get("R2_BUCKET", "encore-site")
    s3 = client()
    upload, delete = plan(local, listing(s3, bucket, prefix), prefix)
    print(f"{len(local)} files built; {len(upload)} to upload, {len(delete)} to delete, under '{prefix or '/'}'")
    if args.dry_run:
        print("\n".join(f"  upload {k}" for k in upload[:20]) + ("\n" if upload else ""), end="")
        print("\n".join(f"  delete {k}" for k in delete[:20]))
        return 0

    def put(key: str) -> None:
        s3.put_object(Bucket=bucket, Key=key, Body=files[key].read_bytes(), ContentType=content_type(files[key]))

    with concurrent.futures.ThreadPoolExecutor(UPLOADS) as ex:
        list(ex.map(put, upload))
    for i in range(0, len(delete), 1000):
        s3.delete_objects(Bucket=bucket, Delete={"Objects": [{"Key": k} for k in delete[i:i + 1000]], "Quiet": True})
    print(f"Uploaded {len(upload)} and deleted {len(delete)} in {bucket}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
