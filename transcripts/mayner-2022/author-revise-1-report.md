I addressed every point in the round-1 report and re-ran the entry with `python tools/entry.py all`: all three notebooks pass, the check reports 0 errors, and every conclusion matches the new outputs. Nothing is committed.

## Outcome changes
- **design-sessions: partially reproduced → reproduced.** The verifier disagreed with the old outcome and was right. All 45 of the paper's sessions are in the dataset with the paper's counts. The 12 extra sessions stay recorded as a finding about the dataset, not as a failure of the claim. Measured values are now 45, 9, 15 and 9.
- **fig4-pupil-effect-size:** still blocked, but the reason changed from methods_underspecified to data_missing, as the verifier said. The diameter the Methods define can't be computed from any public file. The two computable readings disagree, which is now in the notes. The notebooks, summaries and README now give the same reason (problem 6).
- **The five L0 event claims:** still blocked as not_runnable. The verifier said "other"; I kept not_runnable because it is the protocol's reason for software that can't be installed, and recorded the difference.
- **All other outcomes are unchanged.** The fig5 numbers in the record now match the re-run (χ² 18.535, d 0.192; area χ² 16.142, AM d 0.274). The old record had values from the first author run.

## Added or corrected
- **Effect size (problem 3):** I found how the paper's code gets its effect sizes. Its pooled SD weights each group's SD by the *other* group's n − 1, because a groupby sorts "artificial" before "natural". This reproduces `effect_size.parquet` to 4e-15 in all 44 sessions. The discussion cell now tests each extreme against its tolerance. With the code's formula as a variant:
  - the discussion claim's values all fall within tolerance (0.584 to 1.194, pooled 0.343);
  - the locomotion correlation becomes r = 0.892 and 0.894.

  The outcome still rests on the formula the Methods and claims file give. This is recorded as a code_mismatch finding.
- **Sensitivity spectra:** for six of the parameter sets, the dF/F gives the paper's per-trial ND to a relative 1.1e-14 in all 2199 contrast trials with a single matching shift. Across all 108 sets, per-trial values correlate with the paper's at r = 0.993 to 0.9999.
- **Figure 7 statistics:** run on the paper's own data, the code gives the paper's χ²(4) = 32.115 and its printed z values, adjusted p values and intervals.
- **NWB contents:** a listing of one file, plus a search of all 57 files. No path names events, eye, pupil or ellipse.
- **Zenodo pupil data:** `data/eye/` holds 45 pupil area files and one parameter file, and no ellipse fit.
- **L0 detector (problem 7):** a new notebook section reads the published sources and prints why they can't be installed:
  - setup.py doesn't find its C++ sources;
  - the latest version has no `arfpop`, the function the detector calls;
  - the last version with `arfpop` is Python 2, and its C++ is missing an include that current compilers need.

  I dropped the argument about corrected fluorescence.
- **fig4 reading (b):** the deposit is now fetched over parallel byte-range requests. It arrives in about 210 s instead of hitting the 26-minute deadline, so the executed copy shows both readings. The arousal notebook now runs in 5 minutes.
- **Questions:** I added `questions/000036.yaml` with three questions for a reader: which Cohen's d formula the criteria mean, whether the ext3-2 agreement rule fits the paper (problem 1), and whether the AM d of 0.268 is a misprint (problem 2).
- **Verification record:** round 1 is under `verifications` in the attempt record, with each reason in the verifier's words and my response. I also added the detector sources as an input.

## Not done
- **Code's pupil reading for ext3-5 and ext7-1 (problem 8):** not run as a variant. The verifier says it would not decide them, and its two artifact readings already disagree.
- **Patched build of the detector:** while preparing, I made one outside the notebook (patching its C++ and its Python 2 wrapper). It is mentioned only as not run here, and no outcome or number in the record rests on it.
- **Main notebook runtime:** it now takes about 23 minutes, close to the 30-minute CI limit.
