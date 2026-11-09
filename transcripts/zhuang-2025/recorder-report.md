I wrote the notes in `docs/pilot-notes/001177-zhuang-2025-01.md` and changed no other file. Nothing is committed.

A few points that affect how it reads:
- **CatalystNeuro line:** for this dataset the `catalystneuro` field names a contributor (Luiz Tauffer), not a conversion repository. I used the wording earlier notes use in that case: "(Luiz Tauffer of CatalystNeuro is a contributor)".
- **Counts:** `tools/readme_row.py` prints 0, 0, 0, 14, which counts only the claims on the dandiset. The 30 claims tested on the paper's Zenodo deposit are given separately (19, 7, 2, 2), as the 000336 and 000253 notes do.
- **Author's totals:** the author's report gives 18, 9, 1, 16. Those were the outcomes before the verification rounds; the notes use the final record.

```markdown
# 001177, Zhuang et al. 2025

On the dandiset itself no claim reproduced, none partially, none not
reproduced and 14 blocked, as dandiset 001177 holds none of the sorted and
labelled units the paper's electrophysiology rests on. The other 30 claims
were tested on the paper's own deposit at Zenodo (doi:10.5281/zenodo.15258978),
which holds its behaviour, histology, rotarod, open field and slice data: 19
reproduced, seven partially, two not reproduced and two blocked. It pins
version 0.250902.2127, its only published version. The paper, Zhuang, Lemak,
Sridhar and Nelson in Brain, reports that the D2/3R agonist pramipexole (PPX)
and the D1R agonist A77636 make parkinsonian (6-OHDA) mice choose fewer
delayed large rewards in a delay discounting task, that in these mice PPX
raises the firing of optically identified dMSNs and lowers that of iMSNs in
the dorsomedial striatum (DMS) at 4 to 5 h, and that inhibiting DMS iMSNs
(hM4Di) or exciting DMS dMSNs (hM3Dq) shifts their choices the same way. The
claims were written from the version of record in
Europe PMC (PMC12597312) with its supplement, and the paper's analysis code
(UCSF-Nelson-Lab/ICD-Cognitive-Analysis at commit 5528e222) was read for the
event and block names of the operant logs and the hyperbolic fit, which was
re-implemented. The delay discounting results of Figures 1, 2, 5 and 6 and
Figures S2 and S3, striatal and SNc TH, rotarod, instrumental learning, the
TH correlations of Figures 3 and S4, open field locomotion and the slice
validation of Figure S6 were tested. The 14 claims on single units (Figures 4,
6F-I, S5 and S8) are blocked as `data_missing`; `figs2abc-sex-similar` is
blocked as `metadata_insufficient`, as no file gives each mouse's sex; and
`figs1ef-ppx-locomotion` is blocked as `other`, as no PPX open field file was
deposited and the protocol keeps `data_missing` for claims on the dataset.
`fig3a-a-correlates-dms` is not reproduced (r = 0.32, p = 0.13 in 24 mice
against 0.51 +/- 0.051 in the paper's 28), and `fig5jl-dreadd-params` is not
reproduced, narrowly, as eight of its nine parts hold and the K rise in hM4Di
mice does not (p = 0.20). `fig1b-th-loss` is partially reproduced, with losses
of 64.3% (DLS) and 56.8% (DMS) against 50 +/- 5%, and in
`fig1ijk-ppx-a-k-auc` the rise in K is not significant by Dunn's test (p =
0.19), while the Friedman test over three conditions gives p = 0.032, the
paper's printed 0.03; the same procedure gives the paper's A77636 values exactly. The
author asked a reader no questions, so the answer run and the following author
run changed nothing. Round 1 agreed with 43 of 44 outcomes, and the author
took its outcome for `fig5jl-dreadd-params` (from partially reproduced to not
reproduced); its points led to all four pairings of PPX ON and OFF sessions,
both ON readings and a list of the unmatched mice for the Figure 3
correlations, pooled-error Bonferroni comparisons, per-minute velocity for the
CNO files without a tracking gap, and printed checks of the log parsing, the
sex search and the unit names. Round 2 agreed with 43 of 44, disagreeing on
`figs2ijk-ppx-washout`, where it judged the pooled-error comparisons better
supported by the paper's printed p-values, and found statements the outputs
did not support, among them "2 to 5" baselines per mouse, "no sorted units",
and a "twelve files" sentence that missed H1 and J3, which were corrected. A
third round, on the one proposed change, agreed that `figs2ijk-ppx-washout`
is reproduced. Some outcomes rest on weak ground: `figs2ijk-ppx-washout` is
reproduced with the Bonferroni comparisons on the pooled error and partially
reproduced with paired ones; `fig2bc-a77636-locomotion` and
`fig5cf-cno-locomotion` assume injection at 20 min into each open field file,
and the significant mCherry slowing that makes fig5cf partial depends on the 5
mCherry files with no injection mark; and `fig3a-a-correlates-dms` matches 24
of the paper's 28 mice. The author's run went from 10:25 to 11:55 UTC and
nothing failed; the notebook took 17.7 minutes at first and 1031 s in the last
run, under the 30-minute limit.

The dataset was converted by CatalystNeuro (Luiz Tauffer of CatalystNeuro is
a contributor). For 18 mice and 56 sessions it holds the 30 kHz voltage, the
1 kHz LFP and per-electrode threshold crossings with their waveforms, the
input to the paper's manual spike sorting, and none of what the paper's
electrophysiology analysis used: sorted single units (54 files have none),
their putative MSN class, their optical identification, the laser pulse times
and the PPX injection time. The two files with a units table (sub-E0 PPX day
4, sub-P4 PPX day 1) give spike times and unit names only; in E0 even and odd
units differ by about two orders of magnitude in spike count, consistent with
an unsorted and a sorted cluster per channel, but no column says which. Three
sessions have start times in 2025 (sub-H0-2 days 3 and 4, out of day order,
and sub-H4-3 day 3) while the same mice's other days are from 2023, likely the
conversion date; the subject descriptions are mis-encoded ('1.5â€¯microliters')
and the genotype is written 'Drd1a-Cre' in sub-E0's PPX sessions and
'Drd1aCre' elsewhere. In the Zenodo deposit the PPX open field data of Figure
S1E-F are absent, mouse E6 has no PPX or washout sessions and mCherry mouse
R5.5 has no delay discounting file. No file gives each mouse's sex, the open
field files carry no injection time, six A77636 and four CNO open field mice
are in no group list of the README, and the SNc cell count workbook has no
group column, so three of its 32 mice cannot be placed. The deposit holds 2 to
5 baseline sessions per mouse, and the Methods' stability rule finds a stable
run in only 12 of 47 PPX mice; which baselines entered the figures is not
stated, and using all of them gives the paper's statistics closely (delay F =
38.15 against 38.53). Not all sessions follow the Methods' task: the 2020
cohort of six control PPX mice ran delays of 0, 6, 12 and 18 s, and the 2021
cohort ran 30 free choice trials per block where the Methods give 20. 233
operant logs are byte-identical between the PPX and DREADD folders and 75
between the A77636 and DREADD folders, training and baseline sessions of mice
used twice, and the CNO files of H0 and H0.4 hold one recording deposited
under two mice. Two workbook sheets have a mislabelled block and two shifted
rows, and the rotarod workbook has 40 control mice where Table 1 gives 31. Six
of the 30 PPX parkinsonian mice have no striatal histology and two histology
mice are in no README list, so 24 mice can be matched for Figure 3 where the
paper has 28. The Figure S6C legend and Table 1 give p < 0.01 for the oIPSC
reduction in 6 cells, which a two-sided exact signed-rank test on 6 pairs
cannot give (minimum 0.031). Four questions are put to the paper's authors:
when the drug was injected in each open field file; whether striatal TH was
normalized to the controls of each staining cohort or to all controls; which
test gives p = 0.03 for the PPX effect on K in Figure 1J; and whether the
Bonferroni comparisons of Figure S2I-K were made on the pooled error or by
paired comparisons.

The author's points on the protocol: a `data: elsewhere` claim whose data are
public nowhere cannot be blocked as `data_missing`, so `other` was used with a
`data_missing` finding; findings are defined as about the dataset while most
here concern the outside deposit; group labels for data elsewhere had to come
from other files of the deposit or the DANDI subjects, and link claims do not
seem meant for this; the fig5jl criterion defines a partial outcome only for a
case that did not occur; it is unclear whether a claim's readings carry over
when another claim's criterion says "as" it; one expected value covered two
quantities in fig1b, so their mean was recorded; docs/archives.md has no
Zenodo section, so the files were streamed with fsspec as for CRCNS; and the
clock check could not be done for the electrophysiology, as no session has
trial or event tables.
```
