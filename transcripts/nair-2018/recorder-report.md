I wrote `docs/pilot-notes/crcns-bf-1-nair-2018-01.md` and changed no other file. The untracked dotfiles, `.idea` and `scripts` in the repository root were already there, and I left them alone. Two things to know:

- `targets/dandisets.json` has no entry for CRCNS:bf-1, so there was no `catalystneuro` field to check. The note does not open with the CatalystNeuro sentence.
- The sources don't give the paper's title, so the note names only the authors and the journal.

# crcns-bf-1, Nair et al. 2018

Four claims reproduced, four partially (one on an assumption), two not
reproduced and eighteen blocked, sixteen for missing data and two for
insufficient metadata. The first verification round agreed with 27 of the
28 outcomes as they stood and the second with all 28; nothing was proposed
after the second, so there was no third round. CRCNS does not version data
sets, so the version is recorded as unversioned with the data set's DOI
(10.6080/K0MK6B2Q) and the archive's MD5 from `checksums.md5`, which the
notebook checks while streaming it. The paper, Nair, Klaassen, Arato,
Vyssotski, Harvey and Rainer in PNAS, records basal forebrain (BF) LFP in rats
in the home cage and while they explore a novel arena, finds BF gamma power
(30 to 80 Hz) lower in the arena, rising with movement in the home cage but
not in the arena, and relates BF activity to single units and to the
anterior cingulate (ACC) and visual cortex (VC); the data set holds the BF
LFP of six rats at 400 Hz in 2-s segments, with a movement value per segment
and two home-cage and two arena sessions per rat. The claims were written
from the PyMuPDF text of the version of record and its supplement, without
rendering any figure; the paper links no code. The gamma, movement quartile,
low-frequency band, unimodality and excursion claims could be tested; the
behaviour, object, single-unit, ACC and VC claims, the bipolar recordings,
the consistency over days and the switch back to the home cage could not.
Reproduced are `fig3a-each-hemisphere-significant` (all 12 arena recordings
below the home cage, largest p = 2.7e-30 with 2-s epochs),
`fig3b-arena-gamma-unrelated-to-movement` (one-way p = 1.0),
`figs2-bf-low-frequency-bands` (under all 12 readings) and
`figs3-unimodal-states` (smallest dip-test p = 0.102). Partial are
`fig3a-bf-gamma-reduction` (p = 0.012 over 6 rats, but a reduction of 46.8%
to 48.1% against 35 +/- 3%), `fig3c-home-cage-above-both-sessions` (the home
cage above both arena sessions by Bonferroni-corrected paired t, p = 0.038
and 0.035, not by Tukey's HSD, p = 0.30 and 0.19, the session-order part not
judged), `fig3d-gamma-rises-with-time-in-arena` (r = 0.859 in 1-min bins
against 0.72; 30-s bins give 0.744 and 0.747, within tolerance) and
`figs5-arena-excursions` (the gamma and theta tests hold, but 10.7 to 14.5
excursions per 20 min of 5.1 to 5.6 s on average against 8 of 16 +/- 8 s).
Not reproduced are `fig3b-home-cage-gamma-increases-with-movement` (one-way
ANOVA on per-rat quartile means p = 0.82, though gamma rises in 6 of 6 rats
and a repeated-measures ANOVA gives p = 2.0e-05) and `fig3b-matched-movement`
(p = 0.070, a paired t test of the same values p = 0.0071); both rest on the
claims file's test, which puts the between-rat spread into the error term.
The author's first run had 4 reproduced, 3 partially, 3 not reproduced and 18
blocked, with fig3c not reproduced on the assumption that sessions 1 and 2
are a day's first and second arena trials. The author asked no questions of a
reader, so the answer and author-answers runs changed nothing. Round 1
disagreed on fig3c (partially reproduced, the session-order part blocked as
metadata insufficient, as the descriptor calls the sessions "two separate
examples") and found that the criterion's one-way ANOVA cannot detect a
within-rat effect with six rats, that time in the arena assumed each file
starts at arena entry, that Tukey's test ignores the pairing within rat, that
the boxcar zero-padded file ends and that dip tests were run on raw power
only; in reply fig3c was changed, fig3d was marked assumed for its 1-min bins
with a window anchored at the file end and a sweep of bin widths, the boxcar
was fixed, log10 dip tests were added (one per-session p = 0.035) and whether
the per-rat one-way ANOVA is the paper's test went to a reader in
`questions/crcns-bf-1.yaml`, a file written after the answer run, so the
question is unanswered. Round 2 agreed with all 28 outcomes and found text the
outputs did not support, among them a summary that read as 17 data_missing
claims for 16, a run time in the README with no printed support and 20-s
bins with the end anchor (r = 0.662) left out as within tolerance; in reply
the text was corrected. The author briefly opened another attempt's
`entry.yaml` (crcns-hc-9) to check an id format, against the instruction not
to read other attempts. The notebook ran in about 14 s at first and 19 s, 19 s
and 20 s after the later runs; a string-formatting error during development
was the only failure.

The data set holds only the BF LFP of six rats in home cage and arena: the
ACC and VC recordings, single units, object sessions, video and behaviour
scoring of the paper are not in it, and the paper names no other deposit, so
16 of the 28 claims need data that are not in it. Rat_3_Type_HCage_Session_2.mat
is not a separate recording: 287 of its 291 segments are segments of
Rat_3_Type_HCage_Session_1.mat with the same LFP and movement values, 100 s
later on that file's clock, and it was counted once. The sessions carry no
day and no time of recording, and each file has its own clock starting at 0,
so the paper's day factor, the order of home-cage and arena sessions and the
transfer between them cannot be reconstructed; the descriptor does not say
whether sessions 1 and 2 are a day's two arena trials, which matters, as
session 2 has 15.9% lower gamma than session 1 where the paper reports 5.62%
higher in the second trial. Which electrodes were bipolar is not stated.
Artifact segments were removed without a stated rule, 2.6% to 23.5% of each
file's span against the 1-4% the SI reports, and the SI's rule applied to the
delivered segments removes a further 16.8%. The LFP has no stated unit, and
the movement value is dimensionless, with a scale in rats 4 and 5 about a
quarter of that in the other rats, which is not explained. In 13 of 24 files
the movement value correlates best with the 100-200 Hz LFP power of the next
segment, so the movement stream may lead the LFP by up to one 2-s segment,
and rat 2's home-cage session 1 has a line at 50 Hz, 26 times its neighbours,
inside the gamma band. The descriptor names the home-cage condition 'Hcage'
where the files use 'HCage', and describes basal_forebrain_lfp.tar.gz as a
file of .mat files without saying it is a gzipped tar. Questions are put to
the paper's authors: what the observations of the Fig. 3B one-way ANOVAs were
and whether gamma was normalized per animal; how the 35% reduction was
computed; what power scale, histogram bins and minimum length define the
excursions; and what was correlated with time in Fig. 3D, at what bin width
and from which anchor.

The author's points on the protocol: the guidance on CRCNS data assumes zip
files while bf-1 is a `.tar.gz`, so it was streamed with fsspec and
`tarfile` and its MD5 checked during the stream; the clock check names no
method for data without a trial table, so 100-200 Hz LFP power was compared
with the movement values at shifts of -5 to +5 segments; there is no rule for
a criterion that names no partial outcome when the effect holds and its size
does not, as for fig3d, so partially reproduced was used from the general
definition; several criteria fix a one-way ANOVA on per-rat means that large
between-rat differences make insensitive, and the criterion was followed with
the repeated-measures and paired variants shown; and a duplicated recording
breaks session pairing, so the affected pair was dropped (11 pairs) and the
12-pair version shown as a variant.
