# 001262, Heeringa et al. 2024

Fifteen claims reproduced (three on an assumption), one partially, three not
reproduced and four blocked, three as `methods_underspecified` and one for
missing data. The first verification round agreed with all 23 outcomes as they
stood and the second with all 23, and nothing was proposed after the second,
so there was no third round; the round-2 report tallied 14 reproduced and 4 not
reproduced, where the record has 15 and 3. It pins version 0.241205.0959, the
newer of the two published versions; the paper cites only its Dryad deposit
(doi:10.5061/dryad.qv9s4mwn4), and both versions hold the same 1160 files. The
paper, Heeringa et al., "Single-unit data for sensory neuroscience: Responses
from the auditory nerve of young-adult and aging gerbils" in Scientific Data,
is a Data Descriptor of single auditory nerve fibres recorded from 104
Mongolian gerbils (60 young adult, 13 middle aged, 31 old), 1160 units with
recordings of tone, click, silence and complex stimuli, and the dataset holds
them as NWB files, one per unit. The claims were written from the version of
record (PMC11035566), which has no supplement, and the paper's MATLAB toolbox
(Zenodo 10370064). The counts, ages, ABR thresholds, weights and BF ranges of
Table 1 reproduce, the ABR values on the assumption that a stored character is
read as its code point, as do the oxygen, complex-stimulus, sampling-by-age,
Fig. 5b, Fig. 6 and Fig. 7a claims; `fig6a-young-two-sensitive-regions` holds
under reading (b) only, and `fig7b-click-latency-bf` (Pearson -0.882 over 268
units) rests on an assumed click delay of 7.75 ms, with the outcome the same at
5 ms. `recording-type-counts` is partial, five of six counts matching and
CLICK giving 271 or 275 against 261. `isi-exclusion` is not reproduced, 370,
391 and 148 of 1160 units having two or more within-trial ISIs below 0.6 ms
under readings (a), (b) and (c); `fig6b-young-bf-gap` is not reproduced, the
named 2423 to 2936 Hz bin holding 34 young-adult units with neighbours of 34
and 35; and `fig7ab-representative-sampling` is not reproduced under the
record's reading of "none does" as no reading holding for both the CF and CLICK
subsets, the claim being blocked as `methods_underspecified` under the other.
`no-prepotentials`, `rlf-monotonic` and `psth-primary-like` are blocked as
`methods_underspecified`, the paper's checks being visual with no rule, and
`old-success-rate` as `data_missing`. The author asked a reader nothing, so the
answer and author-answers runs changed nothing. Round 1 asked that the assumed
click delay be checked against the data, that the very short ISIs be
inspected, that the CF be computed with levels from the calibrated level
column, and for the analysis table's columns and the fig6b counts by
population; in reply a population PSTH of the CLICK trials, a split of the
500-trial recordings, an ISI histogram, a waveform check of every short-ISI
pair and the other outputs were added, and the Methods' rule for a NaN p-value
(N < 50) was made the main reading with the code's as a variant. Round 2 found
sentences the outputs did not support (the Table 1 means "equal after
rounding" at two decimals, the Fig. 7b axis as support for 7.75 ms, the click
coming at the same time in both trial lengths, cell 75 saying the fig7ab
outcome does not depend on the reading, the README's run time of about six
minutes and the 0.3 to 0.6 ms ISIs called double detections), all corrected.
The author's run took about 35 minutes (13:32 to about 14:07 UTC) with nothing
failing, a text substitution in the notebook build script having been fixed;
the notebook ran in 201 s at first, 177 s after the author-answers run, about
5.5 min after round 1 and 4.3 min at the end. The edits under `tools/` were
found already there and left untouched.

The NWB files keep the analysed outcomes the paper describes as stored with
each recording only as best frequency, spontaneous rate and threshold per
recording type (the analysis table has only `experiment`, `id`, `results_bf`,
`results_sr` and `results_threshold`, in every file); the characteristic
frequency, Q10, vector strength with its p-value, the click latencies and
first-spike statistics and the rate-level and frequency-response rates are not
there, so the CF, vector strength and 2-bin click latency were recomputed from
the spike times with the paper's functions, and the manual corrections the code
allows (CF and response criterion, RLF threshold) cannot be recovered. The ABR
threshold in general/notes is written as a single character whose code point is
the threshold, for example '#' for 35 and 'K' for 75, with control characters
such as a line feed for 10 and 'NaN' for 11 animals; read as code points, the
values are multiples of 5 from 10 to 85 dB SPL and give Table 1's means and SDs
exactly, so the number appears to have been converted to a character in the
conversion to NWB. The CLICK trials carry no delay (NaN in the trial table),
nor do the SR, NOISE, SPS and CVC trials, and click_polarity is 'COND' in every
CLICK trial; the population PSTH is flat up to 8.25 ms and the data are
consistent with 7.75 ms in both the 10 ms and 20 ms trials, but do not fix it.
275 units have one CLICK recording each and 271 give a 2-bin latency with the
paper's function, where the Fig. 7 legend counts 261, and without the stored
latencies the difference cannot be traced. 370 of 1160 units have two or more
within-trial ISIs below 0.6 ms in one recording, although the paper says units
with multiple such intervals were excluded; of the 13,904 short intervals all
1171 below 0.1 ms, 91% of those from 0.1 to 0.3 ms and 39% of those from 0.3 to
0.6 ms lie on one spike waveform by a dip-ratio rule, those below 0.1 ms being
double detections and those from 0.3 to 0.6 ms plausibly so, and counting only
intervals between separate waveforms 176 units still fail. The extracellular
glass-electrode recordings are stored as intracellular (icephys)
VoltageClampStimulusSeries, and the archive's summary lists the measurement
technique as 'voltage clamp technique'. The dataset holds only the 104 animals
with recorded units, so the animals operated on without a successful recording,
which the success rates of 43% of old and 88% of young-adult gerbils count, are
not listed. A question is put to the paper's author: what the click delay of
the CLICK recordings was, and whether it was the same in all of them.

The author's points on the protocol: neither the protocol nor the claims file
says what to do when the criteria name stored values the dataset lacks but the
paper's code can recompute, and they were recomputed with deviations recorded;
`assumed` is defined for methods the paper leaves open, while the ABR decoding
is a reading of the data, and the outcomes were marked assumed so it is
visible; the fig7ab criterion is ambiguous when the CF and CLICK subsets
differ; the protocol does not say whether a blocked claim may have outputs, and
tagged cells were added for `rlf-monotonic` and `old-success-rate`; it does not
say whether code read only for method details goes under `inputs`, which was
left empty; and the clock check of step 2 is phrased as decoding a task
variable, and a contrast of tone against silent trials in 5 ms windows was
used instead.
