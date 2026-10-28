You answer an attempt's questions about the claims file for dataset {dataset} in the reproduction registry, as docs/protocol.md, "Reader", step 6, says. Each question is from an author or a verifier who believes the claims file misreads the paper: a wrong expected value, the wrong panel, a claim that does not say what the paper says.

Paper: doi:{paper}, "{title}". Its full text is under `paper/` (a `.txt` per paper, and the PDF where there is one). The questions are in `questions/{folder}.yaml`; the claims file is in `claims/{folder}/`. Do not look at the dataset's data or at the attempt's notebooks: answer from the paper and its code only.

For each question not yet answered: check the claim against the paper and decide whether the claims file misreads it. Where it does, amend the claim (its statement, source, quote, expected values or criterion, as the paper shows), and say in the question's `answer` what changed and why, quoting the passage briefly. Where it does not, leave the claim as it is and say in `answer` why it stands. A question that only asks for a method detail the claims file lacks is not yours to settle: the author takes such details from the paper (Author, step 1.6); say so in `answer` and change nothing. Set `answered: {date}` on each question. Check quotes with `python tools/claims_check.py`.

Only `claims/{folder}/` and `questions/{folder}.yaml` are kept. Do not commit or push. Write prose plainly: no em dashes, never the word "rather". YAML plain scalars must not contain ": ".

Your final message is a report: each question, whether the claims file changed, and the answer in a sentence. Be concise.
