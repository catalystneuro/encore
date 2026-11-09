I've done steps 1 to 6 of the Author protocol for CRCNS alm-1 against Li et al. (2015). Of the 29 claims, 13 are reproduced, 3 partially reproduced and 2 not reproduced; 11 are blocked because their data are not in the data set. The entry passes its checks and runs from a clean environment in about 4 minutes, and the verifier's handover package is built. Nothing is committed.

The files are `entries/crcns-alm-1-li-2015/` (notebook, `alm.py`, `entry.yaml`, `README.md`, requirements and lock file) and `attempts/crcns-alm-1-li-2015-01.yaml`.

**1. Outcomes**

| claim | outcome |
|---|---|
| task-performance | reproduced (only 19 of the paper's 42 mice are in the data set) |
| unit-counts | partially reproduced |
| fig2-selective-fraction | reproduced (912/1,245, exact) |
| fig2d-response-categories | reproduced under the figure's reading (219/389/304, exact) |
| fig2c-selectivity-time-course | reproduced |
| fig2c-dynamic-single-neurons | reproduced, resting on the claims file's assumed 0.5 bound |
| ed2-error-trials-predict-choice | reproduced |
| fig2e-equal-contra-ipsi | reproduced (427/485, exact) |
| ed1-no-population-contra-bias | reproduced |
| ed1-fast-spiking-properties | partially reproduced (baseline holds, "less selective" does not) |
| tagging-counts | reproduced (45 PT, 27 IT) |
| antidromic-latency-jitter | reproduced, resting on an assumed ±0.5 ms window |
| ed5g-it-second-pulse-jitter | reproduced |
| fig3ei-both-types-preparatory-and-movement | reproduced |
| fig3fj-contra-preferring-pt-not-it | reproduced with selective neurons (IT P = 0.74, as printed in the paper); PT P = 0.089 with all tagged neurons |
| fig3f-late-contra-selectivity-pt | not reproduced (PT 34.4% matches, but all task-selective neurons give P = 0.024 and the onset is 310 ms, not 570) |
| reaction-time | not reproduced, resting on an assumed detection rule (82 to 189 ms against 61.1 ± 10.5) |
| contra-ipsi-selectivity-forms | partially reproduced |
| photoinhibition (2), imaging (3), photoactivation (3), ED3 licking, ED3d anatomy, ED7 | blocked, data missing |

**2. Dataset, assumptions, questions**
- **What matches:** 19 mice, 99 sessions, 1,408 units. The cell-type labels and trial tables reproduce the paper's counts exactly.
- **What doesn't:**
  - Photostimulation types 3 to 5 appear in the data but are not in the description.
  - 43 trials marked "no stimulation" in session ANM210862_20130627 carry light pulses.
  - The deposited waveforms put 34 of the 39 "intermediate" units below 0.35 ms.
  - The neurons that failed the collision test are not labelled.
  - 10 units have spike times out of order.
  - The lick trace's level, scale and sign vary between sessions and it is undocumented.
  - The NWB copies lack the photostimulation type, the AOM trace and `GoodTrials`.
  - In 3,707 trials an epoch differs from 1.3 s.
- **Assumptions:**
  - Where the paper is silent I followed the authors' MATLAB scripts in the data set: 1.3 s response epoch, lick-early and axonal-stimulation trials dropped, each unit's trials limited to its recorded span.
  - Antidromic spikes are those within ±0.5 ms of each neuron's modal latency.
  - Reaction time is the first lick-trace movement at a fraction of the trial's peak excursion; four fractions were run.
- **Questions for the paper's authors** (recorded as `methods_unavailable` findings): how reaction time was detected; how antidromic spikes were told from spontaneous ones; which neurons enter the Fig. 3f/j bootstrap and the P = 0.13 test.
- **Questions to a reader:** none. The claims file already lists both readings of the Fig. 2d text-versus-figure disagreement.

**3. Where the protocol was unclear**
1. `archives.md` describes CRCNS data as zip files. This data set uses one tar.gz per animal, which can only be streamed in sequence (about 14 GB). I streamed each tar and decompressed it in memory, four animals at a time.
2. "Pinned version": CRCNS has none, but the bucket holds `version_1/` and `version_2/` folders that contain only documentation. I used `live`, recorded the version as `unversioned`, and put the MD5 sums in the notebook header.
3. The authors' analysis code ships inside the data set but the paper does not link it, so its rank among the method sources is unclear. I used it as the basis for assumptions and cited it.
4. The data set includes the authors' precomputed results (`ALM_compiled_all_data.mat`). I did not read it, to keep every number computed from the data.
5. `measured` must give one number per expected value, but the activated-neuron values can't be measured. I left `measured` out for tagging-counts and antidromic-latency-jitter and said why in the notes.
6. When a criterion defines no partial outcome but part of the claim holds (ed1-fast-spiking, contra-ipsi-forms), I used the protocol's general definition of partially reproduced.
7. For unit-counts, the criterion's width measure and the data set's labels disagree. I followed the criterion's measure, which gives partial.
8. For fig3fj, the criterion says "under one reading", while step 1.6 says the outcome is what all readings give. I followed the claims file and did not mark it as resting on an assumption; a verifier may disagree.

**4. Runtime and failures**
The work ran from 21:14 to about 22:02 UTC. Nothing failed: the notebook ran in 239 to 251 s per full run, peak memory per worker was about 1.8 GB, and the checks reported 0 errors. The raw voltage traces (about 800 GB) were not read. Untracked dotfiles (`.bashrc`, `.idea` and others) and a `scripts` folder are in the working tree; I did not create them and left them alone.
