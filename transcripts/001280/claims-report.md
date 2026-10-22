I stopped without writing any claims. The version of record's supplement is missing from `paper/`, and several of the paper's results depend on it. Nothing was written under `claims/001280/`.

**What I read**
- `paper/10.1016-j.neuron.2024.12.023.txt`: the accepted author manuscript from Europe PMC. It has the main text, the STAR Methods and the figure legends for Figures 1 to 7. It ends at "Supplementary Material 1" with no content after it, and there is no PDF.
- `paper/10.1101-2024.05.08.593085.txt`: the bioRxiv preprint (version 1), with its supplementary legends (S1 to S8) and figure-by-figure quantification methods.

**What is missing:** the version of record's supplement, Figures S1 to S7 and Table S1. The results rest on it in three ways:
1. **Table S1 holds every sample size.** The legends of Figures 4 to 7 all say "n : see Table S1", so the per-rat session and assembly counts behind every Mann-Whitney, linear mixed effects, regression and chi-square test are not in the text.
2. **Several reported findings appear only in supplementary figures.** These include:
   - head direction reward counts (S2d);
   - jumps of at least 50 cm in 60 to 78% of events (S4a);
   - the tone-removed analyses and the opposite-arm results, p = 0.067 and p = 0.004 (S5a to d);
   - 1.8 to 8.1 active cells, or 10 to 14% (S6b, c);
   - remapping, cosine distance and explained variance (S6d to f);
   - theta phase locking by Rayleigh test, the spectral analysis, multiunit activity, and jump against trajectory by brain state (S7a to d).
3. **The detailed analysis methods are not in the version-of-record text.** The Results cite "(Fig. S6b, Methods)" for the count of high-strength cells, but the Methods never describe it. Also missing are:
   - the denominator of the "fraction of time" measure;
   - the mixed-model specification;
   - how target assemblies and random times are chosen;
   - the state assignment for Figure 7b;
   - the theta null.

   In the preprint these details sit in its quantification section, so in the version of record they are presumably in the supplement.

**Why I didn't use the preprint instead:** it is a different version. Its figures are numbered differently, some numbers changed (SWR-associated representations are 10 to 20% in the preprint against 6 to 11% in the version of record; late-theta preference is 4 of 6 rats against 5 of 6), and it lacks the Figure 3 jump classification and the reward correlation analysis. Claims from it would not match the version that cites dataset version 0.241218.2300, and mixing the two versions would leave methods unsourced.

**To supply:** the Neuron supplemental PDF for doi:10.1016/j.neuron.2024.12.023, with the Figure S1 to S7 legends and Table S1, plus any Methods S1 if it exists.

**Code:** linked as zenodo 10.5281/zenodo.14522610 (analysis) and 10.5281/zenodo.14399029 (real-time decoder). I didn't read it, because stopping came first. The code alone could not stand in for the missing Table S1 and supplementary results.

**Counts:** 0 claims, so no quotes, statistics or criteria. No open details are recorded, since no criteria were written.
