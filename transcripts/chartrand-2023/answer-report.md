The questions file had one question, and I amended the claims file in response.

**fig2b-subclass-ephys-profiles: claims file changed.** The paper says PAX6 cells have "minimal sag and high initial firing rate at the onset of response to depolarizing current injection (Fig. 2A–B)" right after it describes LAMP5 cells. It never ranks PAX6 above L1 VIP on initial firing rate, so requiring "highest of the four" read more into the text than it says. Part (iii) of the criterion now requires the PAX6 median `first_isi_inv_hero` to be higher than both the LAMP5 and the MC4R medians. Parts (i) and (ii) are unchanged.

The paper doesn't compare PAX6 with MC4R on this feature either, so including MC4R in (iii) is a reading choice. I followed the asker's proposal so that "high" means above most of the other subclasses. A narrower test against LAMP5 alone would be the strictest reading of the sentence.

The question now has its `answer` and `answered: 2026-10-31`. `python tools/claims_check.py` on the claims file against the paper text reports 0 problems, and both YAML files parse. Nothing is committed or pushed.
