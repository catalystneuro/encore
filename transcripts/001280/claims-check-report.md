I had nothing to check: there is no claims file for DANDI:001280. `claims/001280/` does not exist, either in the working tree or anywhere in git history, so I did not run the checker and made no changes.

**Why there is no file.** The earlier claims run (`transcripts/001280/claims-report.md`) stopped without writing claims, as protocol step 1 requires when the supplement is missing. I confirmed what it reported:
- `paper/10.1016-j.neuron.2024.12.023.txt` (the accepted manuscript) has the main text, STAR Methods and the legends for Figures 1 to 7. It ends at "Supplementary Material 1" with no content, and there is no PDF.
- The legends of Figures 4 to 7 say "n : see Table S1", and Table S1 is not in `paper/`. Several findings appear only in Figures S2 to S7, which are also missing.
- `paper/10.1101-2024.05.08.593085.txt` is the bioRxiv preprint. It is a different version, with different figure numbering and some different numbers, so it cannot stand in for the published paper.

**Still open.** The paper's supplement is needed: the Neuron supplemental PDF for doi:10.1016/j.neuron.2024.12.023, with the Figure S1 to S7 legends and Table S1. After that, the claims run has to be repeated, including a read of the linked code (zenodo 10.5281/zenodo.14522610 and 10.5281/zenodo.14399029), and then this check.

**Ready:** no. I did not create a file only to hold a `checks` entry, because a file with no claims would not be fit for an attempt.
