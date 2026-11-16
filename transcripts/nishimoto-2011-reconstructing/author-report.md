I finished the author steps 1 to 6 on CRCNS vim-2: the entry is written, locked and run, the attempt record is written, and the handover is built. Of the ten claims, four were reproduced and six are blocked, three by data not in public and three because I ran out of time. `python tools/entry.py all` passed with 0 errors, and the notebook ran in about 26 min with a peak of 11.7 GB of memory. Nothing is committed.

### 1. Outcomes

| Claim | Outcome | Measured (paper) |
|---|---|---|
| fig2de-prediction-accuracy | reproduced | static 0.217, nondirectional 0.375, directional 0.379 (0.24, 0.39, 0.40); both Wilcoxon tests p < 1e-4 |
| fig2e-directional-gain-small | reproduced | directional gain 0.004 against a motion gain of 0.158 (ratio 0.026, bound 0.1) |
| figs1a-motion-better-every-area | reproduced | motion models beat static in 15 of 15 cells; V1 best in all 3 subjects (rank-sum against the other four areas pooled) |
| fig3ab-identification-s1 | reproduced | 424 of 486 (464; tolerance needs at least 418); chance 2.96 |
| fig2fgh-retinotopic-receptive-fields | blocked, too_large (time) | the fits exist; the probes were not run |
| fig2j-speed-eccentricity | blocked, too_large (time) | depends on fig2fgh |
| discussion-color-no-gain | blocked, too_large (time) | the color filter bank was not computed |
| fig3c-identification-large-set | blocked, data_missing | the 1,000,000-clip set is not public |
| fig4-reconstructions | blocked, data_missing | the 18,000,000 s prior is not public |
| fig4d-reconstruction-accuracy | blocked, data_missing | the same prior |

Caveats on the reproduced claims:
- **fig2de** holds only when accuracy is scored on the repeat-averaged test signal. Scored per repeat, the three means are about half the paper's.
- **fig3ab** holds only with the four-delay model on the repeat-averaged signal. Single repeats (357) and the 4 s model (344) fall below 418.
- **The models are fit by ridge regression, not the paper's L1 regression.** An L1 fit of 26,220 regressors for about 13,000 voxels and three models did not fit in the time. This is recorded as a deviation on each claim.

### 2. Dataset, assumptions and questions
- **Version:** CRCNS keeps no versions, so the data set is pinned as `unversioned` (doi 10.6080/K00Z715X), with the MD5 sums of the files read in the notebook header.
- **What the data show:**
  - The shapes match the descriptor.
  - `rv` equals the mean of the ten repeats in `rva`.
  - V1 to V3B hold 4,183, 4,668 and 4,410 voxels in the three subjects, against the paper's "about 4,500".
  - The clock check passes: a 4 s delay predicts best (0.31 to 0.35 against 0.08 to 0.10 at 0 s), so the hemodynamic delay is still in the data.
- **Findings about the data**, which the descriptor does not mention:
  - the responses still include the first 6 s of each block, which the paper discards;
  - the test responses are on a different scale from the z-scored training responses (s.d. about 0.1 to 0.2 against 0.99);
  - 29 to 179 voxels per subject have missing values;
  - there are 30 ROI masks, most undocumented, and one voxel lies in two of the V1 to V3B masks.
- **Assumptions:**
  - Each test repeat is z-scored per voxel, following the paper's Data Preprocessing passage.
  - The Tikhonov penalty is scaled by the mean residual variance; this is a standard choice.
  - The filter bank is pymoten's pyramid, whose defaults give exactly the paper's 6,555 filters. pymoten is recorded as an input.
- **Questions for the paper's authors** (filed as `methods_unavailable` findings): how the L1 penalty was chosen, and whether accuracy and identification used the mean of the repeats or single repeats.
- **Questions to a reader:** none.

### 3. Where the protocol was unclear, wrong or missing something
1. `docs/archives.md` says CRCNS files are zips to open in place. vim-2's files are tar.gz around HDF5 files, which cannot be read at random. Random access through rapidgzip over fsspec ran at 1.1 MB/s. I streamed each member once (HTTP to gzip to tar) into memory, one large file at a time.
2. The protocol has no rule for a computation-heavy method that has to be replaced for time (L1 by ridge). I recorded it as a deviation, not as a block.
3. The penalty reading (b), the claims file's envelope variants, and the criterion's other readings could not all be run in the time. The protocol does not say how to record a reading not run for time; I wrote it in the deviations.
4. `entry.py check` requires the version string ("unversioned") to appear in the code. For CRCNS this is not documented; I added a constant to the helper.

### 4. Runtime and failures
- Two commands hung and cost about 85 min:
  - the rapidgzip test ran into its 1 h timeout;
  - a wait loop never ended because `pgrep -f` matched its own shell.
- A third run was cut off at 40 min because a three-operand `einsum` was extremely slow. I replaced it with matrix products.
- That lost time is why three claims are blocked as too_large.
- The final `all` run took 1,547 s and passed.
- Untracked files I did not create (`.bashrc`, `.idea`, `scripts`, and others) are in the repository root.
