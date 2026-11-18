I've written the reconciliation block in `attempts/gao-2018-02.yaml` and added `entries/gao-2018/earlier_findings.ipynb` to `entry.yaml`. Lock, check and run all pass: `reproduce_gao_2018.ipynb` ran in 918 s and `earlier_findings.ipynb` in 115 s, and `python tools/entry.py check entries/gao-2018` gives 0 errors. Nothing is committed. The blind attempt's outcomes, statements, notes, claims file and notebook are unchanged.

**1. Blind: no (`blind: false`).** The author run and the three author-revise runs saw nothing of gao-2018-01. The one hit in `author.md` is the record the author wrote. The author-answers run was looking for `questions/gao-2018.yaml` and printed lines 400 to 470 of `transcripts/see-2018/author-revise-1.md`. Those lines quote the start of gao-2018-01's questions file, including its E3 question and part of its reasoning: that the Fig. 2c peak lies in the response epoch under only one epoch choice. That run came after the outcomes were recorded and changed nothing. Its transcript also shows `head -4 questions/gao-2018.yaml` printing that file's first lines, although the run then says the file does not exist.

**2. Earlier findings**

| # | Earlier finding | Status | now |
|---|---|---|---|
| 1 | Data missing (CN units, licks, behavior-only sessions, …) | still_present | 1 |
| 2 | `photo_stim_id` has no description and there is no laser trace | still_present (checked) | 14 |
| 3 | Event times described as trial-relative but on the session clock | still_present | 3 |
| 4 | Hemispheres disagree with Supplemental Table 1 | still_present | 4 |
| 5 | anm subjects vs AN105–AN109, genotype "unknown", empty session_description | still_present (checked) | 15 |
| 6 | Unit counts above the paper's | still_present | 7 |
| 7 | 60 "pyramidal" units narrower than 0.45 ms; 20 kHz stated where the Methods give 25 kHz | still_present (checked) | 16 |
| 8 | Sessions not shown locked to trial events | still_present (checked; 2 of the earlier 5) | 17 |
| 9 | BAYLORCD8 20171020: 127 trials after the recording ends | still_present (checked) | 18 |
| 10 | Fig. 2c preference epoch; Fig. 3f random draw | still_present (checked) | 19 |
| 11 | Latency bin placement | still_present | 11 |
| 12 | Coding-direction captured fractions | still_present | 12 |

Findings 14 to 19 are added with `found: on_prompt`.
- **Finding 8:** with the earlier attempt's own test, 50 of 54 sessions show a locked response here; a second test based on lick-direction selectivity shows 48. Neither shows it in BAYLORCD13 20171211 or 20171215, so the finding now covers those two sessions only.
- **Finding 10, Fig. 3f part:** the draw decides the outcome only on code 6 trials (8 and 11 of 20 draws meet the criterion). With codes 5 and 6 pooled, no draw does.

**3. New findings of gao-2018-02:** 2, 5, 6, 8, 9, 10 and 13.

**4. Outcomes that differ.** All nine are most likely differences in method; none comes from a change in the dataset.
- **fig1g-dentate-activation-little-effect** (reproduced → partially): gao-2018-02 also used the CRCNS laser traces and found the result depends on two sessions whose light disagrees with their code.
- **fig1k-inhibition-delay-bias** (partially → reproduced): gao-2018-02 used code 6 alone and included CD8 and CD14; gao-2018-01 pooled codes 5 and 6 on CD12 and CD13.
- **fig2-preparatory-more-in-alm and fig2-peri-movement-equal** (blocked → partially): gao-2018-01 blocked them because the CN half is missing. gao-2018-02 recorded the ALM half, as the criterion allows.
- **fig3e-alm-mean-rate-unchanged** (partially → reproduced): different neurons (486 passing the deposited scripts' trial-count rule, against 676 by spike width) and trials.
- **fig3e-alm-increase-decrease** (partially → not reproduced): the two attempts read the criterion's fraction clause differently.
- **fig3f-alm-selectivity-abolished-by-cn-inhibition** (reproduced → not reproduced): gao-2018-01 judged by most of 20 draws on 438 neurons; gao-2018-02 made one draw on 336 neurons, code 6 only.
- **fig4g-dentate-effect-recovers** (not reproduced → partially): the latency method differs. The claims file also gained a named test for the fastigial comparison.
- **fig4i-fastigial-collapses-cd** (reproduced → partially): different session rule and coding-direction trials.

**5. What did not fit**
- **No pilot-15 notes:** `docs/pilot-notes.md` has no section for pilot-15 or any later version. The `protocol` field says so. It also names the one rule `tools/entry.py` attributes to pilot-15: a finding of kind `other` or `selection_undocumented` must say whether it is about the data or the paper, and a data finding in an attempt on several datasets names its datasets.
- **Earlier entry unavailable:** the repository history is a single squashed commit, so `git show $c:entries/gao-2018/...` returns gao-2018-02's entry, not gao-2018-01's. I rebuilt the earlier checks from its record and from its transcripts in `transcripts/gao-2018/attempt-01`.
- **Possible blinding leak:** `blind.sh` did not stop the earlier questions file from reaching the author-answers run, both through another paper's transcript and apparently directly.
