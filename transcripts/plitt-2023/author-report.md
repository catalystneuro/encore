The attempt is recorded, checked and handed over. The analysis ran from 11:42 to 13:50 UTC (2 h 08 min). The notebook runs from a clean environment in 26.7 min. Nothing failed: `entry.py all` passes with 0 errors, and the executed outputs contain every number the conclusions quote. Nothing was committed.

## 1. Outcomes per claim

There are 57 claims: the reader's 56 plus the link claim I added.

| Outcome | Claims |
|---|---|
| reproduced (31) | link-roi-alignment; fig1f, fig1g; figs2f, figs2g, figs2i; fig2cd-decoding-no-group-difference; figs3a, figs3b, figs3c*; fig2gh, figs3eg; fig3h, fig3i; the three fig4e claims, fig4-block6-activity-increase-pattern, fig4e-novel-increase-grows-over-days, fig4d; figs6b, figs6e; figs7b; the three fig5d claims; both fig6c claims; figs8d; fig6e; figs9b |
| partially_reproduced (4) | fig2ab (7 of 8 counts; Cre-3 day 5 has 82 familiar trials, not 17); vr-reward-location-learning (licking falls rather than rises from day 1 to day 6); fig2cd-decoding-improves-over-days; fig3g |
| not_reproduced (10) | fig3f; figs8h; fig6d; figs9a (Cre mice have more HSE trials); the three fig7e and three fig7h claims (reactivated cells are less stable, not more) |
| blocked (12) | data_missing: fig1c, figs1c, figs1e, both figs1f, fig5h, fig5i, figs4, figs5. methods_underspecified: the three model claims fig3bc, fig3d, fig3e |

\* resting on an adopted reading (see 2). Every imaging outcome carries `assumed: true` because of the activity-signal assumption.

Some matches are very close: figs2f gives F(1,14)=4.89, p=0.044 (paper 4.82, 0.045), and figs2g gives p=0.309 (paper 0.308).

## 2. The dataset, assumptions and questions

**What the dataset holds and lacks**
- It holds the head-fixed VR imaging of Ctrl-1 to 9 and Cre-1 to 7 on days 1 to 6. It also holds 7 SparseKO mice that are not in the preprint.
- The freely moving behaviour, reversal days 7 and 8, Cre-8 (CA2/3), the dentate gyrus session and the morph task are not deposited.
- The deconvolved activity rates the Methods use are not deposited; the files hold dF/F, raw fluorescence and neuropil.

**Problems found in the data**
- The speed series is labelled 10 cm/s but is in cm/s: it integrates to about 288 over the 300 cm track.
- The NWB files do not say which cells are the same across days. The authors' matches are on Figshare (v5), indexed by a session order that exists only in their code. The link claim confirms them: matched cells lie 0.5 to 1.6 px apart.
- Two days are split over two files (Ctrl-2 day 4, Ctrl-4 day 2); I merged each on the ROIs matched between its files.
- 36 files are at 15.51 Hz, where the Methods say 15.46 Hz.
- The reward zone coordinates are not in the files; I estimated them from where rewards were given.
- The code linked from the dataset describes a later version of the paper and differs from the preprint's Methods in two windows.
- The clock check is consistent with a shared clock on the two days checked.

**Assumptions**
- Activity = the deposited dF/F, because the authors' code for these files uses it.
- figs3c: the code's per-bin PV correlation is adopted; the flattened reading gives a group difference (p=0.018).

**Questions for the paper's authors** (recorded as findings)
- Which activity signal and deconvolution kernel the preprint's figures used.
- How the PV correlation is defined.
- How the HSE shuffle null and the "stationary" speed are defined; I ran two readings of the null.
- Where the reward zones are, and how average running speed is taken for normalized speed.

**Questions for a reader:** none.

## 3. Where the protocol was unclear

1. The paper links no code, but the dataset links the authors' code and a Figshare record. I treated the code as support for assumptions only, and the Figshare ROI matches as a `with_labels` input.
2. Outside data may be used only when the claims file says the paper relies on it. The claims file names the custom tracking but not Figshare; I took the tracking mention as enough.
3. The author must add link claims but may not change claims. I added the link claim, and only `depends_on` and `data` on six existing claims, with a header comment saying so.
4. Reader step 3 says a claim holds under any reading the criterion names; author step 1.6 says the outcome is the one all readings give, else adopt one. I applied the any-reading rule where the criterion names readings, and step 1.6 otherwise (figs3c).
5. The absence rule ("judged on the paper's test alone") does not address readings of the measure, as opposed to the test. For figs3c I used step 1.6.
6. An absence test that finds an effect in the opposite direction (fig7h, Cre) is not_reproduced by the literal rule, though the paper's statement ("not higher") holds. I followed the rule and said so in the notes.
7. One assumption here affects about 40 claims, and the protocol can only mark it per outcome. I set `assumed` on each and stated it once in the header.
8. The clock check is written for trial tables or continuous sessions. I used split-half map reliability against time shifts, on two days only.
9. "Develop on a subset" does not fit a 22-minute shuffle reduction that every claim needs. I cached the reduced summaries outside the notebook for development; the notebook recomputes everything.
10. The notebook takes 27 min, over the 10-minute aim but under the 60-minute limit.

## 4. Runtime and failures

- Runtime is in the opening paragraph: about 2 h of analysis, a 26.7 min notebook.
- During development, metadata reads crashed on the differently structured SparseKO files and the pingouin column name had changed; I fixed both.
- The repository shows untracked dotfiles (`.bashrc`, `scripts` and others). They are sandbox device nodes, not mine, and I left them alone.

Files are in `entries/001710-plitt-2023/`:
- reproduce_plitt_2023.ipynb
- stx3.py
- entry.yaml
- README.md
- requirements.in
- requirements.lock.txt

The record is `attempts/001710-plitt-2023-01.yaml`, the claims file `claims/001710/10.1101-2023.11.20.567978.yaml` has the link claim added, and the handover is in `executed/001710-plitt-2023/handover/`.
