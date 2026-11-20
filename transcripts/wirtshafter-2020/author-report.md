I did steps 1 to 5 and the handover. All 31 claims are blocked as `data_missing`, because hc-29 holds no position data and every finding in the paper uses the animal's position on the maze. `entry.py all` passed with 0 errors; the notebook ran in 117 s. The record is `attempts/wirtshafter-2020-01.yaml` and the entry is `entries/wirtshafter-2020/`. Nothing is committed.

**(1) Outcomes**

| Claim | Outcome |
|---|---|
| `units-recorded` | blocked: data_missing. The data set holds 452 LS and 178 CA1 clusters, exactly the paper's two counts, but the other two counts (165 CA1 and 378 LS cells meeting the criteria) need speed and track coverage, and the criterion needs all four |
| The other 30 claims (spatial information, place fields, laps, skew, field locations, CA1-LS cross-correlations) | blocked: data_missing |

**(2) The dataset**
- **What it holds:** sorted spike times and, in Times.mat, one column of timestamps per recording (57 recordings of six rats). There is no position, speed, direction, lap or trial data. The paper's code repository (commit 5c6320a9) holds no data either.
- **Version:** CRCNS does not version data sets, so it is recorded as `unversioned`. All three files' MD5 sums match the data set's `checksums.md5`; Times.mat (2.2 GB) was streamed to check this.
- **Copied spike trains:** in rat 7, two trains (1033 and 1441 spikes) are filed under 18 and 25 cluster names, across 16 recordings and three tetrodes. Every spike that falls outside its recording's time range (5403 of 15.6 million) is in one of these copies. The 452 LS clusters contain 410 distinct trains, which is still within the tolerance.
- **Clusters holding other clusters' spikes:** on rat 6's tetrode 26, in all 14 recordings, one cluster holds at least 99% of the other clusters' spikes. Separately, 24 pairs of clusters on neighbouring tetrodes share 71.5 to 98.5% of their spikes, against a median of 0.8% when one train is shifted by 1 s.
- **Time files:** sampling intervals are 0.512, 3.2 or 0.0512 ms, and the description states none of them. Recordings last from 2.5 min to 31 h, and nothing marks the paper's 30 min maze session. In rats 10 and 12 the spikes cover the whole 4 to 6 h recording.
- **Other:** CA1 clusters come from 2 of the 6 rats, which neither the paper nor the description says. Some cluster names are irregular (ten written `cl1` for `cl_1`, one labelled `MUA9`). One recording repeats timestamps at its end.
- I made no assumptions, have no questions for the paper's authors (no method was ever chosen) and asked a reader nothing.

**(3) Where the protocol was unclear or did not fit**
1. A claim whose criterion needs four counts, of which only two can be computed, fits no outcome cleanly: "partially reproduced" means an effect that is weaker or holds in part, not one tested in part. I recorded it as blocked, with the two matching counts in the notes.
2. The clock check assumes there are trial tables or annotations to align spikes with. Here there are none, so I could only show that spikes fall within each recording's time range, and I said that alignment to behaviour cannot be established for any session.
3. The duplicate check says to "report each pair". With 117 heavily overlapping pairs and 43 copies I reported them grouped in the notebook and as findings, not pair by pair.
4. "One section per tested claim" leaves open how to show a blocked claim with partial numbers. I gave `units-recorded` its own tagged section, and listed the other 30 in one table of what each one needs.

**(4) Runtime and failures**
- The notebook takes about 2 minutes, mostly streaming Times.mat for its MD5, and peaks at about 0.5 GB of memory. The session used about 35 minutes of the 5 hours.
- Nothing failed in the final run. During development a string-escaping slip in my notebook-building script broke one run; I fixed it and re-ran.
- Untracked dotfiles (`.bashrc`, `.idea` and others) and a `scripts` folder were in the working tree; I did not create them and left them alone.
