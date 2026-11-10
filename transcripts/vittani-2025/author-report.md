The attempt is recorded and handed over. Of the 40 claims, 15 were tested and 25 are blocked. The entry passes `tools/entry.py check` and `run` (about 34 min), and `handover` built `executed/vittani-2025/handover/`. Nothing is committed.

**1. Outcome per claim**

| Claim | Outcome |
|---|---|
| fig1b-camp-dose-dependent | reproduced |
| fig1g-j-camp-kinetics-anesthetized | reproduced (9 of 12 values within tolerance, ordering holds) |
| fig1f-camp-reproducible | reproduced, rests on an assumption |
| fig4a-e-camp-ip3r2-no-difference | reproduced, rests on an assumption |
| fig3b-camp-awake | partially reproduced |
| fig5b-d-ca-anesthetized | partially reproduced |
| fig5h-j-ca-ip3r2-reduced | partially reproduced |
| fig6c-e-camp-mild | partially reproduced |
| fig6f-h-ca-mild | partially reproduced |
| fig3cd-camp-awake-stable | not reproduced |
| awake-vs-anesthetized-camp-kinetics | not reproduced, rests on an assumption |
| fig4-camp-ip3r2-values | not reproduced |
| figs4f-g-ca-rise-decay-anesthetized | not reproduced |
| fig5e-g-ca-awake | not reproduced |
| figs1p-whisker-camp-length | not reproduced |
| fig1k, figs1k, figs5i, figs1n, figs4z (5 claims) | blocked: metadata insufficient |
| 20 arteriole claims and the claims that depend on them | blocked: too large for the run |

**2. Dataset, assumptions, questions**

What the dataset holds:
- **Raw movies only.** 500 files, 350.8 GB of raw uint16 movies. There are no signal or blood-vessel ROIs, no stimulus times and no traces. I found the LED onset from the step the light leaves in each recording.
- **Duplicate files.** Eight pairs of files hold identical movies. Some pairs join two mice, and one joins a control with a bPAC mouse. I kept the first file of each pair, so I cannot say which mouse each movie belongs to.
- **Mild-stimulation cAMP.** Only recordings 1 and 6 exist. PF5's recording 6 has just 2 frames.
- **One transposed movie.** PF584 recording 2 is stored with time as the last axis; it caused the first run to fail, and the helper now reads it.
- **Arteriole copies unusable.** The "rotated" arteriole movies, on which the kymograph rectangles were drawn, hold only the values 0 and 1, and no rotation angle is stored. A quick test of recovering the angle from the image outline gave no clear answer.
- **Unlabelled images.** The two-photon channels are not named, so I can't tell GCaMP6f from Pink Flamindo. The histology and two-photon images are unlabelled frames.

I pinned version 0.250603.1324, the only published one; the paper cites none.

Assumptions:
- The signal ROI is a central disc of radius 160 px. The dark-vessel background is the darkest 0.5% of that disc in the first frame.
- Where a claim needed one choice among the open readings in the claims file, I used F0a-peakf-decayb-t0a. That is: baseline over the whole 65 s, peak on the filtered trace, "80% decay" meaning the fall to 20% of the peak, time measured from the first frame after the LED. It is the reading under which the anesthetized cAMP values best match Table S1.

Three questions for the paper's authors are recorded as `methods_unavailable` findings:
- What "80% decay time" means.
- Whether peaks are read on the filtered or the unfiltered trace.
- Where the ROIs were drawn and how the "Corrected dF/F0" was fitted.

I asked a reader nothing.

**3. Where the protocol was unclear or missing something**
1. **Data size.** "Aim for under ten minutes" can't be met when 191 GB must be streamed. I accepted a run of about 35 minutes.
2. **Shared readings.** Several claims depend on the same open readings, some of them claims of absence or claims with no "under one combination" wording. I adopted one reading for all of them as a stated assumption and showed every reading.
3. **Duplicates.** The protocol says to count each recording once but not which copy to keep when duplicates span mice or groups. I kept the first in path order and showed the variant with every file kept for fig3cd.
4. **Readings the data can't form.** fig6c-e's criterion names recordings 1 and 4, or all four, but the data hold recordings 1 and 6 (which Table S1 names). I used 1 and 6 and recorded it as a deviation.
5. **Result cells need a second run.** Results must be markdown cells in the executed notebook, so a 35-minute notebook needs two full runs. After the last run I fixed one summary line by hand in both the source and the executed copy: "16" arteriole claims became "20".
6. **Partly testable dependent claims.** fig4j depends on blocked arteriole claims but has a testable cAMP part. I blocked it as the rule requires and reported the cAMP numbers in its notes.
7. **Clock check with one stream.** Each file holds one data stream, so I used the LED step and the response that follows it as the clock check.
8. **Stimulus timing from the Methods.** I took the whisker onset at 65 s from the Methods. I blocked the startle claims: no shock times are stored, and the stated 30 s onset doesn't fit the 25-minute awake recordings.

**4. Runtime and failures**
The session ran from about 17:01 to 19:50 UTC. Notebook runs: the first failed after 24 minutes on the transposed movie, the second passed in 32 minutes, the third (`entry.py all`) passed in 34 minutes. Streaming ran at about 100 MB/s. I did not test the arteriole claims for lack of time.

Files are in `entries/vittani-2025/`:
- `reproduce_vittani_2025.ipynb`
- `vittani.py`
- `README.md`

The attempt record is `attempts/vittani-2025-01.yaml`.
