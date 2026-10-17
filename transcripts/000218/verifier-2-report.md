**Verifier report, round 2: Tingley and Buzsáki 2019 (doi:10.1016/j.neuron.2019.10.012) on DANDI 000218, version 0.250624.0439**

The paper text is saved under `paper/` (`PMC6952543_bioc.json`, `PMC6952543.txt`). This round I also looked at the notebook's figures.

The claims file has 31 claims, and the attempt record has 31 outcomes: 4 reproduced, 8 partially reproduced, 9 not reproduced, 10 blocked.

### 1. Outcomes

I agree with 30 of the 31 stated outcomes.

- **fig5d-lag: I disagree.** I would give not reproduced, as in round 1. The criterion defines no partial outcome. The part of the claim that can be measured, a lag of 6.4 ms with CA1 leading, fails on both channels: 0.00 ms on the detection channel (cell 60), and 0.00 or 0.80 ms re-referenced (cell 68). A correlogram peak at 0 ms does not show CA1 leading. The record states the disagreement correctly.
- **fig7e-ca1-depth: I agree it is blocked, but not with the reason.** The notes say raw 20 kHz data exist for all DT2 files and two DT9 files, so waveforms could be re-extracted there. For those recordings the limit is run time, not missing data, so `data_missing` holds only for the rest.
- **fig1c-hfo-each-animal: I agree, because the criterion requires it.** See the first item in section 2 for why the result may come from the criterion's baseline.

### 2. Sentences the outputs do not support

- **Cell 19, the README ("Many of them are not followed by LS firing") and the Summary (cell 76):**
  - The cell 16 figure shows sharp firing peaks locked to the events in DT1, DT2, DT5 and DT9. In DT9 the peak is about 0.00135 against a baseline of about 0.00075 spikes per bin.
  - In DT7, DT8 and DT9 the curve at HFOs lies below the curve at random times across the whole ±100 ms. That is a baseline offset, not a lack of firing at the events.
  - DT2 and DT5 fail the 3 SEM test because neurons vary widely: the differences are 0.031 and 0.034, but the SEMs are 0.025.
  - The outcome follows the criterion, but the wording that says the events are not LS bursts overstates the evidence. This corrects my own round-1 problem 2.
- **Findings, "25 units in 9 files have spike times out of order":** the table in cell 6 lists units from at least 10 distinct files: DT2 3324um-1144um and 3396um-1180um; DT5 20161007, 1017, 1018, 1026 and 1029; DT7 20170314 and 0321; DT8 20170201.
- **Cell 25, "a fifth to a third of the paper's values":** the pooled fraction is 0.027 against 0.16, which is 0.17 of the paper's value, about a sixth.
- **Cell 61 and the fig5d notes, "Without those pairs … DT9 gives 3.8 ms":** the 3.8 ms comes from all pairs, as the median of DT9's per-recording medians (cell 60), not from the pairs that remain after removing same-sample ones. It is also inside the tolerance (2.2 to 10.6 ms), which neither text says.
- **fig1f notes, "Both means are 6 to 7 ms above the paper's":** the CA1 mean is 7.3 ms above (38.3 against 31). This is minor.
- **Sentences with no printed output behind them:**
  - fig6 notes: the archive search that found 000213 and 000233.
  - fig7e-ca1-depth notes: raw data in 27 files, about 1.1 TB.
  - README: "about 23 minutes". Cell 2 prints 21.4 minutes for the streaming step only.

Every other "Result" sentence, the Summary, the README, and the notes I checked match the printed numbers. "As in the paper" (cell 48), the 5 rats plus a tetrode rat (cell 5), and the `paper_inconsistency` finding all agree with the paper's text.

The record states my round-1 reasons faithfully and in my own terms, including the fig5d disagreement and the fig7e-content-independent reason.

### 3. Round-1 points

**Resolved:**
- Problem 5: the phase taken on another shank still gives 189.7° and 52.3% locked.
- Problems 6, 7, 8 and 9: the PETH slice is now `[90:110]`, `starting_time` is printed as 0, and the clock caveats are stated.
- Problem 3: the fixed-window variant is shown. The criterion's window decides the outcome, and I accept that.
- Problem 4 is acknowledged; the data cannot fix it.
- All of section C except the bipolar check: units-table columns and `group_id`, electrode groups and devices, depth against session name, position coverage, and the ripple count per recording.

**Remaining points that bear on a conclusion:**
1. **Problem 1 is only partly resolved.** Re-referencing within the shank cuts same-sample pairs from 34.8% to 4.1%. But:
   - The jittered PLV is still 0.074, against about 0.021 for random phases.
   - The re-referenced event sets are very different (DT5: 4,032 events become 34,492).

   Neither channel is shown to capture the paper's HFOs. This affects fig1c-event-count, fig1g, fig2, fig5d, fig5e and fig5f-no-phase-coherence.
2. **fig1c-hfo-each-animal:** random times across the whole recording are a baseline confounded by state. Measured against each animal's own flanking baseline, 4 of 6 animals appear to show firing locked to the events. The outcome follows the criterion, but the record should say this and should not describe the events as non-bursts.
3. **Problem 2 in revised form:** participation is low (2.7% of LS neurons per event), and that is still what leaves only 106 pairs and blocks fig4-sessions-few-change and fig4c.
4. **fig5d-lag:** the outcome disagreement stands.
5. **fig7e-ca1-depth:** the reason is partly a run-time limit, and the claim of raw data in 27 files is not shown in the notebook.
