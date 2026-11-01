No outcome changed in this round. I proposed two changes for round 3. I re-ran the entry twice with `python tools/entry.py all entries/001271-semenov-2025`: all three notebooks pass and the check reports 0 errors. Nothing is committed.

**Outcomes**
- **figs2-before-firing-then-depolarization** and **fig3c-sustained-firing-2s** stay `partially_reproduced`, as round 2 requires. Each now has a `proposed` change to `not_reproduced`, because I agree with the verifier: all 24 readings for the first claim and all 48 for the second give not reproduced, and the criterion has no partial outcome. The notebook conclusions and summaries say the same. The record also notes that the failing part rests on the claims file's sustained-depolarization measure (O4), whose levels are above the small plateaus in these recordings.

**Corrected sentences** (in the notebooks and the record, checked against the new run)
- Firing before the change no longer "holds under every reading". The 5-SD height gives 18 or 19 of 20 neurons with the first ROI reading, O1(a), and 1 of 7 with the eroded one, O1(b).
- The main summary no longer says the empty O1(b) masks cause most disagreements. It now says where the readings disagree within O1(a).
- ap-amplitude-duration: O1(b) peaks are 15.8 to 18.9%.
- fig2d: the text names the one comparison where modulated thresholds are not higher (20 kHz, 1 AP, O1(b) with the 5-SD height: 12.00 or 11.93 V against 11.00 V).
- fig2-modulated-locks-to-beats: 91% of 213 APs, and 15 of 15 sessions with 5 APs or more.
- fig2c: p = 4.7e-10 to 7.8e-07.
- fig1-20khz: 1 to 3 neurons have modulated 20-kHz thresholds for 1 AP, and 0 or 1 for 5 APs.
- fig3c: with the 5-SD height, 1 to 3 cells meet the first part and 3 or 4 the second.
- The round-1 block now says eleven shared claim ids, not ten.

**Added output**
- The notebook now prints the unmodulated 9_2 session at 3.4 V: 8 APs of 11.6 to 15.0% dF, pre-onset SD 1.40%, under both AP heights. The "eight clear APs" sentence now cites this output.
- A variant without 13_1's 20-kHz sessions, which show another cell (the verifier's point B8). fig1-20khz and fig2d still fail under every reading.

**Claims-file questions:** I added two questions for a reader to `questions/001271.yaml`, without changing any claim:
- **O4:** its no-AP condition rules out the coalesced oscillations the paper describes, and its levels are above the plateaus in these recordings. This decides four outcomes.
- **O1:** the ROI readings do not suit 16 x 16 crops. This decides the three `methods_underspecified` outcomes.

**Assumptions:** three choices the verifier said were not marked as assumptions are now labelled as such: the vehicle change point, extending the after-TTX level to O4, and the 18 V/cm per volt scale. Each deviation also says the outcome does not depend on it.

**Record:** round 2 is under `verifications` for all 20 claims, with the verifier's reasons and my responses.

**Not done**
- **Stimulus timing (B10):** not changed. The files hold no stimulus record, so it cannot be confirmed in more sessions. The response says the AP times agree with the Methods: no peaks before the onset in the 282 stimulated sessions of 001271 or in the first 50 ms of the 624 sessions from 001032, 001033 and 001035.
- **Figures 4 and 6 claims, and the 001272 pattern claims:** still not attempted.
- **Files I left alone:** `tools/build_site.py` was already modified before this run, and there are untracked dotfiles in the checkout. They are not part of this attempt.
