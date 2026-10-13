# Zheng et al. (2022) from dandiset 000207

Tests the findings of [Zheng et al. (2022)](https://doi.org/10.1038/s41593-022-01020-w) that can
be tested on [DANDI:000207](https://dandiarchive.org/dandiset/000207/0.220216.0323), which holds
the spike times of medial temporal lobe neurons and the behaviour of 19 patients who watched
video clips with no boundary, a soft boundary or a hard boundary, and were then tested on what
they remembered.

| Claim | Outcome |
|---|---|
| Order memory is at chance across a hard boundary, with slower and less confident answers (three claims) | Reproduced |
| Scene recognition accuracy is the same for the three kinds of clip | Reproduced |
| 7.2% of neurons are boundary cells; 6.2% are event cells; their distribution over regions (three claims) | Blocked: methods underspecified |
| 13% of neurons respond to clip onsets and almost none to clip offsets | Reproduced |
| The population state shifts after soft and hard boundaries | Partially reproduced |
| Onset responses and latencies of boundary and event cells (two claims) | Blocked: metadata insufficient |
| Recognition against time since the boundary; firing, state shifts and reinstatement against later memory (six claims) | Blocked: metadata insufficient |
| Cells outside the medial temporal lobe; theta phase locking; similarity of foils (three claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method. It has been checked in two
rounds by an independent agent, which agreed with every outcome.

The cell counts were computed, but the procedure behind the paper's counts could not be
determined. The laboratory's published code only plots rasters, and no reading of the Methods
tried in the notebook gives a chance level near the paper's 2.11%, so those three claims are
blocked. Under a looser reading the data do hold boundary and event cells beyond chance, at a
lower proportion than the paper's.

The notebook pins version 0.220216.0323, the one the paper cites. In the most recent version
the spike times of three subjects are shifted against the trial tables; the notebook shows this.
The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000207-zheng-2022-01.yaml`](../../attempts/000207-zheng-2022-01.yaml).

- `reproduce_zheng_2022.ipynb`: the analysis. It takes about four minutes.
- `cogboundary.py`: loading the sessions, the permutation tests, the definitions of boundary and
  event cells with their chance level, firing-rate traces, and the state-space distance. Other
  notebooks on this dandiset can import it.
