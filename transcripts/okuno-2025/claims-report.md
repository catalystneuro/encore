I wrote `claims/okuno-2025.yaml` and the quote checker passes it with no problems. Nothing is committed.

**Text read.** The eLife Reviewed Preprint v1 (9 October 2025, not revised), from the publisher's HTML. It has the main text, figure legends, Methods, Data availability and the Extended Data figure legends, which are the paper's only supplement. There was no PDF, so I could not read any figure. The text lost the Methods' displayed equations (the FC-SC detection and correlation score, cPPSSI, PPSSI and the two ranking scores); I took them from the code. I read the code at github.com/takuto-okuno-riken/flywalk, commit 4b92add (11 August 2025), the last commit before v1. Later commits answer the reviewers and change the method, so they are not this version's.

**Claims.**
- **Count:** 30 claims. 29 have quotes; one is `inferred` (the FlyEM permutation panels, which the text only cites).
- **Statistics:** 10 values: Mann-Whitney p<1.67e-4; acetylcholine r=0.39, p=0.0013 and GABA r=-0.25, p=0.046; the permutation p-values of Fig. 4e, f and i.
- **Criteria:** 24 claims have one.
- **Data:** 19 are `with_inputs`, because they set the dataset's FC against EM connectome SC or use the template and neuropil atlas from the code repository. 11 are `elsewhere`, on the FlyEM and FlyWire connectomes alone. None runs on the dandiset alone: even the walking GLM needs the repository's template and atlas.

**Details left open, and the readings named:**
- **O1, walking regressor:** the Methods say "1σ … divided into walking and other". The code builds a graded regressor (clipped at 1 SD, 10th-percentile floor). I followed the code and named a binary regressor as a variant.
- **O2, registration:** neither the paper nor the code gives the SPM12 or ANTs settings. Standard choice: SPM12 defaults with ANTs SyN; variant: rigid plus affine. Outcomes are marked as resting on it.
- **O3, sign of FC:** the code correlates SC with |mean z-FC|, the Methods just say "FC". I followed the code; signed FC is a variant.
- **O4, atlas for the GLM regions:** (a) the hemibrain atlas, (b) the JFRC2010 atlas also in the repository.
- **Per claim:** how "optimal" is judged in Fig. 1 (best in each ROI type, or best on average); which ROI type and SC kind give the 50, 1000 and 10,000 ROI ranges and the 20 ROI values; what "strong" activity means in Fig. 5b (peak t, or neuropil rank).
- **Thresholds I set myself:** some bars are mine, not the paper's, and each criterion says so. They are r ≤ -0.9 for "linear", a 0.05 margin for "ineffective", 0.4 to 0.6 for "mean close to 0.5", and below 0.25 for "biased toward 0".

**Missing from the paper:**
- **Values only in figures:** these cannot be known without the figures, mainly the per-method scores of Fig. 1 and the curves of Fig. 2b and 2c.
- **Number of Bonferroni comparisons:** not stated for Fig. 2c, so the criterion uses the printed threshold.
- **Steps missing from the code:** the NWB-to-NIfTI extraction and the registration scripts.
- **ROI atlases and connection lists:** the SCKm and DistKm atlases and the preprocessed connection lists are not in the repository. They are on Zenodo 10.5281/zenodo.15532271, and the claims file names that record.
