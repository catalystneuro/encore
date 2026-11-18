I wrote no claims. The supplement that the dataset's own results rest on is not in `paper/`, so the protocol says to stop.

**What was read**
- `paper/10.1016-j.crmeth.2022.100221.txt`: the version of record from Europe PMC (PMC9142754.1). It has the main text, the legends of Figures 1 to 7, and the STAR Methods.
- `paper/10.1101-2021.10.18.464781.txt`: the bioRxiv preprint, version 1. Its "Supporting information" section is empty.
- There is no PDF.
- There is no code to read. The paper says "This paper does not report original code." The electrophysiology analysis is described only as following Rowland et al. (2018).

**What is missing**
The supplement, Document S1 (Figures S1 to S4 and Tables S1 and S2), is in neither text. The dataset is the paper's in vivo electrophysiology: optrode recordings in medial entorhinal cortex (MEC), with open field sessions and laser stimulation. Its findings rest on that supplement:
- **Figure S4:** the grid, head direction and border cells, and their head direction scores and mean vector lengths.
- **Figure S3:** an input cell whose firing stays stable over at least 3 days of rabies expression.
- **Figure 5C:** the latency and fidelity values for each example cell are printed only inside the figure, and there is no PDF to read them from.
- **Tables S1 and S2:** the animals, viruses, volumes and survival times. Figure 2A, Figure 2B and the controls depend on these.
- **Figures S1 and S2:** the spread of labelled cells over time, both in the hippocampus and to MEC.

**To unblock**
Add Document S1 (or the "Article plus supplemental information" PDF, Document S2) to `paper/`. It is linked from https://doi.org/10.1016/j.crmeth.2022.100221 and from PMC9142754. Then rerun the reader. Nothing was written under `claims/000230/`, so there are no claims, quotes, statistics, criteria or open readings to report.
