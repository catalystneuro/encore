I added the 001075 row to README.md (`4 | 4 (+1) | 0 (+1) | 7`) and appended this subsection to the end of docs/pilot-notes.md. Nothing is committed.

### 001075, Randi et al. 2023

Four claims reproduced, four partially and seven blocked on the dandiset.
With outside data, counted apart: one partially reproduced and one not
reproduced. Two claims on data in the paper's OSF repository: one reproduced
and one blocked. Round 1 gave its own outcome for each claim from the notebook
with its conclusions removed and agreed with 15 of the 19. It found that
`osf-link` passed on 87.4% agreement only because all 2,812 manually located
targets agree by construction, while targets found from the position, which
the claim states, agree in 1,101 of 1,667 (66.0%), and the author changed the
claim from reproduced to partially reproduced. Round 1 also asked for a check
of RID labels, which showed the earlier blocking notes wrong: the dandiset
labels 11 ROIs RID and 8 stimulations in 5 animals target one, and the unc-31
export labels RID in 28 stimulations in 8 of its 18 recordings, so the author
wrote criteria before computing any RID response and moved `fig4-rid-wt` from
blocked to partially reproduced and `fig4-rid-unc31` from blocked to
reproduced. The author kept `not_runnable` for `edfig6-kernel-stereotypy` and
`fig6-spontaneous`, where round 1 would have given `other` and `data_missing`,
and round 2 accepted both, the first with a reservation as no
reimplementation of the kernel fits was tried. Round 2 agreed with all 19 and
nothing was proposed, so there was no third round. The paper builds a signal
propagation atlas of the C. elegans head by stimulating single neurons in 113
WT-background animals during whole-brain calcium imaging, and compares the
measured functional connections with the connectome, with a
connectome-constrained model and with unc-31 mutants, screening for
extrasynaptic-dependent propagation. The recording protocol, the pair counts, the three
example responses of Fig. 1, spatial specificity, the link to the paper's
Source Data and OSF export, the inhibitory fraction and the RID responses were
tested. Every claim that needs q values is blocked as `data_missing`, as they
rest on unstimulated control recordings that are public nowhere, and so is the
model comparison, whose predictions are not public. Some outcomes rest on weak
ground: `fig1f-aver-avar` rests on 7 trials (Wilcoxon p = 0.22);
`fig1g-saadl-ollr` on 5 trials (p = 0.44), and the code's decaying correction
flips its sign to +0.014; and `fig4-rid-unc31` is met barely, with URX 0.031
in unc-31 against 0.032 from a single WT trial and Mann-Whitney p of 0.31 or
higher. The author used the open access full text (PMC10632145) with its
Source Data, and took the head neurons, the response classifier and other
parameters from the paper's code.

The dandiset was converted by CatalystNeuro (catalystneuro/leifer_lab_to_nwb).
The unc-31 recordings, the spontaneous recordings of Fig. 6 and the
unstimulated control recordings are not in the dandiset, and the controls,
which every q value in the paper needs, are not on OSF either, so the paper's
central statistics cannot be recomputed. For about half of the stimulations
the files give only a target position, not the stimulated ROI; the paper's
assignment uses tracking matches that are not in the dandiset, and from the
position 66% of these stimulations get the paper's ROI. The paper's export
marks 950 stimulations as excluded, which the dandiset does not mark. Three of
the 113 subjects (20, 23, 33) have only the raw imaging file, without traces
or stimulation table. In five recordings the labels reached through
`neuropal_ids` and the NeuroPAL table differ from the export for every named
ROI: subjects 64, 76 and 77 have almost no labels (4, 0 and 15 distinct names
against 70, 102 and 87 exported), and in 86 and 91 most names are shared but
sit on other ROIs; in subject 11 the ROI count (161) differs from the export
(200). The traces have unit "n.a." with no description of their processing,
and nine recordings hold values down to -196,646; 3,173 of 433,216 observation
rows have F0 at or below zero, and 897 of 14,039 traces cannot be corrected
for photobleaching with the paper's fit, though the variants without them
change no outcome. Even so, the inhibitory fraction of `fig2d` is 15.1% from
the dandiset against the 11.5% the Source Data means give for the same pairs,
and every variant gives 13.4% to 15.8%. Other findings: `neuropal_ids` holds
"merge" in 63 recordings and "check", "I4" or "RIAR" in others, and 49 ROIs in
21 recordings carry the label "target"; `depth_in_um` runs from -0.875 to
0.875, which cannot be micrometres in a volume imaged from 2.5 to 37.5 um, and
122 stimulations have the target position (0, 0); every stimulation is stored
as 0.5 s at 1.2 mW, constants written by the conversion, so the 0.1 to 0.5 s
AFD pulses of the Methods are not represented; the red channel is described
with the indicator GCaMP6s though it images tagRFP-T, two subjects have strain
"none", every age is P1D and one label confidence is 11; and thirteen
recordings last longer than the paper's "up to 40 min" (up to 48.7 min) and
three have timestamp gaps of up to 8.4 s.

The notebook ran in 404 s in the first clean run, 721 s after round 1 and
634 s after round 2. The paper's pumpprobe package would not install, and a
cell added after round 2 shows that it builds once the numpy headers are added
by hand but cannot be imported, as mistofrutta, wormbrain and wormdatamodel do
not build; OSF returned HTTP 429 for files fetched one at a time, so the
notebook streams a single tarball checked by its md5. Round 2 found statements
the outputs did not support, among them that every variant of
`sourcedata-link` falls in the partial band, which fails for the
detected-responses-only variant, and a deviation of `edfig2ij` that missed
reading (c); these were corrected, while counts differing by one between the
verifier's copy and the re-run were kept, with the Summary stating the
difference. The author's points on the protocol: no rule for the paper's own
published results such as Source Data q values and means; claims that need
data on OSF and data public nowhere, which the rule that elsewhere is never
`data_missing` does not fit; no guidance for an identifier that is absent but
can be inferred from the dandiset; whether a list of head neurons from the
paper's code is an input; a legend percentage that does not say which
neighbours it refers to; a default 10% tolerance meaningless for a count of
113 animals; block reasons resting on checks run outside the notebook; two
published versions with the same files, all re-uploaded; a clock check by
stimulated-neuron response rate in place of decoding; and no rule for outside
services that rate-limit.
