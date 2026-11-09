I wrote the claims file for DANDI:001619: `claims/001619/10.1101-2025.01.27.635041.yaml`. The checker passes with 0 problems. Nothing is committed.

**Text read.** The bioRxiv preprint, version 1 (posted 27 January 2025): main text, the legends of Figures 1 to 5, the Methods, and the supplement with the legends of Extended Data Figures 1 to 12. That supplement was missing in the earlier run, which is why no claims were written then. The two display equations (tuning curve and VAF) are missing from the text, but the words around them name every term. No later version was read.

**Code read.** The paper only says code "will be deposited upon publication". The dandiset description names the analysis code repository, NuoLiLabBCM/KakuEtAl2025, and I read it at commit fbc0abe. It settles these Methods details:
- the unit and trial filters, and lick and inspiration onsets;
- the lick-breath timing analyses (Fig 1f-i, 4e-f);
- the swallow detector and the swallow modulation index;
- phase tuning and the modulation index;
- the activity maps.

It has no statistical tests, and nothing for the GLM, the autoencoder, cross-correlation, the cued-task or photostimulation analyses, or the rats. Its Kuramoto simulations are not described in the preprint, so I didn't use them.

**Counts.**
- 48 claims: 47 findings and one link check.
- 46 claims have quotes. The link check has none, and one is `inferred` (the Extended Data Fig 10 site counts, spread over three legends).
- 13 claims have statistics.
- All 48 have criteria.

**Where the Methods and code disagree.** The Methods version is the main reading; the code's choice is shown as a variant.
- **V1, quality filter:** the code drops the drift-metric threshold.
- **V2, phase filter:** the Methods say "4-pole Butterworth", read as scipy order 4 or order 2; the code uses order 5.
- **V3, significance of the modulation index:** the Methods use 1000 resamples and a rank-sum test; the code uses 100 resamples each side and a one-sided Mann-Whitney. Readings: the code's scheme with 1000 resamples, or the measured index ranked against 1000 random-phase indices.
- **V4, swallow index normalisation:** the mean rate in the swallow window (code), or the PSTH peak.

**Details left open, with the readings named.**
- **O1, tuned-unit threshold:** index > 0.6 (Results) or > 0.9 (Extended Data Fig 8 and the code), with or without the p threshold.
- **O2, recordings for Fig 4e-f:** all sessions (code) or only the 43 simultaneous recordings.
- **O3, regions the Allen atlas doesn't label** (preBötzinger complex, posterior-dorsal or posterior-ventral IRN): within 300 or 500 µm below the nucleus ambiguus, or half-splits of IRN.
- **O4, statistical unit for Fig 1g and 1i:** sessions or mice.
- **O5, ranking of swallow events for Fig 1l and 1n:** by the interval spanning the swallow (code), by the interval before it (text), or all events; plus session means.
- **O6, cross-correlation:** the Results cite a Methods section that doesn't exist. Readings: 5 or 10 ms bins, a trial-shuffle 95% band, and significance with or without Bonferroni.
- **O7, the Kuiper test's second sample:** random-time phases, or phases at −500 ms.
- **O8, GLM:** L1 weight, which lag, and log or logit link.
- **O9, lick angle:** against the jaw at rest (Methods) or the midline (legend).
- Also: how the Fig 1d frequencies were computed, the denominator of 18,485, "position-shuffled", "non-licking units", and the Fig 5g bootstrap.

The paper reports no test for several qualitative claims (locations, ipsilateral preference, preferred phases, Fig 4b-f). Their criteria use a standard test, named in the file as a choice made here.

**Missing from the paper.**
- There is no Figure 5g legend, although the Results cite 5g.
- There is no Methods section for cross-correlation, lick-breath timing or Kuiper entrainment; the code covers the timing analyses only.
- Extended Data Fig 4c gives 19,000 units, against 20,300 in the main text; both are recorded as readings.
- The O5(a) ranking taken from the code favours a positive cycle-0 change, and the file says so.
- The premotor tracing comes from reference 43 (Takatoh et al. 2021) and has no archive identifier. Fig 3a is marked `elsewhere`, and Fig 3b uses outside data (`with_inputs`).
- The autoencoder claims need the raw videos.
