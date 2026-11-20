# sadeghi-2019, Sadeghi et al. 2019

Twelve claims reproduced (three on an assumption), ten partially (three on
an assumption), four not reproduced (one on an assumption) and two blocked,
both for missing data. The first verification round agreed with 21 of the
28 outcomes as they stood and the second with 26; the second did not agree
with fig9a-optimal-resolution and fig10-vocalization-background as recorded,
the author proposed partially reproduced for both, and a third round reviewed
those two and agreed. CRCNS data sets carry no version, so the record gives
`unversioned` and the MD5 sums of `checksums.md5` were recorded. The paper,
Sadeghi, Zhai, Stevenson and Escabi, "A neural ensemble correlation code for
sound category identification" (PLoS Biology 17(10):e3000449), records analog
multiunit activity (aMUA) on 16 channels in the central nucleus of the
inferior colliculus of unanesthetized rabbits while natural sounds play, in
three paradigms (five sounds; the same sounds original and 1/f spectrum
equalized; three categories of six exemplars), and reports that spectral and
temporal correlations across channels identify sounds and categories in
single trials, without relying on the sound spectrum alone; in a cochlear
model of 195 sounds in 13 categories it relates correlation widths,
diversity and stationarity to the categories and classifies them at several
temporal resolutions. The claims were written from a text extraction of the
version of record (PMC6788721) with its supplement, without a PDF, so every
displayed equation was lost, and without reading the MATLAB code in the
deposit, which the author followed where the Methods leave a step open.
Reproduced are, among others, the noise correlations' restriction (Fig 2),
the population classifiers above chance with the drop when tonotopy is
removed (25.6 points, paired t = 7.87), the paradigm 3 categorization (94.8,
94.8, 92.2 and 93.3% at 1 s), the model's correlation widths and category
diversity (with norms not squared) and the similar maxima of the three model
classifiers (81.5, 82.1 and 80.5%). Not reproduced are the original against
1/f correlations at the example site (temporal r 0.898 against 0.72) and
across sites, the stationarity index (environmental 0.719 against 0.49) and
the spectrum classifier lying below the others, which ties the temporal one
at the full duration. Partial are the SNR ranges, the two example-site
classifier claims, the 1/f classification claims and five model classifier
claims. The thresholded MUA of S10 Fig and the model's prediction of neural
correlations in S5 Fig are blocked. The author's first run had 11
reproduced, 5 partially, 3 not reproduced and 9 blocked, with the seven
model classifier claims blocked as too large for the time left; round 1
rejected that, and the classifier was built as a third notebook. Round 1
also asked for the aMUA split-half values (0.980 and 0.830, against 0.98 and
0.83), the window lines of NeuralExample.m and a full listing of the tar.
Round 2 found that the spectro-temporal optimum was tied and that fig10's
difference paired curves by window index, not by duration, and asked that
the spectrum classifier's component count be marked assumed. The tie changes
from machine to machine: of the five runs in rounds 2 and 3, three gave
81.0% at 100 ms and a tie at 141 and 283 ms, and two a three-way tie, and
round 3 found that the reasons quoted the other machine's run, so they were
rewritten to cover both. The author asked a reader nothing, so the answer
and author-answers runs changed no outcome. The author's run took about
3 h 30 min (19:48 to 23:19 UTC), with peak memory 3.6 GB; in each revision
`python tools/entry.py all` stopped at the tool's two-hour limit during or
before the model notebook, which was run on its own after round 2 and kept
from an earlier run after rounds 1 and 3.

The data set holds only the aMUA rasters to the natural sounds: the
tone-pip recordings and best frequencies behind Fig 1A and S5 Fig and the
raw voltage traces behind the thresholded MUA of S10 Fig are not deposited,
so those analyses cannot be repeated. The order of the 16 channels along the
probe is not documented, so the channels cannot be assigned to frequencies,
and the Param.RecordDate field holds values such as May2019 and May2019C2
without explanation. The aMUA rasters are sampled at 2034.5 Hz (12207.03 Hz
divided by 6), where the paper states 2 kHz, and the data description gives
no rate. P2_Site08 has 13 trials per sound, where the paper states one
paradigm 2 site with 14; the other trial and site counts match the paper.
The description says all sound files are double precision WAV; the 195 model
sounds are 16 bit integer PCM and the paradigm sounds 32 bit float, and the
model sounds' SD is 0.0003 to 0.0022 of full scale, where the description
says they are normalised to 0.001. The whole data set is one 5.3 GB tar.gz
file, which cannot be read at random (about 4 minutes to decompress), and
the white noise control of the model analyses is not included. The paper's
ModelExample.m builds the cochleogram with b = 94 + 71 f^1.5 where the
Methods give b = 25 + 75(1 + 1.4 f^2)^0.69, and keeps the envelopes at
3675 Hz where the Methods say 1 kHz; the Methods were followed, and the
code's bandwidths hardly change the stationarity index. Three questions are
put to the paper's authors: how the neural classifier's 100 time samples
enter a decision, how its PCs are chosen and on which data the mixing
coefficient is fitted (the median of S9 Fig changes from 0.0 to 0.9 with
these choices); which forms of the SI and CDI were used; and how the model
classifier, for which the deposit holds no code, forms its features, spaces
its windows, sets its PC and component counts and builds the time-averaged
classifier of Fig 9C.

The author's points on the protocol: `docs/archives.md` assumes zip files,
and the single tar.gz was streamed from the start on each pass; developing on
a subset costs a full stream pass when caching to disk is not allowed;
"reproduced under one reading" with many crossed readings lets weak matches
count; the code's window for Fig 1 is not among the criterion's readings, and
it was adopted with the listed readings as variants; a criterion with no
partial rule conflicts with the protocol's general definition, and the
criterion was followed; `too_large` is defined by compute, while the binding
limit was the author's remaining time; a conclusion quoting run times cannot
stay backed across runs; and CRCNS is unversioned, so the MD5 sums were
recorded.
