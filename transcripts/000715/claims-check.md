# 000715 · claims-check · run 39897041168

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls claims/000715/ paper/; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 96,220p docs/protocol.md; cat claims/000715/*.yaml; python tools/claims_check.py claims/000715/10.1016-j.cell.2020.12.012.yaml paper/10.1016-j.cell.2020.12.012.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 120,200p docs/protocol.md; python tools/claims_check.py claims/000715/10.1016-j.cell.2020.12.012.yaml paper/10.1016-j.cell.2020.12.012.txt | tail -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/000715/10.1016-j.cell.2020.12.012.yaml"
}
```

```
1	# Claims for Yemini, Lin, Nejatbakhsh et al. (2021), "NeuroPAL: A Multicolor Atlas for Whole-Brain
2	# Neuronal Identification in C. elegans", Cell 184, 272-288, on dandiset 000715.
3	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23, protocol
4	# pilot-10 as stated in docs/protocol.md.
5	#
6	# Text read: the accepted author manuscript in PubMed Central (PMC10494711, NIHMS1925874), as served
7	# by ncbi_pmc, with its Results, Discussion, STAR Methods, figure legends (Figures 1 to 7, S1 to S3),
8	# and two supplements extracted from their PDFs: Methods S1 (semi-automated neuronal identification,
9	# with the atlas, detection and cross-validated accuracy results) and Methods S2 (optimal coloring).
10	# The version of record was not read. Tables S1 to S6 (spreadsheets), Videos S1 to S4 and the legend
11	# of Figure S4 are not in the text read. No claim below needs a number that only those tables hold,
12	# except that the per-neuron atlas values (Table S3), receptor expression (Table S4), mutant scores
13	# and p-values (Table S5) and whole-brain statistics (Table S6) could not be read.
14	#
15	# Code read. github.com/amin-nejat/CELL_ID at commit d9f5df9 (2020-10-28, the last commit before
16	# publication; HEAD 759898d of 2021-11-14 was also looked at). It holds the NeuroPAL ID GUI: neuron
17	# detection (+Methods/AutoDetect.m, +Methods/Preprocess.m), identification against a pretrained atlas
18	# (+Methods/AutoId.m) and atlas files (Data/Models/atlas*.mat). It does not hold the script that
19	# trains the atlas from annotated worms (Methods S1 Algorithm 4) nor the cross-validation behind
20	# Figure 7B-C; the training set of its shipped atlas is not stated, so that atlas is not used here.
[... 650 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -l paper/*.txt; grep -n -i "variability\|OLLR\|86%\|94%\|eight manual\|50% for the head\|3.5%\|1.7%\|K = 191\|calibrat\|leave-one-out\|footnote\|uncertain" paper/10.1016-j.cell.2020.12.012.txt | head -80
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker reports no problems (32 claims, 32 quotes, 7 statistical values). Now checking the claims against the paper's passages.

**Agent calls Bash**

```bash
cd  f=paper/10.1016-j.cell.2020.12.012.txt; for p in "different positional variability" "OLLR exhibits" "Accuracy was 86%" "eight manual annotations" "restricted the model" "accuracy of 80% in head" "good agreement" "violation of 3.5%" "1.7% when using"; do echo "=== $p"; grep -o ".\{700\}$p.\{900\}" $f | head -2; done
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=paper/10.1016-j.cell.2020.12.012.txt; grep -n "accuracy of 80% in head\|good agreement\|violation of 3.5%\|Figure 6.9\|Figure 6.4\|Figure 6.8\|Figure 6.5\|Figure 6.3\|leave" $f | cut -c1-200
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cell.2020.12.012.txt",
 "offset": 780,
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "=== page\|Methods S1\|Methods S2" paper/10.1016-j.cell.2020.12.012.txt | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  awk '{print NR": "length($0)": "substr($0,1,100)}' paper/10.1016-j.cell.2020.12.012.txt | awk -F': ' '$2>2000 || /=== page|^[0-9]+: [0-9]+: [0-9](\.[0-9])? *$/' | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=paper/10.1016-j.cell.2020.12.012.txt; sed -n 113,420p $f | grep -v "^.\{0,4\}$" | head -250
```

Result: not kept, because it reads the paper's text.

**Agent**

Checker passes. Now reading Methods S2 and the paper's statistics sections to check the remaining criteria.

**Agent calls Bash**

```bash
cd  f=paper/10.1016-j.cell.2020.12.012.txt; sed -n 1480,3111p $f | grep -n -i "margin\|95%\|adjacen\|neighbor\|violation\|1/3\|10,000\|7,500\|7500\|sparsity\|atlas" | cut -c1-300 | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=paper/10.1016-j.cell.2020.12.012.txt; sed -n 1740,1775p $f; sed -n 2185,2195p $f; sed -n 2410,2440p $f;  sed -n 2690,2700p $f
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=paper/10.1016-j.cell.2020.12.012.txt; sed -n 2215,2250p $f; grep -o "Figure 7\. .\{2500\}" $f | head -1; grep -o ".\{300\}optimal-coloring algorithm\b.\{1500\}" $f | sed -n 1,3p | cut -c1-1800
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=paper/10.1016-j.cell.2020.12.012.txt; grep -o "QUANTIFICATION AND STATISTICAL.\{4000\}" $f | head -1; echo; grep -o ".\{200\}Bonferroni.\{600\}" $f | head -3; echo; grep -o "Figure 5\. .\{2500\}" $f|head -1
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "p_relation" -r tools/ docs/ | head; f=paper/10.1016-j.cell.2020.12.012.txt; grep -o "Significant responses (p or q ≤.\{1500\}" $f|head -1
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "relation\|<=\|≤" tools/claims_check.py tools/*.py | head -20; ls tools; grep -rn "p_relation" claims/ | awk -F'p_relation: ' '{print $2}' | sort | uniq -c
```

```
tools/build_site.py:138:    return VERIFICATION_TIER.get(latest["kind"], "runs") if claims <= agreed else "runs"
tools/build_site.py:284:                             if r["id"].startswith("entry:") and r["relation"] == "derived_from"],
tools/build_site.py:342:    words = ("firing rate tuning population response selectivity latency decoding accuracy correlation "
tools/build_site.py:662:        parts.append(f'p {s.get("p_relation", "=")} {p_text(s["p"])}')
tools/build_site.py:1160:  var nums=[1,pages,state.page-1,state.page,state.page+1].filter(function(p,i,a){return p>=1&&p<=pages&&a.indexOf(p)===i;})
tools/build_targets.py:94:            "relation": (r.get("relation") or "").removeprefix("dcite:") or None,
tools/build_targets.py:110:    return found + [{"doi": p["doi"].lower(), "title": p.get("title"), "relation": "IsDescribedBy",
tools/entry.py:373:    papers = {r["id"] for r in entry.get("related", []) if r["relation"] == "reproduces"}
tools/progress.py:25:    return line if len(line) <= WIDTH else line[:WIDTH - 1] + "…"
__pycache__
agent_run.py
archive_transcripts.sh
build_site.py
build_targets.py
claims_check.py
conversion_issue.py
datasets.py
entry.py
flagged.py
get_papers.sh
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "relation\|statistics" tools/claims_check.py | head; grep -rn "schema" tools/claims_check.py | head -5; ls docs
```

```
92:        for s in c.get("statistics", []):
5:Validates the file against schemas/claims.schema.json, checks every quote word for word
25:from entry import _plain, schema  # noqa: E402
82:    for err in schema("claims").iter_errors(_plain(doc)):
agents
archives.md
conversion-tracker.md
design.md
encore.md
fixing-conversions.md
pilot-notes
pilot-notes.md
pipeline.md
protocol.md
queue.md
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));
import re;t=json.dumps(s);i=t.find('p_relation');print(t[i-100:i+300])"
```

```
"The reported p-value as printed, or its bound when the paper gives one ('p < 0.05' is p 0.05 with p_relation '<'). A paper that prints 'P = 0' (below the precision it reports) is recorded as 0.", "type": "number", "minimum": 0, "maximum": 1}, "p_relation": {"description": "How p was reported: exactly (the default) or as a bound.", "enum": ["=", "<", ">"]}, "corrected": {"description": "The corre
```

**Agent calls Bash**

```bash
cd  f=paper/10.1016-j.cell.2020.12.012.txt; for p in "expressed in 97% of all" "every postsynaptic partner of every" "31% of GABA" "brightest integrant" "variable brightness" "41 different" "robust cyclical" "low Pearson correlation" "NaCl evoked stereotyped" "odors also evoked"; do echo "=== $p"; grep -o ".\{300\}$p.\{1100\}" $f | head -1; done
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=paper/10.1016-j.cell.2020.12.012.txt; grep -o "(B) The GABA.\{2200\}" $f | head -1; echo; grep -o ".\{300\}75%.\{300\}" $f | head -3; echo; grep -o ".\{100\}(H).\{700\}" $f | grep -i avf | head -2
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=paper/10.1016-j.cell.2020.12.012.txt; grep -o "Figure 4\. Metabotropic.\{3000\}" $f | head -1
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=paper/10.1016-j.cell.2020.12.012.txt; grep -o "Variability in Neuronal Cell Body Positions The C. elegans.\{1500\}" $f; echo; grep -o "Figure 2\. .\{900\}" $f | head -1; echo; grep -o "Whole-Brain Activity Imaging of Gustatory.\{1800\}" $f | sed -n 2p
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && timeout 60 git clone -q https://github.com/amin-nejat/CELL_ID.git 2>&1 | tail -2; cd CELL_ID 2>/dev/null && git checkout -q d9f5df9 && git log -1 --format='%h %ci' && grep -n "iter_sinkhorn\|1e5\|0.25\|major_axis_align\|function" +Methods/AutoId.m | head -40
```

```
d9f5df9 2020-10-28 16:37:25 -0400
11:        iter_sinkhorn       = 500;
15:        max_log_likelihood  = 1e5;
23:        theta = 0: 0.25: 2*pi
38:        function obj = instance()
48:        function [atlas, version] = getAtlas()
58:        function BatchId(file, bodypart)
81:        function rotmat = rotmat(theta)
86:        function pos = major_axis_align(pos,sign)
92:        function D = pdist2_maha(X,Y,Sigma)
104:        function vec_x = vec(x)
111:        function beta = MCR_solver(Y,X,sigma,lambda)
139:        function [S,R,T]=scaled_rotation(X,Y)
173:        function P = sinkhorn_logspace(logP,niter)
199:        function P = sinkhorn_logspace_extended(logP,niter, p, n1)
215:        function [P,varargout] = update_permutation(colors, positions, model, known)
256:        function [col,pos,cost] = local_alignment(col,pos,model,theta,sgn,annotated)
267:            pos = AutoId.major_axis_align(POS,sgn);
280:            pos = AutoId.major_axis_align(pos,1);
298:                beta_col = AutoId.MCR_solver(model.mu(:,4:end), P'*[col ones(size(col,1),1)], sigma_weighted(4:end,4:end,:),1e5);
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/CELL_ID; sed -n 327,362p +Methods/AutoId.m; sed -n 513,540p +Methods/AutoId.m; sed -n 608,640p +Methods/AutoId.m
```

```
function add_to_image(obj, im)
            % add_to_image  function simply updates some properties of the image
            % structure that depend on auto_id
            
            neuron_names = obj.atlas.(lower(im.bodypart)).N;
            % convert assignment (probabilistic/deterministic) to neuron
            % names
            ids = repmat({'Artifact'}, size(obj.assignments,1),1);
            ids_prob = repmat({'Artifact'}, size(obj.assignments,1),obj.ncandidates);

            [rows, cols] = find(obj.assignments);
            ids(rows) = neuron_names(cols);

            for i=1:size(obj.assignment_prob_ranks,1)
                for j=1:obj.ncandidates
                    if(obj.assignment_prob_ranks(i,j)>0)
                        ids_prob{i,j} = neuron_names{obj.assignment_prob_ranks(i,j)};
                    end
                end
            end
[... 78 more lines not kept]
```

**Agent**

Code details I spot-checked in CELL_ID at d9f5df9 match the file (500 Sinkhorn iterations, theta step 0.25, ridge 1e5, ranking by top probability, positions in µm). Now making the edits.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000715/10.1016-j.cell.2020.12.012.yaml",
 "old_string": "    the fraction of worms in which it is correct (accuracy), with left/right midline pairs scored\n    by class as in the Figure 6.8 footnote. The paper gives no measure of agreement. Read as (a)\n    a positive Spearman correlation between per-neuron confidence and accuracy with p < 0.05 and\n    (b) a mean absolute difference between confidence and accuracy under 10 percentage points\n    (the default tolerance of the protocol). Reproduced when both hold in head and tail; the\n    reliability plot is shown.",
 "new_string": "    the fraction of worms in which it is correct (accuracy), with left/right midline pairs scored\n    by class as in footnote 1 of Methods S1 section 6.4. The paper gives no measure of agreement\n    and no threshold; \"largely in good agreement\" is open. Two readings, each run, (a) a positive\n    Spearman correlation between per-neuron confidence and accuracy with p < 0.05 and (b) a mean\n    absolute difference between confidence and accuracy under 10 percentage points (a standard\n    choice, not from the paper). Reproduced in head and tail when both readings agree that it\n    holds; when they disagree the claim is blocked as methods_underspecified. The reliability\n    plot is shown."
}
```

```
The file claims/000715/10.1016-j.cell.2020.12.012.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000715/10.1016-j.cell.2020.12.012.yaml",
 "old_string": "    Whether head and tail are pooled or the figure is per body part is not said; pooled, head and\n    tail are all reported, and the number is matched under any of them. The outside inputs are the",
 "new_string": "    Whether the 3.5% pools head and tail is not said for NeuroPAL itself; the solver runs of\n    Methods S2 section 4.2 use the 235 head and tail neurons together, and Methods S2 Figure 1A\n    shows head and tail with one value, so pooled is the main reading; head and tail apart are\n    reported as variants, and the number is matched under any of them. The outside inputs are the"
}
```

```
The file claims/000715/10.1016-j.cell.2020.12.012.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000715/10.1016-j.cell.2020.12.012.yaml",
 "old_string": "  statistics:\n  - test: two-tailed paired t test, stimulus against the preceding equal period, FDR q-values\n      (Storey 2002)\n    p: 0.05\n    p_relation: \"<\"\n    corrected: FDR\n    n: up to 42 left/right neuron pairs or 21 single neurons, from 21 heads\n  data: elsewhere\n  where: Zenodo doi:10.5281/zenodo.3906530\n  criterion: Not tested on the dandiset.",
 "new_string": "  data: elsewhere\n  where: Zenodo doi:10.5281/zenodo.3906530\n  criterion: Not tested on the dandiset. Responding neurons are those significant (q of at most\n    0.05) by a two-tailed paired t test of the stimulus period against the equal period before it,\n    FDR q-values (Storey 2002), with up to 42 left/right neuron pairs or 21 single neurons from 21\n    heads (STAR Methods, Analysis of brainwide imaging data)."
}
```

```
The file claims/000715/10.1016-j.cell.2020.12.012.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000715/10.1016-j.cell.2020.12.012.yaml",
 "old_string": "  statistics:\n  - about: post-stimulus responses\n    test: one-tailed paired t test, post-stimulus mean against stimulus mean, FDR corrected\n    p: 0.05\n    p_relation: \"<\"\n    corrected: FDR\n    n: 21 tails\n  data: elsewhere\n  where: Zenodo doi:10.5281/zenodo.3906530\n  criterion: Not tested on the dandiset.",
 "new_string": "  data: elsewhere\n  where: Zenodo doi:10.5281/zenodo.3906530\n  criterion: Not tested on the dandiset. Post-stimulus responses are those whose stimulus mean\n    exceeds the pre-stimulus mean and whose post-stimulus mean exceeds the stimulus mean by a\n    one-tailed paired t test, FDR corrected at q of at most 0.05, over 21 tails (STAR Methods,\n    Analysis of brainwide imaging data)."
}
```

```
The file claims/000715/10.1016-j.cell.2020.12.012.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000715/10.1016-j.cell.2020.12.012.yaml",
 "old_string": "    legend). The sparsity giving 3 reporters is not stated;",
 "new_string": "    legend), both with 3 colors at 3 intensities (Figure 7 legend; Methods S2 Figure 1 panel\n    labels, Colors=3 Intensities=3 Reporters=39 and Reporters=3). The sparsity giving 3 reporters\n    is not stated;"
}
```

```
The file claims/000715/10.1016-j.cell.2020.12.012.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  grep -l "^checks:" claims/*/*.yaml | head -1 | xargs sed -n '/^checks:/,$p' | head -20
```

```
checks:
- date: 2026-10-20
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - behavior-touches. The criterion stated that the touch and trial counts come from the 111 cortical cells and from principal-whisker touches; the paper says neither. Named both as open, with readings for the recordings and for the whiskers counted.
  - vpm-whisking. Added that the 13.5 spikes/s "after onset of whisker movement" is read as the whisking-epoch rate of Fig. 5d, since the paper defines no spike window after whisking onset.
  - exc-vm-touch-whisking. The criterion gave the Supplementary Fig. 4 windows as the measure of the 1.2 mV whisking change; the paper does not say how it is measured. Named it open, with readings (a) those windows and (b) whisking-epoch minus nonwhisking mean Vm.
  - ion-cut-exc-whisking. Uses both readings of the whisking change, as exc-vm-touch-whisking now does.
  - exc-inhibition-timing. Removed the requirement that the delay be positive in most neurons, which the paper does not state (its Discussion gives a range of -0.8 to 1.6 ms); the range is now reported against that.
  - exc-thalamus-photoinhibition. Removed latency reading (b), a 3 s.d. threshold on Vm that appears nowhere in the paper. The Methods' touch-latency rule is applied to laser onset, and the criterion says this is an assumption.
  - pv-enphr-suppression. Same change for its latencies; the Methods' dPSTH/dt rule is applied to the laser-onset PSTH, as an assumption.
  - ion-cut-exc-no-touch. The post-touch Vm (Vm at the peak of the average PSP) is undefined without a PSP and biased upward on a flat average. The test now uses the paper's touch epoch (4 to 50 ms) against the 0 to 5 ms pre-touch mean, with the peak-based amplitude as a variant.
  - fs-suppress-movement-spiking. The paper does not name the groups of its Kruskal-Wallis test; the criterion now says the test is reported and does not enter the outcome.
  - auc-weak-strong. The criterion compared groups on the Fig. 
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat >> claims/000715/10.1016-j.cell.2020.12.012.yaml <<'EOF'
checks:
- date: 2026-10-23
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - ms1-calibration. The 10 percentage point bound was justified as the protocol's default tolerance, which is 10% of a reported value, not 10 points; it is now named as a standard choice not from the paper. The criterion required both readings to hold; it now follows the protocol rule for readings (agreement decides, disagreement blocks as methods_underspecified). The class-level scoring is cited to footnote 1 of Methods S1 section 6.4, where the footnote sits, not to the Figure 6.8 legend.
  - ms2-neuropal-color-violations. The criterion said pooling of head and tail is not stated; Methods S2 section 4.2 runs the solver on the 235 head and tail neurons together and Methods S2 Figure 1A shows one value for head and tail, so pooled is now the main reading and head and tail apart are variants.
  - fig7de-optimal-coloring-violations. Added the source for 3 colors at 3 intensities in both solutions (Figure 7 legend, Methods S2 Figure 1 panel labels).
  - fig6ef-nacl-novel-interneurons. Removed the statistics entry; the paired t test at q of at most 0.05 selects which neurons count as responding, a threshold used to count units, not a result. The test is kept in the criterion.
  - tables6-tail-pvq-and-post-stimulus. Removed the statistics entry for the same reason (the post-stimulus test identifies responding neurons); kept in the criterion.
  - Open. Every remaining statistics entry (fig5ab-pag3-fate-changes, fig5efg-eor1-rme, fig6d-ase-nacl-asymmetry) records the paper's significance standard, p or q of at most 0.05, as p 0.05 with "<" since the schema has no "<=" relation; the actual p-values are in Tables S5 and S6, not in the text read.
  - Open. fig2cd-variability-differs has no test or threshold in the paper; the factor of two taken from the OLLR and OLLL example in the Figure 2C legend is a reading of "different positional variability", and is easily met.
  - Open. ms1-calibration and ms1-uncertain-first-faster judge qualitative statements ("largely in good agreement", "much faster") for which the paper gives no measure; their readings are named in the criteria but are not the paper's.
  - Checked against the code. CELL_ID at d9f5df9 holds the details cited from it (iter_sinkhorn 500, theta from 0 to 2 pi in steps of 0.25, ridge 1e5 in MCR_solver, ranking by top probability in add_to_image, positions scaled to um).
EOF
python tools/claims_check.py claims/000715/10.1016-j.cell.2020.12.012.yaml paper/10.1016-j.cell.2020.12.012.txt | tail -3; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

I checked the claims file against the paper and made five corrections. It is ready for an attempt. Nothing was committed or pushed.

**Checker result (after my edits):** `claims/000715/10.1016-j.cell.2020.12.012.yaml: 32 claims, 32 quotes, 5 statistical values, 0 problems`. Before the edits it was the same except for 7 statistical values.

**Changes, by claim**
- **ms1-calibration:** The 10-percentage-point bound had been justified as "the protocol's default tolerance". The protocol's default is 10% of a reported value, not 10 points, so it is now named as a standard choice that does not come from the paper. The criterion had required both readings to hold; it now follows the protocol's rule: if the two readings agree, that decides the claim, and if they disagree it is blocked as methods_underspecified. The class-level scoring of left/right pairs is now cited to footnote 1 of Methods S1 section 6.4, where the footnote actually sits, not to the Figure 6.8 legend.
- **ms2-neuropal-color-violations:** The file said the paper does not state whether head and tail are pooled. Methods S2 section 4.2 runs the solver on the 235 head and tail neurons together, and Methods S2 Figure 1A gives a single value for both. Pooled is now the main reading, with head and tail apart as variants.
- **fig7de-optimal-coloring-violations:** Added the source for "3 colors at 3 intensities" in both solutions (the Figure 7 legend and the Methods S2 Figure 1 panel labels).
- **fig6ef-nacl-novel-interneurons** and **tables6-tail-pvq-and-post-stimulus:** I removed the statistics entries. In both, the q ≤ 0.05 test decides which neurons count as responding, so it is a threshold for counting units, not a result. The test is now described in each criterion.

All other quotes, statements, sources, expected values and tolerances match the paper. Every main finding has a claim, and all claims come from this paper.

**Still open**
- The three remaining statistics entries (fig5ab, fig5efg, fig6d-ase) record the paper's significance standard, "p or q ≤ 0.05". They are written as `p 0.05` with `"<"` because the schema has no "≤" option. The actual p-values are in Tables S5 and S6, which are not in the text read.
- **fig2cd-variability-differs:** The paper gives no test. The pass rule, a factor of two between the most and least variable neuron, comes from the OLLR/OLLL example in the Figure 2C legend. It is a reading of the paper, and it will be passed easily.
- **ms1-calibration** and **ms1-uncertain-first-faster:** The paper says "largely in good agreement" and "much faster" without giving any measure. The readings used to judge them are named in the criteria, but they are not the paper's own.

All of this is recorded in a `checks` entry at the end of the file, with `ready: true`.

## End of run

33 turns, 4 minutes, result: success.
