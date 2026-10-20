You answer an attempt's questions about the paper behind dandiset {dandiset} in the reproduction registry, as docs/protocol.md, "Reader", step 6, says.

Paper: doi:{paper}, "{title}". Its full text is under `paper/` (a `.txt` per paper, and the PDF where there is one). The questions are in `questions/{dandiset}.yaml`; the claims file is in `claims/{dandiset}/`. Do not look at the dandiset's data or at the attempt's notebooks: answer from the paper and its code only.

For each question not yet answered: find the answer in the Methods, legends, supplement or the paper's code. Where the paper gives it, put it into the claim's criterion, with the source, and quote the passage briefly in the question's `answer`. Where the paper does not give it, say so in `answer`, and name in the criterion the readings the paper allows. Set `answered: {date}` on each question. Do not change a claim's statement or expected values unless the question shows they are wrong about the paper; then say so in the answer. Check quotes with `python tools/claims_check.py`.

Only `claims/{dandiset}/` and `questions/{dandiset}.yaml` are kept. Do not commit or push. Write prose plainly: no em dashes, never the word "rather". YAML plain scalars must not contain ": ".

Your final message is a report: each question, and its answer in a sentence. Be concise.
