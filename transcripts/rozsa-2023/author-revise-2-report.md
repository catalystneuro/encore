The round-2 revision is finished. The final run of `python tools/entry.py all entries/rozsa-2023` passed all three notebooks, and `tools/entry.py check` reports 0 errors. I did not commit or push.

**Outcomes**
- **No outcome changed.**
- **fig2e-sag-raf-smaller** stays partially reproduced, the one claim the verifier did not accept yet. Rerun on tested cells only (6 human and 14 rat files had no induction sweeps), the rat difference still clears P < 0.001: 0.060 (n = 95) against 0.125 (n = 20), P = 0.00039. It is weaker than before (P = 2.8e-05) and fragile: P = 0.0080 at the step nearest −90 mV and 0.0061 on drug-free files. Human gives P = 0.12.
- **Proposed changes for round 3:** the four rat claims that rest on the mixture's AP classes (fig3l, fig3k, fig3m-rat-ais-phase-coupling, fig3m-rat-ra-no-phase) keep their verified outcomes, with a change to blocked (`methods_underspecified`) under `proposed`. A new notebook cell shows why:
  - The mixture puts 0.754 of rat active-slice APs in the RA class. The paper's Figure 3M has 0.125.
  - Its two classes are 8 mV apart in threshold. In the rat induction recordings, where the protocol defines the classes, they are about 20 mV apart.
  - So by the standard used to block the human and in vivo claims, these classes are not the paper's either.

**Added or corrected**
- **New outputs:** the fig2e table for tested cells (the old all-files version kept for comparison), the class-share check above, and the Vm/LFP start-time count over all files.
  - Rat: in 24 of 39 recordings every LFP series starts with a Vm series. The text now calls the rat clock evidence weak.
  - In vivo: 135 of 245 files.
- **fig2e assumption:** the rationale now rests only on the two Methods passages. The 0.980 argument the verifier called a non sequitur is gone.
- **Every sentence quoted in section 2 of the report is fixed:**
  - the threshold ranges are now given as per-file medians, plus the RA-class medians;
  - the rat bleb slope;
  - the order-4 angle (255°);
  - the rat 100 kHz exception for fig1c;
  - the round-1 response for fig1f;
  - the run times.
- **Claims file gap:** the human and in vivo notes now say that the claims file's reading (b) has no component check, and what it would give if applied as written.
- **Record:** round 2 is under `verifications`: 30 claims agreed, fig2e not agreed, with no outcome given since the verifier gave none.
- **Questions file:** no question added. The verifier reported a gap in the claims file, not a misreading of the paper.

**Things to know**
- **Mixture numbers drift between runs.** The in vivo and induction mixtures (fitted to a 200,000-AP draw) gave slightly different counts from the verified round-2 run: 224,598 against 224,419 in vivo AIS-APs, and a human slope of 6.94 against 6.95. My last three runs agreed with each other. I did not find the cause. I updated the record to the final run, rounded those numbers in the notebook text, and noted the drift in the README; no outcome rests on these numbers.
- **Run times:** the in vivo notebook took 41.2 minutes in the final run. The README gives ranges from the runs so far.
- **Stray files:** dotfiles such as `.bashrc` and `.gitconfig`, plus `.idea`, `.vscode` and `scripts`, are untracked at the repo root. I did not create them and left them alone; the workflow's commit should not pick them up.
