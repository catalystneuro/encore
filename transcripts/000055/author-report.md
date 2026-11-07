All five Author steps are done and the handover is built. The entry passed `tools/entry.py all` with 0 check errors, and the notebook ran from a clean environment in 1723 s (29 min). I did not verify my own work, commit or push.

**1. Outcome per claim** (pinned version 0.220127.0436: it is the only published version, the paper cites no DANDI version, and the draft lists the same 55 files with the same total size)

| Claim | Outcome |
|---|---|
| subject-days (link) | reproduced |
| roi-projection-link (link claim I added) | reproduced |
| cohort | partially reproduced |
| fig2-event-counts | not reproduced: 211 to 996 events per subject, median 770.5 |
| fig2-features-differ-across-subjects | reproduced |
| fig2-reach-shape | partially reproduced: angle peaks near ±70, not ±90 |
| fig2-bimanual-skew | reproduced |
| extfig2-1c-contralateral-larger | reproduced |
| extfig2-2-feature-correlations | partially reproduced: 5 of 6, magnitude–duration r = 0.233 against 0.26 ± 0.026 |
| fig2-days-and-waking | partially reproduced: S04's busiest day holds 38% |
| fig3-group-lfb-decrease-hfb-increase | reproduced (assumed) |
| fig3-sensorimotor-largest | reproduced (assumed) |
| fig3-lfb-more-widespread | blocked, methods_underspecified: the criterion's two readings disagree |
| fig4-precentral-subject-variability | reproduced (assumed; one tie broken) |
| fig5-band-power-differs-across-subjects | reproduced |
| table1-subject-band-power-ci | partially reproduced: 23 of 24 inside |
| fig5-recording-day-effects | reproduced: 24 of 24 agree |
| extfig5-1-baseline-reduces-day-variability | reproduced (assumed) |
| discussion-day-changes-small | reproduced (assumed) |
| The six Figure 6 and Extended Data 6-2 regression claims | blocked, too_large |

The regression claims are blocked because one model timed in the notebook took 8.0 s. The 2192 models give an estimate of 4.9 h on one core, or 1.2 h on 4 cores, before the variants the claims ask for.

**2. Dataset, assumptions, questions**

What I found about the dataset:
- **ECoG clock:** in three files (sub-01 ses-7, sub-04 ses-3, sub-06 ses-3) the ECoG covers only the end of the day but has `starting_time` 0. The events and pose use a clock that starts at midnight. Shifting the ECoG by 29241 to 30682 s fixes it, and the neural response confirms the shift.
- **Event count:** the files hold 8088 events with no false positives marked. The data descriptor says 6931, and the paper's counts per subject are lower.
- **Undocumented conventions:**
  - The reach angle is stored in image coordinates and not folded.
  - The pose is labelled meters but holds pixels.
  - Bimanual overlap is described as a fraction but reaches 3.83.
  - `session_start_time` gives midnight UTC labelled as 19:00 at UTC-5.
- **Missing values:** 124 event segments have missing (NaN) ECoG samples.
- **Subjects:** sex and age are not recorded. Seven subjects have electrode groups described as depth, where the paper says five.
- **Good flags:** the electrode `good` flags differ between days. I used each subject's first file, as the paper's code does.

Inputs: the paper's projection matrices on Figshare (doi:10.6084/m9.figshare.12114408.v1), checked by the link claim, and the paper's code at commit 04c6faf, which I only read.

Assumption: how a segment's power is summarised for the 0 dB and 3 SD rejection rules. I checked that it does not change the outcomes of the Figure 5, Table 1 and day-effect claims. I did not check that for the claims marked "assumed" in the table, so those carry `assumed: true`.

Two questions for the paper's authors are recorded as `methods_unavailable` findings:
- How was each segment's power summarised for the bad-segment rules?
- What measure decided that low-frequency decreases are "more spatially widespread"?

I asked a reader no questions.

**3. Where the protocol was unclear**
1. Step 4 says the author writes link claims but not whether that can happen after looking at the data. I wrote `roi-projection-link` after listing electrode and row counts, said so in its deviations, and added it to `depends_on` of the claims that use the Figshare matrices. I changed no statement, expected value or criterion.
2. Ties in a criterion's ranking: the protocol says to break them "as the paper implies", and here the paper implies nothing. In fig4 I broke the tie with a finer form of the same measure (interpolated width in Hz), recorded it as a deviation and gave the other result.
3. `measured` cannot hold null when some expected values cannot be measured. I left it out for cohort and explained in the notes.
4. After the run I corrected one conclusion's numbers (reading b gives 211 to 979, median 739, not 211 to 989, median 764). I edited that markdown cell in both the committed and executed notebooks, which is not re-run evidence. The protocol does not say how to handle this.

**4. Runtime and failures**

About 1 h 30 min of the 5 h (03:15 to about 04:43). Reading the ECoG segments takes 26.5 min of each notebook run, so it is close to the 60-minute limit. Nothing failed.

Two leftovers in the checkout:
- `entries/000055-peterson-2021/.claude/` is an empty folder the harness created. Removing it needed approval, which was denied automatically. Git ignores empty folders, so it should not show up in the commit.
- The untracked dotfiles at the repository root are sandbox device mounts dated 03:10, before this run. I left them alone.
