I made the attempt on dandiset 000055 for Peterson et al. 2021 (eNeuro) and ran steps 1 to 6. The final run passes check and run in a clean environment in 554 s (9.2 min). I did not verify my own work, and nothing is committed.

I used the paper's full text (open access, CC BY, PMC8225404), saved under `paper/`. I did not read the Extended Data figures, which are EPS files; claims about them rest on their legends and the Results. The pinned version is 0.220127.0436, the only published one. The paper cites only its own Figshare dataset, not a DANDI version.

**1. Outcomes per claim**

| Claim | Outcome |
|---|---|
| subjects-days-hemispheres | reproduced |
| demographics | blocked (data_missing: no sex or age anywhere) |
| electrode-counts | partially reproduced (7 subjects have depth electrodes, paper says 5) |
| bad-electrodes | partially reproduced (surface 4.83 matches; depth 4.29 against 1.0) |
| event-counts | partially reproduced (211 to 996, median 770.5, against 151 to 947, median 640) |
| features-differ-subjects | reproduced |
| days-one-dominant | reproduced |
| duration-magnitude-small | reproduced |
| angle-bimodal | not reproduced (strong upward peak, weak downward one) |
| feature-correlations | partially reproduced (5 of 6 within 10%) |
| bimanual-skew | reproduced |
| projection-link (with inputs) | reproduced |
| group-pattern-rois (with inputs) | reproduced |
| precentral-subject-ci (with inputs) | reproduced (22 of 24 inside Table 1's intervals) |
| precentral-subjects-differ (with inputs) | reproduced |
| precentral-day-effects (with inputs) | reproduced (23 of 24 calls agree) |
| baseline-reduces-day-variability (with inputs) | reproduced |
| regression-r2-max, -r2-sensorimotor, -angle-day-top, -angle-coefficient, -angle-retained (with inputs) | reproduced |

The "with inputs" claims use the paper's electrode-to-region projection matrices from Figshare (doi:10.6084/m9.figshare.12114408.v1). They match the dandiset's electrodes in all 12 subjects.

**2. What was found about the dandiset**
- **Clock error:** in three files (sub-01 ses-7, sub-04 ses-3, sub-06 ses-3) the ECoG starts at `session_start_time`, 8.1 to 8.5 h after the day's start, but its `starting_time` is 0. The reaches table, epochs and pose count from the day's start, while the `ReachEvents` timestamps follow the ECoG clock. The stored times give no movement response; subtracting the offset brings it back. The notebook applies this correction.
- **Time of day:** the full-day files state 19:00 at UTC-05:00, but the sleep labels place the file start at local midnight.
- **Events:** the dandiset appears to hold the events before the paper's visual removal of false positives, with no flag marking them.
- **Metadata errors and gaps:**
  - `Bimanual_overlap` is in seconds, though described as a fraction.
  - The reach-angle convention (image coordinates, y down) is not stated.
  - Pose is stated in meters with a NaN conversion but holds pixels.
  - The ECG series carry the EOG description.
  - Electrode location is "unknown" for every electrode.
  - Subject 03's 16 depth electrodes have no coordinates.
  - In subject 12, the electrodes without stored R² are not the ones with zero projection weight.
  - One event (sub-08 ses-4) starts past the end of its file.
- **Code against Methods:** the regression code uses an 80/20 split and shuffled-test ΔR² where the Methods say 90/10 and unshuffled. Here the outcome is the same either way.

**3. Where the protocol was unclear, wrong or missing something**
1. **Version to pin:** the paper cites Figshare, not DANDI. I pinned the only published version and said why in the header.
2. **Clock check:** the suggested contrasts don't fit ECoG with an event table. I used the event-locked response at the true times against 30 s later, plus wrist speed from the pose. The protocol also doesn't cover two event series in one file that disagree; I recorded it as a finding.
3. **Stored derived results:** the files store the paper's regression R² per electrode, and it is unclear whether a claim may be judged on them. I judged one claim (regression-r2-sensorimotor) on them, said so, and showed they agree with my recomputation (r = 0.78 to 0.87).
4. **Code under `inputs`:** the protocol does not say whether code read for method choices belongs there. I listed the code repository and commit, as the example attempt did.
5. **Size against runtime:** the dandiset is 845 GB, and the protocol has no rule for subsampling within the 30 min limit. I used:
   - electrodes carrying 95% of the precentral weight, for all events;
   - five events per file for the eight-region pattern;
   - up to eight electrodes per subject and 40 splits (paper: 200) for the regression.

   All are recorded as deviations.
6. **Many expected values in one claim:** there is no rule for turning 24 confidence intervals into one outcome. I set the threshold (20 of 24) in the criterion before the analysis.
7. **Data check before criteria:** a trial run of the loader showed me subject 01's precentral values before I wrote that criterion. I said so in the claims file's opening comment.
8. **Duplicate check:** comparing raw traces was not feasible at this size. I compared the stored per-electrode SDs and the event tables between files instead; no recording is deposited twice.

**4. Runtime and failures**
- The final notebook runs in 554 s and nothing failed.
- Problems found and fixed during development:
  - h5py chunk lookups over the network took about 0.4 s per chunk row. I replaced them with a direct reader of the chunk index, checked against h5py.
  - `h5o.get_info` took about 2 minutes per file; `h5g.get_objinfo` returns the same address at once.
  - Chunk length differs in one file (54412 samples, not 84375).
- My first conclusion cells were drafted before the run. I replaced them with placeholders and wrote all conclusions from the executed outputs.
- Untracked character-device dotfiles (`.bashrc`, `.gitconfig`, `scripts` and others) in the repository root come from the sandbox, not from this attempt. I left them alone; they should not be committed.

Files are in `claims/000055/`, `attempts/`, and `entries/000055-peterson-2021`:
- 10.1523-eneuro.0007-21.2021.yaml
- 000055-peterson-2021-01.yaml
- reproduce_peterson_2021.ipynb
