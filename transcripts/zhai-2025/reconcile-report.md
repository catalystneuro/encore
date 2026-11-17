I've written the reconciliation block into `attempts/zhai-2025-02.yaml` and added the `earlier_findings.ipynb` notebook. `python tools/entry.py check entries/zhai-2025` reports 0 errors, and `entry.py all` ran both notebooks cleanly (`reproduce_zhai_2025.ipynb` in 611 s, `earlier_findings.ipynb` in 187 s). The record diff only adds lines: none of the blind attempt's outcomes, statements or notes changed. Nothing is committed.

**1. Blind: yes.** The audit found one line: the runner URL in the attempt's own provenance block. A wider search found only the notebook header saying the draft postdates 0.260527.1302, and the author's report saying it did not look for earlier attempts.

**2. Earlier findings**

| Earlier | Kind | Status | Now | Evidence |
|---|---|---|---|---|
| 1 | data_missing | partly_fixed | 11 | The oxo-M line scans are now in the draft (5 wild-type, 6 KO cells). Control and 6-OHDA patch-clamp files and open-field data are still missing. |
| 2 | selection_undocumented | partly_fixed | 4 | All 33 Sr2+ cells and 34 GRAB regions are now there. Figure 8 AIM mice are still incomplete, but the description now says so. |
| 3 | metadata_error | still_present | 13 (on_prompt) | The same 11 baseline cells (4 baseline only) are in files named for a drug. Condition and drug are now in standard columns. |
| 4 | metadata_error | fixed | | All 42 behaviour mice have consistent labels, and 18 of 18 Figure 8 mice agree with the paper's groups. |
| 5 | other | still_present | 4 | Figure 8 AIM totals still differ from the paper's; Figure 10 matches in 103 of 105 sessions. |
| 6 | metadata_error | partly_fixed | 1 | The six-trial series are now two three-trial spots of one site, still with no proximal-distal pair. The 1-, 2- and 4-trial series remain. |
| 7 | data_missing | partly_fixed | 2 | iSPN 2019-05-08 cell 3 now has a site pair (index 0.217, the paper's value). dSPN 2019-04-11 cell 1 is still incomplete. |
| 8 | metadata_insufficient | still_present | 12 | Still no spine counts. |
| 9 | metadata_error | fixed | | All 102 dendritic stimulus series peak at 2.0 nA, and all 1276 sweeps have a valid kymograph slice. |
| 10 | metadata_error | fixed | | All 333 Sr2+ sweeps have one pulse at 0.02 s and a stimulus reference. |
| 11 | metadata_error | fixed | | No GRAB object is described as a background, PMT or zero-laser image. |
| 12 | metadata_error | fixed | | All 391 files cite the published paper; no mention of the preprint or "Figure 7J". |
| 13 | identifier_missing | still_present | 6 | Subjects are still defined per recording day. |
| 14 | paper_inconsistency | still_present | 14 (on_prompt) | Oxo-M in KO gives P = 0.4697 (paper 0.910); Figure 8A gives P = 0.01198 (paper 0.0092). |
| 15 | other | still_present | 15 (on_prompt) | 18 of 123 cells miss a step and 14 repeat one, unchanged. |

**3. New findings:** 3, 5, 7, 8, 9 and 10. Findings 13, 14 and 15 are the three I added with `found: on_prompt`.

**4. Outcomes that changed**
- **`fig1i-dspn-dendritic-sch-lower`** (not_reproduced → reproduced): a difference in method. Both attempts get P = 0.066 with dSPN 2019-04-11 cell 1 included. The new attempt leaves that incomplete cell out as an assumption and gets P = 0.027, citing the draft's description.
- **`fig3f-ispn-dendritic-sul-no-change`** (not_reproduced → reproduced): a change in the dataset. The missing proximal site of iSPN 2019-05-08 cell 3 is now deposited, and P = 0.093. There is also a small method difference in the on-state group (10 cells against 9).
- **`fig2h`, `fig2i`, `fig4g`, `fig4h`** (blocked → reproduced): a change in the dataset. The draft holds all 33 Sr2+ cells, where the earlier version held one per mouse and no test could reach P < 0.05. The new outcomes rest on a stand-in event detector.
- **`fig5f-ach-6ohda-elevated`, `fig5f-ach-d2-control`, `fig5f-ach-da-suppresses`** (blocked → reproduced): a change in the dataset, from one GRAB region per mouse to all regions.
- **`fig10b-m1r-aims`** (blocked → reproduced): a change in the dataset, from 2 of the 21 Figure 10 mice to all 21.
- **`fig8bc-cdgi-aims`** is blocked in both attempts, but its reason changed from `other` to `data_missing`. The outcome is the same, so it is not listed under `outcomes`.

**5. What did not fit the protocol**
- `docs/pilot-notes.md` has no section for pilot-11 or pilot-15, so the `protocol` note covers pilot-8 to pilot-14 only.
- The claims file is still the one the earlier author wrote after seeing the data, which pilot-7 allowed and pilot-10 no longer does. The claims it blocked for having too few units have no criterion at all, so the new author tested them with the paper's default tests.
- The checkout was a shallow clone, so `git log -1 -- attempts/zhai-2025-01.yaml` returned HEAD. I ran `git fetch --deepen=200` to reach the right commit (72c9fcd).
- Earlier finding 14 is about the paper, so I checked it on the paper's tables on Zenodo, not on the dataset version.
- The empty dotfiles that now show as untracked in the repository root (`.bashrc`, `.gitconfig`, `.idea`, `scripts` and others) are `/dev/null` mounts from the sandbox. I left them alone, but they should not be committed if the workflow runs `git add -A`.
