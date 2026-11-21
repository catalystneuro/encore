The reconciliation block is written into `attempts/pelot-2020-02.yaml`. `python tools/entry.py check entries/pelot-2020` reports 0 errors, and `entry.py all` passed both notebooks: the main one in 376 s and the new `earlier_findings.ipynb` in 14 s. Nothing is committed.

## 1. Blind
The author was blind (`blind: true`). `tools/blind.sh audit` printed one line, `author.md:4178`. It is the author's own record being built, with `"id":"pelot-2020-02"` and its provenance; it says nothing about the earlier attempt.

## 2. Earlier findings (pelot-2020-01)

| # | Earlier finding | Status | Now |
|---|---|---|---|
| 1 | The deposited derivative RatVNMorphology_OutputMetrics.mat is an older output whose rat values don't match the traces | still_present | 1 (also its 2 and 3) |
| 2 | The code folder's output file keeps only 7 of the 22 rat perineurium thicknesses | still_present (checked) | 14 |
| 3 | The readme gives rat ages from 65 days; the subjects sheet says 75 | still_present | 5 |
| 4 | samples.xlsx doesn't say the subdiaphragmatic samples are anterior; R17-1 has an unexplained NerveMask | still_present (checked) | 15 |
| 5 | The code keeps FascicleIn{1}, not the largest rat fascicle | still_present | 11 |
| 6 | The Discussion's rat ratios rest on the connective tissue boundary | still_present | 9 |
| 7 | Question on the JMP settings | still_present | 10 (part 1) |
| 8 | Question on the test for no level difference in the perineurium fits | still_present | 10 (part 2) |
| 9 | Question on the age-trend test | still_present | 10 (part 3) |

I checked findings 2 and 4 directly on sparc-60 version 5 in `earlier_findings.ipynb`:
- **Finding 2:** `thkperi_um` still holds 7 values, against 22 rings in the traces.
- **Finding 4:** no row of samples.xlsx says "anterior". R17-1 has one perineurial ring but still has a NerveMask (126.9 um), and no text file mentions NerveMask.

I added both as findings 14 and 15 of pelot-2020-02, rated minor, with `found: on_prompt`. The new notebook is listed in `entry.yaml`.

## 3. New findings
Findings 2, 3, 4, 6, 7, 8, 12 and 13 of pelot-2020-02 are new. Findings 2 and 3 also support earlier finding 1.

## 4. Outcomes that differ
- **fascicles-larger-cervical:** partially_reproduced before, reproduced now. Cause: `reading`, high confidence.
  - Both attempts use the same Kenward-Roger mixed model. The earlier attempt computed it on the observed information: pig p = 0.055 (df 3.74), so two species pass. This one uses the expected information: pig p = 0.012 (df 7.6), so all three pass.
  - The earlier attempt chose the observed form because it gives the paper's nerve diameter F values. Neither form gives the paper's pig p of 0.0009, so I left `supports` out.
- **rat-carotid-sheath-bundles:** blocked before, reproduced now. Cause: `claims_changed`, high confidence.
  - The old criterion contradicted itself about whether the claim could be tested when only the vagus is traced. The rewritten criterion asks for a count by eye on the micrographs.
  - At full resolution this attempt counted 2 to 6 bundles per section; on thumbnails the most it found was 5.

## 5. What did not fit
- **No pilot notes for the change:** `docs/pilot-notes.md` has no section after pilot-14, so I couldn't read the pilot-16 to pilot-18 changes there. I took them from `tools/entry.py` instead:
  - From pilot-17, an attempt lists the paper authors' notes it used. This paper has none, so it changed nothing.
  - From pilot-18, every finding about the data needs a severity. No outcome depends on this.
- **Larger differences come from the claims file:** it was rewritten under pilot-18 for all seven datasets. This explains most of the differences between the attempts; no protocol rule does.
- **No earlier entry in git:** the repository has a single commit, so `git show $c:entries/...` shows the new entry. I used the `earlier-entry/` copy for the earlier code.
- **The earlier record lists only sparc-60 as a dataset:** it read the human and pig datasets as inputs, and sparc-65 at version 6, not the version 8 used now.
- **Untracked files I didn't create:** `scripts/` and several dotfiles at the repository root (`.bashrc`, `.vscode` and others) appeared during the run. I left them alone; check them before the workflow commits.
