I couldn't do this check because there is no claims file for DANDI:001132. `claims/001132/` doesn't exist on this branch, on `origin/main`, or anywhere in the git history.

The earlier claims run (commit 718f6aaf, labelled "success") never wrote the file. Its report in `transcripts/001132/claims-report.md` says a safety classifier blocked the write to `claims/001132/10.1038-s41593-024-01782-5.yaml` and it did not retry.

- **Checker result line:** none. There was no file to run `tools/claims_check.py` on.
- **Changes, by claim:** none.
- **What remains open:** all of it. The file needs a new claims run, or someone writing it by hand, and then a separate check run. I didn't write it myself, because a check has to come from a different reader than the one who wrote the file. The earlier run's report lists what that run should cover:
  - **Text and code:** the text it read (PMC11881784 with the supplement) and the code it read (`braingeneers/AndrewsGengVoitiukEtAl_SourceCode` at 6865bf6).
  - **Planned claims:** about 35.
  - **Open method details:** for example, which trials count, the amplitude measure, the UMAP dimensions, the KS-test correction, and the residual type.
  - **Places where the paper contradicts itself:** for example, the numbering of the supplementary tables, and the 1 ms bins against 200 dimensions.
- **Ready:** no. There is nothing under `claims/001132/` that could be fit for an attempt.

I changed no files.
