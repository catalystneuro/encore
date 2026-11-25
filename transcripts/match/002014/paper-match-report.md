I judged the one paper the archive links to DANDI:002014 as `primary`, and wrote the verdict to `papers/match/002014.yaml`. The file passes `python tools/paper_match.py validate` (it ran without errors).

**doi:10.1016/j.jneumeth.2025.110467** (Choi et al., J Neurosci Methods 2025): **primary**, `by: agent`.

- **Deciding evidence:** the paper's Data availability section says "Data used in this paper are available at repositories in zenodo ( 10.5281/zenodo.14825992 )". The archive metadata says the dataset holds those same processed Zenodo data, plus the raw recordings they were derived from.
- **Why the checks left it open:** the script saw that the paper names a Zenodo record and not this dataset. That record is part of this dataset, so it does not point to other data.
- **Supporting evidence:** the paper's recording figures (Figs. 8 and 9) come from monkey T, 497 days after electrode implant: dopamine measured by fast-scan cyclic voltammetry (FSCV) at site c8ds, spikes at c5d, and beta-band local field potentials (LFP). The dataset's only file is one monkey T session, `sub-Monkey-T_ses-09272024`, with the same site names.
- **Not testable from the dataset:** the surgical, fluid-drainage and bacterial-culture observations, which cover both monkeys T and J, are not in the dataset.

I did not commit anything; the workflow commits the match file.
