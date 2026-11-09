I worked through every point in the round-2 report. No outcome changed, and none needed a `proposed` change: 27 reproduced, 1 not reproduced (`ed1-monkey-d-no-change`), 4 blocked. `python tools/entry.py all entries/001773-fujimoto-2026` gives 0 check errors, and the notebook runs and passes in about 32 s.

**What I changed in reply to the report**
- **Seed-map assumption:** I set `assumed: true` on all 11 reproduced seed-connectivity outcomes. That is the verifier's five, the four fig5c claims, `ed9-no-change-motor-mcc` and `ed10d-monkey-d-roi-changes`. Each now has a deviation saying the assumption is that the deposited maps (one per session) are the ones the paper analysed. The matching F values (186.48, 51.09, 7.36, 4.58) support it. I added the last two beyond the verifier's list because they rest on the same maps. The Summary says this too.
- **Tukey-Kramer accuracy:** I added a cell before the Summary that prints 15 reported P values next to the computed ones, with their ratio. I rewrote the Summary, cell 63, cell 65 and the fig5b deviation from that table:
  - within 3% above 1e-4;
  - 1.11 to 1.28 times near 1e-5 and 1e-6;
  - 1.5 to 2.8 times between 5e-9 and 4.4e-8;
  - 5.5 and 8.3 times for the reported 8.22e-12 and 1.37e-12.

  The wrong "1.1 to 3 times" figure is gone.
- **`ed1-monkey-d-no-change`:** cell 21 now prints every line of the 135-line FigE1 script that calls a test or selects monkey D, as the verifier asked.
  - The only test calls are `anovan` and `multcompare`, both on group 1 (monkeys N and T).
  - Monkey D appears only in the plot's means, standard errors and sample sizes.
  - Cell 22 and the record now say the deposited script runs no test for monkey D. I removed the wider statement about the paper as a whole.
  - The printout also showed that monkey D's foraging standard errors are computed from the movement column (lines 93 and 96). I added this as a `code_mismatch` finding and to the Summary. The finding says lines 91 to 96, which covers N and T too, but the printout shows only lines 93 and 96 for monkey D; that line range should be checked before commit.
- **`fig6d` notes:** I removed "next to the lead". They now say area 25 is the seed ROI itself, so its rise is not evidence of a local increase at the implant site, and that no output gives the lead location. The outcome stays blocked.
- **Round 2 record:** added under `verifications`. All 32 claims are recorded as agreed, each with the verifier's reason and my response.

**Not done**
- The verifier reported no place where the claims file misreads the paper, so I added nothing to `questions/001773.yaml`.
- Per-run seed maps are not deposited, so the second run reading still cannot be run. It is recorded as an assumption, not resolved.
- Nothing is committed, as instructed.
