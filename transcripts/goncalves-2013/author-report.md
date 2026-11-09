I tested 11 of the 28 claims: 5 reproduced, 3 partially reproduced and 3 not reproduced. The other 17 are blocked because their data are not in ssc-8. The entry passed `tools/entry.py all` with 0 errors, and the notebook runs in 203 s. The handover package is in `executed/crcns-ssc-8-goncalves-2013/handover/`. Nothing is committed.

**1. Outcomes**

| Claim | Outcome | Key numbers |
|---|---|---|
| group-sizes | not reproduced | 13/8/7 WT and 9/10/6 KO mice, against 12/9/8 and 9/10/8 in the paper |
| fig1d-distance-dependent-decorrelation | partially reproduced (assumed) | drops of 0.191, 0.105, 0.025 against 0.223, 0.159, 0.067; the significance pattern holds |
| fig1e-age-decrease | reproduced | p of 1.8e-07 (WT) and 8.1e-08 (KO) |
| genotype-pooled-ages | partially reproduced (assumed) | p = 0.0064 (paper 0.0057); no reading puts both means within the s.e.m. |
| pearson-genotype | partially reproduced (assumed) | p = 0.023 (paper 0.026); means not both within the s.e.m. |
| fig1ef-p14-16-difference | not reproduced (assumed) | means match (0.169, 0.204), but Student's p = 0.057; the difference is not largest at P14-16 |
| p30-40-no-difference | reproduced | p = 0.22 |
| fig2b-peak-frequency | reproduced | 0.060 and 0.054 per s, p = 0.52; the same under all four readings |
| fig2c-participation | not reproduced | p = 0.15 to 0.37 under all eight readings |
| imaging-firing-rate-no-genotype-difference | reproduced | p ≥ 0.73 at every age |
| unanesthetized-p14-16-values | reproduced | 0.304 and 0.304 Hz; WT correlation 0.169 |
| 7 whole-cell, 6 EEG, 1 at 15.6 Hz, 3 isoflurane claims | blocked (`data_missing`) | none of these data are deposited |

For the blocked suppl4a claim I ran a variant on 3-min segments of the recordings. It does not decide the outcome.

**2. The dataset, assumptions and questions**
- **Group sizes:** the dataset has 53 mice where the paper has 56, and the groups differ in size. Nothing says why.
- **Descriptor errors:** neuron counts go up to 198 (the descriptor says 40 to 149). Recordings last 3.8 to 15.4 min (it says 7 to 8). It gives no unit for the firing rates; the values fit Hz.
- **Frame rate and size:** the movie folders are named "4Hz", but the paper says 3.9 Hz. Most recordings are 2160 frames, which is three 3-minute movies at 4 Hz. Frames are 128 x 256 pixels, while the Methods say 512 x 128.
- **Clock check:** each rate matrix k belongs to `Movie_k.tif`, and they share one frame clock. This holds for all 53 recordings, but the descriptor does not say it.
- **Duplicates and stray files:** no recording is deposited twice. The TIFF archive also holds 5 macOS `._` resource-fork files.
- **Not deposited:** cell contours, dF/F traces, and the whole-cell, EEG, isoflurane and 15.6 Hz data.
- **Assumption:** correlations use the deposited deconvolved rates (reading T-a). Reading T-b, the filtered dF/F traces, cannot be rebuilt without cell contours. So the four correlation outcomes that are not plain matches carry `assumed: true`.
- **Questions for the paper's authors** (recorded as `methods_unavailable` findings):
  - Which trace and measure the correlation uses, including mean subtraction and lag.
  - For peaks of synchrony: when a cell counts as active, how traces were shuffled, and how participation is formed.
  - How the pooled average was formed and how the ANOVA was fitted. The paper's s.e.m. match a mean of the three age means.
- **Questions to a reader:** none.

**3. Where the protocol was unclear**
1. Step 2 (clock check) assumes trial tables or annotations, and this dataset has neither. I compared the population rate against each movie's frame brightness, against the other movies and against time-shifted rates instead.
2. archives.md does not say that `+` in a CRCNS file name must be URL-encoded as `%2B`. Without it the bucket returns 404. I encoded it.
3. "Run every reading" does not cover a reading that cannot be run at all (T-b). I ran T-a only and marked the outcomes that rest on it as assumed.
4. A `.tar.gz` cannot be opened in place the way a zip can. I streamed it once in order, holding one movie in memory at a time, and hashed each member, since the archive's own MD5 needs the whole compressed stream.
5. The protocol does not say whether a variant for a blocked claim may have its own tagged cell. I tagged it `variant:suppl4a-...` and stated that it decides nothing.

**4. Runtime and failures**
- The run took about 42 minutes (08:13 to 08:55 UTC).
- The first attempt to read the TIFF archive failed with a 404 until I encoded `+` as `%2B`.
- In one exploratory pass, parsing the TIFFs with the `tifffile` library peaked at 7.3 GB of memory. I replaced it with a small parser in the helper module, and streaming a member then peaks at about 0.5 GB.
