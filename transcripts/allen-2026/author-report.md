The attempt is recorded, the entry's checks pass (0 errors), the notebook runs clean in 63 s with a 3.9 GB peak, and the verifier's handover is built in `executed/allen-2026/handover/`. Nothing is committed.

## 1. Outcomes (31 claims)

| Claim | Outcome |
|---|---|
| fig1b-metabolic-rate | reproduced |
| fig1c-ammonia-excretion | reproduced (the paper's F and p exactly) |
| fig1d-blood-ph, fig1e-blood-pco2, fig1f-blood-bicarbonate | reproduced |
| methods-body-size, stable5-seawater-chemistry, stable3-acute-shallower, sfig4a-amplitude-attenuation | blocked, data_missing |
| sfig2-distance-unchanged, fig2c-velocity-unchanged | reproduced (the paper's H and p exactly) |
| fig2d-acute-upper-zone, fig2e-left-right-unchanged, fig2f-front-back-unchanged | reproduced |
| fig2g-attack-willingness | not reproduced |
| fig2h-hunt-duration, fig2i-strike-attempts, sfig3-prey-velocity-unchanged | reproduced |
| fig3c-ratio-declines | not reproduced |
| fig3d-cff-unchanged, fig3d-cff-variance | reproduced |
| rnaseq-assembly | reproduced (mapping rate not in the dataset, so not tested) |
| fig4a-pca | partially reproduced, rests on an assumption |
| sfig5b-acute-clusters-with-control | reproduced |
| fig4b-shared-down-sets, fig4fgh-chronic-up | partially reproduced |
| fig4c, fig4d, fig4e, chronic-nachr-subunits-down | reproduced |
| optic-lobe-no-ion-regulation | not reproduced |

**Why the three not-reproduced claims failed:**
- **fig2g:** the per-squid file lacks 11 chronic-OA squid. The workspace's own Figure 2G table has 22, and with those counts the paper's model comes out exactly.
- **fig3c:** the ratio stays near 1 up to about 50 Hz, so "below the 20 Hz value at every frequency above 40 Hz" fails in all groups.
- **optic-lobe-no-ion-regulation:** three ion-transport terms are significant under chronic-OA.

## 2. Dataset, assumptions and questions

**What the dataset holds.** One version is public (439366). It has per-squid CSVs and `squid.zip`, which holds the authors' scripts, the ExN50 statistics, the RSEM count matrix and their R workspace (1.1 GB). The workspace contains the DESeq2, sva and GSEA results and the per-figure tables. I wrote a streaming reader for R's file format in `squidoa.py`, because the general `rdata` package needed 12 GB and 5 minutes. The RNA-seq claims were therefore tested on the authors' own objects; the only outside input is the TSA record's sequence count.

**Findings about the data:**
- **Critical:** the count matrix header names 16 samples but each row has 15 values. The values are the gill sample plus 14 optic lobe samples; `Re_8.1_OL-3` is missing. Read the way the authors' script reads it, every sample name shifts by one.
- **Critical:** in the workspace's shrimp-velocity table, the CO2 10 to 20 min column is an exact copy of the control column.
- **Major:** the prey capture file is missing 11 chronic-OA squid.
- **Major:** the deposited hemolymph PCO2 values are one tenth of what the formula printed beside them in `Carbonate_calibration.csv` gives. The files don't show which of the two is wrong.
- **Major:** the 3-D tracks, ERG recordings, seawater chemistry, mass and mantle length are not deposited, although the paper's Data availability says they are.
- **Minor:** the zone file has a 9th acute-OA squid the paper left out, unmarked. Leaving out that one row gives the paper's sums of squares exactly.
- **Minor:** the metabolic rate file has 26 squid against the paper's 29.
- **Minor:** no squid identifiers, and the README gives the PCO2 unit as "atm".

**Paper-side findings:** the sign of the logistic regression intercept in Supplementary Table 4 is wrong, and the PCA chunk of the deposited script disagrees with the figure.

**Assumption:** for fig4a, the control "spread" is read as the range of the control samples. Under the SD reading the claim would be reproduced. This is recorded as a `methods_unavailable` question for the paper's authors.

**Questions to a reader** (`questions/allen-2026.yaml`):
- fig4b: the "36" is the sets significant in both treatments. The paper calls it "the intersect GSEA ridgeplot" and the script plots exactly 36. Neither of the criterion's readings matches.
- fig4fgh: the paper's counts (82, 314, 128) match the script's subset (up in chronic-OA and not down in acute-OA), not all up-regulated sets (101, 321, 133).

## 3. Protocol issues

1. Claims marked `data: elsewhere` (SRA/TSA) whose processed data are actually in the dataset have no category. `entry.py check` requires `inputs` for them. I tested them on the dataset's objects and added the TSA sequence count as a real input, noted in the record.
2. The protocol does not say how to judge a criterion that lists readings when the paper's own code settles a different one (fig4b). The claims header permits taking open details from the deposit's scripts, but the protocol says to test as written. I tested as written, showed the code's reading as a variant, and asked a reader.
3. "Measured" has no way to mark an expected value that cannot be measured (the mapping rate). I left `measured` out for rnaseq-assembly and gave the values in the notes.
4. The protocol does not cover tests with no SciPy equivalent (GraphPad's Welch W and Dunnett's T3). I implemented them; Welch W and the T3 intervals differ from Supplementary Table 2 without changing any conclusion. This is recorded as a deviation.
5. The rating guide doesn't fit a duplicated column that anyone comparing columns can see but that silently corrupts an analysis. I rated it critical, citing the "deposited as two" example. The verifier should review that rating.

## 4. Runtime and failures

The run took about 40 minutes (20:07 to 20:46 UTC). The notebook runs in about 63 s. During development the general `rdata` parse took 5 minutes and 12 GB, which is why I replaced it. A first read of the count matrix failed on its header mismatch, which is how the critical finding above was found. Nothing failed in the final run.
