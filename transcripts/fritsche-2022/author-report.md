I've finished steps 1 to 6 of the Author section. `tools/entry.py all` passes: the notebook runs in 492 s with 0 check errors. `handover` built `executed/fritsche-2022/handover/`. Nothing is committed.

## 1. Outcomes (31 claims, none blocked)

| Claim | Outcome |
|---|---|
| units-responsive-count | reproduced (2422 units; V1 580, LGN 142, LP 91) |
| fig1d-v1-1back | reproduced (0.821, p = 6e-58) |
| fig1d-extrastriate-1back | reproduced (0.795 to 0.876) |
| fig1d-thalamus-1back | reproduced (LGN 0.935, LP 0.833) |
| fig1e-consistent-across-mice | partially reproduced (thalamus 21 of 23 mice) |
| fig2-v1-tuning-main-effect | reproduced |
| fig2-v1-tuning-interaction | reproduced |
| fig2-v1-adaptation-at-all-orientations | reproduced |
| fig2-thalamus-no-tuning-dependence | reproduced |
| fig3a-v1-long-term | reproduced (significant up to 8-back) |
| fig3a-v1-double-exponential | reproduced (14.2%, 0.82, 3.8%, 6.71) |
| fig3a-v1-half-life | reproduced (13.96 s) |
| fig4-cumulative-adaptation | reproduced (20.4% against 17.9%) |
| fig4b-linear-accumulation | reproduced |
| fig3b-thalamus-short-term | reproduced, rests on an assumption |
| v1-vs-thalamus-welch | reproduced (exactly 2, 4, 9 against LGN and 3 against LP) |
| fig3c-mice-long-term | reproduced |
| decay-cortex-double-better | reproduced |
| table1-extrastriate-tau-slow | reproduced |
| decay-thalamus-single | reproduced, rests on an assumption |
| fig5-repeat-suppression | partially reproduced |
| fig6c-static-v1-1back | reproduced (0.897, 545 units) |
| fig6c-static-other-areas-1back | reproduced |
| fig6d-static-consistent-across-mice | partially reproduced |
| fig7a-static-v1-long-term | reproduced |
| fig7b-static-cortex-decay | reproduced |
| fig7-static-lgn-single | reproduced |
| fig7b-static-areas-long-term | reproduced |
| fig7c-static-long-term-across-mice | partially reproduced |
| fig8-no-spurious-long-term | not reproduced, seed sensitive |
| robust-threshold-preferred-window | reproduced |

Totals: 26 reproduced, 4 partially reproduced, 1 not reproduced.

## 2. Dataset, assumptions, questions

**Version.** I pinned 0.251116.2246. The paper cites no version, and this is the only published one. The notebook header says why.

**What the files hold.** All 32 mice are there, with the genotypes and stimuli the paper describes. Spike times share the clock of the stimulus tables in every session: orientation tuning measured with the true labels beats tuning with labels shifted by whole presentations. No recording or unit was deposited twice.

**Findings (all minor):**
- The units table holds every sorted unit and labels 20182 of 74658 `noise`. Neither that column nor the quality metric columns are described in the files.
- Three sessions have 598 drifting gratings, not 600.
- 13 sessions list invalid intervals tagged by probe, some inside the grating epochs. I did not apply them.
- Some units sit on channels labelled `grey` or `VIS`, which name no area.
- Static blank sweeps come about one in 31, where the Methods say about one in 25.

**Adopted reading.** Of all the readings the claims file lists, the unit counts point to one: leave out `noise` units, require a rate above the gray mean plus 1 SD from blank trials, and pool the preferred orientation over the other stimulus parameters. Under it the per-unit ratio pools over orientations, the region value is a geometric mean, and blanks hold their positions in the sequence. With this reading the 1-back values match the paper to within about 0.01.

**Assumptions:**
- **The `noise` filter.** It affects two claims. If the noise units are kept, LGN becomes significant at 7-back and its decay time constant (tau) drops to 0.000. So decay-thalamus-single and fig3b rest on the filter.
- **Significance means a ratio below 1 (fig3b).** A two-tailed test also flags LP at 3-back, where the ratio is 1.03, i.e. facilitation, not adaptation.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- Do the significance borders in Figure 3B include ratios above 1?
- What rate and noise model did the Figure 8 simulated neuron use?
- Were the `noise` units excluded?

**Questions to a reader:** none.

## 3. Where the protocol was unclear or missing something

1. **Any reading or all readings.** Author step 1.6 says the outcome is the one all readings give. The claims file's criteria say "reproduced under one reading". I followed the claims file.
2. **Direction of a two-tailed test.** Nothing covers whether "significant n-back" counts ratios above 1. I assumed adaptation only, and showed both.
3. **Filters outside the listed readings.** The `noise` label is not among the claims file's readings. I treated it as an assumption, and ran the key results without it as a variant, not every claim.
4. **Seeds for one bootstrap per region.** It is unclear whether each region's generator should take seed +1, +2 and so on. I gave every region the claim's seed (plus 1000·k for the four extra runs).
5. **Streaming URL.** `archives.md` doesn't say how to get the S3 URL. Following the download redirect returned 403, so I took the S3 address from the asset metadata's `contentUrl`.
6. **Missing partial rules.** The fig5 criterion has no partial rule, so I rated it partially reproduced from the protocol's general definition. The fig8 criterion is strict about confidence intervals at every n, so tiny, chance-level exclusions fail it.

## 4. Runtime and failures

- The notebook takes about 8 minutes (492 s); streaming the 32 files is 2 to 3 minutes of that. Peak memory is about 3.2 GB.
- The first full run failed because a cell boundary was missing, which left a function inside a markdown cell. I fixed it and the later runs passed.
- Some harmless RuntimeWarnings (division by zero) remain in the fig4b cells; the units they come from are reported as dropped.
