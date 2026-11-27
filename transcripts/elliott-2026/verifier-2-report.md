**Verifier report, round 2: Elliott, Andrews et al. 2026 on DANDI:001132**

The claims file has 24 claims. The attempt record has 24 outcomes: 6 reproduced, 7 partially reproduced, 8 not reproduced, 3 blocked. "Spike nb" means `reproduce_elliott_2026.ipynb` and "LFP nb" means `lfp_elliott_2026.ipynb`.

### 1. Outcomes

I agree with all 24 outcomes. Five need a comment.

- **s4-ka-no-epileptiform (partially reproduced, assumed): agree.**
  - Once only synchronized bursts are kept (more than half of the units rising), S3 to S6 have none under any reading. S1 has 77 to 138 and S2 has 89 to 134 (spike nb cell 35).
  - The positive control still fails for S1: its longest epoch is 8 to 10 s, and it is the same with every burst kept. So the miss comes from the 5 s gap rule, not from the synchrony filter.
  - The criterion does not define a partial outcome. "Partial" fairly describes a case where neither of its clauses applies.
  - Both assumptions are stated in the deviations and are reasonable: "synchronized" means more than half of units rising, and "sustained" means an epoch longer than 10 s.
- **ext3-onset-spectral-signature (reproduced, assumed): I now agree; in round 1 I said partial.**
  - The new variant uses the first epoch that has 5 s of recording before it, under the criterion's own burst reading (b). It gives 3 of 3 electrodes in both electrode sets (LFP nb cell 40). So the result no longer rests only on the author's 14.4 s onset.
  - The criterion names the 0.1 to 100 Hz amplitude as an allowed reading, so "reproduced" follows from it.
  - The assumption is stated and reasonable: the criterion's own onset (0.73 to 0.90 s) leaves no 5 s baseline and falls inside the wavelet's edge region.
  - The notes should keep saying that the theta-amplitude reading fails at every onset (0 of 3 everywhere; at most 1.92x).
- **table2-phase-locking-counts (not reproduced): I now agree; in round 1 I said partial.** The criterion and the claims file's opening comment make the Methods' envelope selection the main reading and the code's cycle selection a variant. Under the envelope selection S1 gives 60, outside 70 ± 7. One condition remains (section 3a).
- **fig2b-phase-cluster-kuiper (reproduced): agree only by the letter of the criterion.**
  - Under the Methods' spike selection, the only reading with p ≤ 0.01 is reading (b). That split cannot fail (p = 0, LFP nb cell 18).
  - The spatial readings under the Methods' selection give 0.037 and 0.11, which would be partial.
  - The record treats the cycle selection as a variant that does not count in table2. For consistency, this outcome then rests on a test that carries no evidence.
- **methods-rolling-wave-counts (blocked): agree.** The criterion's detector was run and finds 0 rolling waves in 63 cycles (LFP nb cell 34). Adopting it would give not reproduced. Declining to adopt it is allowed by the criterion and the reason is given.

The other 19 outcomes are supported by the outputs I cite in section 2 and need no comment: link, table1, fig1g, burst counts, rate, onset latency, fig1j, ext4b, ext4, fig2a, table2-seizure-vs-not, fig2c, the two ext9 claims, the two fig3a claims, ext10, table3 and ext12.

### 2. Sentences against the printed outputs

The "**Result:" cells I checked hold against their outputs: spike nb cells 15, 18, 24, 28, 31, 37, 43, 46, 49, 53, 58, 61 and 64, and LFP nb cells 13, 16, 19, 26, 29, 32, 35, 38 and 42. Exceptions:

- **Attempt record, ext4 notes and round-1 response.** The record says "every window of one theta cycle or longer passes under all five seeds (250 ms …; 500 ms …; 1 s …; 35.0 to 35.5 s …)". The response says "250 ms, 500 ms and 1 s … all pass under all five seeds". Cell 24 runs the five seeds only for the 250 ms and 500 ms windows. The 1 s and 35.0 to 35.5 s windows were run with one seed (cell 23). Notebook cell 26 itself does not make the five-seed claim.
- **Attempt record, finding 5.** "electrode locations are all 'unknown'" is not shown by any printed output; spike nb cell 3 prints age and sex only.
- **LFP nb cell 42.** "amplitude ratios 0.77 to 1.31" is the broadband range only. The theta ratios at those onsets reach 1.91 (cell 40). This is minor.
- **Spike nb Summary (cell 67), "What was found about the dataset".** It leaves out the possible sub-3C duplicates, which are a major finding in the record and are shown in cell 5.

The README sentences and the other notes in the record are supported by the outputs.

My round-1 reasons appear in `verifications` in my own words. Each of the 14 problems is attached to its claim, and the agree/disagree flags are right (ext3 and table2-counts disagree; all others agree).

### 3. Round-1 points

Resolved:

- Problem 1 (s4 synchrony).
- Problem 2 (ext3 onset): the criterion's onset was rerun under all four readings, and a variant with a 5 s baseline was added.
- Problem 3 (S2 initiation windows; sub-burst sources printed, LFP nb cell 8).
- Problem 4 (ext12 reason). The NEST 3.10 and NESTML trials were run outside the notebook and are not shown.
- Problem 5 (bin edges: markdown corrected, edge weights and half-bin offset in cell 57).
- Problem 7 (baselines now burst-free, cell 21).
- Problem 11 (spans and windows printed beside their source, cell 8).
- Problem 12 (ext9 second eigenvector).
- All of section C: repository inputs printed, S5 shown absent from the 3C files by the 40 s test, the requested s4, ext3 and S2-window outputs added.

Problems 6, 8, 9 and 13 are claims-file questions now put to a reader. Problems 10 and 14 are stated in the notes.

What remains that bears on a conclusion:

- **a. table2-phase-locking-counts.** The criterion keeps spikes while the envelope exceeds "the RMS of the whole series". `hippo.phase_lock_unit` uses the RMS over the analysed windows only, which for recordings 1 and 3 means the seizure windows (`hippo.py:453-454`). Notebook cell 9 says this, but the record does not list it as a deviation. S1 misses by 3 units (60 against at least 63), so the outcome could turn on it. The run needed is the envelope selection with the RMS taken over the whole recording.
- **b. fig2b.** "Reproduced" rests on circular reading (b), as set out in section 1.

### 4. Critical findings

No finding is rated `critical`. Severities in the record: findings 1, 2, 3 and 8 are major; 4, 5 and 6 are minor; 7 is none; 9 to 14 are about the paper and carry no severity.

I would re-rate one:

- **Finding 8 (sub-3C-1 to sub-3C-4 may be copies of one recording).** Spike nb cell 5 shows what it states:
  - The 6 pairs among these files have 78 to 82% identical samples and correlations of sample-to-sample changes of 0.86 to 0.90.
  - The 24 other same-length pairs of a slice have 4 to 8% identical samples and correlations of -0.013 to 0.011.

  I would rate it **critical**. If confirmed, this is one recording deposited as several files, and nothing in the files shows it. A user treating these as four recordings would count one recording four times.

  The evidence covers 1 s and 64 channels only. A comparison over the full 40 s and all channels should be run to settle it. If the files turn out to share a common artifact rather than being copies, major would fit. No analysis in this attempt uses these files.
