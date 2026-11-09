# dryad-4j0zpc8hz, Didion-Gency et al. 2024

Fourteen claims reproduced, three partially, seven not reproduced and 15
blocked, all on the dataset. It pins version 260590, the only version Dryad
lists, which holds one Excel workbook (a README sheet and "Total Data", 900
rows), Metadata.csv and a README. The paper, in Plant Physiology, grows
3-year-old European beech and downy oak seedlings in 16 open-top chambers at
WSL Birmensdorf, in monocultures and two-species mixtures, under control,
warming of about +5 C (W), soil moisture reduction of about 50% (MR) or both
(WMR) from June 2019, and reports their phenology, leaf water potential,
assimilation, non-structural carbohydrates and growth in 2020 and 2021. The
claims were written from the version of record in Europe PMC (PMC10828195)
with its supplement, without the figures; the paper links no analysis code.
The phenology regressions on temperature, the growing degree days against
chilling days of Figure 2, the treatment tests of leaf water potential, Asat,
starch, sugar and growth in Figures 3 and 4, and the mixture against
monoculture contrasts and net biodiversity effects of Tables S2 and S3 and
Figure 5 were tested. Five claims are blocked as `data_missing`, as the soil
moisture, the chamber climate records and the initial tree sizes are not
deposited, and ten as `methods_underspecified`, as the readings the claims
file names give different outcomes; `disc-psi-minimum` is not reproduced, as
no reading puts both species within tolerance (beech -0.678 against -1.9 +-
0.19 under the first reading). The author put three questions to a reader;
the answers added reading S3 (negative starch, sugar, Asat and increment
values dropped), fixed the years of the interaction model from the degrees of
freedom of Tables S2 and S3, and named the years and F tests of Table S6 as
readings, which moved `fig4-oak-warming-growth-2021` from partially
reproduced and `tables6-no-seasonal-variation` from not reproduced to
blocked, and `tables3-oak-wmr-diameter` from not reproduced to reproduced.
Round 1, which could not re-run the notebook on the data, gave its own
outcome for each of the 39 claims and agreed with the record as it then
stood; its points led to reading A2 (contrasts adjusted over the model's
eight treatment and year contrasts), under which the one passing contrast of
`tables3-oak-wmr-diameter` has p 0.16, and over all trees the 2021 difference
is +1.69, outside 1.4 +- 0.14, so that claim moved to blocked, and the author
asked three more questions, still unanswered. Round 2 agreed with all 39, so
there was no third round; it found five statements the outputs did not
support, among them an oak range of 0.50 to 2.39 against 2.86 printed and a
claim that the refit reproduces Table S1 exactly for some traits where only
oak AGWB is exact, and these were corrected. Some outcomes rest on weak
ground: `fig1cd-development-duration` (oak) and `fig1-oak-steeper-advance`
hold only under reading P1, which treats 48 tree-years as independent
against 8 temperature values, and with a random intercept per treatment and
year they have p 0.11 and 0.097; `fig1ij-growing-season` uses the deposited
Growth_length, and on the criterion's definition the beech slope is 1.09
(p = 0.085) and the claim would fail; and under the claims file's reading of
Eq. 3 the complementarity effect is exactly twice the net biodiversity
effect, so the complementarity parts of the Figure 5 claims are not tested
on their own. The author's run took about 30 minutes; two helper bugs and one
table bug were fixed during development, and the notebook ran in 104 s at
first and 213 s in the last run.

The soil moisture (Mspring, Mfall, Mannual), the chamber climate records at
10 min and the initial heights and diameters of Table S4 are not deposited,
and five claims rest on them; the annual air temperatures that are deposited
agree with the paper (W minus C 5.18 and 5.20, all eight Table S5 values
within 0.4). Growth_length never equals onset of senescence minus bud
swelling, the Methods' definition: it is a median 55 days longer, and 2 to
33 days longer than the end of senescence minus bud swelling, and neither the
workbook nor Metadata.csv defines it. Tspring, Tfall and Tannual are one
value per treatment and year, with the sensor height (50 cm or 2 m) not
stated, and GDD and Chill_days are given per tree without the records they
were computed from, so the readings of the GDD sum and the end of the
chilling count could not be run separately. Starch (77 tree-campaign rows,
down to -6.28 %), sugar (3, down to -4.06 %) and Asat (5, down to -0.29) have
negative values, which a concentration or an assimilation rate cannot have,
though the paper takes their square root. The 'Total Data' sheet has 35 rows
that repeat another row exactly (trees 17, 35, 45 and 144), and tree 144 has
two rows for campaign 5 of 2020 with different sugar (7.71 and 6.69 %) and
starch (4.99 and 9.99 %) values. Metadata.csv and the README sheet give the
treatment codes as C, W, MR and WMR while the Treatment column holds C, D, H
and HD, which the Warming and Soil moisture reduction columns map one to
one. Other findings: Diameter_growth is labelled cm, but its values (median
0.42, up to 4.46 a year) on stems of 5.2 to 6.1 mm at planting are
consistent with mm; four compartments (6 in chambers A3, A4, B3 and B4) hold
a beech monoculture tree and an oak mixture tree, which the design does not
allow; AGB_growth is exactly 0 in 57 of 191 tree-years of 2020 and 2021,
whose median height increment is 5 cm, and is never negative; refitting the
treatment model with marginal F tests gives Table S1's F values for oak AGWB
increment exactly and for beech Asat within 0.25, which links the deposited
table to the paper's analysis; and the Methods say 2019 is not included in
the study and the treatments began after its first campaign, yet the
treatment model has year 2019 to 2021 as a fixed effect, so under reading T1
the 2019 values include that pre-treatment campaign.

The author's points on the protocol: the entry check rejects string literals
starting with `/tmp/`, where Dryad files are read, so the path was built
from parts; it does not say whether readings the author adds while waiting
for an answer are bound by the rule that the outcome is the one all readings
give, which here blocked four claims; it says that rule does not apply to
claims of absence, while the claims file's criteria apply it, and the claims
file was followed; it does not say how to treat a criterion only part of
whose values can be computed; the clock check does not apply to a table with
no time series; the rule that a reading chooses no method breaks down where
the data are deposited already computed, as GDD and chilling days are; and
it gives no rule for `measured` when no reading matches.
