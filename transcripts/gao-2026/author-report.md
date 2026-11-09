I've done Author steps 1 to 6 on DANDI:001683, version 0.260109.2104. That is the only published version and the paper cites none, so I pinned it. The entry is `entries/001683-gao-2026/`: three notebooks and a helper, `tfus.py`. The record is `attempts/001683-gao-2026-01.yaml`. `entry.py check` reports 0 errors, `entry.py all` passes, and the handover is in `executed/001683-gao-2026/handover/`. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig2c-sham-duration-stable | not reproduced |
| fig2d-seizures-under-two-minutes | reproduced |
| fig2e-sham-count-stable | reproduced |
| fig2f-sham-percent-time-post3 | reproduced (assumed) |
| fig3a-count-reduction | reproduced |
| fig3a-count-sham-vs-tfus | reproduced |
| fig3b-percent-time-reduction | reproduced |
| fig3b-sham-percent-time-no-change | not reproduced (assumed) |
| fig3b-percent-time-sham-vs-tfus | not reproduced |
| fig3c-interval-increase | reproduced (assumed) |
| fig3c-interval-sham-vs-tfus | reproduced |
| fig3d-duration-decline | not reproduced |
| fig4-no-theta-alpha-gamma-power-change | not reproduced (assumed) |
| fig4c-beta-decrease | partially reproduced |
| figs4-sham-power-no-change | not reproduced (assumed) |
| fig4ef-ai-increase | partially reproduced |
| fig6-epileptic-pli-s1-decrease | partially reproduced (the S1-specific decrease is not seen; the criterion's partial clause still applies) |
| figs5-seizures-lower-ai | blocked: data missing (the comparison with 0 does hold) |
| figs7-seizure-pli-s1-vs-non-s1 | blocked: data missing |
| fig5b-tfus-evoked-potentials | blocked: methods underspecified (the criterion's own readings disagree) |
| fig5cdj-wild-type-gamma-pli-decrease | blocked: data missing (no sham EEG) |
| fig5ghi-low-band-pli-s1-only | not reproduced |

## 2. Dataset, assumptions, questions

**What the dataset holds:**
- All 16 epileptic rats: 10 tFUS with 4 blocks each, 6 sham with 5 blocks each, with the paper's seizure labels.
- The labels reproduce the percent changes of Fig. 3 to within 0.5 point. This needs each rat's change from its own baseline, and the interval read as the gap between one seizure's end and the next one's start.
- The target-confirmation LFP recordings of all 23 rats.
- EEG recordings of 20 ms pulses, labelled for PLV analysis, for 20 of the 23 rats.

**Problems with the dataset:**
- The seizure label times are in minutes, not seconds. The EEG confirms it: 30 to 80 Hz power is higher inside the labels in all 136 block-hemispheres, and the contrast disappears when the labels are shifted.
- BH635's block files are mislabelled: two SHAM files, one file named for rat BH636, and no post3.
- BH649's post 3 file has the session id `None`.
- Every file says the rats are Wistar (HSD:WI), aged 24 weeks; the paper says Sprague-Dawley, 3 to 6 months.
- The EP files are described as EEG but hold the intracranial LFP.
- Most of the files labelled "1Hz" have pulses every 2 s.
- Missing: the EEG before 4-AP, the resting EEG of the wild-type phase, and three rats' PLV files.
- The files don't record the labelling channels, the S1 channels or the chosen transducer position.

**Assumptions**, each recorded as a deviation:
- **Repeated-measures ANOVA:** I took this as the paper's "two-way ANOVA" wherever the two readings disagree on a claim of absence. It is the only reading that gives the paper's significant within-group changes in Fig. 3.
- **BH635's blocks:** taken in time order.
- **Inter-seizure interval:** the gap from one seizure's end to the next one's start.
- **Channels:** 8 and 25 for labelling, from the Fig. S1 drawing; the S1 channels from the PLV files' notes.
- **No ICA**, because which components were removed is not recorded.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- Which ANOVA type and which Bonferroni families were used?
- For Fig. 5B: which channels, which transducer position, which sham onsets?
- Which segments were analysed for band power, AI and PLI, and how was AI normalised?

**Reader questions:** none.

## 3. Where the protocol was unclear

1. **Correct but too generous criteria.** fig6's partial clause makes it "partially reproduced" even though the non-S1 condition fails. I applied the criterion literally and flagged this in the notes.
2. **Blocked claims with a testable part.** Neither the protocol nor the criteria say what to do. For figs5 and fig5cdj I blocked the claim (`data_missing`) and put the testable part's numbers in the notes.
3. **ANOVA readings that disagree on a claim of absence.** The absence rule says to use "the paper's test", but the claims file leaves that test open (M3). I adopted one reading by step 1.6 and used it consistently.
4. **No single Bonferroni family for all claims.** The criteria let each claim pass "under one reading", so different claims of the same figure pass under different families (fig3c). I recorded this in the notes.
5. **"Data the paper describes" versus extra data.** The PLV files fit the Methods better than the claims file's reading of them. I used them and recorded a deviation, without asking a reader.
6. **No per-notebook run.** `entry.py` cannot run a single notebook, so a one-line fix to a data-check cell cost a full 22-minute rerun.

## 4. Runtime and failures

- Notebook runtimes: `seizure_metrics` 1 min, `eeg_blocks` 13.5 min (streams 205 GB), `wild_type` 7.7 min.
- Each full `entry.py all` run took about 22 min; I ran it twice.
- The work ran from 08:14 to 09:56 UTC.
- Nothing failed.
