I've completed protocol steps 1 to 6 for dandiset 001545 (Rajebhosale et al. 2025). The entry, the attempt record and one question for a reader are written. `entry.py lock` and `all` pass with 0 errors, and the handover package is built. Of the 56 claims, 13 were tested on the dandiset; 43 are blocked. Nothing is committed.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| fig1j (WT SGCs have more hyperpolarized RMP) | not reproduced: right direction (-83.8 vs -75.3 mV), U = 32, p = 0.083 |
| fig1k (WT SGCs have narrower spikes) | not reproduced: right direction, p = 0.082 |
| fig1l (WT SGCs have faster downstroke) | not reproduced: right direction, p = 0.35 |
| fig1m (phase plots) | not reproduced (the criterion judges it through 1k and 1l) |
| figs1-remaining | partially reproduced: no GC vs SGC difference (smallest p 0.139); the soma-position half can't be run |
| fig2i, fig2j, fig2k (V321L GC vs SGC: RMP, width, downstroke) | reproduced (p = 0.59, 0.22, 0.88) |
| fig2m (four-class LDA) | blocked, methods_underspecified: the criterion's two readings disagree (features: WT GC apart; 9 PCs: WT SGC apart) |
| figs2d (k-means) | reproduced under both readings and 11 seeds |
| figs2e (PCA ellipses) | not reproduced: WT centroids fall inside each other's ellipses |
| figs2g (LDA classifier) | not reproduced: WT 55% (chance is 60%), kappa 0.12; V321L 42 to 46% |
| figs2f (LD1 centroids) | partially reproduced: the V321L distance shrinks, but both centroids are on the WT GC side |
| 12 claims needing soma position or morphology; 11 on Golgi or RNAScope | blocked, data_missing |
| 19 snMultiome claims (GEO) | blocked, not_runnable |
| figs9c (Allen Brain Atlas images) | blocked, other |

**2. Dataset, assumptions and questions**
- **Version:** I pinned 0.250809.1653, the only published version; the draft has the same 48 asset ids.
- **Genotype:** the files code it as VV or LL. The files' own metadata and the GEO sample records both say VV is wild type.
- **Cell counts differ from the paper:** WT has 13 GC and 9 SGC (paper 14 and 9); V321L has 12 GC and 14 SGC (paper 10 and 15). Dropping one WT GC at a time moves the fig1j p-value between 0.043 and 0.127.
- **Metadata errors:**
  - Stimulus values are picoamperes but labelled amperes.
  - Every file gives the cell as "VP neuron".
  - The stimulus text says cells were held near -65 mV and stepped to 200 pA; the data sit at -68 to -89 mV, and 14 cells were stepped to 250 or 300 pA.
- **Data checks:** no recording is deposited twice, and the stimulus and voltage share one clock.
- **GEO:** it holds raw matrices of every barcode plus ATAC tracks. The kept nuclei, the cluster labels and the per-nucleus ATAC fragments are not there.
- **Assumptions:** none of the outcomes rests on one (no `assumed: true`).
- **Questions for the paper's authors** (recorded as methods_unavailable findings):
  - Was the Fig 2M LDA fitted on the features or on PCs?
  - Which 20 features were used, and how were cells with a missing feature handled?
- **Question for a reader** (`questions/001545.yaml`): the figs8a criterion calls LL the wild type, which is reversed. No outcome here changes.

**3. Where the protocol was unclear**
1. A claim where only part of the criterion can be run, with no partial rule given (figs1-remaining, and figs2f where one of two conditions holds). I recorded `partially_reproduced` and explained why in the notes.
2. `elsewhere` claims whose needed data are not deposited anywhere in usable form (per-nucleus ATAC fragments exist only as raw reads). The protocol forbids `data_missing` for these, so I used `not_runnable` and explained.
3. The protocol has no rule for criteria that rely on software in another language (Seurat and Monocle3 in R) while the entry environment is Python-only. I treated these as `not_runnable` without trying a Python re-implementation, because that would replace the paper's clustering with mine.
4. Streaming: per-sweep `remfile` reads took 6.7 minutes for the dataset. A 16 MB first chunk streams each file in one request and takes 20 s, but it uses a private `remfile` argument.
5. A qualitative image claim (figs9c) fits no `blocked_by` category; I used `other`.

**4. Runtime and failures**
The notebook runs in 38 s. The author run took about 30 minutes of wall time. Nothing failed.

Files are in `entries/001545-rajebhosale-2025/`:
- `reproduce_rajebhosale_2025.ipynb`
- `nrg1_ephys.py`
- `entry.yaml`
- `README.md`
- `requirements.in`
- `requirements.lock.txt`

The record is `attempts/001545-rajebhosale-2025-01.yaml`.
