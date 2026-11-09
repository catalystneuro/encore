I finished steps 1 to 5 and ran the handover. The notebook passes `check` and runs from a clean environment in 760 s, which is over the 10-minute aim but under CI's 30-minute limit. Nothing is committed.

**Paper:** I used the full text of the author manuscript in PubMed Central (PMC8930615), saved under `paper/`. The supplement PDF was blocked by a browser check, so claims on Figures S1 to S7 rest on the main text only.

**Version:** pinned 0.261013.1707, the latest published version. The paper predates the dandiset and cites no version. All three published versions and the draft hold the same 4139 files (same blobs); they differ only in dandiset-level metadata. The notebook header says this.

### 1. Outcomes (38 claims)

| Outcome | Count | Claims |
|---|---|---|
| Reproduced | 18 + 1 on Zenodo data | fig1f, fig2b, fig2c, fig2d, fig2m, fig2n, figs1i, figs2b, fig3h, fig4f, fig4h, fig5h, fig5i, fig6h, fig6i, fig7g, fig7h, fig7i; the Zenodo one is figs3ab |
| Partially reproduced | 8 | fig1e, fig2a, fig2k, fig2l, fig2o, fig3g, figs5f, fig6g |
| Not reproduced | 7 | fig1d, fig3f, fig4g, fig5f, fig5g, fig6-nphr-learning-dropout, fig7f |
| Blocked, data missing | 4 | fig3e (RI30 photometry), figs1a (fear conditioning), figs3cd (open field), fig3c (histology) |

The main photometry results do not hold here. The DMS score is in the paper's order across phenotypes but not significant (p = 0.100). Its correlation with shocks is r = 0.17 pooled; only early sessions alone reach significance (r = 0.375, p = 0.045). The DLS score correlates with shocks (r = 0.326, p = 0.024), where the paper finds none. That last result depends on a dropout-masking step I added (item 3 below); without it r = 0.113.

### 2. What the dandiset holds and lacks

- **What is there:** operant behavior for the fiber photometry cohort and three optogenetic cohorts, and photometry for 62 RI60/RR20 sessions. The photometry mice carry their phenotype labels in the files, which made Figure 2 testable.
- **Missing photometry:** none for RI30 or the shock probes, though the Methods say they were recorded.
- **Missing mice:** 6 of 9 RR20 mice are present, 33 of 39 DMS excitatory, 42 of 47 DMS inhibitory and 35 of 36 DLS excitatory. Several mice lack one shock probe.
- **No markers:** nothing marks inhibitory group 1 vs 2, and optogenetic mice have no stored phenotype.
- **Duplicates and misfiling:** 137 "Unknown" DLS files repeat sessions filed under named arms (counted once). Mouse 290.407 is filed under two experiments.
- **Format errors:** in left-side shock probes the reward series is named `right_reward_times`. One stitched photometry session mixes MedPC reward times with TDT nosepoke times.
- **Data quality:** six photometry sessions have raw-channel dropouts that push the z-score above 1000 without the masking step.
- **Metadata:** fiber coordinates are stored without their minus signs.
- **Label vs rule:** one stored label (048.392) disagrees with the Methods rule by one shock (13 is not "more than 13").
- **Paper inconsistencies:** omission times are printed in seconds but are minutes. Group sizes differ between the Methods and the figures.
- **Zenodo densitometry:** female samples only, and the labels read as lanes from one wild-type and one heterozygous mouse.

### 3. Where the protocol was unclear, wrong or missing something

1. **Supplement not reachable.** The protocol covers full text vs abstract but not a full text whose supplement can't be fetched. I used the main text and noted it in the claims header.
2. **Tolerance from "stated spread".** When that spread is the SD across mice, the tolerance becomes very wide (e.g. DPR 2.1 ± 2.63). I followed the protocol, which makes the pairwise tests decide most of these claims.
3. **Processing choice made after seeing scores.** Masking photometry dropouts was decided after I had seen per-session scores. The protocol has no rule for a data-quality fix found that late. I recorded it as a deviation and show the authors' processing without masking as a variant.
4. **Absence claims with no test in the paper** (fig7f, fig7h, figs3ab). The protocol says to judge absence on the paper's test, which doesn't exist here. I chose tests before running them. My fig7f criterion ("no group by index interaction") was ambiguous; I judged it on all three group pairs.
5. **Data only partly deposited.** The fig6 dropout claim ran, but most dropped mice are probably not in the dandiset. No outcome category fits "tested, but the data needed are only partly there". I followed my pre-written criterion (not reproduced) and said this in the notes.
6. **Early/late probe rule changed after the data check.** Some mice have one or three probe days, so I refined the rule after seeing the data, which the protocol allows. The claims header records it.
7. **Runtime aim vs size.** Ten minutes is hard with 4139 files. Selecting files from the asset-list metadata (no file opens needed) brought loading down to about 2200 files.
8. **Version pinning.** The protocol doesn't cover a paper that predates its dandiset when all versions have identical content. I pinned the latest and said why.

### 4. Runtime and failures

- **Runtime:** the notebook takes 760 s, about 440 s of it streaming events and 310 s photometry.
- **Paper downloads:** Europe PMC full-text XML returned a 500 error, NCBI BioC rate-limited then overloaded, and the supplement was blocked by a browser check. The PMC HTML page worked.
- **Analysis:** nothing failed.
- **Stray files:** git shows untracked `.bashrc`, `.idea`, `scripts` and similar at the repo root. They are sandbox device mounts, not files I made, and I left them alone.

Files are in `entries/000971-seiler-2022/`, `claims/000971/` and `attempts/000971-seiler-2022-01.yaml`; the verifier's package is in `executed/000971-seiler-2022/handover/`.
