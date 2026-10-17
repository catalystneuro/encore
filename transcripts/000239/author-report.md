I've finished steps 1 to 6 for dandiset 000239. The entry passes `check` and runs from a clean environment, and the handover package is built in `executed/000239-xu-2022/handover/`. Nothing is committed.

I used the full text of the accepted author manuscript in PubMed Central (PMC9109820), fetched through NCBI efetch; the version of record is not open access. The Figure 3b R² values are printed only inside the figure, so I read them from the figure image on Nature's page. I pinned 0.230607.1752, the only published version (the paper cites none).

**1. Outcomes** (39 claims: 20 reproduced, 5 partially reproduced, 3 not reproduced, 11 blocked)

| Claim | Outcome |
|---|---|
| fig3-session-counts, fig3-units-per-session, fig3a-trial-count | reproduced |
| fig3c-length, -velocity, -angle, -identity, -time (all 20 R² values within the paper's SDs, order as stated) | reproduced |
| ed5b-variables-uncorrelated, ed5e-variance-explained (0.454, just inside 0.45–0.55), fig3e-cca | reproduced |
| fig4g-zigzag-context, ed7f-target-position-alm, ed7h-no-time-coding | reproduced |
| ed4o-rhythmicity, ed6-alm-reward-drop | reproduced |
| ed1h-sequence-duration (0.992 s, 17 mice), ed1l-learning-curves, ed2e-missed-licks, ed7b-correct-side | reproduced |
| ephys-unit-counts (339 multi-units, paper 303) | partially reproduced |
| ed5f-axes-orthogonal (one pair at 0.302, bound 0.3) | partially reproduced |
| fig3f-backtracking-svm (S1TJ and S1BF also above chance) | partially reproduced |
| ed4m-active-neuron-counts (S1TJ 155, paper 119) | partially reproduced |
| ed4l-alm-initiation (ALM vs M1TJ p = 0.14) | partially reproduced |
| ed1l-proficiency-1500 (200 or 1100 trials) | not reproduced |
| ed2-backtracking-counts (55 sessions, paper 47) | not reproduced |
| ed6b-consummatory-licks (6 video licks or 4 touches, paper ~5) | not reproduced |
| Five opto claims (Fig. 2b,c; ED 3l,m), earplug, odour masking, numbing, lick force | blocked: metadata_insufficient |
| ed3f-inhibition-efficiency | blocked: data_missing |
| ed4j-nnmf-clusters | blocked: methods_underspecified |

**2. What was found about the dandiset**
- **What is there:** the behaviour and spikes behind Figures 1, 3 and 4. The session groups match the paper exactly: 13/9/8/5 Figure 3 sessions, 57 recording sessions, 6 zigzag sessions from 3 mice, 15 learning mice.
- **Recorded area:** given only by the session description (the lab's folder name). There is no electrodes table, and no unit location, quality label or waveform.
- **Opto and control sessions:** opto sessions do not name the inhibited region, and control sessions do not say which session or block was the manipulation.
- **Duplicated spikes:** 1446 spike times in 35 files are duplicated within units. The Methods say these Phy duplicates were removed.
- **Duplicate deposit:** the MX181003 learning file of 2018-10-02 repeats all 4028 touches of the MX181002 file, then continues.
- **Learning files:** `start_time` is on a different clock from the event times, and `seqId` holds an unreadable MATLAB object.
- **Units and code:** force sensors are in volts with no calibration, and tongue landmarks in pixels with no scale. The paper's code is "available at GitHub" with no address, and I found no repository.
- **Undocumented exclusion:** 8 sessions with very short touches fit the Methods' 8 excluded sessions; leaving them out gives the paper's 47.

**3. Where the protocol was unclear, wrong or missing something**
1. The header table only has to say which claims are tested or blocked, but nothing stops an author from adding outcomes, and `handover` would not strip them. I first put outcomes there; I removed them before the final run.
2. The protocol does not say whether numbers printed only in a figure may serve as expected values. I used them and recorded where they came from.
3. Using the paper's SD as the tolerance for an across-session mean is generous (an SD, not a standard error). I followed the rule as written.
4. Step 1.5 assumes the paper links its code. It gave no address, so I read the NWB conversion code instead and recorded it.
5. The rule for absence claims assumes the paper names a test. For "no region encodes time to trial start" it gives none, so I fixed a bound of R² < 0.1.
6. It is unclear whether an undefined term like "proficiency" should be blocked (methods_underspecified) or defined and tested. I defined two readings and the result was not reproduced; that may reflect my definition more than the paper.
7. The suggested clock check (decoding a task variable around trial start) is weak here, because sequences alternate direction and ALM codes direction throughout. I used the video-to-touch shift and decoding of tongue length with shifted spike times instead.
8. "Count each recording once" does not say what to do when the owner of a duplicate is unknown. I left out both files.
9. A variant outside the pre-registered readings matched the paper's 47 sessions, but the outcome stays not reproduced. I described the variant in the notes.
10. The figure marks p < 0.001 for comparisons that an exact paired permutation cannot reach with 8 sessions. I used p < 0.05.

**4. Runtime and failures**
- **Runtime:** the notebook runs in about 350 s (limit 30 min); loading takes about 75 s of that, and the analyses run in parallel processes.
- **Getting the paper:** Europe PMC full text returned 500, NCBI BioC returned 429, and the PMC page hit a reCAPTCHA; NCBI efetch worked. Extended Data figure images could not be downloaded, and none were needed.
- **Streaming:** h5py's global lock made threaded streaming slow (15 min for an early scan of all files), so the notebook uses processes.
- **Bug fixed:** an early trial filter wrongly required video before the cue; I fixed it before any claim was judged.
- **Untracked files I did not touch:** the repository has untracked files I did not create (`.bashrc`, `.idea`, `scripts`, and others).

Files are in `entries/000239-xu-2022/`:
- reproduce_xu_2022.ipynb
- seqlick.py
- README.md
- entry.yaml

The claims are in `claims/000239/10.1038-s41586-022-04478-7.yaml` and the record in `attempts/000239-xu-2022-01.yaml`.
