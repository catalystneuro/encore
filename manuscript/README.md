# Numbers for a paper on the registry

`analysis.ipynb` computes every number and figure a paper on the registry would cite, from the registry's own
files at one commit, with the site's loader (`tools/build_site.py`), so that they match encorescience.org. It
writes `out/numbers.json` (the numbers to quote), `out/per_dataset.csv` and three figures.

```bash
pip install -r manuscript/requirements.txt
python manuscript/make_notebook.py      # the notebook is written from this script; edit the cells there
jupyter nbconvert --to notebook --execute --inplace manuscript/analysis.ipynb
```

Before submission, freeze the registry at a dated release (archived with a DOI) and re-run this at that commit.
Not computed here yet: the human validation of a sample of outcomes and findings, run-to-run reliability, and the
cost of a run, which is in the Actions logs, not the records.
