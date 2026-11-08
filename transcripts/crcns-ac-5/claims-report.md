I'm stopping here and have written no claims. The supplement this paper's results depend on is not under `paper/`.

**Text read:** `paper/10.1038-s41467-020-14835-7.txt`, the version of record (PMC7046699, from the Europe PMC full-text XML). It is complete for the main text, figure legends for Figs. 1 to 7, Tables 1 and 2, the Methods and the Data availability statement. There is no PDF of the paper; the only PDF is the dataset's own description. I read `paper/ac-5.data-description.txt` only to see what the dataset holds.

**What is missing:** the Supplementary Information (Supplementary Figs. 1 to 3 and their legends). In the text it is only a heading ("Supplementary information is available for this paper at 10.1038/s41467-020-14835-7"), with no content. Two Results sections rest entirely on it:
- **"Response reliability over extended recording durations is high"** rests on Supplementary Fig. 2. It reports that test-retest STRF correlations for large and small PSPs were high and "significantly exceeded those for spike STRFs". The test, n and p-values are given only in the supplement.
- **"Different mean DMR intensities have only minor effects on STRF"** rests on Supplementary Fig. 3: five neurons at 38, 54 and 69 dB SPL showed no significant change in peak latency or STRF bandwidth. This is a claim of absence, so its criterion needs the paper's own test and threshold, which are only in that legend. The same figure is also cited in the Methods and the Discussion.
- Supplementary Fig. 1 (the biocytin-labelled recording site) is cited in the Methods.

The dataset's description also says its "Supplementary" folder holds the data for Supplementary Figs. 2 and 3, so both findings are ones the dataset is meant to test.

**Claims written:** none, so there are no counts of quotes, statistics or criteria, and no open details or readings to report. No file was created under `claims/crcns-ac-5/` and the quote checker was not run. I did not read the analysis code, since no criteria were going to be written; the description says the Matlab scripts are in the dataset's "codes" folder.

**To unblock:** add the Supplementary Information PDF for doi:10.1038/s41467-020-14835-7 to the paper store, for example as `10.1038-s41467-020-14835-7.supp.pdf` or appended to the `.txt`, then run the reader again. `papers/manifest.yaml` has no entry for crcns-ac-5 yet, so this gap is not recorded there.
