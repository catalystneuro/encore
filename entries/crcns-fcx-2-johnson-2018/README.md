# Johnson et al. (2018) from CRCNS fcx-2

Tests the findings of [Johnson et al. (2018)](https://doi.org/10.1371/journal.pbio.2004274) on
CRCNS [fcx-2](https://doi.org/10.6080/K0VX0DQD), which holds the preprocessed intracranial EEG of
the paper's 10 subjects (254 bipolar MTL, PFC and OFC electrodes) in the visuospatial working memory
task, with trial tables and the paper's MATLAB analysis scripts.

| Claim | Outcome |
|---|---|
| All subjects proficient (accuracy 0.79 to 0.97) | Reproduced |
| Accuracy and response time do not differ by condition | Reproduced, resting on assumptions |
| 254 electrodes, 36 MTL, 116 PFC, 102 OFC | Reproduced |
| About 100 correct trials per subject | Reproduced |
| ERPs do not differ by condition | Not reproduced, resting on an assumption |
| Sustained theta power in all regions | Not reproduced |
| 8 electrodes with power condition effects | Not reproduced |
| PLV peaks in theta | Reproduced |
| Theta PSI shifts from frontal to MTL leads | Not reproduced, resting on an assumption |
| Cross-spectral PSI shifts after the test cue | Not reproduced |
| Counts of theta phase-directing electrodes and pairs | Not reproduced |
| Equal cross-spectral strength across frequencies and directions | Blocked (methods underspecified) |
| Individual theta peak bands | Not reproduced |
| Theta PAC by condition (eight claims) | Blocked (methods underspecified) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The analysis windows are placed by the trial table and the descriptor, 1.5 s earlier on the
derived time axes than the paper's deposited code places them: the trials with the two delay
lengths part where the table puts the delay-dependent events, and not where the code does. The
code's windows are run as a variant. If the deposited scripts produced the paper's figures, the
paper's numbers come from the code's windows, so the main reading tests the claims against the
events the Methods describe and does not recompute the paper's numbers. The table's windows start
close to a segment's first sample; joining the three segments of each trial shows that this leaves
baseline power unchanged and lowers theta power only in the first 250 ms of encoding, without
changing an outcome. The phase-directing units that the equal-strength and PAC
claims rest on cannot be selected: the PSI of the paper's Methods selects at most 3 per system, and
the deposited code's own form of PSI selects as many units with trials shuffled as on the real
data. The behaviour claim is reproduced with condition as one numeric term, as the amended claims
file judges it, on the response times of `summary_file.csv`; the trial tables' response times
differ from those in 7 of 10 subjects, no summary of them gives the file's values, and they would
show a condition effect. The attempt record, with the reasons and the differences from the paper's
method, is
[`attempts/crcns-fcx-2-johnson-2018-01.yaml`](../../attempts/crcns-fcx-2-johnson-2018-01.yaml).
