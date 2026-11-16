All 30 outcomes are unchanged and I proposed no changes. The entry was re-run twice with `python tools/entry.py all entries/okuno-2025`. Both runs printed identical output, `entry.py check` reports 0 errors, and the executed copies match the current entry hash.

**Why the text described another run.** The installed antspy (0.6.3) silently ignores the `random_seed` argument we were passing to `ants.registration`. So the registration had never been seeded, and every number resting on it changed from run to run. It is now seeded through `ants.config` with ITK on one thread, which makes it repeatable. A notebook cell registers one image twice and shows zero difference.

**What I added or corrected:**
- **Voxel size:** each fly now uses its own NWB grid_spacing. Before, fly-087's spacing was used for all nine.
- **Motion check (verifier point 3):** I estimated a rigid in-plane shift per volume from the tdTomato channel. The motion is not sub-voxel: per fly, the median is 0.6 to 3.2 µm and the 95th percentile 2.8 to 6.1 µm, against a 2.6 µm voxel. Regressing the shifts out moves fig3d by only 0.005, so it stays below tolerance. I corrected the round-1 response that called the motion sub-voxel.
- **Orientation (point 4):** the notebook now prints a per-neuropil GLM check alongside the voxel-wise one. Both point weakly towards flipping left and right:
  - voxel by voxel, 0.359 as registered against 0.394 mirrored;
  - per neuropil, 0.41 against 0.463.
  The per-region FC check points the other way, and by more (0.661 against 0.407). I kept "no flip" and recorded the conflict in the orientation deviation. The dataset finding now names fig3e, fig4e and fig4i as the outcomes a flip would change.
- **The paper's positive GLM cluster** (416,801 voxels) is now printed.
- **Registration instability (point 2):** fig3e's note now says the outcome is not robust. Every registration so far gives 53 to 56 regions, one to four above the bound of 52.2, and a registration with another seed moves voxels by a median of 2.5 to 44 µm per fly. The "second or third decimal" wording is gone.
- **All Result cells, the Summary, and the record's notes, `measured` fields, deviations and findings** were rewritten from the new output. With the new numbers, two statements the verifier said reversed now read:
  - fig4i: without nuisance removal the synapse result is again below the null (p = 1.3e-6).
  - fig5b activation: reading (b) holds for all four regions under the hemibrain atlas and fails only for LAL under JFRC2010.
- **Runtimes** in `entry.yaml` are updated to 36 and 20 minutes.
- **Round 2 is recorded under `verifications`**, with the verifier's reasons and a response for each of the 30 claims.

**What I did not do:**
- **No full SPM12-style realignment or slice-timing correction.** The shift regression is a check, not a correction, and I applied it only to fig3d.
- **No Tukey taper in the GLM.**
- **fig4b stays partially reproduced.** The mean holds and the count does not, which matches the protocol's "holds only in part". The question for a reader in `questions/okuno-2025.yaml` stays open.
- **Nothing committed**, as instructed.
