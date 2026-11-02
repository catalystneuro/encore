No outcome changed in this revision. The 27 claims stand at 20 reproduced (`fig6c-decay-length` among them, marked as resting on an assumption), 1 partially reproduced (`fig7fg-activation-suppresses`) and 7 blocked (the Figure 2 claims, `too_large`). The verifier agreed with every one. The final `python tools/entry.py all entries/001249-ishii-2025` run passed in 110 s, `check` reports 0 errors, and the conclusions match its numbers.

**Questions for a reader** (added to `questions/001249.yaml`; the claims are unchanged):
- **Point 1, the test for Figure 7:** the claims file takes the rank-sum test as the main reading, but the legend's p-values match the paired signed-rank test. This one question covers `fig7fg`, `fig7kl` and `fig7s3`. Only `fig7fg`'s outcome depends on the answer: it stays partially reproduced as tested.
- **Point 2, Figure 7, supplement 1G:** the paper's t values are those of a paired test, while the claims file takes the unpaired test. Both are significant.

**What I added or corrected:**
- **Figures 4 to 6, animals as units (point 7):** I added results with animal means as units. Some conclusions are weaker this way: no Figure 4H behaviour is significant after correction (ejaculation p = 0.176), and the ejaculation responder fraction differs by Mann-Whitney (p = 0.038) but not by t-test (p = 0.104). The conclusions now say these results rest on treating cells as units, as the paper and the criterion do. I also added breakdowns by animal for `fig5` and the clusters of `fig6k`.
- **`fig6c` (point 3):** I added a table of the 12 cells where my decay length and the deposited one differ. 11 are from one mouse (Vgat_4), and the deposited value is 0.3 to 5.2 s longer in each. The outputs do not show which convention produced them. The outcome keeps `assumed: true`; the verifier found that assumption reasonable.
- **`fig6k` (points 5 and 6):**
  - The "fast" cluster is now justified from the paper's code, which numbers clusters by their 0 to 5 s response, so type 1 is the largest early response.
  - The cluster that peaks earliest is shown as a variant. It does not hold more Vglut2 than Vgat cells (p = 1), so the fast part holds only under the code's numbering.
  - I state that at the paper's 55 neighbours the late cluster's 33 Vgat cells fall outside the tolerance of 37 ± 3.7.
  - `elbow_pcs` is now documented as the code's rule: it counts the components before the elbow, which gives 4, the code's printed value and the Methods' number.
- **`fig7s2`:** I printed the legend's place-preference p-values next to mine. The comparisons with eYFP match. For post-ejaculatory against appetitive hM3Dq the legend prints 1, 1 and 0.8472, while the test gives 0.162, 0.696 and 0.0615, the same values the paper's code prints. None is significant either way; I recorded this as a `paper_inconsistency` finding.
- **Figure 2 (point 8):**
  - I opened the Figshare Figure 2 zip. Its subject table matches all 14 brains by name, and the 4/5/5 groups equal the density table's group labels, so the grouping half of the link claim holds.
  - That table gives each brain's orientation, which the NWB files lack; this is a new `metadata_insufficient` finding.
  - I timed cheaper reads: a row band reads at about 13 MB/s, a crop at 1.5 MB/s, and a plane subsample for registration takes 12 to 31 min.
  - The claims stay `too_large`. Each one corrects over atlas regions that cover the whole brain, so the full-resolution signal channel must be streamed: 312 min at this run's 37 MB/s.
  - The 60-minute limit is now cited from `docs/protocol.md`, and the missing classifier is named as a second reason (`methods_underspecified`).
- **Record and README:** the attempt record gains a `verifications` round 1 with the verifier's reasons and my response for each claim. Notes, deviations and findings are updated, and the README mentions the reader question and the animal-level results.

**Not done:**
- I did not change the claim statements, expected values or criteria, as the rules require.
- I did not run any Figure 2 registration or segmentation.
- I did not find which convention gives the 12 deposited `fig6c` values; the authors are asked through the existing finding.

The working tree also has untracked dotfiles and `scripts/` in the repository root that I did not create. I left them alone, so they should not go into the commit.
