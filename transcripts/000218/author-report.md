I've finished steps 1 to 6 for dandiset 000218 (Tingley and Buzsaki 2019). The entry passes `check` and ran cleanly from a fresh environment in 17.7 min, and the handover package is built in `executed/000218-tingley-2019/handover/`. I did not verify my own work, commit or push.

I used the full text: the accepted author manuscript in PMC (PMC6952543), saved under `paper/`. Its supplementary figures were not included, so claims on Figures S1 to S5 rest on the main text. The pinned version is 0.250624.0439: the paper cites no version, and the older published version 0.220131.1608 holds the same 98 files with identical blobs (the notebook shows this).

The files contain no detected HFOs or ripples, and the paper does not name its channels. So every event-based outcome tests my own detector (Methods parameters, gaps filled from buzcode `bz_FindRipples`) as much as the data. Many detected LS events are not followed by LS firing, which drives most of the HFO outcomes.

**(1) Outcomes (31 claims)**

| Claim | Outcome |
|---|---|
| dataset-composition | partially reproduced |
| fig1c-hfo-each-animal | not reproduced (1 of 6 animals) |
| fig1c-event-count | reproduced (31,984 vs 29,955) |
| figs1-participation | not reproduced (2.7% vs 16%) |
| fig1d-phase-locking | partially reproduced (56% locked vs 92%; trough preference holds) |
| fig1f-shorter-than-ripples | reproduced |
| fig1g-slower-than-ripples | not reproduced (LS faster) |
| fig1h-no-amplitude-frequency-correlation | not reproduced (r = 0.056, significant) |
| fig2-confined-to-ls | not reproduced |
| fig4b-pre-post-unchanged | reproduced (only 106 pairs) |
| fig4b-hfo-above-behav | reproduced |
| fig4d-compression | not reproduced |
| figs2-post-rate-increase | partially reproduced (LS only) |
| fig5b-nrem-and-rates | partially reproduced |
| fig5d-lag | partially reproduced (coupling holds, lag 0 ms vs 6.4) |
| fig5e-state-coupling | not reproduced (p = 0.089) |
| fig5f-ripple-triggered-firing | not reproduced |
| fig5f-no-phase-coherence | not reproduced (31 SD above jitter) |
| fig7e-ca1-spikes, fig7e-state, fig7e-duration | partially reproduced (above chance, out of tolerance) |
| fig2ef-intermediate-ls, fig3-travelling-waves | blocked: metadata insufficient |
| fig4-sessions-few-change, fig4c-temporal-bias | blocked: other (too few recordings after selection) |
| fig6-optogenetic-hfos, fig7e-ca1-depth | blocked: data missing |
| fig7e-replay, fig7e-seqnmf, fig7e-content-independent | blocked: methods underspecified |
| fig8-model | blocked: other (a simulation) |

Totals: 5 reproduced, 9 partially reproduced, 9 not reproduced, 8 blocked.

**(2) What was found about the dandiset**
- **What is there:** 98 files from 6 rats, matching the paper. Files with both LS and hippocampal units number 37, as in the paper; LS-and-CA3 files number 10 against the paper's 25.
- **Missing data:**
  - No detected events and no detection channels.
  - No unit waveforms, unit channels or quality metrics.
  - The CA3 recordings have no CA1 reference channel.
  - The optogenetics rats are absent.
- **Missing metadata:**
  - Electrode coordinates are NaN in every file.
  - 268 units in 9 files have no region label.
  - The `hpc` label does not say whether a site is in CA1.
  - Four DT7 files label every electrode `unknown`.
- **Format error:** 25 units have spike times out of order.
- **Clock and duplicates:** spikes, LFP, sleep states and trials are consistent with one clock, and no recording is deposited twice.
- **Shared signal:** 35% of LS HFOs coupled to a CA1 ripple fall on the same sample as the ripple (71% in DT8). This points to a 120–200 Hz signal shared by LS and hippocampal channels.
- **Code:** the paper's linked repository holds no analysis code for this paper, only the Figure 8 model.
- **Paper inconsistencies:** the band is given as both 120–180 and 120–200 Hz, and the Methods cite the wrong figure numbers in places.

**(3) Where the protocol was unclear, wrong or missing something**
1. It has no guidance for when the dandiset lacks the intermediate products the results depend on (here the events and channels). I detected events with a fixed rule written into the claims file and recorded the detector as a deviation and a finding.
2. Using the paper's stated spread as tolerance gives very wide bounds when the spread is an SD (27 ± 9 ms). I followed the rule and noted that the bounds are wide.
3. There is no threshold for "too few units under the claim's own rule". After selection I blocked two per-session claims (7 and 4 recordings, against 53 in the paper) as `other` and kept the pair-level claims tested. Their numbers are in the notes.
4. The clock-check examples (decoding a task variable) do not fit continuous sleep recordings. I used three contrasts instead:
   - spike phase-locking to the ripple band at shifted spike times;
   - ripple rate by state with the state table shifted;
   - the share of trial time scored as NREM, with trials shifted.
5. `inputs` is framed around data. I listed buzcode and the paper's repository there although only their parameters were used.
6. A model or simulation claim fits no block reason; I used `other`.
7. When different counts match under different readings, it is unclear whether `measured` should use one reading for all. I recorded the matching reading per quantity.
8. Step 5 assumes linked code exists. Here it does not, which I recorded as `methods_unavailable`.
9. A two-part criterion (fig5d: coupling plus lag) did not define partial. I applied the protocol's general "holds only in part".
10. Runtime cannot meet the 10-minute aim for a 1.5 TB dandiset. Loading each file's chunk index takes about 33 s, so the run takes about 18 min, which is recorded in `entry.yaml`.
11. The date rolled over to 2026-10-17 during the run; I kept 2026-10-16 as you specified.

**(4) Runtime and failures**
- Each full run took 17.7 min, of which 16.1 min was streaming all 98 files with 6 workers.
- No file failed. The 4 DT7 files with only `unknown` electrodes were skipped for LFP analysis.
- One bug (an empty interval list) was found and fixed during development.
- `git status` lists sandbox placeholder files (`.bashrc`, `.idea`, `scripts` and others). They are device nodes created by the sandbox, not files I wrote, and the workflow should not commit them.
