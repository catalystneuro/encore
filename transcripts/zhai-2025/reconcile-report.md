The reconciliation block is written into `attempts/zhai-2025-03.yaml`, and `python tools/entry.py check entries/zhai-2025` passes with 0 errors. I checked six earlier findings in a new notebook, `entries/zhai-2025/earlier_findings.ipynb`, which is listed in `entry.yaml`. The lock file came out unchanged. In the full entry run, `reproduce_zhai_2025.ipynb` passed in 439 s and `earlier_findings.ipynb` in 31 s. Nothing is committed.

**1. Blind: yes.** The audit printed five lines, and none points at an earlier attempt's results. Three are links to the protocol and README, and one is this attempt's own runner URL. The fifth, from the author's report, flags the claims file's opening comment about an earlier data check (it names `lid.py` and a `condition_subfolder` column). The claims file is the one earlier item the author is allowed to keep. The author also noticed that the dandiset's own description gives the "90 of 123 cells" figure. That is the data owner's text, not an attempt record.

**2. Earlier findings (zhai-2025-02)**

| # | Earlier finding | Status | Now |
|---|---|---|---|
| 1 | Two dendritic cells imaged at one site only | fixed (both cells now have a Proximal1/Distal1 pair) | – |
| 2 | 2019-04-11 cell 1 missing its first site pair | still_present | 3 |
| 3 | Somatic spike counts of 33 cells don't match the paper's table | still_present | 4 |
| 4 | Figure 8 AIM sheets differ from the paper | still_present | 2 |
| 5 | Mouse 7830 sessions 4 and 5 identical | still_present (checked) | 9 |
| 6 | Subjects defined per recording day; mouse counts short | still_present (checked) | 10 |
| 7 | GRAB-ACh3.0: no identifier, missing trials | still_present | 6 |
| 8 | Two Sr2+-oEPSC cells with extra sweeps | still_present | 5 |
| 9 | Paper's "average" Sr2+ amplitude is the median | still_present (checked) | 11 |
| 10 | TaroTools settings not given | still_present | 7 |
| 11 | Control/6-OHDA recordings, rotations, open field not deposited | still_present | 1 |
| 12 | Spine counting cannot be repeated | still_present | 8 |
| 13 | Drug-named session files hold baseline cells | still_present (checked) | 12 |
| 14 | Two P values in the paper don't recompute | still_present (checked) | 13 |
| 15 | Missing and repeated current steps | still_present | 4 |

On finding 7, the earlier attempt said 2024-04-02 Slice1Roi2 has no acetylcholine trial, while zhai-2025-03 finds two (4.4 s and 1.2 s long). This may be an artefact of the earlier code, not a change in the files: its helper gives no Fmax when any acetylcholine trial of a region is shorter than 2 s.

Findings 9 to 13 of zhai-2025-03 are the ones added with `found: on_prompt`. Each points at its cell in `earlier_findings.ipynb`.

**3. New findings of zhai-2025-03:** none. Each of its findings 1 to 8 matches an earlier one.

**4. Outcomes that changed**
- **`fig1i-dspn-dendritic-sch-lower`** (reproduced before, not_reproduced now). Cause `data_used`, high confidence. Both attempts get the same numbers: P = 0.066 with 2019-04-11 cell 1 and 0.027 without it. The earlier attempt left that cell out as an assumption, because only its second site pair is in the files; this attempt kept it. I left `supports` out.
- **`fig8bc-cdgi-aims`** (blocked before, reproduced now). Cause `error`, in this attempt, medium confidence; I marked it as supporting blocked. The claim depends on `link-aim-mice`, which fails in both attempts, and the protocol (Author, step 1, item 4) blocks a claim whose link fails. This attempt tested it on the deposited preprint scores anyway (F(1,19) = 31.24), and its author's report says this goes past that rule.

**5. Protocol points that did not fit**
- `docs/pilot-notes.md` has no section for pilot-15 or any later version; its last is pilot-14. The `protocol` note is therefore read from `docs/protocol.md` itself. Findings now carry a severity (from pilot-18), and the notebook cell that shows them and the versions they were seen in (from pilot-19). `not_runnable` is now an allowed block reason, which explains why the spine claims are blocked as `not_runnable` here and as `methods_underspecified` before. None of these changes moved an outcome.
- The checkout is a shallow clone with one commit, so `git show $c:entries/...` returns the current entry, and `git fetch --deepen` timed out. I used the `earlier-entry/` copy instead.
- An exclusion choice like the fig1i one could be filed as `reading` or as `data_used`. I chose `data_used` because the only difference is one excluded cell.
- `versions` on the new data findings lists `draft`, which is a version name that can change.
- `git status` shows untracked dotfiles and `scripts` in the repository root. They are sandbox device nodes, not real files, so I left them alone.
