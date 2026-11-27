I wrote `claims/souza-2026.yaml`. The quote checker passes it: 38 claims, 38 quotes, 0 problems. Nothing is committed.

**Text read.** I read the version of record (Front. Behav. Neurosci., published 28 Oct 2026): the main text, Methods 2.1 to 2.8, Results, Discussion and the legends of Figures 1 to 3. The supplement is a single figure (S1, choosing the number of NMF components, ranks 2 to 8), and only its legend is in the text. That figure's image is missing, but it only supports the choice of six archetypes and no claim rests on it. There is no PDF, so no figure was opened and no number comes from a figure. There was no code to read: the paper says it is "available from the corresponding authors upon reasonable request" and links no repository.

**Claims.** There are 38: 1 link claim (sessions, mice and unit counts) and 37 findings.
- **Quotes:** all 38 have one; none is marked inferred.
- **Statistics:** 10 claims carry 13 statistics entries (Kruskal-Wallis, paired Wilcoxon, permutation and FDR p-values).
- **Criteria:** 36 claims have one. The other two rest on their expected values alone.
- **Expected values:** 32 claims have them, at 10% tolerance. The exceptions:
  - Exact counts for the link claim.
  - Tolerances capped where 10% would pass 100% or 1.
  - Peak times judged within 200 ms, because 10% of a −45 ms peak is smaller than one 10 ms bin.
- **Outside data:** the layer claims are `with_inputs`, using the Allen CCFv3 25 µm annotation volume; the paper gives no release.

**Details the paper leaves open, with the readings named:**
- **Session and unit choice:** how 103 sessions were picked is not stated, and no unit quality filter is named. Readings: all units in the six areas, or units passing the Allen default quality thresholds. The link claim must match 103 / 54 / 54,039 exactly.
- **ISI-shuffle span:** the active block (the circular-shift null is wrapped within it) or the whole recording.
- **"Units testable in both contrasts" (33,502):** three possible denominators.
- **Miss-trial pseudo-reward time:** the session median latency, as the text implies.
- **Waveform duration:** computed from the mean waveform, or the value stored in the units table.
- **Median ISI span:** whole recording or active block.
- **Firing rate over the whole recording:** two ways to set the time span; whether the 0.2 Hz filter applies before the rate medians.
- **CV analysis:** minimum number of RW+ units per session and area (1 or 5); how the 20 subsampling draws are averaged; the Results say "sliding window" but I followed the Methods' non-overlapping 10 s windows.
- **CV(t) correlations:** averaged per session or concatenated across sessions; whether same-area pairs belong to the cross block; the test behind p < 10⁻¹³ is unnamed (I used Wilcoxon).
- **Pre/post-stimulus CV (Fig 2F):** window lengths, which image changes, how the CV is formed and whether FDR correction applies are all unstated; the criterion names readings for each.
- **NMF:** initialisation (scikit-learn default or random); peak taken from the signed or the absolute archetype; how weights are normalized; PCA and mixture component counts and how the hard assignment reconstructs a unit; η² definition; number of permutations.
- **Anticipatory label:** pre/post windows not given; three readings.
- **Layer 4 against "the others":** all other layers pooled, or the mean of supra- and infragranular. The paper prints the unmatched layer-4 excess as +0.116 in one place and +0.148 in another, so either counts.
- **Narrow vs broad within each layer:** per-session average across layers, or each session-and-layer as a separate pair.
- **Rho in the latency-jitter control:** read as Spearman, with Pearson as a variant.
- **Change-to-reward latency median:** median of session medians, or pooled over hits.
- **"Nearest lick":** nearest preceding lick, or nearest in absolute time.
- **False-alarm alignment:** to the first lick, or to the session-median latency after the catch change; responsiveness filter run with and without.
- **Lick bout definition and bout baseline:** not defined at all. The gap threshold (250 and 500 ms run) is an assumption, not a reading the paper gives.

**Missing from the paper that claims needed:**
- The autocorrelogram rise time (Fig 1I) is never defined, so that measure is not judged.
- The rate matching used in the layer-4 control is only named, so I took the procedure from the CV section (Methods 2.6).
- The circular-shift null and the smoothing analysis are described as sensitivity analyses but report no results, so they have no claims.
