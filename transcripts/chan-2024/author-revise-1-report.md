I've revised the chan-2024-01 attempt for verifier round 1. Eight outcomes changed, and the final full run passed with no errors (`entry.py all`, 259 s, peak memory 1.6 GB). Nothing is committed.

## What changed in the outcomes

**Changed to the verifier's outcome:**
- **figs5-blend-oxidation**: not_reproduced → partially_reproduced. The monoterpene drop holds; eucalyptol and the aldoxime still change. The missing reagent-ion trace is recorded as a limitation. The paper's detrend also removes most of the monoterpene drop, so drift and chemistry can't be told apart in this run.
- **fig3b-hyles-no3-eliminates**: not_reproduced → partially_reproduced. Both zero proportions hold; the p < 0.05 part does not.
- **figs8-no3-faster-than-o3**: not_reproduced → partially_reproduced. Area and grid-volume weighting give 3.38–3.39 ppt and 42.4 ppb, still outside tolerance.
- **table-s1-field-conditions**: not_reproduced → partially_reproduced.
- **fig4c-preindustrial-change**: blocked → not_reproduced. The Greenland condition fails under every reading. The land-cell statistic the verifier flagged is replaced by the criterion's city readings.

**Changed by a new analysis (round 2 should review these):** The verifier said "data missing" for the wind was arguable. The MERRA-2 2013 bottom-level winds turn out to be public without a login on GEOS-Chem's data bucket. I read July and January 2013 and averaged them to the model's 2 x 2.5 degree grid. City coordinates come from UN World Urbanization Prospects 2018, pinned via an Internet Archive copy with its SHA-256, because the source Table S13 cites gives no coordinates. Both are recorded as assumptions.
- **fig4ab-no3-shortens-recognition**: blocked → reproduced (assumed). Both parts hold under 2 of 32 readings.
- **table-s13-recognition-distances**: blocked → not_reproduced (assumed). At most 1 of 8 values is within tolerance under any reading.
- **figs9-urban-regressions**: blocked → reproduced (assumed). All parts hold under only 4 of 128 readings, on distances that don't match Table S13.

**Kept, now marked as resting on an assumption:** fig3b-manduca-no3-halves. I ran both floral references. The sheet's 11 of 12 gives a 54% drop; the 0.01x row (10 of 14) gives 41%, p = 0.094, which would fail. I adopted the sheet because it is the paper's own Fig. 3B data and its 54% matches the paper's 50%. With the 0.01x reference, fig3b-o3-no2-no-effect still holds and fig3b-proxy-mixture holds marginally (p = 0.049).

## Added or corrected
- **Outputs the verifier asked for:**
  - the Dryad notebook's Table S9 code printed beside `VOCUS_CODE`, plus the aldoxime test on the 0:300 window;
  - Manduca totals (113 against the paper's 138) and moths per stimulus;
  - the README text on the Fig. S6 workbook;
  - README clock lines, per-hour O3 and NO2 means, and the night window read as UTC (O3 would be 28.3 ppb);
  - the factor-map layout and the Greenland map;
  - the Zenodo GC-MS quantitation files, which hold only a one-level calibration of 1,4-dimethoxybenzene.
- **figs6:** the segment labels now cite the paper's stage order (clean air, then O3, then NO3). The doubling threshold is stated as my own choice and the one that decides the outcome.
- **Detrend formula:** the `m*(t - s)` mixing of seconds and index is the paper's own code, transcribed as written.
- **Findings:** finding 4 now mentions the 113 Manduca against 138. Three new findings are added at the end: the missing time zone in the ozone and CAPS logs (minor), and two questions for the authors (the Fig. 3B reference group; the wind and city coordinates behind Table S13).
- **Verification round:** recorded under `verifications` for all 27 claims. `xlrd` added to the requirements and the lock regenerated. README, `entry.yaml` and the summary updated.

## Not done
- **fig2a:** I didn't compare GC-EAD peak retention times with the Fig. S2 labels. The labels would have to be read off the figure by eye, and one antenna per species can't show a response in most antennae.
- **interannual-similar:** stays blocked; the 2019 and 2021 runs are not deposited.
- **questions/chan-2024.yaml:** no new question, since the verifier reported no place where the claims file misreads the paper.
- **Other changes in the working tree:** `tools/build_site.py`, `tools/runner/chain.sh` and `tools/site_assets/list.js` were already modified when I started, and I left them alone.
