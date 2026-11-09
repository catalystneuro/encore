I wrote `claims/wang-2014.yaml`, and the quote checker passes it: 29 claims, 28 quotes, 13 statistical values, 0 problems.

**Text read:** the version of record (`paper/10.1038-nn.3904.txt`), with the main text, legends and Online Methods, plus the supplement (Supplementary Modeling, Table 1, and the legends of Supplementary Figs. 1–17). Nothing the results rest on is missing. The paper links no code, so none was read. I could not render any figure pages because no PDF renderer was installed. I used the figure labels that survived in the text file instead.

**Claims:**
- **Quotes:** 28 of the 29 have one. The exception is `figs5-compression-lost`, which is marked `inferred`: the compression index and CCG sequence results appear only in the Supplementary Figs. 5 and 8 legends and the Methods.
- **Statistics:** 13 claims carry them, as WSR, K-S and Kruskal-Wallis tests.
- **Criteria:** all 29 have one.
- **Without recorded data:** 3 claims are model simulations (Fig. 3c, Fig. 3d, Supplementary Fig. 10b,c).
- **About the dataset:** the hc-5 description covers one rat and does not mention injections. Claims that need groups or a second animal (Fig. 5c, Supplementary Fig. 16) say so; whether the sessions are the muscimol ones is for the author to find.

**Details the paper leaves open, with the readings named:**
- **Peak-to-mean rule:** the Methods print "FRp2m ≤ Thp2m". That sign cannot work, so I read it as ≥ 3.
- **"Small" field margin:** at most 0.5 s or at most 1 s.
- **Parameters adjusted by eye:** this cannot be repeated, so the default values are used and recorded as a deviation.
- **"Excitatory" neurons:** the dataset's own labels, or all units.
- **Muscimol period:** all trials of the muscimol session, or the trials after theta power drops (I set that threshold myself).
- **Time bin for information on the wheel:** 1,250 Hz samples or 75 ms bins.
- **Open-field maps:** 2.5 or 5 cm bins, and the ref. 54 adaptive-binning constant, halved or doubled.
- **Refractory-violation units:** 0.3% or a fraction of 0.3.
- **Autocorrelogram span:** ±0.5 s or ±1 s.
- **The unexplained "30" in the LFP multitaper:** a 1 s or a 2 s window.
- **Recordings for theta sequences:** 9 on the wheel and 5 in the maze (Methods selection), or 13 (legends).
- **Platform neuron counts:** 145 and 247 in the text, or 223 and 372 in the Fig. 5 legend.
- **Periphery border in Supplementary Fig. 12f:** 15 or 25 cm from the walls.
- **Model details:** the cue speed and the "high" DC input are not given.
- **Undefined words:** "complete remapping", "only a few" and "formed place fields" each get readings in their claims.
- **Tests chosen in the claims file:** for the unquantified claims (wheel sequence loss, compression, remapping, and stability under control conditions), the tests come from the Methods' list (WSR, Spearman, K-S, one-sided). The paper does not apply them to these findings.

**Discrepancies inside the paper, recorded in the claims:**
- **Fig. 4b:** the panel prints P = 0.022, the text P = 0.23.
- **Fig. 2j:** the panel prints P < 0.01 and P < 0.005, the text P < 0.001.
- **Wheel information:** the text labels the second value "post-muscimol", but it is the muscimol session.
- **Muscimol recordings:** the text gives 15, the legends 13.

**Missing:** nothing from the paper that a claim needed.
