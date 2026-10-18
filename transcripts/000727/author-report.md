I've finished steps 1 to 5 and ran the handover (step 6). The entry is `entries/000727-brezovec-2022/`. It passes `check`, and `all` ran clean twice in a fresh environment with identical numbers. Nothing is committed.

I used the full text of bioRxiv v1 (21 March 2022, CC BY-NC-ND), the only preprint version, saved under `paper/`. The later Current Biology version is paywalled and was not used. I pinned 0.240106.0043, the only published version. The paper cites no DANDI version, and the draft has the same 18 assets with metadata-only changes.

## 1. Outcomes (8 reproduced, 5 partial, 1 not reproduced, 6 blocked)

| Claim | Outcome |
|---|---|
| dataset-structure (9 flies, 30,456 volumes, 1.88 Hz, 1.6M voxels, 50 Hz tracking) | reproduced |
| fig2c-fraction-correlated (39%) | partially: 31.1% at voxel level. Sampling behaviour at volume start instead of the midpoint gives 39.2% (variant only) |
| fig2c-venn-categories (15 / 20 / 4 / 10%) | partially: 11.9 / 15.9 / 3.2 / 11.5%, ranking holds |
| fig2-symmetry | reproduced (forward map vs its mirror r = 0.82; left and right turning on opposite halves) |
| fig4bcd-pc-structure | reproduced |
| fig4fg-ridge-r2 (R² ≈ 0.3) | partially: medians 0.155, 0.196, 0.212. Interleaved folds give 0.318, 0.252, 0.271 (variant only) |
| fig4h-r2-vs-movement | partially (pooled p = 0.064; largest R² 0.534) |
| fig4i-weights-stereotyped | reproduced |
| fig5a-unique-variance | partially (walking state unique in 0.09% of blocks, forward 0.75%, below my 5% threshold) |
| fig5c-global-below-threshold | reproduced (under one of two threshold readings) |
| fig5f-ipsi-contra | not reproduced: activity rises on the ipsilateral side, but the mirror blocks also rise instead of falling |
| fig6-peak-time-range | reproduced (99th percentile lead 0.32 s; lags beyond 1.2 s) |
| fig6h-peak-vs-width | reproduced (r = 0.672) |
| fig6fg-ipsi-leads-contra | reproduced (ipsilateral leads by 0.14 to 0.16 s) |
| fig2e, fig3, fig6eg, fig7 (region-level) | blocked: metadata_insufficient |
| figs2-tdtomato-control | blocked: data_missing |
| figs4a-supervoxel-number | blocked: too_large |

## 2. What was found about the dandiset
- **Contents:** all nine flies of the paper, no recording deposited twice. The processed volumes are in the Functional Drosophila Atlas (FDA), a space from a later paper of the lab that the preprint does not use. Their voxel size is given as 1, 1, 1 with unit "unknown".
- **Missing:** neuropil labels for any space, the paper's mean brain, the supervoxels, the z-depth maps, per-plane acquisition times, the motion-corrected tdTomato channel, and which half of the volume is the fly's left. The missing plane times move results: the correlated share goes from 31% to 39%, and the forward-velocity lead from 0.32 to 0.58 s.
- **Clock:** imaging and FicTrac both start at 0 by construction; the conversion code notes that sync data were missing. The data are consistent with a shared clock: brain-wide activity follows walking by 0.4 to 0.8 s in every fly.
- **FicTrac metadata:** every series is labelled "meters" with conversion 0.0045, though most hold angles in radians. `RotationDeltaError` has medians of 6,000 to 10,000, which cannot be radians.
- **Code bug:** the walking state uses `np.sqrt(a, b)`, so it reduces to forward velocity alone.
- **Paper errors:** the Methods cite Figure 3F/G for panels that are in Figure 4, and Figure 3G is called the Nodulus in the text and the Ellipsoid Body in the legend.
- **Data statement:** the preprint says the data are on Dryad; there is no Dryad record for this paper.

## 3. Where the protocol was unclear or missing something
1. **Which code to read.** The preprint names no code repository, and the published dandiset links none. I found `ClandininLab/brezovec_volition_2023` (commit 8e2b275) by search; its README gives a different title, but its scripts match the Methods. I recorded it as an input and a finding.
2. **Outside resources the dandiset itself depends on.** The processed data need the FDA atlas, whose labels are public (BIFROST, Dryad), but the paper does not use it. Under step 6 I blocked the four region-level claims. The protocol does not consider this case.
3. **Datasets too large to stream (610 GB).** Nothing covers testing on a sample. I streamed 12 of 91 planes (22 GB) and used 6×6 voxel blocks in place of supervoxels, recorded as deviations.
4. **Where the data check ends.** To find the left-right axis I ran correlation prototypes (one fly's plane, then the Figure 2 correlations) before writing criteria. I listed what I had seen in the claims file's opening comment.
5. **Clock check below the sampling resolution.** At 0.53 s per volume, the check cannot establish the sub-volume alignment that the Figure 6 claims need. I stated the limit and recorded it as a finding.
6. **Partial outcomes for single numbers.** The protocol does not define "partially reproduced" for one expected value outside tolerance. I defined the bands in each criterion.
7. **`measured` when no reading matches.** Unspecified; I recorded the first listed reading, or the one reading that matched.
8. **Following code that tunes on test data.** The code picks the ridge alpha on the held-out folds. I followed it, as the protocol says, and showed a nested-alpha variant.
9. **The 10% default tolerance.** For counts and stated device rates I used 0, with the reason given. For "approximately 0.3" I kept 10%, which is strict.

## 4. Runtime and failures
- **Runtime:** the notebook runs in 483 s: 319 s streaming the planes, about 2.5 min of analysis.
- **Fast reads:** h5py over the network was too slow (2.6 MB/s), so the helper reads the gzip chunks directly by HTTP range requests (about 98 MB/s). These reads match h5py values in all nine files.
- **Transient failures:** bioRxiv rate-limited me (HTTP 429, then succeeded on retry) and the GitHub API hit its limit (I cloned the repositories with git instead). Neither affects the entry.
- **Repo root:** `git status` shows `.bashrc`, `.gitconfig`, `scripts` and other entries as untracked. These are `/dev/null` devices mounted by the sandbox, not files I created, so I left them alone.
