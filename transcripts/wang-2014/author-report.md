I've finished steps 1 to 6 of the Author section. The entry passes `entry.py all` (0 errors, notebook runs in about 24 min, 2.1 GB peak memory), and `handover` has built the verifier's package in `executed/wang-2014/handover/`. Nothing is committed.

**The main result: CRCNS hc-5 holds none of the recordings this paper's findings rest on.** All 26 claims on recorded data are blocked as `data_missing`. Only the three model claims, which need no data, were tested.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| cells-per-recording; fig1d, fig1e, fig1e-restored, figs1; fig2b, fig2c, fig2d, fig2e, figs4a; fig2h, fig2i, fig2j, figs5; fig4a, fig4b (×2), figs11; fig5b, fig5c, figs14, figs15, figs16; fig6 (×3) | blocked, data_missing (26) |
| fig3c-model-theta-builds-fields | partially reproduced, assumed |
| fig3d-model-cues-keep-fields | reproduced, assumed |
| figs10-model-dc-no-fields | reproduced, assumed |

- **fig3c:** theta sequences appear in 5 of 5 seeds with theta and 0 of 5 without. Fields with theta last 3.01 theta cycles (2.96 to 3.12 over seeds), which sits right on the claims file's "more than three cycles" reading, hence partial.
- **fig3d:** reproduced only under the independent-noise reading. With noise shared by all units, fields without theta stay under three cycles.
- **figs10:** the bump outruns the theta field sequence at I=6 and I=10 but not at I=4. I adopted I=10, citing Supplementary Fig. 10c.

## 2. The dataset, assumptions and questions

**What is in hc-5:**
- **Contents:** 13 tar.gz files (130 GB) from one rat, i01, recorded 1 to 19 June 2008. They cover the alternation maze (wheel runs with a median of 19.7 s, against the paper's 9 to 10 s), home-cage wheel running and an open platform.
- **No injections:** no file, description or note mentions muscimol, saline or an injection. Theta during running is present in every session. There is no linear track.
- **"MS" in the file names** marks a maze recording concatenated with the following sleep recording (from the `.cat.evt` files), not the medial septum.
- **Clock:** the LFP and behaviour are consistent with one clock in 12 of 13 sessions; it could not be established in maze8.006.
- **Version:** recorded as `unversioned`. CRCNS does not version data sets, the paper cites none, and the notebook header prints the MD5 sums from `checksums.md5`.

**Findings recorded in the attempt:**
- Two platform sessions (maze13.002, maze15.001) are labelled `WheelHomeCage` in their processed files.
- maze08.001's `.xml` describes home-cage running, but the session is an alternation session with 28 laps.
- maze13.003 lasts 60.2 min against the 53 min listed.
- The `.meta` files give a 2012 date, against 2008 in the `.xml`.
- The descriptor's field list fits only the three MATLAB 7.3 files. The ten MATLAB 5 files use other field names, which also differ between sessions.
- Units of position and speed are not stated and differ between sessions.
- `Spike.res` is a 1-based index, which the descriptor does not say.
- In three sessions the spike theta-phase array is shorter than the spike-time array (a format error).

**Assumptions** (model claims only):
- The noise η(t) is independent in each unit, taken from Fig. 3c,d and the Results sentence "neurons in the network were activated randomly". Shared noise is shown as a variant.
- I=10 is the "high DC" level.
- The paper leaves the duration, step, initial state and seeds open, so I used standard choices: 10 s, 0.1 ms, uniform low rates, seeds 0 to 4.

**Questions for the paper's authors** (one `methods_unavailable` finding):
- Is the noise per unit or shared?
- What value is the "high" DC level?
- What simulation duration and integration step were used?
- Why are fields about 0.43 s here against about 1.2 s in Supplementary Fig. 10f?

**Questions to a reader:** none. The claims file reads the paper correctly; the dataset simply lacks the data.

## 3. Protocol gaps

1. **tar.gz archives.** docs/archives.md covers only zips. A tar.gz cannot be read at an offset, so I streamed each archive from its start, which is still no download to disk. The full inventory costs about 15 min per run.
2. **Simulation claims.** The protocol does not say how a claim that uses no data, with no `data` field, is counted against the dataset. I tested the three model claims and noted in each that it says nothing about the data set.
3. **Threshold readings fixed by the claims file.** fig3c's three-cycle reading lands on a measured value of 3.01. The partial outcome is my judgement.
4. **Deciding from figures.** The protocol allows opening the PDF only to read a figure or table that the text garbles. I rendered Fig. 3 and Supplementary Fig. 10 to settle the noise reading and the DC level, and cited both.
5. **A data set that is not the paper's.** The protocol has no rule for a dataset whose subject is not one of the paper's. I blocked cells-per-recording as `data_missing` instead of counting cells on rat i01.

## 4. Runtime and failures

- **Runtime:** about 1 h 50 min (20:26 to 22:15 UTC). The two full notebook runs took 18 and 24 min.
- **Development fixes:** three processed files were first missed because they are named `_BehavElectrDataLFP.mat`. MATLAB 7.3 files needed h5py, and field names had to be mapped per session. A member-name regex wrongly matched "linearized" and "SyncTrackCoord" as a linear track. All were fixed before the final run.
- **Untracked files:** git shows dotfiles, `.idea`, `.vscode` and `scripts/` at the repository root that I did not create. I left them untouched.
- **Not re-executed:** after the final run I edited a runtime figure in an off-repo generator script and did not regenerate the notebook. The committed notebook header still says "about 20 minutes" against a measured 24.

New files: `entries/wang-2014/` (`hc5.py`, `reproduce_wang_2014.ipynb`, `entry.yaml`, `README.md`, requirements and lock) and `attempts/wang-2014-01.yaml`.
