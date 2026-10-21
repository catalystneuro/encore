I haven't written the claims file. My attempt to write `claims/001955/10.64898-2026.02.17.706301.yaml` was stopped by a safety classifier partway through, so nothing exists under `claims/001955/`. I won't produce that content again in another form. This run has no claims, quotes, statistics or criteria, and the quote checker was never run.

**What I read before the stop:**
- **Text:** the bioRxiv preprint, version 1, flattened from the JATS XML: Results, figure legends, Methods, the data and code links, and the legends of Supplementary Figures 1 to 4. No PDF was supplied, so I couldn't look at any figure image. The supplementary figures exist only as legends, though those legends hold the supplementary numbers. The text's title says "biases backward locomotion"; the dandiset's title for the paper says "biases locomotor direction". Nothing a claim would need was missing from the text.
- **Code:** `github.com/CGonzC/VTAPnO_Locomotion_Analysis`, release `v1.0_manuscript_submission` (commit `1ff5196e`). It has an open-field direction-classification notebook, a fiber-photometry notebook and a MATLAB opto-tagging script. Later tags change only paths and examples.
- **Dandiset:** its description covers the acute and chronic probe recordings and the photometry, so Figures 3 and 4. It does not mention the juxtacellular, slice or open-field experiments.

**Gaps and conflicts the claims file would need to address:**
- **Photometry baseline:** the Methods say −1.0 to −0.1 s; the code uses −3.0 to −0.1 s.
- **Opto-tagging:** the Methods require a waveform-correlation check (≥ 0.90) that the code doesn't do. The text doesn't say how to count a unit that passes at both wavelengths.
- **Open-field tracking:** the Methods filter DeepLabCut tracks by likelihood and fill gaps; the code does neither.
- **Open-field 1-s bins:** the legend corrects post hoc tests by FDR, the Methods by Holm. The baseline window and the post hoc test aren't fixed either.
- **Frequency screen:** the Results say 8 mice; the Methods say the same three mice.
- **Acute activation criterion:** the Methods give three 0.5-s bins over 0 to 1.5 s; the Results say six windows. The paired test and what "time-matched baseline" means are not specified.
- **Chronic units:** whether "activated" means belonging to one of the three response classes or having any activated window is open. The inter-trial interval is 3 to 15 s in the Results and 4 to 35 s in the Methods.
- **Not defined anywhere:**
  - how unit onset latency, spike width and firing-rate epoch are measured;
  - how the DA 2-ms peak and centroid are computed, and which permutation test and confidence-interval method were used;
  - the "response magnitude" measure in Figure 4e;
  - how CV2 and bursts are measured;
  - how speed is measured.
- **Latency to peak speed (Supplementary Figure 2f):** the legend says somatic stimulation was "higher", but its own numbers (0.590 s against 1.164 s) and the Results say lower.

To get a claims file, the reader run needs to be started again.
