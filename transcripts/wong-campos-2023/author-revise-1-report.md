I've revised the attempt for every point in the round-1 report. Four outcomes changed, and one disagreement is kept and recorded. The entry re-ran cleanly with `python tools/entry.py all` (0 check errors, notebook passes in 42 s). Nothing is committed.

**Bug I found while revising:** recordings 14 and 15 of the Fig. 4e-h file are sampled at 1,000 Hz, but the first version read them at 500 Hz. That is why their stimulus onsets looked inconsistent and why two of their STA (spike-triggered average) delays came out above 3 ms. The helper `dendvolt.py` now takes each recording's own sampling rate. Read at the right rate, their onsets match the traces and their delays halve. I withdrew the finding that called their onsets inconsistent and replaced it with one about the mixed rates and their 259 ms stimulus.

**Outcome changes**
- **fig1d:** partially reproduced → reproduced. I agree with the verifier: the criterion asks for dendritic events after most somatic spikes in the dendrites taken together, not in each one.
- **fig4bc and fig4d:** reproduced → partially reproduced. The criterion names both detection thresholds and asks for every reading, so I was wrong to adopt the 4 s.d. threshold as an assumption. Each fails at least one reading at the 5 s.d. threshold.
- **figs12:** reproduced → partially reproduced, marked as resting on an assumption. A new per-recording check does not show that column 1 of the anesthetized recordings is a soma.
- **fig4ijk:** kept as partially reproduced; the verifier says not reproduced. The first bAP is smaller in the average and in most trial and dendrite pairs, so I read the claim as holding in part.
- **fig4fg, fig4h, figs13:** still blocked. With the rate fixed, no dendrite has a delay above 3 ms by either the deposited or the STA delays.

**Other additions and corrections**
- **fig2c:** the `figure2h` and `figure2j` files are now opened and printed. They hold normalized amplitudes pooled over sites with no site label, and no traces or baseline noise, so the claim stays blocked.
- **fig4fg:** reading (b) (dendrite/soma ratio) is now run. As not-deciding variants with distal thresholds of 1.5 ms and 1 ms and on all dendrites, the first bAP is attenuated under both readings. No recording has the 10 trials of the Fig. 4g neuron. The conclusion now says the deposited delays run about 1.9 ms below the paper's, which may explain why no dendrite counts as distal.
- **fig4h and figs13:** these now have analysis cells. Not deciding: no selection gives the biphasic pattern, and the distal versus proximal comparison goes both ways.
- **fig4ijk:** a table of the dendritic spikes with no somatic spike before them shows they are not frame-rounding artifacts. The soma reaches 0.54 to 1.00 of its threshold around most of them.
- **fig4d:** two variants added, a per-branch test of reading (a) and a baseline taken before the first spike of the trio. With that baseline, readings (b) and (c) fail at 4 s.d.
- **Smaller checks:**
  - fig2f: no delay is a 0.00 placeholder.
  - fig1d: a 1 s pulse period fits best of 0.8 to 1.2 s.
  - fig1fg: on synthetic peaks the parabola timing is unbiased on average, with single-phase errors up to about 0.3 ms.
  - fig3d: the notebook now prints the spike-exclusion window. It is 10 ms, as the criterion says; the verifier misread it as 20 ms.
- The record, README and summary are updated, and round 1 is recorded under `verifications` with the verifier's reasons and my responses.

**Not done:** I added nothing to `questions/001791.yaml`, because the verifier reported no misreadings of the claims file. The Fig. 1d pulse series cannot be checked, since the file records no stimulus.
