# Quattrocolo & Maccaferri (2013) from CRCNS hc-9

Tests the findings of [Quattrocolo and Maccaferri (2013)](https://doi.org/10.1523/jneurosci.5680-12.2013)
that can be tested on [CRCNS hc-9](https://doi.org/10.6080/K0HQ3WTH), which holds the current-step
recordings of the three O-LM interneurons of the paper's Figure 7. The recordings from
Cajal-Retzius cells behind the paper's main findings are not in it.

| Claim | Outcome |
|---|---|
| O-LM cells show a sag in their response to hyperpolarizing current (Figure 7A, 7D) | Reproduced, on an assumed measure |
| Figures 1 to 6 and 8 to 12, the light responses of Figure 7, the age analysis (25 claims) | Blocked: data missing |

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/crcns-hc-9-quattrocolo-2013-01.yaml`](../../attempts/crcns-hc-9-quattrocolo-2013-01.yaml).

- `reproduce_quattrocolo_2013.ipynb`: the analysis. It takes under a minute.
- `hc9.py`: streaming the ATF files from the zip in the CRCNS bucket, the step table, and the sag
  measures. Other notebooks on this data set can import it.
