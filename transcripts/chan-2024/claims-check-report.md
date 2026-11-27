The claims file for chan-2024 is fit for an attempt. I corrected 12 claims from the paper and recorded the changes under `checks` with `ready: true`. Only `claims/chan-2024.yaml` was changed; nothing is committed.

**Checker result** (the same before and after my edits): `claims/chan-2024.yaml: 27 claims, 26 quotes, 26 statistical values, 0 problems`

**Changes, by claim**
- **fig1d-assemblage-day-night:** the statement said night visitors are mainly hawkmoths, but Table S2 gives 117 of 276 night visits (42%). It now uses the paper's words: particularly nocturnal hawkmoths and diurnal bees.
- **fig1e-groups:** added the Table S4 p for nocturnal against diurnal exclusion (0.4645). The letters join that pair, but its p was missing.
- **fig2a-gcead-monoterpenes:** the criterion now says the 3 SD and 1 min thresholds and "majority of antennae" are standard choices, not the paper's. I added a reading of "especially sensitive", which was not being tested.
- **table-s6-emission-rates:** the statement is now limited to the 12 antennal-active compounds, because Table S5 lists other abundant compounds. I added a reading that Table S6 comes from the single Fig. S1 sample, since its peak areas are identical to Table S5's.
- **fig2d-other-compounds-unchanged:** removed the made-up "within 5 percentage points" rule. Absence is now judged on the Table S9 test alone.
- **figs5-blend-oxidation:** removed the made-up 5% rule. The criterion now says the paper gives no test and names no ions for Fig. S5.
- **figs7-manduca-sensitivity:** the EAG test at 10^-6 alone was made up. "More sensitive" is now marked open, with readings named.
- **fig3d-field-no3-fewer-visits:** removed the no-odor control against floral odor statistic (p = 0.048), which is not the finding. I confirmed that the Table S11 coefficients follow from the Table S10 counts under reading (a).
- **fig3d-visits-per-night:** named both readings of "untreated flower": the live flower (1.928) or the synthetic floral odor (1.980).
- **fig4ab-no3-shortens-recognition:** the statement said "far more"; the paper says "more severe". I removed the made-up "median under half" rule.
- **fig4c-preindustrial-change:** the Greenland "above 75%" threshold is now marked as a reading.
- **figs8-no3-faster-than-o3:** this criterion could not pass even on the paper's own numbers. Table S12 shows α-terpinene and three green leaf volatiles are also faster with O3, not only the two sesquiterpenes. "Most" now means more than half of the compounds, and I added a test of "monoterpenes most reactive".

**What remains open**
- I could not render the PDF figures here (no poppler or PyMuPDF). So the Fig. 1E letters, the Fig. 3B zero proportions and 50% Manduca decrease, and the Fig. S7C doses are unchecked against the images. The Table S4 p-values agree with the Fig. 1E letters.
- I did not reread the Zenodo code; its description in the file is the first reader's.
- The paper's own inconsistencies are listed in the file header for the author, and were not resolved. Examples: the Fig. 2D inset against Table S9, "logistic" against "log" link, 72 against 47 vertical levels, and 97 against 98 or 99 cities. I also recorded the Table S12 reference mismatch (ref. 74 against ref. 78).

The paper's main findings are all covered, and every claim comes from this paper.
