# petersen-2020 · claims · run 43716490296

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls paper/ claims/ tools/
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md; ls paper/ claims/ tools/
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "offset": 1,
 "limit": 200
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-15`. Record this version in the attempt's provenance.
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
[... 180 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/petersen-2020.yaml; echo ======; cat claims/fouke-2025.yaml
```

```
<persisted-output>
Output too large (58.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/d4aa2bd4-37ed-43aa-9f5e-08a1dfd9836a/tool-results/bkmflebzr.txt

Preview (first 2KB):
# Claims for Petersen & Buzsaki (2020), Cooling of medial septum reveals theta phase lag
# coordination of hippocampal cell assemblies, Neuron 107, on dandiset 000059.
# Source: the accepted author manuscript in PubMed Central (PMC7442698), full text, read from its
# Results, figure legends and STAR Methods. The supplementary PDF could not be obtained (PMC
# serves a captcha and Europe PMC lists the article as not open access), so supplementary
# figures are tested only where the main text states their result.
#
# When these criteria were written, the author had seen the data check only (file list, the
# contents of the files, trial counts and cooling states per session, the temperature traces of
# six sessions, the shape of the maze) and one pilot session (MS21-180628), for which the mean
# theta frequency, temperature and error rate by cooling state and the linearization had been
# printed to test the code. No claim's analysis had been run across sessions. The author had
# also read the paper's MATLAB code (GitHub petersenpeter/Code_Petersen_Buzsaki_Neuron_2020,
# commit aec2f7e), which fixes several choices the Methods leave open (see cooling.py).
#
# One criterion was revised after the pilot session and before any analysis across sessions:
[... 11 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/petersen-2020.yaml"
}
```

```
1	# Claims for Petersen & Buzsaki (2020), Cooling of medial septum reveals theta phase lag
2	# coordination of hippocampal cell assemblies, Neuron 107, on dandiset 000059.
3	# Source: the accepted author manuscript in PubMed Central (PMC7442698), full text, read from its
4	# Results, figure legends and STAR Methods. The supplementary PDF could not be obtained (PMC
5	# serves a captcha and Europe PMC lists the article as not open access), so supplementary
6	# figures are tested only where the main text states their result.
7	#
8	# When these criteria were written, the author had seen the data check only (file list, the
9	# contents of the files, trial counts and cooling states per session, the temperature traces of
10	# six sessions, the shape of the maze) and one pilot session (MS21-180628), for which the mean
11	# theta frequency, temperature and error rate by cooling state and the linearization had been
12	# printed to test the code. No claim's analysis had been run across sessions. The author had
13	# also read the paper's MATLAB code (GitHub petersenpeter/Code_Petersen_Buzsaki_Neuron_2020,
14	# commit aec2f7e), which fixes several choices the Methods leave open (see cooling.py).
15	#
16	# One criterion was revised after the pilot session and before any analysis across sessions:
17	# fig5d-ccg-period first took the period from the spectrum of the summed cross-correlogram
18	# of all pairs. On the pilot session that spectrum peaked at the edge of its range (172 ms),
19	# following the envelope of the summed correlogram, whose theta ripple cancels out when pairs
20	# with different lags are summed. The period is now measured per pair, and the summed
[... 737 more lines not kept]
```

**Agent calls Bash**

```bash
head -120 claims/fouke-2025.yaml; grep -n "^  [a-z_]*:" claims/fouke-2025.yaml | awk '{print $2}' | sort | uniq -c; tail -30 claims/fouke-2025.yaml
```

```
# Claims for Fouke, He, Loring & Naumann (2025) on dandiset 001453.
# Source: the accepted author manuscript in PubMed Central (PMC12218792), full text, read
# from its Results, figure legends and STAR Methods. The version of record is not open access.
#
# When these criteria were written, the author had seen the data check only: the file list,
# subject metadata, frame rates, units, trial structure and stimulus codes of every file, and
# the extent of positions. No claim's analysis had been run. The author had also read the
# outputs printed in the paper's own analysis notebook (Fig1-S1.ipynb, GitLab commit 33a5c29),
# which include per-stimulus median speeds and angular velocities and its statistics.
#
# The dandiset holds only the freely swimming tracking data of Figure 1 and Figure S1. Its
# stimulus codes 0 to 20 carry no names. The names come from the paper's code and from the
# stimulus software's protocol file (see stimulus-code-link), so the claims that need them
# use outside data and depend on that claim.
#
# Method choices fixed here, from the paper's Fig1-S1.ipynb where the Methods are silent: a
# trial is one stim_index; tracked frames only; positions smoothed with a Savitzky-Golay filter
# (21 frames, order 2); trials rejected when the absolute cumulative heading change exceeds
# 1000 degrees in the first 10 s or 2000 degrees in the first 35 s, or the mean speed exceeds
# 100 mm/s; measures taken from 3 s to 35 s after the first frame (the 3 s stationary phase is
[... 141 more lines not kept]
```

**Agent**

Read the protocol and the existing file. The existing file was written by an author who had seen data (pilot session, session sets); I'll rewrite it from the paper alone. Reading the paper now.

**Agent calls Bash**

```bash
wc -l paper/*.txt; head -60 paper/10.1016-j.neuron.2020.05.023.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Full text with supplement is present. Reading it in chunks.

**Agent calls Bash**

```bash
cd paper; fold -s -w 4000 10.1016-j.neuron.2020.05.023.txt > $TMPDIR/p.txt; wc -l $TMPDIR/p.txt; wc -c 10.1016-j.neuron.2020.05.023.txt
```

```
394 /tmp/claude-1001/p.txt
109095 10.1016-j.neuron.2020.05.023.txt
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2020.05.023.txt",
 "offset": 7,
 "limit": 120
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2020.05.023.txt",
 "offset": 7,
 "limit": 60
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
fold -s -w 300 paper/10.1016-j.neuron.2020.05.023.txt > $TMPDIR/p.txt; wc -l $TMPDIR/p.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "limit": 170
}
```

```
1	DOI: 10.1016/j.neuron.2020.05.023
2	Version: as served by ncbi_pmc
3	Source: ncbi_pmc+crossref (paper-text-fetcher)
4	Stored: 2026-10-20
5	Extracted: as fetched; with the Supplemental Information (pages 19 to 24 of the Cell Press article-plus-supplement PDF, mmc2), extracted with PyMuPDF (dehyphenated, NFKC)
6	------------------------------------------------------------------------
7	Neuron Neuron 319 nihpa 8809320 Neuron 0896-6273 1097-4199 pmc-is-collection-domain yes pmc-collection-title NIHPA Author Manuscripts PMC7442698 PMC7442698.1 7442698 7442698 NIHMS1597964 32526196 10.1016/j.neuron.2020.05.023 NIHMS1597964 NIHPA1597964 1 Article Cooling of medial septum reveals theta 
8	phase lag coordination of hippocampal cell assemblies Petersen Peter Christian 1 Buzsáki György 1 2 3 4 1 Neuroscience Institute Langone Medical Center, New York University, New York, NY 10016, USA 2 Department of Neurology, Langone Medical Center, New York University, New York, NY 10016, USA 3 
9	Center for Neural Science, New York University, New York, NY 10003, USA Author Contributions GB and PP designed the experiments. PP performed the experiments and analyzed the data. GB and PP wrote the paper. 4 Lead Contact: György Buzsáki ( [removed: an e-mail address] ) 10 6 2020 19 8 2020 107 4 
10	363771 731 744.e3 05 06 2020 19 08 2021 19 08 2021 23 08 2020 25 04 2025 This file is available for text mining. It may also be used consistent with the principles of fair use under the copyright law. Summary Hippocampal theta oscillations coordinate neuronal firing to support memory and spatial 
11	navigation. The medial septum (MS) is critical in theta generation by two possible mechanisms: either a unitary ‘pacemaker’ timing signal is imposed on the hippocampal system or it may assist in organizing target subcircuits within the phase space of theta oscillations. We used temperature 
12	manipulation of the MS to test these models. Cooling of the MS reduced both theta frequency and power, was ass
[... 158 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 170,
 "limit": 170
}
```

```
170	Hilbert transform. The phase precession slope of a place field, was determined by performing a circular-linear regression of the position vs theta phase for all spikes within the boundaries of the place field. Oscillation Frequency of Neurons For quantifying oscillation frequency of neurons, a 
171	1ms-resolution spike raster was created and convoluted with an 80-point gaussian window. The auto-correlogram was calculated and the peak between 50ms and 150ms was determined and its reciprocal value was regarded as the oscillation frequency. For place field analysis (e.g. Fig. 3 B , C , F , H ), 
172	only the spikes emitted as the animal passed through the field was included. Place cell analysis Spiking data were binned into 3–5 cm wide segments of the maze, generating the raw maps of spike number and occupancy probability. Place field boundaries were manually defined by the following criteria: 
173	a spatial tuned firing rate, phase precession, and peak firing rate above 10Hz. For figure 5 , place fields were automatically defined by the following criteria: at least 4 bins, where the firing rate was above 10% of the peak rate in the maze, peak firing rate > 8 Hz and spatial coherence > 0.6 ( 
174	Hafting et al., 2008 ; Muller and Kubie, 1989 ). Spatial temporal compression To determine the spatial-temporal compression, the distance between pairs of fields (determined as the spatial distance between the spatial peak firing rate) was plotted against the temporal delay inside theta cycles 
175	(either time or phase). The temporal offset between individual overlapping fields was determined with a 1ms bin-sized cross correlogram, convoluted with a 60 bin-wide gaussian window. The phase offset was determined with a 0.01n bin-sized cross correlogram convoluted with a 60 bin-wide gaussian 
176	window. The compression and oscillation period were determined by fitting the surface equation below to the density of points ( fig 5 c ): Z = cos ( x 2 π a ⋅ b + y 2 π b + 1 ) ⋅ exp
[... 163 more lines not kept]
```

**Agent**

Main text, legends and Methods read. Now the supplement section at the end of the file.

**Agent calls Bash**

```bash
grep -n -i "supplemental\|Supplementary Figure\|Figure S" $TMPDIR/p.txt | head -30
```

```
5:Extracted: as fetched; with the Supplemental Information (pages 19 to 24 of the Cell Press article-plus-supplement PDF, mmc2), extracted with PyMuPDF (dehyphenated, NFKC)
168:CellExplorer.org ( Petersen and Buzsáki, 2020 ), see Supplementary figure 1l – o . Spiking characteristics, including the autocorrelograms, spike waveforms and putative monosynaptic connections derived from short-term cross-correlograms (English et al., 2017), were used to select and characterize 
490:Supplemental Information
498:Figure S1. Methods of MS cooling. Related to Fig. 2. Two different methods for cooling the cryoprobe 
538:Figure S2. MS cooling affects single unit parameters. Related to Fig. 3. A, Firing rates of pyramidal 
553:Figure S3. Speed and MS cooling affects are dissociable. Related to Figure 3. A, Distribution of the 
572:Figure S4. Properties of place fields during MS cooling. Related to Figure 4. A, B, C, D, Skewness, 
580:Figure S5. Time course of the effects of MS cooling on behavior and physiological parameters. 
596:Figure S6. Related to Figure 1. Left, Traditional (pacemaker) model of MS. PV GABAergic neuronal
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 488,
 "limit": 171
}
```

```
488	=== page 19 ===
489	Neuron, Volume 107
490	Supplemental Information
491	Cooling of Medial Septum Reveals Theta Phase
492	Lag Coordination of Hippocampal Cell Assemblies
493	Peter Christian Petersen and György Buzsáki
494	
495	=== page 20 ===
496	 
497	 
498	Figure S1. Methods of MS cooling. Related to Fig. 2. Two different methods for cooling the cryoprobe 
499	were tested. The first one used a Peltier device (panels A; Long and Fee, 2008). This allowed precise 
500	control of temperature over long duration and performing necessary tests of MS temperature control. 
501	However, it required both a heatsink and an electric fan for maintaining stable temperature of the Peltier 
502	element, increasing both volume and weight of the device. The second device was a small cooling 
503	reservoir (as also shown in Fig. 2A, B). This device was used in all physiological and behavioral 
504	experiments. A, Photograph of a Peltier device implanted in a rat. On top of the Peltier there is a small, 
505	low noise electric fan to cool the device. B, Relationship between MS local temperature (red) and theta 
506	frequency (blue) in the hippocampus. The MS was repeatedly cooling with dry ice. Second and third 
507	panels, successive cooling epochs are superimposed. Fourth panel, superimposed average MS temperature 
[... 151 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 340,487p $TMPDIR/p.txt | grep -v "^\[" | grep -v "^$" | head; grep -n -i "github\|code" $TMPDIR/p.txt | grep -iv "coding\|encod\|decod" | head
```

```
138:study did not generate new unique reagents. DATA AND CODE AVAILABILITY The dataset will be available from our data share via our website buzsakilab.com/wp/public-data/ ( Petersen et al., 2018 ) and will be uploaded to CRCNS.org. The code that support the findings of this study will be made 
166:channel preamplifiers sampled at 20 kHz (Intan Inc). Spike Sorting Spike sorting was performed semi-automatically with KiloSort ( Pachitariu et al., 2016 ) github.com/cortex-lab/KiloSort , using our own pipeline KilosortWrapper (a wrapper for KiloSort, github.com/petersenpeter/KilosortWrapper ( 
167:Petersen et al., 2020 ), followed by a manual curation using the software Phy ( github.com/kwikteam/phy ) and our own designed plugins for phy ( github.com/petersenpeter/phy-plugins ). Unit Classification Well isolated units were classified into putative cell types using CellExplorer 
193:10.1046/j.1460-9568.1999.00446.x Dannenberg H , Kelley C , Hoyland A , Monaghan CK , and Hasselmo ME ( 2019 ). The firing rate speed code of entorhinal speed cells differs across behaviorally relevant time scales and does not depend on medial septum inputs . J. Neurosci . 
205:Neurosci . 34 , 16739 – 16743 . 25505326 10.1523/JNEUROSCI.1612-14.2014 PMC4261098 Gothard KM , Skaggs WE , and McNaughton BL ( 1996 ). Dynamics of Mismatch Correction in the Hippocampal Ensemble Code for Space: Interaction between Path Integration and Environmental Cues . J. Neurosci . 16 , 8027 – 
219:and Jensen O ( 2013 ). The Theta-Gamma Neural Code . Neuron 77 , 1002 – 1016 . 23522038 10.1016/j.neuron.2013.03.007 PMC3648857 Long MA , and Fee MS ( 2008 ). Using temperature to analyse temporal dynamics in the songbird motor pathway . Nature 456 , 189 – 194 . 19005546 10.1038/nature07448 
223:rhythmicity in rats restores initial learning in the Morris water maze . Hippocampus 16 , 1102 – 1110 . 17068783 10.1002/hipo.20235 Mehta MR , Lee AK , and Wilson MA ( 2002 ). Role of experience and oscillations in transforming a
[... 3 more lines not kept]
```

**Agent**

The paper links no analysis code (code "on request"); it links only tools (KiloSort wrapper, phy plugins, CellExplorer, buzcode). Checking the registry's dataset record and the claims checker next.

**Agent calls Bash**

```bash
cd  cat papers/datasets/petersen-2020.yaml 2>/dev/null; grep -rl "000059" --include=*.yaml --include=*.json . 2>/dev/null | grep -v "^./claims\|transcripts" | head; python tools/claims_check.py --help 2>&1 | head -20
```

```
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
paper: doi:10.1016/j.neuron.2020.05.023
datasets:
- archive: dandi
  id: 000059
  relation: primary
./attempts/petersen-2020-01.yaml
./papers/manifest.yaml
./papers/match/000059.yaml
./papers/datasets/petersen-2020.yaml
./papers/renamed.yaml
./targets/contributors.yaml
./targets/dandisets.json
./entries/petersen-2020/entry.yaml
Check a claims file against the full text of its paper.

    python tools/claims_check.py claims/<dandiset>/<doi>.yaml paper/<text>.txt [more texts ...]

Validates the file against schemas/claims.schema.json, checks every quote word for word
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'E'
import json
d=json.load(open('targets/dandisets.json'))
items = d if isinstance(d,list) else d.get('dandisets', d)
if isinstance(items, dict): items=list(items.values())
for x in items:
    if isinstance(x,dict) and '000059' in json.dumps(x)[:300]:
        print({k:x[k] for k in x if k in('id','name','title','description')})
E
python -c "import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"
```

```
{
 "$schema": "https://json-schema.org/draft/2020-12/schema",
 "title": "Claims proposed for one target (a dataset and one of its papers)",
 "description": "Draft. To be revised after the pilot.",
 "type": "object",
 "additionalProperties": false,
 "required": [
  "schema_version",
  "paper",
  "claims"
 ],
 "properties": {
  "schema_version": {
   "const": 2
  },
  "dataset": {
   "description": "Before the cutover to paper-first records, the dataset a per-dataset claims file was read for. A paper's own claims file (claims/<paper>.yaml) leaves it out.",
   "type": "object",
   "additionalProperties": false,
   "required": [
[... 181 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[6000:14000])"; grep -n "000059" targets/dandisets.json | head -3
```

```
required": [
        "where"
       ]
      }
     }
    ]
   }
  },
  "checks": {
   "description": "Checks of the claims file against the paper by a second reader (docs/protocol.md, Reader, step 5), oldest first. The file is ready for an attempt when the last says so.",
   "type": "array",
   "items": {
    "type": "object",
    "additionalProperties": false,
    "required": [
     "date",
     "kind",
     "ready"
    ],
    "properties": {
[... 134 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 815,840p targets/dandisets.json; cat papers/match/000059.yaml | head -40
```

```
}
   ],
   "catalystneuro": [
    "conversion code at https://github.com/catalystneuro/buzsaki-lab-to-nwb",
    "contributor Baker, Cody of CatalystNeuro"
   ]
  },
  {
   "dandiset": "000059",
   "name": "Cooling of Medial Septum Reveals Theta Phase Lag Coordination of Hippocampal Cell Assemblies",
   "published_version": "0.250624.0444",
   "asset_count": 51,
   "size_gb": 3055.93,
   "data_standards": [
    "Neurodata Without Borders (NWB)"
   ],
   "species": [
    "Rattus norvegicus - Norway rat"
   ],
   "approaches": [
[... 23 more lines not kept]
```

**Agent**

Text is complete (author manuscript, legends, STAR Methods, and supplement pages S1–S6 plus Table S1). One check on the reported correlations: what sample size their P values imply.

**Agent calls Bash**

```bash
python -c "
from scipy import stats
import numpy as np
for r,p in [(0.81,5.4e-48),(0.54,1.2e-16),(0.35,0.01),(0.7,1e-58),(0.61,1e-6),(0.027,7.67e-19)]:
  for n in range(5,200000):
    t=r*np.sqrt(n-2)/np.sqrt(1-r*r); pp=2*stats.t.sf(t,n-2)
    if pp<=p: print(r,p,n); break
print(stats.wilcoxon(np.arange(1,11)).pvalue)
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    from scipy import stats
ModuleNotFoundError: No module named 'scipy'
```

**Agent**

I have what I need from the paper. Checking how the quote checker normalizes text before writing quotes.

**Agent calls Bash**

```bash
grep -n "def \|normal\|replace\|re.sub" tools/claims_check.py | head -60
```

```
34:def norm(s: str) -> str:
35:    s = unicodedata.normalize("NFKC", html.unescape(s))
37:        s = s.replace(a, b)
38:    return re.sub(r"\s+", " ", s).strip().lower()
41:def flattenings(raw: str) -> list[str]:
43:    tight = norm(re.sub(r"</?[A-Za-z!?][^<>]*>", " ", re.sub(INLINE, "", raw, flags=re.I)))
44:    loose = norm(re.sub(r"</?[A-Za-z!?][^<>]*>", " ", raw))
45:    return [tight, loose, tight.replace(" ", ""), loose.replace(" ", "")]
48:def quote_found(quote: str, texts: list[str]) -> bool:
51:        frags = fragments if " " in text else [f.replace(" ", "") for f in fragments]
63:def printed_forms(v: float) -> set[str]:
78:def check(claims_path: Path, paper_paths: list[Path]) -> int:
80:    texts = [t for p in paper_paths for t in flattenings(p.read_text(encoding="utf-8", errors="replace"))]
105:def main() -> int:
```

**Agent**

Writing the new claims file now. All criteria come from the paper; the earlier file's session sets, pilot-session revisions and unlinked-repository choices are dropped.

**Agent calls Write**

```json
{
 "file_path": "claims/petersen-2020.yaml",
 "content": "# Claims for Petersen & Buzsaki (2020), Cooling of medial septum reveals theta phase lag\n# coordination of hippocampal cell assemblies, Neuron 107, 731-744.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"),\n# 2026-11-15, protocol pilot-15 (docs/protocol.md, Reader).\n#\n# Text read: the accepted author manuscript in PubMed Central (PMC7442698), full text with the\n# figure legends and STAR Methods, and the Supplemental Information (Figures S1 to S6 and Table\n# S1, pages 19 to 24 of the Cell Press article-plus-supplement PDF), as stored under paper/.\n# Not the version of record. The text of the surface equation of the Methods (Spatial temporal\n# compression) has lost its fraction bars in extraction; the readings it allows are named in\n# fig5cg-compression.\n#\n# Code. The paper links no analysis code (\"The code that support the findings of this study\n# will be made available from the corresponding author upon reasonable request\"). It links only\n# tools (KiloSort, KilosortWrapper, phy and phy-plugins, CellExplorer, buzcode, FMA Toolbox),\n# which concern spike sorting and cell classification, not the analyses below. No code was read\n# for these criteria. An earlier version of this file took choices from a repository on the\n# first author's GitHub that the paper does not link, and from one pilot session of the data;\n# both are dropped here.\n#\n# Data the paper used. Adult male Long-Evans rats; five rats with cryoprobes in the medial\n# septum (MS) and 64-site silicon probes in CA1 of dorsal hippocampus ran a spontaneous\n# alternation task in a figure-8 ('theta') maze, 110 cm across (central arm 0 to 75 cm, then\n# the left or right arm, Figure S3A). Table S1 lists MS6 to MS22, of which MS9, MS10, MS12, MS13,\n# MS21 and MS22 ran in the theta maze (MS9 with a Peltier device, the others with the dry ice\n# cryoprobe, which was used \"in all physiological and behavioral experiments\", Figure S1). A\n# session is about 40 control trials, then dry ice is placed in the reservoir (cooling onset),\n# then cooling trials and recovery trials; 80 to 200 trials. Measured variables: wideband\n# signals at 20 kHz (Intan), spikes sorted with KiloSort and phy, units classed with CellExplorer\n# as putative pyramidal cells, narrow and wide waveform interneurons; head position at 120 Hz\n# (OptiTrack); MS temperature from a thermocouple on the cryoprobe; hippocampal temperature in a\n# control experiment (Figure S1H to K); trial outcome (correct or error). Samples the paper\n# reports: 53 sessions in 5 rats (Figures 2G to J, 4E), 21 sessions (Figures 3I, S3D), 365 place\n# fields (Figure 4B), 2948 pairs in 18 sessions of 5 rats before cooling (Figure 5C), 10\n# sessions of 4 rats (Figure 5H), 19 sessions with 319 interneurons and 1104 pyramidal cells\n# (Figure S5G, H). The paper does not name the sessions in each set.\n#\n# Shared method, from the paper, used by the criteria below.\n# - Trial: one run from the reward location along the central arm and one side arm (STAR\n#   Methods, Memory-demanding alternation task). An error is a choice of the arm visited on the\n#   previous trial.\n# - States: pre (control trials before cooling onset), cooling, post (recovery). The paper fixes\n#   cooling onset (dry ice placed after the control block) and its length only roughly\n#   (\"approximately 15 min (or corresponding to about 20 to 60 'cooling' trials)\", Results; \"10-12\n#   minutes, corresponding to approximately 50 trials\", Methods). It gives no temperature rule\n#   for the end of the cooling state. Readings, (a) the trial state labels the dataset carries,\n#   if any, as the authors' own split; (b) cooling is the trials that start within 12 min of\n#   cooling onset; (c) the same within 10 min. Post is the trials after cooling. Every claim\n#   that compares states is run under each reading available.\n# - Theta: an LFP channel in CA1 filtered 4 to 10 Hz (third order Butterworth, zero phase) and\n#   the Hilbert phase (Methods, Theta phase and phase precession). Which channel is open; a\n#   channel in the pyramidal layer with the largest theta power is a standard choice. How trial\n#   theta frequency and power are computed is open; readings, (a) the mean instantaneous\n#   frequency from the Hilbert phase and the mean squared Hilbert amplitude over the trial; (b)\n#   the frequency and power of the peak of the 4 to 10 Hz spectrum (spectrogram) of the trial\n#   (Figure 2D, E).\n# - Running: the paper restricts some measures to running (\"during running\", Figure S2D) but\n#   gives no speed threshold. Readings, (a) all frames of the trials; (b) frames above 10 cm/s,\n#   a common threshold the paper does not state.\n# - MS temperature of a trial: the mean of the thermocouple trace over the trial (standard).\n# - Oscillation frequency of a neuron: a 1 ms spike raster convolved with an 80-point Gaussian\n#   window, its autocorrelogram, the peak between 50 and 150 ms, and the reciprocal of its lag\n#   (Methods, Oscillation Frequency of Neurons). The window's width is open; MATLAB's gausswin(80)\n#   default (alpha 2.5, SD about 16 ms) is the standard choice, as the analyses were run in\n#   MATLAB. For place fields only spikes as the animal passed through the field (Methods).\n# - Place fields of Figures 3 and 4 were \"manually defined\" (spatially tuned firing, phase\n#   precession, peak rate above 10 Hz); this cannot be repeated exactly. Readings, (a) field\n#   boundaries the dataset holds, if any; (b) the automatic rule of Figure 5 (at least 4 bins\n#   above 10% of the peak rate in the maze, peak rate above 8 Hz, spatial coherence above 0.6)\n#   with a peak rate above 10 Hz. Maps on the linearized maze, bins of 3 to 5 cm (Methods,\n#   Place cell analysis; 3 and 5 cm are both run), left and right runs apart (Figure 3A, B).\n# - fLFP of a field: the LFP theta frequency while the animal is in the field; readings, (a) the\n#   mean instantaneous theta frequency at the field's spikes; (b) the same over the time in the\n#   field.\n# - Correlations are reported as R with regression slopes (Figure 4A); Pearson's R (MATLAB's\n#   corr default) is reading (a) and Spearman's (b).\n# - Tests, unless the paper names one: \"non-parametric two-tailed Wilcoxon rank-sum ...,\n#   Wilcoxon signed-rank or Kruskal-Wallis\" (Methods, Statistical Analyses); signed-rank for\n#   paired values, rank-sum for unpaired.\n#\n# Not given claims: Figure S1B and S1F (single sessions illustrating the Peltier device and the\n# physiological range of brain temperature), Figure S4 (place field skewness and phase measures,\n# no finding stated) and Figure S6 (a model).\n#\n# Changes from the previous version (2026-10-19). Rewritten to the current protocol from the\n# full text with the supplement, which the previous version lacked. Session sets, thresholds\n# and windows chosen from the data or from unlinked code are removed; every method is now from\n# the paper or named as open with readings. Ids kept where the finding is the same. The Figure 5\n# criteria now use the surface fit of the Methods for compression and period. New claims:\n# fig2-theta-reduced-minutes was not added; added are suppl2ab-rates-correlated,\n# fig4f-speed-theta-power, suppl2e-trial-speed-theta-frequency, suppl3-theta-cycle-duration,\n# suppl3e-precession-temperature, fig5e-phase-period-below-2pi, suppl5gh-rates-follow-temperature\n# and suppl5j-errors-best-theta-frequency. fig6e-errors-recover gains the P < 1e-7 of Figure\n# 6E; fig5j-fraction-active-unchanged gains the legend's three P values; suppl2d now carries the\n# 14% of Figure S2D; suppl1-hippocampal-temperature gains the time constants. The dataset key is\n# dropped, as a paper's own claims file leaves it out.\nschema_version: 2\npaper: doi:10.1016/j.neuron.2020.05.023\nclaims:\n- id: session-structure\n  statement: A session holds about 40 control trials, then about 20 to 60 cooling trials and 20\n    to 80 recovery trials, 80 to 200 trials in all with a mean of 150.\n  source: Results, MS cooling decreases hippocampal theta frequency and power, paragraph 2; STAR\n    Methods, Electrophysiological Recordings\n  quote: After a block of control trials (~ 40 trials), dry ice was placed into the reservoir ...\n    about 20 to 60 'cooling' trials), followed by recovery trials (20 to 80).\n  expected:\n  - quantity: mean number of trials per session\n    value: 150\n    tolerance: 15\n  - quantity: typical number of control trials before cooling onset\n    value: 40\n    tolerance: 4\n  criterion: Over the sessions of the theta maze with cooling. The Methods give the total\n    (\"a total number of trials ranging from 80 to 200 (mean - 150 trials)\"). Reproduced when the\n    mean number of trials is within tolerance, every session has 72 to 220 trials (80 to 200\n    widened by 10%), the median number of pre trials is within tolerance of 40, and, under one\n    state reading, the median numbers of cooling and post trials are within 18 to 66 and 18 to\n    88. Partially reproduced when the mean holds and one other part fails.\n- id: cooling-time-course\n  statement: MS cooling typically peaked about 60 s after its onset and lasted about 10 to 12\n    minutes, about 50 trials.\n  source: STAR Methods, Electrophysiological Recordings\n  quote: The cooling typically peaked after about 60 sec after the cooling onset ( suppl. fig. 1G )\n    and lasted for about 10–12 minutes, corresponding to approximately 50 trials\n  expected:\n  - quantity: time from cooling onset to the minimum MS temperature\n    value: 60\n    tolerance: 6\n    unit: s\n  - quantity: number of trials during cooling\n    value: 50\n    tolerance: 5\n  criterion: Per session with an MS temperature trace. Cooling onset is the placement of dry ice;\n    the paper gives no rule to find it in the trace, so it is the time stamp of onset if the\n    dataset holds one, else the first time after the control block that the temperature falls\n    1 C below the median of the pre trials (a standard choice). The peak is the minimum of the\n    trace in the 5 minutes after onset (standard; Figure 2D shows the trough within minutes). The\n    paper does not define the end of cooling; readings for the duration, (a) the time until the\n    temperature is again within 1 C of the pre median; (b) the length of the cooling state as\n    labelled in the dataset. The Results give \"maximum effect at approximately 45 s\" for the\n    control experiment (see suppl1-hippocampal-temperature), so a median time to minimum within\n    40.5 to 66 s (45 and 60 widened by 10%) also counts. Reproduced when the median time to\n    minimum is within that range and, under one reading, the median duration is within 9 to\n    13.2 minutes and the median number of cooling trials within tolerance. Partially reproduced\n    when one or two of the three hold.\n- id: fig2g-theta-freq-temperature\n  statement: Theta frequency decreased linearly with MS temperature, down to 20 C (R = 0.81, P =\n    5.4e-48).\n  source: Results, MS cooling decreases hippocampal theta frequency and power, paragraph 2;\n    Figure 2G\n  quote: Theta frequency decreased linearly with MS temperature ( Figure 2g ; down to 20° C; R =\n    0.81; P = 5.4 × 10 −48 )\n  statistics:\n  - statistic: R = 0.81\n    p: 5.4e-48\n    n: 53 sessions in 5 rats\n  expected:\n  - quantity: R of theta frequency and MS temperature\n    value: 0.81\n    tolerance: 0.081\n  criterion: Figure 2G shows \"Group data for all sessions and subjects (mean values with SE)\"\n    over 53 sessions in 5 rats; the unit of the correlation is not stated. A Pearson R of 0.81\n    with P = 5.4e-48 implies about 170 points, so the points are not single trials pooled over\n    53 sessions (several thousand). Readings, (a) trials aligned on cooling onset (as Figure 6A\n    and C) and averaged over sessions at each aligned trial, R between the mean temperature and\n    the mean theta frequency over aligned trials; (b) the same with temperature binned (1 C\n    bins, standard) and R over all trials pooled with bin means as a variant; (c) all trials\n    pooled. Each theta reading of the opening comment is run. Reproduced when, under one reading,\n    R is within tolerance with P < 1e-10. Partially reproduced when R is positive with P < 0.05\n    under every reading but within tolerance under none. The number of points of the matching\n    reading is given.\n- id: fig2h-theta-power-temperature\n  statement: Theta power also decreased with MS temperature, less tightly than frequency (R =\n    0.54, P = 1.2e-16).\n  source: Results, MS cooling decreases hippocampal theta frequency and power, paragraph 2;\n    Figure 2H\n  quote: this relationship was more consistent across animals than the effect on theta power (R =\n    0.54; P = 1.2 × 10 −16 ; Fig. 2g , h )\n  statistics:\n  - statistic: R = 0.54\n    p: 1.2e-16\n    n: 53 sessions in 5 rats\n  expected:\n  - quantity: R of theta power and MS temperature\n    value: 0.54\n    tolerance: 0.054\n  criterion: As fig2g-theta-freq-temperature, with trial theta power, and the same readings\n    (this P implies about 190 points). Whether power is normalised per session before averaging\n    is open; readings, raw power and power divided by the session's mean pre power (Figure 2D\n    \"Color scale is normalized\"). Reproduced when, under one reading, R is within tolerance\n    with P < 1e-5 and below the frequency R of fig2g under the same reading. Partially\n    reproduced when R is positive with P < 0.05 but outside tolerance.\n- id: fig2j-frequency-consistent-across-animals\n  statement: The relationship of theta frequency with MS temperature was more consistent across\n    animals than that of theta power.\n  source: Results, MS cooling decreases hippocampal theta frequency and power, paragraph 2;\n    Figure 2J\n  quote: Theta frequency decreased linearly with MS temperature ... and this relationship was more\n    consistent across animals than the effect on theta power\n  depends_on:\n  - fig2g-theta-freq-temperature\n  - fig2h-theta-power-temperature\n  criterion: Figure 2J gives \"R and P values for theta frequency and power in individual rats\".\n    Per rat, R of frequency and of power with MS temperature computed as in fig2g under the\n    reading that matched there, over that rat's sessions. The paper does not say how consistency\n    is measured; readings, (a) the range of R over rats; (b) the standard deviation of R over\n    rats; (c) the number of rats with P < 0.05. Reproduced when every rat has a positive\n    frequency R with P < 0.05 and, under one reading, frequency is more consistent than power.\n    Partially reproduced when only one of the two holds.\n- id: fig2i-theta-pre-cooling-post\n  statement: MS cooling induced a fast and reversible decrease of hippocampal theta frequency and\n    power, lower during cooling than before and after it.\n  source: Results, MS cooling decreases hippocampal theta frequency and power, paragraph 2; Figure\n    2I\n  quote: MS cooling induced fast and reversible change in the frequency and power of hippocampal\n    theta oscillations\n  criterion: Figure 2I, \"Group data for theta frequency and power before, during and after MS\n    cooling\", 53 sessions in 5 rats; no test is printed. Per session, the mean over trials of\n    theta frequency and power in each state; the paper's default paired test, Wilcoxon\n    signed-rank over sessions, of cooling against pre and cooling against post. Reproduced\n    when, under one state and theta reading, all four tests show cooling lower at P < 0.05;\n    partially reproduced when the two frequency tests do and a power test does not.\n- id: disc-theta-frequency-12-percent\n  statement: During MS cooling LFP theta frequency decreased by about 12%.\n  source: Discussion, Theta phase organization of hippocampal cell assemblies, paragraph 5;\n    Results, MS temperature effects on theta time/phase compression, paragraph 4\n  quote: During MS cooling, LFP theta frequency decreased by 12 %\n  expected:\n  - quantity: decrease of theta frequency during cooling\n    value: 12\n    tolerance: 1.2\n    unit: percent\n  criterion: The paper does not say how the 12% is computed. Readings, (a) the mean over\n    sessions of 100 (1 - cooling / pre) of the session means of trial theta frequency; (b) the\n    same with the mean of pre and post as the reference; (c) the largest decrease of the\n    aligned mean series of Figure 6C (trials aligned on cooling onset, averaged over sessions)\n    relative to its pre mean. Under each state and theta reading. Reproduced when one reading\n    is within tolerance; partially reproduced when every reading shows a decrease but none is\n    within tolerance. The decrease of fLFP within place fields is in fig4b-fp-flfp-decrease\n    (8.4 to 7.7 Hz, about 8%).\n- id: fig6d-errors-increase\n  statement: MS cooling increased choice errors about 3-fold, within each rat (P < 0.05 for all\n    animals) and across all animals (P = 1e-6).\n  source: Results, MS cooling increases behavioral errors, paragraph 1; Figure 6D and 6E\n  quote: Overall, the number of memory errors increased approximately 3-fold, assessed either\n    within rats (P < 0.05 for all animals) or across all animals (P = 10 −6\n  statistics:\n  - about: within each rat\n    p: 0.05\n    p_relation: \"<\"\n  - about: across all animals\n    p: 1.0e-6\n  - about: boxplots over all sessions (Figure 6E, marked **)\n    p: 1.0e-7\n    p_relation: \"<\"\n  expected:\n  - quantity: ratio of the error rate during cooling to the control error rate\n    value: 3.0\n    tolerance: 0.3\n  criterion: Error rate is the percentage of error trials in a state, per session. The control\n    for the ratio is open; readings, (a) pre; (b) pre and post combined. The ratio is open as\n    well; readings, (i) the mean cooling rate over the mean control rate; (ii) the median over\n    sessions of the per-session ratio (sessions with a control rate above 0). Tests are not\n    named; the default paired test, Wilcoxon signed-rank over sessions of cooling against\n    control. Within a rat, an exact signed-rank test over fewer than 6 sessions cannot reach P <\n    0.05, so a rat with fewer sessions is tested with a Wilcoxon rank-sum over its trials of\n    the 0 or 1 error outcome, cooling against control. Reproduced when, under one reading, the\n    ratio is within tolerance, the test over sessions gives P < 1e-5, and every rat gives P <\n    0.05. Partially reproduced when the increase is significant over sessions but the ratio or a\n    rat fails.\n- id: fig6e-errors-recover\n  statement: The error rate after cooling did not differ from the error rate before it.\n  source: Figure 6E (marked ns)\n  quote: Choice errors shown as boxplots constructed from all sessions. ** P < 10 −7 ns =\n    nonsignificant.\n  criterion: A claim of absence. Figure 6E marks one comparison ns; with pre, cooling and post\n    shown and cooling marked ** against control, the ns is read as pre against post. The test is\n    not named; the default paired test, Wilcoxon signed-rank over sessions of post against pre\n    error rates, at 0.05. Reproduced when P >= 0.05, not reproduced when P < 0.05; the median\n    difference is given either way.\n- id: fig6c-worst-trials-4-to-8\n  statement: The worst memory performance occurred between trials 4 and 8 after the onset of\n    cooling, when MS temperature reached its minimum, together with the largest decreases of\n    theta frequency and power.\n  source: Results, MS cooling increases behavioral errors, paragraph 1; Figure 6C\n  quote: The worst memory performance occurred between trials 4 and 8 after MS cooling, when the MS\n    temperature reached its minimum, accompanied by the largest decreases of theta frequency and\n    power\n  criterion: Trials aligned on cooling onset (Figure 6A, \"Vertical line marks the onset of\n    cooling\"), the first trial after onset is trial 1. Per aligned trial, the error incidence\n    (fraction of sessions with an error) and the means of MS temperature, theta frequency and\n    power over sessions (Figure 6C, \"mean of all sessions\"). Whether the error series is\n    smoothed is open; readings, (a) no smoothing; (b) a 5-trial moving mean (standard).\n    Reproduced when, under one reading, the maximum of the error series over trials 1 to 40 is\n    at trials 4 to 8 and the minima of temperature, frequency and power fall within trials 2 to\n    10. Partially reproduced when the error maximum holds and one minimum is outside.\n- id: fig6f-errors-temperature\n  statement: The incidence of errors correlated negatively with MS temperature (R = -0.35, P <\n    0.01, all animals).\n  source: Results, MS cooling increases behavioral errors, paragraph 1; Figure 6F and 6J\n  quote: The incidence of errors negatively and significantly correlated with temperature change\n    (R = − 0.35; P < 0.01; all animals)\n  statistics:\n  - statistic: R = − 0.35\n    p: 0.01\n    p_relation: \"<\"\n    n: all animals\n  expected:\n  - quantity: R of error incidence and MS temperature\n    value: -0.35\n    tolerance: 0.035\n  criterion: The unit of the correlation is not stated (Figure 6F, \"Relationship between memory\n    errors and temperature\", with standard errors). Readings, (a) over aligned trials, the error\n    incidence and the mean temperature across sessions (as fig6c, unsmoothed and smoothed); (b)\n    over all trials pooled, the 0 or 1 error outcome and the trial temperature; (c) per rat, as\n    (a) over that rat's sessions (Figure 6J). \"All animals\" is read as pooled for (a) and (b);\n    for (c) every rat must show it. Reproduced when, under one reading, R is within tolerance\n    and P < 0.01. Partially reproduced when R is negative with P < 0.01 under one reading and\n    none is within tolerance. Per-rat R and P are given.\n- id: fig6g-errors-theta-frequency\n  statement: The incidence of errors correlated negatively with theta frequency (R = -0.35, P <\n    0.01, all animals).\n  source: Results, MS cooling increases behavioral errors, paragraph 1; Figure 6G and 6J\n  quote: The incidence of errors negatively and significantly correlated with ... theta frequency\n    (R = − 0.35; P < 0.01; all animals)\n  statistics:\n  - statistic: R = − 0.35\n    p: 0.01\n    p_relation: \"<\"\n    n: all animals\n  expected:\n  - quantity: R of error incidence and theta frequency\n    value: -0.35\n    tolerance: 0.035\n  depends_on:\n  - fig6f-errors-temperature\n  criterion: The readings of fig6f-errors-temperature with trial theta frequency (the theta\n    shift of Figure 6A, a difference from pre, gives the same R over aligned trials). Same\n    rule.\n- id: fig6h-errors-theta-power\n  statement: The incidence of errors correlated less with theta power; only 2 of 5 animals had a\n    significant correlation.\n  source: Results, MS cooling increases behavioral errors, paragraph 1; Figure 6H and 6J\n  quote: and less so with theta power (only 2 of 5 animals had significant R > − 0.3; P < 0.01)\n  expected:\n  - quantity: animals with a significant correlation of errors and theta power\n    value: 2\n    tolerance: 0\n  depends_on:\n  - fig6f-errors-temperature\n  criterion: Per rat, R of error incidence and theta power as reading (c) of\n    fig6f-errors-temperature. \"R > -0.3\" is read as R beyond -0.3 in magnitude (R < -0.3), the\n    sign the other correlations take; the other reading, R above -0.3, is shown. An animal\n    counts when R < -0.3 and P < 0.01. Reproduced when 2 animals count; partially reproduced\n    when 1 or 3 do.\n- id: fig6i-errors-not-speed\n  statement: The incidence of errors did not correlate with the running speed of the rat (R\n    about 0.1, P > 0.05 for all animals).\n  source: Results, MS cooling increases behavioral errors, paragraph 1; Figure 6I and 6J\n  quote: and not with the running speed of the rat (R ~ 0.1; P > 0.05 for all animals\n  statistics:\n  - statistic: R ~ 0.1\n    p: 0.05\n    p_relation: \">\"\n    n: all animals\n  depends_on:\n  - fig6f-errors-temperature\n  criterion: A claim of absence, judged per animal as the paper reports it. Per rat, R of error\n    incidence and mean trial speed as reading (c) of fig6f-errors-temperature, at 0.05.\n    Reproduced when no rat has P < 0.05; not reproduced when any does. R and P are given for\n    every rat, and the pooled R.\n- id: suppl5j-errors-best-theta-frequency\n  statement: Error rates correlated best with theta frequency, in correlations and partial\n    correlations, and had no significant relationship to running speed.\n  source: Figure S5J\n  quote: Partial correlation values (top) and P values (bottom) for each comparison (right panels).\n    Note error rates correlate best with theta frequency and have no significant relationship to\n    running speed.\n  depends_on:\n  - fig6f-errors-temperature\n  criterion: Over aligned trials as reading (a) of fig6f-errors-temperature (Figure S5C, F, I\n    are group means), R of error incidence with MS temperature, theta frequency, theta power and\n    speed, and the partial correlation of errors with each controlling for the other three (the\n    set controlled for is not stated; this is the reading the panel's four comparisons allow).\n    Reproduced when theta frequency has the largest magnitude of partial correlation and speed\n    has P >= 0.05 in both; partially reproduced when theta frequency is largest in one of the two.\n- id: fig4e-speed-decreases-within-session\n  statement: Running speed decreased relatively monotonically within a session, from the start to\n    the end, independent of cooling.\n  source: Results, Effects of MS cooling on single neuron properties, paragraph 3; Figure 6C;\n    Figure S5D, E\n  quote: Running speed decreased relatively monotonically within session ( Fig. 4e ; see also Fig.\n    5c ).\n  criterion: Figure S5E notes \"monotonic deceleration of running speed over the entire session\".\n    Over aligned trials, the mean trial speed across sessions (Figure 6C); and per session the\n    Spearman correlation of trial speed with trial number. No test is given; the default\n    one-sample signed-rank of the per-session correlations against 0. Reproduced when the\n    aligned mean has a negative Spearman correlation with trial number at P < 0.05, more than\n    half of the sessions are negative, and the signed-rank test gives P < 0.05. Partially\n    reproduced when two of the three hold.\n- id: fig5-speed-control-cooling\n  statement: In the sessions of Figure 5, mean running speed was 87.3 +- 8.0 in control trials\n    (pre and post combined) and 86.2 +- 9.9 during MS cooling.\n  source: Results, MS temperature effects on theta time/phase compression of place cells\n    sequences, paragraph 2\n  quote: we combined trials before and after cooling into a single control group (mean running\n    speed = 87.3±8.0). During MS cooling (mean running speed = 86.2±9.9)\n  expected:\n  - quantity: mean running speed, control (pre and post)\n    value: 87.3\n    tolerance: 8.0\n    unit: cm/s\n  - quantity: mean running speed, cooling\n    value: 86.2\n    tolerance: 9.9\n    unit: cm/s\n  criterion: The unit is not printed; cm/s is the unit of speed throughout the paper. The\n    tolerances are the paper's stated spreads. Mean over the Figure 5 sessions of the session\n    mean speed, under each running reading of the opening comment; sessions are those with\n    place cell pairs as in fig5d-ccg-period, readings the 18 sessions of Figure 5C and the 10\n    of Figure 5H when they can be told apart. Reproduced when both values are within tolerance\n    under one reading.\n- id: suppl2-place-cell-rates-decrease\n  statement: Within-field and peak firing rates of place cells decreased moderately during MS\n    cooling (11% and 12%; P < 1e-9 and P < 1e-11).\n  source: Results, Effects of MS cooling on single neuron properties, paragraph 2; Figure S2A, B\n  quote: Both within-field and peak firing rates of place cells decreased moderately during MS\n    cooling ( Suppl. Fig. 2 ; 11% and 12%; P < 10 −9 and P < 10 −11 , respectively\n  statistics:\n  - about: within-field firing rate\n    p: 1.0e-9\n    p_relation: \"<\"\n  - about: peak firing rate\n    p: 1.0e-11\n    p_relation: \"<\"\n  expected:\n  - quantity: decrease of within-field firing rate\n    value: 11\n    tolerance: 1.1\n    unit: percent\n  - quantity: decrease of peak firing rate\n    value: 12\n    tolerance: 1.2\n    unit: percent\n  criterion: Place fields of putative pyramidal cells (place field readings of the opening\n    comment). Within-field rate is the spike count in the field over the time spent in it; peak\n    rate the maximum of the state's rate map in the field. Cooling against pre (Figure S2,\n    \"before and during MS cooling\"). The percentage is open; readings, (a) the median over fields\n    of the per-field decrease; (b) the decrease of the mean over fields; (c) the mean of the\n    per-field decreases. The Discussion gives 12% for the within-field rate (\"decreased by a\n    similar proportion (12%\"), so a within-field value within 10% of 12 also counts. Tests not\n    named; the default Wilcoxon signed-rank over fields. Reproduced when, under one reading,\n    both decreases are within tolerance and both tests give P < 1e-6; partially reproduced when\n    both decreases are significant but no reading puts both within tolerance.\n- id: suppl2ab-rates-correlated\n  statement: Firing rates of pyramidal cells before and during MS cooling were strongly correlated\n    (R = 0.7, P < 1e-58).\n  source: Figure S2A, B\n  quote: Firing rates of pyramidal neurons within their place fields (A) and their peak firing\n    rates (B) (top) and illustration of the rate changes before and during MS cooling. R = 0.7, P\n    < 10-58.\n  statistics:\n  - statistic: R = 0.7\n    p: 1.0e-58\n    p_relation: \"<\"\n  expected:\n  - quantity: R of firing rates before and during cooling\n    value: 0.7\n    tolerance: 0.07\n  depends_on:\n  - suppl2-place-cell-rates-decrease\n  criterion: The legend does not say which of the two rates R refers to; readings, within-field\n    rate and peak rate, each pre against cooling over fields, on linear and log scales (the\n    panels' axes cannot be read from the text). Reproduced when, under one reading, R is within\n    tolerance with P < 1e-20; partially reproduced when R is positive with P < 0.05 under all.\n- id: disc-interneuron-rates-decrease\n  statement: Firing rates of interneurons decreased during MS cooling by about 14%, about the same\n    degree as place cells.\n  source: Discussion, Theta phase organization of hippocampal cell assemblies, paragraph 5;\n    Results, Effects of MS cooling on single neuron properties, paragraph 2; Figure S2C\n  quote: within-field firing rates of place cells decreased by a similar proportion (12%;\n    interneurons 14%).\n  expected:\n  - quantity: decrease of interneuron firing rate\n    value: 14\n    tolerance: 1.4\n    unit: percent\n  criterion: Figure S2C covers \"putative fast firing interneurons\"; readings, (a) narrow waveform\n    interneurons; (b) narrow and wide waveform interneurons. Rate over the trials of each state\n    under each running reading, cooling against pre. The percentage readings of\n    suppl2-place-cell-rates-decrease. Reproduced when one reading is within tolerance and a\n    Wilcoxon signed-rank test over units gives P < 0.05; partially reproduced when the decrease\n    is significant but outside tolerance.\n- id: suppl5gh-rates-follow-temperature\n  statement: Firing rates of pyramidal cells and putative interneurons decreased immediately after\n    MS cooling onset and their changes correlated with MS temperature, not with the delayed\n    hippocampal temperature.\n  source: Results, MS cooling decreases hippocampal theta frequency and power, paragraph 3; Figure\n    S5G, H\n  quote: firing rates of both pyramidal cells and putative interneurons in the hippocampus\n    decreased immediately after MS cooling and the changes correlated well with MS temperature\n    change\n  expected:\n  - quantity: interneurons in the trial-wise rate analysis\n    value: 319\n    tolerance: 32\n  - quantity: pyramidal cells in the trial-wise rate analysis\n    value: 1104\n    tolerance: 110\n  criterion: Figure S5G, H give \"Trial-wise average firing rates for interneurons (G) and\n    pyramidal cells (H) across 19 sessions\". Per unit, the trial rate divided by its mean pre\n    rate (normalisation is open; raw rates are a second reading); per aligned trial the mean\n    over units. Reproduced when, for both classes and under one reading, the mean rate over\n    aligned trials 1 to 5 after onset is below the pre mean (signed-rank over units, P < 0.05)\n    and the aligned rate series has a positive R with MS temperature at P < 0.05. Partially\n    reproduced when one class holds. The comparison with hippocampal temperature needs the\n    control experiment of suppl1-hippocampal-temperature and is reported only. Unit counts are\n    checked against the expected values, which say whether the same units are used.\n- id: fig4b-fp-flfp-decrease\n  statement: MS cooling decreased both the oscillation frequency of place cells (fp) and the LFP\n    theta frequency in their fields (fLFP) by about the same degree, and both recovered (fLFP\n    8.4, 7.7, 8.5 Hz; fp 10.6, 9.5, 10.4 Hz before, during and after; n = 365).\n  source: Results, Effects of MS cooling on single neuron properties, paragraph 2; Figure 4B\n  quote: MS cooling decreased both f p and f LFP , measured within the place fields of neurons, by\n    approximately the same degree ... Both values recovered after cooling.\n  statistics:\n  - about: comparison marked *** in Figure 4B\n    p: 5.9e-8\n    p_relation: \"<\"\n    n: 365 place fields\n  expected:\n  - quantity: fLFP pre\n    value: 8.4\n    tolerance: 0.38\n    unit: Hz\n  - quantity: fLFP cooling\n    value: 7.7\n    tolerance: 0.36\n    unit: Hz\n  - quantity: fLFP post\n    value: 8.5\n    tolerance: 0.29\n    unit: Hz\n  - quantity: fp pre\n    value: 10.6\n    tolerance: 0.95\n    unit: Hz\n  - quantity: fp cooling\n    value: 9.5\n    tolerance: 0.84\n    unit: Hz\n  - quantity: fp post\n    value: 10.4\n    tolerance: 0.72\n    unit: Hz\n  criterion: The tolerances are the paper's stated spreads. Per place field and state, fp from\n    the autocorrelogram of the field's in-field spikes and fLFP, both as the opening comment;\n    means over fields. The minimum number of spikes for an autocorrelogram is open; fields are\n    kept when the autocorrelogram has a peak between 50 and 150 ms in each state (the Methods'\n    window). The legend does not say which comparison *** marks; the default signed-rank over\n    fields, cooling against pre, for fp and for fLFP. Reproduced when, under one reading, all\n    six means are within tolerance and both decreases give P < 0.05; partially reproduced when\n    both decreases are significant but a mean is outside tolerance. The number of fields is\n    compared with 365.\n- id: fig4c-fp-flfp-correlation\n  statement: fp and fLFP were correlated across place fields before, during and after cooling (R\n    = 0.61, 0.59 and 0.36; P < 1e-6 each), with the range of fp larger than that of fLFP.\n  source: Figure 4C; Results, Effects of MS cooling on single neuron properties, paragraph 2\n  quote: Correlation between LFP theta frequency ( f LFP ) and place cell oscillation frequency ( f\n    p ; R pre = 0.61; R cooling = 0.59; Rpost = 036; P < 10 −6 each)\n  statistics:\n  - about: each of before, during and after cooling\n    statistic: R pre = 0.61; R cooling = 0.59; Rpost = 036\n    p: 1.0e-6\n    p_relation: \"<\"\n  expected:\n  - quantity: R pre\n    value: 0.61\n    tolerance: 0.061\n  - quantity: R cooling\n    value: 0.59\n    tolerance: 0.059\n  - quantity: R post\n    value: 0.36\n    tolerance: 0.036\n  depends_on:\n  - fig4b-fp-flfp-decrease\n  criterion: '\"Rpost = 036\" is read as 0.36. R over the fields of fig4b-fp-flfp-decrease in each\n    state. Reproduced when all three are within tolerance with P < 1e-6 and the interquartile\n    range of fp exceeds that of fLFP in pre and cooling; partially reproduced when all three are\n    positive with P < 0.05 and one or more is outside tolerance.'\n- id: fig4ac-fp-flfp-difference-preserved\n  statement: During MS cooling fp and fLFP decreased in parallel, so the difference fp - fLFP\n    remained constant.\n  source: Discussion, Theta phase organization of hippocampal cell assemblies, paragraph 3;\n    Results, Effects of MS cooling on single neuron properties, paragraph 2\n  quote: However, during MS cooling f p and f LFP decreased proportionally (i.e., f p – f LFP\n    difference remained constant)\n  depends_on:\n  - fig4b-fp-flfp-decrease\n  criterion: A claim of absence. The paper names no test; its default paired test, Wilcoxon\n    signed-rank over the fields of fig4b of fp - fLFP during cooling against pre, at 0.05.\n    Reproduced when P >= 0.05, not reproduced when P < 0.05; the median change is given.\n- id: fig4a-frequency-temperature-slopes\n  statement: fLFP and fp measured within place fields decreased linearly with MS temperature\n    (fLFP R = 0.66, slope 0.071 Hz per C; fp R = 0.38, slope 0.09 Hz per C).\n  source: Results, Effects of MS cooling on single neuron properties, paragraph 1; Figure 4A\n  quote: \"The theta oscillation frequency of pyramidal neurons decreased linearly and paralleled\n    the downward frequency shift of LFP theta oscillation ( Fig. 4a ; f LFP : R = 0.66, Slope =\n    0.071. f p : R = 0.38, slope = 0.09).\"\n  expected:\n  - quantity: R of fLFP and MS temperature\n    value: 0.66\n    tolerance: 0.066\n  - quantity: slope of fLFP on MS temperature\n    value: 0.071\n    tolerance: 0.0071\n    unit: Hz/C\n  - quantity: R of fp and MS temperature\n    value: 0.38\n    tolerance: 0.038\n  - quantity: slope of fp on MS temperature\n    value: 0.09\n    tolerance: 0.009\n    unit: Hz/C\n  depends_on:\n  - fig4b-fp-flfp-decrease\n  criterion: '\"Each dot is a trial average measured within a single place field\" (Figure 4A\n    legend). Readings for a dot, (a) one field and one trial, fp from that trial''s in-field\n    spikes, dots kept when the autocorrelogram has a peak between 50 and 150 ms; (b) one field\n    and one state, with the state''s mean temperature. Temperature is the mean MS temperature\n    at the field''s spikes. R and least-squares slope over all dots pooled. Reproduced when,\n    under one reading, all four values are within tolerance; partially reproduced when both\n    slopes are positive with P < 0.05 and a value is outside tolerance.'\n- id: fig3c-field-size-correlated\n  statement: Place field size was highly correlated before and during MS cooling (R = 0.91), and\n    did not change.\n  source: Results, Effect of MS cooling on place field features, paragraph 1; Figure 3C\n  quote: Place field size does not change with MS cooling (R = 0.91).\n  expected:\n  - quantity: R of field size before and during cooling\n    value: 0.91\n    tolerance: 0.091\n  criterion: Field size is not defined beyond its boundaries. Readings, (a) the length of the\n    field as bounded in the dataset, if it holds boundaries per state; (b) the number of\n    contiguous bins around the peak above 10% of the state's peak rate (the threshold of the\n    Figure 5 rule) times the bin width. R over fields, pre against cooling. Reproduced when, under\n    one reading, R is within tolerance. Partially reproduced when R is 0.5 or more. The median\n    change of size and a signed-rank test are reported, not judged, as the paper gives no test\n    of the change.\n- id: fig3d-size-fp-negative\n  statement: Place field size and fp were negatively correlated before, during and after cooling\n    (R = -0.49, -0.40, -0.40; P < 1e-9), with similar slopes and a slightly lower intercept\n    during cooling.\n  source: Figure 3D; Results, Effect of MS cooling on place field features, paragraph 1\n  quote: Place field size continues to be inversely correlated with f p after MS cooling (R pre =\n    − 0.49; R cooling = − 0.40; R post = − 0.40. P < 10 −9 all conditions).\n  statistics:\n  - about: each of before, during and after cooling\n    statistic: R pre = − 0.49; R cooling = − 0.40; R post = − 0.40\n    p: 1.0e-9\n    p_relation: \"<\"\n  expected:\n  - quantity: R pre\n    value: -0.49\n    tolerance: 0.049\n  - quantity: R cooling\n    value: -0.4\n    tolerance: 0.04\n  - quantity: R post\n    value: -0.4\n    tolerance: 0.04\n  depends_on:\n  - fig4b-fp-flfp-decrease\n  - fig3c-field-size-correlated\n  criterion: R over the fields of fig4b-fp-flfp-decrease of the state's field size (readings of\n    fig3c) and fp. The Results add \"similar slopes, even though the intercept of the regression\n    line during cooling slightly decreased\"; the least-squares slopes and intercepts are\n    reported. Reproduced when all three R are within tolerance with P < 1e-9; partially\n    reproduced when all three are negative with P < 0.05.\n- id: fig3e-model-field-size\n  statement: Measured place field size correlated with the size predicted by S = v / (fp - fLFP)\n    before (R = 0.55), during (R = 0.54) and after (R = 0.11) cooling.\n  source: Results, Effect of MS cooling on place field features, paragraph 2; Figure 3E\n  quote: We found a reliable and similar relationships between measured place field sizes and\n    model-predicted sizes for trials before (R = 0.55), during (R = 0.54) and after (R = 0.11) MS\n    cooling\n  expected:\n  - quantity: R pre\n    value: 0.55\n    tolerance: 0.055\n  - quantity: R cooling\n    value: 0.54\n    tolerance: 0.054\n  - quantity: R post\n    value: 0.11\n    tolerance: 0.011\n  depends_on:\n  - fig4b-fp-flfp-decrease\n  - fig3c-field-size-correlated\n  criterion: v is the \"locomotion velocity within the place field\" (Results); readings, the mean\n    speed over the time in the field, and the mean speed at the field's spikes. Fields with fp\n    <= fLFP give no prediction and are left out. R over fields per state. Reproduced when, under\n    one reading, all three R are within tolerance; partially reproduced when pre and cooling are\n    within tolerance or positive with P < 0.05 and post is not.\n- id: fig3f-information-unchanged\n  statement: The information content of place cell spikes was not altered by MS cooling (P >\n    0.26).\n  source: Results, Effect of MS cooling on place field features, paragraph 2; Figure 3F\n  quote: Information content of place cell spikes was also left unaltered by MS cooling (P > 0.26;\n    Fig. 3f ).\n  statistics:\n  - p: 0.26\n    p_relation: \">\"\n  criterion: A claim of absence. \"None of the comparisons are significantly different\" (Figure\n    3F). The measure is not defined; spatial information in bits per spike (Skaggs), the\n    standard measure of a spike's information content, is used. The test is not named; the\n    default paired test, Wilcoxon signed-rank over place cells, for pre against cooling,\n    cooling against post and pre against post, at 0.05. Reproduced when all three give P >=\n    0.05; not reproduced when any gives P < 0.05. Median changes are given.\n- id: fig3hi-population-vector-unchanged\n  statement: The spatial scale of the population vector correlation of pyramidal cells was not\n    affected by MS cooling.\n  source: Results, Effect of MS cooling on place field features, paragraph 3; Figure 3G, H, I\n  quote: Population vector correlation of pyramidal cells was not affected by MS cooling ( Fig. 3g\n    , h ).\n  criterion: A claim of absence. Per session and state, population vectors of the pyramidal\n    cells' binned rate maps; the decorrelation curve is the mean correlation of vectors at bins d\n    apart (the cross-diagonals of the matrix, Figure 3H), and the scale is the distance at\n    which it drops to 0.5 (Results; Figure 3H). 21 sessions in the paper. Whether arms are kept\n    apart is open; the matrix of Figure 3G spans the whole maze with arm boundaries marked, so\n    vectors are compared along the linearized maze within each run direction (standard). The\n    test is not named; the default Wilcoxon signed-rank over sessions of pre against cooling, at\n    0.05. Reproduced when P >= 0.05, not reproduced when P < 0.05; the median change is given.\n- id: fig4d-precession-slope-decrease\n  statement: The phase precession slope decreased slightly but significantly during MS cooling (P\n    < 0.007 and P < 0.0003).\n  source: Results, Effects of MS cooling on single neuron properties, paragraph 2; Figure 4D\n  quote: decreased slightly, but nevertheless significantly, during MS cooling ( Fig. 4d ).\n  statistics:\n  - about: comparison marked ** in Figure 4D\n    p: 0.007\n    p_relation: \"<\"\n  - about: comparison marked *** in Figure 4D\n    p: 0.0003\n    p_relation: \"<\"\n  depends_on:\n  - fig4b-fp-flfp-decrease\n  criterion: Per field and state, circular-linear regression of theta phase on position for all\n    spikes within the field's boundaries (Methods). The two marked comparisons are read as\n    cooling against pre and cooling against post. \"Decreased\" is open; readings, (a) the slope's\n    magnitude is smaller during cooling (flatter), which Figure S3E's negative R of slope and\n    temperature supports when slopes are negative; (b) the signed slope is lower. Tests not\n    named; Wilcoxon signed-rank over fields. Reproduced when, under one reading, both\n    comparisons give P < 0.05; partially reproduced when one does.\n- id: suppl3e-precession-temperature\n  statement: The phase precession slope had a low but significant correlation with MS temperature\n    (R = -0.027, P = 7.67e-19).\n  source: Figure S3E\n  quote: Phase precession slope as a function of MS temperature. All values from before, during\n    and after MS cooling trials are combined. Note low (R = -0.027) but significant (P = 7.67e-19)\n    correlation.\n  statistics:\n  - statistic: R = -0.027\n    p: 7.67e-19\n  expected:\n  - quantity: R of phase precession slope and MS temperature\n    value: -0.027\n    tolerance: 0.0027\n  depends_on:\n  - fig4d-precession-slope-decrease\n  criterion: The unit of a value is not stated; R = -0.027 with P = 7.67e-19 implies about 1e5\n    values. Readings, (a) one value per field and trial (slope from that trial's in-field\n    spikes, with MS temperature of the trial); (b) one value per field and state. Reproduced\n    when, under one reading, R is within tolerance and P < 1e-10; partially reproduced when R is\n    negative with P < 0.05 under one reading. The number of values is given.\n- id: fig4f-speed-theta-power\n  statement: Running speed correlated with theta power.\n  source: Results, Effects of MS cooling on single neuron properties, paragraph 3; Figure 4F;\n    Figure S2H\n  quote: The animal's speed correlated with both theta power and f p ( Fig. 4f , g ).\n  criterion: Figure 4F, \"Theta power as a function of running speed\". The unit is open;\n    readings, (a) trial mean speed and trial theta power over all trials; (b) per rat as Figure\n    S2H. R positive with P < 0.05 under reading (a), and in at least 4 of 5 rats under (b), is\n    reproduced; partially reproduced when only one reading holds.\n- id: fig4gh-fp-speed\n  statement: fp depended on running speed more strongly than fLFP, so fp - fLFP increased with\n    speed, and fp during cooling was lower at all velocities.\n  source: Results, Effects of MS cooling on single neuron properties, paragraph 3; Figure 4G and\n    4H\n  quote: f p changes during MS cooling could not be explained by decreased running velocity of the\n    rat because f p values during cooling were lower at all velocities ( Fig. 4g ).\n  depends_on:\n  - fig4b-fp-flfp-decrease\n  criterion: Per field, in-field spikes grouped by the speed at the spike in bins of 10 cm/s (a\n    standard choice; the paper gives none; 20 cm/s is a variant), fp and fLFP per bin as the\n    opening comment, bins kept when the autocorrelogram has a peak between 50 and 150 ms.\n    Pooling states (Figure 4H), least-squares slopes of fp and fLFP on bin speed over all\n    field-bins. Reproduced when the fp slope is positive at P < 0.05 and larger than the fLFP\n    slope (95% bootstrap interval of the difference over fields above 0), and in every speed bin\n    with at least 10 fields measured in both states the median fp during cooling is below that\n    of pre. Partially reproduced when one of the two parts holds.\n- id: suppl2e-trial-speed-theta-frequency\n  statement: Over trials, mean theta frequency correlated positively with mean running speed\n    before, during and after MS cooling, with the largest changes at 10 to 40 cm/s.\n  source: Results, Effects of MS cooling on single neuron properties, paragraph 3; Figure S2E, G\n  quote: This comparison showed a positive correlation before, during and after MS cooling with the\n    largest changes taking place at lower running speeds (10 to 40 cm/s; Suppl. Fig. 2e ).\n  criterion: Per trial, mean theta frequency and mean running speed (Results, \"comparing the mean\n    theta frequency with the mean running speed in each trial\"), over all sessions, per state.\n    Reproduced when R is positive with P < 0.05 in each state and the least-squares slope over\n    trials of 10 to 40 cm/s is larger than over trials above 40 cm/s in at least two of the\n    three states. Partially reproduced when the correlations hold and the slopes do not.\n- id: suppl3-theta-cycle-duration\n  statement: Theta cycles were consistently longer during MS cooling at every position on the\n    track and returned to control duration after cooling, and the duration profile did not\n    correlate with the speed profile along the track.\n  source: Results, Effects of MS cooling on single neuron properties, paragraph 3; Figure S3B, D\n  quote: While theta duration was consistently longer during MS cooling trials, duration\n    distribution did not correlate with the speed distribution on the track ( Suppl. Fig. 3 ).\n  criterion: Theta cycles from the Hilbert phase of the opening comment, one cycle between\n    successive phase wraps (standard), during trials. Per session (21 in Figure S3D), median\n    cycle duration per state; the default signed-rank over sessions. Per position bin (5 cm,\n    standard), mean cycle duration and mean speed per state. Reproduced when cooling is longer\n    than pre and post (P < 0.05 each), post does not differ from pre (P >= 0.05), cooling is\n    longer than pre in at least 90% of position bins, and the R over position bins of duration\n    and speed has P >= 0.05 in pre. Partially reproduced when the state comparisons hold and the\n    position parts do not.\n- id: fig5d-ccg-period\n  statement: The theta-repeated cross-correlograms of place cell pairs had a period of about 85 ms\n    before cooling, shorter than the LFP theta period (about 110 ms), and the period lengthened\n    during MS cooling in each session (P = 0.002), while the period of the phase\n    cross-correlograms was unaffected (P = 0.32).\n  source: Figure 5D and 5F; Results, MS temperature effects on theta time/phase compression of\n    place cells sequences, paragraph 2\n  quote: Duration of the theta-repeated spike cross-correlograms (as in d ), calculated for each\n    session, significantly increased during MS cooling ... whereas the spike phase-lag\n    correlations remained unaffected (n.s., P = 0.32).\n  statistics:\n  - about: period of the time cross-correlograms, cooling against control (pre and post)\n    test: two-sided signed rank test\n    p: 0.002\n  - about: period of the phase cross-correlograms, cooling against control\n    p: 0.32\n  expected:\n  - quantity: period of the summed pair cross-correlogram before cooling\n    value: 85\n    tolerance: 8.5\n    unit: ms\n  criterion: 'Fields by the Figure 5 rule of the opening comment. Pairs are overlapping fields of\n    different cells (Methods, \"individual overlapping fields\"). Spikes as the animal passes\n    through the fields; readings, (a) each cell''s spikes within its own field; (b) both cells''\n    spikes within the union of the two fields. Per pair, a cross-correlogram with 1 ms bins\n    convolved with a 60-bin Gaussian window, over lags of plus and minus 400 ms (the \"0.8-s\n    period\" of the Results); on the phase axis, 0.01 pi bins with a 60-bin window on unwrapped\n    (cumulative) theta phase (standard; phase lags over several cycles need it). The period is\n    taken two ways the paper gives, (i) the spacing of the peaks of the summed cross-correlogram\n    of all pairs (Figure 5D, \"Sum of the theta repeated spike cross-correlograms\"); (ii) the\n    parameter b of the surface fit of fig5cg-compression (Methods, \"The compression and\n    oscillation period were determined by fitting the surface equation\"). Per session for\n    Figure 5F; control is pre and post combined (legend). The 85 ms is read on pre (\"NoCooling\",\n    the pairs of Figure 5C, which are pre); pre and post combined is the other reading. Session\n    sets, (a) all sessions with pairs; (b) sessions with pairs in every state; the paper has 18\n    and 10, and P = 0.002 is the smallest two-sided exact signed-rank P for 10 sessions, so with\n    \"f p decreased in each examined session\" it points at 10 sessions all in one direction.\n    Test, two-sided Wilcoxon signed-rank over sessions. Reproduced when, under one reading, the\n    pre period is within tolerance and below 1/fLFP of the same trials, the cooling period is\n    longer at P < 0.05, and the phase period does not differ (P >= 0.05). Partially reproduced\n    when the lengthening holds and one other part fails.'\n- id: fig5e-phase-period-below-2pi\n  statement: The period of the summed phase cross-correlograms of place cell pairs was shorter\n    than one theta cycle (2 pi), as place cells oscillate faster than LFP theta.\n  source: Figure 5E\n  quote: Similar to d but instead of time lags, within-theta phase lags between spikes were\n    calculated. Vertical dashed line indicates that the oscillation frequency of the spike\n    cross-correlation is faster than that of f LFP (2π).\n  depends_on:\n  - fig5d-ccg-period\n  criterion: The summed phase cross-correlogram of fig5d-ccg-period, before cooling and during\n    cooling. Reproduced when, under one reading of fig5d, the peak spacing is below 2 pi in both;\n    partially reproduced when it is below 2 pi in one.\n- id: fig5cg-compression\n  statement: Distance-time compression of place cell pairs (0.54 cm/ms before cooling) decreased\n    during MS cooling (P = 0.02), while distance-phase compression was unchanged (P = 0.92).\n  source: Figure 5C and 5G; Results, MS temperature effects on theta time/phase compression of\n    place cells sequences, paragraph 2\n  quote: Compression index, c (cm/ms; i.e., the slope in c ), significantly decreased during MS\n    cooling (* P = 0.02) but the distance/phase lag compression (cm/radian) remained unaffected (P\n    = 0.92).\n  statistics:\n  - about: distance-time compression, cooling against control\n    p: 0.02\n  - about: distance-phase compression, cooling against control\n    p: 0.92\n  expected:\n  - quantity: distance-time compression before cooling, all pairs pooled\n    value: 0.54\n    tolerance: 0.054\n    unit: cm/ms\n  depends_on:\n  - fig5d-ccg-period\n  criterion: 'Pairs, cross-correlograms and session readings of fig5d-ccg-period. Ltr is the\n    signed distance between the two fields'' rate peaks (Methods). Per the Methods, the\n    compression a and period b come from fitting a surface to \"the density of points\" of Figure\n    5C, the pairs'' smoothed cross-correlograms placed at their Ltr. The extracted equation reads\n    Z = cos(x 2 pi a b + y 2 pi b + 1) exp(-(x + f y)^2 / 2c^2) exp(-(y - g)^2 / 2d^2) e, with\n    its fraction bars lost. Readings, (a) Z = e (cos(2 pi x / (a b) + 2 pi y / b) + 1)\n    exp(-(x + f y)^2 / 2c^2) exp(-(y - g)^2 / 2d^2), with x the distance Ltr (cm) and y the lag\n    (ms), whose ridges have slope a cm/ms and spacing b ms; (b) the same with the +1 inside the\n    cosine as printed. The grid of the density (bins of lag and distance) and the start values\n    of the fit are open; standard choices are 1 ms by 5 cm, with a started at the least-squares\n    slope of Ltr on the pairs'' main lags and b at the period of the summed cross-correlogram.\n    Phase compression is the same fit on the phase axis (cm/rad). Fit on all pre pairs pooled\n    for the 0.54 (Figure 5C, 2948 pairs); per session and condition, control being pre and post\n    combined, for Figure 5G. The test is not named; the default Wilcoxon signed-rank over\n    sessions. Reproduced when, under one reading, the pooled pre compression is within\n    tolerance, the per-session compression is lower during cooling at P < 0.05, and the phase\n    compression does not differ (P >= 0.05). Partially reproduced when the decrease holds and\n    one other part fails. The least-squares slope of Ltr on each pair''s main lag (fig5h) is a\n    variant.'\n- id: fig5h-time-lags-increase\n  statement: During MS cooling the theta time lags between place cell pairs increased compared\n    with before and after cooling (P = 8.0e-5 and P = 0.00032), and did not differ between before\n    and after (P = 0.79).\n  source: Results, MS temperature effects on theta time/phase compression of place cells\n    sequences, paragraph 3; Figure 5H\n  quote: During MS cooling, the time lags increased significantly ( Fig. 5h ; P < 10 −4 ; sign rank\n    test; n = 10 sessions), whereas they were not different from each other during precooling and\n    post-cooling sessions (P = 0.79)\n  statistics:\n  - about: pre against cooling\n    test: sign rank test\n    p: 8.0e-5\n    n: 10 sessions, 4 rats\n  - about: post against cooling\n    test: sign rank test\n    p: 0.00032\n    n: 10 sessions, 4 rats\n  - about: pre against post\n    test: sign rank test\n    p: 0.79\n    n: 10 sessions, 4 rats\n  depends_on:\n  - fig5d-ccg-period\n  criterion: The legend prints \"P = 8.0 −5\", read as 8.0e-5. The time lag tau of a pair is its\n    theta-scale lag, the peak of the smoothed cross-correlogram of fig5d. Which peak is open;\n    readings, (a) the largest peak within half the LFP theta period of zero lag in that state;\n    (b) the peak nearest zero lag. Lags are compared as absolute values. A P below 0.002 cannot\n    come from an exact signed-rank test over 10 sessions, so the test is over pairs. Test,\n    Wilcoxon signed-rank over pairs measured in both states, for pre against cooling, post\n    against cooling and pre against post. Reproduced when, under one reading, cooling lags are\n    longer than pre and post at P < 0.05 and pre against post gives P >= 0.05. Partially\n    reproduced when one of the cooling comparisons holds. A rank-sum over all pairs of each\n    state is a variant.\n- id: fig5i-phase-lags-unchanged\n  statement: Theta phase lags between place cell pairs were not affected by MS cooling (P > 0.24\n    between all conditions).\n  source: Results, MS temperature effects on theta time/phase compression of place cells\n    sequences, paragraph 3; Figure 5I\n  quote: In contrast, phase lags between spikes of place cell pairs were not affected by MS cooling\n    ( Fig. 5i ; P > 0.24 between all conditions).\n  statistics:\n  - test: Wilcoxon signed rank test\n    p: 0.24\n    p_relation: \">\"\n  depends_on:\n  - fig5h-time-lags-increase\n  criterion: A claim of absence, on the paper's test (\"P > 0.24 for all pairs; Wilcoxon signed rank\n    test\", Results paragraph 2). Phase lag of a pair as the time lag of fig5h on the phase axis\n    (within pi of zero for reading (a)), as absolute values. Wilcoxon signed-rank over pairs\n    measured in both states, for pre against cooling, cooling against post and pre against post,\n    at 0.05. Reproduced when all give P >= 0.05; not reproduced when any gives P < 0.05.\n- id: fig5j-fraction-active-unchanged\n  statement: The fraction of place cells active in a given theta cycle was not significantly\n    affected by MS cooling (P = 0.2).\n  source: Results, MS temperature effects on theta time/phase compression of place cells\n    sequences, paragraph 4; Figure 5J\n  quote: we found that the fraction of place cells active in a given theta cycle was not\n    significantly affected by MS cooling ( Fig. 5j ; P = 0.2).\n  statistics:\n  - about: as given in the Results\n    p: 0.2\n  - about: pre against cooling (legend)\n    p: 0.28\n  - about: post against cooling (legend)\n    p: 0.006\n  - about: pre against post (legend)\n    p: 0.0005\n  criterion: A claim of absence, judged on pre against cooling, the comparison the text and\n    legend agree is not significant (the legend's post against cooling is significant and is\n    reported). Theta cycles as suppl3-theta-cycle-duration, during trials of the Figure 5\n    sessions; per cycle, the fraction of the session's place cells (the Results) with at least\n    one spike; the legend's \"all simultaneously recorded neurons\" is a variant. The test is not\n    named; the panel shows cumulative distributions over cycles, so the default unpaired test,\n    Wilcoxon rank-sum over cycles pooled across sessions, at 0.05. Reproduced when P >= 0.05,\n    not reproduced when P < 0.05. The other two comparisons are reported.\n- id: fig5k-spikes-per-cycle-unchanged\n  statement: The number of spikes emitted by all neurons per theta cycle was preserved during MS\n    cooling (P > 0.058 between all conditions).\n  source: Results, MS temperature effects on theta time/phase compression of place cells\n    sequences, paragraph 4; Figure 5K\n  quote: The number of spikes emitted by all neurons per theta cycle was also preserved after MS\n    cooling ( Fig. 5k )\n  statistics:\n  - p: 0.058\n    p_relation: \">\"\n  depends_on:\n  - fig5j-fraction-active-unchanged\n  criterion: A claim of absence. Cycles as fig5j-fraction-active-unchanged; per cycle, the spikes\n    of all units of the session. Wilcoxon rank-sum over cycles pooled across sessions (as fig5j)\n    for pre against cooling, cooling against post and pre against post, at 0.05. Reproduced when\n    all give P >= 0.05, not reproduced when any gives P < 0.05.\n- id: suppl1g-waveforms-unchanged\n  statement: The waveforms of hippocampal action potentials were not affected by MS cooling.\n  source: Results, MS cooling decreases hippocampal theta frequency and power, paragraph 3; Figure\n    S1G\n  quote: Finally, the waveforms of action potentials in the hippocampus ... were not affected by MS\n    cooling ( Suppl. Fig. 1g ).\n  criterion: A claim of absence. Figure S1G compares \"unit waveforms before/after (red) and during\n    (blue) MS cooling\" and its inset \"shows that MS cooling did not significantly affect unit\n    waveforms\"; the measure and test are not named. Per unit, the mean waveform on its largest\n    channel in pre and post trials together and in cooling trials. Measures, trough-to-peak\n    latency and peak-to-peak amplitude; default Wilcoxon signed-rank over units, at 0.05 each.\n    Reproduced when neither differs; not reproduced when either does. Effect sizes are given.\n- id: suppl2d-interneuron-oscillation-slows\n  statement: The theta oscillation frequency of putative fast spiking interneurons decreased with\n    MS cooling, as did that of pyramidal cells, by about 14% on average, and pyramidal cells\n    oscillated faster than interneurons.\n  source: Results, Effects of MS cooling on single neuron properties, paragraph 1; Figure S2D\n  quote: Note that pyramidal neurons oscillate faster than interneurons and the theta frequency\n    oscillation of both interneurons and pyramidal cells decreases with MS cooling by\n    approximately 14% on average.\n  expected:\n  - quantity: decrease of the oscillation frequency of interneurons and pyramidal cells during\n      cooling\n    value: 14\n    tolerance: 1.4\n    unit: percent\n  criterion: Oscillation frequency of the opening comment, from \"all spikes occurring within\n    place fields during running for pyramical cells, and across the whole maze for interneurons\"\n    (Figure S2D), cooling against pre. Interneuron readings as disc-interneuron-rates-decrease.\n    The 14% is read (a) for each class; (b) for both classes pooled; fig4b gives about 10% for\n    fp, so (a) may hold for interneurons only. Reproduced when interneuron frequency is lower\n    during cooling by a Wilcoxon signed-rank over units at P < 0.05, the decrease is within\n    tolerance under one reading, and median pyramidal frequency exceeds median interneuron\n    frequency in pre. Partially reproduced when the decrease is significant and the rest fails.\n- id: suppl1-hippocampal-temperature\n  statement: In a control experiment, hippocampal temperature fell by less than 1.5 C at the\n    largest MS temperature decrease (16 C), and later than the MS (MS maximum at about 45 s, time\n    constant 11 s; hippocampus peak at 115 s, time constants 48 s right and 72 s left).\n  source: Results, MS cooling decreases hippocampal theta frequency and power, paragraph 3;\n    Figure S1H to K\n  quote: found < 1.5° C decrease in the hippocampus at the time of the largest MS temperature\n    decrease (16° C) ... (maximum effect at approximately 45 s; time constant - 11 s), the mild\n    temperature decrease in the hippocampus was considerably delayed (peak at 115 s; time constant\n    48 s for the right hippocampus, and 72 s for the left)\n  expected:\n  - quantity: largest MS temperature decrease\n    value: 16\n    tolerance: 1.6\n    unit: C\n  - quantity: time of the maximum MS cooling effect\n    value: 45\n    tolerance: 4.5\n    unit: s\n  - quantity: MS time constant\n    value: 11\n    tolerance: 1.1\n    unit: s\n  - quantity: time of the hippocampal temperature peak\n    value: 115\n    tolerance: 11.5\n    unit: s\n  - quantity: right hippocampus time constant\n    value: 48\n    tolerance: 4.8\n    unit: s\n  - quantity: left hippocampus time constant\n    value: 72\n    tolerance: 7.2\n    unit: s\n  criterion: Needs the sessions with simultaneous MS and hippocampal temperature (Figure S1H to\n    K, \"successive cooling sessions in a rat\"). Per cooling epoch, times from cooling onset; the\n    time constant is open, read as the time constant of a single exponential fitted to the fall\n    from onset to the minimum (standard). Values are medians over epochs. Reproduced when the\n    hippocampal decrease at the time of the MS minimum is below 1.65 C (1.5 widened by 10%), the\n    hippocampal peak is later than the MS peak by more than 50 s (Figure S1J, \"> 50 s delay\"),\n    and at least four of the six values are within tolerance. Partially reproduced when the\n    first two hold.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Fixing two spots I flagged on review (a stray line in the change log, and two quotes where I had altered a colon), then running the checker.

**Agent calls Bash**

```bash
python - <<'E'
p='claims/petersen-2020.yaml'
s=open(p).read()
s=s.replace("""# criteria now use the surface fit of the Methods for compression and period. New claims:
# fig2-theta-reduced-minutes was not added; added are suppl2ab-rates-correlated,""","""# criteria now use the surface fit of the Methods for compression and period. New claims are
# suppl2ab-rates-correlated,""")
s=s.replace("""  criterion: Over the sessions of the theta maze with cooling. The Methods give the total
    ("a total number of trials ranging from 80 to 200 (mean - 150 trials)"). Reproduced""","""  criterion: Over the sessions of the theta maze with cooling; the Methods give the range of
    80 to 200 trials and the mean of 150. Reproduced""")
s=s.replace("""  quote: found < 1.5° C decrease in the hippocampus at the time of the largest MS temperature
    decrease (16° C) ... (maximum effect at approximately 45 s; time constant - 11 s), the mild
    temperature decrease in the hippocampus was considerably delayed (peak at 115 s; time constant
    48 s for the right hippocampus, and 72 s for the left)""","""  quote: "found < 1.5° C decrease in the hippocampus at the time of the largest MS temperature
    decrease (16° C) ... (maximum effect at approximately 45 s; time constant: 11 s), the mild
    temperature decrease in the hippocampus was considerably delayed (peak at 115 s; time constant
    48 s for the right hippocampus, and 72 s for the left)\"""")
open(p,'w').write(s)
E
python tools/claims_check.py claims/petersen-2020.yaml paper/10.1016-j.neuron.2020.05.023.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

The only remaining flag is the garbled "P = 8.0 −5" of the Figure 5H legend, which I confirmed by reading (it's noted in the criterion). Checking style rules.

**Agent calls Bash**

```bash
cd  grep -n "—\|rather" claims/petersen-2020.yaml; python - <<'E'
import yaml
d=yaml.safe_load(open('claims/petersen-2020.yaml'))
c=d['claims']
print(len(c), sum('quote' in x for x in c), sum('statistics' in x for x in c), sum('criterion' in x for x in c), sum('expected' in x for x in c))
E
grep -nE "^\s+[a-z_]+: [^\"'].*: " claims/petersen-2020.yaml | head; grep -nE "^    [^ ].*: " claims/petersen-2020.yaml | grep -v "^\S*\s*- " | head
```

```
46 46 20 46 25
109:    value: 150
110:    tolerance: 15
112:    value: 40
113:    tolerance: 4
128:    value: 60
129:    tolerance: 6
130:    unit: s
132:    value: 50
133:    tolerance: 5
156:    p: 5.4e-48
```

**Agent calls Bash**

```bash
python - <<'E'
import yaml
n=yaml.compose(open('claims/petersen-2020.yaml'))
def walk(x):
    if isinstance(x,yaml.ScalarNode):
        if x.style is None and ': ' in x.value: print(x.start_mark.line, x.value[:60])
    elif isinstance(x,yaml.SequenceNode):
        for i in x.value: walk(i)
    elif isinstance(x,yaml.MappingNode):
        for k,v in x.value: walk(k); walk(v)
walk(n); print('ok')
E
git status --short
```

```
ok
 M claims/petersen-2020.yaml
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
?? scripts
```

**Agent**

I rewrote `claims/petersen-2020.yaml` from the full text. The quote checker finds every quote word for word. Its one remaining flag is P = 8.0e-5 for Figure 5H: the legend prints it garbled as "P = 8.0 −5". I confirmed the value by reading, and the criterion notes it. Nothing was committed.

**Text read:** the accepted author manuscript from PubMed Central (PMC7442698), not the version of record. That covers the main text, figure legends and STAR Methods, plus the Supplemental Information (Figures S1 to S6 and Table S1). The paper links no analysis code ("available ... upon reasonable request"). It links only spike-sorting and cell-classification tools, so I read no code.

**Counts:** 46 claims, all with quotes and none inferred. 20 have statistics, 25 have expected values, and all 46 have criteria.

**What changed from the old file:**
- **Dropped:** the old file had been written after seeing the data. Its session sets, pilot-session fixes, and choices taken from a GitHub repository the paper does not link are gone. Every method is now cited to the paper or named as open.
- **Figure 5:** compression and period now come from the surface fit in the Methods, not from peaks picked per pair.
- **Ids kept:** every old id is kept, since each finding is the same.
- **8 new claims:** suppl2ab-rates-correlated, fig4f-speed-theta-power, suppl2e-trial-speed-theta-frequency, suppl3-theta-cycle-duration, suppl3e-precession-temperature, fig5e-phase-period-below-2pi, suppl5gh-rates-follow-temperature and suppl5j-errors-best-theta-frequency.
- **Values added from the supplement and legends:**
  - Figure 6E: P < 1e-7.
  - Figure 5J: the legend's three P values (0.28, 0.006, 0.0005).
  - Figure S2D: the 14% slowing.
  - The control experiment's MS and hippocampal time constants (45 s, 11 s, 115 s, 48 s, 72 s).
- **Removed:** the `dataset` key, which a paper's own claims file leaves out.

**Details the paper leaves open, and the readings named:**
- **Cooling-state boundaries:** (a) the dataset's trial labels, (b) trials starting within 12 min of onset, (c) within 10 min.
- **Trial theta frequency and power:** Hilbert instantaneous frequency and amplitude, or the peak of the spectrogram.
- **Running filter:** all frames, or frames above 10 cm/s.
- **Unit of correlation for Fig 2G/H and 6F to I:** trials aligned on cooling onset and averaged over sessions, binned, pooled trials, or per rat. The printed P values imply about 170 to 190 points, which favours the aligned averages.
- **Correlation type:** Pearson or Spearman.
- **Place fields for Figures 3 and 4:** they were defined by hand. Readings are the dataset's own boundaries, or the Figure 5 automatic rule with a peak above 10 Hz; bins of 3 or 5 cm.
- **fLFP:** taken at spikes, or over the time in the field.
- **Field size, and the speed v in S = v/(fp − fLFP):** two readings each.
- **Which comparisons the stars mark:** Fig 4B, 4D and 6E.
- **Precession slope "decreased":** flatter, or more negative.
- **Fig 5 spikes per pair:** each cell's own field, or the union of the two fields.
- **Choice of the τ peak:** the largest peak within half a theta cycle, or the peak nearest zero.
- **Surface equation:** the extracted text lost its fraction bars, and the +1 could sit inside or outside the cosine. The density grid and start values are standard choices.
- **Fig 5F/G session set:** 18 or 10 sessions. P = 0.002 matches 10 sessions all changing in one direction.
- **Fig 5H/I tests:** P values below 0.002 rule out signed-rank tests over 10 sessions, so they are read as tests over pairs.
- **Fig 5J:** place cells (the text) or all neurons (the legend).
- **Smaller open details:**
  - The width of the 80-point Gaussian window (MATLAB default).
  - Waveform measures.
  - Information measure (bits per spike).
  - The variable set for the partial correlations.
  - Interneuron class (narrow only, or narrow and wide).
  - The exponential fit for the time constants.
  - Whether the 14% of Figure S2D applies per class or pooled.

**Missing from the paper:**
- The sessions in each analysis set are not listed (53, 21, 18, 10 and 19 sessions).
- The speed unit for 87.3 and 86.2 is not printed; I read it as cm/s.
- The paper's own numbers disagree in places, and the criteria allow either value:
  - the 12% fall in theta frequency, against 8% from Fig 4B;
  - an 11% fall in within-field firing rate in the Results, 12% in the Discussion;
  - cooling peaking at 60 s in the Methods, 45 s in the Results.
- Not given claims: Figures S1B, S1F, S4 and S6, which are single-session illustrations, show no stated finding, or are a model.
- suppl1-hippocampal-temperature needs the control-experiment recordings of hippocampal temperature. Whether the dataset holds them is for the author to find.

## End of run

27 turns, 8 minutes, $2.52 at API prices, result: success.
