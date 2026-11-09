I did steps 1 to 5 of the Author section and built the handover. The entry `entries/crcns-fcx-3-johnson-2019/` passes `entry.py all` (0 errors; the notebook runs in 19 min, about 7 GB peak memory), and two full runs gave identical outputs. The record is `attempts/crcns-fcx-3-johnson-2019-01.yaml`. Nothing is committed.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| table1-electrodes | partially reproduced (187 channels, 1135 pairs) |
| trial-counts | reproduced |
| fig1b-accuracy | reproduced |
| fig1b-rt-identity-slower | reproduced |
| erp-no-condition-difference | reproduced, rests on an assumption |
| fig2-spatial-power | partially reproduced (counts 5 and 2 match; percentages low) |
| fig3-temporal-power | partially reproduced |
| power-difficulty-subjects | reproduced |
| power-low-frequencies | reproduced, rests on an assumption |
| fig4-maintenance-parietal-led | not reproduced |
| fig4a-delta-theta-shift | partially reproduced |
| fig4c-alpha-beta-shift | not reproduced |
| directional-pairs | reproduced (1014 and 1043 against 1008 and 984) |
| fig5a-delta-theta-epochs | not reproduced |
| fig5a-identity-direction | not reproduced |
| fig5a-spatiotemporal-bidirectional | not reproduced, rests on an assumption |
| fig5b-alpha-beta-no-sustained | reproduced, rests on an assumption |

**2. Dataset, assumptions and questions**

What the dataset shows:
- **Version.** It is pinned as `unversioned` with the DOI; the notebook header prints the MD5 sums. Only `live/` exists in the bucket.
- **Epochs and clock.** The derived epochs are bipolar differences of the continuous data (r ≥ 0.9998). They sit at fixed offsets from the trial table, which puts the deposited scripts' windows where the Methods put them.
- **Channels.** The channel list has 187 analysed channels, not 192: S4 has 5 parietal channels where Table 1 has 10. The list gives 1135 pairs, not 1129.
- **Trial tables.** In S6 and S7 they hold only the kept trials (101 and 90 rows), not all 120.
- **Timing.** In S2, S3 and S4, responses in the 1150-ms-delay trials come about 0.25 s later relative to the processing column than in the 900-ms trials. This is consistent with those columns being early, but the test does not prove it.
- **Deposited code.**
  - `psianalysis.m` omits the conjugate of the cross-spectrum, so its sign follows the channel order.
  - `psi_compute.m` does not run as written.
  - `subtracterp.m` selects temporal trials by the delay column, which selects none.

Assumptions:
- **Cluster neighbours** (ERP claim): adopted contacts adjacent on the same lead, judged at 0.05 per tail.
- **Electrode positions** (power-low-frequencies): matches only under the distance reading of neighbours, which assumes how numbered contacts sit on the grids.
- **PSI computed per trial** (the code's structure), adopted for the two claims of absence. It is the only reading that gives the paper's directional-pair counts.

Two questions for the paper's authors are recorded as `methods_unavailable` findings: which electrodes were neighbours and the per-tail alpha, and how PSI was computed.

I asked no reader any question.

**3. Where the protocol was unclear**
1. **Analysis code inside the dataset.** The scripts are among the dataset's files, so the reader never read them, and it is unclear whether they count as an outside input. I took details from them, cited by file name, and did not list them under `inputs`.
2. **Code that disagrees with the Methods and cannot run as written.** The order "Methods, then code" does not say what to do when the code is also buggy. I ran the Methods' readings with the conjugate fixed, and the deposited code as a variant.
3. **Claims of absence with several readings.** Absence is judged "on the paper's test alone", but the paper's test is itself underspecified. I applied step 1.6: adopted one reading as an assumption and showed the others.
4. **Clock check.** CRCNS data come pre-epoched in tar.gz files, which the decoding suggestion does not fit. I matched the derived epochs to the continuous data and added a delay-jitter contrast on high-frequency amplitude.
5. **Streaming.** tar.gz files cannot be opened in place the way docs/archives.md describes for zip. I streamed each file sequentially, with decompression in memory.

**4. Runtime and failures**

The run took about 2 h 5 min (19:11 to 21:13 UTC); the notebook takes 19 min per run. My first loader failed on S4's unequal trial lengths and on S3's labels file, which is in MATLAB 5 format; both are fixed. A first timing check based on low-frequency signals did not work and was replaced. Nothing is blocked.
