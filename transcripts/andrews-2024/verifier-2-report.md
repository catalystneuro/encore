**Verifier report, round 2: Andrews et al. 2024 on DANDI:001132 version 0.241130.1903**

The claims file has 29 claims and the attempt record has 29 outcomes: 1 partially_reproduced and 28 blocked (27 data_missing, 1 not_runnable). No outcome is marked `assumed: true`.

### 1. Outcomes

I agree with all 29 outcomes.

- **table1-cohort, partially_reproduced.** Cell 20 checks the following against Table 1 in code, and all match:
  - 12 slices and 7 patients;
  - 5 F and 2 M, aged 20 to 52;
  - each patient's age and sex;
  - all 8 HcKCR1 slices of Table 2 present by name.

  Cells 6 and 20 show that no field under `general/` names an opsin, virus or genotype, and neither does the dandiset metadata. The partial verdict reads "identifiable" in the criterion as "identifiable by name". The record says so ("which is read here as partial"), but this reading is not marked `assumed: true`. It is reasonable, and it should be flagged as an assumption.
- **simulation-dampening, blocked.** I agree it is blocked; the code question is discussed below.
  - Cell 27 shows:
    - the published environment file (NEST 3.4 from conda-forge, NESTML 5);
    - PyPI has no NEST 3.4;
    - NEST 3.10.0 with NESTML 5.3.0 fails at `generate_nest_target` (`nest.ll_api` has no attribute `sli_func`).
  - The block also rests on an unflagged assumption: that "the locked pip environment cannot use" conda-forge. The notebook shows no such attempt. It does build a throwaway environment with `uv`, so a conda-forge environment with micromamba may well have been possible.
  - Also untried: NESTML 6 to 8, and NEST 3.9.0.post0.dev14.
  - The author says docs/protocol.md lists `not_runnable` (author, step 1.5). I do not have the protocol and cannot check that. If it says so, I withdraw my round-1 objection to the code.
- **The 27 data_missing blocks.** All are supported by cell 5 (no units, intervals, processing modules or stimulus series in any file), cell 6 (no condition labels) and cells 14 and 17 (light events). I see nothing that would unblock any of them.

### 2. Sentences the outputs do not support

- **Cell 18, a markdown cell (checked because it backs the record's notes):** "Outside 3C no group of any file has a step of 60 counts between consecutive bins (largest 83.8 counts, in 5C-5, unpaired at that threshold)." The sentence contradicts itself. Cell 17 prints a lag-1 `max_step` of 83.8 in 5C-5. What holds is that no group has a paired light trial at 60 counts.
- **Cell 18:** "Their timing and length match the 3C light periods." The length (10 s) matches. The spacing does not: 3C-7 is 20 s, 7D-2 and 7D-0 are 30 s, and 7D-5 is 40 s (cell 17).
- **Cell 28 (Result):** "Later NESTML versions change the modelling language, so running the model under them would mean porting the model." No NESTML version other than 5.3.0 is run in the notebook.
- **Record, simulation-dampening notes:** "While preparing, not run in the notebook, NESTML 9 required porting the model … the port's build failed at cmake …". The sentence is honestly labelled as not in the notebook, but no output supports it. The same goes for "3.4 is distributed through conda-forge, which the locked pip environment cannot use."
- **Record notes with no output behind them:**
  - units-per-recording: "needs MATLAB and a CUDA GPU, which the locked environment does not have" and "the paper's repository at commit 6865bf6 holds per-unit summaries and waveform templates". The same claim about MATLAB and a GPU is made in cell 22.
  - transduction-range: "nor in the paper's repository at commit 6865bf6".
  - waveform-clusters: "The 69 files are not the code's 66 recordings".

  None of these changes an outcome.
- **Record notes for intensity-threshold, physio-bic-reduction-all-slices and table2-fr-decrease-physio-bic, and the findings:** "no light step is found in any channel group of 5C". Cell 17 finds a paired step at 40 counts and lag 2 in 5C-5 (groups 10 and 14, 0.76 s long). Cell 18 dismisses it, so these should say "no 10 s light step".
- **Record, closed-loop-bicuculline notes:** "The steps in 7D-0, 7D-2, 7D-5 and 7D-7 are 10 s periods at regular intervals." 7D-7 has a single period (cell 17).
- **Record, fig3a notes:** "seconds with over 1,000 crossings occur next to the light steps". In cell 24, 22 of the 54 such seconds lie wholly inside light, and 8 lie in pre/off. Cell 25 states these counts correctly.
- **README:** "It takes about 31 minutes". Cell 30 prints 27.0 min.
- **Cell 15 and the record (fig3a):** "3C-6 has 5 trials with a full pre window". The windows are within the file, but `window_rates` does not check for overlap with neighbouring trials, and 3C-6's onsets are 18 to 21 s apart (cell 14).
  - The pre window of the trial at 19.1 s holds 1.9 s of the previous light period (0.9 s with `skip_s` 1).
  - The OFF windows of the trials at 19.1 s and 80.35 s hold the next onset.

  So cell 25's "whose pre windows follow earlier light periods" understates this: some of them contain light. The `window_rates` docstring assumes a 20 s spacing. No outcome depends on this.

Every other number checks against its cell:
- Cell 25: 86 to 90%, 89 to 93%, 81 to 94%, 26 to 52%, −16% (p 0.82), +6% (p 0.87), −18% (p 0.77), +17% (p 0.06), and 22/54, 6/12 and 8/124.
- Cells 17 and 18: steps of 40 to 88 counts, the 4C-1, 4C-3 and 7D onset times, and 4C steps of 40 to 58 confined to groups 5 to 11.
- Cell 21 (Result) and the table1 notes.
- The Summary.
- The README counts (23 + 3 + 1 + 1 + 1 = 29) and "47 files of seven slices".
- The conversion factors (cell 9), 34% for 5C (cell 9) and 2024-09-28 (cell 5).

**My round-1 reasons in the record.** They are stated faithfully in my own words for all 29 claims. The record also attaches my problems 3 and 4 to physio-bic-reduction-all-slices and problem 1 to zero-mg-isolated-bursts. This matches what I wrote; I had rated problems 3 and 4 as not affecting a conclusion. My note on the two partial routes through the repository CSVs is not recorded, but it was not a per-claim reason.

### 3. Round-1 points

Resolved:
- **Point 1 (`general/` not read).** Cell 6 reads every object under `general/` (`visititems`) in all 69 files and finds no opsin, virus, condition or protocol field and no matching word.
- **Point 3 (first channel group only).** Cell 17 reads every group of the 47 files of seven slices, finding light events in 4C-1, 4C-3, 7D-0, 7D-2, 7D-5 and 7D-7.
- **Point 4 (split steps).** Lag 2 is now used.
- **Point 6.** Second 80 is now labelled as transition.
- **Point 7.** The cell 0 header is corrected.
- **Point 8.** Cell 20 now compares with Table 1 in code.
- **Point 5, partly.** The `skip_s` 1 run is added, and the per-chunk threshold that still includes transients is disclosed.
- **Point 2, partly.** The install and build attempt and its error are now shown.

Remaining:
1. **Bears on a conclusion (simulation-dampening).** The block rests on two untested steps:
   - that conda-forge's NEST 3.4 cannot be installed;
   - that no NESTML between 5.3 and 9 builds the published model unchanged against an installable NEST.

   An attempt with micromamba (`nest-simulator=3.4`, `nestml==5.*`) in a throwaway environment would settle it. Until then the block is plausible, not shown, and the assumption should be marked `assumed: true`. The reason code depends on the protocol, which I cannot see.
2. **Wording only.** table1-cohort's reading of "identifiable" should be marked `assumed: true`; the outcome stands.
3. **Do not bear on a conclusion:**
   - the contradictory 60-count sentence in cell 18;
   - the README run time;
   - the 3C-6 window overlap in the variant;
   - "no light step" for 5C where cell 17 shows a 0.76 s pair;
   - record sentences about the repository, MATLAB and a GPU, and the NESTML 9 port, which have no notebook output behind them;
   - 9E and 12G read on the first channel group only (disclosed);
   - the per-chunk threshold including transients (disclosed).
