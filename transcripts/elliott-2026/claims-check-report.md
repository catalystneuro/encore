The checker's result after my edits: `claims/elliott-2026.yaml: 23 claims, 21 quotes, 2 statistical values, 0 problems`. It gave the same result before the edits.

I read the numbers in Extended Data Tables 1 to 3 and the connection counts in Extended Data Fig. 10 from the PDF pages, and they match the file. I also checked the cited code at commit 0f83f70 (seizure windows, Kuiper group thresholds, S1 sub-burst times, simulation levels), and it matches what the file says.

**Changes, by claim**
- **table1-unit-counts:** added the eight recording durations as expected values. The statement and criterion used them, but they were not listed.
- **fig1g-ka-synchronized-bursting:** the expected value was 7 ± 1.8, which gives 5.2 to 8.8. The stated range is 6 to 8 widened by 10%, which is 5.4 to 8.8, so I changed it to 7.1 ± 1.7. The quoted sentence cites Fig. 1h, so I added a second reading: the number of bursts in the first epoch.
- **methods-burst-counts:** added the next sentence of the same paragraph ("For both slices, bursts occurred for roughly 350 seconds") to the quote, the statement and the expected values (S2, 350 s).
- **ext3-onset-spectral-signature:** the Methods' ">2x baseline LFP" does not name a band, but the criterion applied it to theta only. Theta amplitude and 0.1 to 100 Hz amplitude are now both readings.
- **fig1j-theta-propagation-stages:** the statement says the initiation wave runs along the layer's long axis, and nothing tested that; it is now tested. The paper's wording conflicts ("orthogonal" yet "along the granule cell layer from the hilar to outer aspect"). The file now names the conflict and says how it is read.
- **methods-rolling-wave-counts:** the per-burst tolerance gave 1.6 to 4.4, but 2 to 4 widened by 10% is 1.8 to 4.4, so I changed it to 3.1 ± 1.3. Added the S1 fraction: the paper saw the rolling wave in every S1 burst it investigated.
- **table2-phase-locking-counts:** tolerances of 0.1 to 0.8 units contradicted the criterion's rule of rounding small tolerances up to one unit. They are now set to 1.
- **fig2b-phase-cluster-kuiper:** the Results and the Fig. 2b legend say units phase locked "across the entire recording", but the code uses the seizure windows. The whole-recording units are added as a variant.
- **ext12-simulation-recurrence:** the criterion had borrowed the made-up burst definitions from fig1g and required "near zero" bursting at the lowest level, which the paper does not say. It now uses the simulation code's own levels (0, 5, 10 and 30% sprouting) and measures (burst rate, burstiness index).

**Still open (recorded under `checks`)**
- The paper and its code never define bursts, superbursts, stages or rolling waves. The claims that depend on them use readings the file names.
- s4-ka-no-epileptiform claims an absence, but the paper states its test only in words. The LFP part of that test is not tested.
- ext4b-theta-delay borrows the Methods' ±40 ms lag window from the clustering method, so the expected 40 ms lag sits at the edge of the window.
- The simulation code's README credits Andrews, Voitiuk et al. (ref 8), but this paper cites the same directory for Extended Data Fig. 12.
- Extended Data Fig. 7 and Fig. 8e have no claim. Both are supporting panels.

**Ready:** yes. The last check is recorded with `ready: true`. Nothing is committed.
