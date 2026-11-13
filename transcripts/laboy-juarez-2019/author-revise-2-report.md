No outcome changed and I proposed no changes. The counts are still 29 reproduced, 13 partially reproduced, 7 not reproduced and 1 blocked. The verifier agreed with all 50 outcomes, and the round is recorded as `verifications` round 2 in `attempts/laboy-juarez-2019-01.yaml`. The entry re-ran cleanly with `python tools/entry.py all entries/laboy-juarez-2019` (2024 s), the earlier main-analysis numbers came out the same, and `check` reports 0 errors.

**Text corrections the verifier asked for**
- **exp2-units:** the range of the other readings is now "236 to 240", in both cell 51 and the record's notes.
- **Summary table:** fig1e's assumption is now "same-direction sequences".
- **README:** the claim that the inbound order preference "mostly reproduces" is gone. It now says the experiment 2 dt tuning and PCA claims are partially reproduced and the order decoders are not reproduced.
- **Round-1 record:** the verifier's point B10 (two recordings without sham trials, no lick exclusion) was missing from the reasons. It is now under exp2-units and exp3-units-cw-tuned.

**Outputs added**
- **Calibrated group (B1).** Every selective-group claim now also runs on the 162 sets that FDR selects from the calibrated p-values. All 162 are among the 318 of the main analysis. Compared with the 318:
  - Three claims would get a different outcome:
    - fig3g would be reproduced (0.681 at N = 10, 0.929 at N = 100).
    - supp8 would be reproduced (0.598).
    - supralinear would not be reproduced (0.031 and 0.093).
  - fig6b-enhancement-not-different would be reproduced under O3 (b) only (p = 0.073).
  - supp4 and fig7a stay partially reproduced.

  supralinear's outcome now also depends on which selective group is used, so I marked it `assumed: true` and added that assumption as a deviation. I did not propose changing these outcomes. The verifier called the selective-group assumption stated and reasonable, and the main analysis uses the test the Methods describe.
- **Band-edge checks (B6).** I re-ran the two decoders near a band edge with 20 more refits each:
  - fig3g: 0.6329 (s.e. 0.0012), 2.4 s.e. above the 0.63 edge, so partially reproduced holds.
  - supp8: 0.5840 (s.e. 0.0008), 1.2 s.e. below the 0.585 edge. The expected accuracy is within about 0.002 of the edge, and the notes say so.
  - supralinear is a count, 23 of 318 sets, with no sampling error: one set fewer would put it below the band.

**Not done**
- **B3 (methods-dt-modulation):** still not reproduced, and I found no other scoring reading in the Methods to try. It stays an open question to the authors.
- **B4:** the question whether the expected values are in Hz was already in `questions/laboy-juarez-2019.yaml`, so I added nothing.
- **Unrelated file:** the existing change to `tools/site_assets/list.js` was there before this run and I left it alone.

Nothing is committed.
