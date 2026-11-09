There was one question, and the reader's answer changes no claim and no outcome. All four affected claims stay **blocked (`data_missing`)**, as they were before. The entry was locked, checked and run (it passed in 221 s), and the handover was built. Nothing is committed or pushed.

**The question (`tracking-error-dataset1`, also covering `tracking-mean-error`, `tracking-error-challenge` and `behavior-clock-drift`).** I asked whether these claims should take their data from the paper's original data release on Zenodo (ref. 13, doi:10.5281/zenodo.4743837). That release's README lists a `trainset/` folder of tracking-error tables and a behavioral log file for each session.

**The answer.** The claims file is unchanged. The paper names ref. 13 only as the release this dataset "improves on" and never says what it holds. The tracking results are credited to ref. 8, not ref. 13, and the "carefully curated labeled data" the abstract offers names no archive. So the four claims keep their data on the dandiset, and the reader asked me to say in each blocked claim's notes where I looked.

**What I changed:**
- **Notebook:** the `behavior-clock-drift` cell and the cell on the three tracking claims now say where the data were looked for: the dandiset, then the Zenodo README. They also say why that release is not used and that a reader confirmed this. The Zenodo release itself was not read.
- **Attempt record:** the notes of the four claims now state that, and that the answer changed nothing in the test. The finding about missing data now adds that the paper does not say where the training sets are, and that the Zenodo README lists them.
- **README:** no change was needed.

| Claim | Earlier outcome | Outcome now |
|---|---|---|
| tracking-mean-error | blocked, data_missing | blocked, data_missing |
| tracking-error-dataset1 | blocked, data_missing | blocked, data_missing |
| tracking-error-challenge | blocked, data_missing | blocked, data_missing |
| behavior-clock-drift | blocked, data_missing | blocked, data_missing |

In the executed notebook, all the other claims give the same result, in the same order, as the attempt record.

The handover is in `executed/000231-rodgers-2022/handover/`.
