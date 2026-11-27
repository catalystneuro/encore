**Verifier report, round 2: chan-2024-01**

The claims file has 27 claims and the attempt record has 27 outcomes, one per claim. Cell numbers below count from 0 in the re-executed notebook. The cell numbers quoted from my round-1 reasons refer to the round-1 notebook; for example, my "cell 31" for figs5 is now cell 36.

## 1. Outcomes

I agree with 25 of the 27 outcomes. All 20 that did not change in round 2 are the same as I gave them in round 1. Of the round-2 changes, I agree with fig4c-preindustrial-change and table-s13-recognition-distances, and I disagree with fig4ab-no3-shortens-recognition and figs9-urban-regressions, as explained below.

Seven outcomes are marked `assumed: true`. Each states its assumption in its deviations or notes.

- **figs6-oxidation-products** (partially reproduced): reasonable. The deciding doubling threshold (r3) is now stated as this attempt's own choice. On the segment assignment: the Methods' order (clean air, O3, NO3) is the order of stages within one run. The workbook holds two separate runs, each with its own clean-air baseline (cell 40: 9 and 7 rows before onset). So the Methods' order does not settle which run is which. The chemistry does, since organic nitrates need NO3, and that argument supports the same assignment.
- **fig3b-manduca-no3-halves** (reproduced): reasonable, because the sheet is the paper's own Fig. 3B file. One of the two stated reasons ("54% matches the paper's 50%") picks the reading by its result. Neither floral reference gives the paper's p = 0.047 (cell 46).
- **fig3b-proxy-mixture** (reproduced): reasonable. The claim holds with either floral reference under the z-test, marginally with the 0.01x row (p = 0.049, cell 46).
- **table-s13-recognition-distances** (not reproduced): I agree, and the outcome does not depend on the assumed wind. The three percentages need no wind, and they fail under every reading (cell 65): Hong Kong 0–2.2% against 4.9, Tokyo 0–2.7% against 6.7, Kinshasa 52–76% against 89.8. Even if all five distances matched, only 5 of 8 values could pass, short of the 6 needed for partial. The record could say this.
- **fig4c-preindustrial-change** (not reproduced): I agree. The Greenland condition needs neither wind nor city coordinates. In cell 69 the Greenland median is 34–66% and at most 0.4% of cells are above 75%. The Greenland box is a stated and reasonable choice.
- **fig4ab-no3-shortens-recognition** (reproduced): I disagree. I would rate it partially reproduced.
  - The "more severe" part holds under every NO3-and-O3 reading, with share 1.0 in cell 67. It does not depend on wind.
  - The "below 400 m in many populated areas" part holds only with the speed of the mean wind vector (x), in 2 of 32 readings.
  - Under those same two readings, Table S13's distances are matched for 0 and 1 of 8 values (cell 65). Santiago comes out at 634 and 2122 m against 101.8. The dependency, table-s13, is not reproduced.
  - The count of 8 or 10 cities is therefore a count of recomputed cities that only partly overlap the paper's nine. London, Delhi, Los Angeles, Rome and Beijing appear on the recomputed lists.
  - The vector speed goes as low as 0.05 m/s (cell 63), where wind directions cancel. The paper's "mean horizontal wind speed" reads more naturally as reading (y), the monthly mean speed, and under (y) the count is 0 or 1.
- **figs9-urban-regressions** (reproduced): I would not accept this outcome as it stands.
  - It holds in 4 of 128 readings, all using the monthly mean speed (y). fig4ab holds only under the vector wind (x), so no single wind reading supports both claims.
  - Under the deciding readings, Kabul comes out at 762–973 m against Table S13's 73.1 (cell 65).
  - The criterion runs the regressions "on the Table S13 rows". The paper prints population, distance and percentage for all 97 cities (paper text, Table S13; I parsed 97 rows). The paper's own rows are the natural deciding test, and they need no assumed wind. They were not run.

## 2. Statements the outputs do not support

All other "**Result:" sentences, the Summary (cell 80) and the record's notes agree with the printed values I checked. These do not:

- **Cell 39** still contains the round-1 sentence "because only in the second do the nitrates rise many-fold (an assumption from the data and Fig. S6A/B, recorded)". It is followed by the new paragraph that gives the Methods' stage order as the reason. The two disagree, and the record's deviation gives only the second.
- **Findings 2 and 15 (from 1)** each state more than their cells print.
  - Finding 2 says "only the 1e-6 value differs". Cell 10 prints only the eight identical values, not the two 1e-6 values.
  - Finding 15 says "Kabul 105 to 155 m against 73.1 with the vector wind". That range holds only for the containing cell. With the vector wind and threshold (a), cell 65 gives 105–335 m.
- **Finding 9** cites `sanity` (cell 7) for "a night temperature of 22.7 C". That value is printed in cell 75, not cell 7.
- **README** outcome table:
  - "Recognition distances around cities (Table S13) | Not reproduced" and "75% or more decrease … | Not reproduced" leave out "(assumed)". The record and the Summary mark both as assumed.
  - The proxy-mixture claim is `assumed: true` in the record but is not marked assumed in the README row.

The record's verification entries give my round-1 reasons in my own words. For several claims (figs5, figs6, fig3b-manduca, fig4ab, fig4c, figs8, table-s1) it folds in text from my numbered problems, and that text is accurate.

## 3. Round-1 points

All my round-1 points are resolved:

- **1:** Both floral references are run (cell 46), and the totals of 113 and 138 are printed (cell 12).
- **2:** fig4c is now not reproduced, on the city readings (cell 69).
- **3:** The percentages and regression B are computed.
- **4:** The MERRA-2 wind is used.
- **5:** The doubling threshold is stated as the deciding assumption, and the 5-against-9 points are given (cell 41). The stage-order argument is cited, with the caveat in section 1.
- **6:** The missing reagent-ion trace is recorded as a limitation, with detrended and block-mean variants (cell 36).
- **7:** The Dryad notebook's cells are printed beside `VOCUS_CODE` and match (cell 28).
- **8:** The time zone is checked (cell 75).
- **9:** The weighted means are run (cell 60).
- **C list:** Done, except the fig2a retention-time comparison. The record explains why that was skipped, and the reason is acceptable.

What remains that bears on a conclusion:

1. **fig4ab:** It should be partially reproduced (section 1). Its 400 m part rests on readings under which Table S13 is not matched.
2. **figs9:** The regressions should be run on Table S13's printed rows as the deciding test. As it stands, "reproduced" rests on distances an order of magnitude from the paper's.
3. **finding-fig3b-control-is-1x:** The deciding Manduca reference may be 1x data filed as the 1/100 control. That would be data under the wrong label. The finding is filed `about: paper` with no severity, so it should be given one.
4. **Text fixes, which do not change an outcome:** the cell 39 contradiction, the README's missing "(assumed)" markers, and the imprecise wording in findings 2, 9 and 15.

## 4. Critical findings

One finding in the record is rated `critical`: number 2, `finding-eag-duplicated-series`.

- **The output shows it.** Cell 10 prints Hyles rows 12–19 and 21–28: eight identical values, "identical: True". The search for runs of eight finds only (12, 21) in the Hyles column and none in the Manduca column. The one point the output does not show is "only the 1e-6 value differs", as noted in section 2.
- **The rating is right.** One antenna's dose series appears to be deposited as two antennae, and nothing in the file marks it, so any per-antenna analysis takes it as given. In this attempt the effect is small: cell 50 shows that dropping the series lowers Hyles means slightly, e.g. 25.35 to 24.71 mV at 1e-3, and leaves the outcome unchanged.
- The finding gives no `versions` or `fixed_in`.
