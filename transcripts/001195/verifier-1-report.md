**A. Outcomes**

| Claim | Outcome | Reason |
|---|---|---|
| fig6df-epsp-ipsp-at-rest | reproduced | At 2 and 3 SD, every region has a cell with an EPSP and some cells have an IPSP (cell 13). Cell counts are 15/40/56 against the paper's 19/36/48; the criterion says to judge on the cells present. The 2 and 3 SD tests also pass on pure noise (problem 1), so the support comes from the 5 SD variant and the clock check: 55 cells above 10 SD at light onset, 2 at the shifted time. At 5 SD there are EPSPs in all regions, plus inhibition-only and mix cells. |
| fig6gi-firing-responses | partially_reproduced | Under all four readings, CeA and BLP have both excited and inhibited cells, and every BNST cell with intervals is excited (cell 15). But that is only 2 BNST cells (B7 has no spikes), and the counts are 3/13/13 against 5/20/17 at tolerance 0. |
| fig6j-epsp-amplitude-region | partially_reproduced | Reading (a) passes at 2 and 3 SD: at 2 SD H = 6.92, p = 0.031, Dunn CeA vs BLP p = 0.042, close to the paper's 6.790 / 0.0335 / 0.0378. Reading (b) fails at both (p = 0.76 and 0.55, cell 17). The criterion asks for "under the readings" and does not say what to do when they disagree. |
| fig6k-ipsp-amplitude-region | not_reproduced | The ANOVA fails at 2 SD (p = 0.69). At 3 SD it gives p = 0.026, but CeA vs BLP is not significant (Tukey p = 0.16, Holm-Sidak p = 0.13). The IPSP counts are 85 and 51 against 34 ± 3.4. Reading (b) leaves 3–4 cells and cannot be tested (cell 19). |
| fig6-s1de-monosynaptic | blocked (metadata_insufficient) | I agree. No sweep description names TTX or 4-AP (cell 6), and no asset's DANDI metadata mentions TTX, 4AP or tetrodotoxin (my API query). No part can be tested. |
| fig6no-cea-clusters | not_reproduced | Under all 16 readings, the late-firing cluster (17–18 cells) has 2–3 inhibited cells and 3 with no response data. "Every late-firing cell excited" therefore fails. 5 of 9 regular-firing cells are inhibited. 27 cells against 26 (cell 25). |
| fig6-s1h-cea-cluster-properties | reproduced | All four t-tests give p < 0.05 in all four readings (cell 27). The t values differ from the paper's (e.g. delay 2.8 against 5.05). |
| fig6pq-blp-clusters | partially_reproduced | The direction holds. Pyramidal cells inhibited: 58.8–64.7% against 93 ± 9.3. Interneurons excited: 72.7% against 62 ± 6.2. 28 cells against 27 (cell 29). |
| fig6-s1i-blp-cluster-properties | reproduced | All four t-tests give p ≤ 0.003 under both sag readings (cell 31). |
| fig6-s1jk-cluster-voltage-area | reproduced | Area: CeA p = 0.0001–0.0005, BLP p = 0.011. BLP EPSP p = 0.014. CeA EPSP p = 0.42–0.83. Holds under every reading (cell 33). |
| fig6-s1ln-combined-clusters | not_reproduced | The joint clustering puts CeA late-firing with BLP pyramidal cells and CeA regular-firing with BLP interneurons, agreeing with the separate clusterings in 50 of 52 cells. In each region one cluster is mostly excited and the other mostly inhibited, but the excited cluster differs between regions. The criterion requires it to be the same, so the claim fails on that condition alone (cell 35; see problem 9). |
| fig7-s1ef-red-vs-blue | reproduced | Every measure gives an ANOVA p ≤ 0.007 on 9 cells (F(2,16)). Red exceeds each blue power in 8–9 of 9 cells (cell 37). F is about 25 against the paper's 200. |
| fig7-s1hi-red-during-blue | partially_reproduced | Amplitude passes: p = 0.007–0.008, smaller during blue light in 10–11 of 13 cells. Area fails: p = 0.26 and 0.16. The criterion needs both. 13 cells against 12 (cell 39). |
| fig7e-no-behavioural-change | blocked (data_missing) | The imaging files hold no side or position data and do not say which cup held the juvenile (cell 10, and my asset listing). The behaviour videos are there, so side times could in principle be tracked from them; that was not attempted. |
| fig7gh-delta-auroc-trend | blocked (data_missing) | No pose or cup interactions. The cell-count part is testable and fails: 869/913/854 ROIs against 429/441/484 ± 10% (cell 10). The files do not mark which ROIs the paper kept. |
| fig7j-proportions-unchanged | blocked (data_missing) | Needs cup interactions. |
| fig7i-little-overlap | blocked (data_missing) | The response counts need interactions. The 202 co-registered cells could be tested with CellReg on the stored footprints; not attempted. |
| fig7m-social-excited-predicts-preference | blocked (data_missing) | Needs interactions and side times. |
| fig7-s1no-no-other-correlations | blocked (data_missing) | As fig7m. |
| fig7-s1l-tdtomato-no-change | blocked (data_missing) | Needs interactions. The counts are testable and fall outside tolerance: 35/138/89 against 39/61/76. |
| fig7-s2-functional-clusters | blocked (data_missing) | Trials are defined by cup interactions. |
| fig1c, fig1h, fig1-s2d, fig2d, fig2-s2, fig3a-c, fig3-s1, fig3g, fig4e, fig4h, fig4k, fig4r, fig4-s2d, fig5, fig8c, fig8d, fig8-s1 (17 claims) | blocked (data_missing) | The API lists 230 assets: 148 patch-clamp NWB files, 41 imaging NWB files and 41 mp4 videos. There are no tracing, behaviour or RNAscope files. |

The claims file has 38 claims: 12 tested, 26 blocked.

**B. Problems**

1. [affects a conclusion] `drn_ephys.evoked` with the criterion's 2 and 3 SD readings detects responses in noise. I tested it on synthetic noise with no response:
   - At 2 SD and 3 SD, 200 of 200 white-noise and 5 ms correlated traces were classed "mix".
   - At 3 SD with 50 ms correlated noise, only 19 of 200 were "none".
   - At 5 SD, 199 of 200 or more were "none".

   The peak of a 55,000-sample window compared with the SD of the baseline is almost always beyond 2–3 SD. This explains the near-empty "none" class (cell 13), IPSP counts of 85 and 51 against the paper's 34 (fig6k), 107 of 111 cells entering fig6j reading (a), and the "detected in 13/13" check in fig7-s1hi. It also affects the cluster labels, because a false "mix" is labelled by the sign of the area (cell 22, `label`). The thresholds are the claims file's readings, but the notebook never ran detection on a light-free window to show the false-positive rate. The labels were not rerun at 5 SD, which could change fig6no (the 2–3 inhibited late-firing cells), fig6pq and fig6k.
2. [affects a conclusion] Cell selection ignores sex (cells 6, 13). The paper's mice were all male (Methods; line 718, "experiments were conducted in male mice"). DANDI metadata gives subjects 23, C137 and C150 as female, 17 patch-clamp cells in all, and they are all included. Leaving them out would make the BLP rest count exactly 48, as in the paper, and CeA 37 against 36. The notebook never reads or reports sex.
3. [affects a conclusion] Rest and firing sweeps are classed by description alone (`sweep_kind`). The measured ch-1 current in rest sweeps reaches +108 pA, and in sweeps described as positive-hold it falls to −57 pA (cell 7); neither was followed up. Rest sweeps were not checked for spikes. A peak of 41.9 mV (cell 13) suggests action potentials in some rest averages, which would inflate EPSP peaks in fig6j and fig6-s1jk.
4. [affects a conclusion] Cell 13 includes a BLP cell (P10, in_vivo_9) with a baseline of −17.9 mV and ch-1 outside ±10 nA. That is a failed recording, and it is also in the firing set as "inhibition" (cell 15).
5. [affects a conclusion] For fig7-s1ef, the "+0.3mW blue" and "+0.2mW blue" sweeps are read as blue-only light (cell 36). The descriptions start with the 635 nm red protocol. The small responses make the reading plausible, but it is an assumption. The light onset of 5.468 s was checked only on ChR2 rest sweeps (cell 9), never on the ChrimsonR red or blue sweeps.
6. [does not affect a conclusion] The firing-sweep check in cell 15 counts only BNST cells that have intervals, so B7 (no spikes) is silently dropped from "every BNST cell excited". The 0 mV spike threshold was not checked on cells with no spikes (C47 has 13 firing sweeps and no spikes).
7. [does not affect a conclusion] `capacitance_pf` underestimates. On a synthetic RC cell (Rs 15 MΩ, Rm 300 MΩ, Cm 50 pF) it returned 42 pF, because it applies no Rs/Rm correction and starts integrating 10 samples early. The bias is systematic and BLP capacitance still separates (p = 0.001). Seal-test pulses standing in for the Methods' 250 ms step are stated as a substitution.
8. [does not affect a conclusion] The cell 20 markdown says the session description and other fields were searched for TTX. The code in cell 6 searches only ch-0 series descriptions; file-level notes and the icephys tables were not read. My API metadata search also finds nothing.
9. [possible misreading in the claims file, not corrected] The fig6-s1ln criterion requires "the excited cluster the same for both regions". The paper's text says only "a very similar result". Late-firing CeA and pyramidal BLP cells sharing a phenotype (low frequency, long delay) and co-clustering is consistent with that text. The outcome above turns on this condition, which I could not check against Figure 6 supplement 1N.
10. [does not affect a conclusion] The imaging files' metadata contradict the paper and the notebook does not comment on it (cell 10). The virus field reads "GRIN in mPFC … Chrimson in BLA" and the stimulus field "589nm, 20Hz", against the paper's CeA, 620 nm and 30 Hz. Subject IDs "4484" and "4484?", "235" and "235 cage", "in_vivo_5" and "in_vivo_5_2" are probably the same mice, so the count of 20 subjects is likely too high.
11. [does not affect a conclusion] I tested `dunn`, `holm_sidak`, `iei_change` and `sweep_kind` on synthetic inputs and they behave correctly. Cluster names (late-firing by delay, pyramidal by capacitance) follow the criteria.

**C. What I could not check**

- Figure images. The PDF could not be rendered here, so I could not see Figure 6 supplement 1N (which combined cluster is excited per region) or the class proportions in Figure 6D–F. A notebook figure of the combined dendrogram with region and response bars, next to the same counts read from the paper, would settle problem 9.
- The false-positive rate on real data. Needed: per-cell detection at k = 2, 3 and 5 on a light-free window (e.g. light sweeps read beyond 12 s), and fig6k, fig6no and fig6pq rerun with labels at 5 SD.
- Which late-cluster CeA cells are "inhibited" and why. Needed: a per-cell table with label source (intervals or rest), class at each k, area and peak.
- Spikes in rest sweeps and holding mismatches. Needed: a per-sweep table of described against measured holding current and spike count in rest sweeps.
- The effect of sex on selection. Needed: sex per cell from `general/subject/sex`, and every count and test repeated with male mice only.
- Light timing for the ChrimsonR sweeps. Needed: the cell 9 onset check run on the red, blue and constant-blue sweeps.
- Whether TTX/4AP is recorded anywhere in a file. Needed: a dump of file-level text fields (session_description, notes, slices, protocol, icephys experimental-conditions and repetitions tables) for a few cells.
- The in vivo parts that are testable without pose: CellReg co-registration counts for GH off and GH on (fig7i's 202), and one behaviour-video frame per session showing whether the juvenile's cup can be identified (fig7e).
