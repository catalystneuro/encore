I couldn't run the check because there is no claims file for DANDI:001349.

- **No file to check:** `claims/001349/` does not exist. The checker has nothing to run on, so there is no result line.
- **Why:** the last commit (`8847a94c`) is the claims run, and its report (`transcripts/001349/claims-report.md`) says it stopped at Reader step 1 and wrote no claims. The reason given is that the paper's supplement (Document S1, with Figures S1 to S9 and their legends) is missing from `paper/`.
- **That reason holds:** `paper/10.1016-j.isci.2025.112104.txt` contains only the label "Supplemental information Document S1." and a link to the DOI. There is no supplement text and no PDF. The pairwise correlation and mutual information results, the subnetwork checks, the CNO results, the robustness and cell-identity analyses, and several Methods details (event detection threshold, quiescence selection) are all in that supplement.

**Changes:** none. There are no claims, so there was nothing to correct and nowhere to add a `checks` entry.

**Open:** Document S1 needs to be put under `paper/` and the claims role re-run. That run should also read the code repository the paper links for its statistics, https://github.com/EdnaHuang/SubnetworkAssembley2024 (folder `Statistical_Script_Data`), and record which commit it read.

**Ready:** no.
