I've written `claims/dvali-2025.yaml` and the quote checker passes: 34 claims, 32 with quotes, 0 problems. Nothing is committed.

**Text read.** `paper/10.1103-6wgv-b9m6.txt`. Its header says "version of record", but only the abstract and the reference list come from the publisher. The body is the arXiv preprint 2412.14498v2 (12 Aug 2025), which has the full Results, Methods, Tables 1 and 2, and Extended Data Figures 1 to 14 plus Extended Data Table 1. I used those Extended Data in place of the publisher's supplement. There is no PDF, so numbers that appear only inside figure panels are not used.

**Code read.** github.com/SophieDvali/FunconnNetworkAnalysis at commit 35e87ca. The scripts all load precomputed files that are not in the repository: the two adjacency matrices, the q-values, the observation counts and the community-motif tables. So the code that builds the networks, computes the q-values, classifies community motifs and computes the adjusted Rand score is not available. Where the code does fix a detail, the file follows it: degree is in plus out, the rich-club cutoffs are degree > 25, > 40 and > 62 for anatomy, and the shuffle counts and tests are as in the code.

**Claims.**
- 2 claims have an `inferred` note instead of a quote: the Table 1 membership and the Extended Data Table 1 control odds.
- 10 have statistics and 27 have criteria.
- What each claim's test uses:
  - 12 rest on the dataset alone (the signaling network).
  - 7 also need the cell-class and role labels (`with_labels`).
  - 10 compare against the connectome (`with_inputs`).
  - 5 are about the connectome only (`elsewhere`).

**Details the paper leaves open, and the readings named:**
- **Where the q-values come from:** (a) recompute them from the dataset with the method of Randi et al. 2023, or (b) use the q-values that paper released. Which strains are included is also unstated: wild type only is the main reading, with unc-31 recordings included as a variant.
- **Rich-club tiers:** "degree 25 or higher" in the Results against "k > 25" in the legend and code; both are named. The number of rewired null networks is 1000 in the Methods, 100 in the legend and 500 in the code. The Methods value is used and the others are variants.
- **Community motifs on a directed network:** the between-community density counts either edges from r to s only, or edges in both directions.
- **Feed-forward measure:** the legend's count of forward over backward edges is used; the code's other measure is a variant.
- **Forcing the number of communities** (Extended Data Fig. 4): the code doesn't show how. The reading is graph-tool with the first level fixed at B blocks.
- **Rich-club thresholds in the control networks:** not given; the reading is the original cutoffs.
- **Counting observations and stimulations:** the paper doesn't define it here; a reading is named.
- **Adjusted Rand score:** not in the code; the standard ARI is used.
- **The community detection is random and unseeded**, so results can vary run to run. Each claim that depends on it asks for at least five runs.
- **Three criteria use choices the paper doesn't make**, and each says so: a Jaccard ≥ 0.5 cutoff for matching recomputed communities to Table 1, a chi-square test for the triad distributions, and a "majority of runs" rule.

**Missing from the paper that some claims needed:**
- The construction of the q-values is only in Randi et al. 2023 (reference 27), not in this paper or its code.
- The connectome is outside data. The paper doesn't name which four EM datasets it used ("three adults and one L4" from White 1986 and Witvliet 2021), nor how gap junctions get a direction.
- The triad counts in Extended Data Fig. 1 can't be matched to triad types from the text.
