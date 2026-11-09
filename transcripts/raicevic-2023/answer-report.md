I answered the one question on 000491 and changed the claims file. `tools/claims_check.py` reports 22 claims, 22 quotes and 0 problems. Nothing is committed.

**fig8-ellipse-parameters** (claims file changed): The asker was right that the ellipse should be fit to the PVS and the vessel together, not to the two PVS lobes alone.
- **Paper evidence:** the Figure 4 legend says the shapes are fit "to the PVS and vessel segmentation". The Results say the major axis "includes the vessel radius". R3 peaks at 35 um, above the 28 um vessel radius, which an ellipse of the lobes alone can't produce. The method follows Tithof et al., whose elliptical annulus has the vessel inside the outer ellipse.
- **P9 in the opening comment:** the ellipse is now fit to the region inside the PVS's outer boundary (PVS and vessel segmentations together, holes filled). P9 also says this ellipse applies to every claim that uses the ellipse fit: fig5d, table2, fig5b, ellipse-annulus-underestimate, fig7 and fig8.
- **fig8 criterion:** it now points to that fit.
- **Unchanged:** the expected values, and the two existing readings of which part of the ellipse counts as PVS (the ellipse minus its overlap with the circle, or ellipse area minus circle area).

The question is marked `answered: 2026-11-04`.
