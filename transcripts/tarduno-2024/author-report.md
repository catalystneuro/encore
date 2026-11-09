I wrote the entry, the record and the handover package. The notebook runs in 27 s in a clean environment, `entry.py check` reports 0 errors, and nothing was committed. One claim misses its bar narrowly: the Table 2 fit statistics match 23 of 29 values (79%, the criterion asks for 80%), so it is partially reproduced.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| glass-specimen-set (link) | reproduced |
| glass-success-rate | reproduced |
| table2-fit-statistics | partially reproduced, rests on an assumption (23 of 29 values) |
| table2-no-fit | reproduced |
| fig1-linear-components | reproduced, rests on an assumption |
| fig2-changing-field | reproduced, rests on an assumption |
| glass-directions-not-random | partially reproduced (8 of 22 specimens) |
| glass-af-no-change | reproduced (8 of 10 unchanged) |
| table1-max-intensity | reproduced (24 of 24 values) |
| baseline-range | reproduced (0.200 to 0.500 µT) |
| example-14053g1-threshold | reproduced only under the misprint reading (the numbers are 12040g1's) |
| fig3-nrm-consistent, fig3-590-inconsistent, fig3-alteration-check-inconsistent | reproduced |
| crystal-14053g1-400c-stable | reproduced |
| no-alteration-recording-efficiency | reproduced |
| interpretation-impact-no-dynamo | blocked (`other`): the claims file says it is not tested |

**2. Dataset, assumptions and questions**

What the dataset shows:
- **Synthetic replicates.** In four glass sheets (g2, ss8, ss39, ss48), the rows given as repeated measurements are one row multiplied by factors between 0.95 and 1.03. In three of them the same factor scales moment, declination and inclination; one ss8 declination becomes 361.7°. No other sheet has this pattern.
- **Bad values.**
  - ss19 has an inclination of −136.
  - ss18 has an empty row.
  - ss48 has an extra `CSD` column.
- **Undocumented details.**
  - Glass steps were measured 2 to 19 times, with nothing saying how the repeats were combined.
  - ss6's 250.1 step holds two groups of directions.
  - The lab field varies by sheet (14.4, 15 and 18 µT); the paper states only 18 µT.
- **Paper against data.**
  - The Technical Validation example for 14053g1 uses 12040g1's numbers.
  - Table 2 gives ss36 a pTRM check that is not in its sheet, and gives ss27 six points where the sheet has five.
  - Table 1's maximum intensities match the formula rounded up for 10 of 12 crystals, but rounded normally for only 4.
- **Threshold.** All 37 of the crystals' 590 °C zero-field moments are above the 8e-11 emu threshold the paper uses.
- **Item description.** The file names it lists differ from the actual file names.

Assumption: the repeated measurements of each step are averaged as vectors. With the average, a free-line MAD matches 8 of the 9 printed MADs, 6 of them within 0.3°. With the first measurement only 38% of the Table 2 values match, which would make that claim not reproduced.

Questions for the paper's authors, recorded as a `methods_unavailable` finding:
1. Were repeated measurements averaged?
2. Is MAD a free line fit?
3. How is the pTRM check percentage defined? No single definition I tried matches more than 5 of the 11 printed values.
4. What measure supports "consistent" and "inconsistent" for the crystal replicates?
5. Were the Table 1 maximum intensities rounded up?

Questions to a reader: none.

**3. Where the protocol was unclear or missing something**
1. It gives no outcome for a claim the claims file says is "not tested". I used blocked with `other` and listed the outcomes of the four claims it depends on.
2. How repeated measurements are combined was missing from the claims file and changes the outcome. I followed step 1.6: ran both ways and adopted averaging as an assumption.
3. Counting a value as matched "under any reading" inflates matches when there are many readings: each pTRM value has 4 named readings, 8 counting both ways of combining repeats. The protocol does not address this. I also printed how many values each single reading matches.
4. The example claim's criterion does not say what outcome label to give when only the misprint reading matches. I used `reproduced` under the "any reading" rule of reader step 3, and said so in the notes and a deviation.
5. The clock check in step 2 does not apply to static measurements with no time axis. The notebook says so.
6. The duplicate-recording check of step 1.2 does not cover values made up from one measurement. I adapted it to detect scaled copies, and recorded the result under `other` since no finding kind fits.
7. `tools/entry.py` needs `pyyaml`, `jsonschema` and `nbformat`, which the checkout's Python lacked. I installed them in a temporary environment.

**4. Runtime and failures**
The run took about 17 minutes (19:48 to 20:05 UTC). One notebook cell failed on the first execution (a pTRM-check table with no rows); I fixed it in the helper and nothing else failed.

Files are in `entries/figshare-24639285-tarduno-2024/`:
- `reproduce_tarduno_2024.ipynb`
- `apollo.py`
- `README.md`, `entry.yaml`, and the requirements and lock files

The record is `attempts/figshare-24639285-tarduno-2024-01.yaml`, and the verifier's package is in `executed/figshare-24639285-tarduno-2024/handover/`.
