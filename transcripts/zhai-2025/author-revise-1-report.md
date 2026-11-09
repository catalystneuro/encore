I revised the attempt for round 1. The entry re-runs cleanly (about 10 minutes), `tools/entry.py check` reports 0 errors, and every conclusion matches the new outputs. Nothing is committed.

**Outcome changes**
- **fig1i-dspn-dendritic-sch-lower**: partially reproduced → not reproduced, as the verifier said. The criterion only defines the reproduced case, and P = 0.066 is above 0.05. The difference comes from one cell, 20190411 cell 1, which gives 0.584 here against the paper's 0.228. The dandiset holds only its second pair of sites. With the paper's value for that cell, the exact P is 0.0133, which is the P the paper reports.
- **Six spine claims**: the reason for the block changed from `not_runnable` to `methods_underspecified`, as the verifier said. For fig4bc, the notes add that the control and 6-OHDA stacks are missing. All six stay blocked.
- All other outcomes are the same. The counts are 24 reproduced, 2 partially reproduced, 4 not reproduced and 15 blocked, matching the verifier.

**What I added or corrected**
- **Dendritic index (B1–B4):** checking the per-cell table turned up a data problem. Three line-scan series hold six trials, which is two sites stored under one name. I now split each into its first and last three trials and take the half with the smaller area as the distal site. That assumption is stated, and the sites as labelled are shown as a variant.
  - Two cells that had no index now get one, matching the paper's values (0.146 and 0.293, against 0.146 and 0.299).
  - Every group now matches the paper's rows. The median difference from the paper is 2.9%, with a Spearman correlation of 0.938.
  - The verifier's second large difference (1.062 against 0.527) is a proximal site with only one trial. Dropping it gives 0.553.
- **fig3f-ispn-dendritic-sul-no-change** stays not reproduced (P = 0.0097). The one sulpiride cell without an index has only a distal site in the dandiset. With the paper's value for it, P = 0.0545, the paper's figure.
- I recorded two new findings: the series holding two sites, and the two cells whose missing sites decide the two dendritic claims above.
- **Outputs the verifier asked for:**
  - one-to-one matching for the somatic link (72.4% exact) and the GRAB link (5 of 11), with outcomes unchanged;
  - a check that the paper's somatic rows follow the dandiset's order, which supports matching dendritic cells by order;
  - for cells with a repeated step, keeping the first or the last sweep makes no difference in 13 of 14;
  - exact Mann-Whitney P values printed next to scipy's, with no outcome changing;
  - a listing of the 86 spine files: none has a processing module or analysis entry, so no counts are stored;
  - the Fig. 7E KO pairing table (the pairing is correct; an unpaired test gives 0.885, so neither test gives the paper's 0.910);
  - AIM scores per time point for the five Fig. 8 mice. The paper's totals don't match any way of summing them, so the scores themselves differ;
  - a figure of the Sr2+ detector on 20230405b and on 07062023c, a cell where it comes close to the paper's count. On 20230405b the detection window starts on the decay of a large synchronous current, and the small events on it stay below the threshold.
- Notes now state the low power and the cells shared between groups for the absence claims, and that the iSPN on-state result depends on the basal-ratio rule (P = 0.077 under the stricter variant).
- I added matplotlib for the figure and relocked; only new packages were added. The runtime in `entry.yaml` and the README is now 10 minutes. The round is recorded under `verifications` for all 45 claims.

**What I did not do**
- I kept the 0.5–2 basal-ratio rule as the main analysis because it was fixed before the analysis ran; the stricter rule is shown as a variant for every claim.
- A per-time-point AIM comparison with the paper isn't possible, because the paper's tables give session totals only.
- I didn't change the claims file.
- No paper text was downloaded this round, so nothing new is under `paper/`.
