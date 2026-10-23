I checked the claims file and it is ready for an attempt. I also downloaded the paper's code from Zenodo (commit 3bec502) to check the parts of each method that come from the code.

**Checker:** `claims/000931/10.1016-j.celrep.2024.114013.yaml: 37 claims, 37 quotes, 8 statistical values, 0 problems`. I got the same result before and after my edits.

**Changes, by claim:**
- **inhalation-sorting:** the statement said inhalation durations "are bimodal". The paper only says they "appeared bimodal", so I changed it to "appear bimodal".
- **fig1hi-sniff-changes-responses:** the criterion gave two cut-offs for the shuffle test ("exceeds every shuffle, or at least the 95th percentile"). It now uses the 95th percentile, because Figure 1I gives no p-value. Whether the result beats every shuffle is still reported.
- **figs1d-rs-fs-similar:** I added two expected counts from the Figure S1D legend: 440 responses from regular-spiking neurons and 310 from fast-spiking neurons.
- **fig6-simulation-mechanosensory-rescues:** the criterion left out choices that the Methods leave open and the code settles. I added them from the code:
  - only neurons with a significant speed or concentration weight (p ≤ 0.01) are simulated;
  - 100 events are drawn per speed and concentration;
  - the fitted intercept is included, and negative rates are shifted up.

  Simulating all neurons is now a variant.

Everything else that comes from the code matched the scripts.

**Still open (recorded in the file, not settled):**
- Two thresholds are the claims-writer's readings, not numbers from the paper:
  - "unresponsive to odors" after bulbectomy is judged against a 5% false-positive rate;
  - the rise "several tens of milliseconds" before a sniff is read as at least 20 ms.
- Several claims are judged with tests the paper does not report. These are the "similar" claims (regular- vs fast-spiking neurons, the nerve-cut mice, the airflow latencies) and the "mean ± 1 SD" readings of the decoding figures (5B, 5D, 5F, 5H, S1B, 4G). Each is named as a reading in its criterion.
- Figure S3A (cutting the airway stops activity following the breathing rhythm) has no claim. It is a control, and the paper gives no test or number for it.

The paper's main findings each have a claim, and every claim comes from this paper. The check entry is at the end of the file with `ready: true`. Nothing was committed.
