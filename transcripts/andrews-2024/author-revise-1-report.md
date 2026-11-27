The round-1 revision is finished. The entry re-ran cleanly with `python tools/entry.py all entries/andrews-2024` (passed, 30.2 min, 1.8 GB peak memory), `check` reports 0 errors, and nothing is committed.

**Outcomes:** none changed. `table1-cohort` stays partially reproduced and the other 28 claims stay blocked. Round 1 is recorded under `verifications` in `attempts/andrews-2024-01.yaml`: for each claim, the verifier's outcome, its reason and my response. The verifier agreed with every outcome. On `simulation-dampening` it would use the reason code `other`. I kept `not_runnable`, because docs/protocol.md lists it for a `data: elsewhere` claim whose software cannot be installed, and recorded the disagreement.

**Added or corrected, by the verifier's points:**
- **Opsin and condition fields (1):** the helper now reads every object under `general/` in all 69 files, and a new data-check cell prints them. There is no `virus`, `pharmacology`, `protocol`, `notes`, `optogenetics`, `stimulus` or genotype field, and no opsin, drug or medium word anywhere. `experiment_description` is just the paper's title. So the cohort stays partial and "conditions not labelled" still holds. I added a finding for the empty fields.
- **Simulation (2):** the notebook now shows the attempt. It prints the published environment file (NEST 3.4 from conda-forge, NESTML 5) and the PyPI releases (no NEST 3.4). It then installs NEST 3.10.0 with NESTML 5.3.0 in a throwaway environment and runs the script's first step, which fails with `nest.ll_api has no attribute sli_func`. I added the paper's repository at commit 6865bf6 under `inputs`.
- **Other channel groups and split steps (3, 4):** I read every channel group of the 47 files of 3C, 4C, 5C, 7D, 8D, 10F and 11G (132 GB, 14 min), and also counted steps between bins 20 ms apart. This changes what the record said: the light events are not limited to 3C.
  - 4C-1 has six 10 s light periods and 4C-3 has one.
  - 7D-0, 7D-2, 7D-5 and 7D-7 also show 10 s light periods.
  - These steps are 40 to 88 counts, sit on part of the array only, and are often split across two bins.
  - No channel group of any 5C, 8D, 10F or 11G file shows a light step.

  The notes for nine claims, the light-events finding, the README and the notebook text are corrected. No outcome changes, because the sorted units are still missing.
- **Light-response variant (5, 6):** the comparison now also runs with the first second of each window left out. Crossings still fall 89 to 93% in 3C-1 to 3C-5; 3C-6 falls 18% (p 0.77) and 3C-7 rises 17% (p 0.06). The per-second table of 3C-7 no longer counts the seconds that hold an onset or offset as light-on.
- **Header (7) and Table 1 check (8):** the header now says `transduction-not-explaining-response` is blocked through the two Table 2 claims, not histology. The cohort cell now checks slices, patients, ages and sexes against Table 1 in code, and all match.
- **Read retries:** S3 timed out once during a full run, so chunk reads are now retried up to five times. The cell's install subprocess had also failed under Jupyter's matplotlib backend setting; that is fixed.

**Not done:**
- No question for a reader: the verifier did not report a place where the claims file misreads the paper.
- I did not adopt the routes through the authors' per-unit CSVs and saved waveforms in their GitHub repository. The claims file does not use them, and they would test the authors' derived data, not the deposit.
- I did not map 3C-6 and 3C-7 to the code's recording index, or compare the 3C step sizes with the sweep order of Extended Data Fig. 7. Neither can change an outcome, since the units are missing.
- 9E and 12G were read on their first channel group only. The notes say so.
- The NESTML 9 port of the model was tried while preparing and did not build. It is described in the notes but not run in the notebook.
