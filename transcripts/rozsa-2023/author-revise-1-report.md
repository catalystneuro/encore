I've finished the round-1 revision. The entry passes `python tools/entry.py all` (all three notebooks), the outputs matched the previous run exactly, and `check` shows 0 errors. Nothing is committed.

**Outcome changes**
- **fig2e-sag-raf-smaller**: not_reproduced → partially_reproduced (assumed). The verifier asked for the continuous-recording RAF reading. Under it, rat cells with RAF have lower sag at P = 2.8e-05; human cells don't (P = 0.10). The assumption is that RAF status should come from continuous-recording RA-APs. Counting the APs between induction pulses would give RAF to 98% of cells, against the paper's 23%.
- **fig3-human-ap-states and fig3f**: partially_reproduced → blocked (methods_underspecified). I refitted the mixture on clean data and checked it, as the verifier asked. Its "RA" component still has the steeper slope (3.54 vs 2.18 mV/ms), which is the opposite of how the paper describes RA-APs. The numbers under those classes are still in the notes.
- **figs3-no-modulators**: partially_reproduced → blocked (data_missing), as the verifier gave it.
- **The 8 in vivo claims**: blocked too_large → blocked methods_underspecified. The verifier was right that the size didn't justify the block: a new third notebook reads all 383 GB in 41 minutes. But the in vivo mixture has the same flaw, an RA component with the steeper slope (3.24 vs 1.99 mV/ms), so I blocked these claims for that reason and kept the numbers in the notes.
- **figs5**: still blocked, now metadata_insufficient. The genotype is in the files but no field records the anesthesia condition.
- All other outcomes stay as they were. They were re-checked with every verifier point applied.

**What I added or corrected**
- **Threshold detection:** it now uses a 50 µs smoothed dV/dt. A synthetic test in the data check gives the right threshold at every sampling rate from 5 to 200 kHz. fig1c holds within each sampling rate.
- **Data cleaning:** artefact APs are removed before any analysis. RA-APs must now have no positive current in absolute terms, holding current included.
- **Baselines and subsets:** each induction file now has its holding current and spontaneous firing before induction printed. Every induction result is also shown on drug-free files and on cells that are quiet before induction.
- **Mixture checks:** the mixture's component means, SDs and weights are printed, with scatter plots and its range over five seeds. The induction mixture shifts with the seed (86,085 to 2,453,230 APs), so no outcome rests on it.
- **Missing readings now run:** fig2c with one epoch per induction run, and without the 20 µM file; fig2h with the bleb trace during a somatic step, without implausible sweeps, and with the duplicated rat soma counted once.
- **fig2h caveat:** the bleb-higher result vanishes without step sweeps that go below -150 mV (P = 0.28). The notes now say the outcome rests on those sweeps.
- **Bleb checks:** paired soma and bleb sweeps start at the same time in every file. I added example traces, and a split by latency sign that shows the paper's pattern but isn't one of the criterion's readings. Somatic thresholds of -30 to -11 mV and an implied 26 to 57 MΩ of uncompensated resistance are now recorded as a finding.
- **Clock and metadata:** the Vm and LFP starting times are printed side by side, with an AP-triggered LFP average. A metadata dump of one file per folder, in vivo included, is in the data check.
- **Other fixes:**
  - Non-normal paired data now get the Mann-Whitney U test, as the paper's rule says.
  - A bug in how the LFP was decimated was fixed.
  - Notebooks now read files in parallel worker processes, which cut the induction notebook from 69 to 24 minutes and peak memory to about 1.5 GB.
- **New findings:** 18 session IDs appear in both an induction folder and an active-slice folder (possible double deposits); the bridge and threshold problems in the bleb recordings; and the in vivo metadata gaps.
- **Record:** the verification round is recorded for all 31 claims, quoting the verifier's reasons, with my responses.

**Not done**
- I added nothing to `questions/rozsa-2023.yaml`: the report doesn't say the claims file misreads the paper anywhere.
- `runtime_minutes` in `entry.yaml` (8, 27, 41) are slightly above the final run's 7, 24 and 40. I left them, because editing the entry would have invalidated the run stamp.
