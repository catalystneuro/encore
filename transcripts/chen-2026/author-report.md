I've finished attempt `001933-chen-2026-02`. The entry runs from a clean environment in about 8 minutes, and the handover is built in `executed/001933-chen-2026/handover/`. Nothing is committed. `tools/entry.py check` still reports 8 errors, all in the earlier record `001933-chen-2026-01.yaml`, which I left as it is (point 4 below).

**What pilot-7 changed.** It adds a claim kind, `data: elsewhere`, for data the paper put in another public archive, and `data_missing` now means public nowhere. The eight Figure 1 to 5 claims were blocked as `data_missing` in -01. They now carry `data: elsewhere`, a `where:` and criteria, and are tested on Zenodo, PRIDE and BioImage Archive data, counted apart from the dandiset's claims. The ten photometry claims are unchanged. Version 0.260825.1457 is still the draft's content, so the helper constant, `entry.yaml`'s `dandi:` relation and the notebook header keep that version.

**1. Outcomes (this attempt, with -01's in brackets)**

| Claim | Outcome (-01) |
|---|---|
| source-data-link | not reproduced (not reproduced) |
| fig6e-anxa1-evoked-reduced | reproduced (reproduced) |
| fig6e-anxa1-evoked-per-mouse | reproduced (reproduced) |
| supp7c-anxa1-evoked-all-powers | reproduced (reproduced) |
| fig6f-anxa1-spontaneous-reduced | reproduced (reproduced) |
| fig6f-anxa1-spontaneous-per-mouse | partially reproduced (partially reproduced) |
| supp8c-calb1-spontaneous-not-reduced | reproduced (reproduced) |
| supp8e-calb1-evoked-reduced | reproduced (reproduced) |
| supp8e-calb1-few-mice-reduced | partially reproduced (partially reproduced) |
| cohens-d-anxa1-larger | not reproduced (not reproduced) |
| fig1d-lrrk2-enriched-vulnerable | reproduced (blocked, data_missing) |
| fig2b-rab3-phosphorylation | not reproduced (blocked, data_missing) |
| fig2eg-prab3-increased | reproduced (blocked, data_missing) |
| fig3d-rim-binds-unphosphorylated | reproduced (blocked, data_missing) |
| fig4d-fewer-active-zones | partially reproduced (blocked, data_missing) |
| fig4i-rim1-reduced | reproduced (blocked, data_missing) |
| fig5-bassoon-vulnerable-axons | partially reproduced (blocked, data_missing) |
| fig5j-no-axon-loss | reproduced (blocked, data_missing) |

Three of the new outcomes rest on something you should know:
- **fig2b:** on the abundances as deposited, 1694 peptides pass the thresholds (the paper says 289). The RAB3 T86 peptide is altered, but in the wrong direction.
- **fig3d:** RILPL2 is found only in the p-RAB3A pulldowns, so the criterion's paired test cannot run for it. I decided it with the Methods' imputation and recorded that as a deviation; without it the count is 3 of 4, which would be partially reproduced.
- **fig4d:** the per-area values on Zenodo show both effects. My Python version of the Methods' FIJI image analysis shows neither, but it finds far fewer synaptosomes per image than the paper (median 183 against about 1000), so that part may be my implementation failing.

**2. Earlier findings.** None is fixed; the dandiset, the code and the paper are unchanged.
- Still present: the Calb1 dF/F is not the paper's (0 of 384 traces match), the 4398 series ends early, the epochs table description is wrong, mice 3742 and 4885 got 0.33 s trains, the dF/F unit is "a.u.", the archive summary lists only a behavioral approach, the excluded mice are left out without a note, the three code mismatches (repository still at d34558f), the Welch/Student/tail inconsistency, and the paper still does not cite the dandiset.
- One changed kind: "Figures 1 to 5 not in the dandiset" was `data_missing`. Under pilot-7 those data are public elsewhere, so I recorded it again as `other`: the dandiset does not link to those deposits.

**3. New findings, about the other archives**
- **Figure 2B direction:** in PRIDE PXD065006 (the same table as Supplementary data 1), the RAB3 T86 phosphopeptide is higher in the samples labelled MLi-2. The paper's own volcano table is MLi-2 minus vehicle, while the legend reads positive as higher with vehicle. Either the sample labels or the figure's direction is swapped. At the legend's thresholds that table gives 254 peptides, not 289.
- **Figure 3 counts:** the text gives 69 and 16 proteins at p < 0.05. The deposited limma table gives 121 and 32 at that p, and 69 and 16 at adjusted p < 0.05. The Figure 3E/3F p-values come from tests on intensities without the log, which the legend does not say.
- **Figure 1D:** the legend's unpaired test over 16 sections gives p = 4.65e-06. The paper's 0.0008 matches a paired test, or a test on the three mouse means.
- **Figure 5D/5E:** one WT section appears twice in the source data. Counted once, as the claims file fixes, one comparison moves from p = 0.0344 to 0.058. That is why fig5 is partially reproduced.
- **Counts:** Figure 4E has 51 G2019S areas against the legend's 57, and the 5E legend repeats the 5D genotype F value.
- **Identifiers:**
  - The source data name no G2019S animals for Figures 5G, 5H and 5J.
  - The image study for Figure 5 names a WT mouse 1923 where the source data say 1723.
  - The synaptosome images name mice only as 1 to 5.
- **Image studies hold images the figures do not use, without saying which were used:** extra images in the Figure 1 study, an extra WT mouse in the Anxa1 study, and 64 volume images per genotype where the legend gives 96.
- **No method for some values:** the Imaris image analyses and the western blot quantification cannot be recomputed from what is deposited.

**4. Where the protocol did not fit a repeat attempt**
- **The check fails on the earlier record.** It applies the current claims file to every attempt of the entry, so -01's eight `data_missing` blocks fail the new `elsewhere` rule. You told me to leave -01 unchanged, and the pilot notes say pilot-6 attempts keep their claims. There is no exemption by protocol version, so `entry.py all` stops at the check; I ran `check` and `run` separately. The workflow's check will fail on this until the tool is changed.
- **One claims file serves both attempts.** Updating it for pilot-7 also changes the claims that -01 points to.
- **Repeat attempts assume a changed dandiset.** Here only the protocol changed, so "fixed or not" is trivially "still present". There is no rule for an earlier finding whose kind becomes invalid under a new protocol.
- **Findings are defined as being about the dandiset.** The `elsewhere` claims produce findings about other archives, and the schema has no field for which archive. I named it in each statement.
- **Criteria for the eight new claims came after seeing the data.** I wrote them after seeing the deposited values, though before computing any statistic; the claims file's opening comment says so. For fig2b, the criterion did not fix a normalisation step, and that decided the outcome; the normalised result is shown as a variant.

New files: `attempts/001933-chen-2026-02.yaml` and `entries/001933-chen-2026/archives.py` (a helper for the archive data and the image analysis). Changed: the notebook, `README.md`, `entry.yaml`, `requirements.in` (adds scikit-image and tifffile), the lock file and the claims file.
