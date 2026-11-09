The entry for CRCNS bf-1 is written, locked and run, and the attempt record and verifier handover are in place. Of the 28 claims, 10 were tested and 18 are blocked; `entry.py check` and `all` pass with 0 errors, and nothing was committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig3a-bf-gamma-reduction | partially reproduced: gamma falls 48% in the arena (paper 35 ± 3), paired t p = 0.012 over 6 rats; every reading gives 46.8–48.1% |
| fig3a-each-hemisphere-significant | reproduced: all 12 arena recordings p < 1e-7 |
| fig3b-arena-gamma-unrelated-to-movement | reproduced: one-way p = 1.0 |
| fig3b-home-cage-gamma-increases-with-movement | not reproduced: the claims file's test gives p = 0.82. Gamma does rise in all 6 rats; a repeated-measures ANOVA gives p = 2e-5 |
| fig3b-matched-movement | not reproduced: one-way p = 0.070; a paired test of the same values gives p = 0.007 |
| fig3c-home-cage-above-both-sessions | not reproduced: arena session 2 is 15.9% *below* session 1 (paper +5.62%), p = 0.020. Rests on an assumption (below) |
| fig3d-gamma-rises-with-time-in-arena | partially reproduced: r = 0.86 in 1-min bins (paper 0.72); 0.13 and 0.045 under the other readings |
| figs2-bf-low-frequency-bands | reproduced under all 12 readings |
| figs3-unimodal-states | reproduced: smallest dip-test p = 0.102 |
| figs5-arena-excursions | partially reproduced: the gamma and theta tests hold, but there are 10–14 excursions per 20 min averaging 5 s, against the paper's 8 lasting 8–44 s |
| bipolar-gamma-reduction, fig3c-consistent-over-days | blocked, metadata_insufficient |
| fig3d-rapid-switch-to-home-cage, plus 15 behaviour, object, unit, ACC and VC claims | blocked, data_missing |

## 2. Dataset, assumptions and questions

**Findings about the data:**
- Rat 3's home-cage session 2 is a second copy of 287 segments of its session 1, shifted 100 s, with the same LFP and movement values. I counted it once.
- Each file has its own clock starting at 0, and there are no day labels.
- 2.6–23.5% of segments were removed, where the paper's supplement reports rejecting 1–4%. The paper's own rule, applied again, drops another 16.8%.
- The LFP unit is not stated, and the movement values in rats 4 and 5 are on a different scale from the other rats.
- The data description says `Hcage` where the files say `HCage`, and calls the archive a file of .mat files without saying it is a gzipped tar.
- One file has a strong 50 Hz line inside the gamma band.
- The movement values may lead the LFP by up to one 2-s segment.
- The dataset holds only the basal forebrain LFP of six rats.

**Assumption:** fig3c treats the dataset's session numbers 1 and 2 as the paper's first and second daily arena sessions. It is marked `assumed: true`.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- What were the observations in the movement-quartile ANOVAs, and was gamma normalized per animal?
- How was the 35% reduction computed?
- Are sessions 1 and 2 the same day's two arena trials?
- For the excursions, what power scale gives the 2.6 threshold, how were histogram bins set, and was there a minimum excursion length?
- What was correlated with time in Fig. 3D?

**Questions to a reader:** none.

**Version:** CRCNS datasets are unversioned, so I recorded `unversioned` and pinned the single copy in `live/` by the MD5 from `checksums.md5`. The notebook checks the streamed archive against it.

## 3. Protocol points

1. The guidance on reading CRCNS data (docs/archives.md) assumes zip files, but bf-1 is a `.tar.gz`. I streamed it with fsspec and `tarfile` in stream mode, loaded every member into memory, and checked the archive's MD5 during the stream.
2. Protocol step 2's clock check names no method for data with no trial table. Theta power gave a weak relation, so I used 100–200 Hz LFP power (movement artefact) against the movement values at shifts of −5 to +5 segments. In 23 of 24 files the peak is at 0 or +1. Files can't be checked against each other because they share no clock.
3. The protocol has no rule for when a criterion names no partial outcome but the effect holds while its size does not (fig3d). I used `partially_reproduced` from the general definition and said so in the notes.
4. Several criteria fix a one-way ANOVA on per-rat means, which large between-rat differences make insensitive. The protocol binds me to the criterion, so I recorded `not_reproduced`, showed the repeated-measures and paired variants, and asked the authors. It is not a misreading of the paper, so no reader question.
5. A duplicated recording also breaks session pairing. I dropped the affected pair (11 pairs) and showed the 12-pair version as a variant.
6. I briefly opened another attempt's `entry.yaml` (crcns-hc-9) to check the `related` id format for CRCNS, against the instruction not to read other attempts. It affected nothing else.

## 4. Runtime and failures

The notebook runs in about 14 s; streaming the 22 MB archive takes about 3 s. Nothing failed apart from a string-formatting error I fixed during development. The untracked dotfiles and `scripts`/`.idea` entries in the repo root are sandbox device mounts, not mine.
