There was one question, and I changed the claims file to answer it.

**Question: `firing-rate-depth`, also covering `fig4s1-cs-peak-suppression-not-different`, `fig5ej-cs-pause-cells-shallower` and `fig6g-us-response-depth`.** Yes, these four claims should get recording depth from the paper's Source data 1, so they are now `data: with_inputs`.
- **Why:** the paper publishes Source data 1 with the article as a structure of "51 variables relevant to the analyses in this paper" for the 372 cells, in the dataset's order. CRCNS cb-1 does not list depth.
- **Changes:** the opening comment of `claims/brinke-2017.yaml` now names `elife-28132-data1-v2.mat` and its eLife URL as outside data that supplies depth. Each of the four claims is marked `data: with_inputs`, and its criterion says depth comes from that file.
- **Not `elsewhere`:** the spike and eyelid data still come from the dataset, so only the depth is outside data.
- **Unchanged:** statements, quotes and expected values.
- **Left to the author:** the link claim that matches cells by order and checks shared values (Author, step 4).
- **Not verified from the paper:** the paper's text never lists the variable names. That a variable called `Depth` is in the file comes from the question, since the attempt read the names.

The question is marked `answered: 2026-11-13`. `python tools/claims_check.py` reports 55 claims, 55 quotes and 0 problems, and both YAML files parse. Nothing is committed.
