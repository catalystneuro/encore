I've finished steps 1 to 6 for dandiset 000003. The entry locks, passes `check`, and the notebook runs from a clean environment in 8.1 minutes (twice, with identical outputs). The handover package is built in `executed/000003-senzai-2017/handover/`. Nothing is committed.

**Paper:** I used the full text, from the accepted author manuscript in PubMed Central (PMC5293146), saved under `paper/`. The supplementary figures were not available.

**Version:** pinned to 0.260218.2052. The paper cites no DANDI version. All four published versions hold the same 101 files (same paths, sizes and checksums) and differ only in metadata, so I took the most recent. The notebook header says this and prints the comparison.

### 1. Outcomes (31 claims: 15 reproduced, 11 partially, 3 not reproduced, 2 blocked)

| Claim | Outcome |
|---|---|
| unit-counts (586 GC, 500 MC; here 609 and 568) | partially reproduced |
| first-stage-labels | partially reproduced |
| interneuron-rates | partially reproduced |
| gc-narrower-waveform | reproduced |
| optotag-drd2 (64% of MC suppressed here, paper 27%) | partially reproduced |
| mc-more-active | reproduced |
| gc-nrem-highest | partially reproduced |
| ca3-wake-highest | not reproduced |
| nrem-wake-ratio | reproduced |
| theta-modulation | reproduced |
| gamma-modulation | reproduced |
| gamma-rate-correlation | partially reproduced |
| ds2-recruitment | reproduced |
| monosyn-gc-to-mc (65 pairs one way and 8 the other here; paper 32 and 0) | partially reproduced |
| burst-facilitation | reproduced |
| state-transmission | not reproduced |
| zero-lag-synchrony | partially reproduced |
| tmaze-central-active | partially reproduced |
| tmaze-multiple-fields | partially reproduced |
| tmaze-peak-info | reproduced |
| tmaze-splitters | reproduced |
| remap-positive | reproduced |
| remap-gc-lt-mc | not reproduced |
| remap-fractions | partially reproduced |
| pv-remap | reproduced |
| inheritance-tmaze | reproduced |
| inheritance-openfield | reproduced |
| mc-deeper (17 files only) | reproduced |
| gc-mc-classification (17 files, 94.4% agreement with the labels) | reproduced |
| gc-mc-distance | blocked: metadata_insufficient |
| gc-backpropagation | blocked: metadata_insufficient |

### 2. What I found about the dandiset
- **Corrupted spike trains in 24 files.** The first unit's spike train is cut short by a multiple of 65,536 spikes, and the missing spikes sit at the start of the second unit's train. It looks like an integer overflow at conversion. The loader moves them back and reports each repair.
- **Genotypes don't match the paper.** The files give 6 SST-Cre, 5 Drd2, 4 POMC-Cre::Arch and 1 POMC-Cre::Ai35. The paper gives 7 SST-Cre, 5 DRD2, 3 POMC and 1 wild type.
- **Recording sites are mostly missing.** 83 of 101 files don't say which shank a unit was on, and no file gives site coordinates (x, y, z are NaN). That leaves depth testable on 17 files only and distances not at all. The units table comes in two layouts.
- **The authors' detected connections weren't converted.** The monosynaptic pairs file was skipped by the conversion code, so the pair-based figures can't be checked on the authors' own pairs.
- **Undocumented fields.** The T-maze position series and the state labels (`quiet`, `transit`) have no description; I inferred their meaning from the values. Interneuron labels don't say whether a unit is in the dentate gyrus or CA3.
- **Counts differ from the paper.** There are 568 mossy cells against the paper's 500, plus 237 units labelled `missing`.
- **Smaller issues.** One file has 24,286 duplicate light-pulse times. The paper gives two burst-index thresholds (1.2 in the Methods, 1.8 in the Figure 1A legend).
- **No duplicate recordings.** The second files on seven same-day pairs (`b` sessions) are separate recordings, not copies, but the metadata don't say what they are.

### 3. Where the protocol was unclear, wrong or missing something
1. **Writing criteria before analysis.** Building and debugging the helper on all files printed preliminary results before I wrote the criteria. I listed in the claims file exactly what I had seen, and tuned nothing on it.
2. **Deposited labels versus re-running the classification.** The protocol is silent on this. I used the labels for all claims and tested the paper's classification as a separate claim.
3. **Code to read.** Neither the paper nor the dandiset links code. I read the NWB conversion code (two commits) and recorded it in the notebook header, not under `inputs`, since it supplies no data.
4. **Repairing broken data.** "Trust the data" doesn't say whether to repair a detectable format error. I repaired it in the loader and recorded it as a finding.
5. **Tolerance for a reported zero.** The 10% rule gives zero tolerance for "none of 202". I put a bound (below 0.05) in the criterion instead.
6. **Dependents of partially reproduced claims.** The `depends_on` rule only covers blocked claims. I tested the dependents and said in their notes that they rest on the automatic pair detections.
7. **Finding new metadata mid-attempt.** I found the shank information in 17 files after writing the criteria. I added criteria for two claims I had planned to block, before running them, and recorded the timing and the one preliminary result I had seen.
8. **Multiple readings make passing easier.** For "earlier/later phase" the outcome depends on where the phase cycle is cut. I listed both cuts, and the claims pass on one. This rule lets ambiguous claims pass easily.
9. **Clock check for continuous sessions.** The suggested contrasts assume trial tables. I used state labels shifted by 30 minutes, and spikes shifted by 20 s against positions.
10. **Same unit across days.** Each unit has its own ID and the probe moved 70 µm a day. I stated "once per day" as an assumption.
11. **Supplementary figures unavailable.** Claims citing them rest on the main text.

### 4. Runtime and failures
- **Notebook:** 8.1 minutes, of which loading takes 4.6.
- **Total session:** about 3 hours.
- **Slow first loader:** the first version used threads and took 50 minutes, because h5py runs only one thread at a time. I switched to processes.
- **Bugs found and fixed before the final run:**
  - The first T-maze run detection mistook the waiting area for the reward port. This is the one change made after seeing results, and it is recorded.
  - A column named `info` clashed with a pandas method.
  - A table variable named `C` clashed with the C() term in the ANOVA formulas (statsmodels).
- **Unexplained files:** about ten unexpected untracked entries appeared in the repo root (`.bashrc`, `.idea`, `scripts` and others). They are device files that appeared at 02:07, about when the session began, and I didn't create them. I left them alone; check they don't get committed.
