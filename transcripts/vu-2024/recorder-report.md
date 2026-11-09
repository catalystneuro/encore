I ran `python tools/readme_row.py 001084 --write`, which added the 001084 row to README.md. It gives 10 (+1) reproduced, 10 partially, 0 not reproduced and 1 blocked. I then added the subsection below to the end of docs/pilot-notes.md. I haven't committed anything. The repository root has some untracked files I didn't create (.bashrc, .idea, scripts and others), and I left them alone.

### 001084, Vu et al. 2024

Ten claims reproduced, ten partially and one blocked on the dandiset, none
not reproduced. With outside data, counted apart: one reproduced. Four claims
on data in other archives are blocked. Round 1 gave its own outcome for each
claim from the notebook with its conclusions removed and agreed with all 26,
giving `data_missing` as the reason for the five blocked claims; the author
kept `other` (not attempted) for the four whose data are on Zenodo, and changed
`figs3-targeting-errors` to `data_missing` after a new data check showed that
no file's fiber table holds a planned target and the paper's code reads the
targets from calibration files in none of the Zenodo archives. After round 1
the author also added variants that rank AP and the response within each mouse
and permute within mice, under which the light amplitude gradient (r = 0.152,
p = 0.013) and the light and tone latency gradients (r = -0.223, p = 0.0014;
r = 0.214, p = 0.003) remain, and a refit of DL18 with its 14 tones of 12 kHz
identified from the paper's published results. Round 2 agreed with all 26 and
nothing was proposed, so there was no third round. The paper records D1 SPN
calcium and dopamine release through micro-fiber arrays across the mouse
striatum, and reports that light and tone evoke dopamine release with distinct
spatial patterns and latency gradients, and that stimulating dopamine axons
through one fiber evokes release at other sites that falls with distance. The
isosbestic control, the pairwise correlations and bundle cross-talk, the
chronic reward responses, the link to the paper's published GLM results on
Zenodo, the light and tone patterns and their consistency across mice and
against movement, the 415 nm control, the latencies and their gradients, and
the optogenetic counts, spread with distance and tdTomato and photoswitching
controls were tested. The histology, the freely moving recordings and the two
D1-cre jaw claims are blocked as `other`, as their data are on Zenodo and were
not tested in this attempt. Some outcomes rest on weak ground:
`fig5ab-response-latencies` is partially reproduced only because the Methods
count latency from the onset frame, while the code's count, one frame later,
gives the paper's means within 2 ms; `figs4eh-patterns-not-movement` fails
under the code's raw DF/F because of the level before onset in the
deceleration trials, and a baseline-subtracted variant holds the tone pattern
in both splits; `fig1d-chronic-reward-stability` can be tested only to week 8;
and in `fig4e-light-increases-widespread` the paper gives p < 1e-6 for its
significance test where the chance rate per fiber is 0.024, which the author
did not block on, since the raw averages are identical to the paper's and
significance agrees with its published calls for 93.6 to 94.5% of pairs. The
author used the NIH author manuscript in PubMed Central (PMC10957316), whose
supplement was blocked by a captcha, so the supplementary figure legends were
not read, and took method choices where the Methods are silent from the
paper's code on Zenodo (doi:10.5281/zenodo.10272874).

The dandiset was converted by CatalystNeuro (catalystneuro/howe-lab-to-nwb).
The 280 fibers of the 7 salient-stimulus mice are the paper's, and their raw
triggered averages equal the paper's published values (largest difference
0.0). The optogenetic sessions (Opto2, Opto4, Opto9, UG21) hold no stimulation
times and no record of which fiber was stimulated, and the trigger line the
paper's code uses is not in the files; both can be recovered only from the
laser artefact in the DF/F, which is unambiguous in Opto2 and UG21 but spreads
over many fibers in the tdTomato mice. The event table gives tones without
their frequency, so DL18's 44 tones cannot be reduced to the 14 at 12 kHz the
paper analysed, and the tone start times are the trigger times, 11 frames
before the sound according to the paper's code, which the dandiset does not
say. DL15's sessions from 2021-09-10 (44 to 70 rewards) were run in a ViRMEn
task whose variables are not in the files, so unpredicted rewards cannot be
separated and Figure 1D can be tested only to week 8. The FiberPhotometryTable
column `included` is described as "whether this fiber has been successfully
implanted", but it marks fibers within the striatum, and in Opto2 two fibers
labelled Caudoputamen are not included; with them the counts match the paper's
24 locations. UG21's indicator is given as tdTomato, while its 3 sessions, 22
included fibers and stimulated fibers 12, 18 and 24 match the paper's rDAm3.0
mouse without opsin. In DL31 and DL32 the fiber photometry series store a
regular rate, but the frame timestamps of the behaviour drift from it by up to
0.43 and 0.54 s over the session. The data of Figures 2, 3, 7, S1 and S5A-D
are not in the dandiset and are on Zenodo, and Opto9 has 12 sessions, so one
of the paper's 26 tdTomato stimulations is missing; the planned fiber targets
behind Figure S3 are neither in the dandiset nor on Zenodo. Other findings: the
paper gives p < 1e-6 for its test of a significant response, the value for
independent frames, while with the same test three given consecutive frames
are all outside the band at a rate of 0.0037; the paper's latency code divides
the 1-based index of the half-maximum frame by the frame rate, so its
latencies are one frame (33 ms) longer than the Methods' definition; its
cross-correlation of DF/F with locomotion does not shift negative lags; the
Figure 1C legend describes 23 example fibers of a 93-fiber array, while the
code plots 33 fibers of mouse 842, whose recording has 82 fibers; and the
archive's summary gives the approach as "cell population imaging" and lists
only NWB container types as variables measured.

The notebook ran in 827 s in the first clean run, in about 10 minutes in two
runs after round 1 and in 12.2 minutes after round 2. Zenodo returned "429 Too
Many Requests" during preparation, handled with retrying range requests, and
early runs failed on a column named `tail` that clashed with a pandas method,
windows running past the end of the recording and event placement in the
18 Hz sessions. Round 2 found sentences the outputs did not support, among
them that none of the 405 nm traces has frames above the threshold (11 of 61
have none), an exact match of the data to the paper's analysis claimed for
mice beyond the 7 where it was shown, and the README run time, and these were
corrected; a slip in the verifier's own round-1 reason for fig1d was left as
given and corrected in the round-2 entry. The author's points on the protocol:
no blocking reason for a claim on data elsewhere that could be tested but was
not attempted; a reported number that matches code disagreeing with the
Methods, where the rule for several readings and the rule for Methods against
code point different ways; no guidance for criteria on supplementary figures
whose legends are unavailable; whether the stated spread in the tolerance rule
includes an SD across fibers; facts seen only while preparing that matter but
may not supply numbers; a duplicate check that needs data from every file; and
a 10-minute runtime aim that the Methods' 10,000 null refits exceed.
