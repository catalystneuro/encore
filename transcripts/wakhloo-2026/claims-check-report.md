The file is ready for an attempt. I made two small corrections and found nothing else wrong.

**Checker:** `claims/wakhloo-2026.yaml: 27 claims, 27 quotes, 7 statistical values, 0 problems`. It gave the same line before and after my edits.

**How I checked:** I read the full paper text (main text, legends, Methods). I also cloned the paper's code at commit 9674a6c, the commit the claims file cites, and checked the details the criteria take from it:
- 19 units in both areas.
- Behavioural error is 1 minus the fraction correct.
- The notebook prints R2 = 0.477 (CA1) and 0.510 (PFC).
- Sessions are coded 0 to 7.
- P values are adjusted over all 24 together.
- The Fig. 7 panel layout makes 7j the correlation panel.
- `results/rat_stats.csv` meets every P bound in the four mixed-model claims.

All of these match the file. Statistics, expected values and tolerances are the paper's own, and none of them is a threshold used to select units.

**Changes, by claim:**
- **fig3bc-mlp-theory-tracks-error:** the statement said "at every layer"; it now says "across layers". The paper says only that theory closely tracks the empirical errors.
- **svc-hebbian-correlation:** the criterion now notes that the paper's SVC notebook loads an older results file and does not cut it to sessions 1 to 8. Using the 64 rat-and-session values of the main pipeline is therefore a choice, and the criterion now says so.

**Coverage:** every main finding has a claim: Eq. 1 and its sample dependence, the MLPs, the pose network, macaque V4/IT, the optimal-code results, and the rat learning results with their mixed models. All claims come from this paper.

**Still open (recorded under `checks`):**
- The Supplementary Information is not in the text. That covers Supp. Figs. 3 and 12 and Supp. Tables 1 and 2. The supplementary values the rat claims rest on come from the code's outputs instead.
- The paper gives no measure for "plateau" (fig7d, fig7e), "good agreement" (fig7f) or "strong correlation" (svc). The cut-offs in those criteria were chosen by the reader who wrote the file, and each criterion names them as such.

I added the check entry with `ready: true`. Nothing is committed; the only tracked change is `claims/wakhloo-2026.yaml`.
