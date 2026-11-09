# 000774, Hickman et al. 2026

Eleven claims reproduced, three partially, seven not reproduced and 21
blocked. The first verification round agreed with 40 of the 42 outcomes and
the second with 38, and a third round, held on the four changes of outcome
proposed after the second, agreed with all four. It pins version
0.260520.1753, the version the paper cites and the only published version.
The paper, Hickman, Hughes, Sahai, Miles and Denman in Cell Reports, records
units in nine awake, head-fixed mice with three Neuropixels 1.0 probes
inserted around a 16-channel stimulating electrode in layer 5 of left V1,
gives single biphasic pulses of 5, 25, 50 and 100 uA, cathodal, anodal or
bipolar, and relates the evoked potential, direct responses, FS and RS
classes, the modulation of the wider circuit and its dimensionality to
amplitude and distance; four further mice with chronic electrodes learn to
detect the pulses in a lick task. The claims were written from the NIH author
manuscript (PMC13404931) and Document S1, without Table S1, and from the
paper's code at commit c4aaa60. 21 claims were tested; the 11 evoked-potential
and saturation claims of Figures 1 to 3, S1 and S2 are blocked as
`data_missing`, as they rest on the raw AP band, and so are the 10 behaviour
claims of Figure 7 and S10. Three tested claims use the evoked-potential
boundaries the paper's code computed (EP_distances.pkl), the outside input
their criteria name. `fig4h-ks-distinct` is not reproduced, 5 against 100 uA
having Holm-Sidak adjusted p = 0.1105 with the dataset's contact coordinates
and 0.0164 with the code's. `fig4f-responders-within-ep` and
`fig5i-fs-within-ep` are not reproduced, RS responders within the evoked
potential at 5 uA being 0.400 against 0.333 +- 0.033 (0.333 with the code's
coordinates), and `fig4h-distance-decreases` is partial, its tests holding but
the 25 uA mean being 264 um against 300. `figs3e-early-windows` is not
reproduced, the 100 uA proportions being 0.058 and 0.106 against 0.092 and
0.175, and so is `fig5-fsrs-proportion`, no reading giving the four
proportions. `fig6c-modulation-cortex` gives the paper's values under the
code's 0 to 500 ms window, but under the Methods' 500 to 1000 ms window the
region term has p = 0.457, and the criterion asks for every reading, so it is
not reproduced. `fig6d-hva-subcortical` is not reproduced, the legend's groups
giving 13.91 against 13.26 (Tukey p = 0.784); the paper's 15.82 comes from the
code's groups. `fig6e-circuit-responders` is partial, two values being just
outside 10% from the resampling of the ZETA test, and `figs9-state-drp` is
partial, its values being about a quarter of the paper's at 5 uA and a sixth
at 100 uA. `fig5j-fs-closer` and `figs6b-fsrs-early-firing` reproduce on the
code's 0.4 ms duration classes, where under 20 k-means runs the waveform
effect of fig5j is never significant (p 0.087 to 0.401), and
`fig6f-no-propagating-wave` reproduces on the code's peak rule, the
criterion's 4 ms width filter making both correlations significant (r = 0.131,
p = 0.001 and r = -0.115, p = 0.004). `fig4i-proportion-within-ep` reproduces
on the code's sign of the raw distance, the unsigned distance giving 0.0221,
just outside 0.020 +- 0.002. The author's first run gave 9 reproduced, 7
partially, 2 not reproduced and 24 blocked, with fig4f, fig4i and fig5i
blocked as depending on a blocked claim. The author asked a reader no
questions, so the answer run and the following author run changed nothing.
Round 1 disagreed with `fig5ef-polarity-clusters`, as the notebook had not
searched the assignments of clusters the criterion allows, and with
fig5-fsrs, as reading (b) was not run; it asked for fig4f, fig4i and fig5i to
be tested with the code's boundaries, and found that the k-means classes rested
on one run, that the peak rule of fig6f left out the 4 ms width, that the
legend's subcortical group of fig6d was never run and that the text on the
ZETA trials was wrong. In reply the assignment search made fig5ef reproduced,
reading (b) made fig5-fsrs not reproduced, fig4f and fig5i became partial and
fig4i reproduced, fig6f was marked `assumed`, and four questions were put to a
reader. Round 2 disagreed with fig4f, fig5i, figs3e and fig6c, partial where
their criteria have no partial clause, and found sentences the outputs did not
support (the code's coordinates said to match the paper exactly, where the 50
uA extent is 868 against 965 um and the 50 against 100 uA KS p 0.8245 against
0.083, counts of 273 CA1 and 151 units printed nowhere, values a quarter of
the paper's where at 100 uA they are a sixth, 20 k-means runs from other seeds
where one is the original run, and unit counts said to equal the code's table
with no output comparing them), which were corrected. The author proposed not
reproduced for the four, and round 3 agreed. The author's run took about 1 h
47 min (17:03 to 18:50 UTC); an earlier version used zetatest from zetapy 4.1,
which gave lower responder proportions, and was replaced by getZeta from zetapy
2.7.2 with a one-line scipy shim. The notebook ran in about 12 min at first,
520 s after the answer, 747 s after round 1, 803 s after round 2 and 727 s in
the last run.

The raw AP band, LFP band and NI-DAQ files are not deposited (the paper says
they are available on request), so 11 claims cannot be tested and the
comparisons of units with the evoked-potential boundaries can be made only
with the boundaries from the code's repository; the behaviour of the four
trained mice is not deposited anywhere the paper names, and its code reads it
from local CSV files, which blocks 10 claims. The stimulation contact
coordinates of jlh31 and jlh32 in the trials table differ from those in the
paper's code by 206 um (100, 150, -100) and 373 um (370, 0, -50), the other
seven recordings agreeing exactly, and with the code's coordinates the three
not reproduced distance claims would be reproduced. The electrodes table holds
placeholders (location "none" for all 1152 channels, x 5 to 53, y 0, z 3820,
impedance 0), so channel coordinates were fitted from the units' coordinates,
and the stimulation contacts have no region. The units table holds neither the
waveform classes nor the stability flags; recomputed, the stability filter
gives the code's unit counts for every cathodal and anodal condition and 1 to
5 more or fewer for bipolar ones. The paper's code assigns FS and RS by a 0.4
ms duration threshold, where the Methods describe k-means, and the two give 616
and 332 FS units and different outcomes for fig5j and figs6b. The dandiset
holds ten recordings where the paper analyses nine, and does not say that the
tenth, jlh41, which has no CCF coordinates or regions, was left out. Cathodal
single pulses are in seven of the nine recordings, while the legends give n =
9; jlh39 and jlh49v1 hold only bipolar pulses and jlh40 no bipolar ones, jlh33
has 60 trials per condition where the Methods state 75 and no anodal 50 uA
single pulse, and trial and spike times of jlh40 and jlh53concat are negative
in part. In jlh53concat each run number 0 to 7 is used by a monopolar and a
bipolar run, so the paper's ZETA code takes 150 trials of both polarities. The
file of jlh49v1 is filed under subject jlh48, with an age (P381D) one day more
than that of the jlh48 file, recorded four months later. In all nine
recordings the population fires less in the 3 ms before the logged pulse
onset, down to 0.07 to 0.20 spikes per trial from 2 to 1 ms before it (0.61 in
jlh31), against 0.81 to 2.03 from 8 to 7 ms before. The code's HVA group for
Figure 6D adds superior colliculus and dentate gyrus units (151 good stable
units in nine recordings) and its subcortical list has no CA1, and its region
mapping looks for "posteromedial area", which leaves 16 PM units out of Figure
6E. Questions are put to the paper's authors: whether the FS and RS classes
were assigned by k-means or by the duration threshold; which window and bins
the modulation index uses, the Methods' 500 to 1000 ms, the legend's or the
code's 0 to 500 ms; and whether the 4 ms minimum peak width of Figure 6F was
meant to apply.

The author's points on the protocol: the claims file calls the code's
evoked-potential boundaries an outside input for the author to judge while the
protocol blocks a claim that depends on a blocked claim, and the first run
blocked the three dependent claims; nothing says what to do when an outside
check such as the code's coordinates flips an outcome, and the outcome was
judged on the dataset with a `code_mismatch` finding; the reader's step 2
(follow the Methods, the code as a variant) conflicts with the author's step
1.6 for the FS and RS classes, and step 1.6 was followed with the outcomes
marked `assumed`; the fig6c criterion asks for every reading to pass against
the protocol's rule that one matching reading is enough, and the criterion was
followed; nothing covers paper software that needs a patch to run on the
locked Python 3.13, and zetapy 2.7.2 was run with a scipy shim; nothing covers
running only part of a test for time without blocking it, and ZETA was run on
the cathodal conditions only, with the full model shown from the cached
p-values; and the tool's provenance field name and the prompt's harness string
differ slightly, and "Claude Code" was recorded.
