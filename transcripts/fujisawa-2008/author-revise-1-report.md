I've worked through every point in the round-1 report and re-run the entry. The final run passed in 42 min with 10.0 GB peak memory, and `entry.py check` reports 0 errors. Nothing is committed.

## Outcomes
- **population-vector-width** changed from not reproduced to **partially reproduced**, still marked as resting on an assumption. This is the verifier's outcome. With each neuron's rate normalised to its peak, layer 5 is within tolerance and layer 2/3 is 0.268 against a limit of 0.267.
- **central-arm-selectivity** stays partially reproduced but is now marked as resting on the unit list. If every NWB unit is counted, both values fall within tolerance under one rat reading.
- **fig2c-active-fraction** stays partially reproduced. The verifier says not reproduced; I kept partial because one of the two values, the layer difference and the constancy hold. The disagreement is recorded under `verifications`.
- **No other outcome changed.** The new outcomes are 5 reproduced, 12 partially reproduced, 15 not reproduced and 1 blocked; 8 rest on an assumption.

## Fixes and added output, by report point
- **B1, unit lists.** I compared the lab's cell lists with `spikeph` and the NWB units. The files have no "Cells" variable. The lab's lists look like the description's 1 Hz list: 98.9% of listed units reach 1 Hz in the trials, against 28.7% of those left out. I kept them as the paper's units, stated as an assumption, because they total 627 against the paper's 633, while every NWB unit totals 1,373. That larger list is now run as a variant for the unit-count, fraction, active-fraction and rate claims. No rat has 222 units and no session has 142 units in either list. A new finding records that the lab's lists are undocumented.
- **B2, peak positions.** Peaks now use both rate readings. Results are unchanged.
- **B3 and B4, facilitation and depression.**
  - The test now jitters both cells with 1,000 surrogates, as the claims file says.
  - A pair is called depressing or facilitating by which tail of the permutation distribution it falls in, citing the Figure 6c legend. This matters because the distribution is above 0 in 76% of tests.
  - Facilitation is now above the 5% null level in every combination, depression in none, so fig6 stays not reproduced and fig6b stays partial.
  - The claims file's literal wording ("first above later") is now a question for a reader in the new `questions/fujisawa-2008.yaml`.
- **B6, head direction.** The LED axis points along the direction of movement. The early difference at 0.02 is the turn out of the start box, not a wrap artefact. A second significant run starts at 0.23, but the criterion takes the first position.
- **B7, troughs.** 58 of the 112 inhibitory connections share a pair with an excitatory peak, so many troughs may come from the peak itself. Example cross-correlograms are printed.
- **B8, one-cell jitter.** This variant finds more connections, not fewer, so it does not explain the excess.
- **B9.** The counting bug is fixed; the values are unchanged.
- **B10.** The conclusion now notes that the FF files label their channels like rat EE's and the GG files label them "neural".
- **B11, clock check.** A binomial test now names EE049, FF103, GG097 and GG149 as sessions where this check does not establish a shared clock.
- **Other requested output.** I added positions at trial edges and the whl trial-number ranges (no gaps). I also added the global band index of the left-right tests: median pointwise-equivalent level 0.20%, against the paper's example of 0.6%.
- **A correction to my own round-1 finding.** The frames with position above zero outside trials are the trials' own nose-poke periods, not unlisted runs. The finding is rewritten.

## Not done
- Of the verifier's "not checked" list, I added everything except the error-trial count from the poke sensors. The criterion blocks task performance whenever only correct trials are listed, so that count could not change the outcome.
- `entry.yaml` gives a runtime of 40 minutes against the 42 measured. Changing it would have forced another full run.
