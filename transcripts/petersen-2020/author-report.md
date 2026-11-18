I've written the entry at `entries/petersen-2020/` and the record at `attempts/petersen-2020-02.yaml`, and built the handover in `executed/petersen-2020/handover/`. The entry passes `check` and its clean run (`all`) with 0 errors. Of the 46 claims, 17 are reproduced, 18 partially reproduced, 10 not reproduced and 1 blocked. Nothing is committed.

**I saw part of an earlier attempt's results by accident.** I didn't search for any earlier attempt. But the release notes of the pinned version (0.261115.0311, which I read with the dandiset's metadata) say the conversion "fixes problems found by a reproduction attempt (issue #78)". They list what was fixed: electrode groups, trial times one sample late, cooling-state labels, measured versus modelled temperature, unit labels, and known gaps. I didn't open the issue. My findings come from the data, but I knew those topics before I looked.

### 1. Outcomes

| Outcome | Claims |
|---|---|
| Reproduced (17) | fig2h, fig2j (4 of 5 rats testable), fig2i, disc-theta-12%, fig6e, fig6c, fig6h, fig4e, fig5-speed, suppl2ab, suppl5gh, fig4b, fig3hi, fig4f, suppl2e, fig5e, fig5i (rests on an assumption) |
| Partially reproduced (18) | session-structure, cooling-time-course, fig2g, fig6d, fig6f, fig6g, suppl5j, suppl2, disc-interneuron, fig4c, fig4a, fig3d, suppl3e, fig4gh, suppl3, fig5d, fig5h, suppl2d |
| Not reproduced (10) | fig6i, fig4ac, fig3c, fig3e, fig3f, fig4d, fig5cg, fig5j, fig5k, suppl1g (waveforms, measured on 4 sessions) |
| Blocked (1) | suppl1-hippocampal-temperature (`data_missing`) |

The 21 outcomes on place fields and pairs are marked `assumed`. fig5cg is weakly supported: the surface fit converges poorly (pooled fit R² is −0.14, and only 5 to 10 of 23 sessions converge).

### 2. The dataset, assumptions and questions

**Pinned version:** 0.261115.0311, the latest published one; the paper cites no version. It has 51 sessions from 5 rats; the paper reports 53.

**What the data show against their description:**
- The tracking descriptions say 40 Hz in every session, but the timestamps give about 120 Hz in 44 sessions, 40 Hz in 6 and 30 Hz in 1.
- Only 31 sessions have a measured MS temperature; the other 20 hold the lab's modelled curve, so MS10 has none at all.
- The measured traces contain artefacts, from −1751 to 1354 °C and runs at the 0 and 50 °C rails.
- The two 2018-07-19 sessions are labelled as cooled, but their temperature doesn't fall.
- 13 sessions have two cooling epochs, two of them with cooling intervals that run far past the last trial.
- The lab's theta channel in MS13-171130 is marked bad, and some theta-maze epochs are labelled with a linear-track environment.
- The dandiset holds no hippocampal temperature, no unit waveforms and no place fields. 23 sessions have no curated units.

**Assumptions:**
- Place fields are found on the rate map over all trials of an arm, so each field has the same boundaries in every state.
- For fig5i, a pair's phase lag is the largest peak within π of zero. Under the other reading (nearest peak) the claim fails.

**Questions for the authors** (recorded as `methods_unavailable` findings):
- Which rate map were the fields found on?
- Which peak defines a pair's phase lag?
- What was the surface-fit procedure, since its equation is garbled in the text?
- Can the hand-drawn fields of Figures 3 and 4 be released?

I asked a reader no questions.

### 3. Where the protocol was unclear or missing something
1. **Too many reading combinations.** Running every reading for every claim multiplies out. For place fields I ran 5 and 3 cm bins with the lab states, plus the 12-minute states at 5 cm only, and maps from all trial frames only. The notebook says so.
2. **Absence claims and measure readings conflict.** The rule "absence is judged on the paper's test alone, readings do not apply" clashes with step 1.6 when the measure itself has readings (fig5i). I took the best-supported reading as an assumption and showed both.
3. **Release notes can unblind a repeat attempt.** Nothing in the blind rules covers archive metadata that summarises an earlier attempt's findings. I reported it above.
4. **Default tests on large samples break the absence claims.** Signed-rank or rank-sum over hundreds of fields or tens of thousands of cycles (fig4ac, fig3f, fig5j, fig5k) detects very small effects. I followed the criteria and showed per-session variants.
5. **No block reason for "out of run time".** It's unclear whether to use `too_large` or `not_runnable`. It didn't matter in the end: I measured the waveform claim on a subset instead of blocking it.
6. **Prep-only checks can't go in the record.** A check run outside the notebook showed many precession slopes at the ±2π search limit. The protocol forbids outside numbers in the record, so I removed them and left a qualitative note on fig4d.
7. **The entry directory didn't exist.** The prompt said it was empty; I created it.

### 4. Runtime and failures
- The notebook runs in about 16.4 min, peaking at 4.7 GB of memory. This session ran from 13:21 to 16:08 UTC.
- An early pair cross-correlogram version took 27 minutes, and the first surface-fit version took 20. I vectorised the pair code (it now takes 18 s) and capped the fit evaluations.
- My first record failed the schema check because assumed outcomes need deviations; I fixed it.
- One Result cell (fig3f) went stale after a code change. I caught it, corrected it and re-ran the notebook.
