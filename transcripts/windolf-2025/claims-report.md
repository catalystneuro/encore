I stopped without writing claims. The full text and the Methods are missing, so `claims/windolf-2025.yaml` is unchanged and still the pilot-10 version.

**What `paper/` holds**
- `10.1038-s41592-025-02614-5.txt` is labelled "as served by crossref", but it is only the Nature Methods subscription preview page ("This is a preview of subscription content"). It contains:
  - the abstract and the figure titles;
  - Data availability and Code availability;
  - acknowledgements, author list and contributions;
  - the legends of Extended Data Figs. 1 to 9, and the title of Extended Data Table 1 without its contents.
- It has no Results, no Methods and no main figure legends. None of the sentences the current claims quote are in it ("r = 0.98", "n = 47 recordings", the Methods section titles); I searched for them.
- `10.1038-s41592-025-02614-5.supp.pdf` (25 pages, 70 MB) seems to be the Supplementary Information (Supplementary Text and Supplementary Figs. 1 to 18). I couldn't read it: this environment has no PDF text or page-rendering tools (poppler, PyMuPDF and pypdf are all missing).

**Missing, to be supplied**
1. The full main text and Methods of the paper, either the version of record or the accepted author manuscript. The existing file was written from the manuscript in PubMed Central (PMC13055889, NIHMS2068114), which is no longer under `paper/`. Every claim's quote, statistics, expected values and criterion rest on its Results and Methods. The Methods sections the criteria cite include "Preprocessing of AP band data", "Setting parameters", "Robust decentralized registration", "Tracking fast motion from spikes using clustering and splines" and "Spike registration quality metrics".
2. The contents of Extended Data Table 1, the parameter listing behind the registration settings.
3. A readable copy of the supplement, either as text or with PDF tools installed in the runner.

**What the update will change once the text is there**
- Under pilot-14, the paper has two datasets. The Fig. 4 claims (`fig4-nhp-insertion`, `fig4f-insertion-anatomy`) move from `data: elsewhere` to the dataset, with `datasets: [001282]`.
- The Extended Data Fig. 3 claims get `datasets: [001290]`.
- The opening comment needs the new provenance line and both datasets.

So there are no counts of claims, quotes, statistics or criteria to report, and no open details or readings were assessed in this run.
