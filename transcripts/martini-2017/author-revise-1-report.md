I've worked through the round-1 report. None of the 18 outcomes changed, and the entry re-ran cleanly with `python tools/entry.py all entries/martini-2017` (passed, 31 min). The two full runs printed identical numbers, and the conclusions match them.

**What I added or corrected (verifier problem numbers):**
- **ROI set (1):**
  - The data check now shows the ROIs on the mean images of all 49 fields.
  - I added a "Sensitivity" section that re-runs the main reading of every tested claim four ways: a strict set of the 1054 strongest ROIs, the literal halo formula, both together, and without the five fields that fail the clock check.
  - The strict set's threshold is chosen to hit the paper's count, so it is not a test of dataset-size.
  - The only change across a bound: responsive-fraction reading (a) reaches 45.5%, just inside its tolerance, when the five clock-check fields are left out. I kept not_reproduced because the claim covers all 49 fields, and the notes say how fragile it is.
- **Per-mouse tuning (2):** The notebook now prints tuned counts for exp8 to exp10 next to the paper's: 22/349, 25/219 and 16/238 here against 59/167, 39/102 and 47/117. The fig2de notes say the pooled match does not hold mouse by mouse. The outcome stays reproduced because the criterion is pooled.
- **Halo formula (3):** The literal reading, (F − bg) − 0.7·H, now runs as a reading for fig3c, neuropil, fig3e and the beyond-200 µm test. It gives 0.2193 against 0.1099 shuffled for fig3c, so those outcomes stay the same.
- **Neuropil (4):** Added the dF/F0 reading. Neuropil is 0.55 against 0.11 for neurons, higher in 49/49 fields and still far above 0.179.
- **Histology (5):**
  - I rendered the three PDFs at full resolution around the imaged area.
  - exp8 does place five of its six fields, with neurons drawn as coloured dots, and has barrel outlines.
  - exp9 shows neurons with no field labels, and exp10 only a dashed square.
  - fig4c and fig4d stay blocked because the criterion pools all three mice. The notes, the finding and the notebook section are corrected, and the per-mouse counts (which fail) are recorded.
- **P1 count and the phase-0 file (8):**
  - The onsets run from 1.96 to 90.01 s in 95 s files, and the command never moves more than 9.8 mV from rest outside the deflections found. So the 90th presentation was never given; the parser did not miss it.
  - The phase-0 file (exp10/exp3_0004) starts with the command 13 mV from rest for 39 s. The parser counts this as a deflection, but it has no response window and enters no analysis. I added this to the findings.
- **SI zeros (10):** 3 of 35 fields have SI of zero for every pair, so the Wilcoxon test's effective n is 32. Counting them with zsplit or pratt gives p = 0.623.
- **Points 9 and 11** are now stated in the data-check text and the tuning-consistency conclusion.
- **Record:** Round 1 is under `verifications`, with the verifier's reasons and my response for each claim. Notes and deviations are updated and `entry.yaml` now gives the run time as 31 min. `entry.py check` reports 0 errors.

**Not done, and why:**
- **Matching the example neuron and field (6):** I did not attempt the matches for fig2ab and fig3b. Figure 2C and the Figure 3F inset draw about ten masks as circles on a plain grey background, with no image of the field. Matching ten circle centres against ROIs that are not the paper's could not identify a field, and the notes now say so. These claims stay blocked.
- **Barrel-map test for exp8 alone:** not attempted, because the criterion needs all three mice.
- **Questions for a reader:** none added. The report did not say the claims file misreads the paper.

Several untracked files appeared at the repo root during the run (`.bashrc`, `.profile`, `.gitconfig`, `.zshrc`, `.idea`, `.vscode`, `scripts`, and others). I didn't create them, so I left them alone; they should be kept out of the commit. Nothing was committed.
