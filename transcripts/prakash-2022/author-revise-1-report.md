I've finished the round-1 revision. The entry re-ran cleanly (`python tools/entry.py all`, 41 min, 0 errors), `entry.py check` passes, and every conclusion matches the numbers from the final run. Nothing is committed.

**What changed in the outcomes**
- **fig6f-nonfunctional-opsin-no-response:** changed from `not_reproduced` to `blocked`, as the verifier said. The published "SB alone" column is a copy of a column from another figure (Fig. 4e(i)), so a test on it says nothing about Fig. 6f. The verifier's other suggestion, the 21-value column of Fig. 5c, gives p = 0.534 against the paper's 0.7870, so it is not the right group either. The block reason is `other`, not `data_missing`: the check rejects `data_missing` for a claim whose data the claims file places in the article's Supplementary Data. The response in the record says so.
- **Every other outcome is unchanged.** The verifier agreed with all of them.

**What I added or corrected**
- **Onset sensitivity (problem 4):** every in vivo claim is re-run with two other onsets per imaged mouse (the second-largest rise, and the onset shifted to best match the paper's own series in Supplementary Data 7). No outcome changes except through one mouse's MUA:
  - With interlum_ctrl_4's second rise as onset (228 s), part of its MUA rise falls into the baseline, and the MUA electrode test drops to p = 0.012 to 0.15.
  - The paper's own series for that mouse puts its onset at 210 s, close to the 206 s used, which gives p = 0.69 to 0.92.
  - The fig7f notes now say the outcome rests on this onset.
- **fig7d bootstrap (problem 3):** added a 10 s block bootstrap as a variant. The claim still holds under none of its 8 readings; Opsin (-) mice still have 20.3 to 29.3 contacts above baseline, against the paper's 2.7.
- **Bias of P (problem 2):** the notebook now prints it: -0.43 dB on white noise. It also prints each mouse's rise against its own baseline: Opsin (+) 0.39 to 0.80 dB, Opsin (-) 0.20 to 0.51 dB. The fig7c notes say "not seen in Opsin (-)" holds only as a group comparison. The paper's own per-mouse means also go negative, so this is the Methods' measure.
- **Probe orientation (problem 5):** the notebook prints the electrode table, group and device descriptions and the label-to-position map. None of them says which end of the probe is superficial, and the paper's Fig. 7d source data give no depths, so fig7d-superficial stays blocked.
- **Comparison with the paper's per-mouse values:** a new check compares each mouse with the Supplementary Data 7 values for Figs. 7d to 7f. Two mice match on mean gamma power to within 0.004 dB:
  - interlum_8 matches the paper's exp 2, a mouse the paper did not image, although interlum_8 has images.
  - interlum_ctrl_4 matches the paper's cntrl 2.

  Event counts are below the paper's lowest mouse in every file, so that difference comes at least partly from our pipeline. This is now in the findings.
- **Smaller fixes:**
  - The direction checks now use medians for all electrode-level claims.
  - The errant-contact finding notes the per-animal flags sum to 11, against the paper's 7.
  - The header claim count is corrected to 10.
  - The README says 11 in vitro claims reproduced; it said 12, which was already wrong.
  - Round 1 is recorded under `verifications`, with the verifier's reasons in its own words and my responses.

**What I did not do**
- No question went into `questions/prakash-2022.yaml`, because the verifier reported no place where the claims file misreads the paper.
- Whether the ephys and image clocks are aligned is still unchecked: nothing in the files allows it.
- I kept the claims file's bootstrap over single 1 s steps as the main test, since it is the criterion. The block bootstrap is shown only as a variant.
