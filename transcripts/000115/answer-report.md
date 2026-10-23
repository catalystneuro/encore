I answered both questions, setting `answered: 2026-10-22` on each. `claims_check.py` reports 33 claims, 33 quotes, 27 statistical values and 0 problems. Nothing is committed.

1. **Which sessions are "sessions 1 and 3" of subject 1 (fig1d-sessions-blocks).** The paper does not say. The Methods only describe the two sessions: one with fewer than 75% of frames decoded on the same segment, and one where not all arms were visited. The code picks sessions using a `$gooddecode` flag and a per-animal `$session` field, both from task records that are not in the repository, so the code does not settle it either. The criterion now names two readings:
   - **(a)** the first and third run sessions in order of recording;
   - **(b)** the two sessions that match the Methods' description.

   Both are to be run, and (b) decides when they differ. That tie-break is my choice, because (b) is what the Methods describe.

2. **Which trial closes the old block after a goal change.** The code settles it as reading (b): the first valid trial after a goal change always belongs to the old block. In `label_trial_interval.m` (its `goalbounds`) and in `dfa_ripcontent.m` (`[1 ctemp(1:end-1)]`), that trial is labelled n + 0.9 if it goes to the old goal and n + 0.3, 0.5 or 0.8 if it goes to another arm. The trial after it starts the new block's search. I wrote this into the claims file's opening comment and the fig1d-sessions-blocks criterion, without changing the statement or the expected values.

I read the code at LorenFrankLab/Gillespie_Neuron_2021, commit 1be6a6a, which I cloned into a temporary directory.

`git status` also lists untracked files I did not create (`.bashrc`, `.idea`, `scripts`, and others). I left them alone.
