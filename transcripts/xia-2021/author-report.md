The entry for xia-2021 is done. Of the 29 claims, 9 were tested and 20 are blocked. `python tools/entry.py all` passes (0 errors, notebook runs in 74 s) and the verifier's package is built in `executed/xia-2021/handover/`. Nothing is committed: the new files are `entries/xia-2021/` and `attempts/xia-2021-01.yaml`.

**1. Outcome per claim**

| Claim | Outcome |
|---|---|
| fig2d-hplc-yield | not reproduced: main peak is 66.6% of the pHAb area (tolerance 69.3–84.7%); retention volumes match at an assumed 0.5 mL/min |
| fig2e-page-bands | reproduced |
| figs5-btx-staining | reproduced (judged by eye, with supporting numbers; SPARC:75) |
| fig3d-sensor-on-soma | partially reproduced, rests on an assumption: overlapping spots are visible, but neither the overlap nor the position on somata is above chance (a 5 µm shift of the pHAb mask leaves the overlap at 78–98%) |
| fig4b-michaelis-menten | not reproduced, rests on an assumption: Km 0.03–0.73 µM against 49 µM, under all 80 readings (one mouse of three) |
| fig4b-lod | not reproduced, rests on an assumption: none of 160 crossings near 228 nM |
| fig5b-in-vivo-response | not reproduced, rests on an assumption: dF/F 17–37% against 3.7%, on two 3 V recordings |
| fig6-vesamicol | partially reproduced, rests on an assumption: one experiment of four; reduction 70–89%; the example's 17% ratio is matched in 24 of 48 readings |
| figs16-af647-stable | reproduced, resting on which half of the frame is AF647 |
| figs6a-response-time | blocked: metadata insufficient (the time ACh was added is not recorded) |
| fig2g, figs3, fig3bc, figs4, figs6b, fig4c, fig5b-control, figs8, fig5c-voltage-dose, fig5c-ach-concentration, fig5d, fig5e, figs7b, figs10, figs13 | blocked: data missing |
| figs9, fig7-rostral-caudal, fig7-peak-timing, figs12 | blocked: not runnable (AQuA is MATLAB, and the paper gives no parameters) |

**2. Dataset, assumptions and questions**

- **Versions:** both datasets have only version 1, and the paper cites version 1 of SPARC:108, so version 1 of each is pinned.
- **What SPARC:108 holds:** only part of the paper's data. It has:
  - 1 of the 3 calibration mice;
  - 1 of the 4 vesamicol experiments;
  - the 3 V and 8 V recordings of one ganglion, listed as two subjects (sub-2 and sub-3);
  - one 10 V recording with a single stimulation.

  It has no control nanosensor, pH, 5 V, pulse-number, AFM, two-photon or fiber data.
- **Metadata problems in SPARC:108:**
  - The primary `manifest.xlsx` uses names that don't match 40 of the 50 files, and seven of the eight calibration files lack the `.tif` extension.
  - The recordings have no channel labels, spatial scale, or stimulation or ACh-addition times.
  - The frame timestamps say 0.50 s, where the paper says 0.55 s.
  - 69% of the tissue pixels saturate at some frame in the washout recording that the vesamicol ratio uses.
  - It names the bioRxiv preprint, not the PNAS paper, as its source article.
- **SPARC:75:** the high-magnification BTX stack has data in only 12 of its 62 planes; the other 50 are empty.
- **Paper inconsistency:** Figure S2C labels gel lane 1 as unpurified nanosensor, but the gel itself fits Figure 2E's label (DNA scaffold).
- **Assumptions I made:**
  - Stimulation starts at 10.45 s (frame 19), taken from Fig. 6A and 7A.
  - In the calibration recordings, ACh was added just before the largest one-frame rise.
  - The HPLC flow rate is 0.5 mL/min.
  - In the dual-channel frames, the left half is AF647 and the right half pHAb.
  - The deposited recordings stand for the paper's Fig. 5B mice and Fig. 6 example.
- **Questions for the paper's authors** (recorded as a `methods_unavailable` finding):
  - Which frames, onset and baseline give the initial rate?
  - Which ROIs were used, and which recordings are the Fig. 5B mice?
  - Is the frame interval 0.55 s or 0.50 s?
  - What was the HPLC flow rate, and how were the overlapping peaks integrated?
  - Which frames was the photobleaching curve fit to?
  - Which AQuA version and parameters were used?
- **Questions to a reader:** none.

**3. Where the protocol was unclear or didn't fit**

1. The protocol doesn't say what to record under `measured` when no reading matches. I recorded the first reading.
2. Claims judged "by eye" sit awkwardly with the rule that every Result sentence must rest on a printed number. I printed counts alongside chance references (shifted masks, the share of the field a mask covers).
3. The clock check assumes event times exist; here none are recorded. I checked that each response starts after the paper's stated onset, and reported this as consistent, not shown.
4. The protocol doesn't say whether a claim whose data are only partly deposited (1 of 3 mice, 1 of 4 experiments) should be tested or blocked. I tested these and recorded the shortfall as a deviation.
5. When a claim's software can't run and its parameters are also unstated (AQuA), both `not_runnable` and `methods_underspecified` apply. I used `not_runnable` and gave the other reason in the notes.
6. The requirement to print each file's SHA-256 in the notebook header is in docs/archives.md, not in the protocol's list of notebook parts. I nearly missed it; the notebook now lists every file read and checks at the end that nothing else was read.

**4. Runtime and failures**

The session took about 45 minutes (06:49 to 07:34 UTC), and the notebook runs in 67–74 s at about 1.4 GB peak memory. Nothing failed in the final runs. Along the way, two runs of `entry.py` failed only because I had started them from my scratch environment, which lacks pyyaml; I re-ran them with the system Python. The git status also shows untracked dotfiles (`.bashrc`, `.idea` and similar) and a `scripts` folder that I didn't create, and I left them alone.
