# yang-2026-flexible, Yang et al. 2026

Eight claims reproduced on the dandiset alone and twelve more that also use
the Allen metadata, two partially, both with outside inputs, none not
reproduced and seven blocked, all seven with outside inputs; `join-link`, the
link claim the author added to check the files against the paper's metadata
join, reproduced and is counted apart. One outcome, `table1-phenotype-spaces`,
rests on an assumption. The first verification round agreed with all 30
outcomes as they stood, giving the seven blocked claims the reason
data_missing where the record has other, and the second agreed with all 30
after `split-half-reliability` moved to reproduced; nothing was proposed after
the second, so there was no third round. It pins version 0.210913.1639, which
the paper cites and which is the only published version. The paper, Yang,
"Flexible Cellular Phenotypes Retain a Shared Type-Level Organization across
Response Regimes" in eNeuro, reuses the Allen Institute Patch-seq recordings
of mouse visual cortex neurons, builds a separate phenotype space for
long-pulse, ramp and brief-pulse responses, and reports that cell-level
distances and neighborhoods are only partly conserved across the regimes,
that t-type anchors the phenotype more than Cre line does, that type-type
distance maps are shared across regimes, and that transcriptomic distance
tracks the shared map more than the regime-selective differences. The claims
were written from the version of record (PMC13737997) without the Extended
Data files, and from the paper's code at commit 61a5a41, which lacks the
script that ran IPFX on all cells and the one behind the 1,000-shuffle null of
Table 2 rows m and n; the claims check corrected six criteria. Every claim on
the phenotype spaces, the cell-level and type-level comparisons and the t-type
labels was tested, and most counts equal the paper's exactly. Partial are the
size of the t-type alignment A_t (0.0337, 0.0278 and 0.0137 against 0.021,
0.025 and 0.021, each p = 0.0099) and of the same after removing each Cre
line's mean (0.0081, 0.0064 and 0.0103 against 0.011, 0.010 and 0.004), with
no seed of five bringing all three within tolerance. The six Figure 4 claims
and `wgcna-mobility-within-type` are blocked as other: the NeMO data server,
the only source the paper names for the public count matrix, answered 502 or
timed out on every request from 09:20 to 11:46 UTC and in both runs of the
second revision, and the WGCNA claim would also need R. `split-half-reliability`
was partial in the first version, with the claim's seed giving 3,256 cells and
16 random splits against 3,598 and 358; round 1 asked for the criterion's seed
0, which gives the paper's 3,598 cells exactly, and the claim moved to
reproduced, marked seed-sensitive. Round 2 found sentences the outputs did not
support, among them a cause for the A_t offset given as the machine's sort,
which was removed. In the first full pass a killed worker made the pool mark
661 files as failed, fixed before the final runs; the first revision's run
took 77.5 minutes and needed the workflow's longer limits, as the default
60-minute limit timed out during extraction, and the final runs took about 55
minutes each.

Two files hold the same recording: sub-673135474_ses-680563483 and
sub-673135516_ses-680897463 are from different mice, and the paper's join
gives them different Cre lines (Vip-IRES-Cre and Ndnf-IRES2-dgCre), t-types
(Vip Lmo1 Myl1 and Lamp5 Lsp1), layers and transcriptomic samples, yet the
voltage traces of all their usable long squares are identical (SHA-1) and so
are all 94 of their IPFX features; no other two files share a trace or a
feature vector. The four files of subject 636828314 list two response series
for sweep number 1, so IPFX cannot open them, and the join has no row for
them either. The files hold no transcriptomic label or sample identifier, so
t-types, subclasses and RNA sample ids come only from the Allen metadata,
joined by session or file name; the Cre line can be read from the subject
genotype, which agrees with the Allen metadata for every cell. Otherwise every
count the paper reports for the dataset is in the files: of the 4,435 files,
4,430 join to the paper's metadata with matching session, subject and
genotype, and IPFX 2.1.2 gives the paper's 4,344, 4,139 and 4,422 cells per
regime, its 42, 20 and 21 retained features and its k80, with the long-square
extraction failing in 87 of 4,431 files opened, the short-square in 9 and the
ramp in 2. Stimulus and response share a clock. On the paper's side, the code
ranks the binary t-type mismatch with ties in an arbitrary order, so A_t
carries an offset shared with its null; the code's own draws on the paper's
published PCA scores give 0.0370, 0.0316 and 0.0106 against the printed
0.0214, 0.0250 and 0.0213, while A_t minus the null mean is within 0.0005 of
the printed difference, and what produces the gap is not shown. The
split-half random fallback draws a fresh seed-0 permutation for each cell, so
the seed decides the pool (3,582 to 4,100 cells under the seeds 1000 to 4000),
which the paper does not say. A question is put to the paper's author: which
IPFX version and call made the feature table, what sets extract_ok, and where
the script for Table 2 rows m and n is.

The author's points on the protocol: adding a link claim means editing the
claims file, which the author is otherwise told not to change; notebook
conclusions are part of the run hash, so writing them after the run forces a
second 43-minute run; the protocol's seed rule can conflict with a reported
count that depends on the code's seed 0; no `blocked_by` value fits a public
input whose server is down, and `other` was used; Python 3.13 runs process
pools in spawn mode when a pool restarts its workers, and fork was used with
the author's own restarts; and nothing says how to rate a duplicate recording,
rated critical.
