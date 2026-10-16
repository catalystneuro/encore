I did steps 1 to 6 of the protocol for dandiset 000070 and the entry runs cleanly. The paper's full text is open access: I used the NIH author manuscript (PMC3393826) and the Supplementary Information PDF from Nature, saved under `paper/`. I pinned version 0.260528.0919. The paper cites no version, and both published versions hold the same 10 files (same blobs and sizes), differing only in metadata. Nothing is committed.

**1. Outcome per claim**

| Claim | Outcome |
|---|---|
| array-dataset-composition (108 conditions; 146 and 218 isolations) | partially reproduced |
| fig3ef-same-direction | reproduced (94.4% and 100% of conditions rotate the same way) |
| fig3-independent-of-curvature | partially reproduced |
| fig3-phase-from-prep-state | partially reproduced |
| var-captured-jpc-plane | reproduced (20.0% and 23.1%; mean 21.6% against 28%) |
| pc23-variance | partially reproduced |
| suppfig4-j-array-planes | not reproduced (40% against 54%) |
| suppfig4-planes-range | partially reproduced |
| fig6a-angle-peak | reproduced |
| fig6b-skew-fit | reproduced (6-D ratio 0.905 and 0.845) |
| rotation-frequency | partially reproduced |
| suppfig3-shuffle-controls | not reproduced (shuffle 1 removes the rotations; shuffles 2 and 3 do not by the chosen measure) |
| suppfig5-areas-variance | partially reproduced |
| suppfig5-m1-faster | reproduced |
| fig6-velocity-model | not reproduced (poor rotational fit holds; the angle peak is not near 0) |
| fig6-complex-kinematic-model | not reproduced (same pattern) |
| Six claims: leech and walking monkey, single-electrode datasets (2), EMG, generator model, speed task | blocked: data_missing |

Totals: 5 reproduced, 7 partially, 4 not reproduced, 6 blocked.

**2. What was found about the dandiset**
- **Coverage:** it holds the paper's two array datasets (J 2009-09-18, N 2010-09-23) plus 8 array sessions the paper does not describe. Its units are 192 per file, one per electrode. The paper's sorted isolations (146 and 218) are not there, and the Units table does not say what a unit is.
- **Wrapped index:** in 9 of 10 files the first entry of `spike_times_index` wrapped at 65536. Unit 0 is cut short (61030 of 257638 spikes in J-array) and the rest of its spikes open unit 1. The loader corrects this.
- **Clock restarts:** in 5 Nitschke files, N-array among them, the clock restarts at each recording segment after the first. Trials overlap in time (2094 overlapping pairs in N-array) and spike times are unsorted. The loader places spikes in trials by their storage order, and a decoding check shows this is right in every clock segment.
- **Hand position:** it is labelled metres but the values are in mm. It is also offset 35 to 53 mm in y from the target, which the files do not describe; the cursor lands on the target.
- **Dates:** the conversion code writes the year 2009 into every session date. `ses-20090910` has the same reached target as the 2010 N-array session for all 108 conditions. So it is probably the "N-9-10-2010" dataset of Supplementary Figure 5, dated a year early, but this is not proven.

**3. Points where the protocol was unclear, wrong or missing something**
1. **Figure-only values:** some criteria needed values that appear only in figures (Figure 6a/b). Step 7 asks for reported numbers. I read thresholds off the figure and said so in the claims file.
2. **Code the paper does not link:** the lab's jPCA download page returned HTTP 403. I used the Python port at a pinned commit and recorded it, together with the conversion code, under `inputs` as code read, with no data. The protocol does not say whether code read for method choices belongs in `inputs`.
3. **Simulated control populations:** the paper's velocity and kinematic models are simulations built from the data, and the protocol has no category for that. I kept them `data: dandiset` and fixed the free choices (a 100 ms lead and others) in the helper before running. Both models then failed on the angle part of the criterion. Under the protocol's rules this is `not_reproduced`, not `methods_underspecified`, though the outcome depends on those choices.
4. **Averages over datasets not deposited:** some reported numbers are averages over 9 datasets of which the dandiset has 2. I handled this with listed readings (mean of two, or each against the stated range).
5. **Faults the loader corrects:** the protocol says to trust the data and record findings, but not whether an analysis may repair a format error. I corrected both faults in the helper, showed the corrections in the data check, and recorded them as `format_error`.
6. **Extra session for a variant:** Supplementary Figure 5 uses a dataset that may be in the dandiset under the wrong date. I used it only as a variant, because the link to that dataset cannot be shown.

**4. Runtime and failures**
- The notebook runs in about 4 minutes (245 s under `tools/entry.py all`), and `check` reports 0 errors.
- The locked run matches the run the conclusions were written from, and two runs gave identical numbers.
- Reading spike times through remfile took 251 s per file. The helper reads the stored bytes directly with parallel range requests (5 s), and checks the result against h5py.
- The Supplementary Information was not reachable from PMC (bot page). I took it from the publisher's site.
- The handover is in `executed/000070-churchland-2012/handover/`.
- The repo root has untracked files I did not create (`.bashrc`, `.gitconfig`, `.idea`, `.vscode`, `scripts`, and others). I left them alone.
