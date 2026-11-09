**Verifier report, round 3: Chartrand et al. 2023 (doi:10.1126/science.adf0805) on DANDI:000630 0.230915.2257**

The claims file has 41 claims and the attempt record has 41 outcomes. Three outcomes carry a `proposed` block (record lines 124, 227 and 390), and these are the only ones I reviewed. Cell numbers refer to `reproduce_chartrand_2023.ipynb`. `docs/protocol.md` is not among my materials, so I worked from the task statement.

| Claim | Proposed | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| fig2c-subclass-ephys-differences | reproduced | Yes, on one condition (the assumption must be recorded as a field, see below) | — | See point 1. |
| fig2c-lamp5-gradient | not_reproduced | Yes | — | See point 2. |
| fig6a-ephys-dprime-subclass-structure | not_reproduced | Yes | — | See point 3. |

**1. fig2c-subclass-ephys-differences**

*The numbers come from the data.*
- c27, variant (a'): first_isi_inv_hero has FDR p = 3.90e-9 (n = 179) and sag has 3.28e-20. Both are below 1e-7.
- c27, reading (a): first_isi_inv_hero has 4.70e-7, which is above the threshold. On the paper's values (reading b) it is 1.67e-8.
- c18 confirms the counts the proposal cites:
  - 16 cells fall back to another sweep; in 9 of them the value disagrees with the paper's, and 7 of those 9 agree in (a').
  - The median share of cells within 1% of the paper's value rises from 0.895 to 0.933.
  - The share is higher in (a') for 38 of 39 features. The one lower is fi_fit_slope, 0.707 to 0.695.
- From the c18 table I checked the fig2c subset in the notes: 11 fallback cells, 6 of them disagree, and 4 of those 6 are resolved in (a').

*The choice was not made to reach the result.*
- (a') was added after (a) missed the threshold, in answer to my round-2 question about the hero sweep.
- It is justified by a check that does not involve the p value: agreement with the paper's own per-cell values, across all 39 features and not only this one (c18).
- It is applied to every claim, and the record says it changes no other outcome.
- Reading (b) also falls below 1e-7.
- So I accept (a') as the recomputation best supported by the paper's own values.

*The criterion is applied as written, with one caveat.*
- The threshold is applied as the criterion states.
- However, O1 reading (a) is "the Methods' definitions with IPFX conventions", and (a') drops one of the Methods' sweep QC criteria (rms < 0.5 mV over 500 ms, `l1ephys.py:250-287`, extracted with `max_rms_long_mv = inf`). Reproduced therefore rests on a departure from the Methods' QC as IPFX measures it.
- The record states this only in prose ("(assumed: true)" inside the reason). My condition: the outcome should carry it as a structured assumption, together with the question to the authors about how the 500 ms noise was measured.

*Fragility, not decisive.* The leave-one-donor-out check (c28) was run only on reading (a). Its worst uncorrected p for first_isi_inv_hero is 3.5e-5, and it was not run on (a').

**2. fig2c-lamp5-gradient**

- c38: the test covers 96 LAMP5 cells of the strict set (NMBR 71, LCP2 13, DBP 12), with filter_dropouts=False.
- first_isi_inv_hero passes under every reading: rho 0.45 to 0.46, FDR p 2.5e-5 to 3.0e-5.
- Sag fails under every reading. Its rho is positive, but its FDR p is:

| Reading | Sag FDR p (threshold 0.001) |
|---|---|
| (a) | 0.022 |
| (a') | 0.015 |
| (b), the paper's values | 0.0020 |
| Three sites, 113 cells | 0.0039 |

- The criterion requires both features below 0.001 and names no partial level. The record already applied not_reproduced on that ground to fig4b-adarb2, fig4d and fig5d, so not_reproduced follows.
- For a reader (reported, not corrected): even the paper's own values, under the method the claims file prescribes, give sag FDR p above 0.001 (c38). Either the claims file's method differs from what produced the paper's "p<10−3", or that statement does not hold for sag. I can't tell which from my materials, since the code is not among them.

**3. fig6a-ephys-dprime-subclass-structure**

- c56, all nine runs (readings a, a' and b, seeds 0 to 2):
  - Mean within-subclass d' (1.12 to 1.31) is below mean between-subclass d' (2.39 to 2.56).
  - Under "high" as d' ≥ 2.2, NMBR/LCP2 is the only high within-subclass pair in 7 of 9 runs. The exceptions are reading (b) with seeds 1 and 2, where no within-subclass pair reaches 2.2.
  - Under "high" as above the median between-subclass d' (2.40 to 2.62), no within-subclass pair is high in any run. For example, NMBR/LCP2 is 2.39 against a median of 2.62 (reading a, seed 0).
- The criterion requires both readings and names no partial level, so not_reproduced follows.
- Both cell-count rules (at least 5 or at least 4 cells) keep the same nine t-types, so only one was run, which is correct.
- For a reader (reported, not corrected):
  - In the paper (main text, line 129 of `paper/10.1126-science.adf0805.txt`), the sentence "The single within-subclass pair with a high d’ was LAMP5 NMBR and LAMP5 LCP2, which sit at opposite ends of the LAMP5 continuum" follows the cross-modality comparison (Fig. 6B). It may refer to the transcriptomic matrix or to both matrices, not the electrophysiological one alone.
  - The outcome turns on the reader's second reading of "high", which the paper does not define.
