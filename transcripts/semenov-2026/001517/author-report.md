I've finished steps 1 to 5 of the Author section and run the handover; the verifier's package is in `executed/001517-semenov-2026/handover/`. The notebook passes `tools/entry.py all` with 0 errors and runs in about 5.6 minutes; a second full run gave identical numbers. Of the 31 claims, 16 were tested and 15 are blocked because the data are not in the dandiset. Nearly every tested outcome rests on choices the paper and files leave open (listed in section 2). Nothing is committed.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| fig1-pole-dimming | reproduced |
| fig2a-fluovolt-saturation | partially reproduced (shape holds, the two values miss) |
| fig2a-fluovolt-stable | not reproduced (a few small significant changes among 24 tests per reading) |
| fig2b-di8-climbs-to-570 | reproduced (every reading, all 56 five-cell subsets) |
| fig2b-di8-bleaching | reproduced (reading b, −5.11%) |
| fig2b-di8-decline-within-set | reproduced |
| fig3-dye-sensitivity | not reproduced (slopes 21.6 and 7.4 against 26 and 9.1; correlations match) |
| fig3-fluovolt-nonlinear | not reproduced (Di-8 responds less on the cathodic side than the anodic, so it departs from the shared line) |
| fig4a-fluovolt-limits | not reproduced |
| fig4a-fluovolt-cathodic-decline | not reproduced |
| fig4b-di8-limits | not reproduced |
| fig4b-first-10-pulses | not reproduced |
| fig4b-cathodic-asymmetry | partially reproduced (3 of 4 conditions; anodic −18.5% against −30%) |
| fig4c-equator-follows-cosine | not reproduced |
| fig5b-conductivity-calibration | partially reproduced (the 10-fold value is 1.3%, not ~2%) |
| fig7b-charging-during-pulse | reproduced (ratios 1.47 and 2.15) |
| 15 claims on Fig. 2C/D, 4D, 5A, 5C, 6, 7A/C | blocked, data missing |

**2. The dataset, assumptions and questions**

- **Version:** pinned 0.261006.1856, the only published version; the paper cites none.
- **Contents:** 220 sets of 100 raw images (40 baseline, 60 with pulse), 1-µs pulses only:
  - 6 FluoVolt and 8 Di-8-ANEPPS cells with the nine-step escalation;
  - 5 more Di-8-ANEPPS cells (2025-01-22) on other steps that the paper does not describe;
  - no duplicate recordings.
- **Data checks:**
  - The baseline/pulse split at frame 40 is confirmed in 98% of sets.
  - The field axis is the same across sets (median deviation 1.6°).
- **Findings recorded:**
  - Amplitude is given only as generator volts in free text, not the paper's V/cm.
  - No pixel size, field direction or cell outline is stored.
  - The files give an electrode distance of 1.00 mm; the paper says 1.6 mm.
  - The dandiset description says Di-8 replaced FluoVolt, but 68 sets are FluoVolt.
  - Frame 0 of most sets and 290 other frames have no laser flash and are not flagged. Apart from frame 0 they are 5× more frequent during pulses.
  - The paper does not say which cells form its n = 4 and n = 5.
  - Eq. (2) disagrees with the paper's 10-fold "~2%" (paper inconsistency).
- **Assumptions:** each tested outcome except fig5b is marked `assumed`, and every reading is shown in the notebook.
  - Volts are matched in order to the paper's V/cm; the data favour neither scale.
  - Background comes from regions 8–10 µm outside the membrane. Reference [20] says only "near the poles", and nearer regions still carry the membrane's glow. The three readings change dF up to threefold.
  - Pixel size is 0.267 µm, from the camera and objective. With 0.192 µm (which gives the paper's 8 µm mean radius) the Fig. 3 slopes fall within tolerance.
  - FluoVolt uses cells c2, c3, c4, c6; Di-8 uses all 8 cells, with all 56 five-cell subsets reported.
- **Questions for the paper's authors** (recorded as `methods_unavailable` findings): where the background regions were placed; the pixel size and how the radius was measured; which volts correspond to which V/cm; which cells were used.
- **Questions to a reader:** none.

**3. Where the protocol was unclear, wrong or missing something**

1. Choosing among readings when the support comes from the data (the glow profile), not the paper, is not covered. I adopted the 8–10 µm background as an assumption and showed all three readings.
2. An open detail (background) crosses each criterion's own readings, and how to combine them is not stated. I applied each criterion within the adopted background and reported the others.
3. The absence rule ignores multiple comparisons. fig2a-fluovolt-stable makes 24 tests per reading and fails on 2 to 6 small changes. I recorded not_reproduced and noted the chance rate.
4. Nothing covers an unnamed subset of cells (5 of 8). I used all 8 and reported results for all 56 subsets.
5. A sibling dandiset in the same archive (001518 names the paper) is not covered by `elsewhere`. I kept data_missing and did not read its files.
6. The clock-check guidance assumes trial tables or spikes. I tested the 40/60 split by moving the split frame instead.
7. The line between partially and not reproduced is unclear when value conditions fail but the shape holds. I called it partial when most conditions held.
8. Taking a fitted constant from a cited paper is not clearly covered by `inputs` or by entry `related`. I recorded it under `inputs` with its DOI and as `uses_data`.

**4. Runtime and failures**

The run took about 55 minutes (20:44 to about 21:38 UTC), well inside the limit. No claim was blocked for time and nothing failed.

Files are in `entries/001517-semenov-2026/`:
- `reproduce_semenov_2026.ipynb`
- `strobe.py`
- `entry.yaml`
- `README.md`
- `requirements.in`
- `requirements.lock.txt`

The attempt record is `attempts/001517-semenov-2026-01.yaml`.
