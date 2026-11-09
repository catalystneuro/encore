I worked through every point in the round-1 report, re-ran the entry with `python tools/entry.py all`, and checks report 0 errors. The notebook runs in about 6.3 minutes and gave the same numbers on two runs. Nothing is committed.

**Outcomes changed (both now match the verifier's):**
- **fig4b-connectome-motifs**: reproduced → partially_reproduced. The criterion needs both sorts, and reading (b) can't be built because the hemibrain neuron names give only the protocerebral bridge glomerulus. It stays marked as resting on an assumption.
- **figs2-performance-independent-of-n**: partially_reproduced → not_reproduced. Both readings fail and the criterion needs both. The new Monte Carlo error estimate shows the one failing value (N = 16 at 0.1/s, 0.041 below the reference) is real. It is 4.3 standard errors of a difference, and no other value is beyond 3.

The other 11 outcomes are unchanged, and the verifier agreed with all of them.

**Added or corrected:**
- **Released code:** a data-check cell prints the lines of the paper's code that define what the verifier could not check:
  - `kappa_z = 15` is commented "called gamma_z in manuscript".
  - The columns of the `*_stats` arrays.
  - The axes of the Figure 3 grids.
  - The number of runs per scan (10,000).
- **Monte Carlo error:** each simulated accuracy averages 10,000 runs, and from that I estimated its standard error.
  - fig3d: the two rises that break condition 4 are 0.32 and 0.52 standard errors, so they are within sampling error. The outcome stays partial because the criterion gives no tolerance.
  - fig4gh: the differences above 0.01 are 1.16 to 1.95 standard errors, close to the sampling error. The outcome stays partial for the same reason.
- **Noise claim:** in the full network the noise raises the global inhibition (from 0.5 to between 0.57 and 0.76 at 1 s), which shrinks the bump. With the inhibition held at its noise-free level, the bump amplitude rises to 1.01–1.33. That is within 1.5 standard errors of what the paper's SI Eq. S124 predicts.
  - The outcome stays partially_reproduced, because the criterion tests the full network.
  - I added a question to `questions/000289.yaml` asking a reader whether it should test only the noise's direct effect, as the SI derivation does.
  - The finding about the released code now names this cause.
- **Prediction claim:** I ran 18 variants of the raw-fluorescence signal (smoothing, baseline percentile, with and without dividing by the baseline). The test passes (p < 0.05) in all 9 variants that don't divide by the baseline and in none of the 9 that do. So the split between readings comes from that division, and the claim stays blocked.
- **Smaller fixes:**
  - The header no longer says "No claim is blocked".
  - The missing value in the Fig. S2 data (N = 128 at 100/s) is now printed.
  - The fig1 notes say that comparison (a) is a weak test.
  - The bump decoder's reversed phase sign is documented as a convention; amplitude, the only thing the prediction uses, doesn't depend on it.
  - README, summary and `runtime_minutes` are updated.
- **Attempt record:** the `verifications` round is recorded, with the verifier's reasons and my response for each claim.

**Not done:** I did not re-run the paper's large simulation scans, which are beyond the time limit; the error estimates come from the stored results instead. The hemibrain v1.2.1 release (the version the paper cites) still needs a personal token, so the connectome remains the public v1.2 export.
