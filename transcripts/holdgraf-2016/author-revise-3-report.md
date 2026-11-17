The verifier agreed with both proposed changes in round 3, so I applied both. No proposals remain.

**Outcomes changed:**
- **supp6a-connectivity-increase**: reproduced → not_reproduced, still marked `assumed: true`. Integrated from the lowest frequency the tapers resolve (10 Hz at NW = 4), neither target region shows an increase: frontal P = 0.46, temporal P = 0.72.
- **supp6a-after-closer-to-middle**: reproduced → not_reproduced, still marked `assumed: true`. Integrated from 10 Hz, AFTER is not closer to MIDDLE in either region, at either bandwidth.

For both claims I removed `proposed` and rewrote the notes and the integration-range deviation so they rest on the 10 Hz reading, with 2.5 Hz as the variant. The notebook's two result cells and summary, and the README's table and text, now say the same. No other outcome changed.

I added round 3 under `verifications`: it reviewed only these two claims, both agreed and not_reproduced, with the verifier's reasons and my responses.

`python tools/entry.py all entries/holdgraf-2016` passed with 0 errors in 24 minutes. The re-run gives the same supp6a numbers as the record. One correction came from that check: the verifier wrote that BEFORE and AFTER coherence span 8.64 to 8.69 bits/s, but the output gives 8.54 to 8.69. I fixed the range in the claim notes and left the verifier's reason as it wrote it. `entry.py check` still passes.

Nothing is committed.
