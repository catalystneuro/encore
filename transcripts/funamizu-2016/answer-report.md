I answered the one open question, `supp9-preserved-representation`, and changed the claims file.

**Answer in brief:** yes, the measure in the paper is the signed difference, and the old criterion was wrong to treat it as absolute. Supplementary Fig. 9b plots "Difference to continuous condition (cm)" from -58.6 to 37.7 cm, with boxes on both sides of zero, and the Mann-Whitney stars sit on those signed boxes. The claims file also wrongly said that only an absolute difference can show which area preserved its preference better. A signed difference nearer zero shows that too.

**What changed in the criterion:**
- **Test:** PPC is now compared with PM using a Mann-Whitney U test on the signed differences (continuous minus intermittent).
- **What "preserved more" means:** the area whose median signed difference is nearer zero.
- **When it counts as reproduced:** in intermittent 1, PPC and PM after-reaching neurons differ with P < 0.05 in at least one layer, with the PPC median nearer zero. No significant comparison may have the PM median nearer zero.
- **Check against the figure:** this matches what the figure shows. In every starred comparison PPC is nearer zero, including the layer 2 group nearest 67 cm, where both medians are positive and PM's is larger. The after-reaching group is starred in layer 3 of intermittent 1.
- **Old test:** the absolute-difference test stays as a variant that is reported but not judged.

The statement, source, quote and statistics are unchanged. I read Fig. 9b from a page rendered with PyMuPDF, which I installed into `$TMPDIR` because no PDF renderer was available.

`python tools/claims_check.py` passes all 40 quotes. It reports 6 problems, all p-values it cannot find because the text garbles "× 10⁻ⁿ". They are the same 6 the earlier check confirmed by reading, and none is in this claim. Both YAML files parse. Nothing is committed or pushed.
