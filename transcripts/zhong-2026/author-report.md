I did steps 1 to 5 and the handover. Of the 13 claims, one is reproduced (a link check I added), one is partially reproduced and the other 11 are blocked. The three Figure 3 claims are blocked because the paper's boundary and onset neurons cannot be identified in the dataset, and re-selecting them by the method of Zheng et al. 2022 (the source study, ref. [41]) gives a very different set. `tools/entry.py check` and `all` pass with 0 errors, the clean run of the notebook took 337 s, and the handover is in `executed/zhong-2026/handover/`. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| link-zheng-table-s2 (link claim I added) | reproduced |
| methods-subjects-included | partially reproduced |
| fig3a-dip-after-boundary | blocked: methods_underspecified |
| fig3b-individual-subjects | blocked: methods_underspecified (depends on fig3a) |
| fig3c-onset-control | blocked: methods_underspecified (depends on fig3a) |
| fig1d-basic-capacity-four, fig1d-chunking-retrieves-six, eq1-new-magic-number, fig2b-hierarchical-retrieval, figs2-delayed-hebbian-binding | blocked: other (simulations and a derivation; no data needed, simulation code not public) |
| fig4a-universal-slope, fig4b-plateau-near-eight, fig4b-three-languages | blocked: other (1950s–1980s recall tables printed in paywalled articles, in no data archive) |

- **Subject exclusion.** Using the per-subject cell counts in Supplementary Table 2 of [41], the rule excludes exactly the four subjects with no onset cell (TWH103, TWH109, TWH111, TWH125). That keeps 14 subjects, P64CS and TWH120 among them. The part that fails is the starting count: the dataset has 19 subjects, not 18. The paper's 18 matches only if TWH138 is set aside, because its spikes cannot be lined up with its trials.
- **Figure 3 selection.** Applying [41]'s Methods as written finds 8 to 10 boundary and event cells, where [41] counts 76 for the same subjects. Its chance rate is 0.02% and 0.25%, against [41]'s 2.11% and 2.26%. So this is not the selection the paper used.
- **Figure 3 results under that selection, for reference only.** Under every reading, the other neurons dip and then ramp after cuts. The lag is 75 to 490 ms, within 130 ± 13 ms in 5 of 64 readings. Clips with no cut show the pattern in 0 of 32 readings.

## 2. The dataset, assumptions and questions

**Version.** I pinned 0.220216.0323, the version the paper cites.

**What I found:**
- **No unit labels.** No unit is labelled as a boundary, event or onset cell, and [41] publishes only counts per subject.
- **TWH138 (sub-19).** Its spike times are on a different clock (about −7.02e12 s) from its trial table, in both the pinned and the latest version.
- **Clock not shown in 11 of the other 18 sessions.** In 7 sessions the population clearly responds to clip onsets. In the other 11 it does not, so I could not show that spikes and trial tables share a clock there. Three sessions respond to recognition images but not to clip onsets. TWH125, which has no onset cell in [41]'s table, has one of the strongest onset responses.
- **Fewer units.** The dataset has 565 units, all in the medial temporal lobe; [41] reports 580 there.
- **Later version.** 0.230530.1822 changes the spike times of TWH120 and has no release notes.
- **Table check.** The "all cells" column of [41]'s table sums to 943, not the 985 in its header.

**Outside material, all listed under `inputs`:**
- the Methods of [41], from PMC8966433;
- its Supplementary Table 2, typed by hand into the helper because it is an image in the PDF;
- the dataset's example code at commit 60f7ece, for which boundary columns are cuts.

**Method details I left open and ran every way.** These are: whether the permutation test is paired, whether soft and hard cuts are each compared with no-cut clips or pooled, and whether to use all cuts or the first cut of each clip. No outcome rests on an assumption.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- Which units were the boundary and onset neurons, and how were they chosen?
- What bin width, smoothing, window and z-score reference were used?
- Which cuts were used?
- Separately, I recorded that [41]'s selection cannot be repeated from its Methods text.

**Questions to a reader:** none.

## 3. Where the protocol was unclear

1. **Simulations and derivations.** No `blocked_by` value fits claims that need no data. I used `other`.
2. **`elsewhere` data that is only a table in a paywalled article.** The protocol forbids `data_missing` and gives no reason that fits. I used `other`.
3. **Chance-level rule.** It is written for a chance level stated by the paper. Here the paper reports none; the source study [41] does, so I applied the rule to [41]'s counts and chance rates.
4. **"No embedded numbers" against an outside table that exists only as an image.** I typed it into the helper as a constant, cited it, and checked it against the table's own column sums.
5. **Changing claim fields.** Using outside labels requires `data: with_labels` and a `depends_on` on the link claim. I changed only those two fields on methods-subjects-included, not its statement, expected values or criterion.
6. **The clock check.** The suggested decoding check cannot tell "no response" from "different clock". I added a population test, a scan of time shifts and recognition onsets, and named the sessions where the clock could not be shown.
7. **No null in the claims file's dip and ramp test.** It passes easily on noise, and the criterion gives no reference. I added clips with no cut as the reference.
8. **Harness string.** The prompt says "Claude Code"; the example entry used "Claude Code (GitHub Actions)". I followed the prompt.

## 4. Runtime and failures

The work took about 55 minutes, from 03:38 to about 04:32 UTC. Nothing failed in the final runs. I fixed one bug during development: a p-value key was being overwritten in the selection output; it changed no classification.
