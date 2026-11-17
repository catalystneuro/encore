No outcome changed and I proposed no change for round 3. The entry was re-run twice with `python tools/entry.py all entries/mehrotra-2024`: all four notebooks pass and `check` reports 0 errors. I recorded round 2 under `verifications` for all 22 claims. Nothing is committed.

**Outcomes**
- **fig1b** stays reproduced, resting on the assumption that HD information is in bits per spike. The verifier still says not_reproduced, and that disagreement is recorded. The question to a reader stays in `questions/mehrotra-2024.yaml`.
- **fig1j** stays not reproduced, and is now called fragile. On the main draw of the ring, one of 20 bins still falls outside the shuffle range: 294 UP states at −0.47 rad, against a range of 300 to 422. The test's own chance rate is 3.3%. Over three random draws of the ring, two fail by one bin and one passes.
- **fig1k** stays not reproduced. The verifier's numbers are now in all the text: U = 98, p = 0.27. The other two draws give p = 0.10 and 0.21. With the steps below the threshold kept, p is 0.052 on the main draw and 0.025 and 0.044 on the others.

**Added or corrected**
- **Ring repeatability.** Isomap's default eigen solver starts from an unseeded random vector, so the ring could differ between runs. It now uses the dense solver. A second fit of one session's ring with the same seed is identical, and the main-draw numbers were the same in both full runs. A ring's mirror orientation is arbitrary and flips the sign of the fig1j angle differences, so each ring is now turned to follow head direction (7 of 16 were mirrored). The unturned rings are shown too and give the same result. A new cell re-fits every ring with two other seeds.
- **fig1b.**
  - I rendered the paper's PDF and read Figures 1B and S1D to S1F. The Figure 1B axis is −2 to 1, with no cell beyond about 0.5. The depth axis runs from 0 (dorsal) down to −0.8 mm (ventral), so the paper's sign convention matches ours.
  - The opposite direction is now printed, and the direction is recorded as a deviation.
  - The notes say that the three measures that do not vary have the opposite sign to the paper's, none of them significant, so no direction matches all five signs.
  - The quotation now reads "0.2 bins/spike", as the paper prints it, with "bins" read as a misprint for bits.
- **Text fixes the verifier listed:**
  - fig5e: the result no longer quotes a load time; the record gives this run's printed 965 s.
  - fig5f: the threshold range now reads −0.259 to −0.238.
  - posub Summary: the 15 other event files are said to share the spikes' clock only by the cross-correlogram peak (−2.5 to −17.5 ms), with the low match counts in A3701, A3710 and A3716 stated.
  - The round-1 response numbers for fig1k and fig5e were corrected to what that run printed.
- **The optional A3708 check.** The session's LFP shows no gamma rise after its event file's UP starts either (0.997 against 0.998 shifted). So the LFP fits neither the spikes nor the event file, and the check cannot say which one is off. This is added to the fig2f notes and the LFP finding.
- **Run time.** The ring notebook now takes about 40 minutes, up from 12; `entry.yaml` and the README are updated.

**Not done**
- The fig1b unit question is left to a reader, as the protocol requires.
- The executed copies come from the second run. After it, I changed two numbers in the notebook text to match its output: the seed-2000 kept-steps p (0.023 to 0.025) and the fcx load time. The executed markdown still shows the earlier wording for those two cells. That seed-2000 value moved slightly between the two runs; those seeds are fitted in parallel threads, while the main draw is fitted one session at a time and was identical.
