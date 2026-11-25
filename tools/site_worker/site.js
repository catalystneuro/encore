// Serves encorescience.org from the R2 bucket encore-site, as GitHub Pages served it from the gh-pages branch:
// /folder/ is folder/index.html, /folder redirects to /folder/ when that folder has an index.html, and anything
// else that is not in the bucket is 404.html with status 404.

const SHORT = "public, max-age=300";              // pages and data: a change shows within five minutes
const LONG = "public, max-age=31536000, immutable"; // assets named with their version (?v=)

async function serve(request, env, key, status = 200) {
  const object = await env.SITE.get(key, { onlyIf: request.headers, range: request.headers });
  if (object === null) return null;
  const headers = new Headers();
  object.writeHttpMetadata(headers);
  headers.set("etag", object.httpEtag);
  const url = new URL(request.url);
  headers.set("cache-control", url.searchParams.has("v") && key.startsWith("assets/") ? LONG : SHORT);
  headers.set("x-content-type-options", "nosniff");
  if (!("body" in object)) return new Response(null, { status: 304, headers });   // the client's copy is current
  if (object.range && status === 200 && request.headers.has("range")) {
    headers.set("content-range", `bytes ${object.range.offset}-${object.range.offset + object.range.length - 1}/${object.size}`);
    status = 206;
  }
  return new Response(request.method === "HEAD" ? null : object.body, { status, headers });
}

export default {
  async fetch(request, env) {
    if (request.method !== "GET" && request.method !== "HEAD") {
      return new Response("Method not allowed", { status: 405, headers: { allow: "GET, HEAD" } });
    }
    const url = new URL(request.url);
    // www is the same site: sent to the address without it, as GitHub Pages did.
    if (url.hostname.startsWith("www.")) {
      url.hostname = url.hostname.slice(4);
      return Response.redirect(url.toString(), 301);
    }
    let key;
    try { key = decodeURIComponent(url.pathname).replace(/^\/+/, ""); }
    catch { key = null; }
    if (key !== null && !key.split("/").includes("..")) {
      if (key === "" || key.endsWith("/")) key += "index.html";
      const found = await serve(request, env, key);
      if (found) return found;
      // A folder named without its slash, as GitHub Pages does it: any folder, with or without an index.html.
      if (!/\.[A-Za-z0-9]+$/.test(key) && (await env.SITE.list({ prefix: key + "/", limit: 1 })).objects.length) {
        url.pathname += "/";
        return Response.redirect(url.toString(), 301);
      }
    }
    return (await serve(request, env, "404.html", 404)) || new Response("Not found", { status: 404 });
  },
};
