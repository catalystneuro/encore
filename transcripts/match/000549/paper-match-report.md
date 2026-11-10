I gave the one paper a verdict of `partial`. The file `papers/match/000549.yaml` passes `validate`.

**doi:10.1016/j.bioelechem.2022.108319** (Kim et al., "Action spectra and mechanisms of (in)efficiency of bipolar electric pulses at electroporation"): **partial**, `by: agent`.
- **Deciding evidence:** the dataset holds only the experiment in the paper's section 3.3, "Effect of pulse duration." Every file path is named for Figs. 4 and 5 (for example `sub-Fig4-5-Bi1200ns-02_ses-BPAE-5xBipolar-1200ns_image.nwb`). Those files cover the paper's bovine endothelial (BPAE) cells taking up YO-PRO-1 dye under uni- and bipolar pulses of 300 ns to 500 µs. The dataset's title and description say the same.
- **What can be tested here:** the paper's findings on how pulse duration affects the bipolar inhibition, which the paper calls cancellation, and the electrode-side comparison in Fig. 5.
- **The rest of the paper's data:** the paper has no data availability statement. A search of the archive found sister Dandisets from the same lab that appear to hold its other experiments, and I listed them in `data_in`:
  - DANDI:000489: the second-phase amplitude experiment (Fig. 2)
  - DANDI:000548: the pulse-number experiment (Fig. 3)
  - DANDI:000550: the repetition-rate experiment (Fig. 6)
  - DANDI:000448: the strobe imaging of membrane potential in CHO cells (Fig. 7)

I matched these four by their titles only and did not open their metadata.
