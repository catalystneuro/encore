The claims file is ready for an attempt. I changed six claims and the header, added one claim, and appended the `checks` entry. Nothing is committed.

**Checker result:** `claims/huang-2025.yaml: 45 claims, 45 quotes, 1 statistical values, 0 problems` (it was 44 claims before I added one).

I read the paper and its supplement, and the linked repository (EdnaHuang/SubnetworkAssembley2024) at the commit the file cites. Almost all the contrasts and p-values the criteria quote from the repository outputs are as stated. The four conflicts the file already names are real: MI by sex at P21, CNO and Pearson correlation, subnetwork number across clustering methods, and the VGAT layer difference.

**Changes, by claim**
- **figs6efg-cno-topography-unchanged:** for two of the three distances it quoted pre-bootstrap ANOVA p-values (0.145, 0.746). The paper's test is the bootstrapped contrast, which gives p = 0.097 and 0.660. Replaced.
- **fig4fgh-configuration-trajectory:** the multiple-cluster part was supported only by a pre-bootstrap p = 0.101. The paper's own output has P13 minus P15 = 6.2 points with p = 0.029, which fails the claim's own rule. I recorded this as a conflict and added it to the header's list of conflicts.
- **fig2e-subnetworks-present-same-number:** "most P11 datasets" was a bound the paper never gives. It now reads "more than half" and says the bound is this file's choice.
- **fig4b-synchrony-gradual-decline:** now says the rule for "gradual" is this file's reading, not the paper's.
- **figs5e-mostly-glutamatergic:** the claim pointed at the imaging dataset, but the counts come from histology. Set `data: elsewhere`, naming the Mendeley deposit, and said the paper does not state that it holds these counts.
- **Added figs5f-hm3dq-mostly-gabaergic:** the Figure S5F finding (hM3Dq-expressing neurons are mostly GABAergic) had no claim.
- **Header:** says why the code's event threshold is used. Read literally, the Methods' threshold (four times the mean Z score of the quietest window) would be close to zero.

**Still open**
- The paper's sentences contradict its own statistics outputs in five claims: figs4b-mi-sex-p21, figs6ab, fig4fgh (multiple-cluster part), figs7-subnetwork-number-stable and figs9 (VGAT part). These claims are tested as written.
- Some decision rules are this file's, not the paper's, and each criterion says so. They are the Wilcoxon test in figs3c, "similar" read as within 5 points in figs7-method-comparison, and the "largest contrast" readings.
- In figs7a, the paper's "about 25% of events" may count single-cluster events only, or single- and multiple-cluster events together. The two readings differ by about 1 point, which is inside the tolerance.
- It is not known whether the Mendeley deposit holds the S5 and S9 histology. The S9 claims use the repository's spreadsheet; the S5 claims have no public source that the paper names.
