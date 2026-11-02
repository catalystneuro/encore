I ran steps 1 to 6 of the Author section. The entry passes `tools/entry.py all` (the notebook ran in 27 min), and the handover package is in `executed/001290-windolf-2025/handover/`. Nothing is committed.

**(1) Outcomes**

| Claim | Outcome |
|---|---|
| edf3a-ap-dredge-slow-trend | reproduced, assumed |
| edf3b-hdbscan-clusters | reproduced, assumed |
| edf3c-spline-subsecond | reproduced, assumed |
| edf3de-spline-improves-registration | partially reproduced, assumed |
| 29 claims on data held in other archives | blocked, `too_large` (not attempted in this run) |
| edf1-lfp-runtime | blocked, `not_runnable` (needs a GPU) |

- **edf3a:** the mean template correlation rose from 0.302 unregistered to 0.332 with nonrigid and 0.334 with rigid registration.
- **edf3b:** all 16 combinations of the open readings gave 6 to 41 clusters. The clusters are broad (s.d. 22 to 135 µm), so they are groups of units, not single units.
- **edf3c:** in all 32 combinations the spline beat the 5th percentile of the scrambled control. This is partly circular, because the spline is fit to the same spikes it is judged on.
- **edf3de:** the within-cluster s.d. got lower in all 32 combinations. The template correlation got higher in only 22 of 32. All 10 misses are the readings that cluster on depth and amplitude without lateral position.

**(2) Dataset, assumptions, questions**

- **Version:** I pinned 0.260827.1449, the only published version; the paper cites no version.
- **What it holds:** one 600 s Neuropixels 1.0 recording from one macaque (AP and LF bands). There are no trial, stimulus, unit or processed tables. With no trial or stimulus record, I could not show that the AP and LF bands share one clock; their start times and durations match, which is consistent with that but does not prove it.
- **Findings recorded:**
  - The dandiset description cites "Supp. Fig. 3", the preprint's numbering, for what the paper calls Extended Data Fig. 3.
  - The probe is labelled "unknown subtype" and every electrode location is "unknown".
  - The session description says static gratings, while the Methods say mostly noise stimuli.
  - The asset name has `ses-None`, so the session has no identifier.
  - Only raw voltages are deposited.
  - The paper places the spline method in a human recording in the Results and in this macaque recording in the Methods.
- **Assumption behind all four outcomes:** spike detection follows reading (ii) of the claims file, the SpikeInterface settings from the DREDge repository's demo notebook. I could not run reading (i) (IBL preprocessing then DARTsort).
- **Questions for the paper's authors:** which detection and localization were used for this recording, and do the "registered positions" given to HDBSCAN include the lateral coordinate? If they do, edf3de would be reproduced. Both are recorded as a `methods_unavailable` finding.
- **Questions to a reader:** none.

**(3) Where the protocol was unclear or did not fit**

1. A criterion names a reading that cannot be run in time. The protocol has no rule for this. I gave outcomes on the reading that ran, set `assumed: true`, and stated it in the deviations. The evidence that reading (i) cannot run comes from a trial outside the notebook: DARTsort did not finish a 31 s segment in 13.5 min on CPU. The protocol says outside runs may not decide outcomes; I used this one only to justify not running the reading.
2. For claims on data held elsewhere that were never started, the protocol gives no fitting `blocked_by` reason (`too_large` assumes a computation that stopped, and `data_missing` is forbidden). I used `too_large` with "not attempted" in the notes. For claims whose data the paper names but are not known to be public, the protocol says `data: dataset` with `data_missing`, but I cannot change the claims file, so I left them as they are.
3. The claims file says the DREDge code applies no raster smoothing by default. In fact the code replaces the empty default with the bin size, which matches the Methods. The notebook shows the two give identical results. I noted it as a deviation and asked no reader, since it cannot change an outcome.
4. Part of the edf3de criterion is ambiguous: "partially reproduced when one measure improves under every combination and the other does not" overlaps with "methods_underspecified when readings disagree". I applied the partial clause.
5. The tied-to-a-clock check cannot be run on a continuous recording with no annotations. I stated that.

**(4) Runtime and failures**

- The notebook takes about 28 min, of which about 16 min is streaming the 7.4 GB file and detecting spikes.
- The DARTsort trial failed as described in point 1.
- The run took about 2 h 30 min and finished at about 06:10 UTC, well before the cut-off.
- Shell dotfiles (`.bashrc`, `.profile` and others) and `scripts/` appeared untracked in the repository root. I did not create them and left them alone; they should be kept out of the commit.
