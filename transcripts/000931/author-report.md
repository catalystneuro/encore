None of the 37 claims could be tested: the dandiset holds one mouse's spike times and none of the other recordings the claims need. All 37 are recorded as blocked (`data_missing`). The entry passes its checks, runs from a clean environment in 21 s, and the handover package is built.

**1. Outcomes**

| Claims | Outcome | Main missing data |
|---|---|---|
| inhalation-sorting, figs1a, figs3-aen, fig3f | Blocked: data_missing | breathing signal; the other mice |
| fig1-odor-responsive-fraction | Blocked: data_missing | odor trials, brain areas, the other five mice |
| fig1hi, fig1h, figs1c, fig1j, fig1l, figs1b | Blocked: data_missing | breathing, odor trials, brain areas |
| figs1d, figs2ab, figs2c | Blocked: data_missing | as above, and unit waveforms |
| fig2 GLM claims, figs2d, all fig5 claims, figs5i, fig6 | Blocked: data_missing | breathing, odor trials; the other concentration-series mice |
| fig3c, fig3b | Blocked: data_missing | the anesthetized mice and their airflow pulses |
| figs4-bulbectomy, fig4 (sniff fraction, 4d to 4g), figs4-motor-cortex | Blocked: data_missing | breathing; the bulbectomized and control mice |
| figs6h-waveforms-homogeneous | Blocked: data_missing | waveforms; the other experimental conditions |

**2. What was found about the dataset**
- **Contents:** one NWB file from one of the paper's 22 mice. It holds 1013 units with spike times and their Kilosort and Phy labels, and nothing else. Every other group in the file is empty: no breathing, odor or TTL signals, no trials, no electrodes table, no waveforms and no brain areas. The paper says processed data are available "upon request".
- **Version:** I pinned 0.261011.1559. The paper cites no version, and all three published versions and the draft share the same file (same SHA-256), so the choice does not change the data.
- **Which experiment:** only the keyword "Concentration Series" places the mouse in a group; the odors are not stated.
- **Units cannot be selected as the paper did:** the 359 units curated "good" in Phy lie along the whole probe, and there is no area label to pick out piriform layers 2 and 3.
- **Contradictory labels:** `KSLabel` is "good" and `ContamPct` is 100 for every unit, which contradict each other. `quality` is missing for 644 units.
- **Thin metadata:** most unit columns have no description, and `depth`, `Amplitude` and `amp` have no unit. The file's `related_publications` names the preprint, and the two 2024 versions do not name the paper.
- **What could be checked agrees with the paper:**
  - The good units' ISI violation rates (median 0.0066, Q3 0.029) and presence ratios (all 1) fall in the ranges the Methods report.
  - All good units fire above 0.5 Hz, and no unit is duplicated.
  - The good units nearest the probe tip show a 2.78 Hz rhythm, within the range of mouse breathing.
- **No clock check:** with only one data stream, the alignment of spikes to trials could not be checked.
- **Questions:** I made no assumptions, have no questions for the paper's authors, and asked a reader nothing.

**3. Where the protocol was unclear or missing something**
1. Nothing covers a dataset where no claim can be tested. I kept the required notebook parts. Instead of one section per claim, a single cell tagged `blocked-claims` shows each claim's needs against what the file holds, and every blocked outcome points to it.
2. The clock-alignment check (step 2) assumes a second data stream. Here there is none, so I said in the notebook that it could not be made.
3. "Stream, do not download" says nothing about reading the claims file from a notebook. I read it by relative path to check that the per-claim table covers every claim id.
4. Writing the record with PyYAML left `id: 000931` unquoted. Python reads that back as a string, but other YAML parsers would read the number 931. I quoted it by hand; `entry.py check` did not catch this.

**4. Runtime and failures**
- The run took about 15 minutes, from 17:20 to 17:34 UTC. The notebook runs in about 21 s.
- `lock`, `all` (check plus clean run) and `handover` all passed with 0 errors.
- Nothing failed. The sandbox created some placeholder files in the repo root (`.bashrc`, `scripts` and others, all empty device files, not mine). The workflow should not commit them.

Files are in `entries/000931-dehaqani-2024/`:
- README.md
- entry.yaml
- mechano.py
- reproduce_dehaqani_2024.ipynb
- requirements.in
- requirements.lock.txt

The record is `attempts/000931-dehaqani-2024-01.yaml`.
