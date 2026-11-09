There were no questions to answer, so I changed nothing.

- **No questions file:** `questions/crcns-ac-2.yaml` is missing from the working tree, and git history on every branch has no such file. The `questions/` directory only has a file for another CRCNS dataset (`crcns-ret-1.yaml`).
- **The author asked none:** the author's report says "Questions to a reader: none" (`transcripts/crcns-ac-2/author-report.md:44`). No verifier has run on this attempt yet; the latest commit is the author run.
- **Questions sent elsewhere:** the open points the author raised are aimed at the paper's own authors, not a reader. They are about the spike rule, how input resistance was measured, how mEPSPs were detected and sized, and the culling procedures. They are recorded as `methods_unavailable` findings in the attempt record.
- **One possible issue in the claims file:** the author found its opening comment wrong about spikes. It says the spike rule "can change only the few trials with spikes", but the rule moves several results across their tolerances. The author treated this as a method detail under Author step 1.6 and did not ask a reader, so I did not take it up.

`claims/crcns-ac-2/` is unchanged, I created no questions file, and nothing was committed. If a later verifier round raises questions, this answer run can be started again.
