# Zaimi, Wabartha, Herman, Antonsanti, Perone & Cohen-Adad (2018) from dandiset 001436

Tests the findings of [Zaimi et al. (2018)](https://doi.org/10.1038/s41598-018-22181-4), AxonDeepSeg,
that can be tested on [DANDI:001436](https://dandiarchive.org/dandiset/001436/0.250512.1625), which
holds 158 TEM images of the splenium of 20 control and cuprizone mice with manual axon and myelin
masks. The paper's released TEM model (`default_TEM_model_v1`, GitHub commit 7f60132) is run on
every image and scored as in Table 3.

| Claim | Outcome |
|---|---|
| The dandiset's mice can be labelled control or cuprizone through the White Matter Microscopy Database (registry check) | Reproduced |
| Mean pixel-wise accuracy 0.9451 on the mouse images | Reproduced |
| Mean axon Dice, myelin Dice, sensitivity and precision on the mouse images | Reproduced |
| Myelin Dice is below axon Dice in every test sample (mouse images) | Reproduced |
| Sensitivity above 93% in every test set (mouse images) | Reproduced |
| Pixel-wise accuracy 0.8438 on the macaque image (data elsewhere) | Blocked: methods underspecified |
| Myelin is underestimated on the macaque image (data elsewhere) | Reproduced |
| SEM rat and human rows of Table 3, and the other measures of the macaque row | Blocked: data missing |
| Full rat spinal cord slice: processing time and Figure 7 morphometrics (five claims) | Blocked: data missing |

The paper does not name its 3 test mice; every set of 3 mice of the dandiset gives values within
the tolerances. The dandiset does not say which mice are controls; the group comes from the
folder names of the White Matter Microscopy Database (OSF), linked by mouse number and checked
by image content. The attempt record, with the reasons and the differences from the paper's
method, is [`attempts/001436-zaimi-2018-01.yaml`](../../attempts/001436-zaimi-2018-01.yaml).

- `reproduce_zaimi_2018.ipynb`: the analysis. It takes about 21 minutes, most of it the
  segmentation of 158 images twice (with and without the contrast inversion) on CPU.
- `axondeepseg_tem.py`: reading the dandiset and the OSF deposits, the TEM model rebuilt from its
  checkpoint in TensorFlow 2, the inference pipeline of AxonDeepSeg's `segment.py`, and the scores
  of its `segmentation_scoring.py`. Other notebooks on this dandiset can import it.
