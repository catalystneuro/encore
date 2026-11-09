I wrote the claims file at `claims/crcns-rrf-1/10.1016-j.cub.2021.02.055.yaml`.

**Text read:** the version of record with its full supplement: main text, STAR Methods, Table 1, Figures S1 to S6 and Tables S1 to S4. The extracted text mangles the layout of Tables S1 to S4, so I rendered those pages and Figure 6 from the PDF to read them. Figure 6 is also the only source for each cluster's outcome window.

**Code:** none was read. The paper says its MATLAB code goes to crcns.org, which puts it inside the dataset that readers may not open. The lab page it names, http://mcdannaldlab.org/resources, returns 404. Every method in the file comes from the STAR Methods, the Results, the figure legends or the supplement.

**Counts:** 30 claims. 29 have quotes; 1 (`table-s3-cluster-regression`) is marked inferred because its results appear only in Table S3. 104 statistical values are recorded and all 30 claims have criteria. Every quote passes the checker. The checker still exits with 9 problems, all p-values or CI bounds it cannot match because the text prints them oddly (powers of ten as "3 10�", Table S3's E-notation, the Figure S4 bound "1-.62"). I confirmed each one by reading.

**Details the paper leaves open, and the readings named for each:**
- **Normalization:** the z-score is taken over four trial types or over three (uncertainty pooled).
- **Cluster labels:** use the paper's own labels if the dataset holds them, or redo the k-means and match each cluster to k1 to k8 by its described cue firing pattern.
- **K-means:**
  - The six outcome epochs start at shock onset or at shock offset.
  - "Performed 10 times" means ten replicates per k or ten separate runs.
  - The input is normalized firing (Results) or raw firing rate (Methods).
- **The elbow at eight clusters:** the paper judges it by eye. I set a standard rule (every drop after k = 8 smaller than the drop from 7 to 8) and said that it is one.
- **Tuning curves:**
  - Average the 10 cue bins (Methods) or each cluster's own period from Figure 3 (Results).
  - Normalize each trial with the unit's mean and SD, or z-score across the unit's 16 trials.
- **Peak threat probability regressions:**
  - The sign is flipped for k4, k6 and k8 as it is for the tuning curves, or left as computed.
  - The Results call bin a between-units factor, but the printed df fit a within-units factor, which is the main reading.
  - Those df imply 362 units, not 364; the author is asked to report which units drop out.
- **Figure 5F:** each unit's betas are averaged over the 10 cue bins or over all 14 bins.
- **Behavior:** each rat's value is the mean over sessions or over all pooled trials.
- **Firing characteristics:** inter-spike intervals are pooled over the 16 trials or the measure is averaged over trials.
- **ANOVAs:** the printed partial eta squared values fit repeated measures with units as subjects, so that design is used. Whether a sphericity correction was applied is not stated; uncorrected df are the main reading and Greenhouse-Geisser a variant.

**Missing from the paper:**
- No analysis code was available, as above.
- The paper gives no numbers for the Figure 6 differential CIs. Their signs were read from the figure (the plus signs) and the per-trial-type values come from Table S4.
- The time courses described as early or sustained for k6, k7 and k8 appear only in the traces. Those claims are judged on each cluster's single Figure 6 window.

Nothing is committed.
