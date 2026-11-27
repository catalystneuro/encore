# longcore-2024, Longcore et al. 2024

Ten claims reproduced, one partially, two not reproduced and none blocked;
no outcome rests on an assumption. The first verification round agreed with
12 of the 13 outcomes and gave `cct-effect-grows-with-intensity` as not
reproduced where the record had partially reproduced, since its criterion
defines no partial outcome; the author changed it. The second round agreed
with all 13 and nothing was proposed, so there was no third round. It pins
Dryad version 300765, the only published version, whose four files match
the SHA-256 values of Dryad's file list. The paper, Longcore, Villanueva,
Nguyen-Ngo, Ghiani, Harrison and Colwell in the Journal of Experimental
Biology (227, jeb247235), gives 16 mice a 1-h light pulse at night at each
of 12 combinations of illuminance (0.01, 0.5, 5 and 50 lx) and correlated
color temperature (CCT; 1750, 1950 and 3000 K), and reports that light of
0.5 lx and brighter suppressed wheel running, that 0.01 lx increased it,
that illuminance mattered several times more than CCT in a GLM with a
significant interaction, that lower CCT suppressed less, that males were
less suppressed than females, that mice differed, and that cFos counts in
the SCN after 50 lx did not differ between 1950 and 3000 K. The claims were
written from the version of record (PMC11418196), whose extracted text lost
the cells of Table 1, so the four claims that rest on it carry no expected
values; the paper links no code, and the statistics were run in JMP and
Prism. Every claim could be tested. The two Table 1 claims reproduce on the
sign of the means, as their criteria say, but three of the eight
suppression means and all four increases cannot be told from zero (p 0.055
to 0.67 for the increases). The GLM claims, the AICc order, the sex
predictions and the extreme mouse effects reproduce only with an identity
link and illuminance in lux. Not reproduced are the Tukey-Kramer sentence,
which matches no comparison under either reading, and
`cct-effect-grows-with-intensity`, where the spread across CCTs is 5.64
points at 0.5 lx against 9.28 at 0.01 lx. `glm-illuminance-cct-interaction`
is partial: the smallest interaction p is 0.0063 against the paper's
p < 0.002, while with mouse identity added every bound is met (interaction
p 0.0007). The cFos t-test gives the paper's t(10) = 0.9409 and p = 0.3689
exactly. Round 1 also found that the log-link fits with lux leave their
parameters undetermined, that the record did not cite the abstract's
"multiple linear regression", and that the sex test treats each
mouse-by-treatment value as independent (Mann-Whitney p 0.083 on one value
per mouse); in reply a cell printing the log-link fits and a cell with the
models with sex and mouse identity were added. Round 2 corrected two
Summary sentences and a note that the increases come from the males, which
holds at two treatments only. Five questions are put to a reader in
`questions/longcore-2024.yaml`. The author's run took about 15 minutes
(18:10 to about 18:24 UTC) and nothing failed but a read-only array error
during development; the notebook ran in 9 s.

The dataset holds derived values only: the wheel counts in 3-min bins from
which suppression was computed are not deposited, so the suppression values
cannot be checked, and cFosdata.csv holds one value per animal with no
animal identifier, sex, section, side or observer, so the averaging over
observers the Methods describe cannot be checked, though the paper's data
statement calls the deposit raw data. SuppressionDataset.csv holds 183 of
the 192 mouse-by-treatment values: mouse 6FC1, P2 has no value at the six
0.01 and 0.5 lx treatments and mouse 6FC2, P8 none at the three 0.01 lx
treatments, so those treatments have 14 or 15 mice where the paper gives
n = 16, and neither the README nor the paper says why; the AICc values here
are 3.6 to 4.2 above the paper's, and n = 192 cannot be rerun to find the
source. The README says suppression "ranges -1 to 1", but the values are
percent, from -59.59 to 100. The illuminances, CCTs, 16 mice and cFos
groups are those of the Methods, no value is deposited twice, and the
treatment means at 0.01 and 50 lx match the four the abstract gives. In the
paper, the Methods state a log link, but the reported results fit an
identity link; the 3000 K cFos spread of 8.22, given as an s.d., is the
s.e.m. of the deposited values (s.d. 20.13); and the sentence that within
color temperatures only 50 lx at 1750 K differed cannot be traced to a
comparison. Three questions are put to the paper's authors: which link and
which scale of illuminance the JMP models used, why the nine values are
missing, and which comparisons the Tukey-Kramer sentence describes. The
dataset was not converted by CatalystNeuro.

The author's points on the protocol: developing on a subset and timing do
not apply to a 5 KB table; the clock-alignment check does not apply to one
value per mouse and treatment; no finding kind covers a sentence of the
paper that matches none of its data when the paper gives no pairs, and
`methods_unavailable` was used; criteria that say 16 mice were run on the
14 or 15 present as a deviation; a criterion with no partial rule was first
judged by the protocol's general definition; two readings in the claims
file cannot be run on the deposited data; JMP's centering of illuminance in
the interaction is fixed by neither the paper nor the claims file; and the
finding on checks that passed has no `finding-*` cell of its own.
