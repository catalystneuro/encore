I've done steps 1 to 5 for dandiset 001933 and built the verifier's handover; the clean run passes in 162 s with 0 check errors. The Anxa1 half of the dandiset links exactly to the paper's published values, but the Calb1 dF/F is not the trace behind Supplementary Figure 8. Nothing is committed.

I used the paper's full text, which is open access (CC BY), plus its Supplementary Information, saved under `paper/`. The pinned version is 0.260825.1457: the paper cites no DANDI version (or the dandiset at all), and this is the only published version, with the same 27 assets as the draft.

### 1. Outcomes

| Claim | Outcome |
|---|---|
| `source-data-link` (with_inputs) | not reproduced: Anxa1 links exactly, Calb1 does not |
| `fig6e-anxa1-evoked-reduced` | reproduced (p = 1.2e-22; with the code's window 1.1e-20, the paper's exact value) |
| `fig6e-anxa1-evoked-per-mouse` | reproduced (7 of 8 mice, 3743 the exception, under all four test readings) |
| `supp7c-anxa1-evoked-all-powers` | reproduced (4 of 4 powers) |
| `fig6f-anxa1-spontaneous-reduced` | reproduced (1064 and 798 transients, exactly the paper's counts) |
| `fig6f-anxa1-spontaneous-per-mouse` | partially reproduced (5 of 8; 6 of 8 with the paper's actual measure) |
| `supp8c-calb1-spontaneous-not-reduced` | reproduced, but only just: p = 0.0509 against a 0.05 threshold |
| `supp8e-calb1-evoked-reduced` | reproduced |
| `supp8e-calb1-few-mice-reduced` | partially reproduced (4 mice where the paper has 2) |
| `cohens-d-anxa1-larger` | not reproduced (Anxa1 d = 2.21 is within tolerance; Calb1 d = 1.40 against the paper's 0.76) |
| 8 claims from Figures 1 to 5 | blocked, `data_missing` (the data are in BioImage Archive, PRIDE and Zenodo) |

### 2. What the dandiset holds
- **Contents:** only the photometry of Fig. 6 and Supp. Figs 7 and 8, one session per mouse. There are 15 Anxa1 and 12 Calb1 mice, matching the paper's counts after its exclusions. No recording appears twice, and the clock checks pass.
- **Anxa1 links exactly:** the paper's source data on Zenodo match the dandiset's dF/F to 1e-12. The only miss is one stimulation of mouse 4398, whose processed series ends 0.8 s after onset.
- **Calb1 does not link:** none of the 384 published Calb1 traces or 384 evoked integrals match. Recomputing dF/F from the deposited raw signal with the published code reproduces the dandiset's series, not the paper's, at any background fraction. The processing the paper used for Calb1 is neither deposited nor described.
- **Metadata errors:**
  - The epochs table describes one train type, four powers and gaps of at least 20 s. The files hold two train types, eight powers, and 51% of gaps under 20 s.
  - Two Anxa1 G2019S mice got the paper's powers as 0.33 s trains of 9 ms pulses; every other mouse got 0.51 s trains of 8 ms pulses.
  - The dF/F unit is `a.u.` for a series in percent.
  - Two trains have a pulse length of 0.
  - The archive summary lists only a behavioral approach.
  - The four excluded mice are left out without a note.
- **Code mismatches:**
  - `chunking_index.m` as written starts its window 1 s after onset; the source data show the figures used the window starting 1 s before.
  - `plot_results.m` selects power code 'h' (4 mW) for Fig. 6E, while the figure and its source data are at 0.5 mW.
  - The published spontaneous "integrals" are 0.005 times the mean dF/F over each transient, not the integral the Methods describe.
  - Methods, legend and code each name a different per-mouse test; the paper's Fig. 6F count follows the legend's one-tailed Student test.

### 3. Where the protocol was unclear or did not fit
1. **Source data with no dependent claims.** The protocol frames outside data as supplying labels or measurements that other claims need. Here the source data were used only to check the dandiset. I made one standalone `with_inputs` link claim that no other claim depends on.
2. **The source data showed the paper's spontaneous measure differs from the Methods text.** Following the rule to judge on the choice fixed beforehand, the plain integral stays the main measure and the mean is a variant. This keeps the link claim not reproduced and the Fig. 6F per-mouse claim partial; I recorded it as a deviation.
3. **Methods first, even when the source data prove the paper used the code's window.** I kept the Methods' light-on window as the main result, as the protocol requires, and showed the code's window as a variant.
4. **The protocol does not cover code that has a bug and was evidently not what was run.** I showed the literal window only as a variant and recorded it as a finding.
5. **`measured` when no reading matches the expected value.** The protocol only says what to record when readings match. For the Calb1 per-mouse claim I recorded the closest reading (4).
6. **The 10% tolerance rule does not work for p-values like 1e-20.** I used counts as expected values, p < 0.05 in the criteria, and quoted the paper's p-values in the notes.
7. **No category for "data present but not the version the paper analysed".** I tested the Calb1 claims on the dandiset's data, gave each a deviation, and recorded a `data_missing` finding instead of blocking them.
8. **The required clock contrast exposes genotype differences before the criteria are written.** I said so in the claims file's opening comment.
9. **No randomness** in this analysis, so there are no seeds to fix; the notebook says so.
10. **Figs 1 to 5 summary values are public in the source data**, but I blocked those claims as `data_missing` because the registry judges the dandiset.

### 4. Runtime and failures
- The notebook ran in 162 s in the clean environment. The whole session took about 40 minutes.
- Nothing failed in the final run. Early draft bugs (a short trace at the end of a recording, a NaN in a scale factor, a quoting error) were fixed.
- Untracked files at the repo root (`.bashrc`, `scripts` and other dotfiles) are sandbox device files I did not create. I left them alone, and the workflow should not commit them.

Files are in `entries/001933-chen-2026/`:
- reproduce_chen_2026.ipynb
- lrrk2.py
- entry.yaml
- requirements.in
- requirements.lock.txt
- README.md

Elsewhere in the repo:
- `claims/001933/10.1038-s41467-026-75194-3.yaml`
- `attempts/001933-chen-2026-01.yaml`
- the verifier's package in `executed/001933-chen-2026/handover/`
