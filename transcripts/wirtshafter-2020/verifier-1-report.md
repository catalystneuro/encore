**Verifier report, round 1: Wirtshafter & Wilson 2020 on CRCNS hc-29**

The claims file lists 31 claims. The notebook marks all 31 blocked (data_missing). I agree for 30 of them. For `units-recorded` I give partially_reproduced, because the half of it that can be tested matches exactly.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| units-recorded | partially_reproduced (rest blocked: data_missing) | Cell 16 counts 452 LS and 178 HPC clusters from 6 rats, which equals the paper's numbers exactly; 410 LS trains are distinct, still within ±45. The other two counts (165 CA1 and 378 LS cells meeting the rate and coverage criteria) need speed and track coverage, and neither reading in the criterion can be computed without position. |
| fig2ab-fraction-spatial | blocked: data_missing | Bits/spike needs rate maps above 12 cm/s, which need position. There is no position, speed or behaviour variable in any file (cell 11; my bucket listing). |
| fig2c-bits-per-spike | blocked: data_missing | Same: rate maps. |
| fig2b-poisson-control | blocked: data_missing | The artificial units' bits/spike also needs occupancy maps, under every reading in the criterion. |
| fig2s1-mutual-information | blocked: data_missing | Rate maps. |
| fig2f-bits-per-second | blocked: data_missing | Rate maps. |
| fig3ab-field-counts | blocked: data_missing | Place fields. |
| fig3-field-number-distribution | blocked: data_missing | Place fields. |
| fig3s1-speed-acceleration | blocked: data_missing | Speed and acceleration per spatial bin. |
| place-cell-abundance | blocked: data_missing | Place fields and the coverage rule. |
| fig4ab-field-length | blocked: data_missing | Place fields. |
| fig4ef-lap-accuracy-change | blocked: data_missing | Laps and passes through fields. |
| fig4ef-hpc-more-accurate | blocked: data_missing | Laps. |
| fig4gh-firing-increases | blocked: data_missing | Laps. |
| fig5abc-skew-direction | blocked: data_missing | Direction of travel and field profiles. |
| fig5s4-uni-bidirectional | blocked: data_missing | Directional fields. |
| fig5s5-skew-frai | blocked: data_missing | Directional fields. |
| fig5e-reward-proximate-skew | blocked: data_missing | Directional fields and maze location. |
| fig5s2-skew-distance | blocked: data_missing | Distance to reward. |
| fig6-location-counts | blocked: data_missing | Field centres on the maze. |
| fig6de-choice-side-bias | blocked: data_missing | Field centres. |
| fig6-direction-split | blocked: data_missing | Directional fields. |
| fig6g-ls-choice-by-direction | blocked: data_missing | Directional fields and location. |
| fig6s2-rate-not-distance | blocked: data_missing | Distance to reward. |
| fig6hi-probability-distance | blocked: data_missing | Field bins and distance. |
| fig7a-crosscorr-choice | blocked: data_missing | CA1–LS pairs are matched by field centre and located by it. Cross-correlating all pairs would not be the claim. |
| fig7b-lag | blocked: data_missing | Needs the matched pairs. |
| fig7s2-ls-rates-by-location | blocked: data_missing | LS fields located on the maze. |
| fig7s3-pair-distance-control | blocked: data_missing | Matched pairs and field centres. |
| fig7s1-above-shuffle | blocked: data_missing | Forced-arm matched pairs. |
| fig7c-thirds | blocked: data_missing | Matched pairs by location. |

**Archive check.** I listed the S3 bucket myself. It has 12 keys: three .mat files, `spiketrain.m`, the docs, `filelist.txt` and `checksums.md5`. That matches cell 3 and `filelist.txt`. `spiketrain.m` describes its time input as `lfp.timestamp`, and Times.mat is sampled at 0.512 or 3.2 ms, not the paper's ~30 Hz camera rate. So Times.mat is an electrophysiology time base, not tracking data. The paper's Data availability statement names only hc-29 and the code repository. No chance levels apply to any claim.

### B. Problems

1. [affects a conclusion] Cell 0 and `units-recorded`: the whole claim is labelled blocked, although half of it was tested and matches exactly (452 / 178 / 6 rats, cell 16). A label of partially_reproduced, with the inclusion counts blocked, would describe the result more accurately.
2. [does not affect a conclusion] Cell 16: the 452 is a count of deposited LS entries, not units. It includes 42 extra copies of identical trains (one rat-7 train filed under 18 names and another under 25, spread across recordings and tetrodes, plus one rat-6 pair) and a `MUA9` multi-unit cluster. Cell 13 also finds cross-tetrode pairs that look like the same unit sorted twice. The notebook reports all of this, and 410 distinct trains is still within tolerance.
3. [does not affect a conclusion] Cell 16: `rate_hz` is computed over the whole recording. For rats 10 and 12 that spans 3.8–6.4 h, far more than the 30 min session (cell 9). It is labelled a variant that decides nothing, which is correct.
4. [does not affect a conclusion] Cell 18: the check "listed with a need: 31" is circular. Every claim gets a default "needs" string, so it would print 31 whatever the need table holds. It does not show that each claim was actually checked.
5. [does not affect a conclusion] Cell 6: CA1 clusters come from only 2 of the 6 rats (rats 10 and 12). The paper reads as if every rat had a CA1 array. The notebook notes this but does not draw out that HPC/LS comparisons would mix rats unevenly.
6. Helper module `hc29.py`: I tested the name-parsing regexes on synthetic and real-form names (`_cl1`, `run_1`, `maze_and_sleep`, `MUA9`) and they parse correctly. I read `coincident_fraction` and its logic is sound, but I could not run it because there is no numpy here.

### C. What I could not check

- **The paper's GitHub repository.** The notebook (cell 12) and the claims file say it holds no position data, but it is not among my materials. An output listing the repository's non-code files, with their sizes, would confirm that no tracking files are hidden there.
- **The 30 min maze window.** Nothing in the data marks which part of each recording is the maze session. An output scanning each recording for long stretches with no spikes, or using the sampling-rate changes as candidate epoch boundaries, would show whether a session window could even be identified.
- **The middle of Times.mat.** Only the first and last 8000 samples of each recording were examined. The span check makes gaps unlikely, but an output of the full sample-interval distribution for one recording would rule out embedded event codes.
- **Numerical helpers.** `coincident_fraction` and `duplicate_pairs` were not run on synthetic inputs, because numpy is unavailable in this environment.
