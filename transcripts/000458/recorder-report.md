I wrote `docs/pilot-notes/000458-claar-2023-01.md` and changed no other file. Nothing is committed. The other untracked files at the repository root (`.bashrc`, `.vscode`, `scripts` and so on) were not created by me; they appear to be the sandbox mounts that an earlier note also mentions.

# 000458, Claar et al. 2023

12 claims reproduced, 13 partially, seven not reproduced and five blocked. It
pins version 0.230317.0039, which the paper cites and which is the only
published version; the dandiset names the bioRxiv preprint. The paper, Claar,
Rembado, Kuyat, Russo, Marks, Olsen and Koch in eLife, records a 30-electrode
skull EEG and up to three Neuropixels probes in head-fixed mice while single
biphasic pulses at three currents stimulate MOs or SSp in layer 2/3
(superficial) or layer 5/6 (deep), awake (quiet or running), under isoflurane
and in recovery, and shows that deep stimulation evokes a late ERP component
that follows thalamic rebound bursts and that PCIst is lower under anesthesia.
The claims were written from the version of record in Europe PMC with its
figure supplement legends; the paper links only the PCIst code
(renzocom/PCIst at commit e495a0a), whose threshold search was replaced by an
exact count and checked against the original on all 30 sites with a largest
difference of 0. No analysis says which current it uses, so the highest and the
medium current were both run, and the medium current gives the example ERP of
Figure 1, figure supplement 1 (1.011 s and 11.133 SD.s against 1.01 and 11.13).
`stim-depths` and `fig1-supp2-first-peak-flips` are blocked as `data_missing`,
as the files hold no stimulation depth in mm or electrode position,
`fig6a-csd-sink` and `fig6-supp1-erp-deep-csd` as `metadata_insufficient`, as
no channel carries a cortical layer, and `fig3d-magnitudes` as `too_large`, as
its LFP and CSD computation would take 234 to 265 min against the 30 min
notebook limit. Among the not reproduced outcomes, 0 to 2 of 12 superficial
sites lack a late ERP peak in `fig1d-two-erp-peaks`, 2 to 6 of 7 superficial
sites show decreases outside the stimulated area in `fig4be-off-period`, SM-TH
leads cortex in the rebound by 0.9 to 19.5 ms against 36.0 in
`fig5f-rebound-latency`, and the trial-by-trial correlations of
`fig6b-bursts-cortical-rate` and `fig6c-cortical-rate-late-erp` average 0.13 to
0.24 and 0.21 to 0.32 against 0.4 +/- 0.04 and 0.5 +/- 0.04.
`fig3abc-decay-with-distance` is partially reproduced, as MO exceeds VIS for all
three signals in 112 of 128 combinations of readings but no combination puts all
six values within tolerance. Some passes are weak: `fig8e-pcist-recovery` passes
on one combination of readings, `fig2c-superficial-quiescence` rests on 2 sites,
and `fig7f-early-latency-state` rests on an assumption, responsive units taken
from all awake trials, and on 6 to 8 animals against the paper's 13. The
author's first run gave 14 reproduced, ten partially, seven not reproduced and
six blocked. The author asked a reader no questions, so the answer run and the
following author run changed nothing. Round 1 agreed with 35 of 37 outcomes,
disputing the blocks of fig3abc and fig3d, and found that the artifact mask
missed the stimulus artifact, which falls one EEG sample before the onset
sample; masking that sample moved `fig1e-erp-duration`,
`fig7c-erp-duration-state` and `fig7d-erp-magnitude-state` to partially
reproduced and `fig8b-pcist-awake-anesthesia` to reproduced, and
`fig1f-erp-magnitude` now passes without an assumption (3.03 against 5.86,
p = 0.035, paper p = 0.0354). Its points also led to the unit counts per current,
first-trial matching by time, fig8d per animal, an explanation of the fig8e
outlier (site 546655 matched on one trial, PCIst 306.6) and two questions to a
reader, put during the revision after the answer step. Round 2 again agreed with
35 of 37, finding the fig3 blocks to be effort limits, found that the signed
spiking integral lets the suppression cancel the excitation, and found
sentences the outputs did not support, among them 19 sessions where there are
18, which were corrected. The author then wrote claar_lfp.ipynb and proposed
fig3abc as partially reproduced and fig3d as `too_large`, and a third round
agreed with both, with reservations on the fig3d estimate, and led to a third
reader question, on the signed or |z| spiking magnitude. A residue of the
artifact remains in the last 20 ms of the baseline; with a baseline ending 20 ms
before the pulse, outside the criteria, fig1e and fig7d would have all their
means within tolerance and fig8e's passing reading would fail (isoflurane 18.11
against 14.3 +/- 2.3), and the outcomes stay on the criteria's baseline. The
author's run took about 2 h 10 min, ending at 06:12 UTC; the first
`entry.py all` failed in the EEG notebook on the site with no valid trials and
was fixed. The notebooks ran in 14.2 and 13.5 min at first and in about 15, 14
and 6.5 min in the last run.

The depth of the stimulating electrode in mm and its position are not in the
files, which give only the target area and the label "superficial" or "deep", so
the paper's stimulation depths and the spatial analysis of the first ERP peak
cannot be tested. Probe channels and units carry CCF areas without cortical
layers, so the layer-resolved CSD analyses of Figure 6 cannot be run and the
exclusion of layer 1 in Figure 3 can only be approximated (here by the top
100 um of each area). The RS unit counts in the Figure 4 legend (870, 4110, 2559
and 9363) are three times the counts in the files (290, 1370, 853 and 3162;
exactly three times for the first three), and counting each unit once per
current gives 870, 4110, 2559 and 9486, so the legend most likely counts unit x
current; the paper does not say. is_valid marks all 720 pulses of the
superficial SSp site of subject 586468, and 747 of 1440 pulses of subject
569070, as invalid, for "large electrical artifacts" or "off target"
stimulation, without saying which; leaving out the 586468 site gives the
paper's N of 12 superficial sites in Figure 1E and 7 in Figure 4. The trial
start times lag the EEG stimulus artifact by up to one EEG sample (0.4 ms), as
the artifact is largest at the sample before the first sample at or after
start_time in 24 of 30 sites. The units' waveform_duration is described in
seconds, but its values (0.10 to 2.07, median 0.58) are in milliseconds, and the
units' quality threshold is not stated: all meet ISI violations < 0.5 and
amplitude cutoff < 0.1, but presence ratios go down to 0.02. The good EEG
electrodes are marked (is_data_valid, a mean of 23.07 per subject against 23),
and the state trial counts match the paper. Five questions are put to the
paper's authors: which current each analysis uses, what divides the ERP
magnitude, whose "area under the baseline window" is zero for a z-scored GFP,
whether responsive units for Figures 7F and 7G were selected once or per state,
which pre-stimulus window and correction family the modulated-unit test uses,
and whether the spiking magnitude of Figure 3 integrates |z|.

The author's points on the protocol: the claims file's readings multiply to 16
to 128 combinations per claim, so that reproduced under one reading becomes easy
to meet, and all were run with the first-listed reading recorded as `measured`;
it does not say whether a reading that cannot be computed as written, such as
the magnitude divided by zero, is an assumption or a block, and it was treated as
an assumption; it does not separate `too_large` from a run's time limit, and
fig3abc was first blocked as `metadata_insufficient`; it has no rule for a
tolerance of exactly zero, and fig5c's superficial median of 0.003 was judged
literally; criteria without a partial clause were judged by the general
definition (fig4cf, fig8b); and `entry.py` cannot run one notebook, so each fix
cost a full 28-minute run.
