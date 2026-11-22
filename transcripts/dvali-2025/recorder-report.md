# dvali-2025, Dvali et al. 2025

Five claims reproduced on the dandiset, three partially, none not reproduced
and twelve blocked, with four more reproduced and eight more blocked that also
use outside data; the six claims on the connectome alone (`elsewhere`), of
which `anatomy-network-properties` reproduced, `ed6-anatomy-feedforward` was
partial and four were blocked, and the link claim `atlas-dataset-link`,
partial, are counted apart. Four outcomes rest on an assumption. Both
verification rounds agreed with all 39 outcomes, no outcome changed and none
was proposed after the second, so there was no third round. The record pins
0.240920.1434, the version the paper cites, and takes one column, the targeted
ROI of each stimulation, from 0.240930.1859. The paper, Dvali, Seguin, Betzel
and Leifer, "Diverging Network Architecture of the C. elegans Connectome and
Signaling Network", compares the signaling network of 188 head neurons, built
from the q-values of the signal propagation atlas of Randi et al. 2023, with
the anatomical connectome, and reports that the two differ in triad motifs, in
the communities of a nested stochastic block model, in feed-forward structure
along the sensorimotor path and in their rich clubs, which share only AVEL and
AVER. The claims were written from a text whose body is the arXiv preprint
2412.14498v2, without a PDF, and from the paper's code at commit 35e87ca, whose
scripts load precomputed networks, q-values and observation counts that are not
in the repository; the claims check added four claims, for 38, and the author
added the link claim. The q-values cannot be recomputed from the dandiset, so
every signaling claim uses the released atlas (reading (b)), which has 1154
edges where the paper has 1151. Reproduced are the network size and density,
the clustering and small-world coefficient (C 0.1347, sigma 4.624), the triad
distributions, the absence of feed-forward signaling, the sampling control,
the rich club cell classes, the near-disjoint rich clubs, the degree
correlation (r = 0.2186) and AVE as the most connected pair, the last two only
under the assumed EM datasets and AVE only summed over the bilateral pair.
Partial are the broadcaster and integrator test (amphid p = 0.0046, pharynx
p = 0.073), the signaling rich club (tiers of 16 and 5 neurons, but the one-SD
rule fails at k = 4) and the degree against observations (r = 0.7021, 10 of 16
rich club neurons well above the line). The 21 claims on the communities and
what depends on them are blocked as `not_runnable`, because graph-tool has no
distribution on PyPI, and three threshold-control claims for missing data.
Round 1 held that `not_runnable` was not an allowed reason, that about 12
community claims could be tested from the memberships printed in Tables 1 and
2, and that one pair of `rich-club-controls` could be run; in reply the
notebook printed the 0 graph-tool files on PyPI, the memberships were not used
as they are the paper's own results, and the pair was run (8 of 14 anatomical
rich club neurons kept and 5 new, against 9 of 15 and 4 new in the legend of
Extended Data Figure 12a), with the claim kept blocked. The notebook also came
to list what the atlas pickle and the three repositories hold (no q-values)
and to compare its neuron lists with the paper's code (identical). Round 2
withdrew the objection on `not_runnable`, asked that `ed6-anatomy-feedforward`
be marked assumed, and found sentences the outputs did not support, all
corrected; while checking the edge-swap port the author found that the
anatomical network had been rewired with the signaling network's 2000 swaps
where the code uses 6000, and the rerun changed no outcome. The author's run
took about 50 minutes (08:08 to about 08:57 UTC) and no step failed; the
notebook ran in 6.2 min with 1.2 GB peak memory at first, 6.2 min after round
1 and 8.2 min at the end.

The dataset was converted by CatalystNeuro (catalystneuro/leifer_lab_to_nwb).
The control recordings without stimulation, against which Randi et al.'s
q-values are computed, are not in the dandiset, where all 110 recordings have
stimulations, so the signaling network the paper uses and its threshold
controls cannot be computed from it, and no public source of the q-value
matrix was found. The cited version does not say which neuron each
stimulation targeted; version 0.240930.1859 adds a targeted ROI id for 2815 of
the 5614 stimulations, 2090 of those ROIs have a label and 1813 a head neuron
name. 23 of the atlas's 188 neurons never appear as a labeled stimulation
target although the atlas gives them 46 out-edges, and 134 of its 1154 edges
(12%) have no occurrence in the dandiset; where they overlap, the atlas
amplitudes agree with the recordings (Spearman rho 0.524). In the cited
version the green and red signals hold interpolated values for the frames
that were not measured, 17% to 68% of frames and ROIs per file (mean 42%),
with nothing to mark them; the later version keeps them apart. Three
recordings have raw imaging but no segmentation file (sub-20
ses-20210917-132736, sub-23 ses-20211008-115929, sub-33 ses-20220330-110253),
487 activity ROI labels name a bilateral class without its side, 35 are
numbers and 272 are other text with no description, and two subjects (sub-24
and sub-25) give the strain "none" where the other 108 give AML462. pynwb
4.2.0 cannot build the segmentation files from their cached extension
specifications, and they were read with h5py. The stimulation times share the
clock of the signals in 108 of 108 recordings with target ids, and no
recording is deposited twice. In the paper, the Results give the rich club
tiers as degree "25 or higher" and "40 or higher", which gives 22 and 7
neurons, where 16 and 5 have degree above 25 and above 40, as the Figure 5
legend and the code define them. Three questions are put to the paper's
authors: which q-value matrix or atlas file the analysis used, and whether the
q-values can be published; which four EM datasets and which gap junction
direction were used, since with the White 1986 N2U adult or one-way gap
junctions several reported values are not met; and which degree thresholds
define the rich clubs of the control networks.

The author's points on the protocol: it does not say whether the author may
change a claim's `data` field when an outside atlas stands in for the dataset,
and it was left with a deviation recorded; nor whether a column may be taken
from a later version than the cited one, and only the stimulation target
column was, listed under `inputs`; link claims are described for labels and
matching, not for an outside network that replaces the analysis, and one was
written and added to `depends_on`; a claim with no criterion was judged on the
paper's test with full and partial defined by the author; it does not say
whether a substitute is allowed for software that cannot be installed with uv,
and one was written only for the rich club rewiring; a criterion with no
partial clause that failed one condition at k = 4 was judged partial; and the
severity of unmarked interpolated values sits between critical and major, and
major was chosen since the later version fixes it.

---

With the signaling network taken from the atlas released with Randi et al. 2023, the paper's main network comparisons held up: its size and small-world structure, triad motifs that differ from the connectome's, and signaling and anatomical rich clubs that share only AVEL and AVER. The atlas could not be rebuilt from the dandiset, which lacks the unstimulated control recordings behind its q-values. The community findings, six signaling communities mostly distinct from the anatomical ones, could not be tested because the block model's software could not be installed. Pharyngeal neurons as broadcasters fell short of significance (p = 0.073), and AVE as the most connected pair in both networks rests on an assumed choice of connectome datasets.
