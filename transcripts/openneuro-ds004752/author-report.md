I finished steps 1 to 6: the entry is written, locked, checked and run (it passed in 18 min, 0 check errors), the attempt record is written, and the handover package is built. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| cohort-sessions | partially reproduced (68 sessions, not 71) |
| fig1b-accuracy | reproduced |
| capacity-cowan-k | reproduced |
| fig1c-response-time | reproduced (median; correct trials without the artifact flag) |
| fig2bc-gamma-encoding-p1 | partially reproduced (H3 rises 179%, C2 only 17%) |
| fig2d-cortical-beta-maintenance-p1 | reproduced |
| hipp-beta-maintenance | not reproduced |
| fig2fg-plv-theta-p1 | not reproduced (PLV at C3 is 0.16 to 0.24, not 0.4) |
| fig2h-gc-reversal-p1 | reproduced, assumed (only hippocampal reading h1 with the per-frequency test) |
| fig2ijk-spatial-spread-p1 | not reproduced |
| fig3-gc-reversal-p2-p3 | partially reproduced, assumed (Participant 3 only, reading h2) |
| fig3no-p4-right-no-gc | not reproduced (the paper's test finds GC at every contact) |
| table1-left-hemisphere-sources | blocked: not_runnable |
| fig4a-group-gc-reversal | not reproduced |
| scalp-temporal-laplacian | not reproduced |
| fig4bc-auditory-strongest | not reproduced |
| fig4d-reversal-all | not reproduced (medians about half the paper's) |
| table1-heschl-dgranger-correct | partially reproduced, assumed (signs match under d2; at most 3 of 30 values within tolerance) |
| fig4e-lpfc-no-reversal | reproduced |
| fig4f-incorrect-no-reversal | blocked: data_missing |
| balanced-correct-subset | reproduced, assumed (only under d2) |

Totals: 7 reproduced, 4 partially, 8 not reproduced, 2 blocked.

## 2. Dataset, assumptions and questions

**What the dataset holds**
- participants.tsv maps each subject to the paper's participant number. The ECoG participants are sub-10 to sub-13.
- There are 68 sessions and 3353 trials, against the paper's 71 × 50. The correct trials number exactly 3045, the paper's count.
- Pathology differs from Table 1 for participants 5, 6 and 15; 5 and 6 look swapped.
- Every channels.tsv has the low and high cutoffs swapped (1000 and 0.5 Hz).
- The EDF headers leave the physical unit blank.
- In sub-11 the contacts named PHL and PHR have their hemisphere letters reversed relative to the MNI x coordinate. In sub-01, 12 atlas labels name the wrong hemisphere.
- 17 trials are placeholders (set size 0, no response), and ProbeLetter is missing for sub-10 to sub-15.
- The README's list of virtual sensors (it names Broca) does not match the files (DLPFC, OFC, PPC, AC, V1).

**Derivative source files**
- They carry no trial numbers. I matched them to the events in order and confirmed it against the raw EEG: 40 of 40 trials per subject.
- They hold correct trials only. No beamformer filters are deposited, which is why fig4f is blocked.

**The main finding: how ΔGranger is summarised decides the group results**
- The paper's code takes the minimum over 4 to 8 Hz in encoding and the maximum in maintenance (reading d2). That statistic produces the paper's sign pattern by construction:
  - it gives the same "reversal" for every brain area;
  - reversing it (maximum in encoding, minimum in maintenance) gives the mirror pattern;
  - it gives the pattern even on spectra with no direction.
- The band mean that the Results describe ("We averaged ΔGranger", reading d1) shows no effect.
- In the code, the same Granger spectrum row is also stored as opposite directions in encoding and in maintenance. This is recorded as `code_mismatch`.

**Assumptions**
- The paper does not say which hippocampal contact, electrode or white-matter reference was used. I chose them by rule (left electrode first, first unlabelled contact numbered 3 or higher as reference); the rule is stated in `wmflow.py`.
- Reading h1 was adopted for fig2h; reading d2 for table1 and balanced-correct-subset.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings)
1. Which hippocampal contact and reference were used, and which contact was the ECoG reference?
2. Is the per-participant ΔGranger the band mean or the extreme value, and was the 10% subsampling aggregated by median or mean, over 20 or 200 draws?

**Questions to a reader:** none.

## 3. Protocol issues

1. **Readings that disagree.** The claims file lists the readings (d1 and d2) and its criteria say any matching reading counts, but step 1.6 asks the author to adopt one as an assumption. I applied the any-reading rule and set `assumed: true` with deviations. The protocol does not say what to do when the matching reading is shown to make the effect by construction; I recorded the outcome and put the controls in the notes and findings.
2. **"Unable to decide" includes an uninformative test.** The paper's direction-swap null flags nearly every contact, including Participant 4, whom the paper reports as showing no GC. The protocol has no rule for that case. I reported the outcomes as tested and stated this in the notes.
3. **Time limit versus completeness.** To keep the notebook near 18 min, I ran the per-contact grid tests and the spatial test with reading h1 only, and used 20 draws (the code's number) for the non-auditory areas. This is recorded as deviations. The protocol does not say whether these partial runs belong under `too_large`.
4. **Paper code read by the author.** It was needed for method details. I cited it but did not list it under `inputs`, since no data came from it.

## 4. Runtime and failures

- The run took about 2 h 10 min. The notebook ran twice in full (18 min each); the second run had identical numbers.
- One full dev run of the group analysis took 15 min, so I made the spectral factorisation stop each spectrum separately at tolerance 1e-5; the change in GC is below 1e-5.
- No step failed. Warnings that remain: an MNE deprecation (the `standard_1020` montage name) and a pandas FutureWarning.
- The repository root has untracked placeholder files (`.bashrc`, `scripts`, `.idea` and others, character devices created at 08:55). They are not mine; the commit should leave them out.

Files are in `entries/openneuro-ds004752-dimakopoulos-2022/` and `attempts/`:
- `entries/openneuro-ds004752-dimakopoulos-2022/reproduce_dimakopoulos_2022.ipynb`
- `entries/openneuro-ds004752-dimakopoulos-2022/wmflow.py`
- `entries/openneuro-ds004752-dimakopoulos-2022/entry.yaml`
- `entries/openneuro-ds004752-dimakopoulos-2022/README.md`
- `attempts/openneuro-ds004752-dimakopoulos-2022-01.yaml`
