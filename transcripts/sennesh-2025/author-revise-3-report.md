Two outcomes changed and no proposals are left open.

The round-3 verifier agreed with both changes I proposed, so I applied them:

- **fig3h-go-alphabeta-csd-feedback** is now `not_reproduced`, changed from `reproduced`. I removed `proposed`.
- **fig3i-go-theta-csd** is now `not_reproduced`, changed from `reproduced`. I removed `proposed`. The verifier noted that this outcome depends on the minimum sink duration: reading a holds at 1/16 of a cycle and fails at 1/8 and 1/4. It accepted the outcome because the 1/8 value was set for all CSD claims together. The notes now say this.

The attempt record now has 14 reproduced, 10 partially reproduced and 13 not reproduced. No other outcome changed.

Files updated:
- **`attempts/sennesh-2025-01.yaml`:** I rewrote the notes for both claims and added round 3 under `verifications`. It has one result per reviewed claim, with `agrees: true`, `not_reproduced`, the verifier's reason in its own words, and my response.
- **`entries/sennesh-2025/v1_laminar.ipynb`:** I updated the Result cells for fig3h and fig3i and the Summary. That covers the two table rows and the sentence that said a change was proposed.
- **`entries/sennesh-2025/README.md`:** the CSD row now reads "3 reproduced, 6 not reproduced, all resting on an assumption".

`python tools/entry.py all entries/sennesh-2025` gave 0 check errors. The first run failed in `areas.ipynb` on a network read timeout from the archive. On the re-run both notebooks passed (v1_laminar in 992 s, areas in 1996 s). The re-executed fig3h and fig3i cells still print the onset times and window counts the text cites. Nothing is committed or pushed.
