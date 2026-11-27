# malfatti-2026, Malfatti et al. 2026

Three claims reproduced, one partially, four not reproduced and 26 blocked, all
26 for missing data. No outcome rests on an assumption. The first verification
round agreed with 12 of the 34 outcomes: it gave the 21 calcium imaging claims
as blocked for missing data where the record had `too_large`, and
`fig4fh-gamma-session13` as not reproduced where the record had partially
reproduced, an outcome that rested on realigning four LFP mice; the author took
all of them. The second round agreed with all 34, and nothing was proposed
after it, so there was no third round. It pins version 0.261113.1541, the only
published version. The paper, Malfatti, Velica et al., "Increased layer 5
Martinotti cell excitation reduces pyramidal cell population plasticity and
improves learned motor execution" (eLife 14:RP109286), excites Chrna2
Martinotti (Ma2) cells of mouse M1 through hM3Dq and clozapine (CLZ) and
reports, in a pellet prehension task, miniscope imaging of layer 5 pyramidal
cells (PCs) with changed activity amplitudes, earlier and sharper peaks and
more rigid assemblies in Cre+ mice, learning curves unchanged by genotype in a
behaviour-only group, a higher success ratio under CLZ in trained Cre+ mice,
higher theta and gamma LFP power in Cre+ mice and on successful prehensions,
and, after caspase ablation of Ma2 cells, more pasta drops with no change on the
hanging wire. The claims were written from the eLife reviewed preprint v3 and
its supplement, whose Supplemental Tables 1M to 1P are missing, and from the
paper's code at commit 86efdf1, which has no spectrogram or band-power code;
the claims check corrected eight claims and added two, for 34. The two learning
claims reproduce on the behaviour-only group's DeepLabCut tracking with the
paper's prehension detector (genotype p 0.84, 0.84 and 0.58 against the paper's
0.83, 0.856 and 0.574; session F(9,99) = 9.57, 7.86 and 6.30 against
F(10,110) = 9.525, 7.571 and 5.536), and `fig4b-clz-improves-success`
reproduces (Cre+ F(1,4) = 19.66, p = 0.011; controls p = 0.62), on sessions 8
to 13 as session 7 is not deposited. `prehension-overlap` is partial: failed
prehensions overlap more than successful ones in every session, but at most one
of the ten values is within tolerance (successful in session 1 13.89% against
3.17%), and the miniscope tracking finds few prehensions. The four LFP claims
are not reproduced on the files as deposited: theta genotype p 0.235 to 0.480,
high theta accuracy p 0.211 to 0.482, low and high gamma genotype p 0.173 to
0.400 and 0.140 to 0.194, and no band with the genotype by session interaction
outside prehensions; Shapiro's test selects the mixed ANOVA, as the paper's
F(1,8) implies, and the ANOVA-type statistic alone would give a theta genotype
p of 0.017 to 0.034 in four of the six deposited readings, so fig4d rests on
that choice of test. The ANOVA-type statistic was implemented in Python from
the formulas of nparLD and could not be compared with R, which was not
available. The 21 imaging claims are blocked because no traces are deposited,
and the histology and caspase ablation claims because those data are not in
the dataset. The author asked a reader no questions. Round 1 found the
realigned LFP reading circular and confounded with genotype, the miniscope
detection unchecked and the later sessions not renumbered as the paper's code
does; in reply the outcomes were judged as deposited with the four mice left
out as a variant, a per-file tracking table was added and the sessions after 5
were renumbered +1. Round 2 found that the counts per 10 min of the halves of
session 5 were divided by the whole recording, as the paper's code does, and
sentences the outputs did not support, on realigning, the LFP scale, the start
times, the overlap variants, two LFP sessions and the streaming time, which
were corrected; it would have rated the LFP clock finding critical, and the
author kept it major as the files cannot settle it. The author's run took about
1 h 31 min (04:48 to 06:19 UTC); the notebook ran in 672 s at first, with peak
memory 3.4 GB, 7.3 min after round 1 with 4.0 GB, and about 18 min at the end.
Two development runs failed because the column names `norm` and `align`
clashed with pandas DataFrame methods, and were fixed.

The miniscope recordings are deposited only as raw videos (342 AVI files, 89.4
GB), referenced from OnePhotonSeries objects with empty data, with no cell
footprints, fluorescence or traces and no cell matching across sessions, so
none of the 21 imaging claims can be tested without rerunning the whole
extraction, for which the Methods and the code give neither the CNMF-E
parameters nor the matching threshold (major). In all 13 mice of the
behaviour-only group the files labelled session 6 hold the same DeepLabCut
tracking as session 5, one recording deposited twice; the Methods put the spoon
and plate halves of the fifth session in one 10 min recording, so the paper's
session 6 is the second half of the deposited session 5, and one of the 11
sessions the paper analyses is missing (critical). The two session 2
recordings of miniscope mouse 67111 hold the same behaviour video, tracked
twice (same frame count, pellet positions r = 0.98 and a median 0.97 px apart),
each with a different imaging recording (critical). The histology and the
caspase ablation group are not in the dataset, and five claims cannot be
tested. In four LFP mice (69107, 69109, 69110, 69204, all controls) the LFP
shows no potential locked to the prehension onsets at the deposited alignment
in any of 24 sessions, while in 16 of them one appears 6.9 to 9.0 s before the
onsets, consistent with clocks about 8 s apart, but the files hold no LED or
sync trace to settle it, and the clock of two further sessions could not be
established either. The LFP is stated in volts, but its values have standard
deviations of 72 to 1057 and reach plus or minus 6389.6, and mouse 67584 is at
4 to 60 times the other mice. Every file gives the sex as female, where the
Methods say the miniscope mice were male. The miniscope group holds 7 mice
where the paper analysed 6, and neither says which; its tracking has LPaw and
LFinger1 above 0.7 likelihood in a median of 0.2% of frames, against 1.4% and
2.4% in the other groups, and finds a median of 9.7 prehensions per 10 min,
against 66.8 and 117.2. The LFP group's session 7 is not deposited, one file
gives the genotype as unknown, mouse 67314 has 20 s of tracking against 602 s
of imaging in session 1, and 65 of the 66 LFP files start at 23:59:5x on the
last day of a month, which looks like a placeholder. The counts of the
behaviour-only and LFP groups match the paper. The paper's code divides the
counts of both halves of session 5 by the whole recording's length, and per 10
min of its own half session 5 has more prehensions than session 2 (123.1 and
30.3 against 88.7 and 24.0). Two questions are put to the paper's authors:
which spectrogram window and normalisation were used, and whether the alignment
of the four offset mice in the paper's analysis is the one in the files.

The author's points on the protocol: it lets a finding name the notebook cell
that shows it, but the attempt schema rejects `notebook` and `output` on
findings, and they were removed; it does not say what to do when a data defect
can be corrected only by an estimate, and the correction was treated as a
reading; the Methods' "cumulative mean" can be read as a running mean, which
the claims file did not list, and it was added as a reading; R was not
available, so the ANOVA-type statistic was implemented in Python; fig4b's
criterion names a session 7 that is not deposited, and sessions 8 to 13 were
used; and with one LFP channel per mouse the claims file's channel reading has
only one answer.
