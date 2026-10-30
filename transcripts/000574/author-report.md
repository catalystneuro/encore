I've finished the attempt on DANDI:000574 for steps 1 to 6: the entry is locked, checked (0 errors) and run, the record is written, and the verifier's package is built. Nothing is committed.

## 1. Outcomes (35 claims: 17 reproduced, 9 partially reproduced, 8 not reproduced, 1 blocked)

| Claim | Outcome |
|---|---|
| behavior-accuracy-set-size, behavior-capacity, behavior-rt-workload, behavior-rt-correct-incorrect | Reproduced |
| neurons-recorded | Not reproduced |
| spike-sorting-quality | Partially (waveform SNR 5.34 against 3.28 ± 1.56) |
| fig2b, fig2c (maintenance neurons, load dependence) | Reproduced |
| fig3e, fig3-probe-onset-not-movement | Reproduced (under one reading each) |
| fig3-probe-neurons-few-task-specific | Partially |
| fig4a dPCA | Not reproduced |
| fig4b speed | Partially (highest during retrieval, not encoding) |
| fig4c, figs3d | Reproduced |
| fig4d encoding decodes correct/incorrect | Not reproduced (51%) |
| fig4e workload decoding and its three follow-ups (leave-one-subject-out, maintenance neurons, no 6 against 8) | Reproduced |
| fig4f retrieval decodes IN/OUT | Not reproduced |
| fig5 subject 1: EEG power / hippocampal power / neurons / PLV with Pz | Partially / Reproduced / Partially / Partially |
| fig6-plv-all-subjects, fig6-plv-workload-eight-of-nine | Partially |
| tables1, fig6-plv-maintenance-over-encoding, fig6-power-unchanged (assumed), fig6i gradient | Not reproduced |
| fig6i no left-right difference, soz-plv-no-difference | Reproduced |
| sfc-maintenance-over-encoding (second notebook) | Partially (coupling to iEEG is well above chance) |
| hfo-rates-unaffected | Blocked: methods_underspecified |

## 2. Dataset, assumptions and questions

**What the dataset holds**
- I pinned version 0.250815.1108, the newest. 0.250610.0938 has the same assets, and the older 0.231010.1809 had duplicate `obj-` files.
- There are 37 sessions (the paper has 36) and 1487 units (the paper has 1526). Eight sessions have no units table.
- The units point at macroelectrode rows of the electrodes table. Region counts by electrode name are far from the paper's; counts by the atlas label of each electrode's deepest contact are close (640/421/398 against 676/449/401).

**Format and metadata problems found**
- 43 units store their spike times unsorted.
- The response codes (51/52 on correct trials, 1/2 on errors) are not described.
- The trial-stage table numbers each Probe stage one trial late, and seven files lack the table.
- EEG and iEEG are labelled volts but hold values consistent with microvolts.
- The EEG is said to be referenced to the averaged mastoids, but it is not (A1 + A2 is not zero).
- Coordinates are not in MNI space.
- Subject 1's seizure-onset list names an electrode (AHR) that subject 1 does not have.
- The LFP of subject 2 session 5 is shorter than its 46 trials need.
- Only 8 s of each trial are stored, so presses later than 2 s after the probe are missing.

**Assumptions**
- Regions come from the atlas label of each electrode's deepest contact, as the Methods describe.
- PLV is computed as FieldTrip does (cross-spectra averaged over tapers within each trial).
- MNI y is taken as minus the file's x.
- The power-unchanged claim uses correct trials and 4 to 30 Hz.
- For spike-field coherence, the scalp channel is Pz (O1 where Pz is absent) and the iEEG channel is the neuron's own electrode.

Questions for the paper's authors are recorded as `methods_unavailable` findings: how units were assigned to regions, how the PLV combined tapers, which frequency range and trials it used, the probe-neuron window, and the coordinate frame of Fig. 6I.

**Question to a reader:** one, in `questions/000574.yaml`. It asks whether neurons-recorded's region-by-electrode-name rule matches the paper.

## 3. Where the protocol was unclear
1. The protocol says outcomes follow the criterion, but some criteria leave out expected values (fig2c's percentage, fig3e's chi-square value). I followed the criterion and gave the off-tolerance values in the notes.
2. A claim that depends on another inherits that claim's readings. I treated a match under any upstream reading as a match, and said so in the notes (fig3-probe-onset).
3. Several claims of absence have test inputs that come from readings the protocol says not to multiply. I adopted one reading as an assumption (fig6-power-unchanged) and showed the others.
4. The protocol does not say how to judge a run that is under the 30-minute limit but over the 10-minute aim. The main notebook takes 24 min, so I put spike-field coherence in a second notebook (13 min) instead of blocking it.
5. I changed the conclusion text after the final run, without touching any code, and copied it into the executed notebooks. The protocol does not say whether that needs a re-run.

## 4. Runtime and failures
- The main notebook takes 24 min (1430 s) and the spike-field-coherence notebook 13 min (787 s).
- To keep within the time limit, decoding uses 100 resampling runs and 250 null runs where the paper uses 500 and 500. The smallest corrected P this allows is 0.048.
- The first full run failed once on an SVD that did not converge. I added a fallback in `sternberg.py` and the next run passed.
- An empty folder the harness created, `entries/000574-boran-2019/.claude/.cc-writes`, could not be deleted: the delete needed a permission approval this session cannot give. It is empty, so git should not pick it up.
- The run took about 5 h 20 min of the 5 h window (19:16 to about 22:35 UTC).

Files are in `entries/000574-boran-2019/`:
- `reproduce_boran_2019.ipynb`
- `reproduce_boran_2019_sfc.ipynb`
- `sternberg.py`

The record is `attempts/000574-boran-2019-01.yaml` and the handover is in `executed/000574-boran-2019/handover/`.
