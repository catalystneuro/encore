I checked `claims/scholl-2015.yaml` against the paper. It now passes, and I've marked it ready for an attempt. Nothing is committed.

**Checker result:** `claims/scholl-2015.yaml: 25 claims, 25 quotes, 10 statistical values, 0 problems`. That was the result both before and after my edits, and the YAML still parses.

**Changes, by claim**
- **Paragraph numbers in "A Functional Organization of Binocularity":** the writer counted page breaks as new paragraphs. Two places in the text show this is wrong. "From these data (Figure 4F)" sits on the same printed line as the end of paragraph 3. "OD. Here, surrounding populations…" finishes a sentence that starts on the page before. I renumbered these sources:
  - fig4f-od-length-constant: 4 to 3.
  - figs4-same-plane-control, figs5-neuropil-no-relation: 5 to 4.
  - fig4ef-pvminus-od-unrelated, figs6ab-pvminus-pv-like-od: 6 to 5.
  - fig5-camkii-responsive, fig5e-camkii-od-unrelated: 7 to 6. The fig5e criterion also said "paragraph 8"; that is now 6 too.
  - fig4i-pv-disparity-matches-local, fig4k-pv-disparity-length-constant: 9 to 7.
  - fig4jk-pvminus-disparity-weak, figs6cd-pvminus-pv-like-disparity, fig5f-camkii-disparity-unrelated: 10 to 8.
- **cell-counts-responsive:** I removed reading (b), which counted only cells meeting the joint criterion. Under it the monocular and binocular counts are the same cells, so it could never give the paper's different counts (115 against 236, 944 against 2,001).
- **fig4ef-pvminus-od-unrelated:** the "no relation" result at 75 to 150 µm is now judged at p < 0.01, not p < 0.05. The 0.05 came from nowhere in the paper, and the paper reports its shuffle test for these slopes at p < 0.01.
- **fig4ag-salt-and-pepper:** the p < 0.05 threshold is now marked as a standard choice, since the paper reports p = 1 and gives no threshold. I also added a second reading for the MI slope's p-value: shuffling cell positions within the session. That is the only significance test for these slopes that the Methods describe.
- **figs6ab-pvminus-pv-like-od, figs6cd-pvminus-pv-like-disparity:** the writer assumed only the individual cells are limited to the ODI or DSI range. The Supplementary Figure 6 legends leave open whether the surrounding populations are limited too, so both readings are now named.

**Still open** (all recorded in the checks entry)
- **Unconfirmed paragraph breaks:** I couldn't confirm a few from the extracted text, because no tool for reading the PDF's layout was installed. They are the breaks in "Binocular Selectivity in Mouse V1" (paragraphs 3, 4, 5) and the possible break before "PV+ interneurons also exhibited spatial dependence". The cited figure panels still point to the right places.
- **Circular-correlation threshold:** the paper gives no significance threshold for the shuffle-corrected circular correlation, used in fig4i, fig4jk, figs6cd and fig5f. I kept p < 0.05 as a standard choice and named p < 0.01 as the stricter alternative.
- **fig5-camkii-responsive:** the counts 285 and 306 most plainly mean labelled excitatory (CaMKIIa+) cells only. Nothing else in the paper confirms that. Only 50 of them (16%) enter the 50 µm analysis, against 36% for the other cell groups.

Every main finding has a claim, and every claim comes from this paper.
