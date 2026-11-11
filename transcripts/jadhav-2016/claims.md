# crcns-hc-28 · claims · run 42477502425

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ claims/crcns-hc-28/ paper/; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md; ls claims/001453/ claims/crcns-hc-28/ paper/; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "offset": 1,
 "limit": 185
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-13`. Record this version in the attempt's provenance.
4	
5	This is what agents, or people, do to attempt a target and deposit the
6	result. A target is a dataset in a public archive and a paper it names. How
7	each archive's datasets are named, versioned and read is in
8	[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
9	([pilot notes](pilot-notes.md)); the reasons for the rules are there.
10	
11	An attempt has three roles, each a separate run with a separate context:
12	
13	- The **reader** reads the paper and writes the claims file: every finding,
14	  and how each is to be tested, taken from the paper. A second reader checks
15	  it against the paper. Readers never see the dataset's data.
16	- The **author** tests the claims on the dataset. It reads the paper to
17	  understand the claims, but the claims file binds it: it cannot change a
18	  claim's statement, expected values or criterion. A method detail the file
19	  lacks it takes from the paper, citing the passage, and it asks a reader
20	  only when it believes the file misreads the paper.
[... 165 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/001453/*.yaml; head -40 paper/10.1016-j.neuron.2016.02.010.txt; wc paper/*.txt; head -60 paper/hc-28.data-description.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2016.02.010.txt",
 "offset": 40,
 "limit": 1000
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "=== page\|Supplemental\|SUPPLEMENT" paper/10.1016-j.neuron.2016.02.010.txt | head -80
```

Result: not kept, because it reads the paper's text.

**Agent**

Main text and Methods read; the supplement is present (pages 17 to 43). Reading it now.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2016.02.010.txt",
 "offset": 1149,
 "limit": 120
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 1800,2700p paper/10.1016-j.neuron.2016.02.010.txt | grep -v "^\s*[0-9.]*\s*$" | awk 'length($0)>25'
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "Table S1 (related\|Table S2 (related\|Table S3 (related\|SUPPLEMENTAL EXPERIMENTAL" paper/10.1016-j.neuron.2016.02.010.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2016.02.010.txt",
 "offset": 2418,
 "limit": 580
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 60,201p paper/hc-28.data-description.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -i "github\|code\b\|software\|available" paper/10.1016-j.neuron.2016.02.010.txt | head; sed -n 1843,2420p paper/10.1016-j.neuron.2016.02.010.txt | awk 'length($0)>40'
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
ls claims | head -50; ls claims/crcns-* 2>/dev/null | head; sed -n 1,80p tools/claims_check.py
```

```
000003
000004
000005
000006
000008
000009
000010
000011
000013
000015
000016
000017
000019
000023
000034
000035
000036
000037
000041
000044
[... 120 more lines not kept]
```

**Agent calls Bash**

```bash
ls -d claims/crcns-hc*; f=$(ls claims/crcns-hc*/*.yaml | head -1); sed -n 1,60p $f; python -c "import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:5000])"
```

```
claims/crcns-hc-10
claims/crcns-hc-11
claims/crcns-hc-14
claims/crcns-hc-16
claims/crcns-hc-24
claims/crcns-hc-7
claims/crcns-hc-9
# Claims for Lee, Marchionni, Bezaire, Varga, Danielson, Lovett-Barron, Losonczy & Soltesz (2014),
# Neuron 82:1129-1144, on CRCNS data set hc-10 (doi:10.6080/K00P0WXQ).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-06,
# protocol as stated in docs/protocol.md (Reader).
#
# Text read: the version of record with its Supplemental Information, as supplied under paper/
# (PyMuPDF text of the journal PDF): Results, Discussion, Experimental Procedures, the legends
# of Figures 1 to 6 and S1 to S5, Table S1 and the Supplemental Experimental Procedures. The
# extracted text prints micrometres as "mm" and some minus signs as a replacement character.
# Values shown only in Figures S1E to S1H and S3F were read from the PDF pages (rendered here)
# and are marked as read from a figure.
#
# Code read: the model code the paper links, ModelDB accession 153280 ("superdeep", NEURON),
[... 196 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[5000:11000])"; grep -rn "hc-28\|10.6080/K02N50G9" claims targets* 2>/dev/null | head
```

```
'PRIDE PXD012345' or 'Zenodo doi:10.5281/zenodo.123'.",
      "type": "string",
      "minLength": 1
     }
    },
    "allOf": [
     {
      "not": {
       "required": [
        "quote",
        "inferred"
       ]
      }
     },
     {
      "if": {
       "properties": {
        "kind": {
         "const": "link"
        }
[... 181 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python -c "
import fitz
d=fitz.open('paper/10.1016-j.neuron.2016.02.010.pdf')
for i in (10,12,6):
    p=d[i]; p.get_pixmap(dpi=110).save(f'p{i+1}.png')
print(len(d))
"; ls $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
which pdftoppm mutool; python -c "import pypdfium2" 2>&1; pip list 2>/dev/null | grep -i -E "pdf|mupdf"
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pypdfium2
ModuleNotFoundError: No module named 'pypdfium2'
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2016.02.010.pdf",
 "pages": "11"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml",
 "content": "# Claims for Jadhav, Rothschild, Roumis & Frank (2016), Neuron 90:113-127, on CRCNS data set\n# hc-28 (doi:10.6080/K02N50G9).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-08,\n# protocol as stated in docs/protocol.md (version pilot-13, Reader).\n#\n# Text read: the version of record with its Supplemental Information, as supplied under paper/\n# (PyMuPDF text of the journal PDF, 43 pages): Results, Discussion, Experimental Procedures, the\n# legends of Figures 1 to 8 and S1 to S7, Tables S1 to S3 and the Supplemental Experimental\n# Procedures. The extracted text prints minus signs and some symbols as a replacement character,\n# so \"p < 10-11\" appears as \"p < 10?11\"; such values were read in context. The PDF could not be\n# rendered in this run, so no value was read from a figure; values shown only in figures (the\n# ensemble-size groups of Figure 6E, the bars of Figures 5F, 6E and 8D) are not recorded.\n#\n# Code read: none. The paper links no code; it says only that analyses used custom Matlab\n# routines. Methods details therefore come from the Experimental Procedures and the\n# Supplemental Experimental Procedures, and the details they leave open are named in each\n# criterion with the readings the text allows.\n#\n# Data the paper used. Six male Long Evans rats, three on a W-track spatial alternation task and\n# three on a Y-track auditory cue-guided task, 8 to 12 days of training, 2 to 4 run sessions of\n# 20 min per day with interleaved 20 to 30 min rest sessions in a rest box; data pooled across\n# all sessions within a day. W-track animals ran 2 sessions per day for 8 days (24 days in all,\n# Figure S2). Tetrodes (21 per drive) in dorsal CA1 and prelimbic/infralimbic PFC, and in\n# intermediate CA1 in two W-track animals; W-track recordings in the right hemisphere. LFP\n# 0.5-400 Hz at 1.5 kHz, spikes at 30 kHz, position from overhead camera at 30 fps. Cells\n# (Table S1, before the spike criterion) per W-track animal, CA1 / iCA1 subset / PFC: HPa\n# 195/54/40, HPb 165/15/80, HPc 86/0/51. After exclusions 536 CA1 and 312 PFC putative excitatory\n# cells across all six animals (165 PFC on the W-track, Table S2). The measured variables are\n# spike times of clustered units, LFP per tetrode, position and speed, and the task epochs (run\n# and rest).\n#\n# What the data set holds. By its description, CRCNS hc-28 holds the three W-track animals HPa,\n# HPb and HPc (spikes, LFP, position, task, tetrode and cell information by day and epoch). The\n# Y-track animals are not in it. The data set also serves Tang et al. (2017), whose final 3 days\n# alternate novel and familiar environments; this paper uses the 8 days of W-track learning\n# (Supplemental Experimental Procedures, Behavioral Tasks), and the author is to keep those days.\n# Most of the paper's results pool both tasks. The paper says the two tasks taken separately\n# gave consistent results (\"analyses applied to the two tasks separately, and with the exclusion\n# of intermediate CA1 cells, yielded consistent results (data not shown)\", Results, first\n# section, paragraph 4). So, for every claim whose numbers pool both tasks, the claim is judged\n# on the W-track animals, and the rule is this: the claim is reproduced when its direction and\n# its test (as the criterion states) hold in the W-track data and the W-track values fall within\n# the tolerances under `expected`; partially reproduced when the direction and test hold but a\n# value falls outside its tolerance (the pooled value includes animals the data set lacks);\n# not reproduced when the direction or the test fails. Where the paper gives W-track numbers\n# (Table S1, Table S2, Figure S2, Figure 8), those are the expected values. Claims of absence\n# are judged on the paper's test alone (protocol, Reader step 3).\n#\n# Methods fixed by the paper and used throughout (Experimental Procedures and Supplemental\n# Experimental Procedures; cited as SEP):\n# - SWRs. Detected on the ripple band (150-250 Hz) of multiple CA1 tetrodes with a 3 SD power\n#   criterion, at speeds below 4 cm/s; SWRs within 1 s of a previously detected SWR are\n#   discarded (SEP, SWR Detection). The paper defers the rest to Karlsson and Frank (2009),\n#   which is not under paper/. Open, with readings: (a) a crossing on any one CA1 tetrode;\n#   (b) on the power averaged or summed over CA1 tetrodes. Minimum duration, envelope smoothing\n#   and the definition of onset (first threshold crossing, or the earlier return to the mean)\n#   are not given; the author follows Karlsson and Frank (2009) if read, and states the choice.\n# - Units. Putative excitatory cells; fast-spiking cells excluded (PFC width < 0.3 ms and rate >\n#   17 Hz; CA1 width < 0.3 ms and rate > 7 Hz); cells with fewer than 50 spikes in SWR-aligned\n#   rasters on a day excluded (SEP, SWR Modulation). Open, with readings: the unit of analysis is\n#   (a) a cell on one day, sessions pooled within the day (the paper's counts are per day:\n#   \"Data were pooled across all sessions within a day\", and the spike criterion is per day);\n#   (b) a unique unit across days. Reading (a) is the paper's best-supported reading. The span\n#   of the SWR-aligned raster is not given; readings -500 to +500 ms (the background window\n#   starts at -500 ms) and -1 to +1 s (SWRs are 1 s apart).\n# - Awake SWRs are those in run epochs of the W-track task; pre-rest is the rest-box epoch\n#   before the day's first run (SEP, Task and rest period comparisons).\n# - SWR modulation. Per cell, the SWR-PSTH; 5000 shuffles, each circularly jittering the spikes\n#   around each SWR by one random amount; modulation measure = squared difference between real\n#   PSTH and mean shuffled PSTH in 0-200 ms; modulated when it exceeds 95% of the shuffled\n#   measures; excited or inhibited by the rate in 0-200 ms against -500 to -100 ms (SEP, SWR\n#   Modulation). Open, with readings: PSTH bin 10 ms (a standard choice); jitter range uniform\n#   over the raster span.\n# - Theta. 6-12 Hz in LFP downsampled to 150 Hz, phase from a CA1 tetrode in corpus callosum;\n#   theta periods at speed > 5 cm/s with no SWR on any CA1 tetrode (3 SD); cells with >= 50\n#   spikes; Rayleigh test p < 0.05; kappa from a von Mises fit (SEP, Theta Phase Locking). The\n#   filter and the phase estimator are not given; a zero-phase band-pass and the Hilbert phase\n#   are standard choices.\n# - Theta cross-covariance. Theta periods >= 1 s; 10 ms bins; expected coincidences subtracted\n#   from the mean rates; standardized by the mean rates, bin size and total theta time; smoothed\n#   with a Gaussian of 50 ms length and SD 16.7 ms; peak taken within -200 to +200 ms (SEP, SWR\n#   Correlations and Theta Cross-covariance). The exact normalization cites Siapas et al. (2005).\n#   Readings: (a) (CCG - r1 r2 B T) / sqrt(r1 r2 B T), a Poisson z-score, which the words\n#   \"standardized (or Z-scored)\" suggest; (b) (CCG - r1 r2 B T) / (r1 r2 B T).\n# - SWR correlation of a CA1-PFC pair. Correlation coefficient across SWRs of the spike counts in\n#   0-200 ms after onset; only pairs with at least 5 SWRs in which both cells spiked (n = 713\n#   pairs) (SEP). Open, with readings: (a) Pearson over all SWRs of the day; (b) Pearson over the\n#   SWRs in which both cells spiked; Spearman shown as a variant. Pair significance p < 0.05.\n# - Spatial maps. Occupancy-normalized linearized rates on the 4 W-track trajectories; coverage\n#   is the fraction of the area above 25% of the peak rate over all 4 trajectories, for cells\n#   with peak > 3 Hz (SEP, Spatial and Behavioral Coding Properties). Bin size, smoothing and any\n#   speed filter are not given; 2 cm bins, no smoothing beyond the paper's, and speed > 5 cm/s\n#   (the paper's movement criterion) are standard choices, shown with no speed filter as a\n#   variant.\n# - Tests. Nonparametric throughout unless noted (\"rank-sum\" is Wilcoxon rank-sum); values are\n#   mean +- SEM; for comparisons among SWR-excited, SWR-inhibited and SWR-unmodulated cells the\n#   threshold is p < 0.01 (SEP, Data Analysis).\nschema_version: 2\ndataset:\n  archive: crcns\n  id: hc-28\n  doi: 10.6080/K02N50G9\npaper: doi:10.1016/j.neuron.2016.02.010\nclaims:\n- id: wtrack-learning\n  statement: On the W-track all animals performed above chance by the third day of training and\n    above 80% correct by the eighth and final day.\n  source: Results, Excitation and Inhibition of PFC Neurons during Awake Hippocampal SWRs,\n    paragraph 1\n  quote: All animals performed above chance by the third day of training, and performed >80% by\n    the eighth and final day of training\n  expected:\n  - quantity: proportion of correct trials on day 8, each W-track animal\n    value: 0.8\n    unit: fraction\n  criterion: The paper gives no scoring procedure beyond the task rule (SEP, Behavioral Tasks)\n    and the cited Jadhav et al. (2012). Trials are well-to-well visits read from position; an\n    inbound trial (to the center after a side well) is correct when the animal returns to the\n    center; an outbound trial (from the center) is correct when it goes to the side opposite the\n    previous side visit. Chance is not defined in the paper; readings are (a) 50% correct over\n    all trials of the day, (b) a binomial test of the day's correct count against 0.5 at p <\n    0.05. Reproduced when every animal is above chance under one reading on day 3 and above 0.8\n    on day 8. A well visit is a stop within the reward-well zone; its radius is not given, and\n    the author states the one used.\n- id: ytrack-learning\n  statement: On the Y-track auditory task animals performed above chance by the fourth day and\n    above 75% by the seventh day.\n  source: Results, Excitation and Inhibition of PFC Neurons during Awake Hippocampal SWRs,\n    paragraph 1\n  quote: Animals performed above chance by the fourth day of training and performed >75% by the\n    seventh day of training\n  criterion: The Y-track animals are not in the data set by its description; the claim is\n    recorded for coverage and is expected to be untestable.\n- id: tables1-cell-counts\n  statement: Before the spike-count criterion, the W-track animals yielded 446 CA1 cells (69 in\n    intermediate CA1) and 172 PFC excitatory cells; after exclusions 165 W-track PFC cells\n    entered the SWR analysis, of 312 PFC and 536 CA1 cells over all six animals.\n  source: Table S1 and Table S2; Results, Excitation and Inhibition of PFC Neurons during Awake\n    Hippocampal SWRs, paragraph 2\n  quote: We recorded a total of 630 CA1 neurons and 353 PFC neurons in six animals over multiple\n    days of behavior in the two tasks ... resulting in a total of 536 CA1 and 312 PFC putative\n    excitatory neurons\n  expected:\n  - quantity: W-track CA1 excitatory cells before the spike criterion (Table S1)\n    value: 446\n    tolerance: 44.6\n  - quantity: W-track iCA1 cells (Table S1)\n    value: 69\n    tolerance: 6.9\n  - quantity: W-track PFC excitatory cells before the spike criterion (Table S1)\n    value: 172\n    tolerance: 17.2\n  - quantity: W-track PFC cells in the SWR modulation analysis (Table S2)\n    value: 165\n    tolerance: 16.5\n  criterion: Counted as cell-days (reading a of the opening comment) and as unique units (reading\n    b), after the fast-spiking exclusion and then after the 50-spike criterion. Area from the\n    tetrode and cell information files. Reproduced when the counts under one reading fall within\n    tolerance. Per-animal counts are reported against Table S1 and Table S2.\n- id: swr-detection-stats\n  statement: Over 53 days 19,888 SWRs were detected (381 +- 18 per day), lasting 96.7 +- 1.2 ms on\n    average, at a mean rate of 0.12 +- 0.01 Hz.\n  source: Supplemental Experimental Procedures, SWR Detection\n  quote: A total of 19,888 SWRs were recorded over 53 days (mean ± sem = 381 ± 18 per day). The\n    average duration of SWRs was 96.7 ± 1.2 ms (n = 19,888 SWRs), and the average SWR rate was\n    0.12 ± 0.01 Hz\n  expected:\n  - quantity: SWRs per day\n    value: 381\n    tolerance: 38.1\n  - quantity: mean SWR duration\n    value: 96.7\n    tolerance: 9.67\n    unit: ms\n  - quantity: mean SWR rate\n    value: 0.12\n    tolerance: 0.012\n    unit: Hz\n  criterion: SWRs detected as in the opening comment, in run epochs (and, as a reading, run and\n    rest epochs together, since the paper does not say which epochs the count covers), over the\n    24 W-track days. Rate is SWRs per second of the epochs used; readings (a) all time, (b) time\n    at speed < 4 cm/s. Tolerances are 10% of the values (the SEMs pool both tasks and are\n    narrower than the difference the W-track subset can be expected to show). Judged by the\n    pooled-value rule of the opening comment.\n- id: figs2-swr-at-reward-wells\n  statement: Most SWRs occurred at reward wells; on the W-track the fraction was 0.71 +- 0.03 of\n    SWRs (n = 24 days), smaller than on the Y-track (0.79 +- 0.02, p = 0.03).\n  source: Figure S2 legend\n  quote: The fraction of SWRs that occurred at reward wells was 0.76 ± 0.02 (mean ± sem, n = 53\n    days), with a small but significant difference between the two tasks (0.71 ± 0.03 for the\n    W-track task with n = 24 days\n  statistics:\n  - about: W-track against Y-track fraction per day\n    test: rank-sum test\n    p: 0.03\n    n: 24 W-track and 29 Y-track days\n  expected:\n  - quantity: fraction of SWRs at reward wells per W-track day, mean over days\n    value: 0.71\n    tolerance: 0.03\n    unit: fraction\n  criterion: Per W-track day, the fraction of run-epoch SWRs whose position lies at a reward well.\n    The paper gives no radius for \"at a reward well\"; readings are a zone of 10, 15 and 20 cm\n    around each well's position (taken as the end of each arm in the linearization). Reproduced\n    when the mean over the 24 days is within 0.71 +- 0.03 under one reading. The comparison with\n    the Y-track cannot be made with the data set.\n- id: fig3-pfc-swr-modulation-fractions\n  statement: About a third of PFC neurons were significantly SWR modulated, in roughly equal\n    numbers excited and inhibited; on the W-track 30 of 165 were SWR-excited (18%) and 26 of 165\n    SWR-inhibited (16%).\n  source: Results, Excitation and Inhibition of PFC Neurons during Awake Hippocampal SWRs,\n    paragraph 3; Figure 3A to 3C; Table S2\n  quote: Overall, 35% (109/312) of PFC neurons were significantly SWR modulated ... we were\n    therefore surprised to see approximately equal numbers of excited and inhibited response\n    patterns during awake SWRs (Figures 3A-3C; SWRexcited, 57/312, 18%; SWR-inhibited, 52/312\n    cells, 17%)\n  expected:\n  - quantity: W-track SWR-excited PFC cells (Table S2)\n    value: 30\n    tolerance: 3\n  - quantity: W-track SWR-inhibited PFC cells (Table S2)\n    value: 26\n    tolerance: 2.6\n  - quantity: W-track SWR-unmodulated PFC cells (Table S2)\n    value: 109\n    tolerance: 10.9\n  - quantity: W-track fraction SWR-excited\n    value: 0.18\n    tolerance: 0.018\n  - quantity: W-track fraction SWR-inhibited\n    value: 0.16\n    tolerance: 0.016\n  criterion: SWR modulation and its sign as in the opening comment (SEP, SWR Modulation), on the\n    W-track PFC cells that pass the exclusions. Reproduced when the counts, or the fractions,\n    fall within tolerance under one reading of the open details, and excited and inhibited\n    counts are similar (each within 10 percentage points of the other as a fraction of\n    modulated cells). The shuffle is random; the seed is a standard choice. Per-animal counts\n    are reported against Table S2.\n  depends_on:\n  - tables1-cell-counts\n- id: ca1-swr-modulated\n  statement: Most CA1 cells were SWR modulated (429 of 536).\n  source: Supplemental Experimental Procedures, SWR Modulation, paragraph 2\n  quote: Using a similar criterion for CA1 cells, we found 429/ 536 cells to be SWR-modulated\n  expected:\n  - quantity: fraction of CA1 cells SWR modulated\n    value: 0.80\n    tolerance: 0.08\n    unit: fraction\n  criterion: The same shuffle criterion as for PFC, on W-track CA1 cells. Judged by the\n    pooled-value rule of the opening comment.\n  depends_on:\n  - tables1-cell-counts\n- id: fig3-transient-responses\n  statement: Both SWR-excited and SWR-inhibited PFC populations respond transiently, their mean\n    rates returning to baseline within about 300 ms of SWR onset.\n  source: Results, Excitation and Inhibition of PFC Neurons during Awake Hippocampal SWRs,\n    paragraph 3; Figure 3D\n  quote: Both populations showed transient responses to SWRs, with average firing rates returning\n    to baseline values within\n  inferred: false\n  criterion: The population mean of the per-cell z-scored SWR-PSTHs (Figure 3B, D). The paper does\n    not define a return to baseline. Readings are (a) the population mean falls within the\n    baseline mean +- 1 SD (baseline from -500 to -100 ms, the paper's background window and\n    its 1 SD onset rule) and stays there, (b) within the 95% interval of the baseline bins.\n    Reproduced when, under one reading, both populations are back at baseline by 300 ms (with a\n    10% margin, 330 ms).\n  depends_on:\n  - fig3-pfc-swr-modulation-fractions\n- id: fig3de-ca1-precedes-pfc-peak\n  statement: The peak of CA1 population SWR activity precedes the peak of SWR-excited and the\n    trough of SWR-inhibited PFC activity (54 +- 2, 100 +- 9 and 84 +- 10 ms), while excited and\n    inhibited PFC timing do not differ.\n  source: Results, Excitation and Inhibition of PFC Neurons during Awake Hippocampal SWRs,\n    paragraph 4; Figure 3D and 3E\n  quote: The time of the peak CA1 population activity preceded both the peak of the SWR-excited\n    and the trough of the SWR-inhibited PFC population activity\n  statistics:\n  - about: CA1 against PFC excited\n    test: rank-sum test\n    p: 1.0e-11\n    p_relation: \"<\"\n  - about: CA1 against PFC inhibited\n    test: rank-sum test\n    p: 1.0e-6\n    p_relation: \"<\"\n  - about: PFC excited against PFC inhibited\n    test: rank-sum test\n    p: 0.1\n    p_relation: \">\"\n    n: 429 CA1, 57 SWR-excited and 52 SWR-inhibited PFC cells\n  expected:\n  - quantity: CA1 peak time, mean\n    value: 54\n    tolerance: 2\n    unit: ms\n  - quantity: SWR-excited PFC peak time, mean\n    value: 100\n    tolerance: 9\n    unit: ms\n  - quantity: SWR-inhibited PFC trough time, mean\n    value: 84\n    tolerance: 10\n    unit: ms\n  criterion: Per cell, the time of the peak (CA1 SWR-modulated cells and SWR-excited PFC) or\n    trough (SWR-inhibited PFC) of the average SWR-PSTH (SEP, Timing of SWR-response). Which CA1\n    cells enter is read from the n (429, the SWR-modulated CA1 cells). The search window is not\n    given; readings are (a) 0 to 200 ms, the modulation window, (b) 0 to 500 ms. Bin 10 ms is a\n    standard choice. Rank-sum tests. Reproduced when CA1 is earlier than both PFC groups at p <\n    0.05 and excited and inhibited do not differ at p < 0.05, with the means judged by the\n    pooled-value rule.\n  depends_on:\n  - fig3-pfc-swr-modulation-fractions\n  - ca1-swr-modulated\n- id: fig3e-onset-later-in-pfc\n  statement: SWR modulation onset (the first rise or fall of 1 SD from the mean) is later for PFC\n    than for CA1 cells, and does not differ between excited and inhibited PFC cells.\n  source: Results, Excitation and Inhibition of PFC Neurons during Awake Hippocampal SWRs,\n    paragraph 4; Figure 3E, right\n  quote: Similarly, the time of SWR-modulation onset, measured as the time of firing rate\n    increase/decrease to 1 SD above/below the mean, was also significantly later for PFC than\n    CA1 cells\n  statistics:\n  - about: CA1 against PFC excited\n    test: rank-sum test\n    p: 1.0e-9\n    p_relation: \"<\"\n  - about: CA1 against PFC inhibited\n    test: rank-sum test\n    p: 1.0e-7\n    p_relation: \"<\"\n  - about: PFC excited against PFC inhibited\n    test: rank-sum test\n    p: 0.1\n    p_relation: \">\"\n  criterion: Onset is the first time after SWR onset at which the SWR-PSTH rises (CA1, excited)\n    or falls (inhibited) 1 SD away from the mean (SEP, Timing of SWR-response). The mean and SD\n    are not specified; readings are (a) of the baseline -500 to -100 ms, (b) of the whole PSTH.\n    Reproduced when, under one reading, both PFC groups are later than CA1 at p < 0.05 by\n    rank-sum and excited and inhibited do not differ at p < 0.05.\n  depends_on:\n  - fig3de-ca1-precedes-pfc-peak\n- id: fig3f-swr-cross-covariance-lag\n  statement: During SWRs the mean CA1-PFC cross-covariance peaks (excited pairs) or troughs\n    (inhibited pairs) after zero lag, at 13 +- 7 and 20 +- 7 ms, so CA1 leads PFC.\n  source: Results, Excitation and Inhibition of PFC Neurons during Awake Hippocampal SWRs,\n    paragraph 4; Figure 3F\n  quote: The peak (SWR-excited) or trough (SWRinhibited) of the mean cross-covariance occurred at\n    a time >0 ms (Figure 3F; peak for excited cells, 13 ± 7 ms; trough for inhibited cells, 20 ±\n    7 ms)\n  expected:\n  - quantity: peak lag, CA1 against SWR-excited PFC\n    value: 13\n    tolerance: 7\n    unit: ms\n  - quantity: trough lag, CA1 against SWR-inhibited PFC\n    value: 20\n    tolerance: 7\n    unit: ms\n  criterion: Cross-covariance from the SWR-aligned rasters of simultaneously recorded SWR-modulated\n    CA1 and PFC cells, adjusted for mean rates (SEP, Timing of SWR-response); the pairs are the\n    393 and 320 of the SWR correlation analysis (same n). Positive lag means PFC after CA1.\n    Bin size and smoothing are not given; 10 ms bins and the Gaussian of the theta\n    cross-covariance (SD 16.7 ms) are taken from the SEP as the nearest stated choice. Reproduced\n    when both extrema lie after 0 ms and within tolerance (pooled-value rule).\n  depends_on:\n  - fig6-swr-correlated-pairs\n- id: fig4-theta-locked-fraction\n  statement: 60% of PFC neurons (189 of 312) were significantly phase locked to hippocampal theta.\n  source: Results, SWR Modulation Is Related to Theta Phase Locking of PFC Neurons, paragraph 1;\n    Table S3\n  quote: we found that 60% of PFC neurons (189 of 312, see Experimental Procedures) were\n    significantly locked to theta\n  expected:\n    quantity: fraction of PFC cells theta locked\n    value: 0.60\n    tolerance: 0.06\n    unit: fraction\n  criterion: Rayleigh test p < 0.05 on theta phases of spikes in theta periods, cells with >= 50\n    such spikes (SEP, Theta Phase Locking); denominator all PFC cells of the SWR analysis (312, as\n    the paper counts). Judged by the pooled-value rule.\n  depends_on:\n  - fig3-pfc-swr-modulation-fractions\n- id: fig4a-preferred-phases\n  statement: CA1 neurons prefer the falling phase of theta, while PFC neurons are most often\n    locked to the theta trough.\n  source: Results, SWR Modulation Is Related to Theta Phase Locking of PFC Neurons, paragraph 1;\n    Figure 4A\n  quote: CA1 neurons preferred the falling phase of theta, while PFC neurons were most often phase\n    locked to the trough of theta\n  criterion: Preferred phase per significantly locked cell is the von Mises mean of its spike\n    phases, theta from the corpus callosum reference tetrode (SEP). The phase convention is not\n    given; Hilbert phase with 0 degrees at the peak and 180 at the trough is the standard choice,\n    and the inverted reference is a reading the author shows, since the polarity of the\n    reference relative to the figure is not stated. Reproduced when, under one convention\n    applied to both regions, the circular mean of CA1 preferred phases lies in the falling phase\n    (0 to 180 degrees) and the modal 45-degree bin of PFC preferred phases contains 180 degrees,\n    with the CA1 mean earlier than the PFC mean.\n  depends_on:\n  - fig4-theta-locked-fraction\n- id: fig4-swr-modulated-more-theta-locked\n  statement: Most SWR-modulated PFC neurons were also theta locked (44 of 57 excited, 77%; 37 of\n    52 inhibited, 71%), more than unmodulated neurons (108 of 203, 53%), with no difference\n    between excited and inhibited.\n  source: Results, SWR Modulation Is Related to Theta Phase Locking of PFC Neurons, paragraph 2;\n    Table S3\n  quote: This included 44/57 SWR-excited neurons (77%) and 37/52 inhibited neurons (71%). There\n    was no difference in the fraction of phase-locked cells in the excited and inhibited neuron\n    populations (p > 0.4), but both had a higher fraction of phase-locked cells than was seen for\n    SWR-unmodulated neurons (108/203 neurons: 53%\n  statistics:\n  - about: excited against inhibited\n    test: z test for proportions\n    p: 0.4\n    p_relation: \">\"\n  - about: unmodulated against excited\n    test: z test for proportions\n    p: 0.001\n    p_relation: \"<\"\n  - about: unmodulated against inhibited\n    test: z test for proportions\n    p: 0.01\n  expected:\n  - quantity: fraction theta locked, SWR-excited\n    value: 0.77\n    tolerance: 0.077\n  - quantity: fraction theta locked, SWR-inhibited\n    value: 0.71\n    tolerance: 0.071\n  - quantity: fraction theta locked, SWR-unmodulated\n    value: 0.53\n    tolerance: 0.053\n  criterion: Two-sample z tests for proportions. Reproduced when both modulated groups have a\n    higher fraction than unmodulated at p < 0.05 and excited and inhibited do not differ at p <\n    0.05, with fractions judged by the pooled-value rule. With about half the cells, the W-track\n    tests have less power; the effect sizes are reported either way.\n  depends_on:\n  - fig4-theta-locked-fraction\n- id: fig4b-kappa\n  statement: Theta-locked SWR-excited and SWR-inhibited PFC cells lock more strongly (kappa 0.2 +-\n    0.02 and 0.25 +- 0.04) than SWR-unmodulated cells (0.12 +- 0.01), with no difference between\n    excited and inhibited.\n  source: Results, SWR Modulation Is Related to Theta Phase Locking of PFC Neurons, paragraph 3;\n    Figure 4B\n  quote: The circular concentration parameter (k) for theta-modulated cells was larger in both the\n    SWR-excited and SWR-inhibited populations, as compared to SWR-unmodulated neurons\n  statistics:\n  - about: unmodulated against excited and against inhibited\n    test: rank-sum test\n    p: 0.01\n    p_relation: \"<\"\n  - about: excited against inhibited\n    test: rank-sum test\n    p: 0.1\n    p_relation: \">\"\n  expected:\n  - quantity: kappa, SWR-excited\n    value: 0.2\n    tolerance: 0.02\n  - quantity: kappa, SWR-inhibited\n    value: 0.25\n    tolerance: 0.04\n  - quantity: kappa, SWR-unmodulated\n    value: 0.12\n    tolerance: 0.01\n  criterion: Kappa from a von Mises maximum-likelihood fit of each theta-modulated cell's spike\n    phases (SEP). Rank-sum tests at the paper's threshold for three-group comparisons, p < 0.01.\n    Reproduced when both modulated groups exceed unmodulated at p < 0.01 and excited and\n    inhibited do not differ at p < 0.01; means by the pooled-value rule. Readings for the\n    cells entered are (a) theta-locked cells only (the text says \"for theta-modulated cells\"),\n    (b) all cells with >= 50 theta spikes.\n  depends_on:\n  - fig4-swr-modulated-more-theta-locked\n- id: fig4c-theta-locked-more-swr-modulated\n  statement: Theta-modulated PFC neurons (n = 189) are more strongly SWR modulated than neurons\n    that are not theta modulated (n = 123), SWR modulation index 5.2 +- 0.8 against 2.5 +- 0.4.\n  source: Results, SWR Modulation Is Related to Theta Phase Locking of PFC Neurons, paragraph 3;\n    Figure 4C\n  quote: PFC neurons that were significantly theta modulated (n = 189) were also significantly\n    more strongly SWR modulated than neurons that were not theta modulated (n = 123) (Figure 4C,\n    SWR modulation index, 5.2 ± 0.8 and 2.5 ± 0.4 respectively; p < 0.01, rank-sum test)\n  statistics:\n  - test: rank-sum test\n    p: 0.01\n    p_relation: \"<\"\n    n: 189 theta-modulated and 123 theta-unmodulated PFC cells\n  expected:\n  - quantity: SWR modulation index, theta modulated\n    value: 5.2\n    tolerance: 0.8\n  - quantity: SWR modulation index, theta unmodulated\n    value: 2.5\n    tolerance: 0.4\n  criterion: The \"SWR modulation index\" is not defined beyond the modulation measure (squared\n    difference between real and mean shuffled PSTH, 0-200 ms; SEP). Readings are (a) that measure\n    divided by the mean of the shuffled measures, (b) the measure as a z-score against the\n    shuffled measures, (c) the raw measure. Reproduced when theta-modulated cells exceed\n    unmodulated at p < 0.01 (rank-sum) under the reading used, and the values are judged by the\n    pooled-value rule under one reading.\n  depends_on:\n  - fig4-theta-locked-fraction\n- id: fig4-preferred-phase-concentration\n  statement: Preferred theta phases of SWR-excited neurons are more concentrated than those of\n    SWR-unmodulated neurons (p = 0.005), while SWR-inhibited and unmodulated neurons do not\n    differ, nor do excited and inhibited (p > 0.1).\n  source: Results, SWR Modulation Is Related to Theta Phase Locking of PFC Neurons, paragraph 4\n  quote: SWR-excited versus SWR-unmodulated, n = 57 versus 203 neurons, p = 0.005). In contrast,\n    SWR-inhibited and SWR-unmodulated neurons did not differ in their concentration of preferred\n    phases (n = 52 versus 203 neurons, p > 0.1, kuiper test)\n  statistics:\n  - about: excited against unmodulated\n    test: Kuiper test\n    p: 0.005\n    n: 57 and 203 neurons\n  - about: excited against inhibited\n    test: Kuiper test\n    p: 0.1\n    p_relation: \">\"\n    n: 57 and 52 neurons\n  - about: inhibited against unmodulated\n    test: Kuiper test\n    p: 0.1\n    p_relation: \">\"\n    n: 52 and 203 neurons\n  criterion: Two-sample Kuiper tests on the preferred phases. The n (57, 52, 203) are all cells of\n    each group, so the paper's reading enters every cell of the group; the theta-locked cells only\n    are shown as a variant. The text calls the excited distribution narrower than both other\n    groups, but reports p > 0.1 against inhibited; the statement follows the tests. Reproduced\n    when excited against unmodulated is significant at p < 0.01 and the two other comparisons are\n    not.\n  depends_on:\n  - fig4-swr-modulated-more-theta-locked\n- id: theta-lag-past\n  statement: PFC cells phase lock best to hippocampal theta about 15 ms in the past.\n  source: Results, SWR Modulation Is Related to Theta Phase Locking of PFC Neurons, paragraph 5\n  quote: we also found that all PFC cells phase locked optimally to hippocampal theta of the past\n  expected:\n    quantity: delay of maximal phase locking\n    value: -15\n    tolerance: 1.5\n    unit: ms\n  criterion: The paper shows no data (\"data not shown\") and gives no method beyond shifting the\n    time of theta. Spike times are shifted relative to the theta phase in steps of 5 ms over -100\n    to +100 ms (a standard choice), and locking strength is measured as kappa. Readings are (a)\n    the shift maximizing the mean kappa over theta-locked PFC cells, (b) the median over cells of\n    each cell's best shift. Reproduced when, under one reading, the best shift is negative (theta\n    in the past) and within 10 ms of -15 ms. The tolerance is widened to 10 ms because the\n    paper prints \"delay ~15 ms\" without spread and the shift step is 5 ms.\n  depends_on:\n  - fig4-theta-locked-fraction\n- id: fig5b-mean-rates\n  statement: SWR-excited and SWR-inhibited PFC cells fire at higher mean rates during movement than\n    SWR-unmodulated cells (4.2 +- 0.5, 3.2 +- 0.4 and 2.1 +- 0.2 Hz), and excited and inhibited do\n    not differ.\n  source: Results, SWR-Excited and Inhibited PFC Neurons Comprise Distinct Functional\n    Populations, paragraph 2; Figure 5B\n  quote: both SWR-excited and SWR-inhibited cells had significantly higher mean rates than\n    SWR-unmodulated cells\n  statistics:\n  - about: excited against unmodulated\n    test: rank-sum test\n    p: 0.01\n    p_relation: \"<\"\n  - about: inhibited against unmodulated\n    test: rank-sum test\n    p: 0.0001\n    p_relation: \"<\"\n  - about: excited against inhibited\n    test: rank-sum test\n    p: 0.1\n    p_relation: \">\"\n    n: 57 excited, 52 inhibited and 203 unmodulated cells\n  expected:\n  - quantity: mean rate, SWR-excited\n    value: 4.2\n    tolerance: 0.5\n    unit: Hz\n  - quantity: mean rate, SWR-inhibited\n    value: 3.2\n    tolerance: 0.4\n    unit: Hz\n  - quantity: mean rate, SWR-unmodulated\n    value: 2.1\n    tolerance: 0.2\n    unit: Hz\n  criterion: Mean firing rate during movement. \"Movement\" is not defined for this measure; readings\n    are (a) time at speed > 5 cm/s with no SWR, the paper's theta and behavior periods (SEP), (b)\n    time at speed > 4 cm/s, the complement of the SWR speed criterion, (c) the mean rate over the\n    whole run epoch. Rank-sum tests at p < 0.01. Reproduced when, under one reading, both\n    modulated groups exceed unmodulated at p < 0.01 and excited and inhibited do not differ;\n    means by the pooled-value rule.\n  depends_on:\n  - fig3-pfc-swr-modulation-fractions\n- id: fig5c-spatial-coverage\n  statement: SWR-excited PFC neurons cover more of the environment (0.70 +- 0.05) than SWR-inhibited\n    (0.54 +- 0.05) and SWR-unmodulated neurons (0.50 +- 0.02), which do not differ, and CA1 cells\n    cover less than all PFC groups.\n  source: Results, SWR-Excited and Inhibited PFC Neurons Comprise Distinct Functional\n    Populations, paragraph 2; Figure 5C\n  quote: SWR-excited neurons had significantly higher levels of coverage than both the\n    SWR-inhibited and the SWR-unmodulated neurons (Figure 5C; coverages were as follows; excited,\n    0.70 ± 0.05; inhibited, 0.54 ± 0.05; unmodulated, 0.50 ± 0.02\n  statistics:\n  - about: excited against inhibited\n    test: rank-sum test\n    p: 0.01\n    p_relation: \"<\"\n  - about: excited against unmodulated\n    test: rank-sum test\n    p: 0.0001\n    p_relation: \"<\"\n  - about: inhibited against unmodulated\n    test: rank-sum test\n    p: 0.1\n    p_relation: \">\"\n  - about: CA1 against each PFC group\n    test: rank-sum test\n    p: 0.01\n    p_relation: \"<\"\n  expected:\n  - quantity: coverage, SWR-excited\n    value: 0.70\n    tolerance: 0.05\n  - quantity: coverage, SWR-inhibited\n    value: 0.54\n    tolerance: 0.05\n  - quantity: coverage, SWR-unmodulated\n    value: 0.50\n    tolerance: 0.02\n  criterion: Coverage as in the opening comment (cells with peak > 3 Hz). Rank-sum tests at p <\n    0.01. Reproduced when excited exceeds both other PFC groups at p < 0.01, inhibited and\n    unmodulated do not differ, and CA1 is below every PFC group at p < 0.01; means by the\n    pooled-value rule. The coverage of the W-track is the only kind the data set holds, so the\n    linearization is the paper's own 4 trajectories.\n  depends_on:\n  - fig3-pfc-swr-modulation-fractions\n- id: figs3-arm-and-direction-selectivity\n  statement: CA1 cells are more selective than all PFC groups for arm and for inbound or outbound\n    direction, and SWR-excited PFC cells are less direction selective than SWR-unmodulated cells.\n  source: Figure S3B and S3D legends\n  quote: The CA1 population has significantly higher selectivity for specific inbound or outbound\n    trajectories than all the PFC populations ... SWR-excited neurons have significantly lower\n    direction selectivity than SWR-unmodulated neurons (*p< 0.01, rank-sum test)\n  statistics:\n  - about: CA1 against PFC, arm and direction selectivity\n    test: rank-sum test\n    p: 0.0001\n    p_relation: \"<\"\n  - about: SWR-excited against SWR-unmodulated, direction selectivity\n    test: rank-sum test\n    p: 0.01\n    p_relation: \"<\"\n  criterion: Arm index is |left - right| / (left + right) of arm firing rates; direction index is\n    |outward - inward| / (outward + inward) (SEP, Spatial and Behavioral Coding Properties).\n    Which rate enters (mean or peak over the arm's linearized bins) is not stated; readings are\n    mean and peak. Reproduced when, under one reading, CA1 exceeds each PFC group in both indices\n    at p < 0.01 and excited is below unmodulated in direction index at p < 0.01.\n  depends_on:\n  - fig5c-spatial-coverage\n- id: fig5e-speed-correlation\n  statement: SWR-excited cells have higher firing rate-speed correlations than SWR-inhibited cells,\n    whose median correlation is below zero, while unmodulated cells do not differ from either.\n  source: Results, SWR-Excited and Inhibited PFC Neurons Comprise Distinct Functional\n    Populations, paragraph 3; Figure 5D and 5E\n  quote: SWR-excited cells showing a significantly higher firing rate-speed correlation than\n    SWR-inhibited cells (Figures 5D and 5E; p < 0.01 for excited versus inhibited, rank-sum\n    test). Further, the median of SWR-inhibited cells' speed correlations was significantly less\n    than zero\n  statistics:\n  - about: excited against inhibited\n    test: rank-sum test\n    p: 0.01\n    p_relation: \"<\"\n  - about: median of inhibited cells below zero\n    test: shuffle test, 1000 shuffles\n    p: 0.01\n    p_relation: \"<\"\n  - about: unmodulated against excited or inhibited\n    test: rank-sum test\n    p: 0.05\n    p_relation: \">\"\n  criterion: The rate-speed correlation is not specified. Readings are (a) Pearson correlation\n    across time bins of the run epochs between spike count and mean speed, with 200 ms bins (the\n    bin of the paper's behavior GLM, SEP) and 1 s bins; (b) correlation between speed-bin centers\n    and the rate in each speed bin. The shuffle for the median is not described; readings are (a)\n    circularly shifting each cell's spike train relative to speed, (b) shuffling speed bins.\n    Reproduced when, under one reading, excited exceeds inhibited at p < 0.01, the inhibited median\n    is below zero at p < 0.01, and unmodulated does not differ from either at p < 0.05.\n  depends_on:\n  - fig3-pfc-swr-modulation-fractions\n- id: fig5f-pre-swr-vs-movement\n  statement: SWR-inhibited cells fire more just before SWRs than during high-speed movement, while\n    SWR-excited cells show the opposite preference.\n  source: Results, SWR-Excited and Inhibited PFC Neurons Comprise Distinct Functional\n    Populations, paragraph 3; Figure 5F\n  quote: we found that firing rates of SWR-inhibited cells just prior to SWRs were higher than\n    those during high-speed movement. In contrast, SWR-excited cells showed the opposite pattern,\n    with a preference for movement times\n  statistics:\n  - test: rank-sum test\n    p: 0.001\n    p_relation: \"<\"\n    n: 57 excited and 52 inhibited cells\n  criterion: Index (pre-SWR - high speed) / (pre-SWR + high speed), pre-SWR rate in -500 to -100 ms\n    before SWR onset, high speed > 10 cm/s (SEP, Spatial and Behavioral Coding Properties).\n    Reproduced when the inhibited index exceeds the excited index by rank-sum at p < 0.01 (the\n    legend prints p < 0.01, the text p < 0.001) and the group means have opposite signs, inhibited\n    positive.\n  depends_on:\n  - fig3-pfc-swr-modulation-fractions\n- id: figs3e-reward-modulation\n  statement: SWR-inhibited PFC cells increase their firing after reward more than SWR-excited cells.\n  source: Figure S3E and S3F legends; Results, SWR-Excited and Inhibited PFC Neurons Comprise\n    Distinct Functional Populations, paragraph 3\n  quote: PFC SWR-inhibited cells also showed a greater tendency to increase firing rates following\n    reward than SWR-excited cells\n  statistics:\n  - test: rank-sum test\n    p: 0.007\n    n: 56 SWR-excited, 51 SWR-inhibited and 194 SWR-unmodulated cells\n  criterion: Reward modulation index (post - pre) / (post + pre), post 0 to 2 s after reward, pre\n    -3 to -1 s before, reward times extracted for each trajectory from position and speed (SEP).\n    The reward time rule is not given; readings are (a) arrival in the well zone at the end of a\n    rewarded trajectory, (b) the first time speed drops below 4 cm/s there. Reproduced when the\n    inhibited index exceeds the excited index by rank-sum at p < 0.01 under one reading.\n  depends_on:\n  - figs2-swr-at-reward-wells\n  - fig3-pfc-swr-modulation-fractions\n- id: fig5g-ensemble-cofiring\n  statement: During movement, like-modulated PFC pairs fire together while excited-inhibited pairs\n    do not; the theta cross-covariance peak of excited-inhibited pairs is lower than that of every\n    other pair category.\n  source: Results, SWR-Excited and Inhibited PFC Neurons Comprise Distinct Functional\n    Populations, paragraph 4; Figure 5G\n  quote: SWR-excited cells tended to fire in close temporal proximity to other SWR-excited cells\n    and SWR-inhibited cells tended to fire in proximity to other SWR-inhibited cells, but\n    SWR-excited and SWR-inhibited cells tended not to fire together\n  statistics:\n  - test: rank-sum test\n    p: 0.001\n    p_relation: \"<\"\n    n: 42 excited-excited, 36 inhibited-inhibited, 73 excited-inhibited and 369\n      unmodulated-unmodulated pairs\n  expected:\n  - quantity: excited-excited pairs\n    value: 42\n    tolerance: 4.2\n  - quantity: inhibited-inhibited pairs\n    value: 36\n    tolerance: 3.6\n  - quantity: excited-inhibited pairs\n    value: 73\n    tolerance: 7.3\n  - quantity: unmodulated-unmodulated pairs\n    value: 369\n    tolerance: 36.9\n  criterion: Simultaneously recorded PFC pairs, standardized theta cross-covariance as in the\n    opening comment. \"Maximum zero lag cross-covariance\" can be read as (a) the peak of the\n    smoothed cross-covariance within -200 to +200 ms (SEP), (b) its value at zero lag. Whether\n    pairs on the same tetrode enter is not stated; both are shown. Reproduced when, under one\n    reading, excited-inhibited pairs are lower than each other category at p < 0.001 by rank-sum;\n    pair counts by the pooled-value rule.\n  depends_on:\n  - fig3-pfc-swr-modulation-fractions\n- id: fig6-swr-correlated-pairs\n  statement: 16% of CA1-PFC pairs (116 of 713) are significantly correlated across SWRs, more than\n    the about 5% found after shuffling, with similar proportions for SWR-excited (72 of 393, 18%)\n    and SWR-inhibited (44 of 320, 14%) PFC cells.\n  source: Results, Structured Reactivation of CA1-PFC Pairs during SWRs, paragraph 3; Figure S4A;\n    SEP, SWR Correlations and Theta Cross-covariance\n  quote: We found that 16% of CA1-PFC neuron pairs were significantly SWR correlated (n = 116/713\n    CA1-PFC pairs, p < 0.05 criterion for individual pairs\n  statistics:\n  - about: fraction of significant pairs against shuffled\n    test: Z test for proportions\n    statistic: z = 6.5\n    p: 1.0e-8\n    p_relation: \"<\"\n    n: 713 CA1-PFC pairs\n  expected:\n  - quantity: fraction of pairs SWR correlated, all\n    value: 0.16\n    tolerance: 0.016\n  - quantity: fraction of pairs SWR correlated, SWR-excited PFC\n    value: 0.18\n    tolerance: 0.018\n  - quantity: fraction of pairs SWR correlated, SWR-inhibited PFC\n    value: 0.14\n    tolerance: 0.014\n  criterion: Pairs of simultaneously recorded CA1 cells and SWR-modulated PFC cells with at least 5\n    SWRs in which both spike; SWR correlation and its readings as in the opening comment; pair\n    significant at p < 0.05. Shuffle by permuting the PFC rates across SWRs (the paper's \"shuffling\n    the rates across SWRs\"). Reproduced when the fraction exceeds the shuffled fraction by a z test\n    for proportions at p < 0.05 under one reading, with fractions by the pooled-value rule.\n  depends_on:\n  - fig3-pfc-swr-modulation-fractions\n  - ca1-swr-modulated\n- id: fig6ab-both-signs\n  statement: Significant CA1-PFC SWR correlations include both positive and negative correlations,\n    for both SWR-excited and SWR-inhibited PFC cells.\n  source: Results, Structured Reactivation of CA1-PFC Pairs during SWRs, paragraph 3; Figure 6A,\n    6B and S4A\n  quote: these included both positive and negative correlations with both SWR-excited and\n    SWR-inhibited PFC populations\n  criterion: Reproduced when, among significant pairs, at least one positive and one negative\n    correlation occur in each PFC group, under the reading of fig6-swr-correlated-pairs that is\n    used there. The counts of each sign are reported.\n  depends_on:\n  - fig6-swr-correlated-pairs\n- id: fig6c-theta-predicts-swr-correlation\n  statement: Theta-period cross-covariance of CA1-PFC pairs predicts their SWR correlation (r =\n    0.39 for all 713 pairs, and 0.39 for each of the excited and inhibited groups), equally in the\n    two groups.\n  source: Results, Structured Reactivation of CA1-PFC Pairs during SWRs, paragraph 5; Figure 6C\n  quote: This analysis revealed a significant relationship between theta cross-covariance and SWR\n    correlations (r = 0.39, n = 713 pairs ... SWR-excited neurons, r = 0.39, n = 393 pairs ...\n    SWR-inhibited neurons, r = 0.39, n = 320 pairs\n  statistics:\n  - about: all pairs, and each group\n    test: regression test\n    statistic: r = 0.39\n    p: 0.0001\n    p_relation: \"<\"\n    n: 713 pairs (393 excited, 320 inhibited)\n  - about: excited against inhibited strength\n    test: shuffle test, 1000 shuffles\n    p: 0.1\n    p_relation: \">\"\n  expected:\n  - quantity: r, all pairs\n    value: 0.39\n    tolerance: 0.039\n  - quantity: r, SWR-excited pairs\n    value: 0.39\n    tolerance: 0.039\n  - quantity: r, SWR-inhibited pairs\n    value: 0.39\n    tolerance: 0.039\n  criterion: Pearson r between the peak theta cross-covariance and the SWR correlation, with the\n    test of the regression slope. The group comparison by the shuffle of the SEP (pairs pooled\n    and split at random into groups of the same sizes, 1000 times). Reproduced when r > 0 at p <\n    0.05 in all pairs and in each group, and the groups do not differ at p < 0.05; r by the\n    pooled-value rule.\n  depends_on:\n  - fig6-swr-correlated-pairs\n- id: figs4b-ca1-leads-in-theta\n  statement: For CA1-PFC pairs with significant positive SWR correlations, the theta cross-covariance\n    peaks after zero lag, so CA1 leads PFC during behavior as during SWRs.\n  source: Figure S4B legend; Results, Structured Reactivation of CA1-PFC Pairs during SWRs,\n    paragraph 5\n  quote: Only pairs with significant and positive SWR correlations are included ... illustrating\n    that the peaks after 0 ms for both populations, indicating that CA1 leads PFC on average\n  expected:\n  - quantity: positive significant pairs, SWR-excited\n    value: 46\n    tolerance: 4.6\n  - quantity: positive significant pairs, SWR-inhibited\n    value: 26\n    tolerance: 2.6\n  criterion: The population mean standardized theta cross-covariance of these pairs. Reproduced\n    when its peak lies after 0 ms (PFC after CA1) in both groups; counts by the pooled-value rule.\n  depends_on:\n  - fig6-swr-correlated-pairs\n- id: fig6e-glm-swr-prediction\n  statement: A GLM of CA1 ensemble SWR spiking predicts SWR spiking of SWR-modulated PFC cells\n    above chance, better with larger CA1 ensembles and better than for unmodulated cells, with no\n    difference between excited and inhibited cells.\n  source: Results, Structured Reactivation of CA1-PFC Pairs during SWRs, paragraph 7; Figure 6E\n  quote: we found that that prediction performance was better than chance for SWR-modulated PFC\n    cells (n = 77) and increased with the size of the CA1 ensemble\n  statistics:\n  - about: ensemble size groups, modulated cells\n    test: one-way ANOVA, main effect of cell count group\n    p: 0.0001\n    p_relation: \"<\"\n    n: 30, 20 and 27 PFC cells\n  - about: modulated against unmodulated\n    test: two-way ANOVA\n    p: 0.0001\n    p_relation: \"<\"\n    n: 77 modulated and 102 unmodulated cells\n  - about: excited against inhibited\n    test: two-way ANOVA\n    p: 0.29\n    n: 40 excited and 37 inhibited cells\n  criterion: Poisson GLM, log link, PFC 0-200 ms SWR spike count on the CA1 cells' counts; 90/10\n    split repeated 5000 times; error is the mean absolute difference of predicted and actual\n    counts; shuffled error from predictions shuffled across SWRs; performance is the fractional\n    improvement over shuffled error (SEP, GLM; Figure S7D legend). Cells whose GLM does not\n    converge are dropped. Open, with readings - chance test as (a) a signed-rank test of the\n    cells' performance against 0, (b) per cell, real error below shuffled in more than 95% of\n    splits; ensemble size groups are shown only in the figure, so (a) tertiles of CA1 ensemble\n    size, (b) three groups of equal size width. Reproduced when performance is above chance,\n    rises with ensemble size (ANOVA p < 0.05), modulated exceeds unmodulated (two-way ANOVA p <\n    0.05) and excited and inhibited do not differ at p < 0.05, under one reading.\n  depends_on:\n  - fig3-pfc-swr-modulation-fractions\n- id: fig6e-theta-trained-glm\n  statement: GLMs trained on movement activity also predict PFC SWR spiking, better for modulated\n    than unmodulated cells and better with larger ensembles, and predict SWRs better than\n    SWR-trained models predict movement activity.\n  source: Results, Structured Reactivation of CA1-PFC Pairs during SWRs, paragraph 8; Figure 6E\n    (white bars)\n  quote: We found that theta-derived models could in many cases predict PFC SWR firing and that\n    the accuracy of this prediction also increased with the size of the CA1 ensemble\n  statistics:\n  - about: modulated against unmodulated\n    test: two-way ANOVA\n    p: 0.02\n  - about: ensemble size groups\n    test: two-way ANOVA, cell count group\n    p: 1.0e-7\n    p_relation: \"<\"\n  - about: model type by cell count interaction (theta-trained to SWR against SWR-trained to theta)\n    test: two-way ANOVA\n    p: 0.01\n    p_relation: \"<\"\n  criterion: Behavior data are run-epoch time at speed > 5 cm/s with no SWR, in 200 ms bins (SEP,\n    GLM), used to train the model; it is then applied to the SWR counts; and SWR-trained models to\n    the behavior bins. Performance and readings as in fig6e-glm-swr-prediction. Reproduced when\n    theta-trained performance is above chance, modulated exceeds unmodulated at p < 0.05, and\n    theta-to-SWR exceeds SWR-to-theta performance.\n  depends_on:\n  - fig6e-glm-swr-prediction\n- id: figs4c-pfc-predicts-ca1\n  statement: Reversing the model, SWR-modulated PFC ensembles predict CA1 SWR spiking, better than\n    unmodulated PFC ensembles and better with larger ensembles, with excited and inhibited PFC\n    cells predicting similarly.\n  source: Figure S4C legend\n  quote: As expected, predictions using PFC SWR-modulated cells (n = 102) were significantly better\n    than those using PFC SWR-unmodulated (n = 203) cells (SWR-trained model; 2-way ANOVA, p =\n    0.02\n  statistics:\n  - about: modulated against unmodulated PFC\n    test: two-way ANOVA\n    p: 0.02\n  - about: ensemble size, SWR-trained and movement-trained\n    test: one-way ANOVA\n    p: 1.0e-10\n    p_relation: \"<\"\n  - about: excited against inhibited PFC\n    test: two-way ANOVA\n    p: 0.7\n    p_relation: \">\"\n  criterion: As in fig6e-glm-swr-prediction with CA1 cells as targets and PFC ensembles of each\n    category as predictors. Reproduced when modulated ensembles predict better than unmodulated at\n    p < 0.05, performance rises with ensemble size, and excited and inhibited do not differ.\n  depends_on:\n  - fig6e-glm-swr-prediction\n- id: fig7c-spatial-correlation\n  statement: The spatial correlation of CA1-PFC pairs is related to their SWR correlation (r = 0.2\n    for excited, 0.36 for inhibited PFC cells), more strongly for SWR-inhibited cells; SWR-correlated\n    pairs have higher, and anticorrelated pairs lower and negative, spatial correlation than\n    uncorrelated pairs.\n  source: Results, Reactivation in the CA1-PFC Network Reflects Spatially Related Ensembles,\n    paragraphs 1 and 2; Figure 7C\n  quote: SWR-excited neurons, r = 0.2, n = 393 pairs, p < 10?3; SWR-inhibited neurons, r = 0.36, n\n    = 320 pairs\n  statistics:\n  - about: SWR-excited pairs\n    test: regression test\n    statistic: r = 0.2\n    p: 0.001\n    p_relation: \"<\"\n    n: 393 pairs\n  - about: SWR-inhibited pairs\n    test: regression test\n    statistic: r = 0.36\n    p: 0.0001\n    p_relation: \"<\"\n    n: 320 pairs\n  - about: correlated and anticorrelated against uncorrelated pairs\n    test: rank-sum test\n    p: 0.0001\n    p_relation: \"<\"\n  - about: inhibited stronger than excited\n    test: shuffle test, 1000 shuffles\n    p: 0.01\n    p_relation: \"<\"\n  expected:\n  - quantity: r, SWR-excited pairs\n    value: 0.2\n    tolerance: 0.02\n  - quantity: r, SWR-inhibited pairs\n    value: 0.36\n    tolerance: 0.036\n  criterion: Spatial correlation is the Pearson correlation of the two cells' linearized rate maps\n    concatenated over the 4 trajectories (SEP; concatenation is the standard reading, the mean of\n    per-trajectory correlations a variant). Group difference by the SEP shuffle (mixed\n    populations of the same sizes, 1000 times). Reproduced when both r > 0 at p < 0.05, the\n    inhibited r exceeds the excited r at p < 0.05 by the shuffle, and the correlated and\n    anticorrelated groups differ from uncorrelated as stated at p < 0.05; r by the pooled-value\n    rule.\n  depends_on:\n  - fig6-swr-correlated-pairs\n  - fig5c-spatial-coverage\n- id: figs5-matched-selectivity\n  statement: With PFC cells matched for spatial coverage, excited and inhibited groups show similar\n    spatial-SWR correlation relations (r = 0.32 and 0.39, not different).\n  source: Figure S5 legend\n  quote: Both CA1-PFC excited pairs (n = 203, r = 0.32, p < 10-4) and CA1-PFC inhibited pairs (n =\n    203, r = 0.39, p < 10-4) showed significant correlations and these correlations were not\n    significantly different from one another\n  statistics:\n  - about: matched excited pairs\n    test: regression test\n    statistic: r = 0.32\n    p: 0.0001\n    p_relation: \"<\"\n    n: 203 pairs\n  - about: matched inhibited pairs\n    test: regression test\n    statistic: r = 0.39\n    p: 0.0001\n    p_relation: \"<\"\n    n: 203 pairs\n  - about: excited against inhibited\n    test: shuffle test, 1000 shuffles\n    p: 0.18\n    p_relation: \">\"\n  criterion: Only PFC cells whose coverage lies within the interquartile range of SWR-inhibited\n    coverage, in both groups (SEP, Figure S5). The legend's n of 203 for both groups suggests a\n    subsample of equal size; readings are (a) all pairs within the range, (b) random subsamples\n    of the larger group to the size of the smaller. Reproduced when both r > 0 at p < 0.05 and\n    the shuffle finds no difference at p < 0.05.\n  depends_on:\n  - fig7c-spatial-correlation\n- id: figs6-replay-content\n  statement: The SWR spiking of SWR-modulated PFC neurons is more related to the spatial content of\n    CA1 replay than that of unmodulated neurons.\n  source: Figure S6B legend; Results, Reactivation in the CA1-PFC Network Reflects Spatially\n    Related Ensembles, paragraph 2\n  quote: Correlation between the SWR-associated spiking of the PFC neuron and the content of the\n    decoded CA1 locations was significantly higher for SWR-modulated neurons\n  statistics:\n  - test: rank-sum test\n    p: 0.01\n    p_relation: \"<\"\n    n: 17 SWR-modulated and 21 SWR-unmodulated neurons\n  criterion: Bayesian decoding of CA1 spikes in 15 ms bins during SWRs with at least 4 active CA1\n    cells, Poisson model, significance by 500 time-bin shuffles at p < 0.05; PFC cells with at\n    least 10 significant events; R per cell from the correlation of decoded spatial probability\n    and the PFC rate profile on the replayed trajectory (SEP, Replay analysis). How R is formed\n    across events (spike count against overlap, as Figure S6A orders the raster) is open;\n    readings are (a) Pearson of per-event PFC spike count with per-event overlap, (b) Spearman.\n    The replay score is not given; the line-fit score of the cited Karlsson and Frank (2009) is\n    the standard choice. Reproduced when modulated exceeds unmodulated at p < 0.05 by rank-sum\n    under one reading. The paper notes the small sample; few cells may qualify in the W-track data\n    alone.\n  depends_on:\n  - fig3-pfc-swr-modulation-fractions\n- id: fig8a-no-prerest-swr-correlation-relation\n  statement: On the W-track, SWR correlations of CA1-PFC pairs in the pre-task rest show no\n    relation to their SWR correlations during the task (excited pairs r = 0.08, p = 0.2; inhibited\n    r = 0.1, p > 0.1).\n  source: Results, Task-Related CA1-PFC Correlations Are Not Present in Preceding Rest Periods,\n    paragraph 2; Figure 8A\n  quote: Comparing the SWR response correlations between CA1-PFC pairs revealed that there was no\n    detectable relationship between awake SWR correlations and SWR correlations in pre-rest\n    periods (Figure 8A)\n  statistics:\n  - about: SWR-excited pairs\n    statistic: r = 0.08\n    p: 0.2\n    n: 219 pairs\n  - about: SWR-inhibited pairs\n    statistic: r = 0.1\n    p: 0.1\n    p_relation: \">\"\n    n: 196 pairs\n  expected:\n  - quantity: excited pairs recorded in both epochs\n    value: 219\n    tolerance: 21.9\n  - quantity: inhibited pairs recorded in both epochs\n    value: 196\n    tolerance: 19.6\n  criterion: A claim of absence. W-track only, as the paper; cells recorded in both the pre-rest\n    and the run epochs of a day, PFC categories from behavior, SWRs in pre-rest detected as in\n    behavior (SEP, Task and rest period comparisons). Test is the paper's, the regression (Pearson\n    r) test, at p < 0.05. Reproduced when neither group shows a significant relation; r is reported\n    either way. Pair counts within tolerance are reported, not required.\n  depends_on:\n  - fig6-swr-correlated-pairs\n- id: fig8bc-no-prerest-theta-spatial-relation\n  statement: Pre-rest SWR correlations bear no relation to task theta cross-covariance (r = 0.02 and\n    0.12) or to task spatial correlation (r = -0.02 and 0.05) for excited and inhibited pairs.\n  source: Results, Task-Related CA1-PFC Correlations Are Not Present in Preceding Rest Periods,\n    paragraph 2; Figure 8B and 8C\n  quote: Similarly, we saw no relationship between pre-rest SWR correlations and either\n    movement-related correlations (Figure 8B) or spatial correlations\n  statistics:\n  - about: theta cross-covariance, excited pairs\n    statistic: r = 0.02\n    p: 0.8\n    p_relation: \">\"\n    n: 219 pairs\n  - about: theta cross-covariance, inhibited pairs\n    statistic: r = 0.12\n    p: 0.1\n    p_relation: \">\"\n    n: 196 pairs\n  - about: spatial correlation, excited pairs\n    statistic: r = -0.02\n    p: 0.7\n    p_relation: \">\"\n    n: 219 pairs\n  - about: spatial correlation, inhibited pairs\n    statistic: r = 0.05\n    p: 0.5\n    p_relation: \">\"\n    n: 196 pairs\n  criterion: A claim of absence, judged on the paper's regression test at p < 0.05 for each of the\n    four relations, on the pairs of fig8a. Reproduced when none is significant; partially when some\n    are; not reproduced when all are. Every r is reported.\n  depends_on:\n  - fig8a-no-prerest-swr-correlation-relation\n  - fig6c-theta-predicts-swr-correlation\n  - fig7c-spatial-correlation\n- id: fig8d-glm-epoch-specific\n  statement: GLMs trained on task SWRs fail to predict PFC spiking in pre-rest SWRs, and cross-epoch\n    predictions are worse than within-task and within-pre-rest predictions.\n  source: Results, Task-Related CA1-PFC Correlations Are Not Present in Preceding Rest Periods,\n    paragraph 2; Figure 8D\n  quote: GLMs trained on SWR activity in the awake state (CA1 ensemble activity predicting PFC\n    spiking) were unable to predict PFC spiking in SWRs during pre-rest periods (shuffle test, n =\n    1,000, p > 0.5) and performed significantly worse than prediction of PFC spiking in SWRs during\n    behavior\n  statistics:\n  - about: task to pre-rest against chance\n    test: shuffle test, 1000 shuffles\n    p: 0.5\n    p_relation: \">\"\n  - about: task to pre-rest against task to task, SWR-trained\n    test: rank-sum test\n    p: 1.0e-6\n    p_relation: \"<\"\n    n: 38 and 24 cells\n  - about: pre-rest to task against task to task, SWR-trained\n    test: rank-sum test\n    p: 1.0e-6\n    p_relation: \"<\"\n    n: 38 and 22 cells\n  - about: pre-rest to pre-rest against each cross-epoch prediction, SWR-trained\n    test: rank-sum test\n    p: 0.01\n    p_relation: \"<\"\n    n: 39 against 24 and 22 cells\n  expected:\n  - quantity: cells, task to task\n    value: 38\n    tolerance: 3.8\n  - quantity: cells, task to pre-rest\n    value: 24\n    tolerance: 2.4\n  - quantity: cells, pre-rest to task\n    value: 22\n    tolerance: 2.2\n  - quantity: cells, pre-rest to pre-rest\n    value: 39\n    tolerance: 3.9\n  criterion: W-track only. GLMs as in fig6e-glm-swr-prediction; cross-epoch prediction only when\n    all CA1 cells of the model are present in both epochs (Figure S7D legend). The task-to-pre-rest\n    chance test is a 1000-shuffle test of predictions across SWRs. Reproduced when task-to-pre-rest\n    is not above chance at p < 0.05, both cross-epoch predictions are below task-to-task at p <\n    0.05 by rank-sum, and pre-rest-to-pre-rest exceeds both cross-epoch predictions at p < 0.05.\n    Cell counts are reported against expected.\n  depends_on:\n  - fig6e-glm-swr-prediction\n- id: figs7-both-tracks\n  statement: Combining both tracks, pre-rest SWR correlations also show no relation to task SWR,\n    theta or spatial correlations, and cross-epoch GLMs fail to predict above chance.\n  source: Figure S7 legend\n  quote: Task to pre-rest; model trained during behavior predicting SWR-associated spiking during\n    pre-rest periods\n  inferred: false\n  criterion: Needs the Y-track animals, which the data set does not hold by its description;\n    recorded for coverage and expected to be untestable.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd claims/crcns-hc-28 && f=10.1016-j.neuron.2016.02.010.yaml && python - <<'EOF'
f='10.1016-j.neuron.2016.02.010.yaml'
s=open(f).read()
rep=[
("  inferred: false\n",""),
("""    to baseline values within
""","""    to baseline values within ... 300 ms of SWR onset
"""),
("""  quote: SWR-excited neurons, r = 0.2, n = 393 pairs, p < 10?3; SWR-inhibited neurons, r = 0.36, n
    = 320 pairs
""","""  quote: We found that the similarity between the spatial response profiles of the CA1 and PFC
    neurons, quantified as a spatial correlation, was related to their SWR correlation for both
    SWR-inhibited and SWR-excited neurons
"""),
("""SWR-inhibited and the SWR-unmodulated neurons (Figure 5C; coverages were as follows; excited,
    0.70 ± 0.05; inhibited, 0.54 ± 0.05; unmodulated, 0.50 ± 0.02""","""SWR-inhibited and the SWR-unmodulated neurons ... excited, 0.70 ± 0.05; inhibited, 0.54 ±
    0.05; unmodulated, 0.50 ± 0.02"""),
("""than those using PFC SWR-unmodulated (n = 203) cells (SWR-trained model; 2-way ANOVA, p =
    0.02""","""than those using PFC SWR-unmodulated (n = 203) cells ... 2-way ANOVA, p = 0.02"""),
("""  quote: Task to pre-rest; model trained during behavior predicting SWR-associated spiking during
    pre-rest periods""","""  quote: Task Related CA1-PFC Correlations are not Present in Preceding Rest Periods for Data
    Combined for Both Tracks"""),
("""    value: -15
    tolerance: 1.5""","""    value: -15
    tolerance: 10"""),
]
for a,b in rep:
    assert s.count(a)>=1,a
    s=s.replace(a,b)
open(f,'w').write(s)
EOF
grep -n " — \|rather" $f; python -c "import yaml;yaml.safe_load(open('$f'))" && cd ../.. && python tools/claims_check.py claims/crcns-hc-28/$f paper/10.1016-j.neuron.2016.02.010.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd claims/crcns-hc-28 && grep -n ": .*: \|^    .*: " 10.1016-j.neuron.2016.02.010.yaml | grep -v "^\S*:\s*#" | grep -v "^[0-9]*:#" | head -20
```

```
114:    value: 0.8
115:    unit: fraction
145:    value: 446
146:    tolerance: 44.6
148:    value: 69
149:    tolerance: 6.9
151:    value: 172
152:    tolerance: 17.2
154:    value: 165
155:    tolerance: 16.5
169:    value: 381
170:    tolerance: 38.1
172:    value: 96.7
173:    tolerance: 9.67
174:    unit: ms
176:    value: 0.12
177:    tolerance: 0.012
178:    unit: Hz
194:    test: rank-sum test
195:    p: 0.03
```

**Agent calls Read**

```json
{
 "file_path": "claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml",
 "offset": 404,
 "limit": 8
}
```

```
404	  source: Results, SWR Modulation Is Related to Theta Phase Locking of PFC Neurons, paragraph 2;
405	    Table S3
406	  quote: This included 44/57 SWR-excited neurons (77%) and 37/52 inhibited neurons (71%). There
407	    was no difference in the fraction of phase-locked cells in the excited and inhibited neuron
408	    populations (p > 0.4), but both had a higher fraction of phase-locked cells than was seen for
409	    SWR-unmodulated neurons (108/203 neurons: 53%
410	  statistics:
411	  - about: excited against inhibited
```

**Agent calls Bash**

```bash
cd  && f=claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml && sed -i 's/    SWR-unmodulated neurons (108\/203 neurons: 53%$/    SWR-unmodulated neurons (108\/203 neurons/' $f && python -c "import yaml;yaml.safe_load(open('$f'))" && python tools/claims_check.py $f paper/10.1016-j.neuron.2016.02.010.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  && f=claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml && python - <<'EOF'
f='claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml'
s=open(f).read()
a="""related to their SWR correlation for both
    SWR-inhibited and SWR-excited neurons
"""
b="""related to their SWR correlation for both ...
    SWR-inhibited and SWR-excited neurons
"""
assert a in s; s=s.replace(a,b); open(f,'w').write(s)
EOF
python tools/claims_check.py $f paper/10.1016-j.neuron.2016.02.010.txt; grep -c "rather\|—" $f; sed -n 305,308p paper/*neuron*.txt; sed -n 337p paper/*neuron*.txt; sed -n 557p paper/*neuron*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
git status --short; grep -c "^  criterion:" claims/crcns-hc-28/*.yaml; grep -c "^  statistics:" claims/crcns-hc-28/*.yaml
```

```
?? .bash_profile
?? .bashrc
?? .gitconfig
?? .idea
?? .mcp.json
?? .profile
?? .ripgreprc
?? .vscode
?? .zprofile
?? .zshrc
?? claims/crcns-hc-28/
?? scripts
39
25
```

**Agent**

I wrote the claims file at `claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml`. The quote checker passes except for 3 p-values, which are printed correctly in the paper but garbled in the extracted text.

**What I read.** The version of record with its full Supplemental Information, as text extracted from the journal PDF under `paper/`: Results, Discussion, Experimental Procedures, the legends of Figures 1 to 8 and S1 to S7, Tables S1 to S3, and the Supplemental Experimental Procedures. The paper links no code; it only says the analysis used custom Matlab routines. I could not render the PDF (no renderer is installed), so no value was read from a figure, and values shown only in figures are not recorded. The main one is the ensemble-size groups of Figure 6E.

**Counts.** 39 claims, all 39 with quotes, 25 with statistics (61 statistical values in all), and 39 with criteria. The 3 values the checker could not find are p < 10^-11, p < 10^-7 and p < 10^-7. The extracted text prints their minus signs as a replacement character; I confirmed each by reading it in context.

**Scope of the dataset.** By its description, hc-28 holds only the three W-track rats (HPa, HPb, HPc). Most results pool these with three Y-track rats that are not in the dataset. The opening comment fixes a rule for those claims: the direction and test must hold on the W-track data, and a pooled value outside its tolerance makes the claim partial. Where the paper gives W-track numbers (Tables S1 and S2, Figure S2, Figure 8), those are the expected values. Two claims need the Y-track rats and are recorded as untestable: Y-track learning and the both-tracks results of Figure S7. The dataset also holds later novel/familiar sessions used by a 2017 paper; the author is to keep only the 8 learning days.

**Details the paper leaves open, with the readings named:**
- **SWR detection:** the paper defers to Karlsson and Frank (2009), which is not under `paper/` and was not read. Readings are a threshold crossing on any one CA1 tetrode, or on the power averaged over tetrodes. Minimum duration and the definition of onset are not given.
- **Unit of analysis:** a cell on one day (the reading the paper supports best) or a unique unit across days. The span of the SWR-aligned raster is ±500 ms or ±1 s. PSTH bin and jitter range are given standard choices.
- **Peak and trough search window:** 0 to 200 ms or 0 to 500 ms. For onset, the mean and SD come from the baseline or from the whole PSTH. Return to baseline for the transient-response claim: within 1 SD of baseline, or within the 95% interval of the baseline bins.
- **Theta cross-covariance normalization:** a Poisson z-score, or division by the expected count. "Maximum zero lag" (Figure 5G) is the peak within ±200 ms or the value at zero lag. Same-tetrode pairs are shown both included and excluded.
- **SWR correlation:** Pearson over all SWRs, or over the SWRs where both cells spiked; Spearman is a variant.
- **"SWR modulation index" (Figure 4C):** the measure divided by the mean shuffled measure, a z-score against the shuffles, or the raw measure.
- **Theta phase:** convention and polarity of the reference tetrode. Theta lag: best mean kappa, or the median of each cell's best shift; shift range and step are a standard choice.
- **Mean rate "during movement":** speed above 5 cm/s with no SWR, speed above 4 cm/s, or the whole run epoch.
- **Rate-speed correlation:** over time bins (200 ms and 1 s) or over speed bins, plus the form of the shuffle for the median.
- **Spatial maps:** bin size, smoothing and speed filter are standard choices. Arm and direction indices use mean or peak rate. Matched subsample in Figure S5: all pairs in range, or subsampled to equal size.
- **Reward well and reward time:** zone radius 10, 15 or 20 cm. Reward time is arrival in the zone, or the first drop below 4 cm/s. W-track scoring and "chance": 50% correct, or a binomial test.
- **GLM:** the test of above-chance performance (signed-rank across cells, or per cell over the splits). Ensemble-size groups: tertiles or equal-width bins, since they are shown only in the figure.
- **Replay analysis:** how R is formed (Pearson or Spearman over events), and which replay score is used.

**Missing from the paper.**
- **"Data not shown":** the theta-lag result (about 15 ms) has no data or method beyond shifting the time of theta.
- **Pooled results:** most numbers have no W-track-only values.
- **Inconsistencies:**
  - The text calls the SWR-excited phase distribution narrower than both other groups, but reports p > 0.1 against SWR-inhibited. The statement follows the tests.
  - Figure 5F gives p < 0.001 in the text and p < 0.01 in the legend. The criterion uses p < 0.01.

## End of run

26 turns, 6 minutes, $2.22 at API prices, result: success.
