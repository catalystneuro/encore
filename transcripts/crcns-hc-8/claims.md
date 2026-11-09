# crcns-hc-8 · claims · run 42567954211

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md | sed -n '/^## Reader/,/^## [A-Z]/p'; ls claims/001453 claims/crcns-hc-8 paper/ 2>&1
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/*.yaml | head -150; wc -l paper/*.txt; head -30 paper/10.3389-fphys.2016.00425.txt; grep -n -i supplement paper/10.3389-fphys.2016.00425.txt | head -30
```

Result: not kept, because it reads the paper's text.

**Agent**

Supplement is included. Let me read the whole text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.3389-fphys.2016.00425.txt",
 "offset": 30,
 "limit": 310
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '160,260p' claims/001453/*.yaml; sed -n '/^schema/,$p' claims/001453/*.yaml | grep -n -E "^  [a-z_]+:|^- |kind|data:" | sort | uniq -c | sort -rn | head -30
```

```
distributions of the two species differ for every stimulus.
  source: Results, Optic flow induces angular matching and turns in DC, paragraph 2; Figure 1H
    (Kruskal-Wallis test with Bonferroni correction)
  quote: Across directional stimuli, ZF maintained higher angular acceleration than DC
  statistics:
  - test: Kruskal-Wallis test
    p: 0.05
    p_relation: "<"
    corrected: Bonferroni
  data: with_labels
  depends_on:
  - stimulus-code-link
  criterion: Angular acceleration as the Methods define it (degrees per second squared), from
    the heading resampled to 30 Hz so that files with different frame rates are treated alike,
    smoothed with a 7-sample rolling median before and after each derivative as the code does;
    absolute values between 10 and 1000 degrees per second squared kept, frames 0 to 35 s
    into each passing trial, as in Fig1-S1.ipynb. Per stimulus, a Kruskal-Wallis test of ZF
    against DC frames at p < 0.05/9. Reproduced when, for all nine whole-field stimuli, the
    test is significant and the ZF median is higher; partially reproduced when that holds for
    five to eight; not reproduced otherwise. The quantity Fig1-S1.ipynb computes under this
[... 111 more lines not kept]
```

**Agent**

Now the supplement and data description.

**Agent calls Read**

```json
{
 "file_path": "paper/10.3389-fphys.2016.00425.txt",
 "offset": 339,
 "limit": 670
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat paper/hc-8.data-description.txt | head -130; ls tools; grep -rn "crcns" claims/ --include=*.yaml -l | head; ls claims | head -50
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
head -40 claims/crcns-hc-7/*.yaml; sed -n 1,80p tools/claims_check.py; grep -n -i "github\|toolbox\|http" paper/10.3389-fphys.2016.00425.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && for r in nmtimme/NCC-Toolbox nmtimme/Neural-Complexity-and-Criticality-Toolbox; do git ls-remote https://github.com/$r 2>&1 | head -3; done; curl -s "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5037237/fullTextXML" | grep -o '<ref id[^>]*>.\{0,600\}' | grep -i -E "timme.{0,300}2016|github" | head
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && curl -s -o x.xml -w "%{http_code}\n" "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5037237/fullTextXML"; python3 - <<'E'
import re
t=open('x.xml').read() if __import__('os').path.getsize('x.xml')>0 else ''
for m in re.finditer(r'<ref id="B\d+">(.*?)</ref>',t,re.S):
    s=re.sub('<[^>]+>',' ',m.group(1)); s=re.sub(r'\s+',' ',s)
    if 'Timme' in s and '2016' in s or 'http' in s: print(s[:400])
E
gh api search/repositories -X GET -f q="neural complexity criticality toolbox" --jq '.items[]|.full_name' 2>&1 | head
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s -o /dev/null -w "%{http_code}\n" https://github.com/nmtimme; curl -s -o /dev/null -w "%{http_code}\n" https://api.github.com/repos/nmtimme/NCC-Toolbox; curl -s -w "%{http_code}\n" "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PMCID:PMC5037237&format=json" | head -c 300
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5037237/fullTextXML" -o x.xml -w "%{http_code}\n"; python3 - <<'E'
import re
t=open('x.xml').read()
for m in re.finditer(r'<ref id="[^"]+">(.*?)</ref>',t,re.S):
    s=re.sub('<[^>]+>',' ',m.group(1)); s=re.sub(r'\s+',' ',s)
    if ('Timme' in s and '2016' in s) or 'http' in s or 'Marshall' in s: print(s[:400])
E
for q in "neural+complexity+criticality" "NCC+toolbox+timme"; do curl -s "https://api.github.com/search/repositories?q=$q" | python3 -c "import json,sys;d=json.load(sys.stdin);print([i['full_name'] for i in d.get('items',[])][:8], d.get('message'))"; done
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.github.com/users/nmtimme/repos | python3 -c "import json,sys;d=json.load(sys.stdin);print(d if isinstance(d,dict) else [i['full_name'] for i in d])"; curl -s "https://api.github.com/search/code?q=brestimate" | head -c 200; echo; curl -s "https://api.github.com/search/repositories?q=avprops+criticality" | python3 -c "import json,sys;d=json.load(sys.stdin);print([i['full_name'] for i in d.get('items',[])])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"
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
  "dataset",
  "paper",
  "claims"
 ],
 "properties": {
  "schema_version": {
   "const": 2
  },
  "dataset": {
   "description": "The dataset the claims are tested on: the archive and the dataset's identifier there.",
   "type": "object",
   "additionalProperties": false,
[... 185 more lines not kept]
```

**Agent calls Bash**

```bash
grep -rn -B2 -A6 -i "simulat\|model alone\|no recorded data" claims/*/*.yaml | grep -i -E "data:|criterion:.*(simulat|model)" | head -15; python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1)[:3500])"
```

```
claims/000009/10.1038-nature22324.yaml:649:  criterion: A simulation, not a test on recorded data; its parameters are in the Supplementary
claims/000011/10.1038-nature17643.yaml:907:  criterion: A simulation, not a test on recorded data. Parameters from the Methods and Extended
claims/000011/10.1038-nature17643.yaml:924:  criterion: A simulation, not a test on recorded data. Modular attractor with the Methods'
claims/000013/10.7554-elife.06619.yaml:1146:  criterion: Methods, last paragraph, and Figure 6D. Per L4 C2 cell, spike trains simulated as a
claims/000016/10.1016-j.neuron.2019.09.045.yaml:527:  criterion: A simulation, not a test on recorded data. The linearised rate model of the STAR
claims/000016/10.1016-j.neuron.2019.09.045.yaml:546:  criterion: A simulation, not a test on recorded data. As fig5a-nonselective-model; signal-selective
claims/000016/10.1016-j.neuron.2019.09.045.yaml:559:  criterion: A simulation, not a test on recorded data. As fig5bc-selective-models-match, with
claims/000036/10.1523-eneuro.0280-21.2021.yaml-602-  data: with_labels
claims/000036/10.1523-eneuro.0280-21.2021.yaml-1024-  data: with_labels
claims/000054/10.1038-s41593-021-00816-6.yaml:732:  criterion: Methods, Simulating a neural posterior distribution. Per trial, samples s from the
claims/000054/10.1038-s41593-021-00816-6.yaml:752:  criterion: A simulation with priors the authors propose for other laboratories' experiments
claims/000070/10.1038-nature11129.yaml:285:  criterion: One simulated dataset per array dataset from that session's condition-mean hand
claims/000128/10.1016-j.neuron.2010.09.015.yaml:550:  criterion: A simulation, not a test on recorded data. Two units, x(t+1) = W x(t) with W as printed
claims/000128/10.1016-j.neuron.2010.09.015.yaml:564:  criterion: A simulation, not a test on recorded data. As fig8-model-weak-correlation; PCA of the
claims/000138/10.1016-j.neuron.2010.09.015.yaml:402:  criterion: A simulation with no recorded data, from the Figure 8 legend
[... 102 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=5037237&rettype=xml" -o p.xml -w "%{http_code} %{size_download}\n"; grep -c "disp-formula" p.xml; grep -o "<ref-list.\{0,100\}" p.xml | head -2
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'E'
import re
t=open('p.xml').read()
for m in re.finditer(r'<disp-formula.*?</disp-formula>',t,re.S):
    s=m.group(0); print(re.sub(r'\s+',' ',s)[:300]); print('---')
for m in re.finditer(r'<ref id="[^"]+">(.*?)</ref>',t,re.S):
    s=re.sub('<[^>]+>',' ',m.group(1)); s=re.sub(r'\s+',' ',s)
    if ('Timme' in s and '2016' in s) or 'http' in s.lower() or 'Marshall' in s: print(s[:400])
E
```

```
<disp-formula id="E1"><label>(1)</label><mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" id="M2" overflow="scroll"><mml:mrow><mml:msub><mml:mi>f</mml:mi><mml:mi>s</mml:mi></mml:msub><mml:mo stretchy="false">(</mml:mo><mml:mi>S</mml:mi><mml:mo stretchy="false">)</mml:mo><mml:mtext> </mml:mtex
---
<disp-formula id="E2"><label>(2)</label><mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" id="M3" overflow="scroll"><mml:mrow><mml:msub><mml:mi>f</mml:mi><mml:mi>d</mml:mi></mml:msub><mml:mo stretchy="false">(</mml:mo><mml:mi>T</mml:mi><mml:mo stretchy="false">)</mml:mo><mml:mtext> </mml:mtex
---
<disp-formula id="E3"><label>(3)</label><mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" id="M4" overflow="scroll"><mml:mrow><mml:mo>〈</mml:mo><mml:mi>S</mml:mi><mml:mo>〉</mml:mo><mml:mo stretchy="false">(</mml:mo><mml:mi>T</mml:mi><mml:mo stretchy="false">)</mml:mo><mml:mtext> </mml:mtext><
---
<disp-formula id="E4"><label>(4)</label><mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" id="M5" overflow="scroll"><mml:mtable columnalign="left"><mml:mtr><mml:mtd><mml:mfrac><mml:mrow><mml:mi>α</mml:mi><mml:mo>-</mml:mo><mml:mn>1</mml:mn></mml:mrow><mml:mrow><mml:mi>τ</mml:mi><mml:mo>-</mml
---
<disp-formula id="E5"><label>(5)</label><mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" id="M6" overflow="scroll"><mml:mtable columnalign="left"><mml:mtr><mml:mtd><mml:mi>s</mml:mi><mml:mrow><mml:mo stretchy="false">(</mml:mo><mml:mrow><mml:mi>t</mml:mi><mml:mo>,</mml:mo><mml:mi>T</mml:mi><
---
<disp-formula id="E6"><label>(6)</label><mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" id="M7" overflow="scroll"><mml:mrow><mml:mo>〈</mml:mo><mml:mi>S</mml:mi><mml:mo>〉</mml:mo><mml:mo stretchy="false">(</mml:mo><mml:mi>T</mml:mi><mml:mo stretchy="false">)</mml:mo><mml:mtext> </mml:mtext><
---
<disp-formula id="E7"><label>(7)</label><mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" id="M8" overflow="scroll"><mml:mrow><mml:mi>γ</mml:mi><mml:mtext> </mml:m
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'E'
import re
t=open('p.xml').read()
for m in re.finditer(r'<disp-formula id="(E\d+)">(.*?)</disp-formula>',t,re.S):
    s=re.sub(r'<mml:mtext>\s*</mml:mtext>',' ',m.group(2)); s=re.sub('<[^>]+>','',s); print(m.group(1), re.sub(r'\s+',' ',s))
E
curl -s -L -o site.html -w "%{http_code}\n" http://www.nicholastimme.com; grep -o -i 'href="[^"]*"' site.html | head -30
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s -L http://www.nicholastimme.com/software.html -o sw.html; python3 -c "
import re;t=open('sw.html',errors='replace').read();print(re.sub(r'\s+',' ',re.sub('<[^>]+>',' ',t))[:3000]);print(re.findall(r'href=\"([^\"]+)\"',t))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'E'
import re
t=open('sw.html',errors='replace').read()
body=re.sub(r'<(script|style)[^>]*>.*?</\1>',' ',t,flags=re.S)
for m in re.finditer(r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>',body,re.S):
    print(m.group(1)[:60], '|', re.sub(r'\s+',' ',re.sub('<[^>]+>','',m.group(2)))[:80])
txt=re.sub(r'\s+',' ',re.sub('<[^>]+>',' ',body)); print(txt[:2500])
E
```

```
home.html | Home
cv.html | CV
papers.html | Papers
files.html | Files
software.html | Software
data.html | Data
contact.html | Contact
news.html | News
https://twitter.com/nicholastimme?lang=en | Twitter
https://github.com/nmtimme/Neuroscience-Information-Theory-T | here
//nebula.wsimg.com/ca54221c5919b874c5ffb0a03f682560?AccessKe | Version 1
//nebula.wsimg.com/971efb8df3b4cee0918d28361ab5560e?AccessKe | Version 2
http://journal.frontiersin.org/article/10.3389/fphys.2016.00 | link
//nebula.wsimg.com/98697c791c08ce110c0ebe10a6142deb?AccessKe | Version 1
http://link.springer.com/article/10.1007/s10827-013-0458-4 | link
http://arxiv.org/abs/1004.2515 | link
//nebula.wsimg.com/90ed18ce5d120f6c3a6aaf7337193b59?AccessKe | Download
http://arxiv.org/abs/1111.6857 | link
//nebula.wsimg.com/05092315fdd781bd48a05eab5e67b654?AccessKe | Download
https://www.godaddy.com/websites/website-builder?cvosrc=asse | 
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s -L -o ncc.zip "https://nebula.wsimg.com/98697c791c08ce110c0ebe10a6142deb?AccessKeyId=AE70CEF69B3CE16C32E9&disposition=0&alloworigin=1" -w "%{http_code} %{size_download}\n"; file ncc.zip; sha256sum ncc.zip; mkdir -p ncc && cd ncc && unzip -o -q ../ncc.zip && find . -type f | head -80
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/ncc/NCCToolboxV1; wc -l *.m *.txt; ls -la --time-style=long-iso | head -40
```

```
67 asdf2toraster.m
   190 avgshapes.m
   183 avprops.m
   258 avpropvals.m
   245 avshapecollapse.m
   136 avshapecollapsestd.m
   209 bethelattice.m
   131 brestimate.m
   294 cbmodel.m
   208 complexity.m
   323 complexityexamples.m
    92 democomplexity.m
   117 demoempdata.m
   220 demoplotting.m
    93 demotruncdist.m
   238 gendata.m
   145 mymnrnd.m
   173 pldist.m
   183 plmle.m
   189 plparams.m
[... 44 more lines not kept]
```

**Agent**

Paper text, supplement and the equations (recovered from the PMC XML) are in hand; I found the NCC Toolbox V1 the paper cites (nicholastimme.com) and am now reading its key functions.

**Agent calls Bash**

```bash
cd $TMPDIR/ncc/NCCToolboxV1; cat plparams.m pvcalc.m | grep -v "^\s*$" | head -400
```

```
%% PLPARAMS - automated computation of power law parameters using MLE
% Higher level macro and automated algorithm that computes the exponent for
% power-law distributed data and its uncertainty, the p-value and ks
% statistic for the fit, and searches for optimal support [xmin,xmax]. The
% function utilizes a "smart" greedy search algorithm to settle on a
% support pair. Prior to initiating the greedy search, all support pairs
% for which xmin and xmax differ by 1 are removed; the remainder are then
% sorted by log(xmax/xmin).
%
% Syntax: [tau, xmin, xmax, sigmaTau, p, pCrit, ks] = plparams(x, varargin)
%
% Input:
%   x (vector double) - random data that we would like to fit to the power
%     law distribution p(x) ~ x^(-tau) for x >= xmin and x <= xmax.
%
% Variable Inputs:
%   (..., 'samples', nSamples) - the number of sample distributions to draw.
%     Sets the resolution of the p-value (scalar double) (default: 500)
%   (..., 'threshold', pCrit) - for computational efficiency, a critical
%     p-value can be used to halt the computation if the likelihood of a
[... 381 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/ncc/NCCToolboxV1; for f in rebin.m avprops.m brestimate.m; do echo "=== $f"; awk '/^function/{p=1} p' $f | grep -v "^\s*$"; sed -n '1,40p' $f | grep "^%" | head -30; done
```

```
=== rebin.m
function newAsdf2 = rebin(asdf2, binSize)
%%
resolution = (10^(ceil(log10(round(binSize/asdf2.binsize))) + 1))*eps;
newBinIsIntMult = (abs(round(binSize/asdf2.binsize) - (binSize/asdf2.binsize)) < resolution);
assert(newBinIsIntMult,...
    'binSize must be an integer multiple of asdf2.binsize.')
%%
newAsdf2 = asdf2;
rebinFactor = 1 / round(binSize/asdf2.binsize);
for iRaster = 1:newAsdf2.nchannels
    newAsdf2.raster{iRaster} = unique(ceil(asdf2.raster{iRaster} * rebinFactor));
end
newAsdf2.binsize = binSize;
newAsdf2.nbins = ceil(asdf2.nbins*rebinFactor);
%% REBIN - rebins asdf2 formatted data
% Bins divide neuronal activity time series data into blocks of time which
% indicate whether or not a neuron was active. In this case time bins are 
% uniformly spaced and in units of milliseconds.
%
[... 225 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/ncc/NCCToolboxV1; for f in avpropvals.m; do echo "=== $f"; sed -n '1,60p' $f | grep "^%"; awk '/^function/{p=1} p' $f | grep -v "^\s*$"; done
```

```
=== avpropvals.m
%% AVPROPVALS - avalanche property values
% High level macro that returns the values associated with an avalanche 
% property. The function handles size and duration data stored in a cell
% array by overlaying plots onto a single figure, however this feature is
% incompatible with size given duration data stored in a cell array.
%
% Syntax: [tau, xmin, xmax, sigmaTau, p, pCrit, ks, PlotData] = ...
%               avpropvals(Avalanche, property, varargin)
%
% Inputs:
%   Avalanche (vector double or cell array) - avalanche property, size,
%     duration, or size given duration. Size and duration distributions can
%     either be input as a vector double or cell array. Size given duration
%     distribution must be input as a cell array with the size distribution
%     in the first cell and the duration distribution in the second.
%   property (string) - specifies for which avalanche property to 
%     compute the associated values. Options: 'size', 'duration', or
%     'sizgivdur' (average size given duration).
%
[... 163 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/ncc/NCCToolboxV1; for f in avshapecollapse.m complexity.m; do echo "=== $f"; sed -n '1,70p' $f | grep "^%" | head -50; awk '/^function/{p=1} p' $f | grep -v "^\s*$" | grep -v "^\s*%"; done
```

```
=== avshapecollapse.m
%% AVSHAPECOLLAPSE - performs avalanche shape collapse
% Automatically determines scaling parameter 1/(sigma nu z) by computing
% the variance between all possible shape collapses for a range of possible
% exponent values using a set of average temporal profiles. The process
% involves a multi-step refinement of the range of values which optimizes
% computation time without sacrificing accuracy.
%
% Syntax: [sigmaNuZInv, secondDrv, range, errors, figName] = 
%             avshapecollapse(avgProfiles, varargin)
%
% Input:
%   avgShapes (cell array) - array of mean temporal profiles (vector double)
%
% Variable Inputs:
%   (..., 'precision', precision) - sets the decimal precision for the
%     parameter search precision (power of ten scalar double) (default: 
%     10^-3)
%   (..., 'bounds', bounds) - sets the bounds on the initial range of
%     exponent values (vector double) (default: [0 4])
[... 284 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/ncc/NCCToolboxV1; sed -n '1,80p' randomizeasdf2.m | grep "^%"; grep -n "case '" randomizeasdf2.m | head -20; sed -n '1,40p' avgshapes.m | grep "^%" | head -25; cat "README - Criticality.txt" | sed -n '1,80p'
```

```
%% RANDOMIZEASDF2 - randomize asdf2 spike data to produce a null model
% Algorithm for randomizing spiking data in the asdf2 format using a
% specified method. This randomized data can be used as a null model
% version of the data in any given analysis.
%
% Syntax: [randasdf2] = randomizeasdf2(asdf2, method, varargin)
%
% Input:
%   asdf2 (structure array) - contains time raster and other information
%   method (string) - specifies the randomization method used. Choices:
%     'wrap' - cuts each spike train at random time (different for each
%         train) and swaps the resulting pieces. This method nearly
%         preserves the ISI distribution for each neuron, but completely
%         disrupts interneuron temporal relationships. 
%     'jitter' - randomly alters each spike time using a Gaussian
%         distribution centered on the original spike time. The user can
%         set the standard deviation of Gaussian distribution. This method
%         nearly preserves the ISI distribution for each neuron and all
%         neurons considered together. Also, it preserves interneuron
%         temporal relationships to a certain extent, dependent upon the
[... 162 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/ncc/NCCToolboxV1; awk '/^%% /{p=1} p' demoempdata.m | grep -v "^\s*$" | grep -v "^% \|^%$" | head -90; grep -n "cutoffs" -A12 avgshapes.m | head -40
```

```
%% DEMOEMPDATA - analyzing empirical data
%==============================================================================
%% Load and process sample data
load sample_data
Av = avprops(asdf2, 'ratio', 'fingerprint');
%% Plot histogram of branching ratios
minBR = min(Av.branchingRatio);
maxBR = max(Av.branchingRatio);
nEdges = 25;
edges = minBR:((maxBR-minBR)/(nEdges - 1)):maxBR;
BRhist = histc(Av.branchingRatio, edges);
plot(edges, BRhist);
title('Histogram of Avalanche Branching Ratios', 'fontsize', 14)
xlabel('Branching Ratio (s_{t+1} / s_t)', 'fontsize', 14)
ylabel('Frequency of Occurrence', 'fontsize', 14)
%% Compute power-law parameters using macro
[tau, xminSZ, xmaxSZ, sigmaSZ, pSZ, pCritSZ, ksDR, DataSZ] =...
    avpropvals(Av.size, 'size', 'plot');
UniqSizes = unique(Av.size);
Occurances = hist(Av.size,UniqSizes);
[... 65 more lines not kept]
```

**Agent**

Code read (NCC Toolbox V1). Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/crcns-hc-8/10.3389-fphys.2016.00425.yaml",
 "content": "# Claims for Timme, Marshall, Bennett, Ripp, Lautzenhiser & Beggs (2016), Front. Physiol. 7:425,\n# \"Criticality Maximizes Complexity in Neural Tissue\", doi:10.3389/fphys.2016.00425, on CRCNS data\n# set hc-8 (doi:10.6080/K0PC308P).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-09,\n# protocol as stated in docs/protocol.md.\n#\n# Text read: the version of record (PMC5037237, open access) as supplied under paper/ (Europe PMC\n# JATS XML flattened): Methods 2.1 to 2.11, Results 3.1 to 3.3, Discussion, figure legends of\n# Figures 1 to 12 and Table 1, and the supplement (Data_Sheet_1.PDF, supplementary Figures S1 to S9\n# with their text). The supplied text drops the display equations; Equations 1 to 14 were read from\n# the MathML of the PMC XML (eutils efetch, PMC5037237): Eq. 9 integration, Eq. 10\n# C_N(X) = (1/N) sum over k = 2..N of [((k-1)/(N-1)) I(X_1^N) - <I(X_j^k)>_j], Eq. 11\n# B_basic = <A(t+1)/A(t)>_t, Eq. 12 A(t+k) = r_k A(t), Eq. 13 r_k ~ B_new^k, Eq. 14\n# chi = var(A(t)/N_neurons). No PDF of the main article is supplied, so values printed only inside\n# the figures were not read: the mean and standard deviation of each exponent in Figure 8, the\n# branching ratio histograms of Figure 9, the significance stars of Figures 10 and 11, the list of\n# excluded recordings in Figure 2B, and the axes of Figures 7 and 12. Claims on those figures rest on\n# the Results and the legends and carry no expected values from the figures.\n#\n# Code. The paper cites the NCC MATLAB toolbox (Marshall et al., 2016) and \"Timme N. M. (2016).\n# Available online at: http://www.nicholastimme.com\" for brestimate. Read: NCC Toolbox Version 1\n# (June 14th, 2016), downloaded from the Software page of nicholastimme.com, zip sha256\n# b7c912f8154f70fc82b13ab1725ed191935ed2877256cadd7e39f66737be294b. It holds the power-law MLE and\n# support search (plmle, plparams, pvcalc: 500 surrogates, p threshold 0.2, support pairs ranked by\n# log(xmax/xmin) and tried largest first), avalanche detection (avprops), rebinning (rebin, integer\n# multiples of the original bin only), size given duration fit (sizegivdurwls), mean profiles and\n# shape collapse (avgshapes with cutoffs 4 and 20, avshapecollapse: variance of scaled profiles over\n# 1/sigma nu z in [0, 4] refined to 0.001, quadratic fit, secondDrv = 2 times the leading\n# coefficient), complexity with sub-sampling correction (complexity: at most nSubSets random\n# subsets per size, randomized data from independent time permutation of each neuron subtracted,\n# cut at the first peak of the corrected integration over k), randomizations (randomizeasdf2:\n# wrap, jitter, Poisson, swap, swap2), the branching ratio (brestimate), and the two models\n# (bethelattice, cbmodel). The analysis scripts that ran these functions on the cultures are not\n# published. Where the Methods leave a choice open and the toolbox settles it, the criteria follow\n# the toolbox and say so.\n#\n# Data the paper used. Dissociated hippocampal cultures from embryonic day 18 Sprague-Dawley rat\n# embryos, about 200,000 cells plated per culture on Multichannel Systems 60-electrode arrays\n# (200 um spacing, 30 um electrodes), recorded without stimulation from DIV 6 to 35; 435 recordings\n# from 28 cultures (Figure 2B), first 59 min of each, 20 kHz; spikes sorted with wave_Clus (5 SD\n# negative threshold, no dead time, checked by hand); 39,529 neurons in total, most recordings about\n# 100 neurons, firing rates about 0.05 to 20 Hz. Some recordings were excluded for too few\n# avalanches (red squares of Figure 2B; the threshold is not stated). Measured variables: spike\n# times per neuron. The data set's description names files CultureXDIVY with data.spikes in 0.05 ms\n# bins, matching the paper. The model results (Bethe lattice, cortical branching model, chain\n# model) are simulations that use no recorded data.\n#\n# Method common to the culture claims, from Methods 2.3 to 2.11 unless said otherwise. Spikes of\n# the first 59 min are rebinned to the recording's mean network-wide ISI (the ISI of all spikes of\n# all neurons pooled); an avalanche is a run of consecutive bins with at least one spike, its\n# duration the number of bins and its size the number of spikes (avprops). Randomizations act on\n# the rebinned data: jitter with a normal SD of 1, 10 or 100 bins keeping spike counts, wrap,\n# Poisson, spike swap and neuron shuffling (Methods 2.5). Complexity is computed on the avalanche\n# time bins only (Methods 2.9, \"unless otherwise noted\") with the sub-sampling correction of the\n# toolbox, at most 100 subsets per size (Methods 2.9). \"Full data sets\" in Figures 10 and 11 means\n# the whole recorded system without the sub-sampling extrapolation (Methods 2.10).\n#\n# Details the paper leaves open, used by several claims, with the readings each criterion runs:\n# (1) The mean network ISI must be a whole number of 0.05 ms bins for rebin; rounding to the\n# nearest bin is a standard choice that cannot change the outcome. (2) Which recordings were\n# excluded for too few avalanches: the threshold is not stated and Figure 2B could not be read;\n# readings (a) all recordings in which the size and the duration distributions each keep at least\n# one value after the cuts of Methods 2.7 and at least two durations for the shape collapse, (b)\n# all recordings; the number excluded is reported. (3) The multiple comparisons correction of\n# Figures 10 and 11 cites both Benjamini and Hochberg (1995) and Benjamini and Yekutieli (2001);\n# readings (a) Benjamini-Hochberg, (b) Benjamini-Yekutieli, over the comparisons of one panel, at\n# 0.05. (4) Which randomizations appear in Figures 10 and 11: the Methods list jitter 1, 10 and 100\n# bins, wrap, Poisson, swap and shuffling; the criteria use all seven and report each. (5) The\n# susceptibility: Eq. 14 is var(A(t)/N); readings (a) Eq. 14 as printed, (b) N var(A(t)/N), the\n# Williams-Garcia et al. (2014) form, which fits the 0 to 5 range of the Figure S8 axis; both over\n# all time bins of the recording. (6) Shape collapse curvature: the toolbox returns 2 times the\n# leading coefficient of the quadratic fit, negative for an arched profile, while Figures S5 and 7\n# report positive curvatures and Results 3.2 speaks of \"average absolute curvature\"; the criteria\n# use the absolute value.\nschema_version: 2\ndataset:\n  archive: crcns\n  id: hc-8\n  doi: 10.6080/K0PC308P\npaper: doi:10.3389/fphys.2016.00425\nclaims:\n- id: fig3-chain-model-complexity\n  statement: In the 12-neuron chain model, random data (c = 0) give zero integration, ordered data\n    (c = 1) give high integration, and only the complex data (c = 0.8) give non-zero complexity.\n  source: Methods 2.9, paragraph 6; Figure 3B and 3C\n  quote: Note that random data shows no integration, while ordered data shows high integration ...\n    Only the complex data shows non-zero complexity.\n  criterion: A simulation, not a test on recorded data. The chain model of Methods 2.4 (12 neurons,\n    first neuron alternating active and inactive between runs, p(a_i+1 = a_i) = 0.5(1 + c)), with\n    complexity from Eq. 10 on the exact joint distribution (Methods 2.9, last paragraph says the\n    model's distributions were defined exactly). Reproduced when C_N is zero within 1e-6 bits for\n    c = 0 and c = 1 and above that for c = 0.8, and the whole-system integration is near zero for\n    c = 0 and the largest for c = 1.\n- id: fig5d-bethe-small-avalanches\n  statement: In the critical Bethe lattice model (p_trans = 0.5), avalanche sizes are power-law\n    distributed and show shape collapse, and the small avalanches (stopped by the 8th layer) are\n    power-law distributed in size and have non-zero complexity.\n  source: Results 3.1, paragraph 1; Figure 5B to 5D\n  quote: In the original small avalanches, the sizes of the avalanches were power-law distributed\n    and a non-zero complexity was observed\n  criterion: A simulation, not a test on recorded data. Bethe lattice of Methods 2.4 (two outgoing\n    connections per neuron, p_trans = 0.5, activity stopped at layer 10^4, one neuron active in the\n    first layer per run), as in the toolbox's bethelattice.m. The number of runs is not stated; a\n    standard choice of 10^4 runs is used and cannot change the direction of the result. Small\n    avalanches are those that stop on or before layer 8; each run is one time series of network\n    states over the neurons of layers 1 to 8. Reproduced when the size distribution of the small\n    avalanches is accepted as a truncated power law by plparams (p at least 0.2) and their\n    complexity (toolbox complexity, sub-sampling correction on) is above zero.\n- id: fig5e-shuffle-removes-complexity\n  statement: In the Bethe lattice small avalanches, neuron shuffling preserves the avalanche size\n    distribution but removes the complexity.\n  source: Results 3.1, paragraph 1; Figure 5E\n  quote: First, we randomized the neuron identities in the avalanches (neuron shuffling). This\n    operation preserved the avalanches and their power-law size distributions, but removed the\n    complexity\n  depends_on:\n  - fig5d-bethe-small-avalanches\n  criterion: A simulation, not a test on recorded data. Neuron shuffling as in Methods 2.5 (at each\n    time bin the active count kept and the identities drawn uniformly over all neurons). Reproduced\n    when the shuffled size distribution equals the original and the complexity falls to below 10%\n    of the original value (\"removed\" read as near zero; 10% is a choice the paper does not make).\n- id: fig5f-network-state-poisson-keeps-complexity\n  statement: In the Bethe lattice small avalanches, randomizing the order of whole network states\n    preserves the complexity but changes the avalanche size distribution dramatically.\n  source: Results 3.1, paragraph 1; Figure 5F\n  quote: when we randomized the order of the network states, but preserved neuron spiking states at\n    each individual time bin (Poisson randomization for the whole network state), the complexity was\n    preserved, but the distribution of avalanche size changed dramatically\n  depends_on:\n  - fig5d-bethe-small-avalanches\n  criterion: A simulation, not a test on recorded data. Whole network states (one per time bin)\n    placed at random times, as Methods 2.5, paragraph 4, last sentence. Complexity depends only on\n    the distribution of states (Methods 2.9), so it is preserved exactly when the same states are\n    kept; reproduced when the complexity differs from the original by less than 5% (the residue of\n    the random subset draws) and the size distribution of the permuted data is no longer accepted as\n    the original power law (plparams p below 0.2 or exponent outside the original's error).\n- id: fig6-cb-distribution-curvature\n  statement: In the cortical branching model, low transmission probabilities give size and duration\n    distributions that curve downwards, high ones give distributions that curve upwards, and\n    p_trans near 0.25 gives the straightest distributions.\n  source: Results 3.2, paragraph 1; Figure 6A and 6B\n  quote: note that the low transmission probability models produced distributions that curved\n    downwards, whereas the high transmission probability models produced distributions that curved\n    upwards. The model with a transmission probability near the infinite system critical\n    transmission probability ( p trans = 0.25) produced the straightest size and duration\n    distributions\n  criterion: A simulation, not a test on recorded data. Cortical branching model of Methods 2.4\n    (100 neurons on a 10 by 10 torus, four nearest neighbours, p_spont = 10^-4, 3 x 10^5 steps),\n    as cbmodel.m. Curvature read as the sign of the quadratic term of a quadratic fit of\n    log10 probability on log10 size (and duration) over the values kept by the cuts of Methods 2.7;\n    a measure the paper does not define. Reproduced when, averaged over 30 models each, the\n    quadratic term is negative at p_trans 0.2, positive at 0.3, and smallest in magnitude at 0.25.\n- id: fig7ab-cb-complexity-susceptibility-peak\n  statement: Across cortical branching models, the complexity and the susceptibility (both\n    extrapolated to infinite size by sub-sampling) peak near p_trans 0.265, close to the infinite\n    system critical point of 0.25.\n  source: Results 3.2, paragraph 2; Figure 7A and 7B\n  quote: When we plotted the complexity and susceptibility vs. the transmission probability, we\n    found both peaked near p trans ≈ 0.265\n  expected:\n  - quantity: p_trans at the peak of mean complexity\n    value: 0.265\n    tolerance: 0.0265\n  - quantity: p_trans at the peak of mean susceptibility\n    value: 0.265\n    tolerance: 0.0265\n  criterion: A simulation, not a test on recorded data. 30 cortical branching models per p_trans\n    (Methods 2.4); complexity on avalanche time bins; susceptibility by Eq. 14 (common detail 5);\n    each extrapolated to 1/N = 0 by the sub-sampling of Methods 2.10 (sub-samples from 40 to 100\n    neurons, weighted least squares with weight N; for complexity, the 10 largest sub-samples\n    first, smaller ones added until a residual exceeds the mean plus 3 SD of the residuals). Open,\n    the p_trans grid. Methods 2.4 prints \"increments of 0.05\" on 0.2 to 0.3, which gives three\n    values and cannot place a peak at 0.265, while Figure S1 shows p_trans = 0.26 and Figure S2 a\n    curve over the interval; readings (a) steps of 0.005 (21 values), (b) steps of 0.01 (11\n    values). Open, the sub-sampling layout (Methods 2.10, \"30 times at evenly spaced systems\n    sizes\"); readings (a) 30 sub-samples whose sizes are evenly spaced from 40 to 100 neurons, (b)\n    30 random sub-samples at each of the integer sizes from 40 to 100. Reproduced when the mean\n    over models of each extrapolated quantity has its interior maximum within tolerance of 0.265\n    (the rise of complexity at the upper boundary, fig7a-complexity-boundary-rise, is not the peak).\n- id: fig7a-complexity-boundary-rise\n  statement: The cortical branching model's complexity also rises near the upper end of the tested\n    range (p_trans near 0.3), a bias from longer recordings, as higher transmission gives longer\n    avalanches.\n  source: Results 3.2, paragraph 3; Figure 7A legend\n  quote: we also found that the complexity was increasing near the boundary for the tested range of\n    transmission probabilities (i.e., near p trans = 0.3)\n  depends_on:\n  - fig7ab-cb-complexity-susceptibility-peak\n  criterion: A simulation, not a test on recorded data. With the analysis of\n    fig7ab-cb-complexity-susceptibility-peak, reproduced when the mean complexity at the largest\n    p_trans tested is above that at the next lower p_trans and above the minimum between the main\n    peak and 0.3.\n- id: figs2-recording-length\n  statement: In the cortical branching model, longer recordings give higher complexity, and with all\n    time bins analysed the high-p_trans rise shrinks relative to the main peak as the recording\n    lengthens.\n  source: Supplement, Cortical branching model, paragraph 2; Figure S2\n  quote: We found that longer recordings tended to produce higher complexity values. Furthermore,\n    though a secondary peak in the complexity was apparent for high transmission values (similar to\n    results shown in the main text), this peak decreased in magnitude relative to the primary peak\n    near ptrans ≈0.28 as the recording length increased\n  expected:\n  - quantity: p_trans at the primary complexity peak, all time bins\n    value: 0.28\n    tolerance: 0.028\n  criterion: A simulation, not a test on recorded data. 30 models per p_trans run for 3 x 10^4,\n    10^5 and 3 x 10^5 steps; complexity on all time bins (Figure S2 legend). The p_trans grid as\n    the readings of fig7ab-cb-complexity-susceptibility-peak. Open whether the sub-sampling\n    extrapolation was applied (the supplement says the analysis was identical to the main text\n    apart from the time bins); readings (a) extrapolated, (b) whole 100-neuron system. Reproduced\n    when the mean complexity at the primary peak increases with recording length, the primary peak\n    lies within tolerance of 0.28, and the ratio of the value at p_trans 0.3 to the primary peak\n    value decreases with recording length.\n- id: fig7c-cb-curvature-no-peak\n  statement: The shape collapse curvature of the cortical branching model does not peak near the\n    critical point; sub-critical avalanches are more curved than super-critical ones.\n  source: Results 3.2, paragraph 4; Figure 7C\n  quote: We found that the shape collapse curvature did not peak near the critical point (Figure 7C\n    ) ... the curvature results indicate that sub-critical avalanches were more curved than\n    super-critical avalanches\n  criterion: A simulation, not a test on recorded data. Shape collapse of mean profiles of durations\n    of at least 4 with at least 20 avalanches (Methods 2.8, avgshapes cutoffs 4 and 20), absolute\n    curvature (common detail 6), extrapolated by sub-sampling as Figure S1C. Reproduced when the\n    mean curvature at p_trans 0.2 exceeds that at 0.3 and the curvature has no interior maximum\n    within 0.02 of 0.25 and 0.265.\n- id: fig7d-cb-branching-ratio-near-1\n  statement: The cortical branching model's branching ratio is closest to 1 near the same\n    transmission probability at which complexity and susceptibility peak.\n  source: Results 3.2, paragraph 2; Figure 7D\n  quote: Furthermore, the branching ratio was found to be closest to 1 near this same transmission\n    probability (Figure 7D )\n  depends_on:\n  - fig7ab-cb-complexity-susceptibility-peak\n  criterion: A simulation, not a test on recorded data. B_new from Eq. 12 and 13 with delays 1 to 8\n    and 0 <= A(t) <= 5 (Methods 2.11), polyfit slopes and an exponential fit as brestimate.m, no\n    sub-sampling correction (Methods 2.10). Reproduced when the p_trans whose mean B_new is\n    closest to 1 lies within 0.0265 of the peaks found in fig7ab-cb-complexity-susceptibility-peak.\n- id: culture-counts\n  statement: The culture data hold 435 recordings and 39,529 spike-sorted neurons in total; most\n    recordings yield about 100 neurons, and firing rates range from roughly 0.05 to 20 Hz.\n  source: Methods 2.2, paragraphs 1 and 2; Figure 2A and 2C\n  quote: total number of neurons across all recordings: 39,529). Most recordings yielded\n    approximately 100 spike sorted neurons and firing rates ranged from roughly 0.05–20 Hz\n  expected:\n  - quantity: number of recordings\n    value: 435\n    tolerance: 0\n  - quantity: total number of neurons\n    value: 39529\n    tolerance: 0\n  - quantity: modal number of neurons per recording\n    value: 100\n    tolerance: 10\n  criterion: Counts of recordings and of sorted units are exact properties of the deposited data, so\n    the tolerance is zero. \"Most recordings ... approximately 100\" is read as the median number of\n    neurons per recording within 10% of 100. Firing rate as spike count over the first 59 min\n    (Methods 2.2); the range holds when the 5th and 95th percentiles over neurons lie within 0.045 to\n    22 Hz (the range widened by 10% of each bound). Firing rates span \"multiple orders of magnitude\"\n    (Figure 2A legend) is reported.\n- id: fig2d-network-isi\n  statement: Most recordings have a mean network-wide interspike interval of around 7 ms, though some\n    are much higher or lower.\n  source: Methods 2.3, paragraph 1; Figure 2D\n  quote: Most recordings had ISIs of around 7 ms, though some data sets showed much higher or lower\n    ISIs\n  expected:\n    quantity: typical mean network-wide ISI across recordings\n    value: 7\n    tolerance: 0.7\n    unit: ms\n  criterion: Per recording, the mean interval between consecutive spikes of all neurons pooled, over\n    the first 59 min (Methods 2.3). \"Most ... around\" read as (a) the median over recordings, (b)\n    the mode of a histogram with Terrell-Scott bins (the bin rule of Figures 8 and 9). Reproduced\n    when one reading is within tolerance.\n- id: fig2e-avalanche-count\n  statement: After rebinning to the network ISI, most recordings contain around 10,000 avalanches.\n  source: Methods 2.3, paragraph 1; Figure 2E\n  quote: Following the rebinning procedure and avalanche detection, most recordings contained around\n    10,000 avalanches\n  depends_on:\n  - fig2d-network-isi\n  expected:\n    quantity: typical number of avalanches per recording\n    value: 10000\n    tolerance: 1000\n  criterion: Avalanches as avprops on the rebinned first 59 min. Readings as fig2d-network-isi\n    ((a) median, (b) histogram mode); reproduced when one is within tolerance.\n- id: fig8-subsampling-exponents\n  statement: In the culture recordings, sub-sampling extrapolation gives lower values of tau and alpha\n    with lower errors than the search algorithm on the full system, while 1/sigma nu z changes\n    little between the two.\n  source: Results 3.3, paragraph 2; Figure 8A to 8D\n  quote: We found lower values of τ and α using the sub-sampling analysis, as well as lower errors\n    (Figures 8A,B ). The values of 1/σ νz showed little change between sub-sampling and the\n    analysis of the full system (Figures 8C,D )\n  criterion: The means and SDs printed in Figure 8 could not be read (no main PDF), so the claim is\n    judged on directions. Full system, per recording, tau and alpha from plparams after the cuts of\n    Methods 2.7 (sizes or durations of at least 4, and values seen at least 20 times removed one by\n    one, as demoempdata.m does), 1/sigma nu z from the weighted least squares fit of size given\n    duration over the fitted duration range (sizegivdurwls) and from the shape collapse\n    (avshapecollapse). Sub-sampling, per Methods 2.10, the fit over all avalanches surviving the\n    cuts with no range search, values regressed on 1/N with weight N, the intercept kept; layout\n    readings as fig7ab-cb-complexity-susceptibility-peak. \"Errors\" read as the SD across recordings\n    (the legend quotes mean and SD). Reproduced when the mean over recordings of the extrapolated\n    tau and alpha are each below the full-system means and their SDs are smaller, and each mean of\n    1/sigma nu z changes by less than 10% between the two analyses.\n- id: fig8-sigmanuz-methods-agree\n  statement: The values of 1/sigma nu z from the size given duration fits and from the shape\n    collapse agree within error.\n  source: Results 3.3, paragraph 2; Figure 8C and 8D\n  quote: Note that the values of 1/σ νz found using distinct methods (average size given duration\n    fits and shape collapse) agree within error\n  depends_on:\n  - fig8-subsampling-exponents\n  criterion: Within error read as the difference of the two means over recordings smaller than the\n    larger of their two SDs, as quoted in Figure 8 (mean +/- SD); judged for the full-system and the\n    sub-sampling estimates, and reproduced when it holds for both.\n- id: eq4-exponent-relation\n  statement: The culture critical exponents satisfy the relation (alpha - 1)/(tau - 1) = 1/sigma nu z\n    (Eq. 4) with both the search algorithm and the sub-sampling method.\n  source: Results 3.3, paragraph 2; Figure 8\n  quote: Furthermore, note that the critical exponents satisfy the general relationship given in\n    Equation (4) using both the search algorithm and the sub-sampling method\n  depends_on:\n  - fig8-subsampling-exponents\n  criterion: The paper gives no test. Using the means over recordings from Figure 8 as the paper\n    does, reproduced when (alpha - 1)/(tau - 1) lies within one SD (propagated from the SDs of tau\n    and alpha) of the mean 1/sigma nu z from size given duration or from shape collapse, for both\n    analyses. Per-recording agreement is reported as a variant.\n- id: eq4-relation-randomized\n  statement: Randomized culture data also satisfy the critical exponent relation, with different\n    exponent values.\n  source: Results 3.3, paragraph 2\n  quote: However, we also found that randomized data satisfied the critical exponent relationship,\n    though with different exponent values (data not shown)\n  depends_on:\n  - eq4-exponent-relation\n  criterion: As eq4-exponent-relation on the full-system exponents of the randomized data\n    (fig10-randomization-markers lists the methods). Reproduced when the relation holds as defined\n    there for at least one randomization method and that method's mean tau or alpha differs from the\n    real data's by more than one SD. The data are \"not shown\", so the methods it covers are open;\n    every method is reported.\n- id: fig9-branching-ratio\n  statement: With the sub-sampling-corrected method, most culture recordings have branching ratios\n    slightly below 1, while the basic method gives ratios substantially below 1 and more varied.\n  source: Results 3.3, paragraph 3; Figure 9\n  quote: Using the new method, we found most recordings produced branching ratios slightly below 1\n    (i.e., slightly sub-critical). Using the previous basic method, we found most recordings\n    produced branching ratios that were substantially less than 1 and much more varied\n  criterion: B_new per recording by Eq. 12 and 13, delays 1 to 8, 0 <= A(t) <= 10 (Methods 2.11),\n    polyfit and an exponential fit by non-linear least squares as brestimate.m. B_basic by Eq. 11,\n    the time average of A(t+1)/A(t) over bins with A(t) > 0 (the ratio is undefined otherwise);\n    the toolbox's brsimple (slope of A(t+1) on A(t)) and the per-avalanche ratio of avprops are\n    shown as variants. \"Slightly below 1\" is not given a width; readings (a) within 0.05 below 1,\n    (b) within 0.1 below 1. Reproduced when, under one reading, more than half of the recordings\n    have B_new in that band, more than half have B_basic below the band, and the SD of B_basic\n    across recordings exceeds that of B_new.\n- id: fig10a-complexity-randomization\n  statement: Culture complexity decreases under randomization, most under the strongest forms such as\n    Poisson randomization, with the exception of spike swapping.\n  source: Results 3.3, paragraph 4; Figure 10A\n  quote: Complexity decreased under randomization, with the exception of spike swapping\n  criterion: Per recording, complexity of the real data and of each randomization (common method).\n    The Figure 10 legend gives the test, a rank sum test of real against each randomization across\n    recordings with false discovery rate control (common detail 3). Reproduced when, under one\n    correction reading, every randomization other than spike swapping gives a lower median and a\n    corrected p below 0.05, and Poisson randomization is among the two largest median decreases.\n    The swap comparison is judged in fig12a-swap-preserves-complexity.\n- id: fig10b-susceptibility-randomization\n  statement: Culture susceptibility decreases under randomization, most under the strongest forms such\n    as Poisson randomization.\n  source: Results 3.3, paragraph 4; Figure 10B\n  quote: The complexity and susceptibility decreased most under the strongest forms of randomization\n    (e.g., Poisson randomization)\n  criterion: Susceptibility per recording by Eq. 14 (common detail 5). Test as\n    fig10a-complexity-randomization. Swapping and shuffling preserve A(t) and leave chi unchanged\n    (Figure 10 legend), so the claim is judged over the jitters, wrap and Poisson. Reproduced when,\n    under one reading of details 3 and 5, each of these gives a lower median with corrected p below\n    0.05 and Poisson is among the two largest median decreases.\n- id: fig10c-curvature-randomization\n  statement: The culture shape collapse curvature decreases under randomization, so the collapsed\n    avalanches become flatter.\n  source: Results 3.3, paragraph 4; Figure 10C\n  quote: The shape collapse curvature decreased under randomization indicating that avalanches shape\n    collapses became flatter\n  criterion: Absolute curvature of the full-system shape collapse per recording (Methods 2.8, common\n    detail 6). Test as fig10a-complexity-randomization, judged over the jitters, wrap and Poisson\n    (swapping and shuffling preserve the profiles). Reproduced when, under one correction reading,\n    each of them gives a lower median with corrected p below 0.05.\n- id: figs8-complexity-susceptibility-correlation\n  statement: Across culture recordings, complexity and susceptibility are positively correlated\n    (correlation 0.23).\n  source: Results 3.3, paragraph 4; Figure S8\n  quote: We also found a correlation of 0.23 between the complexity and the susceptibility of the\n    recordings\n  depends_on:\n  - fig10a-complexity-randomization\n  - fig10b-susceptibility-randomization\n  expected:\n    quantity: correlation between complexity and susceptibility across recordings\n    value: 0.23\n    tolerance: 0.023\n  criterion: Over the real recordings. The coefficient is not named; Pearson is the reading, with\n    Spearman reported as a variant. Readings of the susceptibility as common detail 5.\n- id: fig11ac-fit-range-randomization\n  statement: The size and duration power-law fit ranges decrease under strong randomization such as\n    Poisson randomization, but increase slightly under 10-bin jittering.\n  source: Results 3.3, paragraph 5; Figure 11A and 11C\n  quote: We found that the fit ranges decreased for strong forms of randomization (e.g., Poisson\n    randomization), but showed slight increases for 10 bin jittering\n  criterion: Fit range per recording as log10(xmax/xmin) of the plparams support (Methods 2.7 defines\n    the ranges in decades). Test as fig10a-complexity-randomization, over the jitters, wrap and\n    Poisson (the fits are unchanged under swapping and shuffling, Figure 11 legend). Reproduced when,\n    for both size and duration, Poisson gives a lower median with corrected p below 0.05 and 10-bin\n    jitter gives a higher median than the real data; the jitter's significance is reported.\n- id: figs9-complexity-fit-range-correlation\n  statement: Across culture recordings, complexity is positively correlated with the size fit range\n    (0.296) and the duration fit range (0.197).\n  source: Results 3.3, paragraph 5; Figure S9\n  quote: We found a correlation of 0.296 between the complexity and the size fit ranges of the\n    recordings and a correlation of 0.197 between the complexity and the duration fit ranges of the\n    recordings\n  depends_on:\n  - fig10a-complexity-randomization\n  - fig11ac-fit-range-randomization\n  expected:\n  - quantity: correlation of complexity with size fit range\n    value: 0.296\n    tolerance: 0.0296\n  - quantity: correlation of complexity with duration fit range\n    value: 0.197\n    tolerance: 0.0197\n  criterion: Over the real recordings, Pearson as the reading, Spearman as a variant.\n- id: fig11bd-exponents-randomization\n  statement: The size and duration power-law exponents increase under randomization, as randomization\n    removes large or long avalanches and steepens the distributions.\n  source: Results 3.3, paragraph 5; Figure 11B and 11D\n  quote: We also found that the power-law fit exponents increased under randomization because\n    randomization tends to remove large or long avalanches and produce a shorter and steeper\n    distribution of avalanche sizes or durations\n  criterion: Full-system tau and alpha per recording from plparams after the cuts (as\n    fig8-subsampling-exponents). Test as fig10a-complexity-randomization, over the jitters, wrap and\n    Poisson. Reproduced when, under one correction reading, for both tau and alpha at least four of\n    the five give a higher median with corrected p below 0.05; partially reproduced for two or\n    three.\n- id: fig12a-swap-preserves-complexity\n  statement: Culture complexity does not change substantially under spike swapping, and real and\n    swapped complexity are strongly correlated with most recordings near the equality line.\n  source: Results 3.3, paragraph 6; Figure 12A; Figure 10A\n  quote: Surprisingly, we found that the complexity did not change substantially under spike swapping\n    (Figure 12A ) ... Furthermore, we found strong correlations between complexity in the real data\n    and complexity in the spike swapped data\n  depends_on:\n  - fig10a-complexity-randomization\n  criterion: A claim of absence, judged on the paper's test, the rank sum test of real against\n    swapped complexity across recordings with the false discovery rate control of Figure 10A\n    (common detail 3); reproduced when the corrected p is at least 0.05 under the reading used for\n    fig10a-complexity-randomization, not reproduced otherwise; the median relative change is given\n    either way. \"Strong correlation\" is not given a value; Pearson r of at least 0.7 is the reading\n    (a choice the paper does not make), Spearman as a variant. A paired signed-rank test is shown\n    as a variant.\n- id: fig12b-shuffle-lowers-complexity\n  statement: Culture complexity decreases somewhat under neuron shuffling; real and shuffled\n    complexity are strongly correlated, but real complexity tends to be greater.\n  source: Results 3.3, paragraph 6; Figure 12B\n  quote: Note that the complexity values were strongly correlated, but complexity in the real data\n    tended to be greater than the complexity in the shuffled data\n  depends_on:\n  - fig10a-complexity-randomization\n  criterion: Shuffling as Methods 2.5 (identities redrawn uniformly over all neurons at each bin);\n    the toolbox's swap2 is shown as a variant. Reproduced when real complexity exceeds shuffled\n    complexity in more than half of the recordings, the rank sum test of Figure 10A gives a\n    corrected p below 0.05, and the correlation is strong as read in\n    fig12a-swap-preserves-complexity.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/crcns-hc-8/10.3389-fphys.2016.00425.yaml paper/10.3389-fphys.2016.00425.txt; grep -n -E "[^ ]: " claims/crcns-hc-8/*.yaml | grep -v -E "^[0-9]+:\s*(-\s)?[a-z_]+: " | head; grep -n -E "—|rather" claims/crcns-hc-8/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd claims/crcns-hc-8 && python3 - <<'E'
p='10.3389-fphys.2016.00425.yaml'
t=open(p).read()
t=t.replace("""  quote: total number of neurons across all recordings: 39,529). Most recordings yielded
    approximately 100""","""  quote: Most recordings yielded approximately 100""")
open(p,'w').write(t)
import yaml
d=yaml.safe_load(t)
def walk(o):
    if isinstance(o,dict):
        for v in o.values(): yield from walk(v)
    elif isinstance(o,list):
        for v in o: yield from walk(v)
    elif isinstance(o,str): yield o
for s in walk(d):
    if ': ' in s or '—' in s or 'rather' in s: print(repr(s[:100]))
print(len(d['claims']))
E
cd ../.. && python tools/claims_check.py claims/crcns-hc-8/10.3389-fphys.2016.00425.yaml paper/10.3389-fphys.2016.00425.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd claims/crcns-hc-8 && python3 - <<'E'
p='10.3389-fphys.2016.00425.yaml'
t=open(p).read()
old="""  quote: Most recordings yielded approximately 100"""
new="""  quote: "total number of neurons across all recordings: 39,529). Most recordings yielded
    approximately 100"""
assert old in t
t=t.replace(old,new)
t=t.replace("""roughly 0.05–20 Hz
  expected:
  - quantity: number of recordings""","""roughly 0.05–20 Hz"
  expected:
  - quantity: number of recordings""")
open(p,'w').write(t)
E
cd ../.. && python tools/claims_check.py claims/crcns-hc-8/10.3389-fphys.2016.00425.yaml paper/10.3389-fphys.2016.00425.txt && grep -n -A3 "total number of neurons across" claims/crcns-hc-8/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/crcns-hc-8/10.3389-fphys.2016.00425.yaml` with 27 claims, and all 27 quotes pass `tools/claims_check.py` with 0 problems.

**What I read**
- **Paper:** the version of record (PMC5037237), the Methods 2.1 to 2.11, the Results, the Discussion and all the figure legends.
- **Supplement:** Data_Sheet_1, Figures S1 to S9 with their text.
- **Equations:** the supplied text leaves out Equations 1 to 14. I took them from the MathML in the PMC XML (fetched through NCBI eutils) and copied the ones the criteria use into the opening comment.
- **Code:** the paper links code only as "http://www.nicholastimme.com". From that site I read NCC Toolbox Version 1 (June 2016); its sha256 is recorded in the file. It holds the toolbox functions but not the scripts the authors ran on the cultures, which are not published.

**Counts**
- 27 claims, all with quotes. 9 are simulations (chain model, Bethe lattice, cortical branching model) and 18 use the culture data.
- No statistics are recorded. The paper prints no p-values; Figures 10 and 11 give only a star key (rank sum test with false discovery rate control), and the stars themselves could not be read.
- 7 claims have expected values: the peak at p_trans 0.265, the all-time-bins peak at 0.28, the counts of 435 recordings and 39,529 neurons (tolerance 0, since they are exact properties of the data), about 100 neurons per recording, ISI about 7 ms, about 10,000 avalanches, and the correlations 0.23, 0.296 and 0.197.
- All 27 claims have a criterion.

**Where the code settled a choice**
- The occurrence cut drops each size or duration value seen fewer than 20 times, one by one (as the toolbox demo does).
- Power-law fit ranges are searched largest first; surrogate count 500, acceptance at p of 0.2 or more.
- The complexity correction subtracts data randomized by permuting each neuron's time bins, then cuts at the first peak.
- The shape collapse searches 1/σνz from 0 to 4 at 0.001 precision.

**Details the paper leaves open, with the readings named**
- **Model p_trans grid:** the Methods print "increments of 0.05", which gives three values and cannot place a peak at 0.265. Readings: steps of 0.005 or 0.01.
- **Sub-sampling layout:** either 30 sub-samples at evenly spaced sizes, or 30 at each size from 40% to 100%.
- **Excluded recordings:** the "too few avalanches" threshold is not stated. Readings: exclude recordings where the size, duration or shape-collapse cuts leave nothing, or keep all.
- **False discovery rate method:** the paper cites both Benjamini-Hochberg and Benjamini-Yekutieli.
- **Susceptibility:** Eq. 14 as printed, var(A/N), or N·var(A/N). The second fits the 0 to 5 axis of Figure S8.
- **Curvature sign:** the code's 2a is negative for arched profiles, but the paper reports positive values. I used the absolute value.
- **Basic branching ratio:** I followed the Methods, Eq. 11, the time average of A(t+1)/A(t). The code computes a regression slope instead, which is shown as a variant.
- **"Slightly below 1":** within 0.05 or within 0.1 of 1.
- **"Strong" correlation:** read as Pearson r ≥ 0.7, with Spearman as a variant. This threshold is my choice, and the criterion says so.
- **"Most ... around":** the median or the histogram mode.
- **Smaller choices:** rounding the ISI bin, the number of Bethe lattice runs, and how to measure the curvature of the Figure 6 distributions. These are marked as standard choices or as measures the paper does not define.

**Missing from what was supplied**
- There is no PDF of the main article. So the per-exponent means and SDs in Figure 8, the Figure 9 histograms, the significance stars of Figures 10 and 11, and the list of excluded recordings in Figure 2B are unread. The claims on those figures are judged by direction only, with no numeric targets. Supplying the main PDF would let a reader add those values.
- The equations are missing from the supplied text, as noted above.

Nothing is committed.

## End of run

32 turns, 5 minutes, $2.15 at API prices, result: success.
