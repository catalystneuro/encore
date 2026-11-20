I wrote no claims for harris-2026: the paper's full text is not under `paper/`. The protocol (Reader, step 1) says to stop in that case and name what is missing, and not to write claims from the abstract.

**What `paper/` holds:**
- `10.1038-s41467-026-68893-4.txt`. Its header says "Version: version of record, Source: find_reuse cache". It contains:
  - the reference list (lines 1 to 480);
  - one line of the article web page (line 481) with the abstract, Data availability, Code availability, references, acknowledgements and licence;
  - the supplement's text from line 485 on: Supplementary Figures 1 to 16, mostly axis labels plus the legends.
- `10.1038-s41467-026-68893-4.supp-41467_2026_68893_MOESM1_ESM.pdf`, which is only the Supplementary Information PDF.

**What is missing, so it can be supplied:**
- The main text of the version of record: Introduction, Results and Discussion.
- The Methods: data selection and sessions, LFP preprocessing, θ and γ band definitions, wavenumber and order parameters, PAC, spike–LFP coupling, classifiers and statistics.
- The legends of the main figures (Figs. 1 to 6 or so).
- The Source Data file, if values are to be taken from it.

The supplement legends keep pointing to the missing parts ("using the same methods as Fig. 3", "as Fig. 4"). So no finding can be stated, quoted or given a criterion from what is here.

The full article is open access (CC BY-NC-ND) at https://doi.org/10.1038/s41467-026-68893-4, so fetching it again should give the complete text. The code to read once it is back: SpatiotemporalMotifs.jl v0.4.0 (https://doi.org/10.5281/zenodo.14550386; the reference list cites https://doi.org/10.5281/zenodo.18113009 for the same version). The paper says it used DANDI:000713 version 0.240702.1725.

**Report:**
- **Text read:** the header says version of record, but only the abstract, availability statements and references of it are present. The supplement (Supplementary Information, Figs. 1 to 16) is present.
- **Claims:** 0, so 0 with quotes, statistics or criteria.
- **Details left open:** none assessed.
- **Missing:** the main text, the Methods and the main figure legends, which every claim needs.

I did not create `claims/harris-2026.yaml` and ran no quote check.
