I wrote `claims/001847/10.7554-elife.109717.yaml` with 38 claims. The quote checker passes every quote. It still flags two p-values, 2.0 x 10-4 and 6.0 x 10-4, because the paper prints them in a form it doesn't parse; I confirmed both by reading the supplement 1 legends.

**Text read:** the eLife Reviewed Preprint, version 1 (30 December 2025, not revised), from the publisher's HTML. It holds the Results, figure legends, Methods with figure-specific methods, and the legends of the four figure supplements. No PDF was supplied, so the grid-map findings rest on the Results sentences that describe them. Nothing the claims need is missing from the text.

**Code read:** the paper names its repos without addresses; the dandiset description gives them.
- LSENS-BMI-EPFL/Bech_Dard_process_NWB at 212a631
- LSENS-BMI-EPFL/Bech_Dard_plot_figures at 91f04fd
- their dependencies cicada_analysis 0.3.0 (998cae7) and explain_behaviour v1.0.1 (ce39723)

The code's session lists give the mouse and session counts in the opening comment. The Zenodo intermediate tables are not needed by any claim.

**Counts:**
- 38 claims, all with quotes, none inferred.
- 8 claims carry statistics, 13 values in all: paired t-tests, Bonferroni-corrected where the code shows it, and hierarchical bootstrap for muscimol.
- 12 claims have expected values. The tolerances are the paper's stated SDs over mice, or 10% where it gives none.
- All 38 have a criterion. 34 are findings from Figures 1 to 4, and 4 come only from the supplements: block duration, spout latency, muscimol, and the photoactivation control.
- No link claims. Every claim is `data: dataset`.

**Details the paper leaves open, and the readings named:**
- **Expert sessions:** (a) the Methods' contrast rule recomputed from the dataset (the code's test is a bootstrap lower bound above 0.375); (b) the code's fixed list of 201 sessions.
- **Opto null distribution:** (i) the Methods shuffle block labels; (ii) the legend and the code shuffle all trials (10,000 times in the code, 1,000 in the legend).
- **Opto d' threshold for an affected site:** none is set anywhere. Readings are 0.5 (where the map's colour scale starts), 0.8 (the smallest effect drawn in Fig 4B) and 2 (the Fig 3H threshold).
- **RSC grid site:** (-1.5, 0.5) or (-0.5, 0.5); the code's coordinate list names both.
- **Widefield baseline:** 50 ms or 250 ms, the two values the Methods give; the code's 100 ms is a variant.
- **Fig 3H excluded window:** frames from 30 ms (the Methods) or from 20 ms (the code).
- **Jaw onset (Fig 3C):** d' ≥ 1 on mouse averages (the Methods) or 3 SD per trial (the code). Which trial types are pooled is also open.
- **Context Off (Fig 1E):** the paper reports no test. Readings are a paired t-test of W+ against W- blocks, or the code's transition test.
- **Fig 1H, no anticipation:** no test in the paper. Readings are a Pearson trend over pre-transition bins, or Fisher's exact test of bin -1 against bins -5 to -2.
- **Fig 1E/3E/3F/3H:** the order of auditory activation is read as (a) peak time or (b) half-peak time.
- **Fig 4B comparison:** (a) the d' ≥ 0.8 line rule or (b) the Bonferroni-corrected related t-test.
- **Fig 4E angle:** the Methods' angle decides; the code's shift by the trace minimum is a variant.
- **Fig 4F/G regression:** sites paired by coordinate; the code's pairing by sorted position (which may mis-pair sites) is a variant.
- **Model early stopping:** the code stops on the test split; stopping on the inner validation split is the variant.
- **Small-effect claims:** "little effect" in catch trials and the trajectory "closeness" use measures I wrote, since the paper gives none. Those criteria say so.

**Problems found in the paper and code:**
- Supplement 1H gives jaw speed before lick as 2.8 ± 0.1 mm/s, with t = −3.7 against the stated direction. This is recorded as a paper inconsistency, and that mean is held to 10%.
- The supplement 1D ± is 9 ms for every group; it may be an SEM, so both SD and SEM will be reported.
- The RSC axon tracing (light-sheet imaging) may not be in the NWB files; whether the dataset holds it is left to the author.

Nothing was committed.
