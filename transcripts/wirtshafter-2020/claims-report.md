I wrote `claims/wirtshafter-2020.yaml`: 31 claims. Every claim has a word-for-word quote, 23 carry the paper's statistics (45 values), 17 have expected values and all 31 have a criterion. Nothing was committed.

**Checker:** all 31 quotes are found in the text. It still exits non-zero on two p-values in the Figure 5 S5 legend, which prints them as "p<9 -13" and "p<9 -10". I recorded them as 9e-13 and 9e-10 and confirmed them by reading the passage.

**Text read:** the version of record (PMC7274787, open access) as flattened JATS text. It has the main text, the Methods and the legends of all 7 figures and their 15 figure supplements. The paper has no other supplement, and no PDF was supplied or needed.

**Code read:** the eLife archived copy, `elifesciences-publications/data_analysis` at commit 5c6320a9 (2020-06-04). The code settles:
- bin sizes (3.5 px per cm)
- the field rule (at least mean + 1 SD; the Methods misprint it as "≤")
- the location boxes for each arm
- how direction of travel is split
- the skew computation and the FRAI formula (the extracted text lost its minus sign)
- how HPC and LS cells are paired and cross-correlated

Where the code and the Methods disagree, the Methods are the main reading and the code is a variant:
- speed smoothing (1 s SD Gaussian against a 30-sample window)
- the minimum rate (0.05 Hz against 0.5 Hz)
- the track-coverage rule (the code's "at least 1950 bins" counts all bins, visited or not)
- whether the shuffle is subtracted in the cross-correlation average (the Methods subtract it; the code's stored average does not)

**Details the paper leaves open, with the readings named:**
- **Full track coverage:** the code's 1950-bin rule, or every arm, the stem and both junctions visited above 12 cm/s.
- **Poisson units:** no script found. A constant-rate Poisson train at the unit's session mean rate, or at its rate above 12 cm/s over fast periods only. The reported df (818) also does not match the sample sizes.
- **Speed and acceleration regression (Fig 3 S1):** no code. Bins from the smoothed or the unsmoothed map.
- **Skew (Fig 5):** the value with its sign flipped for the away direction, or the value in a fixed track orientation.
- **Lap-1 accuracy test:** all fields, or only fields passed at least 15 times.
- **Reward-proximate fields:** with or without the choice-arm ends.
- **Distance to reward:** along the track, or in a straight line.
- **Chi² on field location:** the Results give 6.03 and the legend 12.7. Tested on a 3-location table, or one that includes the junction points.
- **Arm-count t-tests:** CA1 is printed as t(364)=2.34 with p>0.05, which that df does not allow. Tested on all fields, or only those off the junction points.
- **Peak lag:** the Results say the choice arm, the legend says the forced arm. The peak of the mean trace, or the mean of per-pair peak lags.
- **Fig 7 S2 sample:** the df (115) suggests matched-pair LS fields, the alternative is all located LS fields.
- **Shuffle 95% interval:** percentiles, or mean ± 1.96 SD.
- **Field firing rate against distance to reward (Fig 6 S2):** the paper names no test, so the linear regression of Fig 5 S2 is borrowed.
- **"164 HPC units"** is read as a misprint for 124.

**Missing from the paper:** nothing that stops a claim. Some things a claim needed are absent, and each is handled by the readings above:
- no code for the Poisson control or the speed regression
- several garbled or contradictory printed values: the FRAI formula, the p bounds, "2.43e04", the two chi² values, the CA1 t(364)
- the data set's description lists only spike times and "time files", not position data. Every claim needs position, so whether it is in the data set is for the author to find.
