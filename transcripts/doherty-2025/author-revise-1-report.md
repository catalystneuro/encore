I've worked through every point of the verifier's round-1 report and re-run the entry with `python tools/entry.py all entries/001444-doherty-2025`. The check gives 0 errors, the notebook runs in 342 s, and its outputs match my development run. The record now has 18 reproduced, 15 not reproduced, 2 partially reproduced and 5 blocked. Nothing is committed.

**Outcomes I changed**
- **fig2c-control-it23-rate-activated:** partially reproduced → not reproduced. I paired the cells kept in either file, with 0 where a cell is absent, as problem 1 asked. The Wilcoxon test then gives 0.69 and the paired t-test 0.0013, so the criterion fails under both ways of pairing.
- **fig5c-pd-it23-rate-activated:** partially reproduced → not reproduced. No pairing gets all four tests below 0.001: Mann-Whitney stays at 0.0018, and with the cells kept in both files the paired tests find no increase (0.60 and 0.21).
- **rest-synchrony-increase:** not reproduced → reproduced, marked as resting on an assumption. Counting coincident 1 ms bins or the spikes in them hits its ceiling (two or more PT5B cells fire in every bin), so those counts cannot show synchrony. Counting pairs of cells firing together is the one count that can exceed its expectation. Under it, and under every window setting, the parkinsonian rest file has more significant synchrony than control: 3.8 to 3.98 s against 0.8 to 1.65 s.

**Disagreements I kept and recorded**
- **fig1-network-size:** still not reproduced, where the verifier gave partially reproduced. The criterion counts stored units, and that count fails.
- **activated-pt5b-rate-pd-vs-control:** still partially reproduced, where the verifier gave not reproduced. Every test finds the increase, and only Mann-Whitney misses the p < 0.001 bound (0.0052).
- **fig4-control-unitary-events and fig7-pd-unitary-events:** still not reproduced, where the verifier gave blocked. I ran the extra ways of counting coincidences it asked for, and no setting under any count meets the criterion. The rest duration in fig4 comes out at 0 s, 0.8 to 1.65 s, or 3.2 to 3.99 s depending on the count, against the paper's 0.7 s.

**What I added or corrected**
- **Paired tests:** both pairings (cells kept in both files, cells kept in either) are now shown for every rate claim. Only pd-it6-rate-unchanged depends on the choice. With the cells kept in either file a test finds a difference (p ≈ 0.002). It stays reproduced, on pairing only cells kept in both files, which keeps each paired rate inside the group whose mean is tested. That choice is recorded as an assumption.
- **Unitary events:** the helper now has four ways to count coincidences. Each one's false-positive rate is measured on simulated independent cells, and the verifier's synthetic test cases are included. The notebook also prints how often the bin count is at its maximum.
- **Spectrogram (S2):**
  - The 2 Hz check now also runs with 1 s and 2 s windows.
  - Burst rates are now taken over the full 2.3 s window, fixing the roughly 11% overstatement.
  - No outcome changes.
- **New data-check cell:**
  - The LFP and membrane-potential series start at 0 s at 40 kHz.
  - "LFP 0" records no electrode or depth, and the files have no electrode table.
  - The units table has no field listing cells that never fired.
- **Questions for a reader:** two added to `questions/001444.yaml`. One is about how the coincidence share and unitary-event counts are measured (problem 3). The other is about the burst definition and the unsmoothed histogram used for the duty cycle (problem 7).
- **Record and summaries:**
  - The round is recorded under `verifications`.
  - The record's notes and deviations, two questions to the paper's authors, the conclusions, the summary and the README now match the new numbers.

**Not done**
- The mean over 11 electrodes still cannot be computed, because the files hold one LFP trace.
- I could not establish which electrode "LFP 0" is. It is still taken as electrode 0.
