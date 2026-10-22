I couldn't do the check: there is no claims file for DANDI:001282. The folder `claims/001282/` doesn't exist, and nothing in the git history ever touched it.

**Checker result:** not run, because there was no file to give it.

**Why there is no file.** The earlier claims run (commit 8915b891, report in `transcripts/001282/claims-report.md`) stopped on purpose without writing claims, as protocol step 1 requires when the supplement is missing. I confirmed what it found:
- `paper/10.1038-s41592-025-02614-5.txt`, the version of record, is only the paywalled page: abstract, figure titles, data and code availability, and references. It has no Results or Methods, and there is no PDF.
- `paper/10.1101-2023.10.24.563768.txt`, the bioRxiv preprint, has the main text, legends and Methods. It has no supplement, only a "Supplementary Material" link at line 450.
- The NHP insertion results that this dataset holds depend on Supp. Figs. 11 to 13. Those cover the second insertion recording, the Kilosort drift-tracking failure and the anatomical trajectory. None of them are in either text.

**Changes:** none. I added no `checks` entry, because there is no file to add it to, and writing claims is the claims role's job.

**Open:** a claims run needs the full text with its supplement first. The earlier run suggests either of these:
- the PMC author manuscript PMC13055889 (NIHMS2068114) with its supplementary PDF; `claims/001290/` was written from these
- the bioRxiv supplementary PDF together with the preprint

**Ready:** no. Nothing exists yet that an attempt could use.
