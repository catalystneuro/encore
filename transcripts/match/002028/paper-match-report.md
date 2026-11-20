I've given a verdict to the three papers the checks left open, and `papers/match/002028.yaml` passes validation. The dataset holds anesthetized cat LGN recordings with natural movies, white noise and full-field flicker at several contrasts. Its description says it "supported four published studies", and those four are the papers below.

| Paper | Verdict | Deciding evidence |
|---|---|---|
| 10.1016/j.neuron.2007.07.013 (Lesica 2007) | primary (checks, kept) | Abstract: "neurons in the cat lateral geniculate nucleus", with high- and low-contrast natural movies and white noise. |
| 10.1038/nature06105 (Butts 2007) | primary (checks, kept) | LGN responses to spatially uniform noise and natural movies, which matches the dataset. |
| 10.1152/jn.00078.2010 (Butts 2010) | primary (agent) | The abstract studies LGN events "in both artificial and natural visual stimulus contexts and at different contrasts". The archive description names this study. |
| 10.1523/jneurosci.0434-11.2011 (Butts 2011) | primary (agent) | Methods (PMC3197857): "recorded from the LGNs of three anaesthetised and paralysed cats", using spatially uniform noise and natural movies. |
| 10.1152/jn.00847.2004 (Weng 2005) | background (agent) | An earlier study from the same lab on receptive field size and latency in neighboring LGN cells. The archive links it as `IsDocumentedBy`, apparently for the methods, and leaves it out of the four studies the dataset supported. |

- **No full text for two papers:** the store had no text for Butts 2010 or Weng 2005, so I judged them from their Europe PMC abstracts and the archive metadata. For Butts 2011 I read the Methods in the PMC author manuscript.
- **One uncertainty:** neither Weng 2005's abstract nor the archive metadata says whether any of its recordings overlap the dataset.
