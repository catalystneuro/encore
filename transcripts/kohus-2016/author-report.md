I've finished steps 1 to 5 for CRCNS hc-7 and run the handover (step 6). `check` reports 0 errors, and `entry.py all` passes: the notebook runs from a clean environment in 342 s. I did not verify my own work and did not commit.

## 1. Outcomes (44 claims)

| Claim | Outcome |
|---|---|
| fig4b-in-pc-kruskal-wallis | reproduced |
| fig4b-in-pc-posthoc | not reproduced (4 of 8 comparisons hold) |
| fig4c-cckdti-pc-silent-single-ap | not reproduced (3 of 7 pairs silent) |
| fig5c-pv-rip-depression | reproduced |
| fig5c-cck-rip-facilitation | reproduced |
| fig5db-recovery | reproduced (only without multiple-comparison correction) |
| fig6-pv-trains-depression | not reproduced (fails at 1 Hz) |
| fig6-cckbc-pc-trains | not reproduced |
| cckdti-pc-transmission | not reproduced |
| async-charge-epi-vs-160 | partially reproduced |
| decay-epi-vs-160 | partially reproduced |
| fig8-pvbc-pvbc-uipsc | partially reproduced (3 of 5 values within tolerance) |
| fig8-cck-pairs-uipsc | not reproduced (rests on an assumption) |
| fig8-cckbc-vs-cckdti-pairs | not reproduced (rests on an assumption) |
| decay-pc-vs-interneuron | not reproduced (rests on an assumption; the PV+ part holds) |
| fig9-pvbc-pvbc-depression | reproduced |
| fig9-pvbc-pvbc-transmission-probability | not reproduced |
| fig9-pvbc-pvbc-recovery-11th | reproduced |
| fig10-cck-cck-frequency | reproduced |
| fig11-model-pv-udr | partially reproduced |
| fig11-model-cck-facilitation | reproduced |
| table4-model-parameters | partially reproduced (8 of 13 values within tolerance) |
| fig11c-parameter-differences | not reproduced |
| fig11-model-prediction | reproduced |
| fig13-pvbc-pc-recovery-halftime | reproduced (fragile: only free-plateau fits match) |
| fig6-cckbc-async-onset, cckdti-async-onset, fig10-cck-cck-heterogeneity, fig10-cck-cck-async, fig10bd-be-async-charge | blocked: methods_underspecified |
| fig7a-cscl-kinetics, fig7b-cscl-stp | blocked: metadata_insufficient |
| fig2b (3 claims), table1, table2, fig3 (3 claims), fig12, sipsc-continuum, fig13a, fig13c | blocked: data_missing |

## 2. Dataset, assumptions and questions

**What the dataset holds.** One zip of raw paired sweeps plus the authors' per-sweep tables (`_EPA` files) for 60 pairs in 8 connection types. It has fewer pairs than the paper for most types. There are no current-step, connectivity, spontaneous IPSC or field-potential recordings.

**What I found wrong or missing in it:**
- **Stimulation timing:**
  - RIP bursts run at 222 Hz, not 160 Hz.
  - The EPI burst runs at 147 and 303 Hz, not 160 and 320 Hz.
  - The single AP comes 1.3 s before the bursts, not 1 s.
- **The pair listing (`Experiments_description.txt`):**
  - It mislabels two recordings.
  - It names 8 files that are not in the zip.
  - It leaves 20 recordings unnamed.
  - It numbers the pairs differently from the folders.
- **Missing pieces:**
  - 3 recordings have a header but no sweeps.
  - 3 recordings have no `_EPA` table.
- **The `_EPA` tables themselves:**
  - The code "AR" is never described. It sits where the paper's asynchronous-release onset would be.
  - Some tables leave out sweeps without saying so.
  - Two tables hold column labels where the mean values should be.
- **Labels the files don't have:**
  - The order of the recovery intervals.
  - Which pipette solution each pair used.
  - Animal or slice identifiers.
- **The paper contradicts itself:** it says 7 of 8 CCK+DTI to PC pairs were silent, and also that 4 of 8 responded.

**Version.** CRCNS datasets have no versions, so it is recorded as "unversioned". The notebook header gives the `Data.zip` MD5 sum and says why this copy is pinned: it is the only copy in the bucket, and the paper cites only the DOI.

**Assumptions:**
- All IN to PC pairs are treated as high-KCl pairs, since no type has more pairs than the paper's high-KCl count.
- The CCK+ interneuron pairs were recorded only with 10, 40 and 160 Hz trains, so none of the claims file's single-AP readings exists for them. I added a reading: the first AP of each train at 40 Hz or slower. This is marked `assumed` on three claims.

**Why the onset claims are blocked.** Both onset rules in the claims file flag asynchronous release in PV+BC and AAC pairs, which the paper calls synchronous. So neither rule is the paper's procedure, and the paper gives none. Read as onsets, the authors' "AR" marks come close to the paper's medians (12 against 11; 8 against 7). I show them but did not use them to decide.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- How was the onset of asynchronous release determined, and what does "AR" mean?
- Which APs and which fit windows gave the single-AP uIPSCs of the CCK+ interneuron pairs?
- How was the recovery half-time fitted: plateau fixed or free, and is the value tau or tau·ln2?

**Questions to a reader:** none.

## 3. Where the protocol was unclear, wrong or missing something
1. The protocol has no rule for the case where none of the claims file's readings can be run on the data (the CCK+ pairs' single APs). I added a reading taken from the paper's protocol passage, marked it `assumed`, and asked the authors.
2. The false-positive rule is written for a chance level the paper states. Here the paper only says qualitatively that PV+ release is synchronous. I applied the rule by analogy and blocked as `methods_underspecified`.
3. There is no slot for the authors' own scoring inside the dataset (the "AR" marks). I showed it as a variant only.
4. The protocol does not say what `measured` should hold when no reading matches. I recorded the reading the outcome rests on, or the first one listed.
5. Some criteria are fixed counts "of 8" while the data hold 7 pairs, and only one of those criteria has a fallback to a fraction. I judged each as written.
6. Blocking everything that depends on a blocked claim takes out three fig10 claims whose other parts could have been tested. I followed the rule.
7. Breaking results down by animal is impossible because there are no identifiers. I said so and reported the recording days instead.
8. CRCNS offers no published version to pin. I recorded "unversioned" plus the MD5 sum, as the archives guide says.

## 4. Runtime and failures
The notebook runs in 342 s, of which about 72 s is streaming 1.3 GB and about 225 s is the model fits. The whole run took about 1.5 h of the 5 h. Nothing failed in the final runs. The repository shows some untracked root entries (`.bashrc`, `scripts` and others); they appeared at 12:22, before this run started, and are not mine.

Files are in `entries/crcns-hc-7-kohus-2016/`:
- reproduce_kohus_2016.ipynb
- hc7.py
- README.md

The record is `attempts/crcns-hc-7-kohus-2016-01.yaml`; the handover is in `executed/crcns-hc-7-kohus-2016/handover/`.
