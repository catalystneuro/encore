# mansvelder-2026 · claims · run 45034624634

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls paper/; cat claims/fouke-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md; ls -la paper/
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
3	Version: `pilot-18`. Record this version in the attempt's provenance.
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

**Agent calls Read**

```json
{
 "file_path": "claims/fouke-2025.yaml"
}
```

```
1	# Claims for Fouke, He, Loring & Naumann (2025) on dandiset 001453.
2	# Source: the accepted author manuscript in PubMed Central (PMC12218792), full text, read
3	# from its Results, figure legends and STAR Methods. The version of record is not open access.
4	#
5	# When these criteria were written, the author had seen the data check only: the file list,
6	# subject metadata, frame rates, units, trial structure and stimulus codes of every file, and
7	# the extent of positions. No claim's analysis had been run. The author had also read the
8	# outputs printed in the paper's own analysis notebook (Fig1-S1.ipynb, GitLab commit 33a5c29),
9	# which include per-stimulus median speeds and angular velocities and its statistics.
10	#
11	# The dandiset holds only the freely swimming tracking data of Figure 1 and Figure S1. Its
12	# stimulus codes 0 to 20 carry no names. The names come from the paper's code and from the
13	# stimulus software's protocol file (see stimulus-code-link), so the claims that need them
14	# use outside data and depend on that claim.
15	#
16	# Method choices fixed here, from the paper's Fig1-S1.ipynb where the Methods are silent: a
17	# trial is one stim_index; tracked frames only; positions smoothed with a Savitzky-Golay filter
18	# (21 frames, order 2); trials rejected when the absolute cumulative heading change exceeds
19	# 1000 degrees in the first 10 s or 2000 degrees in the first 35 s, or the mean speed exceeds
20	# 100 mm/s; measures taken from 3 s to 35 s after the first frame (the 3 s stationary phase is
[... 302 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.21203-rs.3.rs-11136357-v1.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.21203-rs.3.rs-11136357-v1.txt",
 "offset": 691,
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Main text, Methods and legends read through Fig. 7. Checking what the rest of the text file holds (supplement?).

**Agent calls Bash**

```bash
cd paper; sed -n 1390,1500p *.txt; grep -n -i "supplement\|Table S\|Fig. S[0-9] |\|^Fig\.\|^Figure\|^Table" *.txt | sed -n 1,200p | awk -F: '$1>1390'
```

```
model. Voltage traces in response to hyperpolarizing current injections (a) and 
logarithmic chirp stimulus (0.4 - 40 Hz; 65 s) (b) with corresponding impedance 
profiles (c). Peak resonance frequency (fres) (d) and strength (Q) (e) values are 
depicted for each model.  
f-j FS interneuron morphological features varied in dendritic size and complexity (left 
panel). Plotted are corresponding voltage responses to hyperpolarizing current 
injections (middle panel) and logarithmic chirp stimuli (0.4 - 40 Hz; 65 s) (right panel) 
and corresponding impedance profiles (g). fres (h), Q (i), and 3 dB cutoff frequency (j) 
values are depicted for each model. 
 
 
 

 
Fig. 8 | From subthreshold to firing rate resonance 
a Experimental protocol.  
b-c Voltage responses of a non-resonant (b) and a strongly resonant (c) interneuron 
to 1, 5, and 10 Hz sinusoidal stimuli (150 pA and 130 pA, respectively). Insets: 1 Hz 
and 5 Hz stimuli rheobase injections overlaid for comparison. 
d-g Noisy signal detection protocol. Peristimulus histograms depict trial-averaged 
[... 107 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1500,1560p paper/*.txt; which pdftotext; python -c "import fitz" 2>&1; python -c "import pypdf" 2>&1
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -a -o "/Count [0-9]*" paper/*.pdf | sort | uniq -c; tail -5 paper/*.txt; pip list 2>/dev/null | grep -i -E "pdf|mupdf|poppler"
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.21203-rs.3.rs-11136357-v1.supp-Supplementary_Information.pdf",
 "pages": "44-56"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && pip install --quiet --target ./pylib pypdf 2>&1 | tail -2; ls pylib | head
```

```
pypdf
pypdf-7.1.1.dist-info
Shell cwd was reset to
```

**Agent calls Bash**

```bash
PYTHONPATH=$TMPDIR/pylib python -c "
import pypdf
r=pypdf.PdfReader('paper/10.21203-rs.3.rs-11136357-v1.supp-Supplementary_Information.pdf')
out=open('$TMPDIR/supp.txt','w')
for i,p in enumerate(r.pages):
    t=p.extract_text() or ''
    out.write(f'\n=== PAGE {i+1} ===\n'+t)
    print(i+1, len(t), t[:80].replace('\n',' | '))
"
```

Result: not kept, because it reads the paper's text.

**Agent**

The supplement PDF has Table S3 (statistics, pages 38 to 52) and Table S5 (model parameters) beyond where the text file was cut; I extracted it with pypdf to read it.

**Agent calls Bash**

```bash
awk '/=== PAGE 38 ===/,0' $TMPDIR/supp.txt | tr '\n' ' ' | sed 's/ | / /g; s/  */ /g' | fold -w 4000
```

```
=== PAGE 38 === Supplementary Table 3. Statistical tests Pan el DV Independ ent Variable Statistical test Sample size Coefficien ts of determina tion (Pseudo-R Square) Term Group Median/Mean Test statistic p-value Figu re 2B fres Human v Mouse Two-sample Kolmogorov- Smirnov Human (n=297), Mouse (n=248) D = 0.276 p = 1.32e-09 Q D = 0.274 p = 2.0843e-09 Figu re 2C Resonan t proportio n Human Observed v Mouse Expected Chi-square test Human (n=297), Mouse (n=248) χ² (1) = 43.05 p=5.3457e-11 Figu re 2D human obs = [45, 99]; exp (mouse) = [13.2, 130.8] LAMP5: χ² (1) = 84.34 p=4.1654e-20 human obs = [15, 45] exp (mouse) = [1.22, 58.78] VIP: χ² (1) =158.20 p=2.7942e-36 human obs = [34, 44] exp (mouse) = [10.83, 67.17] PV: χ² (1) =57.53 p=3.3261e-14 human obs = [3, 12] exp (mouse) = [2.09, 12.91] SST: χ² (1) =0.46 p=0.49914 Figu re 2E fres Species x Subclass Linear Mixed- Effects (LME) models (Fixed: Species, Subclass, Vm; Random: Donor) n=286 (92 human donors); n=245 (137 mice) Marginal: 0.187; Condition al: 0.365 Interce pt F(1, 521.81) = 10.62 p = 0.001 Namin g F(3, 390.247) = 17.63 p = 9.8234E-11 Specie s F(1, 189.5) = 10.34 p = 0.002 Namin g * Specie s F(3, 385.8) = 4.24 p = 0.006 Vm F(1, 522) = 0.568 p = 0.451 Human v Mouse Post-hoc Mann- Whitney U test LAMP5: n = 144 human; n = 120 mouse MdnH = 1.09; MdnM = 1.15 U = 7717.00 p = 0.133 VIP: n = 60 human; n = 49 mouse MdnH = 0.95; MdnM = 0.40 U = 756.50 p = 0.00000293579 6592 PV: n = 78 human; n = 36 mouse MdnH = 2.18; MdnM = 1.30 U = 925.00 p = 0.003 SST: n = 15 human; n = 43 mouse MdnH = 0.40; MdnM = 0.40 U = 301.50 p = 0.701 Figu re 2F f3 dB Species x Subclass Linear Mixed- Effects (LME) models n=286 (92 human donors); n=245 (137 mice) Marginal: 0.406; Interce pt F(1, 521.87) = 17.87 p = 0.00002794407 3682 === PAGE 39 === (Fixed: Species, Subclass, Vm; Random: Donor) Condition al: 0.559 Namin g F(3, 378.09) = 65.99 p = 2.4669E-34 Specie s F(1, 186.20) = 37.16 p = 6.1254E-9 Namin g * Specie s F(3, 384.02) = 13.97 p = 1
[... 5 more lines not kept]
```

**Agent**

Now the paper's code and the registry entries for this paper.

**Agent calls Bash**

```bash
cat papers/datasets/mansvelder-2026.yaml 2>/dev/null; grep -n -A3 "mansvelder" papers/keys.yaml; ls claims | head -50; cd $TMPDIR && git clone --quiet https://github.com/nsham2/Shamugia_et_al_2026 code 2>&1 | tail -3; cd code 2>/dev/null && git log -1 --format="%H %cd" && find . -path ./.git -prune -o -type f -print | head -100
```

```
Exit code 1
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
paper: doi:10.21203/rs.3.rs-11136357/v1
title: Ion Channels and Morphology Drive Widespread Resonance in Human Cortical Interneurons
datasets:
- archive: dandi
  id: '000630'
  relation: reuses
295:  10.21203/rs.3.rs-11136357/v1: mansvelder-2026
296-  10.21203/rs.3.rs-11447300/v1: yang-2026
297-  10.21203/rs.3.rs-2587250/v1: raicevic-2023
298-  10.22002/d1.1991: sun-2021
alasfour-2024.yaml
amjad-2025.yaml
andrews-2024.yaml
armstrong-2026.yaml
asari-2009.yaml
ashworth-2025.yaml
athalye-2023.yaml
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s -o /dev/null -w "%{http_code}\n" https://github.com/nsham2/Shamugia_et_al_2026; curl -s https://api.github.com/users/nsham2/repos | grep -E '"(full_name|private)"' | head; curl -s "https://api.dandiarchive.org/api/dandisets/000630/" | python -c "import json,sys; d=json.load(sys.stdin); print(d.get('draft_version',{}).get('name')); print(d.get('most_recent_published_version',{}))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s "https://api.dandiarchive.org/api/dandisets/000630/versions/0.230915.2257/info/" | python -c "
import json,sys; d=json.load(sys.stdin)['metadata']
print(d.get('description')); print(d.get('assetsSummary',{}).get('numberOfSubjects'), d.get('assetsSummary',{}).get('species'), d.get('assetsSummary',{}).get('approach'))
for r in d.get('relatedResource',[]): print(r)"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
sed -n 1,200p tools/claims_check.py | grep -n -i -E "key|field|allowed|schema|data|kind|required" | head -60; grep -l "not public\|404\|could not be read\|not available" claims/*.yaml | head
```

```
5:Validates the file against schemas/claims.schema.json, checks every quote word for word
18:import unicodedata
25:from entry import _plain, schema  # noqa: E402
35:    s = unicodedata.normalize("NFKC", html.unescape(s))
82:    for err in schema("claims").iter_errors(_plain(doc)):
83:        print("SCHEMA", "/".join(str(x) for x in err.path) or "(top level)", err.message)
claims/alasfour-2024.yaml
claims/armstrong-2026.yaml
claims/ashworth-2025.yaml
claims/athalye-2023.yaml
claims/bakalar-2023.yaml
claims/bennett-2024.yaml
claims/bouchard-2013.yaml
claims/buccino-2020.yaml
claims/burman-2023.yaml
claims/calvigioni-2023.yaml
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"; head -40 claims/chartrand-2023.yaml
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
[... 221 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1)); print(json.dumps(s['properties'].get('checks',{}),indent=1)[:800])"; sed -n 40,140p claims/chartrand-2023.yaml
```

```
{
 "expected": {
  "type": "object",
  "additionalProperties": false,
  "required": [
   "quantity",
   "value"
  ],
  "properties": {
   "quantity": {
    "type": "string"
   },
   "value": {
    "type": "number"
   },
   "tolerance": {
    "type": "number",
    "minimum": 0
   },
   "unit": {
[... 224 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -B2 -A2 "where:" claims/*.yaml | grep -i -E "model|dataverse|modeldb|simulat" | head -10; grep -n -i "simulation\|model" docs/protocol.md | sed -n 1,30p
```

```
claims/andrews-2024.yaml-176-    Simulation directory (model code, rerun)
claims/andrews-2024.yaml-177-  criterion: Run Simulation/simulation.py as published (NEST 3.4, NESTML, 1000 granule and 12
claims/brudner-2026.yaml-199-    Dataverse deposit (doi:10.60600/YU/590UBV) holds it; the paper's training and test arrays were
claims/brudner-2026.yaml-258-  criterion: Motion-only models of fig2b-smooth-auc and fig2c-complex-auc refitted with delays tau
claims/brudner-2026.yaml-259-    of 1 to 15 frames (SI, Logistic regression models). In the smooth plume Fig. S2C shows the AUC
claims/brudner-2026.yaml-276-    Dataverse deposit (doi:10.60600/YU/590UBV) holds it
claims/brudner-2026.yaml-353-    the model trained in the complex plume
claims/brudner-2026.yaml-437-    simulation code and trained networks are not in the paper's repository
claims/buccino-2024.yaml-194-    alejoe91/multimodalfitting at commit 24e8e61, cell_models/<cell>/morphology_corrected.swc
claims/buccino-2024.yaml-202-    (estimated using a 270 ms step). For our groundtruth model, the rheobase current was 150 pA
168:paper relies on outside data (a model, a reference dataset, measurements of
421:  runs many small model fits, limit linear-algebra threads to one.
521:  data. One session of four, a substituted model, a threshold the paper does
591:- **`provenance`**: who is accountable, and for an agent the harness, model
```

**Agent calls Bash**

```bash
sed -n 425,445p claims/brudner-2026.yaml; sed -n 165,185p claims/andrews-2024.yaml
```

```
quote: In the smooth-plume, agents using the augmented strategy with the smooth plume-trained dense
    network significantly outperformed agents using the wind-only strategy ... However, agents using
    the augmented strategy with plume-inappropriate computations ... performed worse than agents
    using the wind-only strategy
  statistics:
  - about: every pairwise comparison of success rate within each plume
    test: z-test of proportions
    p: 0.001
    p_relation: "<"
    n: 10,000 trajectories per condition
  data: with_inputs
  where: smooth plume from Dryad doi:10.5061/dryad.g27mq71; complex plume in the dandiset; the
    simulation code and trained networks are not in the paper's repository
  depends_on:
  - fig3ij-dnm-specialization
  expected:
  - quantity: success rate, smooth plume, wind only
    value: 0.176
    tolerance: 0.018
  - quantity: success rate, smooth plume, smooth-trained network
[... 22 more lines not kept]
```

**Agent**

I've read the main text, Methods, legends and the full supplement (via pypdf extraction). Checking one statistic before drafting: how the overall χ² in Fig. 2c was computed.

**Agent calls Bash**

```bash
python -c "
from scipy.stats import chi2_contingency, chisquare
for nm in (268,248):
  for rm in (round(0.093*nm),):
    t=[[97,200],[rm,nm-rm]]
    for c in (True,False):
      r=chi2_contingency(t,correction=c); print(nm,rm,c,round(r[0],2),r[1])
# goodness-of-fit overall
print(chisquare([97,200],[297*0.093,297*0.907]))
# culture 60.8% of 543? of 262
for n in (262,268,536,543): k=round(0.608*n); print(n,k, chisquare([k,n-k],[n*97/297,n*200/297]), chi2_contingency([[k,n-k],[97,200]],correction=False)[0])
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    from scipy.stats import chi2_contingency, chisquare
ModuleNotFoundError: No module named 'scipy'
```

**Agent calls Bash**

```bash
python -c "
def c2(t,yates=False):
  R=[sum(r) for r in t];C=[sum(c) for c in zip(*t)];N=sum(R);s=0
  for i in range(2):
    for j in range(2):
      e=R[i]*C[j]/N;d=abs(t[i][j]-e)-(0.5 if yates else 0);s+=d*d/e
  return round(s,2)
for nm in (268,248):
  rm=round(0.093*nm); print(nm,rm,c2([[97,200],[rm,nm-rm]]),c2([[97,200],[rm,nm-rm]],True))
for n in (262,268,536,543):
  k=round(0.608*n); e=n*97/297; print(n,k,round((k-e)**2/e+((n-k)-(n-e))**2/(n-e),2), c2([[k,n-k],[97,200]]), c2([[k,n-k],[97,200]],True))
"
```

```
268 25 45.3 43.93
248 23 43.05 41.7
262 159 93.58 44.05 42.93
268 163 96.64 44.97 43.85
536 326 193.27 60.64 59.52
543 330 195.14 60.71 59.59
```

**Agent calls Bash**

```bash
cd $TMPDIR && git clone --quiet https://github.com/AllenInstitute/ipfx ipfx 2>&1 | tail -2; cd ipfx && git log -1 --format="%h %cd" && git tag | tail -5; grep -rn -i "lowess\|def .*chirp\|def sag\|def estimate_sag\|def input_resistance" --include=*.py ipfx | head -30
```

```
2197d76 Tue Nov 10 22:01:56 2026 +0100
v2.0.0
v2.0.1
v2.1.0
v2.1.1
v2.1.2
ipfx/bin/run_chirp_fv_extraction.py:100:def run_chirp_feature_vector_extraction(output_dir, output_code, include_failed_cells,
ipfx/subthresh_features.py:131:def sag(t, v, i, start, end, peak_width=0.005, baseline_interval=0.03):
ipfx/subthresh_features.py:152:def input_resistance(t_set, i_set, v_set, start, end, baseline_interval=0.1):
ipfx/x_to_nwb/hr_nodes.py:184:def getChirpKind(byte):
ipfx/chirp.py:9:def extract_chirp_feature_vector(data_set, chirp_sweep_numbers):
ipfx/chirp.py:28:def divide_chirps_by_stimulus(sweep_set):
ipfx/chirp.py:40:def feature_vectors_chirp(chirp_sweeps, min_freq=0.2, max_freq=40.):
ipfx/chirp.py:51:def chirp_amp_phase(sweep_set, start=0.6, end=20.6, down_rate=2000,
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/ipfx && git checkout -q v2.0.0 && git log -1 --format="%h %cd" && sed -n 125,185p ipfx/subthresh_features.py && cat ipfx/chirp.py | head -120; ls ipfx/feature_extractors* 2>/dev/null; grep -rn "chirp" --include=*.py -l ipfx | head
```

```
Encountered 1 file that should have been a pointer, but wasn't:
	tests/data/nwb/Ctgf-T2A-dgCre;Ai14-495723.05.02.01.nwb
1ddc0e5 Mon Oct 28 14:48:55 2024 -0700

    a, inv_tau, y0 = fit_membrane_time_constant(t, v, fit_start, fit_end)

    return 1. / inv_tau


def sag(t, v, i, start, end, peak_width=0.005, baseline_interval=0.03):
    """Calculate the sag in a hyperpolarizing voltage response.

    Parameters
    ----------
    peak_width : window width to get more robust peak estimate in sec (default 0.005)

    Returns
    -------
    sag : fraction that membrane potential relaxes back to baseline
    """
[... 169 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/ipfx && grep -n -i "sag\|-100\|input_resistance" ipfx/stimulus_protocol_analysis.py | head -30
```

```
115:    SAG_TARGET = -100.
130:        extra_sweep_feature_names = ['peak_deflect','stim_amp','v_baseline','sag']
184:        sags = subthreshold_sweep_features["sag"]
185:        sag_eval_levels = np.array([ v[0] for v in subthreshold_sweep_features["peak_deflect"] ])
186:        closest_index = np.argmin(np.abs(sag_eval_levels - self.SAG_TARGET))
188:        features["sag"] = sags.values[closest_index]
189:        features["vm_for_sag"] = sag_eval_levels[closest_index]
213:        features["input_resistance"] = subf.input_resistance(calc_subthresh_ss.t,
Shell cwd was reset to
```

**Agent**

I have what I need. Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/mansvelder-2026.yaml",
 "content": "# Claims for Shamugia, Weiler, ... Goriounova & Mansvelder (2026), \"Ion Channels and Morphology\n# Drive Widespread Resonance in Human Cortical Interneurons\", Research Square preprint\n# doi:10.21203/rs.3.rs-11136357/v1, tested on dandiset 000630.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"),\n# 2026-11-22, protocol pilot-18 as stated in docs/protocol.md (Reader).\n#\n# Text read. The preprint, version 1 (posted 2026-10-12), as text\n# (paper/10.21203-rs.3.rs-11136357-v1.txt): main text, Methods, Quantification and Statistical\n# Analysis, and the legends of Figures 1 to 8. The supplement\n# (paper/10.21203-rs.3.rs-11136357-v1.supp-Supplementary_Information.pdf, 56 pages) is in the\n# text file only up to Supplementary Table 2b; the text file is cut there. The rest of the PDF\n# (Supplementary Table 3, statistical tests, pages 38 to 52; Table 4, the donors of the blocker\n# experiments, page 53; Table 5, model parameters, pages 54 to 55; the end of the Fig. S6\n# legend, page 56) was read from the PDF's own text layer (extracted with pypdf 7.1.1), since no\n# page could be rendered. Statistics and medians taken from Table S3 cite it; they cannot be\n# quoted, as the checker reads the text file only. No figure was opened (the main-text PDF is\n# not under paper/, and the supplement PDF could not be rendered), so the Fig. 3b schematic of\n# sag ratio and input resistance was not seen.\n#\n# Code read. The paper's code is given as github.com/nsham2/Shamugia_et_al_2026 (key resources\n# table; \"Original code will be made available at\" the same address under Open Access data and\n# code Availability). On 2026-11-22 that address returned HTTP 404 and the user nsham2 had no\n# public repository of that name, so no analysis code was read. The software the Methods name\n# for feature extraction, IPFX (key resources table, v2.0.0), was read at tag v2.0.0 (commit\n# 1ddc0e5): subthresh_features.sag ((v_peak - v_steady) / (v_peak - v_baseline), peak averaged\n# over 5 ms, baseline and steady state over 30 ms), the long-square analysis that reports the\n# sag of the hyperpolarizing sweep whose peak deflection is closest to -100 mV\n# (stimulus_protocol_analysis.py, SAG_TARGET), subthresh_features.input_resistance (least-squares\n# slope of peak deflection against current over the hyperpolarizing sweeps), and\n# chirp.chirp_amp_phase (chirp sweeps averaged, downsampled to 2 kHz, FFT over 0.6 to 20.6 s,\n# |Z| = |FFT(V)/FFT(I)| kept from 0.2 to 40 Hz, no smoothing). IPFX is cited, not the paper's\n# own code, so it is used only for details the Methods leave open, as a named reading.\n#\n# Data the paper used (Results, first section; Methods; Tables S1 to S4). Patch-seq\n# recordings of human and mouse cortical GABAergic interneurons: 1085 human interneurons from\n# 259 subjects (542 acute from 170 donors, 543 in organotypic slice culture from 89 donors) and\n# 619 acute mouse interneurons from 293 mice (the Methods say 224 donors and 292 mice). Most\n# human data are from Lee, Dalley et al. 2023 (ref. 2) and Chartrand et al. 2023 (ref. 27,\n# cited by the DOI of this dandiset); 21 new patients (12 at the Allen Institute, 9 at VU\n# Amsterdam). Table S1 lists every human donor with its dataset (\"Chartrand\", \"AcuteLDPublished\",\n# \"PublishedLD_Cultured\" and others), area, disease, sex, age and hemisphere; Table S2 lists the\n# mice and their cell specimen IDs and Cre lines. Human tissue from temporal, frontal, parietal\n# and occipital cortex resected for epilepsy or tumour. Subclasses LAMP5 (LAMP5/PAX6/Other), VIP,\n# PV and SST, from the MTG taxonomy with Patch-seq updates (SST FRZB counted as PV); mouse\n# subclasses from transcriptomic alignment or Cre line. Measures per cell: the response to a\n# chirp (constant amplitude, logarithmic sweep 0.4 to 40 Hz over 20 s, about +/- 5 mV, cell\n# biased to -65 mV), giving the impedance profile, peak resonance frequency fres, 3 dB cutoff\n# f3dB and resonance strength Q = Zmax/Z0; sag ratio and input resistance from hyperpolarizing\n# steps; baseline membrane potential Vm; pia-soma distance; total dendritic length for\n# reconstructed cells; Patch-seq gene expression (CPM). A resonant cell has fres > 1 Hz and\n# Q > 1.05. Chirp samples: 297 human acute (LAMP5 144, VIP 60, PV 78, SST 15) and 248 mouse\n# (LAMP5 120, VIP 49, PV 36, SST 43; the Fig. 2b legend says 268), 268 human cultured (LAMP5 21,\n# VIP 28, PV 125, SST 94, Fig. 5f). Also: ZD7288 (10 uM) wash-in on seven human interneurons\n# (Table S4 lists 8 cells exposed to ZD7288 from 5 donors) and 13 mouse cells from 9 mice; Allen\n# Brain Map single-nucleus SMART-seq (human MTG 2018, 4164 nuclei from 8 donors; mouse VISp and\n# ALM 2018, 10534 cells from 210 mice); and NEURON models of a fast-spiking PV interneuron\n# adapted from Wilbers et al. 2023 (DataverseNL doi:10.34894/TONOHA), parameters in Table S5.\n#\n# Where the data are. This dandiset (\"Human L1 patch-seq electrophysiology\", version\n# 0.230915.2257, 53 subjects, human only) holds the NWB electrophysiology of Chartrand et al.\n# 2023, which is a part of this paper's human acute sample (layer 1 interneurons, mostly of the\n# LAMP5 subclass). It holds no mouse, cultured or blocker recordings, no transcriptomes and no\n# morphologies. This paper's per-cell subclass assignment, Vm, pia-soma distance and gene\n# expression are not given with the paper; claims that need subclass labels only are\n# `with_labels`, claims that need other per-cell data or other recordings are `with_inputs`.\n# The paper says \"Most of the data used in this paper is already open source\" (refs 2 and 27)\n# and \"The remaining data will be made available upon request\"; it names no archive for the\n# mouse recordings, the cultured recordings, the Lee et al. 2023 recordings or the Patch-seq\n# transcriptomes. The new human recordings (including the ZD7288 experiments) are not public.\n# The Allen Brain Map reference data and the base model are public (`elsewhere`).\n#\n# Open details, and the readings named for each (criteria refer to these).\n#  - O1, chirp analysis. The Methods give the FFT ratio, LOWESS smoothing, fres at Zmax, f3dB\n#    where Z falls to Zmax/sqrt(2), and Q = Zmax/Z0, \"Z0\" being \"the impedance at the lowest\n#    frequency\" (Results, first section). They do not give the LOWESS fraction for recordings,\n#    the FFT window, the frequency range searched, or which side of the peak f3dB is taken on.\n#    Readings: (a) IPFX v2.0.0 chirp_amp_phase (sweeps averaged, as Fig. 1a says \"From an\n#    averaged CHIRP sweep\"), then LOWESS with frac 0.04 (the value the Methods give for the\n#    model chirp), Z0 at the lowest frequency kept, Zmax searched over the kept range, f3dB the\n#    frequency above the peak where the smoothed Z first falls below Zmax/sqrt(2); (b) as (a)\n#    with the profile restricted to the stimulus band 0.4 to 40 Hz. The paper's per-cell values\n#    are not public, so neither reading can be checked against them.\n#  - O2, sag ratio. Not defined in the text; Fig. 3b shows a schematic that was not seen. The\n#    representative traces use -100 pA (Fig. 5a), -110 pA (Fig. 5f) and -150 pA (Fig. S3i).\n#    Readings: (a) IPFX v2.0.0 sag on the hyperpolarizing long square whose peak deflection is\n#    closest to -100 mV; (b) the same formula on the -100 pA step, or the nearest step to it.\n#  - O3, input resistance. Not defined in the text (Fig. 3b schematic not seen). Readings: (a)\n#    IPFX v2.0.0 input_resistance over the hyperpolarizing long squares; (b) steady-state\n#    deflection over current for the step used in O2(b).\n#  - O4, Vm covariate. \"baseline membrane potential differences (Vm)\" (Quantification and\n#    Statistical Analysis). Readings: (a) the mean pre-stimulus membrane potential of the chirp\n#    sweeps; (b) the resting potential IPFX reports for the cell. A model without Vm is shown as\n#    a variant.\n#  - O5, mixed models. Type III Wald F-tests with Satterthwaite degrees of freedom, random\n#    intercept for donor, run in SPSS or Python (which for which is not said). Readings: (a)\n#    REML linear mixed model with Satterthwaite F-tests (SPSS MIXED, or lmerTest); (b)\n#    statsmodels MixedLM with Wald tests on the same terms. The paper confirmed its models with\n#    generalized estimating equations (exchangeable correlation within donor is not stated; use\n#    it, a standard choice), shown as a variant. Post-hoc species or preparation contrasts are\n#    two-sided Mann-Whitney U tests per subclass, uncorrected (no correction is stated).\n#  - O6, chi-square tests of proportions. The Methods say expected counts for human acute cells\n#    came from the mouse counts, and for cultured cells from the acute counts (goodness of fit).\n#    Table S3's per-subclass values (Fig. 2d) are reproduced by that goodness-of-fit test, but\n#    its overall values (Fig. 2c, 43.05 with 297 human and 248 mouse cells; Fig. 5i, 44.98 with\n#    268 cultured and 297 acute cells) are reproduced by a 2x2 Pearson test without continuity\n#    correction (checked by hand from the counts). Readings: (a) goodness of fit against the\n#    reference group's proportion; (b) 2x2 Pearson test without correction.\n#  - O7, ZD7288 sample. The text says seven human interneurons; Table S4 lists 8 exposed to\n#    ZD7288. With n = 7 an exact two-sided Wilcoxon signed-rank test cannot give p = 0.004 (its\n#    floor is 0.016), while 9 cells can; p = 0.031 is the floor for 6 cells. So the cells per\n#    measure differ from seven and are not stated. Readings: (a) all cells with both a baseline\n#    and a ZD7288 value for the measure; (b) the cells with all four measures.\n#  - O8, gene-resonance correlations. Pearson correlations on cells with CPM > 1, over \"a\n#    subset of prevalent genes\", BH-FDR per preparation. Table S3 lists the acute family: 10\n#    genes (KCNJ16, HCN1, CACNA1A, KCNQ3, SCN8A, KCNQ5, KCNH7, SCN1A, KCNQ2, CACNA1G) by 2\n#    measures (Q, fres). The scale of expression is not stated. Readings: (a) CPM; (b)\n#    log(CPM + 1).\n#  - O9, Fig. 4b regression. The legend says \"Fixed: pia-soma distance\", Table S3 says \"Fixed:\n#    TDL\" with an intercept of 1632.017. Readings: (a) TDL on pia-soma distance; (b) pia-soma\n#    distance on TDL. Judged on the sign and p of the slope.\n#  - O10, text and Table S3 disagree in places; the criteria name both values where it matters.\n#    Fig. 2c chi-square 42.76 (text) against 43.05 (table); mouse chirp n 268 (Fig. 2b legend)\n#    against 248 (table and Fig. 2e counts); Fig. 2d SST p = 0.544 (text) against 0.499\n#    (table); Fig. 2g VIP p < 0.001 (text) against 0.002 (table); Fig. 3e sag by subclass p =\n#    0.035 (text) against \"0.35\" (table, F(3, 254.894) = 2.912, which gives about 0.035); Fig.\n#    6c p-values (text) against FDR-corrected values (table, 0.001, 0.038, 0.044, 0.044); Fig. 5l\n#    \"did not differ\" (text) against VIP p = .046 and PV p = .031 (table); the acute medians of\n#    Fig. 5j (table) are those of Fig. 2e assigned to other subclasses.\nschema_version: 2\npaper: doi:10.21203/rs.3.rs-11136357/v1\nclaims:\n- id: sample-size\n  statement: The dataset comprises 1085 human interneurons from 259 subjects (542 acute from 170\n    donors, 543 cultured from 89 donors) and 619 acutely recorded mouse interneurons from 293\n    mice.\n  source: Results, Human interneurons show widespread and stronger resonance, paragraph 2; Fig. 1b\n  quote: In total, our dataset comprised 1085 human interneurons from 259 subjects (542 acute from\n    170 donors; 543 cultured from 89 donors; Table S1, Fig. S1a-b) and 619 acutely recorded mouse\n    interneurons from 293 mice\n  data: with_labels\n  expected:\n  - quantity: human acute interneurons\n    value: 542\n    tolerance: 54.2\n  - quantity: human acute donors\n    value: 170\n    tolerance: 17\n  criterion: The dandiset holds only part of the human acute sample (Chartrand et al. 2023, layer\n    1), so it cannot reach these totals. Tested as a link to the paper's tables. The dandiset's\n    subjects are matched to the donors of Table S1 by donor name, and the count of Table S1\n    donors with dataset \"Chartrand\" is compared with the dandiset's subjects. Reproduced when\n    every dandiset subject is a Table S1 donor; the counts of matched donors and of dandiset\n    cells with a chirp sweep are reported. The totals above are recorded as the paper's and are\n    not tested on the dandiset.\n- id: fig2b-human-higher-fres-q\n  statement: Human cortical interneurons have higher peak resonance frequencies and resonance\n    strengths than mouse interneurons (Kolmogorov-Smirnov tests, p < 0.001 each).\n  source: Results, Human interneurons show widespread and stronger resonance, paragraph 3; Fig. 2b\n  quote: Human cortical interneurons had higher peak resonance frequencies (fres:  p < 0.001),\n    resonance strengths (Q\n  statistics:\n  - about: fres, human against mouse\n    test: two-sample Kolmogorov-Smirnov\n    statistic: D = 0.276\n    p: 1.32e-09\n    n: 297 human and 248 mouse interneurons (Table S3; the Fig. 2b legend says 268 mouse)\n  - about: Q, human against mouse\n    test: two-sample Kolmogorov-Smirnov\n    statistic: D = 0.274\n    p: 2.0843e-09\n    n: 297 human and 248 mouse interneurons\n  data: with_inputs\n  criterion: fres and Q per cell from the chirp (O1, each reading). Two-sample two-sided\n    Kolmogorov-Smirnov tests, human acute against mouse (Quantification and Statistical\n    Analysis). Reproduced when both tests give p < 0.001 and the human median exceeds the\n    mouse median for both measures. The dandiset holds only human layer 1 cells; mouse chirp\n    data are an outside input the paper does not locate.\n- id: fig2c-resonant-proportion\n  statement: A larger proportion of human than mouse interneurons are resonant (fres > 1 Hz and\n    Q > 1.05), 32.7% against 9.3%.\n  source: Results, Human interneurons show widespread and stronger resonance, paragraph 3; Fig. 2c\n  quote: proportions of resonant cells (fres> 1Hz and ... Q > 1.05) compared to mouse cortical\n    interneurons (32.7% in human vs 9.3% in ... mouse\n  statistics:\n  - test: chi-square test\n    statistic: χ² (1) = 42.76 (text); χ² (1) = 43.05 (Table S3)\n    p: 0.001\n    p_relation: \"<\"\n    n: 297 human and 248 mouse interneurons (Table S3)\n  data: with_inputs\n  expected:\n  - quantity: resonant fraction, human acute interneurons\n    value: 32.7\n    tolerance: 3.27\n    unit: \"%\"\n  - quantity: resonant fraction, mouse interneurons\n    value: 9.3\n    tolerance: 0.93\n    unit: \"%\"\n  criterion: A cell is resonant when fres > 1 Hz and Q > 1.05 (Results; Quantification and\n    Statistical Analysis), with fres and Q under each reading of O1. Proportions over the cells\n    with a chirp; the chi-square test under both readings of O6. Reproduced when both fractions\n    are within tolerance and the test gives p < 0.001. Table S3's counts (97 of 297 human\n    resonant) are the check of the human fraction.\n- id: fig2d-subclass-proportion\n  statement: Human LAMP5, VIP and PV interneurons are more often resonant than their mouse\n    counterparts (p < 0.001 each).\n  source: Results, Human interneurons show widespread and stronger resonance, paragraph 3; Fig. 2d\n  quote: human LAMP5 (p < 0.001), VIP (p < 0.001), and ... PV interneurons (p < 0.001) were more\n    often resonant than their mouse counterparts\n  statistics:\n  - about: LAMP5, human observed against mouse-expected counts\n    test: chi-square test\n    statistic: χ² (1) = 84.34\n    p: 4.1654e-20\n    n: 144 human LAMP5 cells, 45 resonant\n  - about: VIP\n    test: chi-square test\n    statistic: χ² (1) = 158.20\n    p: 2.7942e-36\n    n: 60 human VIP cells, 15 resonant\n  - about: PV\n    test: chi-square test\n    statistic: χ² (1) = 57.53\n    p: 3.3261e-14\n    n: 78 human PV cells, 34 resonant\n  data: with_inputs\n  expected:\n  - quantity: resonant fraction, human LAMP5\n    value: 31.25\n    tolerance: 3.125\n    unit: \"%\"\n  - quantity: resonant fraction, human VIP\n    value: 25.0\n    tolerance: 2.5\n    unit: \"%\"\n  - quantity: resonant fraction, human PV\n    value: 43.6\n    tolerance: 4.36\n    unit: \"%\"\n  criterion: Fractions from Table S3's observed counts (45 of 144, 15 of 60, 34 of 78; no\n    sentence gives them). Resonance as in fig2c-resonant-proportion; per subclass the\n    goodness-of-fit chi-square of human counts against counts expected from the mouse fraction\n    of that subclass (O6 reading a, which reproduces Table S3's values). Reproduced when the\n    three fractions are within tolerance and each test gives p < 0.001 with the human fraction\n    higher.\n- id: fig2d-sst-similar\n  statement: SST interneurons show similar fractions of resonant cells in human and mouse.\n  source: Results, Human interneurons show widespread and stronger resonance, paragraph 3; Fig. 2d\n  quote: In contrast, SST (p = 0.544) interneurons exhibited similar fractions of resonant cells\n    between species\n  statistics:\n  - test: chi-square test\n    statistic: χ² (1) = 0.46 (Table S3)\n    p: 0.544\n    n: 15 human SST cells, 3 resonant; mouse-expected 2.09\n  data: with_inputs\n  criterion: A claim of absence, judged on the paper's test, the goodness-of-fit chi-square of\n    the human SST counts against counts expected from the mouse SST fraction, at p < 0.05.\n    Reproduced when that test gives p >= 0.05; the two fractions are reported either way. Table\n    S3 prints p = 0.499 for the same test (O10).\n- id: fig2d-pv-highest\n  statement: Among human interneuron subclasses, PV cells have the highest proportion of resonant\n    cells.\n  source: Fig. 2 title and Fig. 2d; Abstract\n  quote: A high proportion of resonant cells among human PV interneurons\n  data: with_labels\n  criterion: Resonance as in fig2c-resonant-proportion. Reproduced when the human PV resonant\n    fraction exceeds those of LAMP5, VIP and SST (Table S3 gives 43.6% against 31.3%, 25.0% and\n    20.0%). The paper reports no test of this ordering.\n- id: figs2a-stringent-criteria\n  statement: Human interneurons are more often resonant than mouse interneurons also under the\n    stricter criteria fres > 1 Hz and Q > 1.1 or Q > 1.2.\n  source: Results, Human interneurons show widespread and stronger resonance, paragraph 3; Fig. S2a\n  quote: Human interneurons consistently exhibited higher resonance prevalence compared to mouse\n    across a range of increasingly stringent resonance criteria\n  data: with_inputs\n  criterion: Fractions of cells with fres > 1 Hz and Q above 1.1, and above 1.2 (O1 readings).\n    Reproduced when the human fraction exceeds the mouse fraction at both thresholds. The paper\n    reports no test.\n- id: fig2e-fres-species-subclass\n  statement: Species differences in peak resonance frequency depend on subclass (species by\n    subclass interaction, p = 0.006); human PV and VIP interneurons have higher fres than mouse.\n  source: Results, Human interneurons show widespread and stronger resonance, paragraph 4; Fig. 2e\n  quote: A linear mixed-effects model revealed species differences in ... peak resonance frequency\n    that were qualified by subclass (p = 0.006; Fig. 2e). ... human PV (p = 0.003) and VIP (p <\n    0.001) interneurons ... had significantly higher peak resonance frequencies than their mouse\n    counterparts\n  statistics:\n  - about: species by subclass interaction\n    test: linear mixed-effects model, Type III Wald F-test\n    statistic: F(3, 385.8) = 4.24\n    p: 0.006\n    n: 286 human cells from 92 donors; 245 mouse cells from 137 mice\n  - about: PV, human against mouse\n    test: Mann-Whitney U\n    statistic: U = 925.00\n    p: 0.003\n    n: 78 human, 36 mouse\n  - about: VIP, human against mouse\n    test: Mann-Whitney U\n    statistic: U = 756.50\n    p: 2.936e-06\n    n: 60 human, 49 mouse\n  data: with_inputs\n  expected:\n  - quantity: median fres, human PV\n    value: 2.18\n    tolerance: 0.218\n    unit: Hz\n  - quantity: median fres, mouse PV\n    value: 1.30\n    tolerance: 0.13\n    unit: Hz\n  - quantity: median fres, human VIP\n    value: 0.95\n    tolerance: 0.095\n    unit: Hz\n  - quantity: median fres, mouse VIP\n    value: 0.40\n    tolerance: 0.04\n    unit: Hz\n  criterion: Medians from Table S3. fres under O1. The mixed model has species, subclass, their\n    interaction and Vm (O4) as fixed effects and a random intercept for donor (Methods; Fig. 2e\n    legend), tested under O5. Reproduced when the interaction has p < 0.05, the PV and VIP\n    Mann-Whitney tests give p < 0.05 with human higher, and the four medians are within\n    tolerance; partially reproduced when the tests hold but a median does not.\n- id: fig2e-lamp5-sst-fres-similar\n  statement: Human and mouse LAMP5 and SST interneurons do not differ in peak resonance frequency.\n  source: Results, Human interneurons show widespread and stronger resonance, paragraph 4; Fig. 2e\n  quote: human and mouse LAMP5 (p = 0.133) and SST (p = 0.701) ... interneurons did not differ in\n    peak resonance frequency\n  statistics:\n  - about: LAMP5\n    test: Mann-Whitney U\n    statistic: U = 7717.00\n    p: 0.133\n    n: 144 human, 120 mouse\n  - about: SST\n    test: Mann-Whitney U\n    statistic: U = 301.50\n    p: 0.701\n    n: 15 human, 43 mouse\n  data: with_inputs\n  criterion: A claim of absence, judged on the paper's test, two-sided Mann-Whitney U per\n    subclass at p < 0.05, fres under O1. Reproduced when neither test gives p < 0.05; the\n    medians are reported either way (Table S3, LAMP5 1.09 against 1.15 Hz, SST 0.40 against\n    0.40 Hz).\n- id: fig2f-f3db-species-subclass\n  statement: Species differences in 3 dB cutoff frequency are subclass-specific (p < 0.001);\n    human LAMP5, PV and SST interneurons have lower 3 dB cutoffs than mouse, while VIP cells are\n    similar.\n  source: Results, Human interneurons show widespread and stronger resonance, paragraph 4; Fig. 2f\n  quote: the species ... differences in 3dB cutoff frequency were subclass-specific (p < 0.001;\n    Fig. 2f)\n  statistics:\n  - about: species by subclass interaction\n    test: linear mixed-effects model, Type III Wald F-test\n    statistic: F(3, 384.02) = 13.97\n    p: 1.1644e-08\n    n: 286 human cells from 92 donors; 245 mouse cells from 137 mice\n  - about: LAMP5\n    test: Mann-Whitney U\n    statistic: U = 15460.00\n    p: 0.001\n    p_relation: \"<\"\n  - about: PV\n    test: Mann-Whitney U\n    statistic: U = 2332.50\n    p: 1.5109e-08\n  - about: SST\n    test: Mann-Whitney U\n    statistic: U = 454.00\n    p: 0.020\n  - about: VIP\n    test: Mann-Whitney U\n    statistic: U = 1600.50\n    p: 0.427\n  data: with_inputs\n  expected:\n  - quantity: median f3dB, human LAMP5\n    value: 7.36\n    tolerance: 0.736\n    unit: Hz\n  - quantity: median f3dB, mouse LAMP5\n    value: 15.20\n    tolerance: 1.52\n    unit: Hz\n  - quantity: median f3dB, human PV\n    value: 13.03\n    tolerance: 1.303\n    unit: Hz\n  - quantity: median f3dB, mouse PV\n    value: 20.86\n    tolerance: 2.086\n    unit: Hz\n  criterion: Medians from Table S3. f3dB under O1; model as in fig2e-fres-species-subclass (O4,\n    O5). Reproduced when the interaction has p < 0.05, LAMP5, PV and SST each show human lower\n    at p < 0.05, VIP does not differ at p < 0.05, and the medians are within tolerance;\n    partially reproduced when the interaction and two of the three lower subclasses hold.\n- id: fig2g-q-species-subclass\n  statement: Human PV, VIP and LAMP5 interneurons, but not SST, show higher resonance strength\n    than mouse counterparts.\n  source: Results, Human interneurons show widespread and stronger resonance, paragraph 4; Fig. 2g\n  quote: human ... PV (p < 0.001), VIP (p < 0.001), and LAMP5 (p < 0.001), but not SST (p = 0.419),\n    ... interneurons showed higher resonance strengths compared to mouse counterparts\n  statistics:\n  - about: species main effect (the interaction is not significant, F(3, 378.27) = 1.58, p =\n      .194)\n    test: linear mixed-effects model, Type III Wald F-test\n    statistic: F(1, 188.00) = 24.31\n    p: 1.79e-06\n    n: 286 human cells from 92 donors; 244 mouse cells from 137 mice\n  - about: PV\n    test: Mann-Whitney U\n    statistic: U = 734.00, z = -4.08\n    p: 4.42e-05\n  - about: VIP\n    test: Mann-Whitney U\n    statistic: U = 960.50, z = -3.10\n    p: 0.002\n  - about: LAMP5\n    test: Mann-Whitney U\n    statistic: U = 6245.50, z = -3.78\n    p: 0.000155\n  - about: SST\n    test: Mann-Whitney U\n    statistic: U = 368.00, z = 0.81\n    p: 0.419\n  data: with_inputs\n  expected:\n  - quantity: median Q, human PV\n    value: 1.04\n    tolerance: 0.004\n  - quantity: median Q, mouse PV\n    value: 1.008\n    tolerance: 0.0008\n  - quantity: median Q, human LAMP5\n    value: 1.013\n    tolerance: 0.0013\n  criterion: Medians from Table S3. Q is a ratio near 1, so the tolerance is 10% of Q - 1, not\n    of Q, which would accept any value from a flat profile. Q under O1. Reproduced when PV,\n    VIP and LAMP5 each show human higher at p < 0.05 by two-sided Mann-Whitney U, SST does not\n    differ at p < 0.05, and the species effect of the mixed model (O4, O5) has p < 0.05;\n    partially reproduced when two of the three subclasses hold. The medians are reported\n    against their tolerances.\n- id: fig3c-sag-species\n  statement: Species differences in sag ratio are subclass-specific (p < 0.001), with higher sag\n    ratios in human LAMP5, VIP, PV and SST interneurons than in mouse.\n  source: Results, Voltage sag ratio and input resistance relate to resonance properties in human\n    interneurons, paragraph 1; Fig. 3c\n  quote: Sag ratios were higher in human LAMP5 (p < 0.001), VIP (p < ... 0.001), PV (p < 0.001),\n    and SST (p = 0.001) interneurons compared to mouse ... counterparts\n  statistics:\n  - about: species by subclass interaction\n    test: linear mixed-effects model, Type III Wald F-test\n    statistic: F(3, 848.14) = 8.33\n    p: 1.84e-05\n    n: 541 human cells from 130 donors; 619 mouse cells from 289 mice\n  - about: LAMP5\n    test: Mann-Whitney U\n    statistic: U = 24305.00, z = -13.39\n    p: 0.0001\n    p_relation: \"<\"\n    n: 276 human, 435 mouse\n  - about: VIP\n    test: Mann-Whitney U\n    statistic: U = 1678.00, z = -8.96\n    p: 0.0001\n    p_relation: \"<\"\n    n: 114 human, 101 mouse\n  - about: PV\n    test: Mann-Whitney U\n    statistic: U = 1096.00, z = -5.37\n    p: 7.9e-08\n    n: 130 human, 39 mouse\n  - about: SST\n    test: Mann-Whitney U\n    statistic: U = 246.00, z = -3.24\n    p: 0.0012\n    n: 22 human, 44 mouse\n  data: with_inputs\n  expected:\n  - quantity: median sag ratio, human LAMP5\n    value: 0.113\n    tolerance: 0.0113\n  - quantity: median sag ratio, mouse LAMP5\n    value: 0.044\n    tolerance: 0.0044\n  - quantity: median sag ratio, human VIP\n    value: 0.177\n    tolerance: 0.0177\n  - quantity: median sag ratio, human PV\n    value: 0.106\n    tolerance: 0.0106\n  criterion: Medians from Table S3. Sag ratio under O2; model as in fig2e-fres-species-subclass\n    with sag as outcome (O4, O5). Reproduced when the interaction has p < 0.05, all four\n    subclasses show human higher at p < 0.05 by two-sided Mann-Whitney U, and the medians are\n    within tolerance under one reading of O2; partially reproduced when three subclasses hold.\n- id: fig3d-input-resistance-species\n  statement: Species differences in input resistance are subclass-specific (p < 0.001); human\n    LAMP5 and PV interneurons have higher input resistance than mouse, VIP and SST do not differ.\n  source: Results, Voltage sag ratio and input resistance relate to resonance properties in human\n    interneurons, paragraph 1; Fig. 3d\n  quote: human LAMP5 (p < 0.001) and PV (p < 0.001) ... interneurons, but not VIP (p = 0.312) or\n    SST (p = 0.108) interneurons, had higher input ... resistances compared to mouse counterparts\n  statistics:\n  - about: species by subclass interaction\n    test: linear mixed-effects model, Type III Wald F-test\n    statistic: F(3, 849.85) = 25.64\n    p: 6.93e-16\n    n: 541 human cells from 130 donors; 619 mouse cells from 289 mice\n  - about: LAMP5\n    test: Mann-Whitney U\n    statistic: U = 10308.00, z = -18.63\n    p: 0.001\n    p_relation: \"<\"\n  - about: PV\n    test: Mann-Whitney U\n    statistic: U = 1476.00, z = -3.95\n    p: 0.001\n    p_relation: \"<\"\n  - about: VIP\n    test: Mann-Whitney U\n    statistic: U = 6217.00, z = 1.01\n    p: 0.312\n  - about: SST\n    test: Mann-Whitney U\n    statistic: U = 366.00, z = -1.61\n    p: 0.108\n  data: with_inputs\n  expected:\n  - quantity: median input resistance, human LAMP5\n    value: 231.26\n    tolerance: 23.13\n    unit: MOhm\n  - quantity: median input resistance, mouse LAMP5\n    value: 125.87\n    tolerance: 12.59\n    unit: MOhm\n  - quantity: median input resistance, human PV\n    value: 151.45\n    tolerance: 15.15\n    unit: MOhm\n  - quantity: median input resistance, mouse PV\n    value: 112.35\n    tolerance: 11.24\n    unit: MOhm\n  criterion: Medians from Table S3. Input resistance under O3; model as in\n    fig2e-fres-species-subclass (O4, O5). Reproduced when the interaction has p < 0.05, LAMP5 and\n    PV show human higher at p < 0.05, VIP and SST give p >= 0.05, and the medians are within\n    tolerance under one reading of O3.\n- id: fig3eg-human-fres-sag-rin\n  statement: In human interneurons, sag ratio and input resistance predict peak resonance\n    frequency in a subclass-specific way; fres rises with sag ratio in LAMP5 (beta 3.31), VIP\n    (4.79) and PV (6.13) cells and falls with input resistance in LAMP5 (-0.002) and PV (-0.006)\n    cells.\n  source: Results, Voltage sag ratio and input resistance relate to resonance properties in human\n    interneurons, paragraph 2; Fig. 3e and 3g\n  quote: Separate linear mixed-effects models ... per subclass showed positive relationships\n    between sag ratio and peak resonance ... frequency in human LAMP5 (β = 3.31, p < 0.001), VIP\n    (β = 4.79, p < 0.001), and PV ... (β = 6.13, p < 0.001) interneurons (Fig. 3e). Input\n    resistance was negatively related to ... peak resonance frequency in human LAMP5 (β = -0.002,\n    p < 0.001) and PV (β = - ... 0.006, p < 0.001) interneurons\n  statistics:\n  - about: sag by subclass interaction, all human cells\n    test: linear mixed-effects model, Type III Wald F-test\n    statistic: F(3, 254.894) = 2.912\n    p: 0.035\n    n: 287 human cells from 92 donors (LAMP5 135, VIP 59, PV 78, SST 15)\n  - about: input resistance by subclass interaction\n    test: linear mixed-effects model, Type III Wald F-test\n    statistic: F(3, 255.621) = 3.052\n    p: 0.029\n  - about: sag slope, LAMP5\n    test: linear mixed-effects model per subclass\n    statistic: b = 3.305, SE = .633, t(128.068) = 5.220\n    p: 7.03e-07\n  - about: sag slope, VIP\n    test: linear mixed-effects model per subclass\n    statistic: b = 4.788, SE = 1.244, t(51.550) = 3.847\n    p: 0.00033\n  - about: sag slope, PV\n    test: linear mixed-effects model per subclass\n    statistic: b = 6.134, SE = 1.355, t(75) = 4.526\n    p: 2.22e-05\n  - about: input resistance slope, LAMP5\n    test: linear mixed-effects model per subclass\n    statistic: b = -.002, SE = .001, t(131.080) = -3.620\n    p: 0.00042\n  - about: input resistance slope, PV\n    test: linear mixed-effects model per subclass\n    statistic: b = -.006, SE = .002, t(75) = -3.470\n    p: 0.00087\n  data: with_labels\n  expected:\n  - quantity: sag slope, LAMP5\n    value: 3.31\n    tolerance: 0.331\n    unit: Hz per unit sag ratio\n  - quantity: sag slope, VIP\n    value: 4.79\n    tolerance: 0.479\n    unit: Hz per unit sag ratio\n  - quantity: sag slope, PV\n    value: 6.13\n    tolerance: 0.613\n    unit: Hz per unit sag ratio\n  - quantity: input resistance slope, LAMP5\n    value: -0.002\n    tolerance: 0.0002\n    unit: Hz per MOhm\n  - quantity: input resistance slope, PV\n    value: -0.006\n    tolerance: 0.0006\n    unit: Hz per MOhm\n  criterion: Human acute cells with fres, sag and input resistance (O1, O2, O3). Model of fres on\n    sag, input resistance, subclass, sag by subclass and input resistance by subclass, random\n    intercept for donor (Quantification and Statistical Analysis; Fig. 3 legend; no Vm term), and\n    per subclass fres on sag and input resistance with donor intercept, tested under O5.\n    Reproduced when both interactions have p < 0.05, the five per-subclass slopes have the\n    stated sign with p < 0.05, and the slopes are within tolerance; partially reproduced when\n    the signs and p-values hold but a slope does not, or when one interaction misses. Table S3\n    also gives VIP input resistance (p = 0.088) and SST (sag p = 0.393, input resistance p =\n    0.231) as not significant; these are reported.\n- id: fig3fh-mouse-fres\n  statement: In mouse interneurons, sag ratio does not predict peak resonance frequency\n    (p = .113); only input resistance does, with no difference between subclasses.\n  source: Results, Voltage sag ratio and input resistance relate to resonance properties in human\n    interneurons, paragraph 2; Fig. 3f and 3h\n  quote: Sag ratio was not predictive of ... peak resonance frequency among mouse interneurons (p =\n    .113, Fig. 3f) and only ... input resistance was a significant predictor of peak resonance\n    frequency, and this ... effect did not differ between subclasses\n  statistics:\n  - about: sag main effect\n    test: linear mixed-effects model, Type III Wald F-test\n    statistic: F(1, 232.375) = 2.525\n    p: 0.113\n    n: 245 mouse cells from 137 mice (LAMP5 118, VIP 49, PV 36, SST 42)\n  - about: input resistance main effect\n    test: linear mixed-effects model, Type III Wald F-test\n    statistic: F(1, 221.377) = 5.263\n    p: 0.023\n  - about: input resistance by subclass interaction\n    test: linear mixed-effects model, Type III Wald F-test\n    statistic: F(3, 216.592) = 0.535\n    p: 0.659\n  data: with_inputs\n  criterion: Model as in fig3eg-human-fres-sag-rin on mouse cells. The absence parts are judged\n    on the paper's test (sag main effect, input resistance by subclass interaction, each at p <\n    0.05). Reproduced when the sag main effect gives p >= 0.05, the input resistance main\n    effect gives p < 0.05, and its interaction with subclass gives p >= 0.05.\n- id: fig3ik-human-q-sag-rin\n  statement: In human interneurons, sag ratio strongly predicts resonance strength (beta 0.47,\n    p < 0.001) with no subclass difference, and input resistance is negatively related to it\n    (beta -0.0001, p = 0.005).\n  source: Results, Voltage sag ratio and input resistance relate to resonance properties in human\n    interneurons, paragraph 3; Fig. 3i and 3k\n  quote: sag ratio was strongly predictive of resonance ... strength among human interneurons (β =\n    .47, p < 0.001), and this effect did not differ ... between subclasses (Fig. 3i).\n    Correspondingly, input resistance was negatively ... related to resonance strength among\n    human interneurons (β = -0.0001, p = 0.005\n  statistics:\n  - about: sag main effect\n    test: linear mixed-effects model, Type III Wald F-test\n    statistic: F(1, 269.086) = 60.275\n    p: 0.001\n    p_relation: \"<\"\n    n: 287 human cells from 92 donors\n  - about: sag by subclass interaction\n    test: linear mixed-effects model, Type III Wald F-test\n    statistic: F(3, 272.054) = 1.801\n    p: 0.147\n  - about: input resistance main effect\n    test: linear mixed-effects model, Type III Wald F-test\n    statistic: F(1, 274.797) = 7.966\n    p: 0.005\n  data: with_labels\n  expected:\n  - quantity: sag slope on Q\n    value: 0.47\n    tolerance: 0.047\n    unit: per unit sag ratio\n  - quantity: input resistance slope on Q\n    value: -0.0001\n    tolerance: 0.00001\n    unit: per MOhm\n  criterion: Model of Q as in fig3eg-human-fres-sag-rin (O1, O2, O3, O5). The slopes are those\n    of sag and input resistance in a model without the non-significant interactions, which the\n    paper does not state; the slopes from the full model are shown as a variant. Reproduced\n    when sag has a positive effect at p < 0.001, its interaction with subclass gives p >= 0.05,\n    input resistance has a negative effect at p < 0.05, and the slopes are within tolerance\n    under one reading; partially reproduced when the tests hold but a slope does not.\n- id: fig3jl-mouse-q-sag-rin\n  statement: In mouse interneurons, sag ratio is only weakly related to resonance strength (beta\n    0.018, p = 0.021) and input resistance is not related to it (p = 0.820).\n  source: Results, Voltage sag ratio and input resistance relate to resonance properties in human\n    interneurons, paragraph 3; Fig. 3j and 3l\n  quote: In mouse interneurons, sag ratio was weakly related to resonance strength (β ... = .018, p\n    = 0.021, Fig. 3j), and input resistance did not relate to resonance strength ... (p = 0.820\n  statistics:\n  - about: sag main effect\n    test: linear mixed-effects model, Type III Wald F-test\n    statistic: F(1, 230.028) = 5.380\n    p: 0.021\n    n: 244 mouse cells from 137 mice\n  - about: input resistance main effect\n    test: linear mixed-effects model, Type III Wald F-test\n    statistic: F(1, 204.982) = 0.052\n    p: 0.82\n  data: with_inputs\n  criterion: Model as in fig3ik-human-q-sag-rin on mouse cells. Reproduced when sag has a\n    positive effect at p < 0.05 and input resistance gives p >= 0.05 (the absence judged on the\n    paper's test); the sag slope is reported against 0.018.\n- id: fig4b-tdl-depth\n  statement: Among reconstructed human interneurons, total dendritic length increases with\n    distance from the pia.\n  source: Results, Resonance dependence on cortical depth locations, paragraph 1; Fig. 4b\n  quote: we found that total dendritic length increased with ... distance from the pia (β = 1.35, p\n    < 0.002, Fig. 4b)\n  statistics:\n  - test: linear mixed-effects model\n    statistic: b = 1.350, SE = .408, t(56.294) = 3.305\n    p: 0.002\n    n: 61 human cells from 28 donors\n  data: with_inputs\n  criterion: Needs morphological reconstructions and pia-soma distances, which the dandiset does\n    not hold. Mixed model with donor intercept, under both readings of O9. Reproduced when the\n    slope is positive with p < 0.05 under the reading the data allow; the slope is reported\n    against 1.35.\n- id: fig4c-human-sag-depth\n  statement: Sag ratio decreases with distance from the pia in human LAMP5, VIP and SST\n    interneurons, but not in PV interneurons.\n  source: Results, Resonance dependence on cortical depth locations, paragraph 2; Fig. 4c\n  quote: sag ratio decreased with larger distance from pia in human ... LAMP5 (p = 0.001), VIP (p =\n    0.008), and SST (p = 0.002) interneurons, whereas it did ... not change in PV (p = .478)\n    interneurons\n  statistics:\n  - about: subclass by pia-soma distance interaction\n    test: linear mixed-effects model, Type III Wald F-test\n    statistic: F(3, 422.347) = 7.962\n    p: 4.0e-05\n    n: LAMP5 218, VIP 107, PV 106, SST 18 human cells from 93 donors\n  - about: LAMP5\n    test: linear mixed-effects model per subclass\n    statistic: F(1, 203.49) = 10.62\n    p: 0.001\n  - about: VIP\n    test: linear mixed-effects model per subclass\n    statistic: F(1, 101.84) = 7.24\n    p: 0.008\n  - about: SST\n    test: linear mixed-effects model per subclass\n    statistic: F(1, 13.65) = 14.58\n    p: 0.002\n  - about: PV\n    test: linear mixed-effects model per subclass\n    statistic: F(1, 84.64) = .51\n    p: 0.478\n  data: with_inputs\n  criterion: Sag under O2, pia-soma distance per cell (an outside input). Model of sag on\n    pia-soma distance, subclass and their interaction with donor intercept, then per subclass\n    sag on distance (Fig. 4 legend; O5). Reproduced when the interaction has p < 0.05, LAMP5,\n    VIP and SST each have a negative slope at p < 0.05 and PV gives p >= 0.05; partially\n    reproduced when two of the three negative slopes hold.\n- id: fig4i-mouse-sag-depth\n  statement: In mouse interneurons sag ratio also decreases with cortical depth, without\n    difference between subclasses.\n  source: Results, Resonance dependence on cortical depth locations, paragraph 2; Fig. 4i\n  quote: An overall decrease in sag ratio ... with cortical depth was also evident in mouse\n    cortical interneurons (p < 0.001) and did ... not vary by subclass (p = 0.185, Fig. 4i)\n  statistics:\n  - about: pia-soma distance main effect\n    test: linear mixed-effects model, Type III Wald F-test\n    statistic: F(1, 469.40) = 12.526\n    p: 0.001\n    p_relation: \"<\"\n    n: LAMP5 391, VIP 90 mouse cells from 228 mice\n  - about: subclass by pia-soma distance interaction\n    test: linear mixed-effects model, Type III Wald F-test\n    statistic: F(1, 473.46) = 1.762\n    p: 0.185\n  data: with_inputs\n  criterion: Model as in fig4c-human-sag-depth on mouse LAMP5 and VIP cells. Reproduced when the\n    distance effect is negative with p < 0.001 and the interaction gives p >= 0.05.\n- id: fig4df-human-no-depth\n  statement: In human interneurons, pia-soma distance does not correlate with input resistance,\n    peak resonance frequency or 3 dB cutoff frequency.\n  source: Results, Resonance dependence on cortical depth locations, paragraph 2; Fig. 4d-f\n  quote: the pia-soma distance in human interneurons did not correlate with input ... resistance,\n    peak resonance, or 3 dB cutoff frequency\n  statistics:\n  - about: input resistance, pia-soma distance main effect\n    test: linear mixed-effects model, Type III Wald F-test\n    statistic: F(1, 417.359) = 2.286\n    p: 0.131\n    n: LAMP5 218, VIP 107, PV 106, SST 18 cells from 93 donors\n  - about: fres, pia-soma distance main effect\n    test: linear mixed-effects model, Type III Wald F-test\n    statistic: F(1, 178.51) = 3.269\n    p: 0.072\n    n: LAMP5 110, VIP 56, PV 57, SST 11 cells from 64 donors\n  - about: f3dB, pia-soma distance main effect\n    test: linear mixed-effects model, Type III Wald F-test\n    statistic: F(1, 169.60) = 0.394\n    p: 0.531\n  data: with_inputs\n  criterion: A claim of absence, judged on the paper's test, the model of each measure on\n    pia-soma distance, subclass and their interaction with donor intercept (Fig. 4 legend; O1,\n    O3, O5), at p < 0.05 for the distance main effect and the interaction (Table S3 gives\n    interactions p = 0.162, .304 and .599). Reproduced when neither term reaches p < 0.05 for\n    any of the three measures; the slopes are reported either way.\n- id: fig4g-human-q-decreases-depth\n  statement: Resonance strength decreases with distance from the pia when all human interneuron\n    subclasses are taken together.\n  source: Results, Resonance dependence on cortical depth locations, paragraph 2; Fig. 4g\n  quote: resonance ... strength even decreased with distance from pia when all interneuron\n    subclasses were ... taken together (p = 0.031, Fig. 4g)\n  statistics:\n  - test: linear mixed-effects model, Type III Wald F-test\n    statistic: F(1, 192.77) = 4.741\n    p: 0.031\n    n: LAMP5 110, VIP 56, PV 57, SST 11 cells from 64 donors\n  data: with_inputs\n  criterion: Model as in fig4df-human-no-depth with Q as outcome. Reproduced when the pia-soma\n    distance effect is negative with p < 0.05.\n- id: figs2-l23-no-depth\n  statement: In a sub-selection of human L2/L3 interneurons, resonance strength and frequency are\n    unrelated to distance from the pia.\n  source: Results, Resonance dependence on cortical depth locations, paragraph 2; Fig. S2b-e\n  quote: Resonance strength and frequency were also ... unrelated to distance from the pia in a\n    sub-selection of L2/L3 human cortical ... interneurons\n  statistics:\n  - about: Q\n    test: linear mixed-effects model, Type III Wald F-test\n    statistic: F(1, 55) = 0.64\n    p: 0.427\n    n: 57 human L2/L3 cells from 23 donors\n  - about: fres\n    test: linear mixed-effects model, Type III Wald F-test\n    statistic: F(1, 53.33) = 1.85\n    p: 0.179\n  data: with_inputs\n  criterion: A claim of absence, judged on the paper's test, the model of Q and of fres on\n    pia-soma distance with donor intercept (Fig. S2 legend), among L2/L3 cells, at p < 0.05.\n    How L2/L3 is assigned (layer label or depth bounds) is not stated; the layer label of each\n    cell is used, a standard choice. Reproduced when neither test gives p < 0.05. Table S3 gives\n    significant depth effects for f3dB (p = 0.008), sag (p = 0.005) and input resistance in this\n    subset, which the text does not claim; they are reported.\n- id: fig4km-mouse-no-depth\n  statement: None of the resonance parameters scale with cortical depth in mouse interneurons.\n  source: Results, Resonance dependence on cortical depth locations, paragraph 2; Fig. 4k-m\n  quote: none of the resonance parameters scaled with ... cortical depth in mouse cortical\n    interneurons (all p > .05, Fig. 4k-m)\n  statistics:\n  - about: fres, pia-soma distance\n    test: linear mixed-effects model, Type III Wald F-test\n    statistic: F(1, 142) = 0.075\n    p: 0.784\n    n: LAMP5 105, VIP 41 mouse cells from 98 mice\n  - about: f3dB, pia-soma distance\n    test: linear mixed-effects model, Type III Wald F-test\n    statistic: F(1, 103.60) = 0.995\n    p: 0.321\n  - about: Q, pia-soma distance\n    test: linear mixed-effects model, Type III Wald F-test\n    statistic: F(1, 140.28) = 1.550\n    p: 0.215\n  data: with_inputs\n  criterion: A claim of absence, judged on the paper's test, the models of fres, f3dB and Q on\n    pia-soma distance, subclass and their interaction with donor intercept, at p < 0.05 for the\n    distance effect and the interaction. Reproduced when none of these reaches p < 0.05.\n- id: fig5be-zd7288-human\n  statement: Blocking HCN channels with ZD7288 in human interneurons increases input resistance,\n    eliminates voltage sag and eliminates resonance (lower fres and Q).\n  source: Results, Ih supports resonance in human interneurons, paragraph 1; Fig. 5a-e\n  quote: Blocking ... HCN channels increased input resistance (p = 0.004; Fig. 5c) and eliminated\n    voltage ... sag (p = 0.004, Fig. 5b) as well as resonance (fres: p = 0.031; Q: p = 0.031\n  statistics:\n  - about: sag ratio, before against after\n    test: Wilcoxon matched-pairs signed rank test\n    p: 0.004\n    n: seven human interneurons (text); see O7\n  - about: input resistance\n    test: Wilcoxon matched-pairs signed rank test\n    p: 0.004\n  - about: fres\n    test: Wilcoxon matched-pairs signed rank test\n    p: 0.031\n  - about: Q\n    test: Wilcoxon matched-pairs signed rank test\n    p: 0.031\n  expected:\n  - quantity: median change in sag ratio\n    value: -0.26\n    tolerance: 0.026\n  - quantity: median change in input resistance\n    value: 74.95\n    tolerance: 7.5\n    unit: MOhm\n  - quantity: median change in fres\n    value: -2.065\n    tolerance: 0.2065\n    unit: Hz\n  criterion: Median changes from Table S3. These are new VU recordings that the paper says are\n    available on request; they are not in the dandiset. Measures at -65 mV before and after 10\n    uM ZD7288 (Methods, Patch-clamp ZD7288 experiments; O1, O2, O3), two-sided Wilcoxon\n    signed-rank tests per measure under both readings of O7. Reproduced when sag and fres fall,\n    input resistance and Q change in the stated direction (Q falls) with p < 0.05 each, and the\n    median changes are within tolerance.\n- id: figs3-zd7288-mouse\n  statement: In mouse cortical interneurons, HCN blockade also reduces sag ratio, resonance\n    strength and frequency measures.\n  source: Results, Ih supports resonance in human interneurons, paragraph 1; Fig. S3l-p\n  quote: HCN channel blockade reduced ... sag ratio, resonance strength and frequency measures\n    (Fig. S3)\n  statistics:\n  - about: sag ratio\n    test: Wilcoxon signed-rank test\n    statistic: V = 83\n    p: 0.010\n    n: 13 paired mouse cells from 9 mice\n  - about: input resistance\n    test: Wilcoxon signed-rank test\n    statistic: V = 16\n    p: 0.043\n  - about: Q\n    test: Wilcoxon signed-rank test\n    statistic: V = 21\n    p: 0.036\n  - about: fres\n    test: Wilcoxon signed-rank test\n    statistic: V = 80\n    p: 0.022\n  - about: f3dB\n    test: Wilcoxon signed-rank test\n    statistic: V = 28\n    p: 0.017\n  data: with_inputs\n  criterion: New mouse recordings (prefrontal cortex), not in the dandiset and not located by the\n    paper. Two-sided Wilcoxon signed-rank tests, baseline against ZD7288 (Fig. S3 legend).\n    Reproduced when sag ratio, Q and fres each fall with p < 0.05.\n- id: fig5g-culture-sag\n  statement: Cultured LAMP5 and PV interneurons have higher sag ratios than acutely recorded ones,\n    while input resistance does not differ between preparations.\n  source: Results, Ih supports resonance in human interneurons, paragraph 2; Fig. 5g-h\n  quote: we observed higher sag ratios in cultured neurons for LAMP5 and PV interneurons\n    (LAMP5: p < 0.001; PV:  p < 0.001). Input resistance did not differ between preparations (p\n    = 0.095, Fig. 5h)\n  statistics:\n  - about: sag, LAMP5, acute against cultured\n    test: Mann-Whitney U\n    statistic: U = 8237.00, Z = 5.03\n    p: 0.001\n    p_relation: \"<\"\n    n: 276 acute, 40 cultured\n  - about: sag, PV\n    test: Mann-Whitney U\n    statistic: U = 31851.00, Z = 12.51\n    p: 0.001\n    p_relation: \"<\"\n    n: 130 acute, 277 cultured\n  - about: input resistance, preparation\n    test: linear mixed-effects model\n    p: 0.095\n    n: 541 acute and 536 cultured cells from 192 donors\n  data: with_inputs\n  expected:\n  - quantity: median sag ratio, cultured LAMP5\n    value: 0.26\n    tolerance: 0.026\n  - quantity: median sag ratio, cultured PV\n    value: 0.28\n    tolerance: 0.028\n  criterion: Medians from Table S3. Cultured recordings (Lee et al. 2023 and new) are not in the\n    dandiset. Sag (O2) by two-sided Mann-Whitney U per subclass; input resistance (O3) in the\n    mixed model of preparation, subclass, their interaction and Vm with donor intercept (Fig. 5\n    legend; O4, O5). Reproduced when LAMP5 and PV sag are higher in culture at p < 0.001, the\n    preparation effect on input resistance gives p >= 0.05 (absence judged on that test), and\n    the medians are within tolerance. Table S3's per-subclass input resistance tests (LAMP5 p =\n    .018) are reported.\n- id: fig5i-culture-proportion\n  statement: A higher proportion of interneurons is resonant in organotypic slice culture than\n    in acute slices (60.8% against 32.7%), in LAMP5, PV and SST interneurons but not VIP.\n  source: Results, Ih supports resonance in human interneurons, paragraph 2; Fig. 5i\n  quote: We found a higher proportion of ... resonant cells among interneurons in organotypic brain\n    slice culture (60.8% in cultured ... vs 32.7% in acute, p < 0.001; Fig. 5i). This was true for\n    LAMP5 (p = 0.002), PV (p < ... 0.001) and SST (p < 0.001) interneurons but not VIP\n    interneurons, which showed ... equal proportions of resonant cells (p = 0.100)\n  statistics:\n  - about: all cells\n    test: chi-square test\n    statistic: χ² (1) = 44.98\n    p: 0.001\n    p_relation: \"<\"\n    n: 268 cultured (Fig. 5f) and 297 acute cells\n  - about: LAMP5\n    test: chi-square test\n    statistic: χ² (1) = 9.19\n    p: 0.002\n  - about: PV\n    test: chi-square test\n    statistic: χ² (1) = 79.76\n    p: 0.001\n    p_relation: \"<\"\n  - about: SST\n    test: chi-square test\n    statistic: χ² (1) = 27.13\n    p: 0.001\n    p_relation: \"<\"\n  - about: VIP\n    test: chi-square test\n    statistic: χ² (1) = 0\n    p: 0.100\n  data: with_inputs\n  expected:\n  - quantity: resonant fraction, cultured\n    value: 60.8\n    tolerance: 6.08\n    unit: \"%\"\n  - quantity: resonant fraction, acute\n    value: 32.7\n    tolerance: 3.27\n    unit: \"%\"\n  criterion: Resonance as in fig2c-resonant-proportion. Overall test under both readings of O6;\n    per subclass the goodness-of-fit chi-square against the acute fraction (O6 reading a).\n    Reproduced when both fractions are within tolerance, the overall test gives p < 0.001,\n    LAMP5, PV and SST are higher in culture at p < 0.05, and VIP gives p >= 0.05 (absence judged\n    on the paper's test). Table S3 prints χ² = 0 with p = 0.100 for VIP, which cannot both hold;\n    the value found is reported.\n- id: fig5jk-culture-fres-q\n  statement: Peak resonance frequency (LAMP5, PV) and resonance strength (LAMP5, PV, SST) are\n    higher in cultured than in acute interneurons.\n  source: Results, Ih supports resonance in human interneurons, paragraph 2; Fig. 5j-k\n  quote: an increase in peak ... resonance frequency (LAMP5: p = 0.007, PV: p < 0.001; Fig. 5j)\n    and strength (LAMP5: ... p = 0.002, PV: p < 0.001; SST: p = 0.023; Fig. 5k) paralleled an\n    increase in sag ratio ... in cultured tissue\n  statistics:\n  - about: fres, LAMP5\n    test: Mann-Whitney U\n    statistic: U = 2061.00, Z = 2.69\n    p: 0.007\n    n: 144 acute, 21 cultured\n  - about: fres, PV\n    test: Mann-Whitney U\n    statistic: U = 6766.50, Z = 4.65\n    p: 3.37e-06\n    n: 78 acute, 125 cultured\n  - about: Q, LAMP5\n    test: Mann-Whitney U\n    statistic: U = 2151.00, Z = 3.13\n    p: 0.002\n  - about: Q, PV\n    test: Mann-Whitney U\n    statistic: U = 7998.00, Z = 7.67\n    p: 1.71e-14\n  - about: Q, SST\n    test: Mann-Whitney U\n    statistic: U = 964.00, Z = 2.28\n    p: 0.023\n    n: 15 acute, 94 cultured\n  data: with_inputs\n  expected:\n  - quantity: median fres, cultured LAMP5\n    value: 2.40\n    tolerance: 0.24\n    unit: Hz\n  - quantity: median Q, cultured PV\n    value: 1.17\n    tolerance: 0.017\n  criterion: Medians from Table S3 (the Q tolerance is 10% of Q - 1, as in\n    fig2g-q-species-subclass). Two-sided Mann-Whitney U per subclass, acute against cultured\n    (Fig. 5 legend; O1). Reproduced when the five comparisons show culture higher at p < 0.05;\n    partially reproduced when four do. Table S3's acute medians for Fig. 5j do not match those of\n    Fig. 2e (O10), so acute medians are not used as targets.\n- id: fig5l-culture-f3db-same\n  statement: The 3 dB cutoff frequency does not differ between acute and cultured interneurons.\n  source: Results, Ih supports resonance in human interneurons, paragraph 2; Fig. 5l\n  quote: the 3 dB cutoff frequency did not differ between ... acute and culture conditions (Fig. 5l)\n  statistics:\n  - about: LAMP5\n    test: Mann-Whitney U\n    statistic: U = 1795.50, Z = 1.3\n    p: 0.166\n  - about: VIP\n    test: Mann-Whitney U\n    statistic: U = 617.00, Z = -2.00\n    p: 0.046\n  - about: PV\n    test: Mann-Whitney U\n    statistic: U = 3995.50, Z = -2.16\n    p: 0.031\n  - about: SST\n    test: Mann-Whitney U\n    statistic: U = 885.50, Z = 1.59\n    p: 0.112\n  data: with_inputs\n  criterion: A claim of absence, judged on the paper's test, two-sided Mann-Whitney U per\n    subclass at p < 0.05 (Fig. 5 legend; O1). Reproduced when no subclass reaches p < 0.05; the\n    medians are reported. The paper's own Table S3 gives p < 0.05 for VIP and PV (O10), so the\n    claim does not hold on the paper's own numbers; this is recorded either way.\n- id: fig6a-hcn1-pex5l-human\n  statement: In Allen Brain Map single-nucleus data, HCN1 and the TRIP8b gene PEX5L are expressed\n    at higher levels in human than in mouse interneurons.\n  source: Results, Voltage-dependent ion channel gene expression associates with resonance,\n    paragraph 1; Fig. 6a\n  quote: with HCN1 showing higher levels ... in human versus mouse interneurons. Additionally, HCN1\n    modulator TRIP8b protein ... RNA readout, PEX5L, levels are elevated in human interneurons\n  statistics:\n  - about: HCN1\n    test: linear mixed-effects model, ln(CPM + 1) ~ species + (1 | donor)\n    statistic: t = 3.09\n    p: 0.002\n    corrected: Benjamini-Hochberg\n    n: 4164 human nuclei from 8 donors, 10534 mouse cells from 210 mice\n  - about: PEX5L\n    test: linear mixed-effects model\n    statistic: t = 13.58\n    p: 1.26e-41\n    corrected: Benjamini-Hochberg\n  data: elsewhere\n  where: Allen Brain Map RNA-Seq (portal.brain-map.org/atlases-and-data/rnaseq), human MTG\n    SMART-seq 2018 and mouse VISp and ALM SMART-seq 2018, as named in Methods, RNA-seq\n  criterion: All GABAergic interneurons, introns and exons, ln(CPM + 1), mixed model with species\n    fixed and donor or animal random intercept, BH over the five genes HCN1 to HCN4 and PEX5L\n    (Methods, RNA-seq). Reproduced when HCN1 and PEX5L are higher in human with BH-adjusted p <\n    0.05.\n- id: fig6b-channel-expression\n  statement: In acute and cultured human slices, all interneuron subclasses express high levels\n    of HCN1, KCNQ3/5 and CACNA1A/G transcripts.\n  source: Results, Voltage-dependent ion channel gene expression associates with resonance,\n    paragraph 3; Fig. 6b and Fig. S4a\n  quote: all interneuron types showed ... high levels of expression of HCN1, KCNQ3/5, and\n    CACNA1A/G gene transcripts\n  data: with_inputs\n  criterion: Needs the Patch-seq transcriptomes, which the dandiset does not hold and the paper\n    does not locate. Per gene and subclass, the fraction of cells with CPM > 1 and the mean CPM\n    (Methods, Patch-seq). \"High\" is not defined; read as the fraction expressing above one half\n    in every subclass for each of the five genes. Reproduced when that holds in acute cells.\n- id: fig6c-gene-resonance-correlation\n  statement: In acute human interneurons, KCNJ16 expression correlates positively with resonance\n    strength and frequency, and HCN1 and CACNA1A expression correlate positively with resonance\n    frequency, after FDR correction.\n  source: Results, Voltage-dependent ion channel gene expression associates with resonance,\n    paragraph 3; Fig. 6c\n  quote: we found significant positive relationships between KCNJ16 and ... resonance strength (n =\n    204, r = 0.28, p < 0.001) as well as resonance frequency (n ... = 204, r = 0.20, p = 0.004) in\n    the acute dataset. HCN1 (N = 240, r = 0.17, p = 0.007) ... and CACNA1A (n = 254, r = 0.16, p =\n    0.009) also positively correlated to resonance ... frequency\n  statistics:\n  - about: KCNJ16 against Q\n    test: Pearson correlation\n    statistic: r = 0.279\n    p: 0.00106\n    corrected: FDR (Table S3; the text gives p < 0.001)\n    n: 204 cells\n  - about: KCNJ16 against fres\n    test: Pearson correlation\n    statistic: r = 0.202\n    p: 0.038\n    corrected: FDR (Table S3; the text gives p = 0.004)\n    n: 204 cells\n  - about: HCN1 against fres\n    test: Pearson correlation\n    statistic: r = 0.174\n    p: 0.044\n    corrected: FDR (Table S3; the text gives p = 0.007)\n    n: 240 cells\n  - about: CACNA1A against fres\n    test: Pearson correlation\n    statistic: r = 0.164\n    p: 0.044\n    corrected: FDR (Table S3; the text gives p = 0.009)\n    n: 254 cells\n  data: with_inputs\n  expected:\n  - quantity: r, KCNJ16 and Q\n    value: 0.28\n    tolerance: 0.028\n  - quantity: r, KCNJ16 and fres\n    value: 0.20\n    tolerance: 0.02\n  - quantity: r, HCN1 and fres\n    value: 0.17\n    tolerance: 0.017\n  - quantity: r, CACNA1A and fres\n    value: 0.16\n    tolerance: 0.016\n  criterion: Needs Patch-seq transcriptomes (not in the dandiset). Pearson correlation of\n    expression with Q and fres over acute cells with CPM > 1 for the gene, BH-FDR over the 20\n    tests of the acute family (O8, both readings of the scale; O1). Reproduced when the four\n    correlations are positive with FDR-adjusted p < 0.05 and within tolerance; partially\n    reproduced when three are.\n- id: figs4-culture-mouse-genes\n  statement: No gene-resonance correlation survives correction in cultured human interneurons;\n    among mouse interneurons only HCN2 is significantly related to resonance.\n  source: Results, Voltage-dependent ion channel gene expression associates with resonance,\n    paragraph 3; Fig. S4a-b\n  quote: None of the correlations survived multiple correction in ... the cultured dataset (Fig.\n    S4a). In contrast, HCN2, but none of the other genes was ... significantly related to resonance\n    among mouse interneurons\n  statistics:\n  - about: mouse, HCN2 against Q\n    test: Pearson correlation\n    statistic: r = 0.265\n    p: 0.015\n    corrected: FDR\n    n: 168 mouse cells\n  data: with_inputs\n  criterion: As in fig6c-gene-resonance-correlation, on cultured human cells (family of Table S3,\n    Fig. S4A) and on mouse cells (Fig. S4B). The cultured part is a claim of absence judged on\n    FDR-adjusted p < 0.05. Reproduced when no cultured correlation reaches FDR p < 0.05 and, in\n    mouse, HCN2 against Q does while no other gene does.\n- id: fig7ae-model-ih\n  statement: In the human PV model, the baseline Ih gives a weak resonance peak (Q = 1.04),\n    removing Ih abolishes it, and doubling Ih raises resonance frequency and strength (Q = 1.09)\n    and lowers input resistance.\n  source: Results, Large human interneurons require increased active properties for resonance,\n    paragraph 1; Fig. 7a-e and Fig. S5a-h\n  quote: The baseline model ... showed a detectable, albeit weak (Q = 1.04), resonance peak in the\n    impedance profile, ... which was absent in the - Ih model (Fig. 7e). Increasing the baseline Ih\n    conductance ... (+ Ih * 2, orange trace) increased the resonance frequency and strength (Q =\n    1.09\n  data: elsewhere\n  where: DataverseNL doi:10.34894/TONOHA (the FS model of Wilbers et al. 2023 that the paper\n    adapted); the adapted model is not deposited and the paper's code address returns 404\n  expected:\n  - quantity: Q, baseline model\n    value: 1.04\n    tolerance: 0.004\n  - quantity: Q, doubled Ih\n    value: 1.09\n    tolerance: 0.009\n  criterion: Model with Table S5's conductances, chirp of 62 s from 0.4 to 40 Hz, dt 0.1, peak\n    deflection within +/- 5 mV, LOWESS frac 0.04 (Methods, CHIRP Experiments). Q tolerances are\n    10% of Q - 1. Reproduced when the -Ih model has no peak above Z0, Q of the baseline and\n    doubled models are within tolerance, and doubling raises fres and lowers input resistance.\n    The adapted model is not public, so this rests on rebuilding it from Table S5.\n- id: fig7-model-ca\n  statement: Adding a low-threshold calcium or M-type potassium conductance to the model raises\n    resonance frequency (5.89 Hz) and strength (Q = 1.25) with little change in sag ratio (0.22)\n    or input resistance (102.42 against 108.45 MOhm).\n  source: Results, Large human interneurons require increased active properties for resonance,\n    paragraph 2; Fig. 7b-e\n  quote: Both the M-type ... potassium and the calcium conductance increased resonance frequency\n    (fres = 5.89, ... Fig. 7d) and resonance strength (Q = 1.25, Fig. 7e), with little change in\n    sag ... ratio\n  data: elsewhere\n  where: DataverseNL doi:10.34894/TONOHA (base model); the calcium (McRory et al. 2001) and M-type\n    channels added are not deposited\n  expected:\n  - quantity: fres, +Ih +Ca model\n    value: 5.89\n    tolerance: 0.589\n    unit: Hz\n  - quantity: Q, +Ih +Ca model\n    value: 1.25\n    tolerance: 0.025\n  - quantity: sag ratio, +Ih and +Ih +Ca models\n    value: 0.22\n    tolerance: 0.022\n  - quantity: input resistance, +Ih model\n    value: 102.42\n    tolerance: 10.24\n    unit: MOhm\n  - quantity: input resistance, +Ih +Ca model\n    value: 108.45\n    tolerance: 10.85\n    unit: MOhm\n  criterion: As in fig7ae-model-ih. The calcium conductance density is not given in Table S5, so\n    it cannot be rebuilt as published; the claim is blocked unless the model is released.\n- id: figs5-model-gpas\n  statement: Varying passive leak conductance in the model changes peak resonance frequency but\n    not resonance strength.\n  source: Results, Large human interneurons require increased active properties for resonance,\n    paragraph 1; Fig. S5i-n\n  quote: we additionally varied the passive ... leak conductance in the baseline model and found an\n    increased peak resonance ... frequency but not resonance strength\n  data: elsewhere\n  where: DataverseNL doi:10.34894/TONOHA (base model)\n  criterion: Baseline model with passive conductance scaled 0.4 to 1.6 times (Fig. S5 legend).\n    Reproduced when fres rises with leak conductance and Q varies by less than its change under\n    doubled Ih (fig7ae-model-ih).\n- id: fig7fj-model-morphology\n  statement: With equal conductance densities, sag ratio and resonance strength increase with\n    morphology size, while 3 dB cutoff and resonance frequencies change with morphology, the human\n    model showing the sharpest resonance profile.\n  source: Results, Large human interneurons require increased active properties for resonance,\n    paragraph 3; Fig. 7f-j\n  quote: We found that the sag ratio and resonance strength increased as the morphology ...\n    increased in size (Fig. 7f, g, i). In contrast, the 3 dB cutoff and resonance frequencies ...\n    decreased (Fig. 7h, j) as the morphology approached the mouse model, with the ... human model\n    showing a sharper resonance profile\n  data: elsewhere\n  where: DataverseNL doi:10.34894/TONOHA (base model); morphologies from Table S5\n  criterion: Three idealized morphologies of Table S5 (reference, human, mouse) with the baseline\n    conductances. The direction of the frequency change is stated two ways in the paper; readings\n    (a) as the Results sentence says, fres and f3dB lower in the mouse than in the human model;\n    (b) as the Discussion says (\"models with larger but less complex human-like morphological\n    features would exhibit lower peak resonance and 3 dB cutoff frequencies\") and the next\n    paragraph implies (higher fres in the mouse model), lower in the human model. Reproduced when\n    sag and Q rise from mouse to reference to human (by size) and f3dB is lowest in the human\n    model, with the frequency ordering reported under both readings.\n- id: figs5-model-normalized-morphology\n  statement: With total conductance normalized across morphologies, the human model still has a\n    sharper impedance peak and the mouse model a higher peak resonance frequency, but resonance\n    strength is no longer higher in the human model.\n  source: Results, Large human interneurons require increased active properties for resonance,\n    paragraph 4; Fig. S6e-k\n  quote: we observed a sharper peak in the impedance ... profile in the human model and a higher\n    peak resonance frequency in the mouse ... model (Fig. S5). However, resonance strength was no\n    longer higher in the human ... model compared to the mouse model\n  data: elsewhere\n  where: DataverseNL doi:10.34894/TONOHA (base model); scaled conductances from Table S5\n  criterion: Dendritic conductances scaled by 0.822 (reference) and 0.428 (human) as in Table S5.\n    \"Sharper\" is read as a lower f3dB. Reproduced when the human model has the lowest f3dB, the\n    mouse model the highest fres, and Q of the human model is not above that of the mouse model.\n- id: fig8bc-firing-resonance\n  statement: The resonant model (+Ih +Ca) is more excitable than the non-resonant model (rheobase\n    130 against 150 pA) and is most excitable at 5 Hz, close to its subthreshold resonance\n    frequency, while the non-resonant model is most excitable at 1 Hz.\n  source: Results, Human resonant morphologies show firing-level resonance, paragraph 1; Fig. 8b-c\n  quote: the resonant cell was most excitable in response to the 5 Hz stimulus (Fig. 8c; 130 pA ...\n    for 5 Hz; 136 pA for 1 Hz), which corresponds approximately to its subthreshold ... resonance\n    frequency\n  data: elsewhere\n  where: DataverseNL doi:10.34894/TONOHA (base model); the resonant model is not deposited\n  expected:\n  - quantity: sinusoidal rheobase, resonant model, 5 Hz\n    value: 130\n    tolerance: 13\n    unit: pA\n  - quantity: sinusoidal rheobase, resonant model, 1 Hz\n    value: 136\n    tolerance: 13.6\n    unit: pA\n  - quantity: sinusoidal rheobase, non-resonant model, 1 Hz\n    value: 150\n    tolerance: 15\n    unit: pA\n  criterion: Rests on fig7-model-ca, whose model cannot be rebuilt from the paper. Reproduced when\n    the values are within tolerance and the resonant model's lowest rheobase is at 5 Hz. The text\n    gives \"5 pA for 5 Hz\" for the non-resonant model, which reads as a typing error; it is not\n    used.\n  depends_on:\n  - fig7-model-ca\n- id: fig8eg-noisy-modulation\n  statement: Under in vivo-like noise, the strongly resonant +Ih +Ca model shows a peak in the\n    normalized modulation index and signal gain that the +Ih and -Ih models lack, and only it\n    fires in phase with a 5 Hz input.\n  source: Results, Human resonant morphologies show firing-level resonance, paragraph 2; Fig. 8d-g\n  quote: The strongly resonating +Ih +Ca2+ model showed a peak in the ... normalized modulation index\n    (Fig. 8e) and the signal gain functions26 (Fig. 8f) which ... was absent in the +Ih and -Ih\n    models\n  data: elsewhere\n  where: DataverseNL doi:10.34894/TONOHA (base model); the resonant model is not deposited\n  criterion: Protocol of Methods, Modulation of firing, and Table S5 (sd, I0, I1, 10 cycles, 10 x\n    f trials, 20 bins per cycle, sine fit). \"Peak\" is read as a maximum of M/R and of gain at an\n    input frequency above 1 Hz. Reproduced when that holds for +Ih +Ca and not for +Ih or -Ih.\n    Rests on fig7-model-ca.\n  depends_on:\n  - fig7-model-ca\n- id: fig8hk-morphology-firing\n  statement: Among resonant morphological models, the human morphology responds most strongly to\n    a 5 Hz input (highest modulation index and signal gain) but fails to follow higher-frequency\n    inputs.\n  source: Results, Human resonant morphologies show firing-level resonance, paragraph 3; Fig. 8h-k\n  quote: the human interneuron morphology ... model showed the strongest response to this input, as\n    reflected by the highest ... modulation index and signal gain amplitude at 5 Hz (Fig. 8i-k)\n  data: elsewhere\n  where: DataverseNL doi:10.34894/TONOHA (base model); the resonant model is not deposited\n  criterion: Inputs of 1 to 50 Hz with noise (Table S5). Reproduced when at 5 Hz the human model\n    has the highest M/R and gain of the three, and its M/R at 50 Hz is the lowest of the three.\n    Rests on fig7-model-ca.\n  depends_on:\n  - fig7-model-ca\n- id: figs1-region-pathology\n  statement: Resonance metrics (fres, Q, 3 dB cutoff) and input resistance do not differ between\n    brain regions of resection or between epilepsy and tumour cases; sag ratio does.\n  source: Results, Human interneurons show widespread and stronger resonance, paragraph 2; Fig.\n    S1e-n\n  quote: The primary resonance metrics did not ... differ between cortical regions of surgical\n    resection (frontal, temporal, parietal, or ... occipital; Fig. S1c, e-i) or donor’s disease\n    type (epilepsy vs tumor; Fig. S1d, j-n)\n  statistics:\n  - about: region, fres\n    test: Kruskal-Wallis\n    statistic: KW = 5.91\n    p: 0.116\n  - about: region, Q\n    test: Kruskal-Wallis\n    statistic: KW = 5.90\n    p: 0.117\n  - about: region, f3dB\n    test: Kruskal-Wallis\n    statistic: KW = 1.34\n    p: 0.719\n  - about: pathology, fres\n    test: Mann-Whitney U\n    statistic: U = 2757\n    p: 0.218\n  - about: pathology, Q\n    test: Mann-Whitney U\n    statistic: U = 2543\n    p: 0.664\n  - about: pathology, f3dB\n    test: Mann-Whitney U\n    statistic: U = 2611\n    p: 0.493\n  - about: region, sag ratio\n    test: Kruskal-Wallis\n    statistic: KW = 19.53\n    p: 0.001\n    p_relation: \"<\"\n  - about: pathology, sag ratio (lower in epilepsy)\n    test: Mann-Whitney U\n    statistic: U = 4845\n    p: 0.001\n    p_relation: \"<\"\n  data: with_labels\n  criterion: Region (lobe) and disease per donor from Table S1. The absence parts are judged on\n    the paper's tests, Kruskal-Wallis across the four lobes and Mann-Whitney U between epilepsy\n    and tumour, at p < 0.05 (Fig. S1 legend; O1). Reproduced when fres, Q and f3dB give p >=\n    0.05 in both tests; sag ratio (O2) is reported. Which cells enter (acute only, or acute and\n    cultured) is not stated; readings (a) acute cells, (b) all human cells.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/mansvelder-2026.yaml paper/10.21203-rs.3.rs-11136357-v1.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -E "^\s+[^#].*\S: " claims/mansvelder-2026.yaml | grep -v -E "^\s*[0-9]+:\s*(- )?[a-z_]+: [^:]*$"
```

```
159:  quote: Human cortical interneurons had higher peak resonance frequencies (fres:  p < 0.001),
878:    voltage ... sag (p = 0.004, Fig. 5b) as well as resonance (fres: p = 0.031; Q: p = 0.031
948:    (LAMP5: p < 0.001; PV:  p < 0.001). Input resistance did not differ between preparations (p
1035:  quote: an increase in peak ... resonance frequency (LAMP5: p = 0.007, PV: p < 0.001; Fig. 5j)
1036:    and strength (LAMP5: ... p = 0.002, PV: p < 0.001; SST: p = 0.023; Fig. 5k) paralleled an
1225:  where: DataverseNL doi:10.34894/TONOHA (the FS model of Wilbers et al. 2023 that the paper
1249:  where: DataverseNL doi:10.34894/TONOHA (base model); the calcium (McRory et al. 2001) and M-type
1280:  where: DataverseNL doi:10.34894/TONOHA (base model)
1295:  where: DataverseNL doi:10.34894/TONOHA (base model); morphologies from Table S5
1314:  where: DataverseNL doi:10.34894/TONOHA (base model); scaled conductances from Table S5
1327:  where: DataverseNL doi:10.34894/TONOHA (base model); the resonant model is not deposited
1356:  where: DataverseNL doi:10.34894/TONOHA (base model); the resonant model is not deposited
1371:  where: DataverseNL doi:10.34894/TONOHA (base model); the resonant model is not deposited
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='claims/mansvelder-2026.yaml'
s=open(p).read()
rep=[
("""  quote: Human cortical interneurons had higher peak resonance frequencies (fres:  p < 0.001),
    resonance strengths (Q
""","""  quote: Human cortical interneurons had higher peak resonance frequencies ... resonance strengths
""","fig2b"),
("""    voltage ... sag (p = 0.004, Fig. 5b) as well as resonance (fres: p = 0.031; Q: p = 0.031
""","""    voltage ... sag (p = 0.004, Fig. 5b) as well as resonance
""","5be"),
("""    (LAMP5: p < 0.001; PV:  p < 0.001). Input resistance did not differ between preparations (p
    = 0.095, Fig. 5h)
""","""    ... Input resistance did not differ between preparations (p = 0.095, Fig. 5h)
""","5g"),
("""  quote: an increase in peak ... resonance frequency (LAMP5: p = 0.007, PV: p < 0.001; Fig. 5j)
    and strength (LAMP5: ... p = 0.002, PV: p < 0.001; SST: p = 0.023; Fig. 5k) paralleled an
    increase in sag ratio ... in cultured tissue
""","""  quote: an increase in peak ... resonance frequency ... and strength ... paralleled an increase in
    sag ratio ... in cultured tissue
""","5jk"),
]
for a,b,n in rep:
    assert s.count(a)==1,n; s=s.replace(a,b)
open(p,'w').write(s)
EOF
python tools/claims_check.py claims/mansvelder-2026.yaml paper/10.21203-rs.3.rs-11136357-v1.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

All 43 quotes pass. The remaining flags are p-values taken from Table S3, which sits past the cut in the text file. Checking how the checker treats them.

**Agent calls Bash**

```bash
sed -n 40,112p tools/claims_check.py
```

```
def flattenings(raw: str) -> list[str]:
    """The text with inline tags removed, with every tag as a space, and both without spaces."""
    tight = norm(re.sub(r"</?[A-Za-z!?][^<>]*>", " ", re.sub(INLINE, "", raw, flags=re.I)))
    loose = norm(re.sub(r"</?[A-Za-z!?][^<>]*>", " ", raw))
    return [tight, loose, tight.replace(" ", ""), loose.replace(" ", "")]


def quote_found(quote: str, texts: list[str]) -> bool:
    fragments = [f for f in (norm(x).strip(" .,;") for x in quote.split("...")) if f]
    for text in texts:
        frags = fragments if " " in text else [f.replace(" ", "") for f in fragments]
        pos = 0
        for f in frags:
            i = text.find(f, pos)
            if i < 0:
                break
            pos = i + len(f)
        else:
            return True
    return False
[... 52 more lines not kept]
```

**Agent**

The checker accepts several text files. I'll run it with my PDF extraction added, to confirm the Table S3 numbers I transcribed (that extraction isn't kept).

**Agent calls Bash**

```bash
python tools/claims_check.py claims/mansvelder-2026.yaml paper/10.21203-rs.3.rs-11136357-v1.txt $TMPDIR/supp.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Remaining flags are rounded forms of Table S3 values (e.g. "0.00000293579 6592" recorded as 2.936e-06); I confirmed each by reading. Now tidying the sample-size criterion and checking style rules.

**Agent calls Bash**

```bash
python - <<'EOF'
p='claims/mansvelder-2026.yaml'
s=open(p).read()
a=s[s.index("  criterion: The dandiset holds only part of the human acute sample"):s.index("- id: fig2b-human-higher-fres-q")]
b="""  criterion: Counts of human acute interneurons and of their donors in the data the attempt
    assembles, against the paper's. The dandiset holds only part of the human acute sample (the
    Table S1 donors whose dataset is "Chartrand"), so on the dandiset alone this is not
    reproduced; the counts of dandiset subjects found among the Table S1 donors and of dandiset
    cells with a chirp sweep are reported. The cultured and mouse totals are recorded as the
    paper's.
"""
s=s.replace(a,b)
s=s.replace("""# quoted, as the checker reads the text file only. No figure""","""# quoted, as the checker reads the text file only, and tools/claims_check.py flags their
# p-values as not found; each was confirmed against the PDF's text layer. No figure""")
open(p,'w').write(s)
EOF
grep -n -i -E "—|–|\brather\b" claims/mansvelder-2026.yaml; python tools/claims_check.py claims/mansvelder-2026.yaml paper/10.21203-rs.3.rs-11136357-v1.txt | tail -1; python -c "import yaml;d=yaml.safe_load(open('claims/mansvelder-2026.yaml'));c=d['claims'];print(len(c),sum('quote' in x for x in c),sum('statistics' in x for x in c),sum('criterion' in x for x in c),sum('expected' in x for x in c)); import collections;print(collections.Counter(x.get('data','dataset') for x in c))"
```

Result: not kept, because it reads the paper's text.

**Agent**

I've written `claims/mansvelder-2026.yaml`. All 43 quotes pass `tools/claims_check.py` and the schema check is clean. The checker still exits with 30 problems: all are p-values from Supplementary Table 3, which is not in the text file, so the checker cannot find them. I checked each against the supplement PDF; 8 of them are rounded forms of what the table prints. The repository's code had not been read when I wrote this. The paper's own code link returns 404.

**Text read.** The Research Square preprint, version 1 (posted 2026-10-12): main text, Methods, statistics section and the legends of Figs. 1–8. The text file holds the supplement only up to Table S2b, where it is cut. I read the rest of the supplement PDF (Table S3 statistics, Table S4 blocker donors, Table S5 model parameters, the end of the Fig. S6 legend) from its text layer with pypdf, because no page could be rendered. No figure was seen. That includes the Fig. 3b schematic of how sag ratio and input resistance are calculated.

**Code.** github.com/nsham2/Shamugia_et_al_2026 returns 404, so no analysis code was read. I read IPFX v2.0.0 (commit 1ddc0e5), which the paper cites, for its sag, input resistance and chirp routines. It is used only as a named reading where the Methods are silent.

**Counts.**

| Item | Number |
|---|---|
| Claims | 43, all with quotes |
| Claims with criteria | 43 |
| Claims with statistics | 31 (105 p-values) |
| Claims with expected values | 18 |
| Data type | 28 `with_inputs`, 9 `elsewhere` (Allen RNA-seq, the model), 5 `with_labels`, 1 `dataset` |

The `dataset` claim is the ZD7288 blocker experiment. Its new recordings are only available on request.

**Details the paper leaves open, with the readings named:**
- **O1, chirp analysis:** LOWESS fraction, FFT window, frequency range, and where Z0 and f3dB are taken. (a) IPFX averaged chirp, then LOWESS 0.04 (the value given for the model); (b) the same, limited to 0.4–40 Hz.
- **O2, sag ratio:** (a) IPFX sag on the sweep closest to −100 mV; (b) the same formula on the −100 pA step.
- **O3, input resistance:** (a) IPFX slope across hyperpolarizing steps; (b) a single step.
- **O4, the Vm covariate:** (a) pre-chirp baseline; (b) resting potential.
- **O5, mixed models:** (a) Satterthwaite Type III tests (SPSS or lmerTest); (b) statsmodels MixedLM. GEE is shown as a variant.
- **O6, χ² tests:** the Methods describe goodness of fit, which matches the per-subclass values in Table S3. The overall values (43.05, 44.98) match a 2x2 Pearson test without continuity correction. Both readings are named.
- **O7, ZD7288 sample size:** n = 7 cannot give the reported p = 0.004 with an exact Wilcoxon test; 9 cells can. Table S4 lists 8 cells. (a) Cells per measure; (b) cells with all four measures.
- **O8, gene correlations:** (a) CPM; (b) log(CPM+1). The test family is the 20 tests listed in Table S3.
- **O9, Fig. 4b regression direction:** (a) dendritic length on depth; (b) depth on dendritic length.
- **Smaller ones named in criteria:** how L2/L3 cells are selected, which cells enter the Fig. S1 tests, and the frequency ordering of the Fig. 7 morphology result, which the Results and Discussion state in opposite directions.
- **O10, text against Table S3:** recorded where they disagree (χ² 42.76 vs 43.05, mouse n 268 vs 248, several p-values, permuted Fig. 5j medians). Table S3 also contradicts the Fig. 5l "did not differ" claim (VIP p = .046, PV p = .031).

**Missing from the paper:**
- **Data locations:** no archive is named for the mouse recordings, the cultured recordings, the Lee et al. 2023 data or the Patch-seq transcriptomes. There are no per-cell subclass labels, Vm or pia-soma distances.
- **Dandiset coverage:** DANDI:000630 holds only the Chartrand human layer 1 subset, so most claims depend on outside data.
- **Model:** the adapted model is not deposited, and Table S5 does not give the calcium-channel density. The model claims after `fig7-model-ca` can only be rebuilt in part.

## End of run

34 turns, 9 minutes, $2.97 at API prices, result: success.
