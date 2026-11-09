I've finished protocol steps 1 to 6 for dandiset 000226, using the full text. The entry passed `check` and ran from a clean environment in 12.7 minutes, and the verifier's handover package is built in `executed/000226-severson-2017/handover/`. Nothing is committed.

**Paper and version.** The version of record is not open access. I used the accepted author manuscript from PubMed Central (PMC5528144) and the publisher's supplement `mmc1.pdf`, which holds Table S1. The supplement could only be fetched from the Elsevier CDN; PMC and Europe PMC returned a challenge page. I pinned 0.230607.1747: the paper cites no version, this is the only published one, and the draft has the same 60 assets and size.

### 1. Outcome per claim
| Claim | Data | Outcome |
|---|---|---|
| table-s1-link | with_labels | reproduced (60 of 60 files match and agree) |
| video-frames | with_labels | reproduced (54,660,000 and 65,710,000 frames) |
| merkel-minutes | with_inputs | reproduced (823.8, 998.2 and 846.4 min) |
| fig2c-baseline-rate | with_labels | reproduced (0.03 Hz) |
| fig2c-touch-rate | with_labels | reproduced (47.9 Hz, all 33 touch-sensitive) |
| fig2c-wt-star | with_labels | reproduced under reading (b) (13 afferents, 19.0 Hz) |
| fig3a-direction-selective | with_inputs | partially reproduced (17 of 26 selective, criterion 80%) |
| fig3d-gam-full | with_labels | reproduced (r = 0.708) |
| fig3d-gam-single | with_labels | reproduced (0.441 and 0.415) |
| fig3d-gam-best-pair | with_labels | partially reproduced (0.622, ranked 2nd of 45 pairs) |
| fig4c-viscoelastic | with_inputs | reproduced (0.657 against 0.686) |
| fig5-phase-modulation | with_labels | reproduced (2.43 and 51.1 Hz) |
| fig5e-phase-span | with_labels | partially reproduced (all four quarter cycles, but Rayleigh p = 0.047) |
| figs3-phase-invariance | with_labels | reproduced |
| figs6-kinematic-gam | with_labels | reproduced (r = 0.975, on 15 of 28 afferents) |
| figs4-nasolabialis | with_labels | reproduced (0.924 and -0.716) |
| sigma-kappa | with_labels | reproduced (10.01%) |
| fig7g-phase-span-28, fig6-cut-eliminated, fig6-cut-remained, fig7e-lost-rate-kinematics | | blocked: metadata_insufficient |
| fig6a-final-length, fig7d-cut-emg, fig7f-precut-emg, figs4-intrinsic-protractor, figs1-optotag-latency, figs1-labelling-specificity, contact-classifier | | blocked: data_missing |

### 2. What was found about the dandiset
- **Labels are missing.** The 60 files match Table S1 one to one, but they don't say which experiment a recording belongs to, the afferent type, Merkel identity, or the three recordings the paper excluded. Every series is "no description".
- **Cutting experiment is mislabelled.** Every trial of the 13 progressive-cutting recordings is labelled `intact`, with one MOI value per file. Yet their rates fall over the session (last fifth below half the first in 10 of 13), so the cut conditions appear to be in the files under the wrong label.
- **Data missing.** There is no intrinsic protractor EMG (7A, 8A, 9A hold video series only), no optogenetic tagging data, no histology, no cut lengths and no manually curated contact frames.
- **Wrong units.** Velocity, acceleration, jerk, dM0, dFaxial and dFlateral are stored per millisecond but labelled per second.
- **Phase convention.** The stored phase runs backwards in time, so phases from -pi to 0 are retraction. This is not documented anywhere.
- **Smaller issues.**
  - Trial intervals are 7 s for 5 s of data.
  - Spike times in KS0277A are unsorted.
  - KS0125_ and KS0128_ lack the unit letter.
  - `distanceToPoleCenter` has unit "unknown".
  - Some values are extreme (position down to -985°).
  - The analysis code is available only on request.
- No recording is deposited twice. The clock was shown for 53 of 57 recordings with spikes.

### 3. Where the protocol was unclear or did not fit
1. **Paper's own table as input.** The protocol has no case for a table from the paper itself. Table S1 is the only source of experiment groups, types and exclusions. I used group membership as `with_labels` and afferent type and Merkel identity as `with_inputs`, with one link claim for both.
2. **Spread as tolerance.** Using the stated spread makes median ± IQR claims nearly untestable (48.0 ± 96.3 Hz accepts anything from 0 to 144). I followed the protocol and say in each note whether the value is also within 10%.
3. **Streaming.** These files hold thousands of tiny datasets, so range-request streaming took 22 minutes for metadata alone. I read each file whole into memory, never to disk, and said why in `merkel.py`.
4. **No public code.** Step 1.5 assumes code exists. I recorded where I looked and a `methods_unavailable` finding.
5. **Fixing my own bugs.** The protocol doesn't cover fixing a bug in the attempt's own code after seeing outputs. Two came up: the spline fitter diverged in the first run, and the viscoelastic fit was badly conditioned. I fixed both without changing any criterion; the optimizer sensitivity is recorded as a deviation without numbers.
6. **Same model, other data.** For a claim on 28 afferents where only 15 are separable (figs6), the protocol doesn't say whether to block or test a subset. I tested the 15 and recorded it as a deviation.
7. **Small ambiguities.** The link rule "remove KS0" did not fit the EMG ids, so I stripped leading zeros and recorded it. A blocked claim with two reasons (fig7d) got the main one, data missing, with the other in the notes.

### 4. Runtime and failures
- The final notebook runs in 12.7 minutes; I ran it five times.
- Runs 1 and 2 had wrong model results from the two bugs in item 5, both fixed before the final runs.
- The first metadata scan with range requests took 22 minutes, which led to the in-memory approach.
- The first lock-and-run attempt failed YAML parsing on a quoted list item, which I fixed.
- `gh` had no token, so I searched GitHub for code through the public API.
