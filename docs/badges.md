# Badges

The registry makes two kinds of badge. Both state how many findings were reproduced, and both link back to a page
in the registry.

- **Dataset badges** are for archives. An archive can show one on a dataset's own page.
- **Author badges** are for people. An author can show one on a lab's site or a profile.

## Dataset badges

A dataset badge says how many findings were reproduced from that dataset. It links to the dataset's page in the
registry.

![Example badge](https://encorescience.org/badge/dandi/000003.svg)

### What the badge counts

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

### Image

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

### JSON

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

## Author badges

An author badge says how many findings of a person's papers were reproduced. It links to the person's page in
the registry. A person has a page when an ORCID iD identifies them as an author of a paper or a contributor of a
dataset.

![Example author badge](https://encorescience.org/badge/authors/0000-0002-3100-4800.svg)

### What the badge counts

The count follows the same rule as a dataset badge, over all of the person's papers in the registry:

- Claims that rest on the paper's datasets.
- Outcome "reproduced". Partial reproductions do not count.
- Current attempts that an independent verifier has checked.

When more than one paper contributes, the badge also gives the number of papers, for example
"129 findings reproduced · 11 papers". A person has a badge only when at least one finding counts.

The person's page shows the outcomes of all their papers' claims in one bar, including attempts not yet
verified. The badge's number can therefore be smaller than the "reproduced" number in that bar.

### Image

```
https://encorescience.org/badge/authors/<ORCID iD>.svg
```

The person's page has a "Badge for this page" section with code to paste, as HTML and as Markdown. The Markdown
form works in a profile README on GitHub:

```markdown
[![Encore: 129 findings reproduced, from 11 papers, in the work of György Buzsáki](https://encorescience.org/badge/authors/0000-0002-3100-4800.svg)](https://encorescience.org/authors/0000-0002-3100-4800/)
```

### Styles with all the outcomes

An author can choose between three styles. The first is the badge described above. The other two show every
outcome, not only the findings reproduced.

| Style | Address | What it shows |
|---|---|---|
| Findings reproduced | `badge/authors/<ORCID iD>.svg` | One number: the findings reproduced in full, in verified attempts. |
| All outcomes | `badge/authors/<ORCID iD>-outcomes.svg` | One line with four counts: reproduced, partially reproduced, not reproduced and blocked. |
| Card | `badge/authors/<ORCID iD>-card.svg` | The person's name, the number of claims and papers, the outcomes as one bar, and the four counts. |

![All outcomes](https://encorescience.org/badge/authors/0000-0002-3100-4800-outcomes.svg)

![Card](https://encorescience.org/badge/authors/0000-0002-3100-4800-card.svg)

The two styles with all the outcomes count differently from the first:

- They count every claim of the person's papers in a current attempt, whether or not a verifier has checked the
  attempt. This is the same count as the bar at the top of the person's page.
- "Blocked" means the claim could not be tested, most often because the data it needs are not in the dataset.
- A person has these two styles when at least one of their papers has an attempt, even if nothing was
  reproduced.

The "Badges for this page" section of the person's page shows all three, and gives the code for the one chosen.

### JSON

```
https://encorescience.org/api/authors/<ORCID iD>.json
```

Every person with a page has this file. It allows requests from any origin. Its fields are:

| Field | Meaning |
|---|---|
| `orcid`, `name` | The person's ORCID iD and name. |
| `url` | The person's page in the registry. |
| `badge` | The badge, with the same fields as a dataset's `badge`, or `null`. Each entry in its `papers` list has no `relation` field. |
| `outcome_counts` | The four counts of the styles with all the outcomes, or `null`. |
| `badges` | The address of each style's image (`reproduced`, `outcomes`, `card`), or `null` for a style the person does not have. |
| `papers` | Every paper of theirs in the registry: its key, byline, title and DOI, whether it has been attempted (`status`), its outcome counts, its verification tier and its page. |
| `datasets` | Every dataset that names them as a contributor: its key, label, their roles and its page. |
| `caution` | A sentence to show next to any outcome. |

Each row of `https://encorescience.org/data/authors.json` has a `badge` field with the badge's text, or `null`.

## Updates

The badge files and the JSON files are rebuilt with the site, each time an attempt is merged. A badge's number
can go up when a new paper is tested or an attempt is verified. It can go down when a newer attempt replaces an
older one.
