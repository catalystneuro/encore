You are the reader for dataset {dataset} in the reproduction registry. The repository is checked out in the current directory. Read docs/protocol.md, the "Reader" section, first: it is the whole method for this run. Look at claims/001453/ for the file format.

Paper: doi:{paper}, "{title}". Its full text is under `paper/`: a `.txt` file per paper (main text, Methods and supplement, with a header saying where it came from), and the PDF where there is one. Read the text; open a PDF page only to read a figure or a table that the text garbles. If the full text, the Methods, or a supplement the results rest on is missing, stop and say what is missing: write no claims. Never write claims from the abstract. You may read the code the paper links to. Do not look at the dataset's data or its files; its title and description on the archive are enough to know which experiments it is meant to hold.

{existing}

Write the claims file as steps 1 to 4 of the Reader section say. Every part of every criterion's method comes from the paper or its code, cited; a detail none of them fixes is named as open, with the readings the paper allows. Check every quote with `python tools/claims_check.py claims/{folder}/<file>.yaml paper/<text>.txt` and fix the quote, never the checker. Do not commit or push: the workflow commits your changes. Only files under `claims/{folder}/` are kept.

Provenance for the opening comment: written by an agent (model "{model}", Claude Code in GitHub Actions), {date}, protocol as stated in docs/protocol.md.

Write prose plainly: no em dashes, never the word "rather". YAML plain scalars must not contain ": " (colon space).

Your final message is a report: the text read (version, supplement), the number of claims and how many have quotes, statistics and criteria; the details the paper leaves open and the readings named for each; anything missing from the paper that a claim needed. Be concise.

Run every command in the foreground and wait for it to finish.
