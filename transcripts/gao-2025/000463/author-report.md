I did steps 1 to 5 and ran the handover (step 6). Of 37 claims, 2 could be tested, on the paper's own dandiset 000946 because 000463 holds none of the paper's data. The other 35 are blocked. The checks and the clean run both pass.

**1. Outcomes**

| claim | outcome |
|---|---|
| fig11-ac-unit-counts | not_reproduced: in the dataset's 200 µs series there are 633 AC units against the paper's 453. Per PRF it is 112, 138, 167 and 127 against 83, 107, 104 and 100, so none of the 5 counts is within 10%. |
| fig11b-ac-prf-responses | partially_reproduced, resting on an assumption: all 6 named responses hold and 300 Hz is the lowest in both windows. But 4500 Hz also responds during sonication under every test reading. |
| 31 claims on S1 or POm units by cell type (fig4 to fig10, fig11c, fig11d) | blocked, `metadata_insufficient` |
| synthesis-prf-pathway | blocked, `metadata_insufficient` (it depends on blocked claims) |
| fig5a (sham), fig5b (CG1 control), methods-insitu-pressure | blocked, `data_missing` |

**2. The data**

- **000463 (pinned 0.250829.1248, the latest; all versions hold the same files):** it cites the paper but holds none of its recordings. It has broadband recordings from one S1 probe in four rats (BH395, BH396, BH401, BH444) made in 2022–23. There are no units, no trial or stimulus times, and every electrode location is "unknown". None of these rats is in 000946.
- **Where the claims were tested:** the paper names 000946 as its deposit. I marked 34 claims `data: elsewhere` with `where:` pointing at 000946 version 0.250829.1249. I changed no statement, expected value or criterion.
- **What 000946 has:**
  - **No cell types:** every `celltype_label` is 0, although the column says 1 is RSU and 2 is FSU. 33 recordings have no such column, and no waveforms are deposited, so RSU/FSU typing cannot be redone.
  - **Duplicates:** 728 recordings are deposited twice, 2 three times and 1 four times.
  - **One mislabelled recording:** BH499_300_200_67_5_POM_S1 has the same spikes in files labelled S1 and POm.
  - **Missing sessions:** there are no sham or CG1 sessions; there are M1-targeted ones instead.
  - **Fewer animals:** 7 AC-group rats against the paper's 12, and 10 rats with POm recordings against 16.
- **Clock check:** S1 firing steps up at the trial start and falls back after about 60 ms. With onsets shifted by 1 s there is no response.
- **Assumption (fig11b):** the normalized rate is the mean count in a window over the mean count in the 67 ms before onset. The other reading, a mean of per-trial ratios, puts an unchanged window near 60% where the paper treats 100% as no change. Under that reading the claim is not reproduced; both are shown.
- **Questions for the paper's authors** are recorded as a `methods_unavailable` finding: how the rate was normalized, what "against baseline" was compared with, and the Bonferroni factor. Only the normalization changed an outcome.
- **No questions to a reader.**

**3. Where the protocol was unclear**

1. It does not say who sets `data: elsewhere` and `where:`. Both live in the claims file, which the author otherwise must not touch. I set them in the claims file, because the author steps say to give `where` and the check tool reads it from there.
2. It does not say whether `elsewhere` applies when the paper's data are in another dataset of the same archive. I applied it to 000946.
3. Fig5a, fig5b and the pressure claim have data in neither dandiset. I kept them `data: dataset` with `data_missing`, as the protocol says for data that are not public anywhere.
4. The entry's `related` field had no slot for a second dataset with a different role. I listed both dandisets as `uses_data`.

**4. Runtime and failures**

The run took about 1 h 35 min, from 09:39 to 11:12 UTC. The notebook runs in 4.1 min (251 s) from a clean environment. Survey reads in threads were very slow (18 min), so I switched to 8 processes, which brought the 000946 survey down to about 3.3 min. Nothing failed in the final run.

Files are in `entries/000463-gao-2025/`:
- reproduce_gao_2025.ipynb
- tfus.py
- README.md
- entry.yaml

The attempt record is `attempts/000463-gao-2025-01.yaml`, and the claims file change is in `claims/000463/10.1523-jneurosci.2218-24.2025.yaml`.
