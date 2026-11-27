Steps 1 to 6 are done. Of the 48 claims, 11 were tested and 37 blocked. Two reproduced, three partially reproduced, six did not reproduce. The record is `attempts/mills-2026-01.yaml` and the entry is `entries/mills-2026/` (notebook, `mills.py` helper, README, locked requirements). `entry.py all` passes with 0 errors and the notebook runs in 18.8 min at 2.7 GB peak memory. The handover is in `executed/mills-2026/handover/`. Nothing was committed.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| fig2-recorded-neurons (link) | not reproduced: 1515 / 0 / 885 / 633 units against 193 / 212 / 145 / 71 |
| figs9-sustained-only-cs-shock | partially reproduced: the statistics hold, but the slow-reward group has 112 neurons against 96 |
| fig2q-trajectories-diverge | reproduced (PCA fitted on paired mice only, the code's variant) |
| figs8-single-trial-divergence | partially reproduced (paired half only) |
| fig3h-cs-decoded-paired-only | not reproduced: Mann-Whitney p 0.015 to 0.065, needs < 0.01 |
| figs13-imaging-mice-discriminate | reproduced (rests on an assumption) |
| fig5j-drd2-cs-shock-responses | partially reproduced: the effect holds, but the ROI counts are 4x the paper's |
| fig5h, fig5k (no-difference claims) | not reproduced, on uncurated ROIs |
| fig5m-drd2-rich-clusters-cs-shock | not reproduced under all 8 readings |
| figs15-no-context-encoding | not reproduced (rests on an assumption): Drd2 peak rate p = 0.042, and Drd2 mice do not freeze more in Context A |
| figs5, figs10lm, fig3fg | blocked, metadata_insufficient (pose clock) |
| 18 claims needing TS, CeA, unpaired mice, the GLM or the US session | blocked, data_missing |
| 13 RNAscope and optogenetics claims | blocked, data_missing |
| fig1b, fig1j, figs2 (snRNA-seq at GEO, R pipeline) | blocked, not_runnable |

**2. Dataset, assumptions and questions**

I pinned 0.261103.1719, the only published version; the draft has the same assets.

- **Neuropixels files:** the 13 files have spikes but no trial events, no behavior and no region per unit. That leaves no unpaired ephys mouse and no TS units to analyse. The Open Ephys files don't state the group; I took their 12 mice as paired from the paper's mouse counts.
- **Pose clock (rated critical):** in the Open Ephys files the poses are offset from the spike and trial clock by a different amount in each session, and nothing in the files says so. Two independent checks show it (nose position at port entry, and the speed jump at shock). The imaging files pass the same check.
- **Uncurated imaging ROIs:** the files hold every CNMF-E ROI, 2.4 to 4 times the paper's curated neuron counts, with no record of which ROIs were kept.
- **Duplicates (rated critical):** two recordings are deposited twice. The 6197 Open Ephys copies are identical. One of the two J933 imaging copies has port entries 236 s off.
- **Missing data:** the paper says its data are in the dandiset, but the RNAscope, optogenetics and unpredicted-US session are not.
- **Minor:** poses have no pixel scale, and the imaging frame rate differs from the Methods.

Assumptions:
- The pixel scale comes from the 30 x 40 cm chamber in the Methods (figs13, figs15).
- The haunch is taken as the "rear body centre" for darting.

Questions for the paper's authors are recorded as a `methods_unavailable` finding:
- How were the Figure S9 slow-reward trials selected?
- What does the Figure 5M "soft normalization" mean?
- How is "total displacement of all body points" computed?
- Is there a record of the curated imaging neurons, and of the Neuropixels regions and events?

I asked a reader no questions.

**3. Protocol gaps**
1. Partial link. The protocol blocks claims that depend on a failed link, but tests them when the link "holds only in part". Here the link's own criterion fails while 10 of the 15 paired ASt mice are usable. I recorded the link as not reproduced and tested its dependents on that subset, saying so in the notes.
2. A claim with one testable half (the paired part) and one untestable half (the unpaired part) has no outcome that fits. I used partially reproduced when the tested half held and not reproduced when it failed, and said in the notes that the untested half is unknown.
3. The reader wrote a link claim, which the protocol gives to the author. I kept it as written.
4. Severity: the table rates "deposited twice" as critical even when the file names make it plain. I followed the table.
5. For data elsewhere that need software the locked environment can't install (snRNA-seq in R), the protocol doesn't say whether to fetch the data first. I listed the GEO files without fetching them and used not_runnable.

**4. Runtime and failures**

The run took about 1 h 50 min (09:03 to 10:52 UTC); the notebook takes 18.8 min. The first imaging load failed on files that store `starting_time` and `rate` in place of timestamps; I fixed the helper. A first calcium baseline gave NaNs because imaged clips start about 9.6 s before the cue; I made the baseline use the bins that hold frames. One shell command that read a saved output file was denied by the permission system; I used the file-reading tool instead.
