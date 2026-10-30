I finished steps 1 to 6 of the Author section. Of the 47 claims, 7 were tested and 40 are blocked. One is reproduced, two partially, four not reproduced. The entry passes `entry.py all` (the notebook runs in about 3 min), and the handover is built in `executed/000166-senzai-2019/handover/`. Nothing is committed.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| fig4a-unit-counts | Reproduced: 1,477 units, 246 I and 1,016 E cells from the wide-band waveform |
| fig4a-ccg-classification | Not reproduced: 673 E and 187 I cells (paper 347 and 100); 74.9% and 72.7% agree with the waveform classes (paper 97.4% and 98.0%) |
| fig7-connection-counts | Not reproduced: 1,295 excitatory and 578 inhibitory connections (paper 525 and 323); no reading of the pair count matches 102,332 |
| fig7c-divergence-convergence | Partially reproduced: both modes are 1, but the largest convergence is 29 (paper 16) |
| figs8f-ie-dip-wake | Not reproduced: dips of 39.6% awake and 39.9% non-REM, p = 0.37 (paper 24.1% and 22.8%) |
| fig4de-optotagging | Not reproduced: PV mice 62 tagged, 48 in the I group (paper 15 and 14); VGAT mice 18 and 14 (paper 52 and 40) |
| figs7-strongest-3-6hz-coupling | Partially reproduced, resting on an assumption: 3-6 Hz is strongest, but 0.5-3 Hz is second, not 30-60 Hz |
| fig1g-landmark-distances-consistent | Blocked, methods_underspecified; every reading was run |
| figs8c-lognormal-strength, fig3ab-alpha-analogy | Blocked, methods_underspecified (the criteria say so) |
| fig1f-sink-b-deeper, fig1f-other-landmarks-same-depth, figs2d-visual-offset-rebound | Blocked, data_missing |
| fig3d (two claims), figs2c, fig3f: LFP sites placed by the landmarks | Blocked, methods_underspecified |
| 30 claims that depend on fig1g (coherence clusters, gamma ICs, the eight unit clusters, every layer claim) | Blocked, methods_underspecified (inherited) |

**2. The dataset, assumptions and questions**

What the dataset is like:
- **Version:** I pinned 0.250624.0434. The paper cites no version, and both published versions hold the same 19 assets.
- **Light flash times:** they are in 2 of the 13 stimulated mice (YMV05 and YMV08). Those two "Visual laser" tables also contain the optogenetic pulses.
- **Genotypes:** the files have 11 PV-Cre and 3 VGAT-Cre mice; the paper reports 5 and 9.
- **Missing from the files:**
  - The electrode table has no depths (y is NaN, location "unknown").
  - There are no unit waveforms and no layer or cluster labels.
  - YMV03 has no unit columns except quality, and YMV19 has no sleep-state table.
- **Undocumented columns:**
  - `max_channel` matches the site of the largest waveform for only 76 of 1,367 units.
  - The `cell_type` labels follow a scheme the paper does not describe. Ten units in 6 mice are labelled "down state"; the paper reports 5 such neurons in 4 mice.
- **Clocks:** spikes, the UP/DOWN table, the state table, the LFP and the laser pulses share one clock, shown with time-shifted controls.
- **Duplicates:** no recording appears twice.

Assumptions:
- For figs7, the LFP comes from a site 200 µm (10 sites) from each unit. On the unit's own site, the unit's spike leaks into the LFP.
- Mean waveforms are averaged from 60 s of raw signal per session, because the dataset holds none.
- Waking is the "Awake" intervals, with micro-arousals left out.

Three questions for the paper's authors are recorded as `methods_unavailable` findings:
- How were landmarks a, b, d and e chosen? The paper marks them by hand; a rule based on the extreme sinks and sources places them inconsistently, with distances ranging 220 to 620 µm across mice.
- Which LFP site was used for the spike-LFP coupling of Figure S7?
- Were further selections applied in the monosynaptic detection? The Methods rule finds about twice the paper's counts.

I asked a reader no questions.

**3. Where the protocol was unclear**
1. **Dependency rule.** fig1g depends on fig1f-sink-b-deeper, which is blocked as data_missing, but it uses only the DOWN-UP half, which the dataset can provide. I ran fig1g on its own and blocked it for its own reason. I then applied "blocked for the same reason" to the 30 claims that depend on it.
2. **Claims without `depends_on`.** Four claims whose criteria place sites by the landmarks list no dependency, and the protocol does not cover this case. I blocked them as methods_underspecified.
3. **Blocking after the analysis ran.** The protocol allows this only for chance levels. I used the same reasoning for the landmark rule, since the paper places the landmarks by eye.
4. **`measured` for an ordering.** The schema requires numbers, but figs7's result is an order of bands. I recorded the mean modulation strengths at 3-6 and 30-60 Hz.
5. **Inherited blocks hide the time limit.** Time was also a limit for those 30 claims: reading the LFP alone is estimated at 46 to 56 min. I gave the inherited reason as the main one and the time estimate in the notes.
6. **Surveying files.** archives.md should warn that walking a whole file with h5py over remfile is very slow (about 6 min per file); see section 4.

**4. Runtime and failures**

The run took about 1 h 20 min (03:59 to 05:18 UTC), and the notebook runs in about 3 min.

What failed:
- A survey of all 19 files that walked every object in each file timed out after 30 min, and its output was lost. Reading only the known groups took seconds per file.
- The first survey crashed because unit columns differ between files.
- Two helper bugs (a misplaced call and a 2-D amplitude array) were fixed before the final runs.

The device-node files at the repository root (`.bashrc`, `scripts` and others) are sandbox mounts, not my changes. The only new files are `attempts/000166-senzai-2019-01.yaml` and `entries/000166-senzai-2019/`.
