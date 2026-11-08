No outcome changed. The round-2 verifier agreed with all 33 outcomes, so there is nothing under `proposed`. The entry ran twice with `python tools/entry.py all`: 0 check errors, and the notebook passes in about 455 s. Every printed number matches the previous run.

**Output the verifier asked for**
- Cell 22 now prints the sound 1 and air-puff results over all ten seeds, the whole-session run and the 'LFP saturation' run. For each it gives the lowest tuned fraction of any genotype and the largest binomial p against 0.25%.
- Across all runs the lowest fractions are 28.8% (sound 1) and 32.3% (air puff), and the largest p is 1.3e-185. Vglut2 and Esr1 are above Ctl at p of 1.1e-14 or less in every run.
- Cell 24 and the fig4e notes now quote these numbers in place of the unsupported "hold under every seed, period and saturation series shown".

**Corrections**
- **Latency (ed7bd):** with the pre-trial baseline the air-puff latencies agree in 2 of 4 subregions under both thresholds, not "2 or 1". Fixed in cell 41, the notes and the latency question to the authors.
- **fig4g-glm-units:** cell 19 and the notes now say the whole-session total (2,195) is also outside the 10% limit (2,139.5).
- **Saturation wording (code-outputs-link):** cell 7 and the record now say the spikes removed are those near the files' 'spike saturation' periods, which is the code's series. They had said "the Methods' removal near LFP saturation".
- **Assumption labels:**
  - ed8r, fig4h and fig4jl were already marked as assumed in the record. Their result cells, the Summary and the README now say so too.
  - ed8h and ed9bg also use the GLM-fitted units, so I marked them as assumed, with a deviation naming the GLM period.
  - fig4i is not marked: its reading (c) uses all selected units, no GLM, and gives the same outcome. A deviation now explains this.
- **Record:** round 2 is added under `verifications`, with the verifier's reasons and my response for each claim.

**Not done**
- The cause of the paper's 1,770 clustered units (fig4h) is still unknown. It stays as the open question to the authors.
- The ed9a block-4 issue stays with the reader question already in `questions/000473.yaml`; the claim is unchanged.
- The fig4e and fig4g-tuned-unit-counts outcomes still depend on the seed, as the notes already say.
- The working tree has untracked files I did not create (`.bashrc`, `.profile`, `.idea`, `scripts`, and others). They should be kept out of the commit.
