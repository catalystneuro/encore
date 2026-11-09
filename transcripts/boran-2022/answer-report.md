There was one question, and I changed the claims file to answer it.

**neurons-recorded: changed.** The paper never says how a neuron is assigned to a region. Methods 2.5 says the neurons were grouped "according to their anatomical region". The Figure 1d legend shows the microwire tip locations colour-coded by region. The Table 1 legend only spells out the electrode abbreviations (AH, PH, EC, A). The claim's criterion had chosen the electrode-name rule without citing anything for it.

- **New criterion:** it now gives two readings and passes the claim if all values fall within tolerance under either one:
  - (a) by where the microwire tips sit anatomically, as Figure 1d shows them;
  - (b) by electrode name.
- **Other per-region claims:** fig2c, fig2d, fig3b and fig4d use whichever reading this claim is judged under.
- **Header:** the list of details the paper leaves open now includes the region assignment.
- **Expected values:** unchanged (809 neurons in total; 454 hippocampus, 209 entorhinal cortex, 146 amygdala).

The question has `answered: 2026-10-30`. `tools/claims_check.py` reports 0 problems. Nothing was committed or pushed. Several untracked files are in the repo root (dotfiles such as `.bashrc`, plus `.idea`, `.vscode` and `scripts/`). They aren't part of this change and I left them alone.
