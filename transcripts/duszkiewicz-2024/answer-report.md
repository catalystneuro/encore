I answered the one open question. The claims file changed.

**ed3k-robust-to-controls** (changed): The claim said ADN-HD cells have higher multipeak scores than PoSub-HD cells, and the paper does not say that. The Extended Data Fig. 3j legend gives only "Multipeak scores in PoSub-HD and ADN-HD cells (Mann-Whitney U, n = (1602, 97), z = 4.25)", with no direction. The cell counts kept below 0.05 in panel k (789 of 1,602 PoSub-HD cells, 69 of 97 ADN-HD cells) point the other way, to lower ADN-HD scores.
- **Statement:** now says only that multipeak scores differ between the two groups.
- **Criterion:** notes that the paper gives no direction and what the counts suggest. It accepts the multipeak test at p < 0.05 in either direction.
- **Unchanged:** the three Fourier-distance tests still have to go in the paper's direction.

I set `answered: 2026-11-02`. `python tools/claims_check.py` reports 34 claims, 34 quotes and 0 problems. Nothing is committed or pushed.
