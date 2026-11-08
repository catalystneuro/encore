I wrote no claims file. The paper text under `paper/` is incomplete, and the protocol (Reader, step 1) says to stop when the full text or the Methods are missing.

**Text read:** `paper/10.1038-nature15741.txt`, the version of record (Nature 528:352–357), "supplied by a person", extracted with PyMuPDF. Its PDF pages 3 to 16 contain no text. What it does have:
- **Pages 1 and 2:** the opening of the Results, up to partway through "Sequence splitting during syllable formation".
- **Pages 17 to 24:** the legends of Extended Data Figs 4 to 10.

I could not read the PDF to fill the gap. The page renderer (poppler) and the PDF libraries (PyMuPDF, pypdf) are not installed here, so I couldn't tell whether those pages are scanned images or text the extraction missed.

**Missing, and needed by the claims:**
- **Rest of the Results** from bird 1 onward: shared and specific neurons and how they change, bout-onset differentiation in bird 2, the motif strategy, and the model results.
- **Discussion.**
- **Figure legends for Figs 1 to 5**, which hold the panels, n values and tests behind the main findings.
- **Full Methods:** the song-stage definitions, how syllable locking and rhythmicity are judged, burst latency, the criterion for calling a neuron "shared", the bias index, the statistics, and the model.
- **Legends for Extended Data Figs 1 to 3** (which neurons were recorded, latency locking, rhythmicity, bout-related neurons, burst coverage).
- **References** (not essential).

**Read but not used:**
- The model code (`paper/10.1038-nature15741.code.m`) is the supplementary MATLAB script for Fig. 5a–d and Extended Data Fig. 10a–d. Its header points to https://github.com/emackev/HVCModelCode for the code of other figures; I did not open that repository.
- The data description (CRCNS am-3, v0.8) says the set holds single-unit HVC recordings from juvenile male zebra finches during singing, 32 birds aged 44 to 112 dph. The paper reports 35 birds.

**Next step:** someone needs to supply a complete text of the paper, with the main text, Methods and Extended Data legends, either a new extraction of the PDF or the HTML version of record. The reader run can then be repeated.

Claims: 0, so there are no quotes, statistics, criteria or open details to report.
