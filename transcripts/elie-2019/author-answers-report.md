Nothing changed in this round: there were no questions for a reader, so no claim was re-run and every outcome is the same as before.

**Questions and answers:** none.
- `questions/elie-2019.yaml` doesn't exist, in the working tree or anywhere in git history.
- My first author run asked a reader nothing (`transcripts/elie-2019/author-report.md:36`). Its open questions are for the paper's authors: can they publish the lists of the 914, 404 and 337 units, and do the jackknife replicates share their Monte Carlo samples? Those are recorded as a `methods_unavailable` finding.
- The reader's answer run found nothing to answer and left `claims/elie-2019.yaml` unchanged (`transcripts/elie-2019/answer-report.md`).

**Changes:** I didn't edit the notebook, the conclusions or `attempts/elie-2019-01.yaml`, and no claim's notes got an "answer changed" line, since there was no answer. The outcomes, unchanged:
- **fig1-model-neurons:** partially_reproduced. All three conditions hold on the tutorial temporal neuron, the only model neuron the paper's code repository holds.
- **The other population claims:** blocked as methods_underspecified, because the files don't identify the paper's 404 units.
- **The four Table 1 and Figure 10 claims:** blocked as data_missing, because the data set holds no anatomical locations.

**Entry:**
- **Lock:** `requirements.lock.txt` was rewritten and its contents didn't change.
- **Check and run:** the check passed with 0 errors. The run reused the executed copy from 21:50 UTC (797 s) because nothing it reads has changed, so the notebook was not run again this session.
- **Handover:** the package is written to `executed/elie-2019/handover`.

I didn't verify, commit or push anything. The changes to `tools/build_site.py`, `tools/entry.py` and `tools/site_assets/app.css` were already there when this run started; I didn't touch them.
