"""Keyword frequencies of the stimuli of Zhu et al. (2022), from the corpus the paper names.

Zhu, Xu, Lu, Hu et al. (2022), Nature Human Behaviour 6, 1104-1111, doi:10.1038/s41562-022-01334-6.
This uses no data of the dandiset. The Methods ("The Chinese language and stimuli design",
paragraph 3) say "All the keywords were of two characters, and the word frequencies were matched
between CORR (same in SYN-P and SEM ...) and SYN-C ... (https://lingua.mtsu.edu/chinese-computing/)".

Where the inputs come from:

- The sentences are the lists of the paper's Supplementary Information (pages 14 to 17: CORR,
  SYN-P, SYN-C, SEM), fetched from the publisher at `SUPPLEMENT_URL` and checked against
  `SUPPLEMENT_SHA256` (the copy the claims file was written from). Words are separated by "/" in
  the lists; the keyword is word 4 of CORR and SYN-C (the claim's criterion), and word 5 of SYN-P,
  after the inserted adverb.
- The site the paper names (Jun Da, Chinese text computing) gives word-level counts only as
  bigram (two-character string) frequencies, for two sub-corpora, news and general fiction; its
  Modern Chinese list is of single characters. As every keyword has two characters, the bigram
  counts are used. They are read one keyword at a time from the site's bigram search
  (`SEARCH_URL`), which returns the raw count in both sub-corpora. The site has no version, DOI
  or commit, so the counts are as served on the day the notebook runs.
- Counts are turned into frequencies per million with the sub-corpus sizes of Table 6 of the
  technical report the site cites for its lists (Da 2004, `REPORT_URL`), read from the PDF: total
  characters and total bigrams of each sub-corpus. Which sub-corpus, and which total, the paper
  used is not stated; the notebook shows every combination.
"""

from __future__ import annotations

import hashlib
import io
import re
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

import pypdf

SUPPLEMENT_URL = ("https://static-content.springer.com/esm/art%3A10.1038%2Fs41562-022-01334-6/"
                  "MediaObjects/41562_2022_1334_MOESM1_ESM.pdf")
SUPPLEMENT_SHA256 = "2c67e8d334b7f5681bb616cd4ebc87e3d4eaa82a352c1e48da0eaab97788a82a"
LIST_PAGES = {"CORR": 13, "SYN-P": 14, "SYN-C": 15, "SEM": 16}   # 0-based pages of the supplement
SEARCH_URL = "https://lingua.mtsu.edu/chinese-computing/statistics/bigram/search.php"
REPORT_URL = "https://lingua.mtsu.edu/academic/dajun-4thtech.pdf"
SUB_CORPORA = ("news", "fiction")


def _get(url, data=None, timeout=120):
    request = urllib.request.Request(url, data=data, headers={"User-Agent": "encore-reproduction"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read()


def supplement():
    """The supplement's bytes and their SHA-256."""
    raw = _get(SUPPLEMENT_URL)
    return raw, hashlib.sha256(raw).hexdigest()


def sentence_lists(raw):
    """{condition: {sentence number: [words]}} from the supplement's stimulus pages."""
    reader = pypdf.PdfReader(io.BytesIO(raw))
    lists = {}
    for condition, page in LIST_PAGES.items():
        rows = {}
        for line in reader.pages[page].extract_text().splitlines():
            m = re.match(r"\s*(\d+)\s*([^\sA-Za-z]+)", line)
            if m and "/" in m.group(2):
                rows[int(m.group(1))] = m.group(2).split("/")
        lists[condition] = rows
    return lists


def corpus_sizes():
    """Total characters and total bigrams of each sub-corpus, from Table 6 of Da (2004)."""
    text = "\n".join(p.extract_text() for p in pypdf.PdfReader(io.BytesIO(_get(REPORT_URL))).pages)
    table = text[text.index("Table 6 Bigram counts"):text.index("Table 7 Number")]
    sizes = {}
    for name, label in (("news", r"News"), ("fiction", r"fiction\s*")):
        m = re.search(label + r"\s+(\d{7,})\s+(\d+)\s+(\d+)\s+(\d{7,})\s+1\s*-\s*(\d+)", table)
        sizes[name] = {"characters": int(m.group(1)), "distinct_characters": int(m.group(2)),
                       "unique_bigrams": int(m.group(3)), "bigrams": int(m.group(4))}
    return sizes, table


def bigram_counts(word):
    """Raw count of a two-character string in the news and the general fiction sub-corpora (0 when absent)."""
    data = urllib.parse.urlencode({"Which": word, "Submit2": "Submit"}, encoding="gb2312").encode()
    page = _get(SEARCH_URL, data).decode("gb18030")
    text = re.sub(r"<[^>]*>", " ", page)
    text = text[text.index("Bigram searched:"):]
    if word not in text.split("Corpus")[0]:
        raise ValueError(f"the search page does not echo {word}")
    out = {"absent_from": []}
    for name, label in (("news", "News"), ("fiction", "General fiction")):
        m = re.search(label + r"\s+(\d+|\(No info\.\))\s", text)
        if m is None:
            raise ValueError(f"no {label} row for {word}")
        # the site answers "(No info.)" for a string that does not occur in a sub-corpus
        out[name] = 0 if m.group(1).startswith("(") else int(m.group(1))
        if m.group(1).startswith("("):
            out["absent_from"].append(name)
    return out


def all_counts(words, workers: int = 4):
    """{word: counts} for every distinct word, read from the site's bigram search."""
    words = sorted(set(words))
    with ThreadPoolExecutor(workers) as pool:
        return dict(zip(words, pool.map(bigram_counts, words)))
