I ran `tools/readme_row.py 000114 --write`, which added this row to README.md: 1 reproduced, 3 partially, 3 not reproduced, 12 blocked. I then added the subsection below to the end of `docs/pilot-notes.md`. Nothing is committed.

The `catalystneuro` field for 000114 names a contributor (Benjamin Dichter) but no conversion repository, and none of the other sources name one either. So the opening uses the "is a contributor" wording that earlier subsections use in the same case.

### 000114, Carcea et al. 2021

One claim reproduced, three partially, three not reproduced and twelve
blocked, all on the dandiset. Round 1 gave its own outcome for each claim
from the notebook with its conclusions removed and agreed with all 19; round
2 agreed again and nothing was proposed, so there was no third round. The
paper reports that oxytocin neurons of the paraventricular nucleus (PVN) in
virgin mice co-housed with a dam and litter are activated by shepherding by
the dam, by nest entry and by the dam's pup retrievals, that silencing them
delays pup retrieval, and that virgins can learn to retrieve by watching
dams, which depends on oxytocin in the auditory cortex. The naming of the
behaviour labels, the fractions of units activated during nest entry,
shepherding and dam retrieval, firing after shepherded against voluntary
nest entries, and the rates of shepherding and of retrieval by the dam were
tested on 194 units from 4 virgins in 7 sessions, with oxytocin and other
PVN units pooled. The ten claims on optically tagged oxytocin units, the
behavioural cohorts, unit recordings during observation, the auditory cortex
and the colliculus are blocked as `data_missing`, and virgin chasing of the
dam and the projection photometry of Fig. 4i as `metadata_insufficient`.
Some outcomes rest on weak ground: in `ed7a-nest-entry-fraction` leaving out
the 20 units above the code's limit of 1,048,500 spikes gives 24.1%, inside
tolerance, and counting V111 once gives 28.8 to 30.3%;
`fig2j-shepherded-entry` would pass without V116 03102018, whose clock is
not known (p = 0.0237); in `ed7a-dam-retrieval-fraction` 9 of the 13
activated units come from the single retrieval of V111 03032018, share a
median 71% of their spikes pairwise within 0.1 ms, and the retrieval falls
on one of the session's largest synchronous bursts; and
`fig1j-shepherding-rate` passes its t-test over sessions (p = 0.0292) but
not over mice (p = 0.193). The author used the full text in PubMed Central,
the Source Data for reported numbers only, and the paper's code on GitHub
for the label names and the parameters of the shuffle test.

The dandiset was converted by CatalystNeuro (Benjamin Dichter of
CatalystNeuro is a contributor). It holds units for 4 of the paper's 17
recorded virgins (228 units in 8 sessions, against 541 in the paper) and
does not say which recordings were deposited or why; the optical tagging
recordings and the identity of the 21 OT-PVN units are not in it, so no
oxytocin-specific result can be tested, and the paper's code reads that
identity from a spreadsheet that is not public. The behaviour labels have no
description, and shepherding, nest entry and dam retrieval can be named only
from the paper's code; one file (V116 03122018) carries both the code's
labels and the paper's names. No test established that spikes and
annotations share a clock in any session, and in V116 03102018 the raw
voltage lasts 4.46 h while spike times and annotations run to 13.4 h. Units
in V110 and V111 have a median 7.0 to 9.2% of inter-spike intervals under 2
ms and 79 to 90% of their spikes within 0.1 ms of another unit's, although
the Methods say such spikes were removed, and V111's three sessions hold 31
units each with spike counts correlated 0.93 to 0.97, with nothing saying
whether they are the same units. The Methods cap nest entries at 40 s, which
the code does not, and on this data the cap changes the fraction activated
from 1.0% to 21.6%. Other findings: session start times disagree with the
dates in the session ids; the units table holds spike times and a name only,
and every electrode location is "unknown"; every subject is described as
co-housed, including the six photometry animals of the observation
experiment; photometry fibre location, fluorophore, wavelengths and gain are
"unknown" or NaN, the trace is stated in watts with values near 1000, and
commanded_voltage varies from 0.07 to 482 within sessions; and which
photometry animals learned to retrieve is known for 2 of 6, so the groups of
Fig. 4i cannot be formed.

In exploration, h5py's visititems hung on the large ecephys files, and a
first survey of all files hit the one-hour timeout before a plain group walk
replaced it. Untracked files in the repository root, which the author took
to be sandbox mounts, were left alone. The author's points on the protocol:
no rule for when the clock check fails to settle alignment; a data check that
showed counts and durations deciding some claims before the criteria were
written; fractions split by a label the dandiset lacks; whether
reference-only sources belong in `inputs`; a claim blocked for two reasons;
the choice between `data_missing` and `metadata_insufficient` for a label
that is absent while the units are present; units probably the same across
days, which the duplicate rule does not cover; and content comparison of
versions at 387 GB.
