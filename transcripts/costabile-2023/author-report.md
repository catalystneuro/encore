I've done steps 1 to 6. The entry passes `entry.py check` and a clean run (40 min), the attempt record is written, and the handover is built. Two claims were tested and both reproduced. The other 33 are blocked as `too_large`, almost all because the paper's CNN would have to be fit to about 433,000 neurons. Nothing is committed.

**(1) Outcomes per claim**

| Claim | Outcome |
|---|---|
| data-zebrafish-coverage | reproduced: 25 fish, 750 planes, 706,543 components (the paper's count exactly); 434,651 pass the brightness cut against the paper's 432,882 (+0.4%) |
| figs6-train-test-uncorrelated | reproduced, resting on an assumption: median inter-trial correlation is -0.051 for temperature and between -0.009 and -0.001 for the three behavior traces, under every bout reading. Temperature fails a stricter variant (median of absolute values 0.266) |
| 12 claims on the zebrafish fits (fig6d, shuffle enrichment, every-cutoff, fig6e ×2, fig6g, fig7b, fig7d, fig7e, lm-recovers, temperature-nonlinear, interaction-terms) | blocked, `too_large`: one CNN fit takes 2.08 s here, so about 62 h on 4 threads, or 125 h with the rotated controls |
| 6 anatomical claims (three Figure 6 supplement region claims, fig7a, fig7c, fig7f) | blocked, `too_large` through the fit claims they depend on; they would also need the Z-Brain registration, which the dandisets don't hold |
| fig6f-reticulospinal-behavior | blocked, `too_large` (218,257 components, about 31 h); 000238 also holds no backfill annotation |
| 14 simulation and mouse claims (Figures 1 to 5, data elsewhere) | blocked, `too_large` for this run's time; the notebook gives the estimates |

**(2) The dataset**
- **Pinned versions:** each dandiset's only published version (000235/0.230316.1600, 000236/0.230316.2031, 000237/0.230316.1655, 000238/0.230316.1519). The paper cites none.
- **What checks out:**
  - No plane is deposited twice.
  - The pixel masks line up with the movie (median r 0.834 between mask-pixel traces and CaImAn's).
  - Calcium is predicted far better by its own plane's temperature than by the next plane's (held-out r 0.656 against 0.393). It rises after swim starts, peaking at 1.8 s. Both are consistent with one shared clock, resolved only to about 2 s.
- **Major findings:**
  - There are no swim bouts or behavior predictors in the files. The lab's bout code with its default threshold of 2 rad/s finds 4.9 bouts per second, which is tracking noise.
  - There is no Z-Brain registration.
  - There is no backfill annotation in 000238.
- **Minor findings:**
  - The imaging rate is 2.384 Hz; the Methods say 2.5 Hz.
  - In 10 planes the tail timestamps span 629 s, so they must contain a jump of up to 128 s.
  - Each temperature trace is about 10.5 s longer than its imaging, and the files don't say where it starts.
  - One backfill file has 25 planes, 8 planes have 1,181 frames, and 10 planes exceed 30 °C.
  - The reference images are empty.
- **Assumptions:**
  - Brightness is computed on the raw movie as deposited.
  - The NWB segment angles are relative, so their cumulative sum gives the point angles.
  - "sum_tail" is the cumulative tail angle.
  - The bout threshold is 5 or 10 rad/s, not the code's 2.
- **Questions for the paper's authors:** what bout threshold, minimum bout length and angle input were used; and whether the brightness projection came from the raw or the motion-corrected movie.
- **Questions to a reader:** none.

**(3) Where the protocol was unclear or didn't fit**
1. `too_large` mixes "the computation is too big" with "the time left in this run". fig1f, Figure 1F (about 1.0 h with five seeds) would fit under the notebook limit, but not beside a 40-minute dataset notebook. I used `too_large` and said so in each claim's notes.
2. The five-seed rule multiplies the cost of the simulation claims by five, and the protocol allows no reduced seed check.
3. A claim gets one `blocked_by`. The anatomical claims have two blockers (the fits and the missing registration), so I put the second in the notes.
4. The clock-check recipes don't fit a slow continuous stimulus: raw lagged correlations are high by chance. I used held-out decoding with the temperature shifted in time.
5. The bout method lives in code the claims file names but didn't read (bitbucket.org/jcostabile/2p), and its default threshold doesn't fit these data. I read it at commit 5ffaa2d, ran every reading, and recorded the choice as an assumption.
6. The train/test criterion ("median ... below 0.2 in absolute value") can pass with strong correlations of both signs. I applied it as written (|median|) and showed median |r| as a variant.
7. A finding needs a cell tag, but the bout-threshold problem shows in a sanity cell, so that cell carries two tags.
8. `runtime_minutes` has to be written before the run, and editing it afterwards invalidates the run's stamp. The record says 33 min; the final run took 40.
9. The backfill annotation may be in the paper's Zenodo processed data (doi:10.5281/zenodo.7737788, `rs_analysis.hdf5`). The claims file doesn't name it as an input, so I didn't open it.

**(4) Runtime and failures**
- **Runtime:** about 2 h 25 min of the session, ending at 01:50 UTC. The notebook takes 40 min, with peak memory about 1.3 GB.
- **Failures:** none in the final runs. One subset run failed on a matplotlib argument and was fixed. Nothing was left unrecorded.

The entry is in `entries/costabile-2023/`; the record is `attempts/costabile-2023-01.yaml`, and the handover is in `executed/costabile-2023/handover/`.
