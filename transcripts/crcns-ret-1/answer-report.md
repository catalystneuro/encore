There was one question (on `fig9d-rf-size-similar`, also covering fig9e, fig9f, fig9g, fig9h and s3), and the paper doesn't answer it.

**Question: which flickering-bar recording of a retina should be used (bar orientation, and what to do when a retina has more than one recording)?**
The Methods give only the bar widths ("we projected gratings of adjacent thin bars (8.3 or 16.6 μm width)"). The Results and the Figure 9 legends don't name an orientation or say anything about retinas with several recordings, the supplement isn't in the text, and the paper links no code.

What I changed:
- **Criteria:** the `fig9d-rf-size-similar` criterion now says the paper leaves this open and names the three readings the question proposed. A is the first vertical-bar recording, B is all vertical-bar recordings pooled, and C is the horizontal-bar recording where the retina has one, otherwise A. fig9e, fig9f, fig9g, fig9h and s3 now need their outcome to hold under all three readings. For fig9f under B, the rate is taken over the pooled spike counts and durations.
- **Unchanged:** no claim's statement or expected values, since nothing in the question shows they are wrong about the paper.
- **Questions file:** the answer quotes the passage, and the question is marked `answered: 2026-10-20`.

`python tools/claims_check.py` reports 26 claims, 26 quotes, 0 problems, and both YAML files load. Nothing is committed.
