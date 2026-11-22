No outcome changed. The verifier gave the same outcome as the record on all 39 claims. The entry check passes and the re-run passes (6.2 min, 1.19 GB peak), and every conclusion matches the new outputs. Nothing is committed.

**Added or corrected, by verifier point:**
- **Problem 2 (rich-club-controls):** I ran the one pair the data allow: the original signaling network against the anatomy network with an average of at least 1.25 contacts. That network has 1161 edges and density 0.0330, against the paper's 0.033. The rich clubs stay apart under both readings:
  - Under reading (a) the overlap is empty, because no neuron in that network has degree above 62 (the highest is 39).
  - Under reading (b) the threshold is k = 28 under all five seeds. That gives 13 neurons that share only AVEL and AVER with the signaling rich club. They keep 8 of the 14 original anatomy rich club neurons and add 5; the legend of Extended Data Fig. 12a says 9 of 15 kept and 4 new.

  The claim stays blocked as `data_missing`, because the other two pairs need q-values that no source holds. The notes give this partial result.
- **Reading (b) is my assumption.** The paper picks thresholds "by eye". I take the local maximum with the largest normalized value among those that leave at least 10 neurons. This rule gives back the paper's 25 and 62 on the original networks. I recorded it as a deviation and added a `methods_unavailable` finding at the end of `findings`, which asks the authors for the thresholds.
- **"Not checked" (q-values):** a new data check cell lists every attribute of the atlas pickle and every non-code file in the three repositories at their pinned commits. None holds q-values or an atlas that is not thresholded at q < 0.05.
- **"Not checked" (lists and code port):** the helper's neuron lists are compared with the ones parsed from the paper's code; all are identical. The code's `swapping_edges` is printed next to my port. Extended Data Fig. 5 is an image, so the code is the only thing the lists can be checked against.
- **Problem 4:** the ed9 notes and conclusion now say the stimulation counts are a subset of those behind the atlas: 23 neurons have no counted stimulation but 46 atlas out-edges.
- **A text error:** I had called the 15-neuron anatomy rich club "the code's list". It comes from the Ext. Data Fig. 12a legend, and the text now says so.
- The round is recorded under `verifications`. No finding is rated `critical`, so there were no finding reviews to record.

**Not done, and why:**
- **Problem 1 (testing community claims from the paper's Tables 1 and 2):** I declined. Those memberships are the output of the model that cannot be run here. Typing them in would put the paper's own results into the entry as an input, which the protocol forbids ("Compute every result from the data. No embedded numbers, arrays"). It would also test the paper's partition, not reproduce it. The claims stay blocked.
- **The block reason for graph-tool claims:** I kept `not_runnable`. The verifier said it is not an allowed reason and would use `other`. Protocol step 1.5 lists `not_runnable` for software that cannot be installed in a locked environment. The registry installs from PyPI, and the notebook now shows PyPI has 0 graph-tool files. The disagreement is recorded.
- **Problems 3, 6 and 7:** no change. The anatomy-dependent outcomes are already marked as resting on an assumption, and the verifier found that assumption reasonable. The chi-square test and the one-SD rule come from the claims file, which I don't edit.
- **Questions file:** no question was added, because the verifier reported no place where the claims file misreads the paper.
