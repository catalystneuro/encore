# Yang, Ni, Sun, Xing, Wang, Zhang, Zhu & Xu (2025) from dandiset 001212

Tests the findings of [Yang et al. (2025)](https://doi.org/10.1109/TNSRE.2025.3614867) on
[DANDI:001212](https://dandiarchive.org/dandiset/001212/0.241023.0931), which holds 600 s ictal LFP
clips (DG, CA1, CA3, ANT, 1 kHz) from 7 pilocarpine-treated rats, each over 4 baseline and 4
closed-loop stimulation groups. The dandiset holds no seizure or stimulation times, no interictal
recordings and no recording durations. Seizure onset and end are marked here by a stated
line-length rule, and stimulation trains are found from their artefact, so every tested outcome
rests on that assumption.

| Claim | Outcome |
|---|---|
| cf_w vectors correlate more within than between baseline groups (Table S1) | Reproduced, with self-pairs included |
| R1's top cf_w node changes across baseline groups (Figure 2) | Partially reproduced |
| The GC targets give 8 target and 20 non-target groups (Figure S2) | Partially reproduced |
| Target stimulation shortens seizures in every rat (Figure 3A) | Not reproduced |
| Some non-target stimulation lengthens seizures | Reproduced |
| Sites differ within rats R2, R3, R4, R5, R7, not R1, R6 | Partially reproduced |
| Target -0.26 against non-target 0.038 normalized duration | Not reproduced |
| Five named non-target sites shorten seizures, less than the target | Partially reproduced |
| Same site, target shortens more than non-target (Figure 3B) | Not reproduced |
| Seizure duration proportion, seizure frequency | Blocked: data missing |
| PSD ratio, alpha and theta or beta up and gamma down after target stimulation | Not reproduced |
| No difference in the other bands | Not reproduced |
| Lower IIS rate 15 to 45 s after target stimulation | Reproduced, resting on one rat (R7) |
| Interictal IIS, IIS against seizure frequency, interictal HFOs | Blocked: data missing |
| No difference in ictal ripples | Reproduced |
| Target stimulation reduces ictal fast ripples | Not reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The Granger causality targets come back for 21 of the 28 baseline groups (AIC order) when cf_w is read as
causal outflow (out minus in strength), which settles a sign the Methods state the other way. The
dandiset's baseline groups hold some stimulated seizures, some clip names occur in two groups, and
the stimulation order of two rats differs from the paper's Figure S2. The attempt record, with the
reasons and the differences from the paper's method, is
[`attempts/yang-2025-01.yaml`](../../attempts/yang-2025-01.yaml).
