I wrote two new files, `docs/pilot-notes/wang-2019-01.md` and `summaries/wang-2019-01.md`, and changed nothing else. `targets/dandisets.json` has no entry for SPARC:212, so the second paragraph does not open with the CatalystNeuro sentence.

# wang-2019, Wang et al. 2019

Eleven claims reproduced, none partially, two not reproduced and eight
blocked, all eight for missing data; the four simulation claims, which the
claims file marks as data elsewhere, are left out of the counts and are
blocked as `not_runnable`. Three outcomes, `fig1bc-rabbit-ap-cat-response`,
`fig1ef-mouse-ap-cat-response` and `fig3f-constant-pacing-sns-prolongs`, rest
on an assumption. The first verification round agreed with 19 of the 25
outcomes as they stood and the second with 24; it disagreed on
`fig2a-rabbit-monotonic`, a change to not reproduced was proposed, and a third
round reviewed that one claim and agreed. The record pins version 1, the only
one; the paper cites none. The paper, Wang, Morotti, Tapa et al. in the
Journal of Physiology, stimulates the sympathetic nerves of innervated,
Langendorff-perfused mouse and rabbit hearts through a spinal catheter and maps
voltage and calcium on the anterior epicardium, and reports that heart rate
rises in both species while rabbit APD and CaTD shorten and mouse APD first
prolongs and then returns by 60 s, that CaT amplitude rises similarly in both,
that APD changes more at the base than at the apex, that the repolarization
wavefront reverses in the rabbit but not the mouse, and, from myocyte models,
how these APD responses shape the CaT. The claims were written from the
accepted author manuscript (PMC6675632) without its figures. Reproduced are
the heart rate increases of Figure 1 (p = 0.0011 rabbit, 0.0033 mouse), the
Figure 1 AP and CaT responses, tested on the first 20 s of the Figure 2 hearts
because the Figure 1 values are not in the dataset (rabbit APD80 only on the
majority reading, 4 of 4 hearts, paired p = 0.13), the biphasic mouse APD
(50.52, 61.18 and 49.54 ms at 0, 15 and 60 s), the CaT amplitude increase,
under the unpaired-test reading of similarity only, the tyramine and
noradrenaline responses, the rate-step response of Figure 3E, the constant
pacing claim of Figure 3F on an assumed pairing of columns, and the base
against apex APD changes (rabbit p = 0.048, mouse p = 0.0019). Not reproduced
are the monotonic rabbit time course of Figure 2A, where heart rate peaks at
20 s (206.5 bpm) and falls to 194.75 bpm at 60 s, and the propranolol claim,
which fails the claims file's rule on one unadjusted paired t-test of 27
(APD80 at 10 s, +1.43 ms, p = 0.010). The paced experiments of Figures 4 and 6
and every map-based claim are blocked. The author's first run gave 11
reproduced, 2 partially, 1 not reproduced and 12 blocked. Round 1 found the
model code in the dataset, the fragility of the propranolol outcome and the
assumed Figure 3F pairing; in reply `fig3abc-tyramine-na-mimic-sns` moved to
reproduced, a pooled-error post hoc variant was added, and a question to a
reader in `questions/wang-2019.yaml` asks whether the simulation claims should
count as dataset claims. The first revision said Octave could not be installed
without root and that the propranolol outcome no longer rested on one
unadjusted test; round 2 found both unsupported, and in reply Octave was
installed from conda-forge, the mouse model was found to run far slower than
real time outside the notebook, the block was rested on the entry's pip-locked
Python environment, and the notes were corrected to say that the propranolol
outcome rests on that test. The author's run took about 20 minutes, nothing
failed, and the notebook ran in 11 s.

The dataset holds no optical maps, traces or ECG; its readme says "There is no
primary data, only a derivative folder", and the files, 3.5 MB in all, hold one workbook
of per-heart summary values for Figure 1 (heart rate only), Figure 2, Figure
3B to 3F and Figures 5F and 7F, with four CSV files that repeat the Fig2
sheet, so the Figure 1 APD, CaTD and CaT amplitude, the paced experiments of
Figures 4 and 6 and all activation, repolarization, APD and CaTD maps are
absent and 8 claims cannot be tested. dataset_description.xlsx gives 0
subjects and 0 samples, subject.csv and sample.csv are empty, and the
curator's note calls it a computational modelling dataset, although the
workbook holds measurements from the hearts of the Methods' 13 mice and 9
rabbits. No table identifies a heart or animal, so hearts cannot be followed
across figures, and the Figure 3F no-SNS and SNS columns can be paired only by
position; that outcome depends on the pairing, as unpaired tests find no
difference, and the SNS series is already 2.7 ms longer at time 0. The Figure
3F no-SNS series has 4 hearts where the legend gives n = 5, with the second
column empty, and one noradrenaline heart has no values at 12.33 s. The
deposited mouse APD80 at 60 s is 49.54 ± 4.94 ms where the Abstract reports
46.5 ± 9.1 ms. In Figure 3E every heart's no-SNS APD80 at 5 s equals its 0 s
value (56.9, 56.02 and 57.3 ms). The tyramine and noradrenaline tables label
time "SNS Time (sec)" though those hearts were not stimulated and each has an
undescribed column B, and the Figure 1 heart rates have no unit and no
statement of which part of the 20 s they are. The MATLAB models of Figures 8
and 9 are in the dataset (files/code/rabbit and files/code/mouse, with
instructions for Figure 8), where the claims file places them behind a
registration form. Two questions are put to the paper's authors: which test
and which comparison after the repeated measures ANOVA give each "*p<0.05 vs.
time 0", with what software and whether sphericity was corrected for, and
whether the Figure 3F columns are the same hearts in the same order.

The author's points on the protocol: it does not say whether a claim may be
tested on the same paper's data from another experiment of the same protocol,
and the Figure 2 hearts were used with `assumed: true`; it gives no guidance
for `data: elsewhere` claims whose code is also in the dataset, which were
blocked as `not_runnable`; its clock check does not apply to data that are only
tabulated values; its rule that absence is judged on the paper's test alone
conflicts with a claims file that names two tests, and the claims file was
followed; and `docs/archives.md` does not say whether to skip the root
`manifest.json`, which has no `s3VersionId`, so only versioned files were read.

---

In this data, sympathetic nerve stimulation raised heart rate in rabbit and mouse hearts, shortened the rabbit action potential and calcium transient, prolonged mouse APD transiently and raised calcium transient amplitude in both species. APD also changed more at the base than at the apex in both species. The paper's monotonic rabbit time course did not hold: mean heart rate peaked at 20 s of stimulation and then fell by 60 s. The repolarization reversal, the paced-heart experiments and the model simulations could not be tested, as the dataset holds only per-heart summary tables and the MATLAB models could not run in the entry's environment. The propranolol control did not reproduce, on a single unadjusted test.
