I've completed steps 1 to 5 and the handover (step 6). The entry passes `python tools/entry.py all` (the notebook runs in 205 s), and the handover package is in `executed/001199-gao-2025/handover/`. Nothing is committed.

The main result: this dandiset probably does not hold the paper's recordings. Its 13 rats were recorded from August 2024 to July 2025, after the paper's preprint of June 2024. The paper's Methods name dandiset 000946 for its data, and that dandiset lists 20 other rats recorded in 2023 and 2024; only BH594 is in both. On top of that, the files hold spike times only, with no waveforms, so the paper's RSU/FSU typing cannot be repeated, and every session uses 200 µs pulses, so the duty-cycle series is absent.

**1. Outcomes (35 claims)**

| Claim | Outcome |
|---|---|
| subjects | partially reproduced: 6 rats with S1+POm (paper 16) and 6 with S1+AC (paper 12); two rats are in both groups |
| fig11b-ac-responses | not reproduced: 194 AC units (paper 453); no Kruskal–Wallis test significant at 0.01; only 1,500 Hz during sonication is significant, and only under one reading (R1/T2); nothing is significant after sonication |
| fig2-target-artifact | blocked, `data_missing`: no raw voltage or target-determination trials |
| 20 claims on RSUs/FSUs (Fig. 4–6, 10A–C, 11C–D) | blocked, `data_missing`: no waveforms or type labels |
| 12 duty-cycle claims (fig7-9-unit-counts, Fig. 7–9, 10D–F) | blocked, `data_missing`: only PD 200 µs; types also missing |

**2. Findings, assumptions, questions**
- **Type labels:** a `celltype_label` column is described as "1 = RSU, 2 = FSU" but holds 0 or the area name (S1/POm); 133 files have no such column.
- **Missing conditions:** there is no CG1 control at 3,000 Hz.
- **Undescribed conditions:** sessions at 10 and 15 V, stimulation at POm, and 64-channel probes; the paper used two 32-channel probes at 5 V.
- **Pressure metadata:** the pressure field reads "67V" (that is the ultrasound duration), and 2025 files state no pressure at all.
- **Unexplained labels:** stimulation targets "S1-6", "NEW", "y-1" and "SEP".
- **Session dating:** in the 2025 cohort, each probe has its own file, and files that share a trial table are one session. Their `session_start_time` values do not date the session (the BH608 sham pair is five months apart).
- **Format error:** 64 units have spike times out of order. Left unsorted, one AC unit read 4,224%; I sort on reading.
- **Duplicate:** one recording is deposited twice (BH646 `ses-None` and `ses-20250308T003900`).
- **Clock:** the 2024 sessions lock clearly to trial starts. Most 2025 sessions, which hold every AC file, do not (only BH648 at 4,500 Hz does). So the AC null result may come from the trial tables, not the neurons; this caveat is in the fig11b notes.
- **Assumption:** I counted "S1-6" as S1-targeted. A variant without it gives the same outcomes, so no outcome rests on it.
- **Questions:** none for the paper's authors, since every reading gave the same outcome. I asked a reader nothing.
- **Version:** pinned 0.250829.1250. All four published versions and the draft hold the same 229 files and differ only in contributor order.

**3. Where the protocol was unclear or missing something**
1. **Dataset that may not hold the paper's data.** The protocol has no rule for this case, where the paper names another dandiset (000946) as its repository. I tested 001199 as the claims file says and recorded the mismatch as a finding.
2. **Reading another dandiset's metadata.** Step 1.4 limits outside data to what the claims file says the paper relies on, but says nothing about reading another dandiset's file list just to identify rats. I listed 000946's asset paths under `inputs` and used them only in the subjects notes and a finding.
3. **Which block reason.** With waveforms absent and the label column mislabelled, the claims could be `data_missing` or `metadata_insufficient`. I chose `data_missing`.
4. **Failed clock check.** The protocol asks only to name sessions where the clock could not be established. It does not say how that bears on a claim whose result is an absence of response. I kept `not_reproduced` and stated the caveat.
5. **"Subset" in the subjects criterion.** "None extra" cannot be checked without the paper's list of rats. I applied it to the counts (both lower, neither higher).
6. **Bonferroni factor B1.** The claims file's "windows or conditions" is ambiguous. I ran factors of 5, 10 and 15; all give the same result.
7. **Format errors.** The protocol records them but does not say whether to repair them. I sorted the spike times and reported it.

**4. Runtime and failures**
- The run took about 50 minutes (08:59 to 09:48 UTC); the notebook takes about 3.5 minutes, most of it streaming.
- Nothing failed.
- One early bug was mine: window counts on the unsorted spike times produced the 4,224% outlier. It is fixed, and the final run uses sorted times.

Files are in `entries/001199-gao-2025/`:
- reproduce_gao_2025.ipynb
- tfus.py
- entry.yaml
- README.md
- requirements.in
- requirements.lock.txt

The attempt record is `attempts/001199-gao-2025-01.yaml`.
