No outcome changed in this round. The verifier agreed with 23 of the 24 outcomes. On the one it disputed, fig5c-rise-decay-gradient, I kept partially reproduced and recorded its disagreement. The entry re-ran cleanly with `python tools/entry.py all` (147 s, 0 check errors), and every conclusion matches the new numbers. Nothing is committed.

**Outcomes and how they are marked**
- **fig5c-rise-decay-gradient:** kept as partially reproduced. The verifier would say not reproduced. The criterion only defines "reproduced", and the protocol calls an effect that is present but weaker partially reproduced: here the gradient and its test hold in every rat, but the values are smaller than the paper's.
- **The four Figure 8 claims** (fig8c, fig8d, fig8-correlation, fig8-coupled-oscillators) are now marked as resting on an assumption: the claims file's definition of a cycle's period. That period shares the reference peak's timing with the per-cycle delay. The notes now say these outcomes are not evidence against the paper's mechanism.

**What I added or corrected**
- **Units (problem 2):** a table of each channel's theta amplitude in µV under both readings of the files, and a sweep of the theta threshold from 200 to 2051.
  - If the integer files are Intan counts, 400 µV leaves no theta epoch in any rat.
  - No threshold gives the paper's 3500 to 5000 cycles in every rat.
  - The asymmetry-related delay stays at 6.0 to 7.6 ms/mm at every threshold, against the paper's 3.56.
  - The notebook text now says the main reading's threshold is 400 µV only if the integer files are in µV, and about 78 µV if they are Intan counts.
- **Channels outside the MEC (problem 3):** I read the dataset's author-proof figure of electrode placements. It marks 6, 5, 6, 5, 6 and 5 electrode tips at the key recording, matching each file's channel count, and labels electrodes outside the MEC "unused". So excluding them selects the same channels already used, and nothing needed re-running. I counted the tips by eye; the figure does not say which tip is which channel.
- **Natural log for Figure 5 (problem 1):** shown as a variant. It brings the rise/decay claim within tolerance (−0.393 and −0.112). I asked a reader whether the claims file should allow it, in the new `questions/hernandez-perez-2020.yaml`. The claim's outcome still uses log10, as the claims file says.
- **Figure 8 timing (problem 4):** a variant that takes frequency from the Hilbert phase, so it uses no peak times, plus the per-rat table the verifier asked for (peak and trough delays against each period definition). With the jitter-free measures the absolute delay falls with frequency, the paper's direction, but by less per mm. The asymmetry correction is what turns the claims file's slope positive.
- **Half of the asymmetry-related delay (Figure 7):** shown as a variant. It gives 2.8 to 3.5 ms/mm and a residual of 6.8 to 9.2, both within tolerance. It does not decide the outcome, because the paper's formula is the full difference.
- **Smaller fixes:**
  - fig6b now has a per-rat table: the rising phase is longer than the peak in 4 of 6 rats.
  - fig6b-hilbert reading (b) is now computed as the median of pooled per-cycle values, and the unused variable and the wrong sentence about the readings coinciding are gone.
  - Two other ways of handling rat 1's zero in the signed-rank test both still give p = 0.0625, at the boundary of the criterion.
  - The robust-regression convergence bug is fixed; the delays are unchanged.
  - The dead code is removed.
  - The cycle-triggered average now requires the window to be artefact-free on every channel; the ventral lags are 16 to 40 ms.
- **Record:** the round is recorded under `verifications` with the verifier's reasons and my responses. The attempt notes, findings, README and notebook summary are updated.

**Not done**
- I did not change any claim in the claims file.
- I did not treat the natural-log or half-delay variants as deciding outcomes; they differ from the paper's stated Methods.
- Untracked files in the repository root (dotfiles, `.idea`, `.vscode`, `scripts`) are not mine, and I left them alone.
