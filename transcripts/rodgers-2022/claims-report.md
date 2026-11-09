I wrote `claims/000231/10.1038-s41597-022-01728-1.yaml`. The quote checker passes: 38 claims, 38 quotes, 0 problems. Nothing is committed.

**Text read.** I used the version of record (Sci Data 9, 620; Europe PMC full text) for the Methods, Data Records, Technical Validation, Usage Notes, Tables 1 to 6 and the figure legends. The paper is a data descriptor with no supplement. No PDF was stored, so I saw no figure; Fig. 2c is known only from its legend and the text. I compared the bioRxiv preprint (v1) only for the reported counts, which are the same in both.

**Code read.** github.com/cxrodgers/NwbDandiData2022 at commit 33d610b holds only `UsageNotes.ipynb`. Its outputs use different NWB names from the paper's text: it reads `processing['behavior']['processed_position_whisker_C2']` and `contacts_by_whisker_C2`, where the text names separate groups such as `processed_whisker_position` and `identified_whisker_contacts`. Table 1 itself says there is one module named "behavior". The criterion for claim nwb-structure accepts either naming. I did not read the tracking forks (PoseTF, whisk), since no criterion rests on them.

**Claims.**
- **Quotes:** all 38 have one; none needed an `inferred` note.
- **Statistics:** none. The paper reports no tests.
- **Criteria:** all 38 have one. They cover:
  - dataset counts and durations;
  - task rules and the trials-table logic;
  - timebase and gap structure;
  - neural timestamps and alignment;
  - unit quality, depth and layer;
  - electrode ordering;
  - pose, contact and file structure;
  - inclusion rules;
  - subject metadata;
  - tracking accuracy;
  - one claim restating findings of the original study (ref. 8), which this paper gives no method for, so it is blocked.

**Details the paper leaves open, with the readings named:**
- **Trials counted in 18,514:** all rows, or rows with `ignore_trial` False.
- **Frames counted in 63,979,800:** the video frame counts, or the pose-series frames.
- **33.8 h of neural recording:** NWB timestamp spans, or the raw Open Ephys main recordings.
- **Timeout:** error trials' (stop_time − choice_time), alone or minus the same value on correct trials.
- **Firing-rate stability bin:** 60 s, or one trial.
- **"Trials to analyse" (90-trial minimum):** `ignore_trial` False, or random non-spoiled trials.
- **≥95% labeled frames:** denominator either the processed-series frames or the video frames. The whiskers counted are C0 to C3, or C1 to C3.
- **Mean tracking error (2.8 px):** curated dataset 1, or all five sets pooled.
- **"Error rates increase":** the total of the four error types, or each type.
- **"Roughly equal" sexes:** a binomial test, or the minority sex being at least one third.
- **"Rarely" for C0 contacts:** read as fewer contacts than each of C1 to C3.

**Thresholds I set myself:** some criteria rest on choices that are mine, not the paper's.
- The pass shares in several criteria (99% or 95% of trials) and the reproduced and partial cut-offs are mine.
- **Sync-pulse detection** uses half-range and half-median-brightness cut-offs. I judged these unable to change the outcome, since the paper says the video goes completely black.
- **"Slowly but predictably" (Arduino clock drift):** I give no measure for it; that part is reported and not judged.

**Missing from the paper's deposits.** Several claims need data the Data Records do not list:
- The curated whisker training sets and held-out predictions, needed by the three tracking-accuracy claims.
- Behavioral trial times in the Arduino timebase, needed by the clock-drift claim.
- Motor onset times, needed by the response-window timing claim.
- The layer boundaries are not printed (only ref. 26 is cited), so that claim checks that layers are consistent with depth.
- The amplitude-based unit-quality criteria lack a detection threshold and units in microvolts; they are reported where possible but do not decide the outcome.
