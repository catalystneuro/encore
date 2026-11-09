I finished steps 1 to 6 of the Author section on DANDI:000223 at version 0.260528.0906. The notebook ran from a clean environment in 18.4 min, `entry.py check` reports 0 errors, and the handover package is built. Nothing is committed.

The paper cites the dandiset without a version. Its two published versions, 0.220823.0826 and 0.260528.0906, list the same 20 assets with the same blob ids, so I pinned the newer one. The notebook header says why.

### 1. Outcomes

| Claim | Outcome |
|---|---|
| data-scale | reproduced (19 recordings, 10 cultures, 20 spines, 101.7 ± 42.6 units) |
| table1-best-r | partially reproduced, rests on an assumption (18 of 20; 19 of 20 with the code's smoothing) |
| fig1e-best-r-gap | reproduced (true for 7 of 20 spines; a weak test) |
| table1-optimal-thresholds | partially reproduced (max F matches for 15 of 19 under the Methods reading, 17 under the code's; optimal quantiles do not match) |
| mean-max-fscore | partially reproduced (0.695 ± 0.121; the SD is just outside the tolerance; the code's reading gives 0.666 ± 0.133, which matches) |
| acceptance-9-of-20 | partially reproduced (7 accepted, 17 or 18 decisions agree; the same band for every reading and noise region) |
| best-r-accepted-vs-rejected | partially reproduced (both means match, p = 0.0015; U = 5, expected 12) |
| best-r-not-predictive | partially reproduced (largest rejected 0.625 matches; smallest accepted 0.515, expected about 0.2) |
| fig5a-rejection-scenarios | reproduced |
| fig5a-threshold-order | reproduced |
| table1-network-measures | not reproduced (spike contrast matches 19 of 19; OUT/IN at most 6 of 19) |
| fig5c-spike-contrast-vs-fscore | reproduced (R = -0.724) |
| fig5d-out-in-vs-fscore | partially reproduced, rests on an assumption (R = 0.592, expected 0.672 ± 0.067) |

### 2. Dataset findings, assumptions and questions

What the dataset showed:
- **Duplicate file:** `sub-3112_ecephys+ophys.nwb` is the same blob as the 2021-02-27 19:02:33 session, so the 20 files hold 19 recordings.
- **No map to Table 1:** nothing links files to Table 1 rows. Two pairs of recordings tie on unit count, and the file with two spines does not say which ROI pair is spine 9.
- **Missing noise regions:** the background ROIs used for the noise estimate are not in the files.
- **Unlabelled ROIs:** the ROIs are not marked as spine or shaft.
- **Stored dF/F differs:** the stored `Dff` series is undocumented and differs from the paper's dF/F by up to 0.23.
- **Indicator missing:** the imaging metadata gives the indicator as "unknown"; the paper used jGCaMP7b.
- **Empty units:** two files each hold one unit with no spikes. Leaving them out gives exactly Table 1's unit counts.
- **Shared clock:** the shaft trace lines up with the population spike rate at zero lag in 19 of 20 spines, and at one frame in the last.

Assumptions:
- The tied rows (14/15, 16/20) are assigned to files by whichever order puts spike contrast nearer Table 1.
- The first ROI pair in the two-spine file is row 9.
- For Figure 5(d), the noise region nearest the spine is used, following "close to the spine" in Methods 2.7.

Questions for the paper's authors, recorded as `methods_unavailable` findings:
- Which p_thresh and hyperactive-unit strategy were used for each recording?
- Where was each spine's background ROI, and was one noise estimate used per recording?
- How was the OUT/IN ratio computed?

I asked a reader nothing; I did not find a misreading in the claims file.

### 3. Protocol points

1. **Main reading or any reading?** The claims file labels a "main reading" and a "variant" in some criteria. Elsewhere it says "under both readings" (mean-max-fscore), while the reader rule says a claim holds if any reading matches. The protocol does not say which applies. I let the main (Methods) reading decide, so table1-optimal-thresholds and mean-max-fscore are partially reproduced; under the code's reading both would be reproduced.
2. **Upstream choices that change a downstream outcome.** The protocol does not say how a choice made for one claim (the noise region of acceptance-9-of-20) carries into claims that depend on it. For fig5d it changes the outcome, so I adopted the nearest region as an assumption, under step 1.6.
3. **Matching files to the paper's own table.** Link claims cover outside data, not matching dataset files to the paper's own table. I matched by culture and unit count and broke ties with spike contrast. That makes the spike-contrast check circular for four rows, which the notes say.
4. **Fitting to the target.** The claims file's rule picks p_thresh as the value nearest Table 1's best-R, which tunes a free parameter towards the values being tested. The protocol does not say how to judge such a match. I followed the rule and also reported the code's default pair, which matches 14 of 20.
5. **Runtime.** The notebook takes 18 min, over the 10-minute aim. The grids need about 6,000 blocks of 1,000 surrogates each. It is still under the 30-minute limit.
6. **Elephant version.** I checked outside the notebook that `spike_contrast` is the same in elephant 0.10.0 and 1.2.1 apart from its docstring. It is recorded as a deviation and decides no outcome.

### 4. Runtime and failures

The run took 03:27 to 04:45 UTC. Nothing failed in the final run.

During development, presigned S3 HEAD requests returned 403, so the helper now uses the asset's public S3 URL. Reading the image series serially was too slow, so it reads in parallel processes (about 160 s for 20 windows).

The sandbox mounted `/dev/null` devices as untracked files at the repo root (`.bashrc`, `scripts`, `.idea` and others) before the run started. I left them alone; they should not be committed.
