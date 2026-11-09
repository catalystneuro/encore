I finished the round-1 revision. I ran the entry again with `python tools/entry.py all entries/henze-2000`: it passed in 552 s with 0 check errors, and the run's numbers match my working run exactly. Every conclusion, the README and the attempt record now use the new numbers. Nothing is committed.

**What changed in the outcomes**
- **duration-correlation**: partially reproduced → reproduced, resting on an assumption. With the new somatic/dendritic rule, R = 0.644 and P = 0.0175 over 13 cells. Under the rule as stated in the paper it would still be partial. The notes say this, and the question goes to the paper's authors.
- **fig3a-example-pair**: blocked → not reproduced, resting on an assumption. I took D11221 then D11222 as the pair, from the folder names and the labels in Fig. 6A. Their latencies are 0.250 and 0.975 ms against the paper's 0.28 and 0.55 ms.
- **fig4bc-burst-attenuation**: reproduced → partially reproduced, resting on an assumption. All parts hold in a bare majority under some cell selections and not under others. The amplitude parts hold in a majority under every selection with more than one cell.
- I kept three outcomes against the verifier and recorded the disagreement:
  - **fig4d-amplitude-correlation** stays reproduced. With the threshold fixed, D15121 gives R = 0.408 (n = 958), and R = 0.374 under the reading the verifier used. Both have P < 0.0001.
  - **propagation-velocity-range** stays blocked (data missing). The paper's cell counts point to the behaving-animal recordings, which are not in the data set.
  - **silent-cells-inference** stays blocked with data missing, not "other". The protocol says a claim that depends on a blocked claim is blocked for the same reason.

**What I added or corrected, by the verifier's problem numbers**
1. **Somatic/dendritic split.** Every timing claim now runs under four rules. The main one counts a cell as somatic when its AP peak is above −10 mV and it has a fast AHP. This rule calls D53 somatic, as the paper's Fig. 1 legend does, and gives 13 somatic and 7 dendritic cells. Only duration-correlation changes outcome with the rule.
2. **Per-spike threshold.** It now starts at the run of the fastest rise (above 10 V/s) before the peak. A new cell checks it on synthetic spikes at 10 and 20 kHz.
3. **Negative-peak window.** It now opens at −2 ms instead of −1 ms, and the baseline moves earlier for early troughs. A synthetic test shows it finds troughs the old window missed. The new cell also plots D11221 and D11222 from −3 to +3 ms. D11222's trough is real at −0.97 ms, and no tetrode cell's latency changed.
4. **Fig. 4 selection.** The notebook now prints each cell's first and fourth intervals in its trains and its step lengths and sizes, and applies the claims file's own selection (slowing trains, first interval about 10 ms).
5. **Extracellular gain.** The amplitudes are compared with those in Fig. 6A. They are 4.3 to 6.0 times larger for D53, D11221 and D11222, and 1.2 times for D81. This is recorded as a finding; no outcome depends on amplitudes in µV.
6. **AHP slope change.** It now uses the first local maximum or minimum of the second derivative. The notebook reports that the AHP peak sits at the end of its window in 5 of 20 cells. The notch outcome is unchanged.
7. **Back-propagation velocity.** The velocity readings now run under all four rules (0 of 96 in range), and the conclusion says the mean-of-ratios reading is unstable.
8. **File checks.**
   - D6811 now uses the extracellular channels its README lists.
   - D13521's 20 kHz rate (from its xml) is confirmed by its spike duration; its README's 10 kHz is recorded as a finding.
   - D13921's measures are shown from each of its two overlapping files alone.
9. **Silicon-probe site order.** The smoothness check is now computed against all 720 orderings of each shank's channels. 4 of 10 cells now reach 100 µm, and 3 of 9 without D15712, whose listed order looks wrong.
10. **Header table.** The notebook's header table now marks propagation-velocity-range as blocked. The notebook also prints the cell-count arithmetic (141.4, 1108.4 and 12.7 cells).

New findings in the record: the deposit looks like an undocumented selection (D107 has no folder), D13521's README rate is wrong, the extracellular gain is uncertain, and a question for the authors about which cells were somatic and what electrode offsets they removed. The round-1 verification is recorded for all 21 claims.

**Not done**
- No questions added to `questions/henze-2000.yaml`: the verifier did not report a place where the claims file misreads the paper.
- For Fig. 4, cells are selected on their median first interval; single trains are not, because the averages are built per cell. The record says so.
- Changes to `tools/` were already in the working tree before this run, and some character-device placeholders the sandbox created now show as untracked files (`.bashrc`, `scripts` and others). I left all of them alone.
