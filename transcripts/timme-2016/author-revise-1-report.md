I fixed the verifier's main problem, the significance test that called connections significant on ties, and re-ran everything. One outcome changed and the reasons behind several others changed. The final `python tools/entry.py all` passed with 0 errors in 52.4 min (3141 s), under the 60-minute limit but closer to it than before. A second run gave identical numbers, and I rebuilt the handover. Nothing is committed.

**What changed in the outcomes**
- **fig5ab-correlations-beyond-null:** now partially reproduced (was reproduced). On the corrected networks, 98% of the out-degree correlations are beyond the null but only 88% of the in-degree ones, so one panel of two meets the criterion.
- **fig4ac-te-lognormal:** still partially reproduced. The fits now have R² of 0.88 to 0.96 (was 0.08 to 0.61); three of eight are just under 0.9, all for normalized TE. With bins t-1 and t-2 every fit passes.
- **fig4bd-out-tail-longer:** still reproduced, but full and sub-networks both pass now. It no longer rests on choosing sub-networks; only the strict-rule variant fails.
- **fig7c-degree-modified-rule-matches:** still partially reproduced, for a different reason. The degree rule now matches and is closest, but the firing-rate rule no longer matches.
- **fig6-information-gain-not-rising:** still reproduced, now resting on the gain being normalized. In bits it is partial.
- **No change:** the other eight claims keep their outcome. fig5a is still partial (p = 0.043, so close to the line). fig5cd, fig7d and figs1 are still not reproduced.
- Outcomes that depend on the tie rule are now marked as resting on that assumption.

**What I added or corrected**
- **Tie rule (problem 1):** a surrogate whose TE equals the real TE now counts as exceeding it. The literal strict rule is kept as a variant.
  - On shifted spike trains, where no pair is connected, the strict rule calls 10.8% of pairs significant, against 0.32% for the new rule and the paper's p < 0.001.
  - About 95% of the strict rule's connections had no surrogate above the real TE.
  - The new rule's networks match [44]'s reported network sizes, and degree rises with firing rate as [44] reports.
- **Other readings now run:**
  - Both past-bin readings (t-1, t-2 and t-2, t-3).
  - Sub-networks with groups of fewer than 75 connections redrawn, and the random-75 reading. Four recordings give fewer than 500 sub-networks at 1.6 ms, and the notebook says so.
  - Fig 6 under sub-networks, with the paper's 100 combinations per n.
- **Smaller fixes:**
  - The PID now uses the claims file's redundancy form, with Eq 8 as a variant; no verdict changes.
  - The fig7d check now requires the degree rule to be above the others.
  - The figs1 verdict is printed for every reading and variant.
  - Undefined model correlations set to 0 change no verdict; the MI estimate's bias is printed.
- **Other outputs the verifier asked for:**
  - The approximation check now covers 3.5 ms.
  - Edges per sub-network are printed.
  - The model and PID equations are printed in the notebook.
- **Question for a reader:** `questions/crcns-ssc-3.yaml` asks whether the claims file's redundancy form misreads Eq 8. I did not change the claim.
- **Record:** the attempt record, README and `hdn.py` docstring are updated. Round 1 is recorded under `verifications`, with a new finding asking the paper's authors how ties were counted. The README and record state the runtime as 52 and 55 minutes.

**What I did not do**
- Under the new tie rule the faster approximation agrees less with the full jitter: they share 83% to 89% of connections, against about 96% to 99% under the strict rule. I report this and did not change the approximation.
- The variants use 100 sub-networks and 20 combinations per n, and Fig 6 still samples 30 receivers, all to stay under the time limit.
- I ran the past-bin variant only under the new tie rule; the strict rule is shown only with bins t-2 and t-3.
- I did not add a separate unit test for the tie fix. The shifted-train false-positive check in the notebook serves as the test.
