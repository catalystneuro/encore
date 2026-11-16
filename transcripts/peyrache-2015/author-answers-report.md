There were no questions to answer, so I re-ran no claims and left the notebook, the conclusions and the attempt record as they were.

**Why nothing changed**
- `questions/peyrache-2015.yaml` doesn't exist. The reader's answer run (`transcripts/peyrache-2015/answer-report.md`) found the same: no questions file and nothing on any git branch, so it answered nothing and left the claims file alone.
- That matches my first author run, which put no questions to a reader (`author-report.md`: "Questions to a reader: none"). The three open method details I raised there are `methods_unavailable` findings for the paper's authors, not reader questions:
  - how the OLE decoders were built;
  - which sessions gave the ADn cells of Supplementary Table 1;
  - how the decoded angular speed in Fig. 2e was computed.
- The claims file's only `checks` entry is the second reader's check from before the attempt. No claim has been amended since my first run.

**Per question:** none, so no claim's outcome moved. The record still has 35 outcomes: 21 reproduced, 5 partially reproduced, 6 not reproduced and 3 blocked, all as they were after the first run.

**Entry checks**
- `lock` rewrote the lock file with exactly the same contents, and `entry.yaml` is unchanged.
- `all` passed with 0 errors. Because nothing the run reads had changed, it reused the executed copy from 14:34 UTC (744 s) and executed nothing.
- `handover` rebuilt `executed/peyrache-2015/handover/`.

I committed nothing and pushed nothing. If questions were meant to go to the reader, the file was probably never committed into this run's checkout. Once it exists, an `answer` run followed by another `author-answers` run would pick them up.
