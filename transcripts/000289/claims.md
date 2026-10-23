# 000289 · claims · run 39988923123

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ claims/000289/ paper/ 2>&1
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '/^## Reader/,/^## Author/p' docs/protocol.md | sed -n '50,400p'; ls claims/001453/ claims/000289/ paper/
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/*.yaml | head -250; wc -l paper/*.txt; head -30 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat paper/10.1073-pnas.2210622120.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1073-pnas.2210622120.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && fold -s -w 4000 paper/10.1073-pnas.2210622120.txt > p.txt && wc -c p.txt && wc -l p.txt && grep -n -o -i "imaging\|EPG\|calcium\|GCaMP\|Basnak\|github\|dandi\|code avail\|data avail\|Fig. 5\|Fig. 6\|Supplementary\|SI Appendix, Fig. S[0-9]*" p.txt | sort | uniq -c | sort -rn | head -60
```

Result: not kept, because it reads the paper's text.

**Agent**

Reading the paper text in chunks: the paper is a theory paper (Bayesian ring attractor), with a supplement that has many lines.

**Agent calls Bash**

```bash
cd $TMPDIR && awk 'NR>=1 && NR<=120' p.txt | cut -c1-4000 | tail -c +51000 | head -c 60000
```

```
<persisted-output>
Output too large (39.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/ad848add-a194-4cc9-ab55-5ad53d50736f/tool-results/bgcmc41ud.txt

Preview (first 2KB):
y task. Recent models for such tasks attribute memory recall errors to the stochastic emission of a limited number of spikes ( 7 , 53 ). As in our network, neural noise can be averaged out once the network has a sufficiently large number of neurons; for this reason, memory errors can be attributed only to the noise of individual neurons in small networks with few neurons. Significant memory errors in larger Bayesian ring attractors thus have to result from other sources of noise, such as imperfect connectivity weights, or correlated input noise from, e.g., shared inputs, that fundamentally limits the amount of information that these inputs provide to the network ( 54 ). In the brain’s HD system, the internal estimate of HD is based on not only HD observations (visual landmarks, etc.) but also angular velocity observations. The process of integrating these angular velocity observations over time is called angular path integration. Angular path integration is inherently noisy, and therefore, uncertainty will grow progressively when HD observations are lacking. Our Bayesian ring attractor network is notable in explicitly treating angular path integration as a problem of probabilistic inference. Each angular velocity observation has limited reliability, and this causes the bump amplitude to decay in our network as long as HD observations are absent, in a manner that well approximates the certainty decay of an ideal observer. In this respect, our network differs from previous investigations of ring attractors having variable bump amplitude ( 55 ). Our work makes several testable predictions. First, we predict that the HD system should contain the connectivity motifs required for a Bayesian ring attractor. Our analysis of Drosophila brain connectome data suppo
[... 3 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/ad848add-a194-4cc9-ab55-5ad53d50736f/tool-results/bgcmc41ud.txt"
}
```

```
1	y task. Recent models for such tasks attribute memory recall errors to the stochastic emission of a limited number of spikes ( 7 , 53 ). As in our network, neural noise can be averaged out once the network has a sufficiently large number of neurons; for this reason, memory errors can be attributed only to the noise of individual neurons in small networks with few neurons. Significant memory errors in larger Bayesian ring attractors thus have to result from other sources of noise, such as imperfect connectivity weights, or correlated input noise from, e.g., shared inputs, that fundamentally limits the amount of information that these inputs provide to the network ( 54 ). In the brain’s HD system, the internal estimate of HD is based on not only HD observations (visual landmarks, etc.) but also angular velocity observations. The process of integrating these angular velocity observations over time is called angular path integration. Angular path integration is inherently noisy, and therefore, uncertainty will grow progressively when HD observations are lacking. Our Bayesian ring attractor network is notable in explicitly treating angular path integration as a problem of probabilistic inference. Each angular velocity observation has limited reliability, and this causes the bump amplitude to decay in our network as long as HD observations are absent, in a manner that well approximates the certainty decay of an ideal observer. In this respect, our network differs from previous investigations of ring attractors having variable bump amplitude ( 55 ). Our work makes several testable predictions. First, we predict that the HD system should contain the connectivity motifs required for a Bayesian ring attractor. Our analysis of Drosophila brain connectome data supports this idea; we expect similar network motifs to be present in the HD networks of other animals, such as that of mice ( 15 , 19 ), monkeys ( 56 ), humans ( 57 ), or bats ( 58 ). In the future, it will be interest
[... 101 more lines not kept]
```

**Agent**

The published PNAS version so far is pure theory. Checking the supplement and the preprint for the imaging experiments.

**Agent calls Bash**

```bash
cd $TMPDIR && grep -n -i "imaging\|calcium\|GCaMP\|two-photon\|EPG\|fly\b\|flies" p.txt | cut -c1-300 | head -40; echo ----; head -8 paper/10.1101-2021.12.17.473253.txt | cut -c1-1500; wc -c paper/10.1101-2021.12.17.473253.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper && fold -s -w 3000 10.1101-2021.12.17.473253.txt > $TMPDIR/pre.txt; grep -n -i -o ".\{150\}\(imaging\|calcium\|GCaMP\|two-photon\|dandi\|github\|zenodo\).\{150\}" $TMPDIR/pre.txt | head -40
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
grep -c "" $TMPDIR/pre.txt; grep -n -i "imaging\|calcium\|GCaMP\|photon\|dandi\|github\|zenodo\|experiment\|reliab" $TMPDIR/pre.txt | cut -c1-200 | head -40
```

```
349
11:Efficient navigation requires animals to track their position, velocity and heading direction (HD). Bayesian inference provides a principled framework for estimating these quantities from unreliabl
15:Navigating a foreign city without a map requires continuous monitoring of one’s current heading direction (HD). If we attempt to track our heading solely by ‘dead reckoning’ (integrating all our tu
21:The experimental accessibility and well-understood connectivity of the Drosophila CX ( Scheffer et al. 2020 ; Hulse et al. 2021 ) make it a compelling model network to seek a biological implementat
23:In what follows, we will address how ring-attractor networks, like the one in the Drosophila CX, could maintain and update a Bayesian HD estimate, and how they strategically use uncertainty for thi
31:An animal’s heading direction estimate is informed by two qualitatively different types of sensory inputs ( Fig. 1a ). On the one hand, the animal’s internal compass might receive self-turning sign
49:Here, we formulate the task of dynamically tracking HD with these two types of input as a dynamic Bayesian inference task, ensuring that unreliable sensory input is properly accounted for. We assum
63:When navigating, absolute heading information, like a GPS reading, helps to calibrate the internal compass. To weigh the reliability of such information against the current HD estimate’s certainty,
65:In our vector representation, including absolute heading information corresponds to adding an absolute heading information vector to the current belief vector ( Fig. 1d ; see Methods). The directio
67:In a dynamic setting, both angular velocity and absolute HD observations are available to the ideal observer as a continual stream. That is, at every point in time, the belief is updated according 
101:Careful tuning of the network parameters yields a class of networks that, in the limit of infinitely many neurons, exactly implements the circular Kalman filter (see Methods for detai
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i "simulat\|elsewhere\|with_inputs\|with_labels\|theor\|model" docs/protocol.md | head -40; ls docs; ls tools
```

```
137:     `with_labels`, `with_inputs` or `elsewhere` (step 4, and author, step
145:paper relies on outside data (a model, a reference dataset, measurements of
205:4. Decide what comes from outside the dataset. Data from elsewhere may be
214:     `data: with_labels`, `data: with_inputs` or `data: elsewhere`. The
215:     `with_inputs` and `elsewhere` claims are counted apart, each group on
217:   - `with_labels` is for outside sources that only name or map codes the
239:   - `elsewhere` is for a claim whose data the dataset does not hold at
248:   - The notes of a `with_inputs` claim say which side a difference comes
259:     `data: elsewhere` instead (step 4).
319:  runs many small model fits, limit linear-algebra threads to one.
387:  data. One session of four, a substituted model, a threshold the paper does
406:- **`provenance`**: who is accountable, and for an agent the harness, model
agents
archives.md
conversion-tracker.md
design.md
encore.md
fixing-conversions.md
pilot-notes
pilot-notes.md
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 200,265p docs/protocol.md; grep -rn -i "simulat\|theory paper\|no experiment" docs/pilot-notes.md docs/design.md | head -20; grep -rln "elsewhere" claims | head
```

```
3. Choose the version to pin. Pin the version the paper cites, as the claims
   file gives it. If it cites none, pin the most recent published version,
   unless an earlier one matches the claims file's description better. Say
   why in the notebook's header. If versions differ in content the analysis
   uses, show the difference.
4. Decide what comes from outside the dataset. Data from elsewhere may be
   used only when the claims file says the paper relies on it, it is public,
   and it is pinned: a DOI, or a repository at a commit. Record each under
   `inputs` in the attempt. A claim whose outside input is not public is
   blocked with `data_missing`, and its notes say where you looked.

   The registry judges the dataset, so claims that use outside data are
   kept apart:
   - Each claim says what its test uses: `data: dataset` (the default),
     `data: with_labels`, `data: with_inputs` or `data: elsewhere`. The
     `with_inputs` and `elsewhere` claims are counted apart, each group on
     its own; the others count towards what is said about the dataset.
   - `with_labels` is for outside sources that only name or map codes the
     dataset already holds, such as stimulus names for its stimulus codes.
     They bring in no measurements. A link claim must confirm the names, and
[... 56 more lines not kept]
```

**Agent**

Let me look at a precedent where the paper is computational (000294, Neural Computation).

**Agent calls Bash**

```bash
head -120 claims/000294/10.1162-neco_a_01672.yaml; grep -n "data:\|where:\|kind:" claims/000294/*.yaml | sort | uniq -c | head; grep -n "^checks\|^questions" -A30 claims/000294/*.yaml | head -50
```

```
# Claims for Buccino, Damart, Bartram, ... Hierlemann & Van Geit (2024) on dandiset 000294.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
# protocol pilot-10 as stated in docs/protocol.md.
#
# Text read: the version of record (Neural Computation 36, 1286-1331, 2024, CC BY 4.0), from the
# PDF supplied to paper/ and its text extraction: main text, Methods (section 5), Tables 1 to 5
# and the appendix (Figures 9 and 10). The paper has no separate supplement.
#
# Code read: github.com/alejoe91/multimodalfitting at commit 24e8e6168b2d5be45c551bcc08b62fde187d01c7
# (2025-04-12), the repository the Data and Code Availability section names. It holds the package
# (ecode protocols, feature extraction, the patch and HD-MEA sync and patch-triggered average in
# mea_patch/mea_patch.py, model and evaluator construction), the optimization script
# (scripts/run_optimizations.py, 20 offspring and 600 generations by default), the notebooks that
# make the figures (notebooks/ground-truth and notebooks/experimental/cell1, cell2, notebook
# outputs stripped), and cell_models/ with the ground-truth model (hay_ais) and the two
# experimental models: morphology_corrected.swc, mechanisms, parameters, and fitting/efeatures with
# the extracted feature and protocol files, the thresholded probe and the template_BPO.npy
# template of each cell. No optimization results (checkpoints, runs.pkl) are in the repository.
# The BluePyOpt extensions are in BluePyOpt pull request 385, release 1.13.88 (not read).
# In the code, cell 1 is "cell1_211006_3148" and cell 2 is "cell1_211011_3436" (the cell1 and
[... 126 more lines not kept]
```

**Agent**

The precedent marks simulation claims `data: elsewhere` with the code repository under `where`. Now fetching the dataset's archive description (title/description only) and the paper's Zenodo code.

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000289/ | python -c "import json,sys;d=json.load(sys.stdin);print(json.dumps(d,indent=1)[:1500])"; curl -s "https://api.dandiarchive.org/api/dandisets/000289/versions/" | python -c "import json,sys;d=json.load(sys.stdin);print([ (v['version'],v['modified']) for v in d['results']])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000289/versions/0.240801.1040/info/ | python -c "
import json,sys;d=json.load(sys.stdin);m=d['metadata']
for k in ['description','relatedResource','keywords','about','studyTarget','protocol','citation']: print(k, json.dumps(m.get(k),indent=0)[:2000])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s https://api.biorxiv.org/details/biorxiv/10.1101/2021.12.17.473253 | python -c "
import json,sys;d=json.load(sys.stdin)
for c in d['collection']: print(c['version'],c['date'],c['title'],'|',c['authors']); print(c['abstract'][:1500]); print()"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -sL https://zenodo.org/api/records/7615975 | python -c "
import json,sys;d=json.load(sys.stdin);print(d.get('doi'),d['metadata']['title'],d['metadata'].get('version'),d['metadata'].get('publication_date'));print(d['metadata'].get('related_identifiers'))
for f in d['files']: print(f['key'],f['size'],f['links']['self'])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && curl -sL -o code.zip https://zenodo.org/api/records/7615975/files/DrugowitschLab/BayesianRingAttractor-v1.0.zip/content && unzip -q -o code.zip -d code && find code -type f | head -80 && md5sum code.zip
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/code/*/ && cat README.md data_raw/figure2i/README.md; wc -l *.py; grep -n "def \|kappa_phi\|kappa_v\|N =\|T =\|dt =\|P =\|nTrials\|numTrials" performance_scan_figure2i.py performance_scan_figure3d.py performance_scan_figure3f.py performance_scan_figure4g.py | head -80
```

````
# Code for "Bayesian inference in ring attractor networks"

This repo contains the code for simulations and figures in

Anna Kutschireiter, Melanie A Basnak, Rachel I Wilson, and Jan Drugowitsch (2023). Bayesian inference in ring attractor networks. Proceedings of the National Academy of Sciences.


## Code structure and environment setup
* `root` - python scripts and jupyter notebooks containing the main code to reproduce figures
* `/data_processed` - `analysed' artificial data
* `/data_raw` - raw data, empty. 

### Python environment

Our code uses Python 3.9.7. 
Packages we used are listed in the file `environment.yml`.
These can either be installed by hand, or alternatively installed in a virtual environment with name `fltenv` by running
```
conda env create -f environment.yml
```
[... 117 more lines not kept]
````

**Agent**

Code is the Zenodo v1.0 snapshot of DrugowitschLab/BayesianRingAttractor (commit a9db6f9): simulations only, no imaging analysis. Checking a few parameters against the Methods.

**Agent calls Bash**

```bash
cd $TMPDIR/code/*/ && sed -n 1,45p performance_scan_figure2i.py; sed -n 20,78p performance_scan_figure3f.py
```

```
import sys
import numpy as np
import circularFiltering as flt
from time import time

kappa_z_array = np.array([0.01,0.03,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,2,3,4,5,6,7,8,9,10,30,100])

# choose a kappa_z according to system variable
kappa_z = kappa_z_array[int(sys.argv[1])]

# choose kappa according to input variable
kappa = float(sys.argv[2])

# pass the number of iterations
nIter = 10000

# where to save
filename = "data_raw/figure2i/k="+str(kappa)+"_kz="+str(kappa_z)

# model parameters
[... 85 more lines not kept]
```

**Agent**

Now the supplement's figure legends, for the SI findings.

**Agent calls Bash**

```bash
cd $TMPDIR && grep -n "^Fig\. S\|^Figure S\|Fig\. S[0-9]\.\|^[0-9]\+\. [A-Z][a-z]" p.txt | head -40; grep -n -i "supplementary information\|SI Appendix\b" p.txt | head -5
```

```
627:1. Circular Kalman filtering
1160:histograms in Fig. S5.
1165:2. Neural encoding example: encoding of the von Mises distribution with a linear probabilistic population code
1410:3. Details on Bayesian ring attractor dynamics and parameter tuning
1777:4. Details on Drosophila-like network
2670:5. The impact of neural noise on inference dynamics
2816:2. Applying Itô’s Lemma to this mapping results in
3163:6. Supplementary Figures
3289:Fig. S1. Encoding the HD with linear probabilistic population codes. a) Tuning curves with respect to encoded HD estimate for small values of encoded certainty κt
3331:Fig. S2. Network inference performance is mostly independent of the number of neurons N in the Bayesian ring attractor network. Here, for each value of the
3366:Fig. S3. The weight with which a single observation contributes to the HD estimate varies with informativeness of both the HD observations and the current HD
3411:Fig. S4. Neural noise changes the optimal fixed point amplitude and decay speed. We simulated a network of N = 64 neurons with different levels of additive Gaussian noise
3480:Fig. S5. Visualizing the HD tracking perfomance measure. To provide a better intuition for the used HD tracking performance measure we here show how a specific
10:memory and its associated uncertainty. Although we focus on the brain’s HD system as a concrete example, our results are relevant to any other brain system that encodes a circular or periodic variable. Results Circular Kalman Filtering: A Bayesian Algorithm for Tracking a Circular Variable. We begin by asking how an ideal observer should dynamically integrate uncertain evidence to estimate a circular variable, specifically head direction ϕ t . Additional information being absent, the ideal observer assumes that HD follows a random walk or diffusion on a circle: across small consecutive time steps of size δ t , the current HD ϕ t is assumed to be drawn from a normal distribution, ϕ t | ϕ t − δ t ∼ 𝓝 ( ϕ t − δ t , δ t / 
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -n 3289,3300p p.txt; sed -n 3331,3340p p.txt; sed -n 3366,3372p p.txt; sed -n 3411,3420p p.txt; sed -n 3480,3486p p.txt; sed -n 1777,1800p p.txt
```

```
Fig. S1. Encoding the HD with linear probabilistic population codes. a) Tuning curves with respect to encoded HD estimate for small values of encoded certainty κt
are cosine-shaped. Here, we show tuning curves of 8 example neurons with κt = 1 (colors indicate preferred HD φi). b) Tuning curves with respect to HD estimate for
large values of encoded certainty κt are von-Mises shaped (same 8 example neurons as in a, but for κt = 10). c) Von Mises probability densities for different values of
encoded certainty κt and fixed mean μt = π
2 . Note that the density sharpens around the mean with increasing certainty. Inset shows vector representation of a von Mises
distribution with mean μt = π
2 , and, respectively, κt = 10 and κt = 1. d) Population activity profile (average neural firing rate conditioned on HD estimate μt and certainty
κt) encoding the von Mises densities with mean μt = π
2 and certainty κt = 1. Neurons are sorted by preferred HD φt. Colored dots correspond to activity of neurons with
tuning curves as in a). The phasor representation of the neural activity (inset) matches the vector representation of the encoded von Mises distribution in c. e) Population
activity profile encoding the von Mises densities with mean μt = π
2 and certainty κt = 10. f) Left: The amplitude (Max-Min) of the activity profile scales (approximately)
Fig. S2. Network inference performance is mostly independent of the number of neurons N in the Bayesian ring attractor network. Here, for each value of the
observation reliability κz and number of neurons in the network N we compute the circular average distance of the network’s HD estimate μT from the true HD φT at the end
of a simulation of length T = 20 from P = 10′000 simulated trajectories. The blue line (hidden below other lines) shows the performance of the quadratic approximation to
the circular Kalman filter that the networks aim to implement. The network parameters of the single-population network in Eq. [S49] were those of the
[... 55 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -n -i "neuprint\|hemibrain\|v1.2" p.txt | cut -c1-400; grep -rn -i "neuprint\|hemibrain" code/*/*.py code/*/*.ipynb | cut -c1-200 | head
```

```
18:κ t ( SI Appendix ). The derivations revealed that, irrespective of the form of the neural noise (additive, multiplicative, etc.), this noise has two effects. First, it causes an unbiased random diffusion of μ t and, thus, an increasingly imprecise memory of the HD estimate. Second, it causes a positive drift and random diffusion of κ t , which, if the drift is not accounted for, results in an 
24:v t and HD observations z t , enters in the same way as before, the network implements the quadratic approximation to the circKF, Eqs. 8 and 11 . General ring-attractor networks with fixed point κ * and decay speed β. In the absence of HD observations ( I t = 0), the amplitude dynamics in Eq. 14 has a stable fixed point at κ ∗ = w sym − 1 / τ w quad and no preferred phase, making it a ring-attr
26:that by setting higher-order recurrent connectivities accordingly, other profile shapes could be realized, without affecting the validity of our analysis from the neural activity vector r t , we retrieved the natural parameters x t with a decoder matrix A = (cos( ϕ ),sin( ϕ )) T , such that x t = A ⋅ r t , and subsequently computed the position of the bump by ϕ t = arctan2( x 2 , x 1 ) and the
Shell cwd was reset to
```

**Agent calls Bash**

```bash
sed -n 185,215p claims/000294/10.1162-neco_a_01672.yaml; python tools/claims_check.py -h 2>&1 | head -20; grep -n "required\|allowed\|keys\|'data'\|where" tools/claims_check.py | head -30
```

```
range, widened by 10% of each bound.
- id: fig6-ais-from-dendrite
  statement: In both cells the axon initial segment does not leave the soma but a dendrite (an
    axon-bearing dendrite).
  source: Results 3.3, paragraph 2; Figure 6
  quote: Moreover, for both cells, the AIS did not originate directly from the soma but from one of
    the dendrites, which is termed an axon-bearing dendrite (ABD
  data: elsewhere
  where: NeuroMorpho.org Buccino_Hierlemann_Cell1 and Buccino_Hierlemann_Cell2; GitHub
    alejoe91/multimodalfitting at commit 24e8e61, cell_models/<cell>/morphology_corrected.swc
  criterion: In each reconstructed morphology (SWC), the AIS is the path labeled "apic" (type 4,
    Methods 5.7.2). Reproduced when, in both cells, the first AIS point's parent is a dendrite
    point (type 3), not the soma (type 1).
- id: gt-rheobase
  statement: The ground-truth model's rheobase, estimated with a 270 ms step, is 150 pA.
  source: Results 3.2, paragraph 4
  quote: All current amplitudes were computed with respect to the neuron's rheobase current
    (estimated using a 270 ms step). For our groundtruth model, the rheobase current was 150 pA
  data: elsewhere
  where: GitHub alejoe91/multimodalfitting at commit 24e8e61, cell_models/hay_ais (model) and
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));c=s['\$defs'] if '\$defs' in s else s.get('definitions');print(json.dumps(s,indent=0)[:5000])"
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
[... 188 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=0)[:3500])"
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
[... 82 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/*/ && python -c "
import numpy as np,glob
for f in sorted(glob.glob('data_processed/*.npz'))+['data_processed/figure3f/sigma=0.0.npz']:
    d=np.load(f,allow_pickle=True); print(f,{k:d[k].shape for k in d.files})
"; for nb in Figure2i.ipynb "Figure3b,c,e,d_FigureS3.ipynb" "Figure3f_FigureS4.ipynb" "Figure4g,h.ipynb"; do echo "== $nb"; python -c "
import json,sys
nb=json.load(open(sys.argv[1]))
for c in nb['cells']:
    if c['cell_type']=='code':
        s=''.join(c['source'])
        if any(k in s for k in ['np.load','kappa_star','beta','argmax','argmin','prior','lognorm','35','perf']): print('---');print(s[:1500])
" "$nb"; done 2>&1 | head -300
```

```
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import numpy as np,glob
ModuleNotFoundError: No module named 'numpy'
== Figure2i.ipynb
---
kappa_z_array = ([1.e-02, 3.e-02, 1.e-01, 2.e-01, 3.e-01, 4.e-01, 5.e-01, 6.e-01,
       7.e-01, 8.e-01, 9.e-01, 1.e+00, 2.e+00, 3.e+00, 4.e+00, 5.e+00,
       6.e+00, 7.e+00, 8.e+00, 9.e+00, 1.e+01, 3.e+01, 1.e+02])

preprocess = False # only set to True if you want to re-run preprocessing on data in /data_raw

path_processed = 'data_processed/'
path_raw = 'data_raw/figure2i/'

if preprocess:

    # # make unique list of parameter values
    fileNames = glob.glob(os.path.join(path_raw, "k=*.npz"))
    kappa_array = np.array( [ re.findall('(?<=k=)(.*)(?=_)', name) for name in fileNames ] )[:,0]
[... 285 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/*/ && python -c "
import json,sys
nb=json.load(open('Figure3f_FigureS4.ipynb'))
cs=[c for c in nb['cells'] if c['cell_type']=='code']
for c in cs[3:]:
    print('---');print(''.join(c['source'])[:2500])
" | head -150; python -c "
import json
nb=json.load(open('Figure4g,h.ipynb'))
for c in nb['cells']:
  if c['cell_type']=='code': print('---');print(''.join(c['source'])[:1200])
" | head -90
```

```
---
kappa_star_array = np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,
                            1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 
                            2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 
                            3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.2, 4.4, 4.6, 4.8, 5.0])
beta_array = np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9, 1, 2 ,4 ,8])
kappa_z_array = np.array([1.e-02, 3.e-02, 1.e-01, 2.e-01, 3.e-01, 4.e-01, 5.e-01, 6.e-01,
       7.e-01, 8.e-01, 9.e-01, 1.e+00, 2.e+00, 3.e+00, 4.e+00, 5.e+00,
       6.e+00, 7.e+00, 8.e+00, 9.e+00, 1.e+01, 3.e+01, 1.e+02])

N = 64

sigmaN_array = np.array([0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.,15,20])
max_MSE = np.zeros(len(sigmaN_array))
noretuning_MSE = np.zeros(len(sigmaN_array))
sig_to_noise = np.zeros(len(sigmaN_array))
noretuning_sig_to_noise = np.zeros(len(sigmaN_array))

# parameters for colorbar (comparable across levels)
vmin = 0.25
[... 138 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/*/ && python -c "
import json
nb=json.load(open('Figure2h.ipynb'))
for c in nb['cells']:
  if c['cell_type']=='code': print('---');print(''.join(c['source'])[:1800])
" | head -120; grep -n "def vM_Projection_Run\|def vM_Projection_quad_Run\|def RNN_filter_Run\|def no_uncertainty_filter_Run\|def generateData\|def xi_fun_inv" -A6 circularFiltering.py | head -70
```

```
---
%load_ext autoreload
%autoreload 2

import numpy as np
import matplotlib.pyplot as plt
import circularFiltering as flt
import matplotlib
matplotlib.rcParams.update({'font.size': 14,
                            'pdf.fonttype': 42,
                            'ps.fonttype': 42})
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
---
####### simulation parameters
np.random.seed(42)
T = 15
dt = 0.01
t = np.arange(0,T,dt)
kappa_phi = 1 # inverse diffusion constant
[... 148 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/*/ && python -c "
import json
nb=json.load(open('Figure3b,c,e,d_FigureS3.ipynb'))
for c in nb['cells']:
  s=''.join(c['source'])
  if 'weight' in s.lower() or 'fisher' in s.lower() or 'arctan' in s: print('---');print(s[:2500])
" | head -120
```

```
---
fig, (ax1) = plt.subplots(ncols=1,nrows=1,figsize = (5,4),sharex=True,tight_layout=True)
dt = 0.1
kappa_array = np.arange(0.2,10,0.01) # own uncertainty right before update
kappa_z_array =  np.arange(0.1,80,0.1) # information rate of observations
alpha_array = np.array( [ flt.xi_fun_inv(kappa_z * dt) for kappa_z in kappa_z_array] )
kappa, alpha = np.meshgrid(kappa_array, alpha_array)
dmu = np.arctan2(alpha,kappa)
CS = ax1.contourf( flt.xi(kappa_array), kappa_z_array * dt, dmu/(0.5*np.pi), levels=10, cmap='Purples')
ax1.plot([flt.xi(best_kappastar),flt.xi(best_kappastar)],[0,10],color='green',linewidth=3)
ax1.plot(flt.xi(vonMises_stats[0,:,2]), kappa_z_array_old * dt,label='Projection Filter',linewidth=2,color='orange')
ax1.plot(flt.xi(vonMises_q_stats[0,:,2]), kappa_z_array_old * dt,label='Q Apppr',linewidth=2,color='blue')

ax1.set_xlim([flt.xi(kappa_array[0]),flt.xi(kappa_array[-1])])
ax1.set_ylim([kappa_z_array[0]*dt,kappa_z_array[-1]*dt])
cbar = plt.colorbar(CS)
cbar.set_label('Relative weight on HD observation')
ax1.set_xlabel('Fisher info of internal estimate')
ax1.set_ylabel('Fisher info per HD obs.')
ax1.set_title('Max update per observation')
[... 26 more lines not kept]
```

**Agent**

I have what I need from the code. Now pulling exact sentences for the quotes from the raw text.

**Agent calls Bash**

```bash
cd paper && for pat in "HD observations increase the observer.\{0,300\}" "This network exhibits a spatially.\{0,200\}" "Meanwhile, the amplitude of the bump accurately.\{0,250\}" "When the visual cue is removed.\{0,60\}" "The Bayesian ring attractor network tracks.\{0,420\}" "When HD observations have high reliability.\{0,400\}" "Even after this optimization.\{0,330\}" "The Bayesian ring attractor.s performance drops.\{0,120\}" "The update weight of the Bayesian.\{0,100\}" "A conventional ring attractor will assign.\{0,120\}" "only deviates from the circKF.\{0,80\}" "The network with the best performance.\{0,500\}" "Indeed, simulating a network of 64.\{0,200\}" "Indeed, doing so reduced.\{0,250\}" "For example, increasing the network size.\{0,120\}" "We found that this network achieves.\{0,200\}" "The connectivity profile of a recurrent.\{0,200\}" "Second, we predict that bump.\{0,320\}" "Network inference performance is mostly.\{0,120\}" "First, it causes an unbiased.\{0,400\}"; do grep -o "$pat" 10.1073-pnas.2210622120.txt | head -2; echo ====; done
```

```
HD observations increase the observer’s certainty if they are confirmatory (i.e., they indicate that the current estimate is correct or nearly so, Fig. 1 D ). Interestingly, however, if HD observations strongly conflict with the current estimate (e.g., if they point in the opposite direction), they actually decrease certainty ( Fig. 1 
====
This network exhibits a spatially localized bump whose position tracks HD, with an accuracy similar to that of the circular Kalman filter itself ( Fig. 2 H ). Meanwhile, the amplitude of the bump accurately tracks the fluctuating HD 
====
Meanwhile, the amplitude of the bump accurately tracks the fluctuating HD posterior certainty in the circular Kalman filter, reflecting how noisy angular velocity and HD observations interact to modulate this certainty, Eq. 2 . When the visual cue is removed, the bump amplitude decays toward base
====
When the visual cue is removed, the bump amplitude decays toward baseline ( Fig. 2 H ). In
====
The Bayesian ring attractor network tracks the true HD with the same accuracy ( T o p ; higher = lower average circular distance to true HD; 1 = perfect, 0 = random; M e t h o d s ) as the circular Kalman filter (circKF, Eqs. 1 and 2 ) if HD observations are reliable and, therefore, more informative but with slightly lower accuracy once they become less reliable, and therefore less informative. This drop co-occurs with an overestimate in the belief’s certain
====
When HD observations have high reliability, bump amplitude is high and accurately tracks HD certainty ( κ t ). Thus, in this regime, the network performs proper Bayesian inference ( Fig. 2 I ). Conversely, when HD observations have low reliability, bump amplitude is low but constant, because it is essentially pegged to its baseline value (the network’s attractor state). In this regime, bump amplitude exaggerates the HD posterior certainty
====
Even after this optimization of the conventional ring attractor, it does not rival the accuracy of the 
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 3331,3345p $TMPDIR/p.txt; cd $TMPDIR/code/*/ && python -c "
import json
nb=json.load(open('FigureS2.ipynb'))
for c in nb['cells']:
  s=''.join(c['source'])
  if 'N_array' in s or 'plot' in s: print('---');print(s[:1200])
" | head -50
```

```
Fig. S2. Network inference performance is mostly independent of the number of neurons N in the Bayesian ring attractor network. Here, for each value of the
observation reliability κz and number of neurons in the network N we compute the circular average distance of the network’s HD estimate μT from the true HD φT at the end
of a simulation of length T = 20 from P = 10′000 simulated trajectories. The blue line (hidden below other lines) shows the performance of the quadratic approximation to
the circular Kalman filter that the networks aim to implement. The network parameters of the single-population network in Eq. [S49] were those of the Bayesian ring attractor,
i.e. weven
1
= 1
τ +
1
κφ+κv , wodd
1
=
κv
κφ+κv vt, and wquad =
1
---
import numpy as np
import matplotlib.pyplot as plt
import circularFiltering as flt
import matplotlib
[... 45 more lines not kept]
```

**Agent**

Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/000289/10.1073-pnas.2210622120.yaml",
 "content": "# Claims for Kutschireiter, Basnak, Wilson & Drugowitsch (2023), \"Bayesian inference in ring\n# attractor networks\", PNAS 120, e2210622120, on dandiset 000289.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-23,\n# protocol pilot-10 as stated in docs/protocol.md.\n#\n# Text read: the version of record as served by Europe PMC (PMC9992764, CC BY-NC-ND), main text,\n# figure legends and Materials and Methods, with the SI Appendix (Appendix 01, PDF, extracted to\n# text in the same file): SI sections 1 to 6 and Figs. S1 to S5. The bioRxiv preprint version 1\n# (10.1101/2021.12.17.473253v1) is also under paper/; it was not used for the claims.\n#\n# Code read: Zenodo doi:10.5281/zenodo.7615975, \"DrugowitschLab/BayesianRingAttractor: Code as used\n# in 2023 PNAS paper\" v1.0 (GitHub DrugowitschLab/BayesianRingAttractor, tag v1.0, commit a9db6f9),\n# the deposit the Data Availability statement names. It holds the filters and the\n# single-population network (circularFiltering.py: generateData, vM_Projection_Run for the circKF,\n# vM_Projection_quad_Run for its quadratic approximation, no_uncertainty_filter_Run for the\n# conventional (fixed kappa*) attractor, RNN_filter_Run, PF_run), the Drosophila-like network\n# (network_filter.py), the scan scripts (performance_scan_figure2i, 3d, 3f, 4g, S2), one notebook\n# per figure, and the processed scan outputs the figures are drawn from (data_processed/\n# figure2i.npz, figure3d.npz, figure3f/sigma=*.npz, figure4g.npz, figureS2.npz,\n# vonMises_q_stats.npz). data_raw/ is empty. The code holds no imaging analysis and no\n# connectome query. Points where the code and the paper differ, used in the criteria below:\n#   - In Figs. 2I, 3B, 3C and 4G the curve labelled \"Bayesian ring attractor\" is the quadratic\n#     approximation of the circKF (vM_Projection_quad_Run), the network's first Fourier mode\n#     dynamics in the continuum limit, not a finite-N network simulation.\n#   - The scan scripts run 10,000 trajectories per setting (nIter); the Methods say P = 5,000.\n#   - performance_scan_figure4g.py uses dt = 0.001; the Methods say 0.01 for all simulations.\n#   - Figure2h.ipynb uses an information rate of 15 (comment \"called gamma_z in manuscript\"),\n#     cue off from 5 to 10 s, seed 42, N = 80; the Methods say gamma_z = 10/s.\n#   - Figure3f_FigureS4.ipynb divides performance by the particle filter reference (ref =\n#     0.6912447327304075), not by the noise-free network as the Fig. 3F legend says.\n#   - The scan scripts call generateData and the filters with the keyword kappa_y, while the\n#     functions in circularFiltering.py take kappa_v; a rerun needs that keyword renamed.\n# The weighted average across information rates (Methods, \"Performance measures\") is the\n# code's objective(): a normal density over log(rate) with mean 0.5 and SD 1, integrated by the\n# trapezoidal rule over the 23 rates 0.01 to 100.\n#\n# Data the paper describes. None recorded. Every result is a simulation of artificial data from\n# the generative model (HD diffusing on a circle with kappa_phi = 1, angular velocity\n# observations with kappa_v, HD observations with information rate gamma_z), with T = 20, dt =\n# 0.01, kappa_v = 1 unless stated, measured by the inference accuracy |m1| (circular average of\n# exp(i(mu_T - phi_T)) over trajectories). Fig. 4B uses the hemibrain connectome v1.2.1 (synapse\n# counts between EPG, Delta7 and PEN1 neurons), cited from Scheffer et al. 2020 and Hulse et al.\n# 2021. The paper has no imaging, behavior or stimulus data.\n#\n# The dandiset. Its archive title is \"Two-photon calcium imaging of EPG cells in Drosophila\n# Melanogaster presented with cues of varying reliability\", and its description says it holds\n# the data of \"Uncertainty and learning in a biological ring attractor\" (Basnak et al., in\n# preparation): imaging, stimulus variables and behavior of flies shown cues of varying\n# reliability. Its related resources list bioRxiv 10.1101/2021.12.17.473253 version 4 and\n# github.com/mbasnak/analysis_code. The bioRxiv record of version 4 (2022-07-03, \"Bayesian\n# inference in ring attractor networks\") has the abstract of the version of record, and neither\n# that text nor the version of record reports experiments. So the dataset holds no data this\n# paper analyses. All findings below are simulation or connectome results (data elsewhere),\n# except the Discussion's prediction about bump amplitude and cue reliability, the one statement\n# of the paper the dataset could bear on; the paper does not test it and gives no experimental\n# method for it.\n#\n# How the simulation claims are tested. Each is judged on the paper's own released outputs in\n# data_processed/ (the README says the figure notebooks reproduce the plots from them), loaded\n# with the figure's notebook. A rerun of the scan scripts (with the keyword fix above, and fewer\n# trajectories if needed) is a variant, shown and not judged. Where the paper says \"similar\",\n# \"indistinguishable\" or \"close\" with no number, the criterion names the readings the text\n# allows; the outcome is the one all readings give.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000289\"\npaper: doi:10.1073/pnas.2210622120\nclaims:\n- id: fig1-conflict-decreases-certainty\n  statement: >-\n    In the circular Kalman filter, an HD observation consistent with the current estimate\n    increases certainty, while one that strongly conflicts with it (opposite direction)\n    decreases certainty.\n  source: Results, Circular Kalman Filtering, HD Observations, paragraph 1; Fig. 1 D and E\n  quote: >-\n    HD observations increase the observer’s certainty if they are confirmatory ... if HD\n    observations strongly conflict with the current estimate (e.g., if they point in the opposite\n    direction), they actually decrease certainty\n  data: elsewhere\n  where: >-\n    Zenodo doi:10.5281/zenodo.7615975 (BayesianRingAttractor v1.0, commit a9db6f9),\n    circularFiltering.py vM_Projection_Run\n  criterion: >-\n    The update is the vector addition of Fig. 1 D and E and the observation term of Eq. 9 (kappa\n    changes by kappa_z cos(z - mu) dt). From the code's circKF (vM_Projection_Run, kappa_phi = 1,\n    kappa_v = 1, dt = 0.01), take a state with certainty kappa_t (any of 1, 2, 5) and apply one step\n    with an HD observation at z = mu (confirmatory) and one at z = mu + pi (opposite), with an\n    observation reliability below kappa_t. Compare the certainty after the step with (a) the\n    certainty before it and (b) the certainty after the same step with no observation (kappa_z = 0).\n    Reproduced when, under both comparisons and every kappa_t, the confirmatory observation gives\n    higher and the opposite one lower certainty.\n- id: fig2h-bump-tracks-circkf\n  statement: >-\n    In a simulated Bayesian ring attractor of 80 neurons, the bump position tracks HD about as\n    accurately as the circular Kalman filter, the bump amplitude tracks the filter's certainty,\n    and when the visual cue is removed the amplitude decays toward its baseline.\n  source: Results, Neural Network Implementation, paragraph 6; Fig. 2H\n  quote: >-\n    This network exhibits a spatially localized bump whose position tracks HD, with an accuracy\n    similar to that of the circular Kalman filter itself ( Fig. 2 H ). Meanwhile, the amplitude of\n    the bump accurately tracks the fluctuating HD posterior certainty in the circular Kalman filter\n    ... When the visual cue is removed, the bump amplitude decays toward baseline\n  data: elsewhere\n  where: >-\n    Zenodo doi:10.5281/zenodo.7615975 (BayesianRingAttractor v1.0, commit a9db6f9),\n    Figure2h.ipynb with circularFiltering.py\n  criterion: >-\n    Run Figure2h.ipynb as released (seed 42, T = 15, dt = 0.01, kappa_phi = 1, kappa_v = 2, N = 80,\n    cue off from 5 to 10 s, information rate 15). The Methods give gamma_z = 10/s; run that as a\n    second reading of the cue strength. Bump position and amplitude are decoded as in the Methods\n    (x = A r, position arctan2(x2, x1), amplitude the vector length). The paper gives no number for\n    \"similar\" or \"accurately\"; readings for both cue strengths: (a) the mean absolute circular\n    difference between the network's and the circKF's HD estimates is smaller than the circKF's own\n    mean absolute error to the true HD, over the whole run; (b) the Pearson correlation between\n    bump amplitude and circKF certainty over the cue periods is at least 0.9. Decay: over the\n    darkness period (5 to 10 s) the bump amplitude falls and ends closer to the baseline kappa* = 1\n    (Methods, Bayesian ring attractor) than it started. Reproduced when the decay holds and (a) and\n    (b) hold under both cue strengths.\n- id: fig2i-accuracy-and-certainty-vs-reliability\n  statement: >-\n    The Bayesian ring attractor tracks HD with the same accuracy as the circular Kalman filter when\n    HD observations are reliable and with slightly lower accuracy when they are unreliable; in the\n    unreliable regime its certainty stays near its baseline and overestimates the filter's\n    certainty.\n  source: Fig. 2I legend; Results, Neural Network Implementation, paragraph 7\n  quote: >-\n    The Bayesian ring attractor network tracks the true HD with the same accuracy ... if HD\n    observations are reliable and, therefore, more informative but with slightly lower accuracy\n    once they become less reliable, and therefore less informative. This drop co-occurs with an\n    overestimate in the belief’s certainty\n  data: elsewhere\n  where: >-\n    Zenodo doi:10.5281/zenodo.7615975 (BayesianRingAttractor v1.0, commit a9db6f9),\n    data_processed/figure2i.npz with Figure2i.ipynb\n  criterion: >-\n    From figure2i.npz as Figure2i.ipynb reads it, compare the circKF (vonMises_stats) and the\n    Bayesian ring attractor (vonMises_q_stats) over the 23 information rates (0.01 to 100/s,\n    kappa_v = 1, T = 20). Accuracy is the stored |m1|, certainty the mean final kappa. The paper\n    names no rate that separates reliable from unreliable; readings for the reliable set: (a)\n    rates of 1/s and above, (b) rates of 3/s and above. \"Same accuracy\" readings: the absolute\n    difference is at most (i) 0.01 or (ii) 0.02 at every reliable rate. Reproduced when, under\n    every combination, the accuracies are the same on the reliable set, the attractor's accuracy is\n    below the circKF's at the lowest rates (0.01 to 0.1/s), and at those rates its mean certainty\n    is above the circKF's.\n- id: fig3b-bayesian-beats-conventional\n  statement: >-\n    A conventional ring attractor (fast decay to a fixed bump amplitude, with that amplitude\n    optimized) is less accurate than the Bayesian ring attractor at every HD observation\n    reliability, and reaches its accuracy only when observations are highly unreliable.\n  source: Results, Bayesian vs. Conventional Ring Attractors, paragraphs 2 and 3; Fig. 3B\n  quote: >-\n    Even after this optimization of the conventional ring attractor, it does not rival the\n    accuracy of the Bayesian ring attractor. The Bayesian attractor performs consistently better,\n    regardless of the amount of information available to the network\n  data: elsewhere\n  where: >-\n    Zenodo doi:10.5281/zenodo.7615975 (BayesianRingAttractor v1.0, commit a9db6f9),\n    data_processed/figure2i.npz with Figure3b,c,e,d_FigureS3.ipynb\n  criterion: >-\n    As in Figure3b,c,e,d_FigureS3.ipynb, the conventional attractor is the fixed-certainty filter\n    (noUncert_stats) at the kappa* that maximizes the prior-weighted average accuracy (objective()\n    with mean 0.5 and SD 1 over log rate, Methods, Performance measures, and Fig. 3B inset); the\n    Bayesian ring attractor is vonMises_q_stats. Reproduced when the Bayesian attractor's accuracy\n    is at least the conventional one's at every one of the 23 rates and strictly above it at every\n    rate from 0.1/s to 10/s. The paper's \"only once HD observations become highly unreliable\" is\n    checked as the difference being smallest at the lowest rates (0.01 and 0.03/s); reported, not\n    judged.\n- id: fig3c-update-weights\n  statement: >-\n    The weight given to a new HD observation by the Bayesian ring attractor depends on both the\n    observation's reliability and the current certainty and is close to that of the circular\n    Kalman filter, deviating only for very uninformative observations; a conventional attractor\n    weights observations by their reliability alone.\n  source: Fig. 3C legend; Results, Bayesian vs. Conventional Ring Attractors, paragraph 3; SI Appendix, Fig. S3 legend\n  quote: >-\n    The update weight of the Bayesian attractor is close to optimal, visually indistinguishable\n    from the circKF\n  data: elsewhere\n  where: >-\n    Zenodo doi:10.5281/zenodo.7615975 (BayesianRingAttractor v1.0, commit a9db6f9),\n    data_processed/figure2i.npz with Figure3b,c,e,d_FigureS3.ipynb\n  criterion: >-\n    In the notebook, Fig. 3C plots the weight w = atan(kappa_z dt / kappa_t) / (pi/2) as a map\n    and draws on it each model's mean certainty against information rate: circKF\n    (vonMises_stats[0,:,2]) and Bayesian attractor (vonMises_q_stats[0,:,2]), both as Fisher\n    information xi(kappa); the conventional attractor is a constant kappa*. Compute, at each of\n    the 23 rates, the weight for a 90 degree observation under the circKF's and under the\n    attractor's mean certainty. The paper gives no bound for \"close\"; readings: the absolute\n    weight difference is at most (a) 0.02 or (b) 0.05 at every rate of 1/s and above. Reproduced\n    when both readings hold and the largest difference falls at rates below 1/s (Fig. S3, \"only\n    deviates ... for very uninformative observations\"). The conventional attractor's weight\n    depending on reliability only follows from its constant kappa* and is not tested.\n- id: fig3d-best-network-slow-decay\n  statement: >-\n    Across ring attractors with different bump decay speeds and baseline amplitudes, the best\n    network has a slow decay (low beta) and performs about as well as the Bayesian ring attractor;\n    performance drops as decay speed increases, which a larger baseline amplitude partly offsets.\n  source: Results, Bayesian vs. Conventional Ring Attractors, paragraph 4; Fig. 3D\n  quote: >-\n    The network with the best performance overall had a slow bump decay speed (low β ), as expected\n    ( Fig. 3 D and E ). While it featured similar performance to the Bayesian ring attractor, it\n    had slightly different β and κ * parameters ... As the bump decay speed β increased further,\n    performance dropped.\n  data: elsewhere\n  where: >-\n    Zenodo doi:10.5281/zenodo.7615975 (BayesianRingAttractor v1.0, commit a9db6f9),\n    data_processed/figure3d.npz with Figure3b,c,e,d_FigureS3.ipynb\n  criterion: >-\n    figure3d.npz holds MSE_array, the prior-weighted average accuracy over the grid of kappa* (0.1\n    to 2.5) and beta (0.1 to 8), normalized by the particle filter reference as in the notebook.\n    The Bayesian ring attractor is kappa* = 1, beta = 1/(kappa_phi + kappa_v) = 0.5 (Methods). The\n    best network is the grid maximum. Reproduced when (1) the best beta is at most 1 (the scanned\n    values above 1 are 2, 4 and 8); (2) the best network differs from (1, 0.5) in kappa* or beta;\n    (3) the Bayesian attractor's normalized performance is within 10% of the best (the paper's\n    \"similar\", default tolerance); (4) for beta above the best, the maximum over kappa* falls as beta\n    rises; (5) for beta above the best, the kappa* that maximizes performance is at least the best\n    network's kappa*.\n- id: fig3f-noise-drop-below-70\n  statement: >-\n    In a network of 64 neurons with additive neural noise, inference accuracy drops below 70% of\n    its noise-free value once the noise is large enough.\n  source: Results, The Impact of Neural Noise on Inference Accuracy, paragraph 1; Fig. 3F\n  quote: >-\n    Indeed, simulating a network of 64 noisy neurons shows that, once the noise becomes\n    sufficiently large, inference accuracy drops to below 70% of its noise-free value\n  data: elsewhere\n  where: >-\n    Zenodo doi:10.5281/zenodo.7615975 (BayesianRingAttractor v1.0, commit a9db6f9),\n    data_processed/figure3f/sigma=*.npz with Figure3f_FigureS4.ipynb\n  expected:\n    quantity: relative performance without retuning at large noise\n    value: 70\n    unit: \"%\"\n  criterion: >-\n    The network without retuning keeps the kappa* and beta that are best at noise SD 0\n    (noretuning_MSE in the notebook). Normalization readings: (a) the notebook's, performance\n    divided by the particle filter reference; (b) the legend's, performance divided by the same\n    network's performance at noise SD 0. Range readings: (i) noise SD up to 10, the plotted range;\n    (ii) up to 20, the largest simulated. Reproduced when the relative performance without\n    retuning is below 70% at the largest noise SD under every combination.\n- id: fig3f-retuning-reduces-drop\n  statement: >-\n    Retuning the bump decay speed and baseline amplitude for each noise level reduces the drop in\n    inference accuracy by about 35% compared with the network tuned for noise-free performance,\n    and raises the signal-to-noise ratio.\n  source: Results, The Impact of Neural Noise on Inference Accuracy, paragraph 3; Fig. 3F; SI Appendix, Fig. S4\n  quote: >-\n    Indeed, doing so reduced the drop in inference accuracy by about 35% when compared to the\n    network tuned to optimize noise-free performance ( Fig. 3 D and F ) and also boosted the\n    network’s signal-to-noise ratio\n  data: elsewhere\n  where: >-\n    Zenodo doi:10.5281/zenodo.7615975 (BayesianRingAttractor v1.0, commit a9db6f9),\n    data_processed/figure3f/sigma=*.npz with Figure3f_FigureS4.ipynb\n  depends_on:\n  - fig3f-noise-drop-below-70\n  expected:\n    quantity: reduction of the accuracy drop by retuning\n    value: 35\n    tolerance: 3.5\n    unit: \"%\"\n  criterion: >-\n    From the notebook, retuned performance is the grid maximum at each noise SD (max_MSE), and\n    the untuned one the noise-free optimum's value (noretuning_MSE); signal-to-noise as the\n    notebook computes it (mean kappa over the weighted average, divided by sigma / sqrt(N/2),\n    Methods). The drop is 100% minus relative performance, and the reduction is 1 minus the\n    retuned drop over the untuned drop. The paper does not say at which noise level the 35% is\n    taken; readings: (a) noise SD 10, the largest plotted; (b) noise SD 20, the largest\n    simulated; (c) the mean of the reduction over noise SD 1 to 10. Each under the two\n    normalizations of fig3f-noise-drop-below-70. Reproduced when the reduction is within 31.5 to\n    38.5% under every reading and the retuned signal-to-noise ratio is at least the untuned one at\n    every noise SD above 0. Fig. S4's statement that larger noise needs larger kappa* and beta is\n    reported from the same grid, not judged.\n- id: noise-effects-on-mu-and-kappa\n  statement: >-\n    Neural noise makes the bump position diffuse without bias and makes the bump amplitude drift\n    upward and diffuse, which leads to overconfidence; for additive noise, a four-fold larger\n    network halves the noise's effective SD.\n  source: Results, The Impact of Neural Noise on Inference Accuracy, paragraphs 2 and 3; SI Appendix, section 5\n  quote: >-\n    First, it causes an unbiased random diffusion of μ t and, thus, an increasingly imprecise\n    memory of the HD estimate. Second, it causes a positive drift and random diffusion of κ t\n  data: elsewhere\n  where: >-\n    Zenodo doi:10.5281/zenodo.7615975 (BayesianRingAttractor v1.0, commit a9db6f9),\n    circularFiltering.py RNN_filter_Run\n  criterion: >-\n    The result is a derivation (SI Appendix, section 5); the Methods give the diffusion SD of\n    kappa under additive noise as sqrt(sigma_nn^2 / N) per unit time. Test it with the code's\n    RNN_filter_Run at the Bayesian ring attractor's parameters (kappa* = 1, beta = 0.5, tau = 1),\n    with no HD input (I_ext = 0) and no angular velocity input (dy = 0), noise SD 1 and 2, N = 64\n    and 256, dt = 0.01, from a bump of amplitude 1, over 2,000 runs of T = 5. Reproduced when (1)\n    the mean change of position is within 2 standard errors of 0 and its variance grows with time;\n    (2) the mean amplitude at the end exceeds that of the noise-free run; (3) the SD of the\n    one-step amplitude increments at N = 256 is half that at N = 64, within 10%. The run length,\n    number of runs and starting amplitude are not given by the paper; they are standard choices\n    that set only the precision.\n- id: fig4b-connectome-motifs\n  statement: >-\n    The connectivity among EPG, Delta7 and PEN1 neurons in the hemibrain connectome resembles the\n    connectivity of a network that implements the approximate circular Kalman filter, with shifted\n    PEN1 to EPG projections and broad EPG to Delta7 to EPG inhibition.\n  source: Fig. 4 B and C legends; SI Appendix, section 4A\n  quote: >-\n    The connectivity profile of a recurrent neural network (RNN) ( Fig. 2 D – F ) that implements\n    an approximate circKF is strikingly similar to the connectivity of neurons in the Drosophila HD\n    system.\n  data: elsewhere\n  where: >-\n    neuPrint hemibrain:v1.2.1 (Scheffer et al. 2020, eLife 9, e57443), synapse counts between EPG,\n    Delta7 and PEN1 neurons\n  criterion: >-\n    Fig. 4B legend: connections from hemibrain:v1.2.1, total synapse count per cell pair as the\n    connection strength, neurons sorted by spatial position as a proxy for preferred HD, Delta7 to\n    Delta7 omitted. The code does not hold this analysis. Sorting is open; readings: (a) by the\n    protocerebral bridge glomerulus in the neuron's name (L9 to R9), (b) by the ellipsoid body or\n    gall position in the name. Reproduced when, under both, (1) PEN1 to EPG connections are offset\n    from the EPG to PEN1 connections, in opposite directions for left and right PEN1 neurons; (2)\n    each Delta7 neuron receives EPG input from, and sends output to, EPG neurons at more than half\n    of the sorted positions (broad inhibition, Fig. 4E).\n- id: fig4gh-drosophila-network-matches\n  statement: >-\n    A Drosophila-like multipopulation network, constrained by the connectome, tracks HD with an\n    accuracy indistinguishable from the idealized Bayesian ring attractor across observation\n    reliabilities.\n  source: Results, Tuning a Biological Ring Attractor, paragraph 3; Fig. 4 G and H\n  quote: >-\n    We found that this network achieves a HD encoding accuracy which is indistinguishable from that\n    of our idealized Bayesian ring attractor network ( Fig. 4 G and H ).\n  data: elsewhere\n  where: >-\n    Zenodo doi:10.5281/zenodo.7615975 (BayesianRingAttractor v1.0, commit a9db6f9),\n    data_processed/figure4g.npz with Figure4g,h.ipynb and network_filter.py\n  criterion: >-\n    From figure4g.npz as Figure4g,h.ipynb reads it, compare the Drosophila-like network (CX_stats)\n    with the Bayesian ring attractor (vonMises_q_stats) at every information rate stored.\n    Readings for \"indistinguishable\": the absolute accuracy difference is at most (a) 0.01 or (b)\n    0.02 at every rate. Reproduced when both hold. The mean certainties (Fig. 4H) are reported,\n    not judged.\n- id: figs2-performance-independent-of-n\n  statement: >-\n    The Bayesian ring attractor's inference accuracy depends little on its number of neurons.\n  source: SI Appendix, Fig. S2 legend; Results, Neural Network Implementation, paragraph 6\n  quote: >-\n    Network inference performance is mostly independent of the number of neurons N in the Bayesian\n    ring attractor network.\n  data: elsewhere\n  where: >-\n    Zenodo doi:10.5281/zenodo.7615975 (BayesianRingAttractor v1.0, commit a9db6f9),\n    data_processed/figureS2.npz and vonMises_q_stats.npz with FigureS2.ipynb\n  criterion: >-\n    figureS2.npz holds accuracy per information rate for N = 3, 4, 8, 16, 32, 64 and 128 (the\n    notebook's N_array), and vonMises_q_stats.npz the quadratic circKF reference. \"Mostly\" is not\n    quantified; readings: for (a) N of 8 and more, (b) N of 16 and more, the accuracy is within\n    0.02 of the reference at every rate. Reproduced when both hold. The values for N = 3 and 4 are\n    reported.\n- id: prediction-bump-amplitude-cue-reliability\n  statement: >-\n    The paper predicts that the bump amplitude in the HD system is higher in the presence of\n    reliable external HD cues, such as salient visual landmarks. The paper does not test this.\n  source: Discussion, paragraph 7\n  quote: >-\n    Second, we predict that bump amplitude in the HD system should vary dynamically, with higher\n    amplitudes in the presence of reliable external HD cues, such as salient visual landmarks.\n  data: dataset\n  criterion: >-\n    The paper gives the measure and nothing else. Bump amplitude is the length of the population\n    vector of the activity's first Fourier component, ordered by preferred HD (Eq. 3; Methods,\n    Simulation parameters, decoder A = (cos phi, sin phi)), in the EPG population that holds the\n    HD bump (SI Appendix, section 4A). The paper does not say how cue reliability is set in an\n    experiment, which activity signal (raw fluorescence or dF/F) feeds the decoder, the time\n    windows, the unit of comparison or a test. Comparison as the paper's text allows: bump\n    amplitude while the fly sees the more reliable cue against the less reliable cue, as the\n    dataset labels them. Readings for the test: (a) per fly, mean amplitude higher with the more\n    reliable cue in more than half of the flies; (b) a one-sided paired Wilcoxon signed-rank test\n    over flies, p below 0.05. Activity signal readings: (i) dF/F, (ii) raw fluorescence minus\n    baseline. Reproduced when every combination finds higher amplitude with the more reliable cue;\n    blocked as methods_underspecified when they differ. The second half of the prediction (a high\n    bump amplitude makes the bump position less sensitive to new cues) has no measure in the paper\n    and is not tested.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/000289/10.1073-pnas.2210622120.yaml paper/10.1073-pnas.2210622120.txt; grep -n "—\|rather" claims/000289/10.1073-pnas.2210622120.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000289/10.1073-pnas.2210622120.yaml",
 "old_string": "  expected:\n    quantity: relative performance without retuning at large noise\n    value: 70\n    unit: \"%\"\n  criterion: >-\n    The network without retuning",
 "new_string": "  criterion: >-\n    The paper states a bound, so no tolerance applies. The network without retuning"
}
```

```
The file claims/000289/10.1073-pnas.2210622120.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/000289/10.1073-pnas.2210622120.yaml paper/10.1073-pnas.2210622120.txt; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/000289/10.1073-pnas.2210622120.yaml` with 13 claims, but this paper reports no experiments, so the dataset can bear on only one of them, and that one is a prediction the paper never tests. The quote checker passes with 0 problems.

**Text read.** I read the version of record from Europe PMC (PMC9992764): main text, Methods and figure legends, plus the SI Appendix PDF (sections 1 to 6, Figs. S1 to S5). Nothing the claims needed was missing from the text. The preprint v1 is also in `paper/`, but I did not use it.

**Code read.** The paper's code is on Zenodo (10.5281/zenodo.7615975, BayesianRingAttractor v1.0, commit a9db6f9). It holds the filters, the network simulations, one notebook per figure, and the processed simulation outputs the figures are drawn from. It holds no imaging analysis and no connectome query.

**Paper and dataset don't match.** The paper is a theory paper: a circular Kalman filter and a Bayesian ring attractor, tested only in simulation and against the hemibrain connectome. It reports no imaging, behaviour or stimulus data. The dataset's description says it holds the data of a different paper, "Uncertainty and learning in a biological ring attractor" (Basnak et al., in preparation). It links bioRxiv v4 of this paper, but v4's abstract matches the published version and also has no experiments. So this paper cannot be reproduced on this dataset.

**Claims.**
- 13 claims, all with quotes. None has statistics, because the paper reports no tests.
- 1 claim has an `expected` value: retuning reduces the noise-induced accuracy drop by 35% (± 3.5).
- All 13 have criteria.
- 11 are simulation results and 1 is the connectome result (hemibrain v1.2.1 via neuPrint). These 12 are marked as using data held elsewhere. The simulation claims are judged on the paper's own processed outputs, and a rerun of its scripts is shown as a variant.
- 1 claim uses the dataset: the Discussion's prediction that bump amplitude is higher when external cues are reliable.

**Details the paper leaves open, and the readings named:**
- **"Same", "close", "indistinguishable", "mostly"** (Figs. 2I, 3C, 4G and S2): absolute accuracy or weight differences within 0.01 or 0.02 (0.02 or 0.05 for the update weights).
- **Which reliabilities count as "reliable"** (Fig. 2I): information rate of at least 1/s, or at least 3/s.
- **"Similar" and "accurately tracks"** (Fig. 2H): the network's distance from the filter is smaller than the filter's own error, and the correlation between amplitude and the filter's certainty is at least 0.9. These are run at the code's cue strength (15) and at the Methods' 10/s.
- **Fig. 3F normalization:** the code divides by the particle-filter reference, while the legend says the noise-free network; both are run.
- **Noise range for "below 70%":** noise SD up to 10 (plotted) or up to 20 (simulated).
- **Noise level for the 35%:** noise SD 10, noise SD 20, or the mean over 1 to 10.
- **Neuron sorting in Fig. 4B:** by protocerebral bridge glomerulus, or by ellipsoid body or gall position.
- **The prediction claim:** the paper fixes only the measure (the population-vector amplitude of the EPG bump). Open are how reliability is set in an experiment, the activity signal (ΔF/F or raw fluorescence minus baseline) and the test (majority of flies, or a one-sided Wilcoxon test across flies). Its second half, that high amplitude makes the bump less sensitive to new cues, has no measure in the paper and is not tested.

**Where the code and the paper differ:**
- The code runs 10,000 trajectories per setting where the Methods say 5,000.
- The Fig. 4G script uses a time step of 0.001 where the Methods say 0.01 for all simulations.
- Fig. 2H uses an information rate of 15 where the Methods say 10/s.
- The curve labelled "Bayesian ring attractor" in Figs. 2I, 3B, 3C and 4G is the filter's quadratic approximation, not a finite network simulation.
- The scan scripts pass the keyword `kappa_y` to functions that take `kappa_v`, so a rerun needs that renamed.

**Missing from the paper:** any experimental method or data for the prediction claim, which is the only point of contact with this dataset.

## End of run

38 turns, 5 minutes, result: success.
