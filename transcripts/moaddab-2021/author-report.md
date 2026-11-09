I ran steps 1 to 6 of the Author section. The attempt is recorded, the entry passes `check` and `run`, and the handover package is built. The notebook runs in about 50 s. Nothing is committed.

**1. Outcomes (30 claims)**

| Claim | Outcome |
|---|---|
| units-and-sessions, cue-responsive-units, behavior-discrimination | reproduced |
| kmeans-elbow | reproduced (assumed) |
| kmeans-clusters, cluster-firing-characteristics, k1-k3-low-baseline, table1-cue-interaction, fig3b, fig3d, figs4, fig4def, fig4ghi, fig4-correlations-differ, fig5a (exaggerated, inhibited, anova), fig5e, fig5-regressor-cluster, fig5f, table1-outcome-anova, fig6c, fig6f, fig6g, fig6h | reproduced (assumed) |
| fig4abc-threat-bias, table-s3-cluster-regression, fig6b-k2, fig6de-k4-k5 | partially reproduced (assumed) |
| fig6a-k1-shock | not reproduced (assumed) |

That is 25 reproduced, 4 partially reproduced, 1 not reproduced, none blocked. "Assumed" is set on every outcome after the first three.

**2. Dataset, assumptions and questions**

- **What the data set holds.** `data.zip` (MD5 bf5c…, the only published copy) contains the derived `cube.mat`, one file per unit, and the paper's MATLAB code. I recorded it as `unversioned` because CRCNS has one live copy and data descriptor 0.6 is the only version in its change history.
- **Checks against the paper.** The counts match exactly: 743 units, 228 sessions, 11 rats, then 423 cue-responsive units from 190 sessions with Figure S1's per-rat counts. Rebuilding `cube.mat` from the spike and event times of the unit files gives identical arrays, and no recording is deposited twice.
- **The paper's own clusters.** I re-implemented the code's k-means run (`rng(1)`, MATLAB's random generator and seeding). It gives exactly the paper's cluster sizes (33, 59, 18, 63, 58, 61, 64, 67), and most of the paper's F values, R² and Z values come out to the printed digits.
- **Assumption.** Normalized firing follows the code: single-trial rates are floored to whole Hz and z-scored over all trials and bins. The Methods describe z-scoring the trial-type means instead. The claims file's two readings of the Methods text are shown as variants; under them the clusters no longer match the paper's.
- **Findings recorded:**
  - The code differs from the Methods on normalization, on the Figure 1E elbow measure and on running k-means "10 times" (the code runs it once).
  - For k1, k3, k5 and k6, the Figure 6 gray boxes show 0 to 8 s but the Table S4 values fit 0 to 4 s after shock offset. This alone decides fig6a: not reproduced in 0 to 8 s, reproduced in 0 to 4 s.
  - The Figure 5E and Table S3 ANOVAs leave out two unnamed units. I identified a likely pair (one k3, one k5) whose removal gives Table S3's numbers.
  - The data set has no cluster labels or per-unit locations.
  - Recording was paused between trials, so spikes exist only from 20 s before to 33.5 s after each cue. This is not documented, and the event channel names appear only in code comments.
  - The data descriptor has errors: `wave` is one waveform per unit, not one per trial type, and `poke.base` covers 20 s, not 2 s.
- **Questions for the paper's authors:** which window Table S4 and Figure 6 used; which two units were excluded and why; whether the code's normalization was used for all results.
- **Questions to a reader:** none.

**3. Points where the protocol was unclear**

1. The code was inside the data set. The protocol does not cover code found there, or code that settles a reading neither the Methods nor the claims file names (outcome epochs from 13 s, tuning-curve bins 3 to 14). I followed the code, as the claims file's last check asked, and cited lines in `rrf.py`.
2. The code and the Methods disagree on normalization. The reader's step 2 puts the Methods first, but the claims file says to follow the code. I followed the code, marked the outcomes assumed and showed the Methods' readings as variants.
3. Table S4 does not match the paper's own figure. This is not a misreading by the claims file, so the question route does not apply. I kept the claims file's window, recorded a paper inconsistency and a question for the authors, and showed the 0 to 4 s result.
4. "Assumed" is ambiguous when the paper's code makes a choice that its Methods text contradicts. I marked every claim that depends on the normalization.
5. The protocol's clock check (shifting onsets into the inter-trial interval) cannot work here because recording paused between trials. I used a pre-cue window and labels shifted by one trial instead: 30.8% of units discriminate with true labels, 5.0% and 7.4% under the controls.

**4. Runtime and failures**

The work took about 51 minutes (07:40 to 08:31 UTC); the notebook itself runs in 49 to 50 s. Nothing failed. Files I did not create appeared at the repository root before the run started (`.bashrc`, `.mcp.json`, `scripts` and others). They are sandbox `/dev/null` mounts; I left them alone, but the workflow should not commit them.
