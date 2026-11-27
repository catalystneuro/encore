I finished steps 1 to 6 for rozsa-2023: the entry, the attempt record (`attempts/rozsa-2023-01.yaml`) and the handover are written, and `entry.py check` passes. Of the 31 claims, 3 were reproduced, 6 partially reproduced, 10 not reproduced and 12 blocked. The executed notebooks predate my last edits, which were text only (see section 4).

**1. Outcomes**

| Claim | Outcome |
|---|---|
| fig1ab-raf-patterns | not reproduced (at most 2 of 8 values match) |
| fig1c-ra-lower-threshold-slope | reproduced |
| fig1d-human-raf-proportion | not reproduced (0.98, 0.55 or 0.53 depending on reading, against 0.226) |
| fig1f-human-raf-ngfc | blocked, metadata_insufficient |
| figs1b-rat-raf-proportion | not reproduced (0.82 to 0.98 against 0.394) |
| figs1d-rat-raf-values | not reproduced |
| fig1g-rat-raf-ngfc | blocked, metadata_insufficient |
| fig1hk-bleb-initiation-order | not reproduced |
| fig2c-zd7288-reduces-raf | not reproduced |
| figs2-zd7288-passive-properties | not reproduced |
| fig2e-sag-species | partially reproduced (test holds, medians off) |
| fig2e-sag-raf-smaller | not reproduced |
| fig2h-bleb-sag-higher | partially reproduced (P = 0.008, not below 0.001; distance 106 µm matches) |
| fig2il-kcl-induces-ra-aps | blocked, data_missing |
| fig3-human-ap-states | partially reproduced, rests on an assumption |
| fig3f-human-pre-ap-fluctuation | partially reproduced, rests on an assumption |
| fig3i-rat-lfp-rhythm | reproduced (1.06 Hz against 1.1) |
| fig3l-rat-spontaneous-ra-proportion | not reproduced, rests on an assumption (30 of 36 cells against 13 of 40) |
| fig3k-rat-pre-ap-fluctuation | reproduced under one reading, rests on an assumption |
| fig3m-rat-ais-phase-coupling | partially reproduced, rests on an assumption |
| fig3m-rat-ra-no-phase | not reproduced, rests on an assumption |
| figs3-no-modulators | partially reproduced (only 2 of the 90 recordings are in the dandiset) |
| the 9 in vivo claims (fig4*, figs4i, figs5) | blocked, too_large |

**2. What I found about the dataset**
- **Version:** 0.241220.1312 is pinned. It is the only published version, and the paper cites the dandiset without a version.
- **Units:** every voltage series states a conversion of 1e-12, but the stored values are already in volts. Many stimulus series (731 of the bleb sweeps, plus some in other folders) are stored in pA under a unit of amperes.
- **No labels:** no file says which APs are AIS-APs or RA-APs, whether a cell shows RAF, or which sweeps are the induction protocol. Only the bleb files record a cell class.
- **Selection:** the induction folders hold 313 human and 132 rat files, against the 385 and 259 cells the paper tested. Nearly every cell in them fires RA-APs, which suggests an undescribed selection of RAF cells.
- **Missing data:** no file mentions a KCl application, only 2 of the 90 no-modulator recordings are present, and one bleb file has no bleb sweeps.
- **Other differences from the paper:** sampling rates run from 5 to 200 kHz, not the 50 kHz in the Methods. Several rat active-slice recordings carry drugs the paper does not mention (gabazine, kainic acid, 4-AP).
- **Assumption:** with no labels, AIS-APs and RA-APs in spontaneous activity come from a two-component mixture on threshold and pre-AP slope (reading (b) of the claims file). It separates the classes poorly (its RA class has the steeper slope in human slices). Every outcome marked as resting on an assumption depends on this split.
- **Question for the paper's authors** (recorded as a methods_unavailable finding): what boundary or per-AP labels separated AIS-APs from RA-APs, how a recording was cut into RAF epochs, and what sag formula was used.
- I asked no reader questions.

**3. Where the protocol was unclear or missing something**
1. It doesn't say how to handle files whose many small datasets make per-object streaming very slow (about 2 MB/s). I read each file whole into memory with parallel range requests and never wrote to disk.
2. Comparing the time to stream a 711 GB dataset with the "time left" means guessing before measuring. I measured throughput on a subset and blocked the in vivo folder (383 GB, 50 to 80 min of streaming alone).
3. It doesn't say whether markdown-only edits after the run require another run, since any edit changes the entry hash. I did not re-run.
4. Reading (b) of the claims file is itself a random fit, so the five-seed rule applies to it. There was no time to run the extra seeds; each affected outcome records this as a deviation.
5. When an expected count with zero tolerance fails but the criterion's partial rule holds (fig3-human-ap-states), the protocol doesn't say which wins. I followed the criterion's decision rule and recorded that the counts failed.

**4. Runtime and what failed**
- The run took about 3 h 05 min (20:19 to about 23:25 UTC). The slices notebook ran in 13 min; the induction notebook ran in 56 min, near the 60-minute limit.
- The slices notebook peaked at 13.0 GB of memory, over the 12 GB guideline.
- My first metadata survey of all 787 files hit its 1-hour timeout, which cost an hour and is why the in vivo folder could not be fitted in.
- After the run I added the result and summary text, the README and the updated runtimes, and fixed the record. No code cells changed, but the entry hash did, so the next `run` will re-execute both notebooks (about 70 min). The handover strips the conclusions, so it does not depend on those edits.
- The bleb variant using the bleb trace during a somatic step was not run.
- The untracked `.bash_profile`, `.bashrc` and `.gitconfig` in the repository root were not created by me; I left them alone.
