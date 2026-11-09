I've written `claims/000402/10.1038-s41586-025-08790-w.yaml`. The quote checker reports 36 claims, 36 quotes and 0 problems. Nothing is committed.

**Text read.** I read the version of record (open access, from Europe PMC, PMC11981939): main text, figure legends, Methods, the legends of Extended Data Figs 1 to 5, and the captions of Extended Data Tables 1 to 3. The supplement is only a Reporting Summary and a Peer Review File, and no result rests on it.

**Code read.** github.com/AllenInstitute/MicronsFunctionalConnectomics at commit be24e51bd7090e9fb32a9099b4e0c6025342629b. It holds only the notebooks for Figs 3f, 3g, 6k and 7a to 7d.

**Claims.** There are 36, all with quotes. 35 have criteria and 29 have expected values. None has statistics: the paper reports no statistical test.
- **16 from the dataset:** the scans and their settings, the mask and unique-neuron counts, the VISp/higher-area split, z drift, the structural stack, the stimulus makeup and repeats, the spontaneous periods, Monet2 directions, oracle reliability (Fig 3f), direction tuning (Fig 3g), the behaviour recordings, and the photodiode decoding.
- **3 with inputs:** they need the CAVE co-registration tables (manual matches, the Extended Data Fig 4 signal-correlation check, Fig 6k).
- **17 elsewhere:** all EM and connectivity claims, plus the automatch and fiducial claims. Their data are at MICrONS Explorer, BossDB and CAVE.

**Details left open, with the readings named:**
- **Neuron consolidation:** how a group's height in z is measured (centroid range, or range plus one mask's height); distance to a group taken from its mean centroid or its nearest member.
- **Masks:** whether the dataset holds all masks with a somatic label, or only the somatic ones.
- **VISp share:** counted over masks, over unique neurons, or as share of the field of view. "Roughly" gets a ±15-point bound that the file sets itself.
- **z drift:** the sections are 10-min blocks or the two halves of the scan.
- **Stimulus duration:** stimulus-table trial times, or nominal clip lengths.
- **Oracle score:** whether a trial is one repeat of the 6 clips together, or each clip is scored apart. The paper's code reads the score from a precomputed table.
- **Fig 3g preferred direction:** the direction with the highest mean response, or the peak of a von Mises fit. The code's fit (radtune VonFit method 3) is not described and its code is not public.
- **Photodiode:** a stored flag, or my own decoding of the signal.
- **Extended Data Fig 4:** "nearest unit" by 3D centroid or within the 2D field.
- **CAVE version:** 1181 (what the code uses) or the latest public one.
- **Automatch precision:** the meaning of "attempted" (the unit or neuron is in the manual table, or its scan was).
- **Fiducial residual:** the 3.8 µm is a leave-one-out residual, or the residual after the third stage of the transform.
- **Synapse matching:** overlap with the annotation, or within 100 nm.
- **"Before proofreading" root:** the earliest materialization, or the root before the first edit.
- **Axon length:** from the released skeleton labels, or from NEURD.
- **Fig 6h cell classes:** which class table is meant.
- **The 94 axons:** fully extended only, or fully or partially extended.
- **"More than 900,000" connections:** synapses onto typed cells (the code's edge list sums to 812,686), or all output synapses.
- **Fig 6f and Fig 7a to c:** the paper gives a range with no share and names no measure. The 90% share and the same-layer measure are bounds the file sets itself, and it says so.

**Missing from the paper:**
- **Extended Data Table 1:** its cells (per-scan parameters) are not in the text and there is no PDF, so the scan claims use the Methods' figures for each group of scans.
- **No code** for the oracle score, the direction fits, or any count in the Results.
- **No materialization version** is given for the EM counts.
- **Not said to be released:** the 8,611 manual synapse annotations and the manual cell-class labels, so those accuracy figures are testable only if they are public.

**Inconsistencies in the paper,** noted in the file's opening comment and left unresolved:
- 1,994 somata plus 942 vessels make 2,936 fiducials, not the stated 2,934.
- Imaging ends at P80 in the Methods timeline and P81 in the main text.
- The timeline puts the structural stack after the perfusion.
- The 8.1% of masks excluded differs from the 8.0% the counts give.
