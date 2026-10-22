You record a finished attempt in the reproduction registry, checked out in the current directory. The attempt on dataset {dataset} is `{attempt}` (entry `entries/{entry}`), and it has been through its verification rounds. Do not change the attempt, its claims or its entry.

1. Write the attempt's notes in a new file, `docs/pilot-notes/{attempt}.md`, headed `# {folder}, <first author's surname> et al. <year>` (for a repeat attempt, say so in the heading, as `docs/pilot-notes/001754-knierim-2000-02.md` does). Change no other file. First read the five notes added most recently (`git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5`): yours follows their shape, length and tone. Write it from these sources only: `attempts/{attempt}.yaml`, the claims file in `claims/{folder}/`, the reports in `transcripts/{folder}/` (`author-report.md` and the `-report.md` files after it), and the entry for this dataset in `targets/dandisets.json`, whose `catalystneuro` field says whether CatalystNeuro converted it.
   - First paragraph: the outcome counts as `python tools/readme_row.py {folder}` prints them (it changes nothing), whether the verification rounds agreed, and in a sentence or two what the paper is and which claims could and could not be tested.
   - Second paragraph: the findings about the dataset, the most consequential first. If the `catalystneuro` field is not empty, open with "The dataset was converted by CatalystNeuro (<repository>)." Keep every number you give exactly as the record states it.
   - Last paragraph: the author's points on the protocol, from the author's report, as one sentence listing them.
   - Anything unusual about how the run went (a failed step, a third round) goes in a sentence where it fits.

Write prose plainly: no em dashes, never the word "rather", no bold, no bullet lists. Add nothing that the sources do not state. Do not commit or push: the workflow commits your changes.

Your final message is the subsection you wrote.

Run every command in the foreground and wait for it to finish: the run ends when you stop.
