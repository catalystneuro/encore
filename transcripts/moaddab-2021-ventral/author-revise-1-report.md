I've worked through all of the verifier's round-1 points. The entry re-runs cleanly (0 errors, 24 s) and the handover is rebuilt. Nothing is committed.

**Outcome changes**
- **supp6-low-nosepoke-pauses**: changed from reproduced to partially reproduced, as the verifier gave it. Low neurons show no inhibition after a pause under any reading. Intermediate neurons do show it under the authors' own pause scaling and under the 5 s / (ii) reading. The 10 s reading has only 25 pauses across 14 of the 34 Intermediate neurons, too few to show that an effect is absent.
- Totals are now 28 reproduced, 15 partially reproduced and 2 not reproduced, with none blocked. The README, notebook summary and record all match.

**Disagreements kept and recorded**
- **fig2-excited-inhibited-split** stays reproduced (resting on A1). The claim is about the paper's 257 neurons, and on those one of the claims file's readings gives 130/127, within tolerance. On the Methods' 271 neurons no reading is within tolerance, and the notes say so.
- **supp9-excited-nosepoke-pauses** stays reproduced (resting on A3). With the authors' definition of a pause, no interval lies above zero under any of the three scalings (3367 pauses). Only the 5 s / (ii) reading shows a rise after the pause, and the notes give it.

**Outputs added**
- A cell that prints the lines of the authors' two scripts that the notebook and helper cite.
- A comparison of neuron groups: the authors' split and the claims file's Hz split put 25 of the 257 neurons in different groups. The notebook also shows how groups A and B overlap.
- A cluster check: the claims file's reading gives exactly the paper's cluster members. The partition k-means finds with more restarts (lower error) moves 20 of the 126 neurons.
- A new section that changes one part of the normalization at a time. Z-scoring single trials, as the authors' code does, puts all seven checked means within the paper's tolerance; Z-scoring trial means, as the Methods describe, puts none there. The baseline length and rounding change little. The code_mismatch finding now names this as the cause.
- Per-neuron pause counts (total, minimum, quartiles, maximum) for every pause reading.
- A chance level for the cue screen: run on windows before the cue, the same screen passes 119 of 435 neurons (27%).

**Corrections**
- The notebook header's claims table no longer shows outcomes.
- A1 is now stated as an exception to "the Methods are the main reading", with the reason.
- Conclusions now say that groups B's clusters do not count towards clusters-differ-in-cue-firing.
- Under scaling (i) the cue-minus-reward difference has no common unit; the conclusion and notes now say so.
- The fig6b conclusion and notes wrongly said the late-cue safety interval contains zero. It lies below zero under the three-cue pool and the authors' normalization.
- The unused expression in the Fig. 1f cell is removed.

**Questions for a reader**: these are new in `questions/crcns-bf-3.yaml`, with no claim changed:
- the 10% tolerance on R² (fig5d-f, fig6g)
- the onset window for supp5
- whether a drop below zero in safety firing contradicts fig6b
- the 100-restart reading for kmeans when the Methods name Matlab's one-start default
- whether scaling (i) belongs among the readings for fig6-excited-peak-cue-vs-reward

**Not done**: the four likely duplicate unit pairs stay in every population, as the paper counts them. The verifier marked this as not affecting any conclusion, and a finding already reports it.
