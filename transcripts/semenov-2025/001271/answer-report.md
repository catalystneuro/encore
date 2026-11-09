I answered the one question on 001271 and changed the claims file. Nothing is committed.

**fig2-modulated-locks-to-beats** (asked whether "sustained firing" means firing that is not tied to the beats). The claims file changed: the criterion misread the paper.
- **What the paper means:** it uses "sustained firing" for pure sine waves, where firing runs through the whole stimulus at a rate that rises with the field to a ceiling of 60 to 90 Hz. It then says modulated stimuli, "unlike pure sine waves", did not trigger sustained firing.
- **Why the criterion was wrong:** it used the header's general definition (O4: at least three APs, one in the last 50 ms). The pattern the same paragraph reports for modulated waves, one AP near the peak of each beat, meets that definition. So the criterion contradicted the claim's own statement.
- **What changed:** the criterion no longer uses that definition for sustained firing. A modulated session now counts as sustained firing when its firing is not bound to the beats. That means either more than two APs in one beat (the paper's limit is two per beat), or, in a session with 5 APs or more, at least as many APs outside 12.5 to 37.5 ms of the beats as inside them. These bounds are standard choices, since the paper gives none.
- **What stayed the same:** sustained depolarization is still judged by O4. The statement, source, quote and the other tests are unchanged.

`python tools/claims_check.py` reports 0 problems, both YAML files load, and the question is marked `answered: 2026-11-01`.

Some untracked files (`.bashrc`, `.vscode`, `scripts` and others) appeared in the working tree that I did not create. I left them alone.
