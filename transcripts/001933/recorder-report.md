I ran `python tools/readme_row.py 001933 --write`. The README already had a row for 001933 from attempt -01, and the script replaced it: the counts are now 6 / 2 / 1 (+1) / 0, where the old row had 8 blocked. I added the subsection below at the end of `docs/pilot-notes.md` and committed nothing.

Every run of `tools/entry.py all` stopped at its check, on 8 errors in the earlier record `001933-chen-2026-01.yaml`. That record was left unchanged, so the workflow's check will likely fail the same way until someone exempts old records or changes the rule.

### 001933 again, Chen et al. 2026, under pilot-7 (2026-10-15)

The second attempt, made because pilot-7 changed the protocol; the dandiset
(0.260825.1457), the paper's code and the paper are unchanged. Six claims
reproduced, two partially and one not reproduced on the dandiset, plus the
link claim using the paper's source data, not reproduced, and eight claims
on data in other archives, of which four reproduced, three partially and
one not reproduced; before, the dandiset's counts were the same and the
eight were blocked. Round 1 disagreed on one outcome,
`fig3d-rim-binds-unphosphorylated`, which the author had decided with an
imputation the criterion lists as a variant, because RILPL2 is found only
in the p-RAB3A pulldowns and the paired test has no pairs for it; the
author changed it to partially reproduced (3 of 4), round 2 agreed with all
18 outcomes and nothing was proposed, so there was no third round. The
paper reports that LRRK2 impairs the release sites of dopamine axons
vulnerable in Parkinson's disease, in G2019S mice. The ten photometry claims of Figure 6 and
Supplementary Figures 7 and 8 were tested on the dandiset as before, and the
eight claims of Figures 1 to 5 on Zenodo, PRIDE and BioImage Archive data,
starting from the deposited per-section and per-blot values, since the
Imaris analyses and the blot quantification cannot be rerun. Two outcomes
rest on weak ground: `supp8c-calb1-spontaneous-not-reduced` has p = 0.0509
and would be below 0.05 in 59 of 121 nearby exclusion windows, and part B
of `fig4d-fewer-active-zones` fails on a re-implementation of the FIJI
analysis that keeps a median of 183 VAMP2 particles per image against the
legend's about 1000.

The dandiset was converted by CatalystNeuro (catalystneuro/dombeck-lab-to-nwb).
None of the earlier findings is fixed. The most consequential is still that
the Calb1 dF/F is not the trace behind Supplementary Figure 8 (0 of 384
published traces match, and recomputing dF/F from the raw signal with the
published code gives the dandiset's series, not the paper's), so the Calb1
claims are results on the dandiset's processing. The finding that Figures 1
to 5 are not in the dandiset is now that the dandiset's description and
related resources do not name the deposits that hold them. The published
spontaneous values are now known exactly: 0.005 times the trapezoid
integral divided by the number of samples in the transient, to 2.2e-15 in
every Anxa1 mouse, where the Methods give the integral. The new findings
concern the other archives. In PRIDE PXD065006 the RAB3 T86 phosphopeptide
is higher in the samples labelled MLi-2, and the paper's volcano table
holds MLi-2 minus vehicle (to within 1.6e-06 up to a constant) while the
Figure 2B legend reads a positive difference as higher with vehicle, so
either the labels or the figure's direction is swapped; with swapped labels
`fig2b-rab3-phosphorylation` would reproduce. That table gives 254
phosphopeptides at the legend's thresholds where the text gives 289; the
Figure 3 counts of 69 and 16 are those at adjusted p < 0.05; the Figure 1D
p = 0.0008 matches a paired test or a test of mouse means, not the legend's
test (4.65e-06); one WT section appears twice in the Figure 5D and 5E source
data, and counted once one comparison moves from p = 0.0344 to 0.058;
counts in the source data and legends differ (51 G2019S areas against 57 in
Figure 4E); the G2019S animals of Figures 5G, 5H and 5J are not identified
in the source data; the image studies hold images the figures do not use
without saying which were used; and three synaptosome images give 488 nm
for all channels in their OME metadata.

`tools/entry.py all` stopped at its check in every run, on 8 errors in the
earlier record `001933-chen-2026-01.yaml`, whose blocks with `data_missing`
fail the pilot-7 rule; the record was left unchanged and the notebook run
with `entry.py run`. The author's points on the protocol: the check applies
the current claims file to every attempt of an entry, with no exemption by
protocol version; one claims file serves both attempts, so updating it
changes the claims the earlier attempt points to; the rules for a repeat
attempt assume a changed dandiset and have none for an earlier finding
whose kind a new protocol makes invalid; findings are defined as about the
dandiset, and the schema has no field for the archive a finding concerns;
and the criteria for the eight new claims were written after seeing the
deposited values, though before any statistic, and for `fig2b` the
criterion did not fix the normalisation that decided the outcome.
