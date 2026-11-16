I finished steps 1 to 6 for the Saez and Friedlander (2016) paper on CRCNS pvc-9 and nothing is committed. The notebook ran from a clean environment in 175 s; the check passed with 0 errors and the handover package is built. The new files are `entries/saez-2016/` (notebook, `pvc9.py`, README, lock) and `attempts/saez-2016-01.yaml`.

**(1) Outcomes**

"Assumed" means the outcome depends on which baseline sweeps are used (explained under (2)).

| Claim | Outcome |
|---|---|
| dataset-size | partially reproduced |
| fig1c-control-outcomes | partially reproduced (assumed) |
| fig1-control-no-net-plasticity | reproduced (assumed) |
| fig1-control-mean-change | partially reproduced (assumed) |
| fig1-vc-ic-same | reproduced |
| fig1fh-control-no-dependence-on-initial | reproduced |
| fig1d-example-nc | reproduced (assumed) |
| fig2a-bicuculline-outcomes | partially reproduced (assumed) |
| bicuculline-increases-plastic-fraction | partially reproduced (assumed) |
| fig2-subgroup-changes | partially reproduced (assumed) |
| fig2-mean-unchanged-variance-increased | partially reproduced |
| fig2cd-example-ltp-ltd | reproduced |
| fig2f-bicuculline-no-dependence-on-initial | reproduced |
| fig3a, fig3c, fig3b | blocked, `data_missing`: the single-cell stimulation data of the paper's reference 17 are not public |

**(2) The dataset**

- **Spreadsheets:** three Excel files mark exactly the paper's included cells (14 current clamp, 14 voltage clamp, 26 bicuculline) and its discard counts (9, 11, 12).
- **Missing control recordings:** 8 of the 28 control cells are missing or incomplete, so the control claims rest on 20 cells.
  - IC22, IC23, VC21 and VC25 have no folder.
  - VC10 and VC17 have no post-pairing recording.
  - The IC11 sheet labels the pairing file as the post-pairing file.
  - IC7's listed post-pairing file has no protocol, no date and no stimulus.
- **Misplaced folder:** IC6's files are in the IC7 folder.
- **Descriptor error:** it says sweeps run every 10 s; test sweeps run every 5 s.
- **Duplicates:** the Concatenate and PRE/POST files copy the original recordings. Four of them state half the true sampling rate.
- **Stimulus timing:** in seven files the stimulus falls at 87 to 99 ms in 26 to 89% of sweeps, so it is found sweep by sweep.
- **Sheet values:** the sheets' per-cell changes give the paper's bicuculline mean and SD exactly, but not its control means. For cell VCB17 the sheet amplitude appears to include the holding current. That cell is +400% with the claims file's measure, which explains the bicuculline mean and SD being out of tolerance.

**Assumption:** where a cell has more than 120 baseline sweeps, I used the last 120. The Methods' wording supports this, and so do the sheets: their baseline means match the last 120 sweeps (median difference 3.8%), not the first 120 (23.8%). Using the first 120 changes several outcomes; it is shown as a variant in each claim.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- Which baseline sweeps form the pre-pairing epoch?
- Which post-pairing window, which t-test form (the sheets say one-tailed), which peak window, and which rule for selecting sweeps?

**Questions to a reader:** none.

**(3) Where the protocol was unclear or did not fit**

1. A gzipped tar cannot be opened in place like a zip. I streamed it once from start to end with `tarfile` in "r|gz" mode.
2. pyabf reads only from a path. The helper redirects its file access to the bytes in memory, so nothing goes to disk.
3. While developing I cached reduced per-sweep features under `$TMPDIR`, never the raw files, and deleted them afterwards. The protocol does not say whether that is allowed.
4. The protocol does not cover claims whose counts are out of 28 when 8 recordings are missing. I measured 20 cells and counted the seven missing cells whose sheet change is under 15% as no-change, with IC23 shown both ways. This is recorded as a deviation and marked assumed.
5. The claims file leaves the end of the stimulus artifact undefined. I found it per file from the data, with fixed 1 and 2 ms ends computed as variants.
6. The protocol does not say how to treat the dataset's own processed values (the sheets). I used them only for inclusion, file mapping and comparison, never to decide an outcome, except the bound in point 4.

**(4) Runtime and failures**

The notebook takes about 3 min, peak memory about 0.5 GB. Nothing failed in the final run. Early versions of the measure missed artifacts and stimuli that moved; I fixed this during development.
