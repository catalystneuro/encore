**A. Outcomes (44 claims in the claims file; the notebook tests 10 and blocks 34)**

| Claim | My outcome | Reason |
|---|---|---|
| subject-group-link | partially_reproduced | Seven of the nine paper groups match the paper's counts (cell 20). The chronic-cohousing group has 14 mice with a First Retrieval session against the paper's 13, and the 12 NV-excitatory mice of Fig. 1f can't be picked out from 20 candidates. No file holds stimulus times or a trial table, so no presentation can be given its call or ISI. The notebook leaves 5 subjects "unknown", but the figshare item titles the criterion allows resolve them (see B1). |
| fig1g-ipsc-depress-faster | not_reproduced | Under reading (a), every Bonferroni p is 1.0 at 175 ms. Under reading (b), IPSCs are higher than EPSCs at 175 ms (0.90 vs 0.68, p=0.33) (cell 22). The mean-trace variant also finds nothing significant at 175 ms. |
| fig1i-operant-prototypes | blocked (methods_underspecified) | Three of the four readings reproduce. Under the 100 ms gap with session 1 vs 8, fast (p=0.0500) and slow (p=0.040) also increase (cell 25), so the readings disagree. |
| ed5b-press-count-unchanged | blocked (methods_underspecified) | Under median×2 with sessions 1-2 vs 7-8, the fast group increases (p=0.049). The other three readings show no increase (cell 27). |
| ed6ef-epsc-tuning | blocked (other) | As computed it would be not reproduced: NV 175 ms does not exceed 125/275/575 ms under any reading, and the EV r is about -0.15 (p≈0.3) (cell 29). But the notebook's own control (cell 13) shows the measure picks up no call-evoked current (B2), so the outputs don't test the claim. |
| fig2h-epsc-enhanced-ev | blocked (other) | As computed it would be not reproduced, because the prototype comparison is significant in every variant (one-tailed p 0.009-0.02, cell 32). The pre-call sham measure shows the same EV>NV differences (p 0.0003-0.012), so what is being measured is recording noise, not evoked EPSCs (B2, B3). |
| fig2i-ipsc-weaker-nv | blocked (other) | The 5- and 10-trial readings disagree at 175 ms (p 0.061 vs 0.040, cell 34). In any case the sham IPSC shows the same EV>NV difference (cell 32), and EV has 7 IPSC cells against the paper's 6. |
| fig2j-ie-ratio-tracks-isi | blocked (other) | As computed it would be not reproduced: EV r = 0.06-0.09, p≈0.7, against 0.47 (cell 36). It rests on the same unvalidated measure, with 7 rather than 6 cells. |
| fig2k-ipsc-exceeds-epsc-575 | blocked (other) | As computed it would be not reproduced: the paired p at 575 ms is 0.17-0.48 (cell 38). Same caveat as ed6ef. |
| ed9b-oxytocin-enhances-spiking | reproduced (weak) | Using Dunn's test on the five baseline-vs-post pairs, stimuli 2-5 have p = 0.022, 0.014, 0.001 and 0.020, stimulus 1 has p = 0.071, and the controls show nothing (cell 40). This is fragile: with all 45 pairs only stimulus 4 is significant. Stimulus 1 also rises a lot (0.04→0.48). Only 5 of the 7 controls have sweeps in the window. |
| fig1a, fig1c ×3, ed2a, ed2b, ed2d, fig4c, fig4d, ed8hi, fig4e | blocked (data_missing) | Confirmed. The dandiset has only ophys movies, and the 60 items of the figshare collection are imaging movies, whole-cell and slice recordings, and operant files/code. There are no retrieval, y-maze or vocalization data. |
| ed4d-response-tracks-isi-probability | blocked (data_missing) | Confirmed: it needs the ISI distribution from fig1a, which is not available. |
| ed3e, fig1f, ed6c, ed3k, ed3m, ed4c, ed4e, ed4g, fig2d, ed6d, fig2e, fig2f, ed7bc, fig3e, fig3h, ed8cd, fig4b, fig4g, fig4h, ed3bc | blocked (metadata_insufficient) | Agreed. The archive API shows no processing, stimulus or interval data in any of the 777 assets. Session descriptions name the call set but not the order of calls in a file. ed3bc additionally needs the blood-vessel regions. |
| fig3-retrieval-onset-range | blocked (metadata_insufficient) | The onset range can't be tested because the start of cohousing is not recorded. The mouse-count part could be tested: 14 mice with First Retrieval sessions against 13 (cell 42). |
| ed6h-dams-evs-epsc-similar | blocked (metadata_insufficient) | Confirmed. The figshare description of article 12611657 v3 says only "experienced females", and nothing separates dams from virgins. |

**B. Problems**

1. **[affects a conclusion] cell 5/20, `group_from_description`:** five subjects (EV56, EV62, NV140, NV64, NV66) are left with no experience group. The claims criterion allows the figshare item titles, and those titles are "EV56_Experienced_Exc", "EV62_Experienced_Exc", "NV140_Naive_Exc", "NV64_Naive_Exc" and "NV66_Naive_Exc". EV56's session description also reads "base_ch72hr". The outcome stays partial because stimulus identity is still missing.
2. **[affects a conclusion] cells 13, 29-38, `invivo_file_sweeps`/`psc_table`:** the measure fails its own positive control.
   - Only 1 of 12 EV and 2 of 14 NV EPSC cells, and 1 of 7 and 0 of 6 IPSC cells, show a call-evoked current of the expected sign. That is about the rate the sham window gives.
   - Only 46-48% of trials have the expected sign.
   - The Methods say every analysed cell had at least five significant prototype-evoked PSCs.
   - The notebook never shows a trial-averaged current aligned to the microphone onset, so a misaligned, diluted or otherwise wrong measure can't be ruled out. Every whole-cell "not reproduced" rests on this.
3. **[affects a conclusion] `psc_table`, "largest 5-10 trials":** trials are ranked by the absolute value of the evoked current, so wrong-sign noise trials get selected. Picking the largest trials in the expected direction is another reading the paper allows, and it was not run. Because EV baseline noise is about twice NV's (s.d. 11.3 vs 5.2 pA), the top-k magnitudes favour EV whatever the response. The sham result in cell 32 shows exactly this, which confounds fig2h and fig2i.
4. **[affects a conclusion] cells 13, 34, 36, 38:** EV has 7 IPSC cells against the paper's 6. The notebook neither explains this nor applies the paper's inclusion rule ("at least five significant prototype-evoked E/IPSCs").
5. **[affects a conclusion] cell 40, ed9b:** the Friedman design (10 columns) and the Dunn family are the author's choices. The two families give different outcomes, and the notebook presents the 45-pair family only as a variant. Two of the seven ACSF cells (191202B and C) have no sweeps after baseline, so all their files may have been read as baseline. Their labels are not printed.
6. **[does not affect a conclusion] `presses`:** because the touch times are printed to five significant digits, the floor of 1.5 times the local step makes the median×2 rule a 1.5 ms gap before 100 s, 15 ms up to 1000 s and 150 ms after that. I checked this on synthetic touches: a 50 ms gap splits a press at t=20 s and t=500 s but not at t=1500 s. Press duration therefore depends on when in the session the presses happen. Separately, `sampling_interval` takes the mean of the intervals, while its docstring and the claims file say median; this is harmless because the floor dominates. Neither point changes the blocked outcomes.
7. **[does not affect a conclusion] cell 22, fig1g:** the per-trial Sn/S1 values come from first responses near zero (cell means range from -1.29 to 4.34). Per-trial and mean-trace give opposite directions at 175 ms. Neither is significant, so the outcome stands.
8. **[does not affect a conclusion] cell 42:** "last baseline" ignores the 24hrsPRE sessions, and NV50 has no "base" session at all. The output only decides that the claim is blocked.

The other helpers I tested on synthetic inputs behave correctly:
- `syllables` and `assign_isi_by_duration` recover all four ISIs exactly.
- `dunn_friedman` gives a type-I rate of 0.045 under the null.

**C. What I could not check**

- **Whole-cell measure:** whether it captures real PSCs. Per-cell trial-averaged current traces aligned to the microphone onset (EPSC and IPSC, by ISI), and the count of cells passing the paper's "at least five significant evoked PSCs" rule, would settle the whole-cell outcomes. So would the results of choosing the top 5-10 trials in the expected direction.
- **Slice pulse timing:** whether `pulse_trains` (the `p1s[i+1]` offset) puts pulses at the stimulus artefacts. An overlay of one sweep with the detected pulse times and peak windows would show this.
- **ed9b labels:** the oxytocin spreadsheet labels behind each role, and the files of 191202B and C.
- **Imaging onsets:** whether call onsets could be recovered from the movies at the known 10 s period (for example by template or phase fitting on single ROIs, not 8×8 block means). Also whether the order in the session-description names (e.g. "61f_5set_1150_850_1300_1600_700") is the playback order; the whole-cell playback turned out to be a fixed order, not pseudorandom. If either held, ed3e and the tone claims could be partly tested.
- **Mouse counts:** which of the 14 First Retrieval mice and the 20 NV-excitatory mice make up the paper's 13 and 12.
