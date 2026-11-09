I finished steps 1 to 6: the entry passes `tools/entry.py all` and `check` with no errors, and the handover is built. The run took 1 h 20 min (14:30 to 15:50 UTC). Only one version of the dandiset is published, 0.260825.0222, so I pinned it; the paper cites none.

**1. Outcome per claim**

| Claim | Data | Outcome |
|---|---|---|
| psc-file-labels-link (link claim I added) | dataset plus the code's file table | partially reproduced |
| fig5b sEPSC frequency | with labels | blocked, methods_underspecified: at 5 pA VEN is lower (p = 0.029); at the RMS-noise threshold VEN is higher |
| fig5b sIPSC frequency | with labels | not reproduced |
| fig5b mEPSC frequency | with labels | not reproduced (depends on the mEPSC label conflict below) |
| fig5b mIPSC frequency | with labels | blocked, methods_underspecified: at 5 pA p = 0.0074; at RMS noise p = 0.24 |
| fig5c amplitudes (sEPSC, sIPSC, mEPSC, mIPSC) | with labels | reproduced (p = 0.23, 0.082, 0.61, 0.46) |
| ven-map-et-ct, fig3e, fig4j-amplitude, fig4d (DANDI:001750), ven-subtypes-similar-physiology (DANDI:001746) | elsewhere | reproduced |
| patchseq-mapping | elsewhere | reproduced, resting on an assumption |
| fig5-connectivity-total, fig5-connectivity-by-type, fig8a, fig8de | elsewhere | partially reproduced |
| fig2d-f (DANDI:001746) | elsewhere | not reproduced |
| scrna ×3, fig6f-g, fig6h, fig7c | elsewhere | blocked: too_large (two of the scRNA claims) or methods_underspecified (the third); the scRNA data are a 23 GB tar.gz, beyond this runner's 15 GB of memory |
| model ×3 | elsewhere | blocked, not_runnable: the hoc scripts are not in the repository |
| fig3c, fig4j-latency, fig6 morphology | elsewhere | blocked, metadata_insufficient |
| fig4ac | elsewhere | blocked, other: those recordings are in no named deposit |
| ven-firing-rate-variability | elsewhere | blocked, methods_underspecified |

**2. Dataset**

- **Findings:**
  - The NWB files have no cell type. Labels come only from the code's `metadata_PSC.csv`.
  - That table gives one sIPSC file to two cells (a PC and a VEN) and names no row for file `fwphyw`.
  - Its mEPSC labels are the opposite of the code's own analysis sheet for all 15 cells.
  - The dandiset holds 15 mEPSC recordings where the paper reports 16.
  - The sIPSC files are held at +20 mV with outward currents, where the Methods say −60 mV.
  - 22 mIPSC files end in zero padding.
  - 44 of 84 recordings are shorter than the 5 min minimum in the Methods.
  - There are no duplicate recordings.
  - My detector, using the paper's 5 pA threshold, finds 4.6 to 15 times the code's event counts in the noisier sEPSC and sIPSC recordings. So the sIPSC "not reproduced" may be a failure of this attempt.
- **Assumption:** for patchseq-mapping, the inhibitory neurons are the 33 cells the code labels as interneurons.
- **Questions for the paper's authors:**
  - Which miniAnalysis settings were used, and which stretch of each recording was analysed?
  - Which rows and cluster numbering are the inhibitory Patch-seq neurons?
- **Questions to a reader:** none.

**3. Protocol points**

1. The claims' criteria say to block when the two threshold readings disagree, while step 1.6 allows adopting the best-supported reading. I followed the criteria and noted in each claim that 5 pA is the value the paper prints.
2. The claims say "the dataset's labels", but the dataset has none. I set `data: with_labels` and `depends_on` the link claim on the 8 Fig. 5 claims. The protocol does not say whether an author may change those fields.
3. The clock check assumes trial tables, which these recordings lack. I checked the time base instead with event decay times and the code's per-cell counts.
4. archives.md says to stream with remfile, which was about 100 times slower for DANDI:001746. I read each file whole into memory, never to disk.
5. My first too_large estimates used remfile's 4.4 MB/s; bulk reads ran at about 300 MB/s. The protocol should say to time the read method itself.
6. It is unclear whether code tables count as the "elsewhere" data. Data missing from the named deposit cannot be blocked as data_missing for an elsewhere claim, so I used `other`.
7. The supplement PDFs are now under `paper/`, but the claims file was written without them. I kept the criteria that block "unless supplied".
8. A link criterion that checks per-cell agreement also tests my detector, not only which file is which.

**4. Runtime and failures**

The main notebook runs in about 65 s and the second in about 215 s. Nothing failed.

Files are in `entries/001752-liu-2026/`:
- reproduce_liu_2026.ipynb
- elsewhere_liu_2026.ipynb
- psc.py
- aic_tables.py

The attempt record is `attempts/001752-liu-2026-01.yaml`, and the claims file has the added link claim.
