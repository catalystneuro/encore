# 001051, Bennett et al. 2024

Ten claims reproduced, five partially, four not reproduced and 20 blocked on
the dataset, with three more reproduced, one more not reproduced and two more
blocked that also need outside data; a link claim added by the author,
`link-code-tables`, is partially reproduced. The first verification round
agreed with 43 of the 46 outcomes and the second with 44, and a third round,
held on the two changes of outcome proposed after the second, agreed with
both. It pins version 0.260922.1827; the paper cites no version, and the two
published versions hold the same 666 assets with the same blobs, the later one
only updating metadata. The paper, Bennett, Ouellette, Ramirez et al., "SHIELD:
Skull-shaped hemispheric implants enabling large-scale electrophysiology
datasets in the mouse brain" in Neuron, records with up to six Neuropixels 1.0
probes through a single-hemisphere SHIELD implant over the left hemisphere in
mice performing a visual change detection task on up to four consecutive days,
compares unit yield, drift and quality with the 5-mm window recordings of the
Visual Behavior Neuropixels (VBN) dataset, and studies 4 Hz alpha events in
VISp and MOp and their coupling with other areas, including caudoputamen (CP)
units with receptive fields (CP-RF). The claims were written from the version
of record with the supplemental figure legends and from the paper's code,
SHIELD_Dynamic_Gating_Analysis at commit 3c09a0dc, whose list of 87 sessions
passing ephys QC sets the session selection; the VBN comparison data come from
DANDI:000713 version 0.240702.1725 through the code's tables. The Figure 4
claims mostly reproduce: 1821.0 non-noise units and 28.11 areas per six-probe
session, 25 mice, 87 experiments and 507 probes with units (within 467 +-
46.7), a median max_drift of 25.05 um against 22.82 for VBN, 41.09% and 40.69%
of units passing QC, and stable unit yield, firing rate, RF fraction and
visual responses across days. `fig4d-qc-metrics-comparable` is not reproduced,
all 7 metrics differing by the code's Mann-Whitney test and 5 of 7 medians
being within 10%. `figs4i-insertion-suppression` is not reproduced, the fitted
recovery time constant being 36.0 min over the common 77.3 min against 22.5 to
33 min, and no window from 30 to 64 min bringing the pooled tau into the
range. The alpha-event claims were run under the claims file's 16
combinations of area membership (L1, L2), event rule (E1, E2), random-time
coherence (R1, R2) and session set: `fig7a-mop-higher-frequency`,
`fig7b-visp-offset-locked` and `fig8e-cp-rf-more-modulated` reproduce,
`fig7b-low-arousal` is partial (pupil smaller and running lower, but VISp -12.9
to -15.4% where the claim has 25%), `figs6-replay` (r = 0.21 to 0.63),
`fig7e-lags-straddle-zero` and `fig7-hippocampus-not-engaged` are not
reproduced, and `fig7cd-visp-coupling`, `fig7cd-mop-coupling`,
`fig7f-visp-network`, `fig7f-mop-network` and `fig8f-cp-rf-higher-coherence`
are blocked as `methods_underspecified`, the readings disagreeing.
`fig8bc-cp-rf-location` is partial, CP-RF units being more dorsal but more
lateral, not medial, and `fig8d-cp-rf-larger-response` partial, the effect
holding but the counts with the Methods' QC (70, 162, 218) missing two of the
expected values, which the code's filter meets (79, 206, 239).
`fig8d-response-latencies` is blocked as `methods_underspecified`, half-peak
latency giving lags of 16 and 20 ms, inside 20 +- 5, and time of peak 34 and 9
ms. The Figure 3 surgery, ISI, histology, MRI and training claims, the
bilateral recordings of Figure 5, the optogenetics of Figure 6 and
`fig4f-rf-match-retinotopy` are blocked as `data_missing`, and the trajectory,
retraction and sharpened-probe claims as `metadata_insufficient`. The author's
first run gave fig7cd-mop-coupling and fig8d-cp-rf-larger-response as
reproduced and fig8d-response-latencies as reproduced on a half-peak
assumption. The author asked a reader no questions, so the answer run and the
following author run changed nothing. Round 1 disagreed with those three
claims and asked for RF agreement per session, a spike-count check of the 6
mismatched sessions, the code's probes table, other fit windows for figs4i, a
run of figs6 on post-offset events only, a zero-padded spectrum for fig7a, a
Benjamini-Hochberg family of brain areas only and a clock check of the running
and pupil streams; in reply fig8d-cp-rf-larger-response became partial, the
other two were kept with the disagreement recorded, the checks were added, and
two questions were put to a reader, on whether fig7e's "straddled zero" means
a test of the median lag and whether fig8d's counts should take the code's
filter. Round 2 would block fig7cd-mop-coupling and fig8d-response-latencies
as `methods_underspecified` and found sentences the outputs did not support
(the 328 units said to be on probes the dandiset lacks, the 202 extra units,
alignment said shown in all but 8 sessions, a KS p, 22 of 32 combinations, the
hippocampal areas significant only under R2, r = 0.9989), which were
corrected; the two changes were proposed and round 3 agreed. The author's run
took about 1.5 h (03:50 to 05:20 UTC), the two sessions without eye tracking
crashing the first development pass, which was fixed; the whole dataset was
streamed twice, once in a full spike pass outside the notebook. The notebook
ran in 24.4 min at first, 1321 s after the answer, about 17 min after round 1
and about 22 min after round 2; the second revision run notes that `date -u`
gave times that do not fit the runs' lengths.

In 6 of the 87 sessions the paper analysed (1176989662, 1178460518,
1178693650, 1179911454, 1180266229, 1181096406) the units under each unit id
differ from the paper's units table at the cited commit: max_drift and
firing_rate differ for 55 to 99.8% of units and quality for 14 to 38%, the RF
p values recomputed from the files are uncorrelated with the table's (r = 0.03
over 251 units, against 0.9990 over 7095 units elsewhere), and the files'
spike counts fit the files' firing rates but not the table's, so the dandiset
seems to hold a different spike sorting or unit assignment for these sessions.
In 5 of them the paper's table has 328 units, 133 in CP, that the files do not
hold, each session's on one probe (probe_id 88, 46, 121, 133 and 139) that is
not among the file's probe_ids. The 87 sessions passing ephys QC are listed
only in the paper's code, the 12 other sessions are not explained, and in the
87 sessions the files hold 40 probe recordings (2004 units, 1873 on
unannotated channels) that the paper's tables leave out and nothing marks;
143,828 non-noise units, the paper's count, are on the 467 insertions in the
code's table and 202 on the other 40, and the code's probes table marks every
probe inserted, so it records no failed attempt. No file records the implant
hole or probe orientation of an insertion, which probes were sharpened, which
sessions had probes retracted 100 um, Dura-Gel use or failed insertion
attempts, and the files hold no per-spike depths. The dandiset holds none of
the Figure 3 material (surgery records, ISI images, histology, MRI, training
histories), the dual-hemisphere sessions of Figure 5, or the VGAT-ChR2 and
Vglut2-Cre mice of Figure 6; its 27 mice are all single-hemisphere
change-detection mice. Sessions 1187475832 and 1202438738 have no eye
tracking, and alignment of the running or pupil stream with the stimulus clock
is not shown in 12 of the 99 sessions. The Methods describe 8 natural images
in the task, where every session holds four image stimuli (three natural
images and im115_r at 0.7 contrast) besides omitted flashes. Questions are put
to the paper's authors: how the random-time coherence was formed, how units
were assigned to areas and which alpha-event rule was used, on which the
outcomes of four alpha claims depend and under which the code's choices give
the 439 events of Figure 8F; which latency measure Figure 8D used; the fit,
window and normalisation behind the 25 to 30 min time constant of Figure S4I;
and the windows and row normalisation of Figure S6F.

The author's points on the protocol: the claims file's header makes a claim
whose readings disagree `methods_underspecified` while step 1.6 allows an
assumption, and the claims file was followed; criteria mix matching under any
reading with requiring all readings to agree, and any was accepted only where
the criterion said "under a reading"; adding a link claim means editing other
claims' `depends_on`, though only reader runs write the claims file, and 28
were edited; there is no outcome for a partly testable claim, and figs4ab was
given as partial; the suggested clock contrasts do not fit eye tracking and
running; the protocol does not address editing conclusions after the run, and
only markdown was changed and copied into the executed copy; expected counts
that match only under a variant have no rule, and the variant's counts were
recorded with a deviation; and a full spike pass run outside the notebook to
develop the analyses streamed the whole dataset twice.
