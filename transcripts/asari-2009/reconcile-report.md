I added the reconciliation to `attempts/asari-2009-02.yaml`. `python tools/entry.py check entries/asari-2009` reports 0 errors, and `entry.py run` passed all three notebooks, including the new `earlier_findings.ipynb`. Nothing is committed.

**1. Blind: no (`blind: false`)**
- **What it saw:** in its first revision run, the author listed `transcripts/asari-2009/`. That folder still held `asari-2009-01`'s transcripts, and the author printed the first 50 lines of that attempt's `verifier-2-report.md`.
- **What that showed:** by the author's own report, the earlier outcomes and the earlier Figure 7 finding. It says it read nothing more, and flagged this itself. The transcript did not keep that output, so I can't confirm exactly what it saw.
- **Before the exposure:** the first author run had not seen any of it. Its record already blocked `fig7-example-frequency-context` and contained the Figure 7 finding.

**2. Earlier findings**

| Earlier | Topic | Status | Now |
|---|---|---|---|
| 1 | No voltage-clamp recordings | still_present | 1 |
| 2 | Figure 7 DMR recording missing | still_present | 7 |
| 3 | Cell counts and ensembles differ from the paper | still_present | 6 |
| 4 | Property ensembles not documented in the data | still_present | 10 |
| 5 | Two cells listed in both groups of Summary.mat | still_present (checked in the notebook) | 16, added as `on_prompt` |
| 6 | How ended probes are averaged | still_present (checked in the notebook: 0.225 vs 0.237) | 17, added as `on_prompt` |
| 7 | Which stimuli form each ensemble, and how they are counted | still_present | 10 |
| 8 | A1 spike detection and time windows | still_present | 8 |
| 9 | 64.6% for 73/110 | still_present | 15 |
| 10 | CxtDep.m centring each trial, and silence as a context | still_present (checked in the notebook) | 18, added as `on_prompt`; the silence part is finding 11 |

**3. New findings in `asari-2009-02`:** 2, 3, 4, 5, 9, 12, 13, 14.

**4. Outcomes that changed**
- **fig3a-proportion-significant** (reproduced, now not_reproduced) and **fig3b-fractional-power-decay** (not_reproduced, now reproduced): the methods differ. `-02` cuts 20051108-ha1-001's probes with the fragment lists that fit its triggers; `-01` used the stored lists, which are swapped. Rerun with the stored lists, `-02`'s code gives exactly `-01`'s fig3a values: 186 significant probes, late fraction 0.252 and 0.267, peak at 4.78 s. The notebook records this. For fig3b, `-02`'s record already shows that the stored lists give `-01`'s 1.74 to 1.78 s.
- **fig8c-relative-effects** (not_reproduced, now partially_reproduced): mostly the same correction. The natural-sound reference area is 0.762 s with the stored lists (`-01` reported 0.752 s) and 0.525 s with the corrected ones. That raises the amplitude and frequency ratios to about 1. The two notebooks also build the property ensembles differently.
- **fig8a-proportion-by-property** (partially_reproduced, now not_reproduced): the two notebooks build the ensembles differently. Higher-order is 45/137 (0.328) in `-01` against 64/131 (0.489) in `-02`, which breaks the order AM > FM > higher-order.

**5. What did not fit the protocol**
- **Blindness failed:** `tools/blind.sh` did not remove the earlier attempt's transcripts before author-revise-1. Both attempts write to the same `transcripts/asari-2009/` folder.
- **Earlier entry not in git:** the checkout has a single commit, so the `git show $c:entries/...` step returns `-02`'s entry, not `-01`'s. I used the untracked `earlier-entry/` folder and the `-01` record instead.
- **One `now` per finding:** earlier finding 10 holds two problems, and `-02` reported only one of them. I pointed `now` at a new `on_prompt` finding for the other part. Earlier findings 4 and 7 both point at `-02`'s finding 10.
- **Paper-side question:** earlier finding 6 is about the paper's text, which doesn't change with the dataset version. I checked it by computing both readings on the data.
- **Slow run:** `entry.py run` has no option to run a single notebook. Adding one 6-minute notebook meant two full reruns of about 70 minutes each.
- **Files I didn't create:** untracked dotfiles (`.bashrc`, `.profile`, `.gitconfig` and others) and `scripts/` appeared at the repo root during the session. I left them alone; the workflow should leave them out of its commit.
