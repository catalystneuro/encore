## Round-2 verification: Clark & Nolan 2024 (eLife 89356) on DANDI:000943 v0.240614.0754

### 1. Outcomes

The claims file has 31 claims and the attempt record has 31 outcomes, one per claim id. All 31 are `blocked`, `too_large`, and I agree with every one.

- **Why all 31 are blocked:** cell 4 shows that none of the 734 files has a units, processing or intervals table. Cell 21 shows that reading the 638 GB of the relevant days alone takes 2.4 h at 72.4 MB/s. That is more than the 60-minute limit, and sorting time would come on top.
- **Assumptions:** no outcome carries `assumed: true`. The outcomes rest on two inputs taken from outside the notebook's own measurements. Both are now stated and reasonable:
  - the 60-minute limit, quoted from docs/protocol.md in cell 20;
  - the 200 cm track length and the 10-trial minimum, taken from the claims file and from the files' notes printed in cell 5.
- **Alternative block reason:** `data_missing` could still be argued, as I said in round 1. Either way every claim stays blocked.
- **Claims file:** I found no misreading of the paper that affects these blocks.

### 2. Sentences the printed outputs do not support

None of these changes an outcome.

- **Notes of all 31 outcomes, and the round-1 responses:** they give the rate as "73 MB/s", but cell 21 prints 72.4 MB/s. The notes also say "638 GB of the 239 days". Cell 10 prints 239 *sessions*, and cell 21 prints 478 files; the number of days is never printed.
- **"open arena sessions of M1 … span about 70 cm"** (outcome notes for grid-cell-count; cell 13; Summary, cell 22, "of M1 and M2 span about 70 cm"):
  - Cell 12 shows that only 18 of M1's 41 and 20 of M2's 21 open-arena sessions span less than 90 cm.
  - Those sessions span 67.5 to 89.8 cm, and the other sessions start at 88.0 cm, so the two groups overlap.
  - The findings entry ("38 … span only 67.5 to 89.8 cm") is accurate.
  - My own round-1 point 3 used the same loose wording.
- **Cell 22, Summary:** "counts differ from the paper's table for four of nine mice". Cell 10 shows five mice differ (M13 has 27 against 25). Four mice differ by more than 10%.
- **README:** "the raw signal of the sessions the paper used (638 GB)". The 638 GB covers the 239 paired sessions of cell 10, not the paper's 215, so it is a superset. A proportional reduction (about 574 GB, about 2.2 h) would still exceed the limit.
- **Cell 9:** "position from 0 to 200 cm on the paper's track". Cell 8 prints only the overall range of 0 to 342 and a track length taken from the median of per-trial maxima. It never prints the range for the 200 cm sessions.
- **Findings, `kind: other`:** "up to 452 s longer and 178 s shorter" is not printed. Cell 12 prints only the median, the 5th to 95th percentiles and the count over 10 s.
- **Findings, `metadata_insufficient`:** "column 6 (values about 30 to 37,700)". Cell 12 prints a median minimum of 1793.02 and a maximum of 37697.43. The lower value of about 30 is not printed.
- **Findings `data_missing`, README and Summary:** "a single 26.5 GB pickle (combined_cohorts.pkl) that cannot be read in part" appears in no notebook output and nowhere in the paper text. It is unsupported here.
- **Findings, `metadata_error` (description):** the quotation leaves out the colons of the printed string ("position: cm, speed: cm/s, …", cell 4). This is minor.

The other sentences match the outputs. I checked:

- cell 11's percentages (15/22/56/33%, up to 43%, within 3%);
- cell 19's clock figures (7 of 9 peak lags within 0.5 s; peaks 0.09–0.34; ratios 1.06–1.27; M14 1.00; M3 and M12 at +1.8/+1.7 and +2.0 s);
- the 2.4 h and 3.7 h figures;
- the counts in the findings (379/355, 29 longer tracks, 48/24 single-type days, the two partial VR files).

**My round-1 reasons in the record:**

- They are in my words, mostly verbatim. Where I wrote "Same.", the record expands it correctly.
- The cell numbers they cite (cells 6, 8 and 19) refer to the round-1 notebook; they are now cells 8, 10 and 21.
- The `reviewed` field says I "found no misreading of the paper in the claims file". I said none that affects these blocks, so the field slightly broadens what I said.

### 3. Round-1 points

**Resolved:**

- **B1:** cell 20 now cites and quotes the protocol limit and calls the estimate a lower bound.
- **B2:** cell 11 now states the difference of 27 against the 21.5 tolerance and the 56% gap for M10.
- **B4:** the helper docstring now says 100 ms bins.
- **B5:** I read the code. `shifted_contrast` no longer wraps around and labels `mua[t]` by `speed[t+sh]`, the same convention as `lagged_corr`. M3 and M12 now give +2.0 s, next to their correlation peaks. I could not re-run my synthetic test because numpy is not installed here.
- **C2:** cell 5 prints `general/notes` and `experiment_description`. They show the 200 cm track statement, the 4.7 cm/s stop over 100 ms, and the 100 × 100 cm open field.

**Addressed, but with wording to fix:**

- **B3:** the inferred open-arena columns and the M1/M2 extent are now stated in cell 13 and in the notes. The "about 70 cm" wording in section 2 needs correcting.

**Remaining:**

- **C1:** docs/protocol.md is still not among my materials, so I can check the quoted limit only as quoted. No timed sort was run. This does not bear on a conclusion, because the read-time lower bound alone is 2.4 times the limit.
- **Text corrections:** the wording issues in section 2 should be fixed, but none of them bears on a conclusion.

Nothing that remains changes any of the 31 outcomes.
