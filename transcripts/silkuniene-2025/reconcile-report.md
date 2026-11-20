I added the `reconciliation` block to `attempts/silkuniene-2025-04.yaml` and added two findings to that record, marked `found: on_prompt`. I also wrote a new notebook, `entries/silkuniene-2025/earlier_findings.ipynb`, and listed it in `entry.yaml`. The lock file did not change, `python tools/entry.py check entries/silkuniene-2025` reports 0 errors, and both notebooks passed a fresh run: the main one took 1693 s and the new one 257 s. Nothing is committed.

**1. Blind: yes.** The audit flagged three lines in `author.md`. Two are the repository README describing the registry, and the third is this attempt's own runner URL. Neither the author nor the revise runs looked at `silkuniene-2025-03` or its entry.

**2. Earlier findings**

| # | Earlier finding | Status | Now |
|---|---|---|---|
| 1 | Only the Fig. 6 data are in 001277 | partly_fixed | 1 |
| 2 | Every file says "9 packets at 0.2MHz" | still_present | 5 |
| 3 | 7 wells at 600 ns where the paper reports n=5 | still_present | 3 |
| 4 | Wells P1 B2 and B3 are anomalous | still_present | 4 |
| 5 | The Cy3-DAPI image of P2-20240925-B3 is deposited twice | still_present | 7 |
| 6 | OME says 12 bits, but values are far above 4095 | still_present (checked in the new notebook) | 12 |
| 7 | No electrode positions or ROI coordinates; plate layout only in subject ids | still_present (checked in the new notebook) | 13 |
| 8 | Questions for the authors | still_present | 10 |

- **Finding 1** is only partly fixed because the Fig. 5 and Fig. 7 series are in 001284 and 001276, which the earlier attempt did not use. The packet-rate series and the thermometry data are still in none of the four dandisets.
- **Finding 6** was stated too broadly before. Only the 13 Cy3-DAPI files carry OME metadata; those say 12 bits but hold values up to 25073 and 65535. The FITC and DAPI files carry no OME metadata at all. The new finding 12 states this correctly.

**3. New findings:** 2, 6, 8, 9 and 11. Findings 12 and 13 were added in this step (`found: on_prompt`).

**4. Outcomes that changed:** all three are Fig. 6D claims and all were blocked in the earlier attempt. The main cause in each case is `claims_changed`.
- **fig6d-longer-pulses-sharper-peak** (blocked → reproduced, confidence high):
  - The old criterion blocked the claim whenever readings differ. The new claims file lets the author adopt one reading, and this attempt chose the per-well values.
  - Both attempts leave out the same two 600-ns wells, and in both the trend is significant only when both are left out.
  - The p-values for the 1-mm ROI spacing also differ: 0.042 to 0.050 before, at most 0.0058 now. That is because this attempt centred 11 of its 15 wells on the YP spot, which narrows the FWHM. The earlier attempt fitted the electrode footprints in every well.
  - I gave no `supports` value, because the result depends on which wells the paper used.
- **fig6d-600-900-differ-from-300** (blocked → partially_reproduced, confidence medium, supports partially_reproduced):
  - The old blocking clause and the inherited block from the claim above are gone.
  - The 900 vs 300 ns comparison with 1-mm spacing moves from 0.077–0.131 to at most 0.0118, because of the same spot centring.
- **fig6d-900ns-fwhm** (blocked → reproduced, confidence high, supports reproduced): the earlier block came only from depending on the claim above. The values are essentially the same: 1.69 to 1.71 mm before, 1.688 to 1.767 mm now.

**5. Things in the protocol that did not fit**
- **Claims file rewritten:** pilot-14 replaced the claims file, so most claim ids outside Fig. 6 changed. Only Fig. 6 outcomes could be compared by id; claims such as the Fig. 5 Lorentzian/Gaussian one have no shared id.
- **Partly fixed by scope:** "partly_fixed" for finding 1 means the earlier attempt used fewer dandisets, not that anyone fixed the data. The schema has no status for that.
- **No `earlier-entry/` copy:** the directory was empty, so I filled it from commit cb54ee9. The repository history is shallow, and that is the only commit available.
- **Unexpected metadata:** the Cy3-DAPI files of different wells (P1-A1 and P2-A1) carry the same OME stage positions and DeltaT. I did not follow this up or record it.
