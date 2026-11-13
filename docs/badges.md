# Dataset badges

An archive can show a badge on a dataset's own page that says how many findings were reproduced from that
dataset. The badge links to the dataset's page in the registry.

![Example badge](https://encorescience.org/badge/dandi/000003.svg)

## What the badge counts

The badge shows one number: the findings reproduced from the dataset. A finding counts when all of these are
true:

- It is a claim of a paper that rests on this dataset alone.
- Its outcome is "reproduced". Partial reproductions do not count.
- It comes from a current attempt that an independent verifier has checked.

The number is the total over every paper tested on the dataset. That includes the paper the data were published
with and papers that reuse the data. When more than one paper contributes, the badge also gives the number of
papers, for example "23 findings reproduced · 2 papers".

The badge never shows a ratio, a score, or the claims that did not reproduce. Those are on the dataset's page
and on each paper's page, one click away.

A dataset has a badge only when at least one finding counts. Otherwise there is no badge file.

## Image

Each dataset with a badge has an SVG at:

```
https://encorescience.org/badge/<archive>/<id>.svg
```

For example `https://encorescience.org/badge/dandi/000003.svg`. A dataset without a badge returns 404, so a
page can hide the image when it fails to load.

To show the badge with a link to the dataset's page:

```html
<a href="https://encorescience.org/datasets/dandi/000003/">
  <img src="https://encorescience.org/badge/dandi/000003.svg"
       alt="Encore: 15 findings reproduced, from DANDI:000003"
       onerror="this.parentElement.remove()">
</a>
```

The dataset's page in the registry has a "Badge for this dataset" section with this code filled in.

## JSON

An archive that prefers to draw its own badge can read the same numbers from the dataset's JSON file:

```
https://encorescience.org/api/datasets/<archive>/<id>.json
```

The file allows requests from any origin. Its `badge` field is `null` when the dataset has no badge. Otherwise
it has these fields:

| Field | Meaning |
|---|---|
| `text` | The text on the badge, for example "15 findings reproduced". |
| `reproduced` | The number of findings reproduced, over all papers. |
| `papers` | One entry for each paper that contributes, with the most findings first. |
| `url` | The dataset's page in the registry. Link the badge here. |
| `svg` | The address of the badge image. |
| `alt` | Alternative text for the image. |

Each entry in `papers` has:

| Field | Meaning |
|---|---|
| `byline` | A short name for the paper, for example "Senzai et al. 2017". |
| `title` | The paper's title. |
| `doi` | The paper's DOI. |
| `relation` | `primary` when the dataset holds the paper's own data, `reuses` when the paper reuses it. |
| `reproduced` | The number of the paper's findings reproduced from this dataset. |
| `url` | The paper's page in the registry. |

A dataset that no attempt has used has no JSON file, and the address returns 404.

`https://encorescience.org/data/datasets.json` lists every dataset in one file. Each row has a `badge` field
with the badge's text, or `null`. Use it to find out which datasets have a badge without requesting each one.

## Updates

The badge files are rebuilt with the site, each time an attempt is merged. A badge's number can go up when a
new paper is tested or an attempt is verified. It can go down when a newer attempt replaces an older one.
