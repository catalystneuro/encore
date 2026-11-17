I worked through every point in the round-1 report. The entry was re-run in full with `python tools/entry.py all entries/peron-2020`: 0 check errors, notebook passed in 45.5 min. The record now has 18 claims reproduced, 6 partially reproduced, 5 not reproduced and 2 blocked. Nothing is committed.

## Outcome changes

**Model claims (problem 1).** I rebuilt the network from the Methods in numpy, with the time-step loop compiled by numba, in a new helper `peron2020_model.py`. It ran 30 networks per condition, 840 runs of 20 s, in 32 min.
- **model-amplification-increases:** reproduced. The input strength matched at Pconn 0.4 is below the one at 0.2 (218 → 28.2 under reading a, 150 → 15 under reading b).
- **model-increased-connectivity-ablation-decreases:** partially reproduced. Scores fall significantly under every reading (0.282 → 0.096), but the values are outside tolerance.
- **model-more-ablation-larger-decline:** partially reproduced. The decline grows with each ablation size, but R = −0.726 / −0.558, outside −0.65 ± 0.065.
- **model-slow-input-sensitive:** partially reproduced. With slow input, scores fall at Pconn 0.4 and not at 0.2, but the values are outside tolerance.
- **model-equal-connectivity-ablation-increases:** not reproduced. Scores fall (0.287 → 0.279) where the paper has a rise.
- **model-response-similarity:** not reproduced. The slopes are positive at Pconn 0.4.
- **model-all-or-none-robust:** now blocked as `methods_underspecified`. The Methods' rule (twice the input strength extrapolated to Pconn 0.44) gives a negative strength here, and the reset pulse is not specified.

All model outcomes rest on choices the paper does not make, marked `assumed`:
- the background PSP size, set to give the stated 0.5 Hz and 10 Hz tonic rates;
- inhibitory PSPs of −1 mV;
- the stimulus amplitude taken as its peak;
- which neurons count as spared.

Calibration reading (a) is adopted. Reading (b)'s best match falls at the weakest input strength tried, and reading (c) (17% of neurons) cannot be reached in this network.

**Data claims:**
- **touch-ablation-size** (problem 2): now partially reproduced. The percentile under the claims file's rank rule is 79.3 ± 27.1, outside tolerance. The code's rule gives the paper's 70.3 ± 35.0, because it scores the top neurons as 1/N; a synthetic check confirms this.
- **whisking-ablation-size:** now partially reproduced. 4.43% is outside 4 ± 0.4, and the rank-rule percentile is 75.4 ± 31.8.
- **per-mouse-table:** now partially reproduced. 23 of 24 rows match under the Methods cylinder; the code's cylinder (24 of 24) is now shown as a variant, and the assumption is dropped.

## Added or corrected
- **Adjusted MAD (problem 7):** the paper's ± values are 1.4826 × the mean absolute deviation, not the median absolute deviation. They now match exactly; recorded as a `code_mismatch` finding.
- **p = 0.042 against 0.031 (problem 11):** the table's own values give 0.042. The difference comes from a rank swap between an278937 and an257220, as the verifier guessed.
- **Trial-type order (problem 3) and touch-property lengths (problem 6):** both are now printed, and both are as the code assumed in all 201 files.
- **an278939 (problem 4):** the notebook now states it enters with 0 neurons. Its files hold only undocumented PSTH matrices, no trial averages.
- **NYU logs (problem 8):** the 510 attempt logs equal the curation files' attempts, so they reconcile with the 279 targets.
- **75-frame averages (problem 9):** all 80 files of the 8 NYU mice, now listed and recorded as a data finding. The 8 neurons with no event rate are never members.
- **Histology check:** the full list of other archive files shows no histology.
- **Questions for a reader:** seven, in `questions/peron-2020.yaml`, covering problems 2 and 10 and the 4% tolerance. Claims, statements, expected values and criteria are unchanged.
- **Round 1 record:** filed under `verifications`, with the verifier's reasons quoted and my replies under `response`.

## Not done
- **Burst merging (problem 5):** still an assumption, as the toolbox method is not public; it stays a question for the authors.
- **Slow input under reading (b):** for the model claims, reading (b) rests on a matching minimum that falls at the edge of the strength sweep. I reported this and did not extend the sweep.
- **an278939's PSTH matrices:** not used to rebuild its trial averages, as nothing documents what they hold.
