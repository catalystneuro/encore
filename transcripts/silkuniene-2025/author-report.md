I've tested all 28 claims across the four datasets. The entry is in `entries/silkuniene-2025/` and the record is `attempts/silkuniene-2025-04.yaml`. Lock, check and the full run passed (0 errors; the notebook ran in 28 min with 2.75 GB peak memory), and the handover package is built. I did not come across any earlier attempt's results.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig1e-field-simulation, fig2-heating-below-44c | blocked: data_missing |
| fig3a, fig3bc, fig3-lorentzian, fig3-tail, fig4b ×3, fig4c ×2 (9 claims) | blocked: data_missing (001047 holds a 3.8-mm array, not the paper's 15.3-mm array) |
| fig5-raised-electrodes-weaken-centre | partially reproduced (2-mm drop passes the error-bar rule, 1-mm drop does not) |
| fig5-killing-focused-centre | reproduced |
| fig5ab-yp-spot-slightly-larger-than-pr | not reproduced (YP/Pr FWHM ratio 0.74) |
| fig5b-gaussian-pr-lorentzian-yp | reproduced |
| fig5b-reversible-beyond-2mm | reproduced (fit reading 2.08 mm; the data reading gives 3.0 mm) |
| fig5c-nuclear-yp-centre | partially reproduced (no high-resolution images, so the nuclear part is untested) |
| fig6b-peak-900ns-not-significant | reproduced |
| fig6c-normalized-decline-similar | not reproduced |
| fig6d-longer-pulses-sharper-peak | reproduced, assumed |
| fig6d-600-900-differ-from-300 | partially reproduced (900 ns holds, 600 ns does not) |
| fig6d-900ns-fwhm | reproduced (1.69 to 1.77 mm) |
| fig7be-center-linear-with-bursts | reproduced, assumed |
| fig7b-ct26-saturation | partially reproduced |
| fig7cf-fwhm-with-bursts | reproduced, assumed |
| fig7-sharpest-peak-one-burst | reproduced (1.03 to 1.13 mm) |
| fig7-offtarget-40-50-fold | not reproduced (ratios about 13 to 30) |
| fig7-cho-replicates-ct26 | reproduced |

## 2. Dataset, assumptions and questions

**What the datasets hold:**
- **001047:** every file states a 3.8-mm array and a 3.2-kV first pulse. The packet-rate series of Figs. 3–4, the field maps, the heating film images and the Fig. 5C close-up images are in none of the four dandisets.
- **001276:** it also holds 1-Hz and control wells that its description does not mention. These may belong to the Fig. 3–4 series. I show them only as a variant that decides nothing.
- **More wells than the paper reports:**
  - 001284 YP groups have 12, 11 and 11 wells (paper: 6 to 7).
  - 001276 has 5 to 8 CHO wells per group (paper: 4).
  - 001277 has 7 wells labelled 600 ns (paper: 5). Two of them, P1-20240926-B2 and B3, show no central peak.
- **Metadata errors:**
  - Every 001277 file says "9 packets", whatever the pulse duration.
  - Two 001284 Hoechst files say 900 ns in wells whose other files say 600 ns.
  - The "10-mm inter-electrode distance" in the descriptions matches no distance the paper gives.
- **Broken or duplicate files:**
  - One 001284 YP image is almost empty (98% zero pixels).
  - One 001276 Hoechst file holds only zeros.
  - One 001277 file is deposited twice.

**Assumptions:**
- Regressions for Fig. 6D and Fig. 7 use the per-experiment values as points. On group means, several of those outcomes would be partial.
- The Fig. 6 600-ns group is the five wells with a central peak. With all seven wells the Fig. 6D trend is not significant.
- Where the electrode footprints could not be found (about half the wells), the array centre is the centre of the central YP spot, at a fixed rotation. In wells where both are known, the two centres are 0.36 mm apart (median).
- The background is taken from the darkest of the four footprints.

**Questions for the paper's authors** (recorded as methods_unavailable findings):
- Were the regressions fitted to individual experiments or to group means?
- Which wells form the 600-ns group?
- Where were the ROIs placed, and which footprint gave the background?

**Questions to a reader:** none.

## 3. Where the protocol was unclear

1. Some claims name only 001047, but part of their series may sit in 001276. The protocol does not say whether to test a claim on a dataset its `datasets` field does not list. I blocked those claims on 001047 and showed the 001276 wells as a non-deciding variant.
2. Some criteria require a result "under every reading", but readings named in the claims file (here the choice between per-experiment points and group means) give different outcomes. I applied step 1.6: I adopted the better-supported reading as an assumption and showed every reading in the notebook.
3. Some groups hold more wells than the paper, with no rule for choosing. I used all wells, except where the paper's n matched a visible anomaly (the two 600-ns wells). There I adopted that as an assumption and showed both versions.
4. `tools/entry.py` needs pyyaml, jsonschema and nbformat, which the system Python lacked. I ran it with `uv run --no-project --with …`.

## 4. Runtime and failures

- Total about 2 h. The full notebook run took 28 min, mostly streaming about 47 GB of images.
- Nothing failed in the final run.
- Footprint detection is weak on faint or raised-electrode wells; a montage figure in the notebook shows every detection.
