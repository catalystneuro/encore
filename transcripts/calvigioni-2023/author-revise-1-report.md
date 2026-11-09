I've revised the attempt against the round-1 report and changed one outcome: fig4e-opto-modulation-genotypes. The entry check reports 0 errors, and the clean run passed in 805 s. Its numbers match my development run line for line, and every conclusion matches them. Nothing is committed.

**Outcome change**
- **fig4e-opto-modulation-genotypes** goes from not reproduced to partially reproduced, as the verifier proposed.
  - Vglut2 and Esr1 are above controls, and all four groups respond to sound and air puff, under every seed, fitting period and saturation series. Only "Npy does not" fails: Npy is above controls at p = 0.044.
  - That failure is fragile. Over ten seeds, Npy is significant in only 5. With a Bonferroni correction for three comparisons p = 0.132, and comparing mice instead of pooled units p = 0.905.

All other outcomes match the verifier's and are unchanged.

**What I added or corrected**
- **GLM period (problem 1):** the helper docstring and the GLM section now say that fitting over blocks 1 to 4 is an assumption, chosen because the paper's code outputs match it. The whole session is shown as a variant.
- **Seed sensitivity (problem 3):** the tuned flags are repeated for ten seeds.
  - fig4g-tuned-unit-counts reaches the required 6 of 8 counts in 4 of 10 seeds, so it stays partially reproduced.
  - For fig4g-opto-tuning-score, the Esr1 corrected p ranges from 0.072 to 0.11, so it stays not reproduced.
- **Chance level (problem 8):** the false-positive rate of the tuned flags, measured on shuffled copies of each unit, is 0.23% (95% CI 0.13 to 0.36%), against the stated 0.11%. The sound and air-puff fractions (37 to 64%) are far above either.
- **LFP saturation (problem 5):** I ran the variant through all four GLM claims. It gives the same outcomes, and the notebook now explains why the code's 'spike saturation' series is the main choice.
- **Clustering quality control (fig4h):** the printout now flags the kept count as out of tolerance. Under the code's rule no fitted unit can be dropped: the fewest active bins of any unit is 454, against a cutoff of 200. None of the other readings I tried gets near 1,770 units.
- **fig4jl-pl-esr1:** the notebook now shows how weak the PL evidence is. PL ranks first on the first measure in only 51.7% of resamples over units and in 7 of 10 seeds. The rule still holds through the other two measures.
- **Blocked claims:** none of the 5,046 units outside the four regions is labelled LHA or LHb. I listed the BioStudies S-BSST1069 files: its cell-type codes 1 to 6 have no names, and their counts match the paper's only in part. I also described the eye data of the one mouse that has any (128514, Npy). All these claims stay blocked.
- **Text fixes:**
  - The ed8h conclusion wrongly said all narrow-spiking units have a peak-to-trough below 0.38 ms; 576 of 606 do.
  - The notebook now states that the decoding accuracies are inflated by temporal autocorrelation (problem 10).
  - The 5-point smoothing kernel is now described as the same kernel as the Methods' Gaussian, not a separate reading.
- **Supplementary tables:** I re-read Tables 6 to 8. The tuned-unit counts match the claims file. Table 6 reports 10 Esr1 and 5 Npy mice, but the data and the code's outputs only have units for 7 and 4. I recorded that as a paper inconsistency.
- **Other records:**
  - Two more findings: a question for the authors about the 1,770 count, and that the units table has no curation label, so 'good' units cannot be checked.
  - A new `questions/000473.yaml` asks a reader whether the ed9a criterion should also test the block-4 similarity, which does not hold on its distance measure. The claim itself is unchanged.
  - BioStudies is listed under inputs, and the README, `entry.yaml` (runtime now 13 minutes) and the summary are updated.
  - Round 1 is recorded under `verifications`, with the verifier's reason and my response for each of the 33 claims.

**What I did not do**
- I did not try to test fig2d-markers by guessing which code is which cell type, since the counts do not settle it.
- I did not open the 40.7 GB PatchSeq.zip, which holds raw reads, not labels.

The notebook now reads from ebi.ac.uk for the BioStudies listing. That worked here, but if the CI runner cannot reach it, that cell will fail.
