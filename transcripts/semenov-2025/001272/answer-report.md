I answered the one question, on `fig1-pure-sine-excites-all`, and changed the claims file. It affects every claim that uses header item O3.

- **Question:** does O3's rule that an AP must be 2 to 20 ms wide at half height follow the paper?
- **Answer:** no, the claims file misread the paper. The Methods' "lasted about 10 ms (... 8 ± 0.7 ms duration, excluding afterhyperpolarization)" is the AP's whole duration, not its width at half height. That figure caps the half-height width but gives no reason for a 2-ms lower bound.
- **What changed:** O3 now accepts APs 1 to 20 ms wide at half height. The 1-ms floor is about 3 frames at the Methods' "3,130 or 3,086.4 frames/s", so it only screens out single-frame noise. The upper bound, the 5-ms spacing between APs and the height readings are unchanged. O3 now explains the bounds in its own text.

`questions/001272.yaml` has the answer and `answered: 2026-11-01`. `tools/claims_check.py` reports 19 claims, 19 quotes, 0 problems, and both YAML files parse. Nothing is committed.
