I stopped without writing any claims. The text I was given lacks the supplement that the NHP insertion results rest on, and the protocol says to stop in that case.

**What is under `paper/`**
- `10.1038-s41592-025-02614-5.txt`, the version of record. This is only the paywalled Nature page: the abstract, the figure titles, the Data and Code availability sections and the references. It has no Results, no Methods and no figure legends. There is no PDF.
- `10.1101-2023.10.24.563768.txt`, the bioRxiv preprint posted October 29, 2023. It has the main text, the figure legends and the Methods, but not the supplement. The page shows only a "Supplementary Material" link, and none of the Supplementary Figure legends appear in the text.

**Why the supplement is needed for this dataset**
The Data availability section says dandiset 001282 holds the NP1-NHP insertion datasets. In the preprint those results are in Fig. 4 and in Supp. Figs. 11 to 13 (Results, "Tracking long-range drift during probe insertion in non-human primates"):
- Supp. Fig. 11 shows the second of the two insertion datasets ("N = 2, Fig. 4 and Supp. Fig. 11") and its spike raster.
- Supp. Fig. 12 shows the finding that Kilosort's template-based drift tracking failed on these recordings.
- Supp. Fig. 13 shows the anatomical trajectory used to align the feature map with brain regions.

Without these, the second recording and the Kilosort comparison have neither a source nor a method, and the anatomical alignment is only partly specified.

**What would let this run go ahead**
Either of these would do:
- The accepted author manuscript in PubMed Central (PMC13055889, NIHMS2068114) with its supplement file (NIHMS2068114-supplement-supplementary.pdf). The claims file for the same paper, `claims/001290/`, was written from exactly these.
- The bioRxiv supplementary PDF for 10.1101/2023.10.24.563768, together with the main text.

Since no claims were written, there are none to count, and no open details or readings to report. Nothing was written under `claims/001282/`.
