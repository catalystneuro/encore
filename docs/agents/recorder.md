You record a finished attempt in the reproduction registry, checked out in the current directory. The attempt on dataset {dataset} is `{attempt}` (entry `entries/{entry}`), and it has been through its verification rounds. Do not change the attempt, its claims or its entry.

1. Write the attempt's notes in a new file, `docs/pilot-notes/{attempt}.md`, headed `# {folder}, <first author's surname> et al. <year>` (for a repeat attempt, say so in the heading, as `docs/pilot-notes/001754-knierim-2000-02.md` does). Change no other file but the summary of step 2. First read the five notes added most recently (`git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5`): yours follows their shape, length and tone. Write it from these sources only: `attempts/{attempt}.yaml`, the claims file in `claims/{folder}/`, the reports in `transcripts/{folder}/` (`author-report.md` and the `-report.md` files after it), and the entry for this dataset in `targets/dandisets.json`, whose `catalystneuro` field says whether CatalystNeuro converted it.
   - First paragraph: the outcome counts as `python tools/readme_row.py {folder}` prints them (it changes nothing), whether the verification rounds agreed, and in a sentence or two what the paper is and which claims could and could not be tested.
   - Second paragraph: the findings about the dataset, the most consequential first. If the `catalystneuro` field is not empty, open with "The dataset was converted by CatalystNeuro (<repository>)." Keep every number you give exactly as the record states it.
   - Last paragraph: the author's points on the protocol, from the author's report, as one sentence listing them.
   - Anything unusual about how the run went (a failed step, a third round) goes in a sentence where it fits.

2. Write the attempt's summary in a new file, `summaries/{attempt}.md`: one paragraph of at most five short sentences and under 120 words, with no heading, shown at the top of the dataset's page on the site. Its reader knows the field but not this paper, and wants to know at a glance whether the paper's main findings hold up in this data. From the same sources as the notes:
   - Open with the verdict on the paper's main findings, in plain words: which held up in this data, which did not, which could not be tested.
   - Name the main findings in the paper's own terms, not as claim numbers. A claim on a main figure or in the abstract is central; one on a supplementary figure, a control or a methods detail is minor. Group the minor claims in one sentence, or leave them out when they do not change the picture.
   - For a central finding that did not reproduce or could not be tested, give the one most likely reason the records give (a method the paper does not describe, data missing from the dataset, a difference the verifiers confirmed), in a few words.
   - Give at most two numbers, and only where they make the point. Do not call the paper right or wrong; the agent's own limits count among the reasons.

Write prose plainly: no em dashes, never the word "rather", no bold, no bullet lists. Add nothing that the sources do not state. Do not commit or push: the workflow commits your changes.

Your final message is the subsection you wrote, then the summary.

Run every command in the foreground and wait for it to finish: the run ends when you stop.
