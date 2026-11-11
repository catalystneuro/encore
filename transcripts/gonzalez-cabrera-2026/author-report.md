Steps 1 to 6 of the Author section are done: the entry is locked, checked and run, the handover is built, and I have committed nothing. The entry's checks pass with 0 errors, and the notebook runs from a clean environment in 482 s. Only the two photometry claims could be tested; the other 39 are blocked because their data are not in the dandiset.

**(1) Outcomes per claim**

| Claim | Outcome |
|---|---|
| fig3b-photometry-continuous-only | reproduced, rests on an assumption |
| fig3c-photometry-opsin-vs-control | reproduced, rests on an assumption |
| 9 acute silicon-probe claims (fig3-optotag-counts to fig3k) | blocked, data_missing |
| 6 chronic silicon-probe claims (chronic-optotag-count to fig4f) | blocked, data_missing |
| 11 juxtacellular and tracing claims (Figure 1, Supp. Fig. 1) | blocked, data_missing |
| 5 slice claims and 8 open-field claims | blocked, data_missing |

Both photometry outcomes depend on how the paper's post hoc tests were computed:
- **Pooled reading (adopted).** The post hoc tests use the ANOVA's pooled error, which is GraphPad Prism's default; the Methods name Prism v10.
  - Fig. 3b: continuous light gives corrected p from 3.8e-06 to 2.9e-04, and the 5, 10 and 20 Hz trains are not significant. The required p < 0.0001 holds in 52 of 64 readings; the 12 that miss it use the code's −3 s baseline.
  - Fig. 3c: corrected p is 0.00074 to 0.0028 for continuous light (the paper reports 0.002), and no train frequency is significant.
- **Separate t-test per frequency.** Neither claim holds: corrected p is 0.048 to 0.11 for Fig. 3b and 0.098 to 0.19 for Fig. 3c. The continuous effect is still positive in all 5 opsin mice.

**(2) The dataset, assumptions and questions**
- **Version.** I pinned 0.261103.0758, the latest published version. The paper cites no version, and 0.260828.0749 has the same 66 files; only the metadata differs.
- **Ecephys files.** All 34 (161 GB) hold only raw voltage and ADC channels named ADC1 to ADC8. There are no sorted units, no tagging results, no event tables, and electrode locations are "unknown".
  - In each tagging recording I checked, one ADC channel carries the 210 tagging pulses, but which channel is which laser is not recorded, and neither are the rotarod direction or block.
- **Chronic subjects.** The files come from 4 subjects; the paper has 3 mice.
- **Photometry files.**
  - The session start times are often earlier than the end of the same mouse's previous file, so they are not recording starts.
  - One file (photometry-exp-5 at 5 Hz) has two stray 3-s stimulation intervals; the outcomes are the same with or without them.
  - The isosbestic fit has R² under 0.30 in 12 of 32 files.
- **Zenodo.** The record the dandiset cites holds figure-level tables, histology images and open-field videos without tracking. I did not use it.
- **Assumption:** the pooled post hoc error. The question for the paper's authors is recorded as a `methods_unavailable` finding: which post hoc error and FDR procedure they used, and which z-score baseline.
- **Questions to a reader:** none.

**(3) Where the protocol was unclear or missing something**
1. Raw ecephys with no sorted units. The protocol does not say whether that is `data_missing` (the curated units are not deposited) or `not_runnable`/`too_large` (redo the sorting). I chose `data_missing` and put a streaming estimate (about 1.4 h just to read the data) in the notes.
2. Open-field videos on a Zenodo record the paper itself does not cite. The rule for `elsewhere` assumes the paper deposited them. I kept these claims as `data_missing` and said why in the notes.
3. A test-form detail (pooled versus separate error) that flips the outcome even though the claims file names the test ("paired ... BH"). I treated it as a detail to take from the paper (step 1.6), ran both forms, and marked the outcomes `assumed`.
4. The paper's code drops every trial under the Methods' 0.9-s baseline (it needs at least 1 s). I applied that rule only with the code's own −3 s baseline.

**(4) Runtime and failures**
- The run took about 65 minutes, 17:53 to 18:58 UTC. The notebook takes about 8 minutes and peaks at 3.6 GB of memory.
- The only failures were two mistakes in my own draft notebook, both fixed before the final run.
- **Stray files.** The working tree also has files I did not create: `.bashrc`, `.profile`, `.idea` and others at the repository root, a `scripts/` folder, and an empty `.claude/` folder inside `entries/gonzalez-cabrera-2026/`. They look like they came from the harness and should not go into the commit.

Files are in `entries/gonzalez-cabrera-2026/`:
- reproduce_gonzalez_cabrera_2026.ipynb
- vtapno.py
- README.md
- entry.yaml

The attempt record is `attempts/gonzalez-cabrera-2026-01.yaml`.
