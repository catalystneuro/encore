No outcome changed, and nothing is under `proposed`. The verifier agreed with all 19 outcomes, and I kept them all. I re-ran the entry twice with `python tools/entry.py all entries/000350-mu-2019`; both runs pass and `check` reports 0 errors. Every earlier number came out the same.

**New outputs the verifier asked for**
- **fig2c:** a count of passivity onsets by protocol code. All 26 onsets in 20161109-2 fall in code 32, which is prolonged open loop with the grating moving. So does 42 of the 46 in 20170203-1. I replaced the wrong claim that this fish's open loop alternates with a still grating every 10 s.
- **figs2a:** the spread of the signal (SD) measured in 10 s windows in both conditions, so closed and open loop are compared on the same time scale. It is higher in open loop in 7 of 8 neuron fish (p = 0.0195, median ratio 2.52) and 3 of 4 glia fish (median ratio 2.07). 20170203-1 is again the exception. I removed the sentence saying drift does not explain the result.
- **Protocol-code cell:** it now also gives the number of switches followed by 16 or more bouts in 20170228-3 (2 of 4) and 20170228-4 (3 of 3).

**Text corrected in the notebook and the record**
- **fig1j:** it now says the closed-loop blocks after the first open loop decide "not reproduced". The variant using only closed loop before the first open loop meets the "partially" criterion. I kept the main reading because it was fixed before the analysis. The sentence on gain is weaker and names the two fish tied at 0.000 and the one that differs by 0.006.
- **fig1i:** only the last interval stands out; the means for k = 2 to 7 are flat. The edge variant is now described correctly: it keeps epochs cut by either edge of a period, not only those starting at a switch.
- **fig2c:**
  - I dropped the suggestion that the glial channel carries little glial signal.
  - In 20170203-1 the neuronal trace also has a low SD (0.0016), and it rises after onset (+0.28 SD, p = 0.0023). The same change is in the record's "other" finding and the Summary.
- **Summary:** it now says the edge variant was run only for fig1h, fig1i, fig2c and fig2h.
- **Raw-image finding:** it now says the counts in brackets are the volumes present, not the ones missing.
- **fig7-glia-accumulate:** the reason now matches the outputs. A Figure 7H analogue is possible in three fish, two of which have only 2 and 3 events. I did not run it: the claims file sets no criterion for it, and it would cover only half the claim. It is left for a new attempt. The block on the Figure 7J/K part stays.

**Record:** I added round 2 under `verifications`, with the verifier's reasons for all 19 claims in its own words and my response to each. I also noted that its round-1 report miscounted the fish with a single switch (4, not 5); I left its round-1 wording as it gave it.

**Not done:** I did not download the paper, so nothing is saved under `paper/`. I did not run the Figure 7H analogue, for the reasons above. Nothing is committed. The untracked files in the working tree (`.bashrc`, `.idea`, `scripts` and others) are not mine and I left them alone.
