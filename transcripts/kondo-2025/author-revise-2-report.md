I've revised the attempt for round 2. No outcome changed, and none has a `proposed` change. The verifier agreed with all 22 outcomes and I found no reason to propose a different one. The final re-run with `python tools/entry.py all entries/kondo-2025` passed with 0 errors in about 38 minutes, and the key numbers in the notes match the new outputs. Nothing is committed.

**Statements corrected to match the printed numbers**
- **Blue/UV assignment** (data check cell and the `metadata_error` finding): the lever-pull response that `dFF_B` has and `dFF_V` lacks shows in only 3 of the 4 sessions. In VG1-GC#116 day 1 neither series responds, so the assignment rests on the brightness and the correlations. The summary now says the intensities and correlations fit the stack names.
- **100 ms onset rule** (fig6b-movement-order conclusion): it does help for smooth noise, from 85% to 42% at 2 s.d. and from 58% to 19% at 3 s.d. It still leaves the false-positive rate far too high. A deviation now says the outcome does not rest on this assumption, so it is not marked assumed.
- **fig4d-auditory-map** (conclusion and notes): I no longer call the map "flat". They give its range (0.17 to 0.83 at most) and which ROIs are on top under each reading.
- **fig5f-lever-tip notes:** 0.978 to 0.985 over sessions and 0.977 to 0.985 over per-mouse means.
- **Editorial:** I removed the repeated 16-day-break sentence from training-breaks, and removed the fig3d entry under deviations, which was a result rather than a change of method.

**Outputs added**
- **External searches for the manual annotations:** a new notebook cell runs them and prints the results.
  - The four BraiDyn-BC repositories, at pinned commits, hold no annotations. The one file whose path mentions validation is code.
  - The Google Drive folder holds five notebooks.
  - The lab platform's dataset folder is 17 TB and locked; asking for its file list returns HTTP 403, permission denied.

  The fig4ab and fig5abc text and notes now say the same as the notebook.
- **Forepaw session count:** the notebook now prints the counts without the two VG1-GC#119 sessions noted "face video is not available": 355 with body keypoints and 354 analysed, the paper's numbers. It is still described as a possible account, since the paper does not say it left them out.
- **fig6b-motor-somatosensory-after-reward:** the conclusion and notes now say the criterion does not test the "returned quickly to baseline" part. In the mean over sessions that part does not show: MOs stays above its baseline in every window, at about half of SSp-n after the reward.

**Record and questions**
- The round-2 verification is recorded for all 22 claims, with the verifier's reasons and my responses.
- The part of the verifier's round-1 problem 8 that was not attached to any reason (the extra tone TTLs) is now added to the fig3d round-1 reason, with its response.
- Two questions for a reader are added to `questions/kondo-2025.yaml`, and no claim was changed:
  - fig6b-movement-order: the −1 to −0.5 s baseline window already contains movement.
  - fig6b-motor-somatosensory-after-reward: the criterion does not test the return to baseline.

I also updated the stated runtime from 25 to 40 minutes in `entry.yaml`, the README and the notebook, since the full runs here took 38 to 41 minutes.

**Not done**
- The pixel-map readings for fig4d were not run, as the verifier noted; no outcome depends on them.
- The lab platform's contents remain unchecked because access is restricted.
- I left the verifier's round-1 reason for the lever-tip claim in its own words, slip included, as the protocol requires.
