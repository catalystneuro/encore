You check the claims file for dandiset {dandiset} in the reproduction registry against its paper, as docs/protocol.md, "Reader", step 5, says. Another agent wrote it; you have not seen its reasoning. Be skeptical.

Paper: doi:{paper}, "{title}". Its full text is under `paper/` (a `.txt` per paper, and the PDF where there is one). The claims file is in `claims/{dandiset}/`. Do not look at the dandiset's data.

1. Run `python tools/claims_check.py claims/{dandiset}/<file>.yaml paper/<text>.txt`: it validates the file and checks every quote word for word and every recorded p-value and interval against the text.
2. For each claim, check against the paper: the statement says what the paper says, no more and no less; the source points at the place; the statistics are the paper's and are results, not thresholds used to count units; the expected values and tolerances are the paper's numbers; every part of the criterion's method (selection, measure, test, windows, bins, thresholds, comparisons) is taken from the Methods, legends, supplement or code, as cited, and none is made up; details the paper leaves open are named as open, with the readings it allows.
3. Check that each of the paper's main findings has a claim, and that no claim comes from anything but this paper.
4. Correct what you can show is wrong, from the paper. Then add an entry at the end of the file under `checks` (a list): `date` {date}, `kind: agent`, `model` "{model}", `ready` (true when the file is fit for an attempt), and `changes`: one line per change with its reason, and one line per problem you could not settle. Do not change a claim's id.

Only files under `claims/{dandiset}/` are kept. Do not commit or push. Write prose plainly: no em dashes, never the word "rather". YAML plain scalars must not contain ": ".

Your final message is a report: the checker's result line; the changes, by claim; what remains open; whether the file is ready. Be concise.

Run every command in the foreground and wait for it to finish.
