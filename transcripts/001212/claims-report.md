I didn't write any claims, because the supplement is missing. Under the protocol's Reader section (step 1), that means I stopped before writing anything, and nothing was created under `claims/001212/`.

**What I read:** the version of record (IEEE TNSRE vol. 33, pp. 4008–4017), from `paper/10.1109-tnsre.2025.3614867.txt`. It is the main text, Methods, Results, Discussion and references, all 10 pages. The PDF is the same 10 pages, so it has no supplement either. The paper links no code or data repository.

**What is missing:** the supplementary material the article points to ("supplementary downloadable material available at https://doi.org/10.1109/TNSRE.2025.3614867"). The results depend on it in four places:
- **Fig. S2** gives each rat's stimulation order and which stimulation groups were target and which were non-target. Every target versus non-target finding depends on this split: seizure duration (Fig. 3A/B), seizure frequency (Fig. 3C), the band power ratios (Fig. 4), the interictal spike rate (Fig. 5) and the HFO rates (Fig. 6). The main text names only the non-target sites that worked (R2 ANT, R3 CA1, R4 CA1, R5 CA3, R7 CA3), not the full assignment.
- **Fig. S3 and Table S1** hold the network-dynamics result for all seven rats: the Pearson correlations of the weighted causal flow vectors within and between baseline groups. The Results cite Fig. S3 as the confirmation "across all experimental rats".
- **Fig. S1** shows the AdaBoost seizure detector's architecture. This is a methods detail, but it decides which seizures triggered stimulation.

Once the supplement (for example the IEEE supplementary PDF) is put under `paper/`, the reader run can be redone.

So the counts are zero: no claims, quotes, statistics or criteria. Since no criteria were written, I named no open details or readings.
