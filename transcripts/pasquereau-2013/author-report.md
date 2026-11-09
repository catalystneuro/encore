I've made the second attempt on the 001636 draft (last modified 2026-10-21T20:16:41Z, version asked for). Every claim has the same outcome as in `001636-pasquereau-2013-01`. Of the 11 earlier findings, 5 are fixed, 3 are partly fixed, and 3 are still present, each now described in the dandiset where it is a data issue. `entry.py all` passes (check clean, notebook ran in 1.8 min, other runs took up to 4.5 min) and the handover is built. Nothing is verified or committed.

**Draft stability.** The archive listed 4 uploads in progress on the draft the whole time. Its modification time and asset count (439) did not change between the start and the end of this run.

**(1) Outcome per claim** (earlier outcome in brackets; all the same)

| Claim | This attempt (-01) |
|---|---|
| cell-counts | reproduced (reproduced) |
| monkey-l-perturbations | blocked: data_missing (same) |
| baseline-rate | reproduced (reproduced) |
| ptn-faster-than-csn | reproduced (reproduced) |
| antidromic-latency | partially reproduced (same) |
| false-positive-rate and the 14 claims that depend on its selection | blocked: methods_underspecified (same) |
| kinematics-slower | not reproduced (same) |
| kinematic-latency-unchanged | not reproduced (same) |
| emg-m2-larger | reproduced (same) |
| emg-duration-longer | partially reproduced (same) |
| emg-onset-unchanged | not reproduced (same) |
| emg-m1-weak | partially reproduced (same) |
| trial-correlations | blocked: methods_underspecified (same) |

Numbers that moved:
- **Cell counts:** now 115 and 157 cells (51/54 PTNs, 32/48 CSNs), still within tolerance. Before, they matched the paper exactly (112 and 159). The draft adds trials from second source files, which brings 3 more pre-MPTP units over the threshold, and drops 2 duplicate units. Counting each unit from its first file only gives exactly the paper's pre-MPTP numbers (112, 49, 31). The notebook lists every unit that differs between the two versions.
- **Session correlation of PTN latency with m2:** now p = 0.023, no longer below the paper's 0.0125 (it was 0.011). The claim stays blocked.
- **Poisson check of the false-positive rate:** I added eight more seeds. Simulated trains give 0.16 to 0.21 against the observed 0.23, so the earlier statement that about a third of the rate is unexplained is dropped.
- **Monkey V cell pre/post comparison:** 12 of 12 magnitude tests now find a difference (11 before); this claim is blocked either way.

**(2) Earlier findings**
- **Fixed:**
  - The analog streams now share the trials' clock (lag 0 ms; the torque command steps 4 to 6 ms after onset).
  - The angle's reference frame now says positive is flexion, and the monkey L series are named Wrist.
  - Repeated files and duplicate units are gone.
  - `unit_also_in_session_id` is removed; neurons recorded across two files are now one unit.
  - The dandiset description is corrected.
- **Partly fixed:**
  - Torque command sizes: the data are unchanged, but the sizes and the missing scale are now described in the files.
  - The EMG description now matches the paper; the 100 Hz monkey L sampling and the A/D units remain but are stated.
- **Still present:**
  - Monkey L has no perturbation times (now documented).
  - Torque onset comes about 1.7 s after the center target (now documented).
  - No analysis code, and a false-positive rate of 0.23.
  - The paper's own inconsistency.

**(3) New findings**
- Three sessions (v1401, v1402, v1501) have labelled perturbations but no pulse in the torque command. The files' torque description says so.
- The code that built the draft is in an open pull request of turner-lab-to-nwb (#33, branch `fix_errors`, 5f9bf63). The main branch the dandiset links does not hold it.

**(4) Where the protocol did not fit a repeat attempt**
- `entry.py check` fails on the `-01` record as soon as `entry.yaml` points at the new version, and passes only once the `-02` record exists. So check cannot be run before the record is written.
- The schema has no field for whether an earlier finding is fixed. Following `001754-knierim-2000-02`, I put the status of every earlier finding in the record's header comment and restated those still present or partly fixed as findings.
- The protocol records a draft's modification time but says nothing about uploads in progress or checking the draft again at the end.
- The claims file's comment says "no unit appears in two files". Merged sessions make that untrue, and units now span source files. I applied the criterion per unit within its own trials and showed the first-file reading as a variant. I did not raise a question because both readings give the same outcome.
- Step 1.3 asks to show how versions differ. That required loading the units of the earlier version as well, which adds streaming time to every run.

Changes are in `entries/001636-pasquereau-2013/` (`stretch.py`, the notebook, `entry.yaml`, `README.md`) and the new `attempts/001636-pasquereau-2013-02.yaml`; the handover is in `executed/001636-pasquereau-2013/handover/`.
