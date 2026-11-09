**Verification report, round 2: Le Merre, Heining et al. 2026 on DANDI:001260 (0.250911.0744)**

The claims file has 40 claims, and the attempt record gives one outcome for each: 12 reproduced, 6 partially reproduced, 4 not reproduced and 18 blocked (11 methods_underspecified, 7 too_large). I agree with all 40.

### 1. Outcomes and assumptions

- **Outcomes where my verdict has not changed:**
  - **dataset-ki-counts, fig1h-waveform-classes (reproduced, assumed).** The main rule is now the Unit quality control passage (≥6 spikes in ≥12 spontaneous epochs). The assumption is stated and reasonable, and the counts do not depend on the sleep-like detector (cells 14, 17). The record says openly that the 5-spike reading misses one fig1h count (951 unclassified) and the active-epochs reading misses another (17,239 ww).
  - **extfig1d-sleep-like-differ (partially reproduced, assumed).** I agree under the main detector. Its outcome depends on that detector: the per-probe detector, the code's detector and the paper's own Zenodo periods all give "reproduced" (cell 23).
  - **extfig1-epoch-counts (not reproduced).** It fails under every detector, so its `assumed: true` is unnecessary but harmless.
  - **fig2e, fig2f, extfig3f, fig2g-pfc-regular-enrichment, extfig5g (assumed).** The block rule (fig2e) and the detector are stated assumptions and reasonable. The notes say honestly that fig2f, extfig3f, fig2g-pfc and extfig5g had different outcomes under the round-1 detector.
- **Outcomes where I now agree, changing my round-1 verdict:**
  - **fig3a-harris-regular-positive (blocked).** The new numbers support it: category 2 has r = 0.61, p = 0.012 under both G2 readings, and category 1 is negative under G2 (a) (cell 72).
  - **fig4g-gao-category1 (blocked).** It now differs under G2: r = 0.39–0.40 under G2 (b) with reference (a), −0.33 to −0.38 under G2 (a) (cell 96).
  - **fig4e-activity-modules (blocked).** The two readings of "ILA-specific" disagree for reference (a) with G1 a (cell 90), which the criterion blocks.
  - **supptable5-no-hierarchy-within-pfc and fig5i-map-similarity (blocked through `depends_on`).** I accept the dependency rule.
  - **IBL claims (too_large, not data_missing).** The data are public, and the claims file marks them `with_inputs`.
  - **fig5cd-tone-maps-cross-subregions (partially reproduced).** I withdraw my round-1 "not reproduced". I accepted "partial" for fig2a under the same kind of all-parts criterion, so I accept it here too.
- **Problems with assumptions:**
  - **The session-skip rule.** The detector assumption justifies skipping sessions by quoting that KI sessions "consistently featured a sufficient number of cortical units" (cell 10, `pfcki.py` docstring, record deviations). In the paper (Methods, Detection of sleep-like periods) that sentence says *all* KI sessions had enough units; it does not describe skipping any. The skip rule (null ≥ 1%, 10 sessions) is the attempt's own. It is reasonable given the paper's `off_used = no` files, but it should be labelled as the attempt's rule, not the paper's.
  - **Inconsistent use of the "Assumption" label.** fig1i and fig5b carry the "Assumption" deviation without `assumed: true`. That is acceptable, because their outcomes are not shown to depend on it.

### 2. Sentences the printed outputs do not support

1. **Record, fig2i-ibl-replication notes:** "It also depends on fig2g-pfc-regular-enrichment, which is blocked." That claim is now reproduced (cell 50, and the record's own outcome).
2. **Record, findings (methods_unavailable, settings):** "for example Aversion against Passive in B, p = 9e-05". That is the round-1 value. Cell 126 gives p = 0.0021, and so do the record's own notes for methods-settings-no-difference.
3. **Cell 40 (markdown, fig2e method):** "where the trials table's `Block` column marks runs of trials (Aversion, Context, Opto and part of Passive)". Cell 41 prints 20 "inherent" files, and the cell 3 table shows these are the 6 Aversion and 14 Context files. Every Opto and Passive file is "fifty". The record's deviation ("20 recordings") is correct.

Every other "**Result:**" sentence (cells 15–124), the Summary (cell 130), the README and the other record notes match the outputs. I checked in particular:
- "four of those eight claims hold" on the paper's SOM: fig2g-ila-pl, fig2g-bursty, fig3a and fig3c (cell 128).
- The blocked-under-G2 count of 8.
- All quoted r, p, E and count values.

**My round-1 reasons in the record.** The verification block gives them faithfully and in my own words. The additions (for example "The verifier gives data_missing", and the Gao top-score IDs for fig4g-pl-orbl) are taken from my report. The "reviewed" summary covers my problems 5, 6 and 8; problems 7 and 9 are answered in the per-claim responses.

### 3. Round-1 points

**Resolved:**
- Problem 2 (the epoch rule).
- Problem 4, as far as the attempt can go: the `relabel_clusters.py` direction is quoted and matches the helper, and the projection onto the paper's SOM was added.
- Problems 5–9: stated or fixed.
- From section C: the fig2j 9-region variant (still not reproduced), the fig4g Gao ranks (19, 20 and 41 rank 6th, 8th and 11th; the question is now with a reader), and the variants on the paper's 42 dataROIs for fig4e, fig5cd and fig5i.

**Remaining, each bearing on a conclusion:**
- **Problem 1, sleep-like detection (partly resolved).**
  - Pooling per session removes the artefact of probes with few units (the null table in cell 27).
  - But well-sampled probes, where the null marks ≤0.1%, are still marked 16–21% sleep-like, and the median is 9.9% against the paper's 6%.
  - The EMG ratio is only 0.9 (IQR 0.8–1.0), and several recordings are ≥1.1: PL032 1.23, 518804 1.20, PL070 1.10. The paper says detected periods "consistently coincided with a flat EMG".
  - Between rounds, the change of detector alone changed the outcomes of extfig1d, fig2f, extfig3f, fig2g-pfc-regular-enrichment, extfig5g, fig3a, fig4e and fig4g-gao-category1, through the units kept and the retrained clusters.
  - Rerunning the SOM and enrichment claims with the paper's own Zenodo sleep-like periods would show which of these outcomes are stable. Today that variant exists only for extfig1d and extfig1-epoch-counts.
- **Problem 3, analyses on 001260 alone (partly resolved).**
  - fig4e is blocked on 24 dataROIs, only 2 of them in ILA.
  - Both variants closer to the paper find no ILA-specific module under either reading: the paper's 42 dataROIs, and all of dataset KI with 39 dataROIs (cell 91).
  - The block follows the claims file, but the evidence leans towards not reproduced.
- **G2 numbering (a claims-file limitation; I report it, not correct it).**
  - The paper's own SOM agrees with reading (b) for only 27.7% of units, and with (a) for 19.9% (cell 128). So reading (b), matching clusters to the text, does not stand in for the paper's numbering.
  - Example: PL's category 1 E-score is −0.1 under (b) but 9.1* on the paper's SOM.
  - The 8 claims blocked under G2 stay open until the authors say how a retrained SOM should be numbered.
- **fig4g-pl-orbl-extremes.** Whether GaoROIs 19, 20 and 41 are the paper's IDs is still open; it is asked of a reader.
