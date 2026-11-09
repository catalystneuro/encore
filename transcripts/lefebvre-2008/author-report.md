I've done steps 1 to 6 of the Author section. `tools/entry.py all` passes (0 check errors, notebook runs in 277 s) and the verifier's handover package is built in `executed/crcns-ret-1-lefebvre-2008/handover/`. Nothing is committed. I added `entries/crcns-ret-1-lefebvre-2008/`, `attempts/crcns-ret-1-lefebvre-2008-01.yaml` and `questions/crcns-ret-1.yaml`. Some untracked dotfiles (`.bashrc`, `scripts` and others) appeared in the repo root; they are sandbox device mounts, not my files, and should not be committed.

### 1. Outcomes

| Claim | Outcome |
|---|---|
| 15 histology claims (Figures 1 to 8, Supplementary Figure 1) | blocked, data_missing |
| fig9a-response-variety, fig9c-on-off-index, fig9-rod-cone, fig9b-direction-selective | blocked, data_missing (no spots, flashes, bars or gratings in the data set) |
| fig9-cell-counts | not_reproduced (200 mutant and 122 control units, against 115 and 143) |
| fig9d-rf-size-similar | not_reproduced (bands separate in 18 of 18 combinations; mutant centres smaller, 116 against 156 um) |
| s3-receptive-field-surrounds | reproduced by the criterion, but null STAs meet the rule in 97 to 99% of cells, so it is no evidence |
| fig9e-slower-time-course | reproduced (36 of 36 separate, mutant slower by 16 to 33 ms) |
| fig9f-lower-firing-rate | reproduced (9 of 9; median rate ratio 0.38 to 0.45) |
| fig9g-threshold-unaltered | not_reproduced (36 of 36 separate, mutant threshold higher) |
| fig9h-gain-reduced | blocked, methods_underspecified (printed form 18 of 18 lower; continuous form overlaps in 14 of 18) |

### 2. The dataset and the question asked

**Version.** CRCNS ret-1 has no versions, so it is recorded as `unversioned`. There is only one form to pin: the paper predates the data set and cites none. The notebook streams the whole zip in memory and confirms its MD5 against `checksums.md5`, and lists each member's CRC-32 so a later change is detectable.

**Contents.** 16 retinas and 325 units, all stimulated with binary white noise only: vertical bars, horizontal bars and checkerboards. `ran1.bin` matches RAN1 with seed -10000, read least significant bit first. The file table matches the description.

**Problems found:**
- **Group sizes and labels.** The paper has 115 mutant and 143 control cells; the files hold 200 mutant and 122 control units. 95 of the control units are labelled "WT (chx10 het)", which is not among the paper's stated controls.
- **Misplaced spikes.** In 8 recordings from 4 retinas, 82 of 86 spike trains are out of order. They run to 1440 s and then hold a segment at 720 to 780 s. This fits the last minute (1440 to 1500 s) being stored with the wrong offset.
- **Broken stimulus in one recording.** The vertical-bar stimulus of 20080702_R4 cannot be rebuilt from its description. None of its 12 units shows a receptive field, though all 12 respond to the checkerboard in the same retina.
- **Duplicate units.** 16 pairs of units share 70 to 100% of their spikes within 0.5 ms, most likely one neuron sorted twice.
- **Missing metadata.** The files give no age, no allele, no recorded region for the Pax6-Cre retinas and no cell types.
- **Weak mutant responses.** 107 of 200 mutant units have weak or no receptive fields. They carry much of the 9D and 9G differences. A variant restricted to units with clear receptive fields is shown for every claim.

**Question asked** (`questions/crcns-ret-1.yaml`): which bar recording per retina to use (orientation, and retinas with more than one recording), citing the Methods passage on bars of 8.3 or 16.6 um. I ran three readings; they agree on every outcome.

### 3. Protocol gaps

1. **"Units with a flicker response" (fig9-cell-counts) is undefined.** I showed two STA-strength thresholds as a standard choice. No threshold can change the outcome, since there are only 122 control units in total.
2. **The protocol says how to count recordings deposited twice, not units sorted twice.** I kept all units, as the claims file reads the counts, and ran a variant without the duplicates.
3. **The criteria don't say what to do when bands separate in both directions (fig9e).** In 8 of 36 combinations there is also a 1 or 2 point reverse separation below 30 ms, from noise-only units. I read the claim as met and recorded it as a deviation. Under the stricter reading, 28 of 36 meet it and the claim would be blocked; the verifier should look at this.
4. **A criterion can be met by noise (s3).** The protocol gives no rule for when a criterion's own null meets it. I kept the criterion's outcome and said plainly in the notes that it is no evidence.
5. **The step 2 clock check assumes trial tables.** For continuous white noise I used the STA peak against a circularly shifted null and the lag of the peak.
6. **The schema has no `kind` for disagreement between the paper and the data set's labels.** I used `paper_inconsistency` for the control genotype mismatch.
7. **`archives.md` says to give MD5s for the files read, but only the zip has one.** I also printed each member's CRC-32 from the zip directory.

### 4. Runtime and failures
The notebook takes about 4.6 minutes (277 s in the clean run). There were two string-escaping errors in my notebook generator along the way, both fixed. Nothing failed in the final run.
