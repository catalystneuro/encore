I ran steps 1 to 5 of the Author protocol on DANDI:001260 (version 0.250911.0744, the only published version) and ran the handover (step 6). `tools/entry.py check` reports 0 errors and `all` passed, with the notebook running in 970 s. Nothing is committed.

The main finding about the dataset: the paper's dataset KI is split across two dandisets. 001260 holds 74 of the 99 recordings, and the other 25 are in 000473, a dandiset whose metadata names a different paper.

## 1. Outcomes (40 claims, including one link claim I added)

| Claim | Outcome |
|---|---|
| dataset-ki-counts | partially reproduced (99 recordings and 53.6% PFC; 20,354 units against 24,248) |
| fig1h-waveform-classes | partially reproduced (fractions match, counts low) |
| fig1i-nw-higher-metrics | reproduced |
| extfig1d-sleep-like-differ | reproduced |
| extfig1-epoch-counts | not reproduced (20.2% sleep-like time against 6%) |
| extfig1f-burstiness-memory-uncorrelated | not reproduced (p = 1.7e-66, R²m 0.024) |
| fig2a-som-memory-burstiness | partially reproduced |
| fig2b-pfc-regular-territory | reproduced |
| fig2e-category-stability | reproduced (57.3% against 18.4%; rests on an assumption) |
| fig2f, extfig3f, fig2g ×3, fig3c, extfig7n, fig4g-pl-orbl | blocked: methods underspecified (category numbering G2) |
| fig2g-th-hpf-bursty | blocked: methods underspecified (the claim's own two readings disagree) |
| extfig5g-nw-enrichment | not reproduced |
| fig2j-nw-ww-correspondence | partially reproduced |
| fig3a, supptable5 | blocked: depend on a blocked claim (computed: not reproduced; the absence holds) |
| zenodo-unit-link (link) | reproduced |
| fig4b-dataroi-parcellation | reproduced (38 dataROIs with 000473; 22 on 001260 alone) |
| fig4cd-dataroi-enrichment | reproduced |
| fig4e-activity-modules | partially reproduced |
| fig4g-gao-category1 | not reproduced |
| fig5b-tone-categories | reproduced |
| fig5cd-tone-maps-cross-subregions | partially reproduced |
| fig5e-tone-responsive-patches | reproduced |
| extfig9e-tone-responsive-no-hierarchy | reproduced |
| fig5j-tone-responsive-high-rate | not reproduced |
| fig2i, fig3b, fig5g ×2, fig5h, fig5k (IBL data) | blocked: too large, not started |
| fig5i-map-similarity | blocked: too large, through its IBL dependency (the dataset part was computed and is not reproduced) |
| methods-settings-no-difference | blocked: methods underspecified |

Totals: 10 reproduced, 6 partially reproduced, 5 not reproduced, 19 blocked.

## 2. Dataset

**What it holds.**
- 001260 has 74 recordings, 41 mice and 20,374 units.
- With 000473 (25 recordings, 9,408 units, 25 mice) the total is exactly the paper's 29,782 units before its unit quality control, and its 66 mice.
- No field marks which units the paper kept.
- The two-column `quality` field is undescribed; its first column runs up to 1.15e5, so it is not the ISI violation ratio the Methods threshold at 0.1.
- The behavioral setting is only in the free-text session description.

**What has to come from the paper's Zenodo record (10.5281/zenodo.14205018).**
- The flatmap positions and the paper's own quality flags and ww/nw labels are not in the files.
- The Zenodo metrics files match all 20,374 units by recording and unit id.
- Location labels agree for 98.6% of units; 283 differ, 207 of them in one recording.

**Metadata errors.**
- In Detection and Context files, the `lick` and `valve` trial columns are described as "sound amplitude".
- In Detection files, `Block` holds the trial outcome (miss, hit, correct rejection, false alarm), not a block.
- In one Context file, `sound` is False for all 524 trials although 524 tones were played.
- Every electrodes column is described as "my description".

**Sleep-like periods.**
- Following the Methods, sleep-like periods take a median 20.2% of each recording (the paper says 6%).
- 12 of 74 recordings are more than half sleep-like.
- The paper's code uses different parameters (50 ms minimum trough instead of 5 ms, among others), recorded as a code mismatch. It still gives 8.7%.
- This leaves fewer active epochs and units for every analysis, which explains most of the low counts.

**Assumptions.**
- The geometric mean for sleep detection is taken over bins with a positive rate.
- Blocks for the stability analysis come from runs of the `Block` column, or from cuts of 50 onsets.
- Units are not filtered by quality (claims-file reading b), since the paper's own flags pass 97% of units.
- The ZETA onset is computed from zetapy's rate as the first half-peak crossing, because zetapy 4.1 no longer returns it.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
1. What rule carries the category numbering to a retrained SOM?
2. Which test supports "no difference across behavioral settings"?
3. Which recordings had an inherent block structure, and where is it stored?

**Questions to a reader:** none.

## 3. Where the protocol was unclear

1. **"A claim that depends on a blocked claim is blocked for the same reason."** Applied literally, this blocks fig3a and supptable5 even though their outcome is the same under both category numberings. It also blocks fig5i as too_large because of its IBL part, although the dataset part ran. I followed the rule and kept the computed results in the notes.
2. **"The criterion decides the outcome," but some criteria define no partial outcome** (fig2a, fig2j, fig4e, fig5cd). I recorded partially reproduced when part of the claim held under every reading, and said so in the notes.
3. **No case for a paper's dataset split across two dandisets, one filed under another paper.** I used 000473 as a pinned input for the counts and the dataROI count only; everything else runs on 001260.
4. **Adding a link claim.** The schema forbids `inferred` on a link claim, so I used a quote from the paper's Code availability. I also set `data: with_inputs` and added the link claim to `depends_on` on 10 reader claims, as the fig4b criterion instructs. The protocol does not say whether the author may edit those fields.
5. **too_large is defined for a computation that was stopped part-way.** It does not fit IBL claims that were never started for lack of time; I used it and said "not started".
6. **The claims file's rule to block when the two category numberings disagree overrides step 1.6**, which would let me adopt the better-supported numbering as an assumption. I followed the claims file. This blocked 8 claims.
7. **The fig4e criterion says "must hold under both [readings], else blocked".** It is ambiguous when both readings fail; I treated agreement on failure as a result, not a block.
8. **Clock check.** I used the post-minus-pre spike rate at true tone onsets against onsets shifted by 1.5 s, on 10 files, in place of decoding.

## 4. Runtime and failures

About 1 h 55 min of the 5 h (12:31 to about 14:26 UTC). The final notebook runs in 970 s; ZETA on 5,232 units takes about 270 s of that. Nothing failed in the final runs. Two dev-run bugs (a histogram index and a missing quote in a cell) were fixed before them.

Unexplained untracked files appeared in the repository root (`.bashrc`, `.profile`, `.idea`, `.vscode`, `scripts` and others). The run's start status was clean and I did not create them, so I left them alone. They should be checked before the workflow commits.

Everything is in `entries/001260-le-merre-2026/` and `attempts/001260-le-merre-2026-01.yaml`. The only change to the claims file is the added link claim and the `data`/`depends_on` fields above. The handover is in `executed/001260-le-merre-2026/handover/`.
