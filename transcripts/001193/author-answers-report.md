There were no questions to act on, so nothing in the attempt changed.

**Questions.** `questions/001193.yaml` doesn't exist, and nothing in the git history shows it ever did. The answer run reached the same conclusion: its report (`transcripts/001193/answer-report.md`) says "I found nothing to answer". That fits my first author run, where I asked a reader nothing because I found no place where the claims file misreads the paper. The claims file `claims/001193/10.1038-s41562-022-01334-6.yaml` was last changed in commit c8ef2971b ("Claims for DANDI:001193, checked"), before the author run, so no claim was amended.

**What changed.** Nothing. With no answers, no claim needed re-running, and I left the notebook, the conclusions, the attempt record (`attempts/001193-zhu-2022-01.yaml`) and the claims' notes as they were.

**Outcomes per claim (earlier outcome / now):**
- participants: partially_reproduced / partially_reproduced
- stimuli-word-frequency: blocked (other) / blocked (other)
- The other 22 claims, from task-structure to nl-low-frequency: blocked (data_missing) / blocked (data_missing)

**Entry checks.**
- `python tools/entry.py lock entries/001193-zhu-2022` rewrote `requirements.lock.txt` with the same content, so git shows no diff.
- `python tools/entry.py all entries/001193-zhu-2022` reported 0 errors, and `reproduce_zhu_2022.ipynb` ran and passed in 90 s.
- `python tools/entry.py handover entries/001193-zhu-2022` wrote `executed/001193-zhu-2022/handover`.

I did not verify my own work and did not commit or push.
