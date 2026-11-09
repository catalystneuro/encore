I wrote `docs/pilot-notes/000023-berg-2020-01.md` and changed nothing else. It has no em dashes, no "rather" and no bold. The untracked dotfiles, `.idea`, `.vscode` and `scripts` in the repository root were not created by me, and I left them alone. Nothing is committed.

# 000023, Berg et al. 2020

Four claims reproduced, three partially, three not reproduced and one blocked
on the dandiset, with three more reproduced and one more partially reproduced
on the dandiset together with the paper's code tables; the link claim
`features-and-labels-link` is reproduced, and of the 17 claims on data
elsewhere, 10 are reproduced and 7 blocked. It pins version 0.210914.1900, the
only published version; the paper cites none. The paper, the bioRxiv preprint
"Human cortical expansion involves diversification and specialization of
supragranular intratelencephalic-projecting neurons", describes Patch-seq
neurons of human L2 and L3 from neurosurgical donors in five glutamatergic
t-types (LTK, GLP2R, FREM3, CARM1P1 and COL22A1) and compares them with mouse
L2/3. The claims were written from the preprint's text without its figures,
and the code, read at commit 3daf9f0, had been updated for the later Nature
version, so its feature table, FREM3 cell set and pathology notebook differ
from the preprint's. The cohort counts, depth by t-type, the type ANOVAs of
electrophysiology, GLP2R sag, the human against mouse comparison, the
classifiers, the FREM3 depth correlations, the deep L3 type tests and
pathology against electrophysiology were tested on the dandiset, and the
pathology scores, the NeuN sections and the morphology on the code's tables.
`fig6c-carm1p1-upstroke-rin` is blocked as `methods_underspecified`, as it is
reproduced with upstroke rate and partially reproduced with the
upstroke/downstroke ratio (CARM1P1 4.63 against COL22A1 4.83, BH p 0.054), as
is `fig6a-deep-dendrites`; four transcriptomic claims are blocked as `other`
because the Allen Brain Map RNA-seq data cannot be pinned, `fig6f-smi32`
because its images are public nowhere, and `fig5d-frem3-gene-depth` because the
only public table is the revision's (4417 genes against 790). The author put
seven questions to a reader; the answers moved
`edfig6-classifier-morphoelectric` from blocked to reproduced (0.720 and 0.582)
and `fig1a-thickness` to reproduced on the human value alone (1.231 +/- 0.155
mm). Round 1 gave its own outcome for 32 claims, none for
`fig6-deep-morph-anova`, and agreed with the record on 26; on six blocked
claims it gave `data_missing` where the record gives `other`, which the
claims' `elsewhere` marking does not allow. It found the port of the mouse
section script faulty, and fixing it moved `fig1b-density` and
`fig1c-soma-area` from partially reproduced and `fig1c-soma-variation` from
blocked to reproduced (ratio 3.94); its question on sweep QC showed that IPFX
2.1.2 applies only the noise limits, and adding the Methods' bias current and
bridge balance limits moved `fig6-deep-ephys-anova` from partially reproduced
to reproduced. Round 2 agreed with all 33, so there was no third round; it
found statements the outputs did not support, among them a run time of 14
minutes against 21.0 printed and the link said to be confirmed by features
for all 283 cells where 261 have features on both sides, and these were
corrected. Some outcomes rest on weak ground: `fig4-glp2r-sag` has BH p 0.046
and 0.060 with cell QC; `edtable1-species-ephys` gives 16 with Student's test
under cell QC; `fig6-deep-ephys-anova` turns on one feature, with tau at R2
0.395; and `fig2ef-pathology-ephys` is not reproduced on the code's 283 cells.
Whether cell QC applies and which input resistance the 15% bridge balance
limit means are asked in questions/000023.yaml and unanswered. Opening the 318
files with remfile took about 8 minutes for metadata alone, so each was read
whole into memory; the notebook ran in 23.5 minutes at first and about 21 in
the last run, beyond the protocol's aim of ten.

The files carry no SpecimenID, the identifier by which the paper's code and
tables name cells, so each was linked by its donor and its ephys session id,
which lies 13 to 685 below the cell's SpecimenID; the code's features confirm
the link for 261 of the 283 cells that have them under the Methods' sweep QC
and for 282 under IPFX's sweep QC alone, and for the 35 cells without features
in the code the sample dates and tube order support it without proving it.
The files also carry no t-type, soma depth, brain region or medical condition,
on which every finding of the paper rests, so all labels come from the code;
session_description and the filtering field read PLACEHOLDER, and the archive
summary gives the variable measured as ProcessingModule and the technique as
"analytical technique". The dandiset holds 318 of the 385 cells of the paper's
table, including all 283 with features in the code, from 56 donors against 90;
of the 35 cells without features in the code, 19 give features here under the
Methods' sweep QC (2 of them fail cell QC) and 25 under IPFX's sweep QC alone,
and which recordings were judged too incomplete, or why, is not said. The
mouse recordings are not in the dandiset, so the mouse claims rest on the
code's tables. The code's feature table measures adaptation, initial firing
rate and tau differently from the Methods, and the features recomputed here
match the code; it is consistent with sweep QC on noise alone, as with the
Methods' limits 22 of its 283 cells give no features here, against 1 with
IPFX's sweep QC alone, and 29 of them fail cell QC as IPFX computes it.
Code7_cortical_depth_code_mouse.r as committed does not give the values its
comments print (mouse L2/3 thicknesses of 32, 133 and 90 um against 281, 223
and 257), and reading the lines as L1 to L4 with case_set_1 at 100 um = 165
pixels, the scale its own comment gives, reproduces them;
Code6_cortical_depth_code_human.r never sets q9 to NULL, so the human bin
table counts the five sections unequally, which explains the printed SD
ratios of 2.4 and 4.0 against 2.33 and 3.94 with each section counted once.
Other findings: donor H18.03.318 is female in the files and male in the
paper's tables, and donor H18.06.005 is 56 years old in the files and 57 in
both tables; the gene-depth table is from the revision, and the Patch-seq
transcriptomes behind either version are not in the repository; and the spike
times computed with IPFX equal those stored in the files for the rheobase
sweep of all 280 cells with features, with no spike in the second before any
long-square step, so the stored spikes, responses and stimuli share one clock.

The author's points on the protocol: the link claim names an identifier the
dataset lacks while its matching is fixed in a criterion the author may not
change; `elsewhere` claims whose criterion is only "Not tested on the
dandiset" must be tested or blocked for a reason other than `data_missing`;
data that is public but cannot be pinned has no `blocked_by` category; images
public nowhere cannot be `data_missing` when the claim is marked `elsewhere`;
no category fits when the only public data is the wrong version; it does not
say whether one unmeasurable expected value makes a claim partial or blocked;
it does not say how to treat an outside input that proves inconsistent; IPFX
reads only a file path or an in-memory buffer, so streaming was slow; the
1000-split classifiers the criterion requires put the run beyond ten minutes;
it does not say whether to restrict to the paper's cohort when the link finds
more cells; the suggested clock check does not fit intracellular recordings;
and the `with_labels` definition does not fit t-types and depths measured by
other methods.
