# sabatini-2024 · claims · run 44717511868

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls paper/ claims/; cat claims/fouke-2025.yaml
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

**Agent calls Bash**

```bash
cat claims/fouke-2025.yaml | head -200; wc -l claims/fouke-2025.yaml paper/*.txt; head -30 paper/*.txt; cat papers/datasets/sabatini-2024.yaml 2>/dev/null
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/fouke-2025.yaml",
 "limit": 160,
 "offset": 26
}
```

```
26	schema_version: 2
27	dataset:
28	  archive: dandi
29	  id: "001453"
30	paper: doi:10.1016/j.cub.2025.04.027
31	claims:
32	- id: stimulus-code-link
33	  kind: link
34	  statement: The dandiset's stimulus codes can be linked to the stimuli the paper names, using
35	    the paper's analysis code and the protocol file of its stimulus software, and the values
36	    computed through that link agree with those the paper's code printed.
37	  source: Data and Code Availability; the paper's Fig1-S1.ipynb at GitLab commit 33a5c29
38	  data: with_labels
39	  criterion: Records are matched by the integer stimulus code. The link holds (reproduced) when
40	    every code the analysis uses (0 to 7, 9, 10, 11, 13 and 20) occurs in the dandiset, and the
41	    species' median speeds for the nine whole-field stimuli computed here are within 10% of the
42	    values printed in Fig1-S1.ipynb for at least 14 of the 18 species and stimulus pairs. It is
43	    partially reproduced for 9 to 13 pairs and not reproduced below 9. The fish cannot be
44	    matched one to one, as no identifier links the dandiset's subjects to the code's folders;
45	    the counts per species are compared instead. The sign of the zebrafish turning response
[... 140 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l paper/*.txt; cat papers/datasets/sabatini-2024.yaml 2>/dev/null; grep -n "sabatini" papers/keys.yaml | head
```

Result: not kept, because it reads the paper's text.

**Agent**

Read the protocol and the example format. Now reading the paper text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41467-024-51308-7.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; grep -v -E '^\s*\\(usepackage|setlength|documentclass)' 10.1038-s41467-024-51308-7.txt | sed -n '50,400p' | cut -c1-30000
```

```
10.1152/jn.1976.39.5.1062

Tanji, J. & Evarts, E. V. Anticipatory activity of motor cortex neurons in relation to direction of an intended movement. J. Neurophysiol. 39, 1062–1068 (1976).

10.1152/jn.2000.84.1.152

Messier, J. & Kalaska, J. F. Covariation of primate dorsal premotor cell activity with direction and amplitude during a memorized-delay reaching task. J. Neurophysiol. 84, 152–165 (2000).

10.1007/BF00241412

Riehle, A., MacKay, W. A. & Requin, J. Are extent and force independent movement parameters? Preparation- and movement-related neuronal activity in the monkey cortex. Exp. Brain Res. 99, 56–74 (1994).

10.1152/jn.00307.2006

Churchland, M. M., Santhanam, G. & Shenoy, K. V. Preparatory activity in premotor and motor cortex reflects the speed of the upcoming reach. J. Neurophysiol. 96, 3130–3146 (2006).

10.1007/BF00231153

Hocherman, S. & Wise, S. P. Effects of hand movement path on motor cortical activity in awake, behaving rhesus monkeys. Exp. Brain Res. 83, 285–302 (1991).

[... 331 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; f=10.1038-s41467-024-51308-7.txt; grep -n -E "Recoverab|Code availability|Data availability|References|Supplement:|github" $f | cut -c1-200; awk 'length($0)>300{print NR": "length($0)}' $f
```

```
61:				\begin{document}$${{{\bf{B}}}{{{\mbox{'}}}}}^{(c)}={{{\bf{L}}}}^{(c){\dagger} }{{{\bf{X}}}}^{(c)}$$\end{document} B ’ ( c ) = L ( c ) † X ( c ) where B’ ( c ) is the recovered temporal basis fu
66:https://github.com/kaufmanlab/LDR-public
329:##### Supplement: 41467_2024_51308_MOESM1_ESM.pdf (from the publisher's site)
7: 53366
25: 1452
34: 1245
52: 2097
61: 46071
267: 321
```

**Agent calls Bash**

```bash
cd paper; f=10.1038-s41467-024-51308-7.txt; sed -n '61p' $f | sed 's/\\documentclass.*\\end{document}/[EQ]/g' | fold -w 4000 -s; sed -n '62,70p' $f
```

```
<persisted-output>
Output too large (45.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/551f65a4-6521-45db-be76-3025df7749cb/tool-results/b8a2j26d2.txt

Preview (first 2KB):
				\begin{document}$${{{\bf{B}}}{{{\mbox{'}}}}}^{(c)}={{{\bf{L}}}}^{(c){\dagger} }{{{\bf{X}}}}^{(c)}$$\end{document} B ’ ( c ) = L ( c ) † X ( c ) where B’ ( c ) is the recovered temporal basis functions for condition c and † indicates pseudo-inversion. We quantified the “recoverability” of temporal basis functions on condition c as the variance explained in the temporal basis functions by the projected neural activity. If this metric is 1, it suggests that the condition’s loading matrix is invertible, and therefore fulfills the requirements of rotations. More specifically, we expect recoverability to fail when two (or more) temporal basis functions are assigned the same dimension in state space by the loading matrix. As each temporal basis functions dynamically supports each other, this overlap would preclude neural activity from acting as a dynamical system. Control for data smoothing One potential concern is that the factorization described above works well on neural data simply because the data are smoothed before analysis, and smoothing limits the frequency spectrum and therefore allows neural activity to be reconstructed by a small number of temporal basis functions. To test these possibilities, for each trial of each condition independently we shuffled time bins before smoothing and averaging, to disrupt the temporal structure of motor cortex activity while preserving inter-neuron spike correlations and total spike counts. We then extracted temporal basis functions, with the number of temporal basis functions matched to the original dataset, and quantified the population variance explained and recoverability (defined above) of the temporal basis functions. We compared this null distribution to the data distribution using a Wilcoxon signed-rank te
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; f=10.1038-s41467-024-51308-7.txt; sed -n '61p' $f | perl -pe 's/\\documentclass.*?\\end\{document\}/[EQ]/g' > $TMPDIR/m61.txt; wc -c $TMPDIR/m61.txt; fold -w 3000 -s $TMPDIR/m61.txt | head -c 25000
```

```
46326 /tmp/claude-1001/m61.txt
				\begin{document}$${{{\bf{B}}}{{{\mbox{'}}}}}^{(c)}={{{\bf{L}}}}^{(c){\dagger} }{{{\bf{X}}}}^{(c)}$$\end{document} B ’ ( c ) = L ( c ) † X ( c ) where B’ ( c ) is the recovered temporal basis functions for condition c and † indicates pseudo-inversion. We quantified the “recoverability” of temporal basis functions on condition c as the variance explained in the temporal basis functions by the projected neural activity. If this metric is 1, it suggests that the condition’s loading matrix is invertible, and therefore fulfills the requirements of rotations. More specifically, we expect recoverability to fail when two (or more) temporal basis functions are assigned the same dimension in state space by the loading matrix. As each temporal basis functions dynamically supports each other, this overlap would preclude neural activity from acting as a dynamical system. Control for data smoothing One potential concern is that the factorization described above works well on neural data simply because the data are smoothed before analysis, and smoothing limits the frequency spectrum and therefore allows neural activity to be reconstructed by a small number of temporal basis functions. To test these possibilities, for each trial of each condition independently we shuffled time bins before smoothing and averaging, to disrupt the temporal structure of motor cortex activity while preserving inter-neuron spike correlations and total spike counts. We then extracted temporal basis functions, with the number of temporal basis functions matched to the original dataset, and quantified the population variance explained and recoverability (defined above) of the temporal basis functions. We compared this null distribution to the data distribution using a Wilcoxon signed-rank test to test for differences in distributions. Control for stereotyped time course of behavior One potential concern is that the factorization described above can find common frequencies 
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n '440,762p' 10.1038-s41467-024-51308-7.txt | grep -v -E '^\s*\S{0,12}\s*$'
```

```
different planes
and eigenvalues
(cond. specific LDS) 
different planes,
shared eigenvalues
Supplementary Figure 4: Rotational planes differ between conditions. a, Alignment indices 
between corresponding (same-frequency) rotational planes on pairs of conditions (colored) and 
distribution expected due to estimation noise (gray).  b, Subspace Excursion Angles for 
corresponding rotational planes across conditions (colored), along with angles expected due to 
estimation noise (gray; Line, mean; shaded, 1 standard deviation).  
0.5 Hz
1.5 Hz
2.5 Hz
4.0 Hz
1.5 Hz
2.5 Hz
4.0 Hz
0.5 Hz
0.5 Hz
1.5 Hz
[... 149 more lines not kept]
```

**Agent**

The full text, Methods and supplement are all present. Next I'll read the linked code (kaufmanlab/LDR-public).

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/kaufmanlab/LDR-public && cd LDR-public && git log -1 --format='%H %ad' && find . -type f -not -path './.git/*' | head -100 && cat README* | head -80
```

```
b65f28dd46106da8cb40bc8a19f0d0c22f5fdb38 Fri Aug 2 12:40:30 2024 -0500
./README.md
./neuralAndKinematicsInvestigation/neuralFromKinematics/Analysis/kinToTBF.m
./neuralAndKinematicsInvestigation/neuralFromKinematics/Analysis/linearControls.m
./neuralAndKinematicsInvestigation/neuralFromKinematics/Analysis/nonlinearControls.m
./neuralAndKinematicsInvestigation/neuralFromKinematics/predictDataUsingTBFandKinCondStructureNonlinear.m
./neuralAndKinematicsInvestigation/neuralFromKinematics/predictDataUsingTBFandKinCondStructure.m
./neuralAndKinematicsInvestigation/neuralFromKinematics/Controls/predictDataUsingKinNonlinear.m
./neuralAndKinematicsInvestigation/neuralFromKinematics/Controls/predictDataUsingKin.m
./neuralAndKinematicsInvestigation/neuralFromKinematics/Controls/predictDataUsingTBFandKinNN.m
./neuralAndKinematicsInvestigation/kinematicsFromNeural/predictKinUsingTBFandDataCondStructure.m
./neuralAndKinematicsInvestigation/kinematicsFromNeural/Analysis/kinFromTBF.m
./neuralAndKinematicsInvestigation/kinematicsFromNeural/Analysis/linearDecodingControls.m
./neuralAndKinematicsInvestigation/kinematicsFromNeural/Analysis/nonlinearDecodingControls.m
./neuralAndKinematicsInvestigation/kinematicsFromNeural/Analysis/kinFromTBFSingleTrial.m
./neuralAndKinematicsInvestigation/kinematicsFromNeural/Analysis/linearDecodingControlsSingleTrial.m
./neuralAndKinematicsInvestigation/kinematicsFromNeural/Analysis/rnnControl.m
./neuralAndKinematicsInvestigation/kinematicsFromNeural/Analysis/nonlinearDecodingControlsSingleTrial.m
./neuralAndKinematicsInvestigation/kinematicsFromNeural/Analysis/kinFromTBFNoPotent.m
./neuralAndKinematicsInvestigation/kinematicsFromNeural/predictKinUsingTBFandDataCondStructureSingletrial.m
[... 83 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/LDR-public && find . -type f -not -path './.git/*' | tail -n +101; wc -l $(find . -name '*.m') | tail -1
```

```
./utils/alignment/findBlocks.m
./utils/alignment/averageTrialsCO.m
./utils/alignment/extractHumanTrials2.m
./utils/alignment/trialAvHuman2.m
./utils/alignment/extractTrialsPursuit.m
./utils/alignment/pairPointPosVel.m
./utils/alignment/extractHumanTrialsTargetPursuit.m
./utils/alignment/xcorrAlign.m
./subspaceStatistics/quantifyProjectedVarianceSingleFrequency.m
./subspaceStatistics/Analysis/quantifySingleFrequencyOverlap.m
./subspaceStatistics/Analysis/quantifyTwoFrequencyOverlap.m
./subspaceStatistics/Analysis/oneComponentToAnother.m
./subspaceStatistics/Analysis/offsetToRotations.m
./subspaceStatistics/Analysis/oneComponentToAnotherNonlinear.m
./subspaceStatistics/predictOneComponentFromAnotherNonlinear.m
./subspaceStatistics/Controls/singleFrequencyOverlapControl.m
./subspaceStatistics/quantifyProjectedVarianceDifferentFrequencies.m
./subspaceStatistics/predictRotationsFromOffsetNonlinear.m
./subspaceStatistics/predictOneComponentFromAnother.m
./subspaceStatistics/predictRotationsFromOffsetMouse.m
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/LDR-public && for f in utils/crossvalidation/preprocessTrials.m utils/alignment/extractTrialsCO.m utils/alignment/averageTrialsCO.m TBF/analysis/TBF.m TBF/getBasisFxns.m; do echo "=== $f"; cat $f; done
```

```
=== utils/crossvalidation/preprocessTrials.m
function trials = preprocessTrials(trials)
%% OVERVIEW

% This function pre-processes trials binned at 1 ms resolution by first
% smoothing the trials with a 20 ms Gaussian kernel then down-sampling to
% 10 ms resolution.

%% Pre-process trials.

% For each trial, smooth then down-sample.
for trial = 1:size(trials,2)
    trialArray = full(double(trials(trial).matrix));
    for neuron = 1:size(trialArray)
        trialArray(neuron,:) = imgaussfilt(1000*trialArray(neuron,:), ...
            20,'FilterSize',111,'Padding','Symmetric');
    end
    trials(trial).matrix = trialArray(:,1:10:end);
end

[... 252 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/LDR-public && grep -rn -i -E "maze|ShenoyMonkeyData\b.*=|timePeriod|-15|850|86\b|101\b|softNorm|soft" --include=*.m . | grep -v "^.*%.*$" | head -60; echo; grep -rln "load('ShenoyMonkeyData" . | wc -l
```

```
./neuralAndKinematicsInvestigation/neuralFromKinematics/Analysis/kinToTBF.m:30:ShenoyMonkeyData = ShenoyMonkeyData(1:2);
./neuralAndKinematicsInvestigation/neuralFromKinematics/Analysis/linearControls.m:33:ShenoyMonkeyData = ShenoyMonkeyData(1:2);
./neuralAndKinematicsInvestigation/neuralFromKinematics/Analysis/nonlinearControls.m:31:ShenoyMonkeyData = ShenoyMonkeyData(1:2);
./neuralAndKinematicsInvestigation/neuralFromKinematics/predictDataUsingTBFandKinCondStructureNonlinear.m:22:kinFxns = kinFuncEval(-350:10:850,'position');
./neuralAndKinematicsInvestigation/neuralFromKinematics/predictDataUsingTBFandKinCondStructure.m:17:kinFxns = kinFuncEval(-350:10:850,'position');
./neuralAndKinematicsInvestigation/neuralFromKinematics/Controls/predictDataUsingTBFandKinNN.m:13:kinFxns = kinFuncEval(-350:10:850,'position');
./neuralAndKinematicsInvestigation/kinematicsFromNeural/predictKinUsingTBFandDataCondStructure.m:17:kinFxns = kinFuncEval(-350:10:850,'position');
./neuralAndKinematicsInvestigation/kinematicsFromNeural/predictKinUsingTBFandDataCondStructure.m:55:kinFxnsVel = kinFuncEval(-350:10:850,'velocity');
./neuralAndKinematicsInvestigation/kinematicsFromNeural/Analysis/kinFromTBF.m:34:ShenoyMonkeyData = ShenoyMonkeyData(1:2);
./neuralAndKinematicsInvestigation/kinematicsFromNeural/Analysis/linearDecodingControls.m:29:ShenoyMonkeyData = ShenoyMonkeyData(1:2);
./neuralAndKinematicsInvestigation/kinematicsFromNeural/Analysis/nonlinearDecodingControls.m:29:ShenoyMonkeyData = ShenoyMonkeyData(1:2);
./neuralAndKinematicsInvestigation/kinematicsFromNeural/Analysis/kinFromTBFSingleTrial.m:34:ShenoyMonkeyData = ShenoyMonkeyData(1:2);
./neuralAndKinematicsInvestigation/kinematicsFromNeural/Analysis/linearDecodingControlsSingleTrial.m:29:ShenoyMonkeyData = ShenoyMonkeyData(1:2);
./neuralAndKinematicsInvestigation/kinematicsFromNeural/Analysis/nonlinearDecodingControlsSingleTrial.m:29:ShenoyMonkeyData = ShenoyMonkeyData(1:2);
./neuralAndKinematicsInvestigation/kinematicsFromNeu
[... 48 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/LDR-public && for f in utils/crossvalidation/pruneRepeats.m utils/evalFit/getVarExplained.m utils/evalFit/getAlignmentIndex.m utils/evalFit/getRecoverability.m utils/evalFit/useFactorization.m TBF/eigTransform.m TBF/analysis/crossValidateDimensionalityBasisFxns.m TBF/analysis/quantifyTBFStats.m; do echo "=== $f"; grep -v '^\s*$' $f; done
```

```
=== utils/crossvalidation/pruneRepeats.m
function data = pruneRepeats(data)
%% OVERVIEW
% This function prunes out the conditions that involve a visual distractor
% in the monkeys vision, but are essentially repeats of curved conditions.
%% Prune repeats.
data(3:3:end) = [];
end
=== utils/evalFit/getVarExplained.m
function VE = getVarExplained(data,approx,flag)
%% OVERVIEW
% This function takes data and approximations to the data and returns the 
% quality of the fit as quantified by the variance explained. If the flag
% is 'pooled', then a scalar is returned. If the flag is 'ind', then an
% array of variance explained for single conditions is returned.
%% Quantify the variance explained.
% Remove parts of the data not approximated, assuming that approximation is
% uniform across neurons but not time.
for cond = 1:size(data,2)
    inds = find(isnan(approx(cond).matrix(1,:)));
[... 290 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/LDR-public/FittingDynamicsToSingleConditions && for f in idDynamics.m eigValDistance.m averageEigVals.m analysis/fitSingleLDS.m analysis/crossValidateDimensionalityConditions.m analysis/compareTrialSimilarity.m analysis/getCorrelationsWithFrequency.m; do echo "=== $f"; grep -v '^\s*$' $f; done
```

```
=== idDynamics.m
function [subspaces,eigVals,params,approx,sim,basisFxns] = idDynamics(data,dimUse)
%% OVERVIEW
% This function takes in data locked to movement onset, along with a
% parameter expressing the dimensionality to use, and returns for each
% condition independently the eigenvectors in which the dynamics reside,
% along with the eigenvalues of those dynamics, the parameters described by
% those eigenvalues, and the approximation to the data provided. 
%% Find the dynamics describing each conditions.
% For each condition, find dynamics. 
subspaces = data;
eigVals = zeros(dimUse,size(data,2));
approx = data;
basisFxns = zeros(size(data(1).matrix,2),dimUse,size(data,2));
params.param = zeros(dimUse,3,size(data,2));
params.functionalForm = zeros(dimUse,3,size(data,2));
params.meaning = ...
    ["Frequency (cycles/sec)" "Phase (degrees)" "Half-life (sec)"];
for cond = 1:size(data,2)
    % Fit dynamics to the data in the low-dimensional space. 
[... 425 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/LDR-public/subspaceStatistics && for f in quantifyProjectedVarianceSingleFrequency.m Analysis/quantifySingleFrequencyOverlap.m Controls/singleFrequencyOverlapControl.m quantifyProjectedVarianceDifferentFrequencies.m Analysis/quantifyTwoFrequencyOverlap.m; do echo "=== $f"; grep -v -E '^\s*(%.*)?$' $f; done
```

```
=== quantifyProjectedVarianceSingleFrequency.m
function output = quantifyProjectedVarianceSingleFrequency(loadings,basisFxns,params)
IDs = pairID(params(:,1));
uniqueIDs = unique(IDs);
for ID = uniqueIDs
    inds = find(IDs == ID);
    output(ID).alignmentIndex = zeros(size(loadings,2),size(loadings,2));
    for cond1 = 1:size(loadings,2)
        for cond2 = 1:size(loadings,2)
            output(ID).alignmentIndex(cond1,cond2) = getAlignmentIndex( ...
                loadings(cond1).matrix(:,inds)*basisFxns(:,inds).', ...
                loadings(cond2).matrix(:,inds));
        end
    end
    copyArray = output(ID).alignmentIndex;
    for cond = 1:size(loadings,2)
        copyArray(cond,cond) = nan;
    end
    copyArray = copyArray(:);
    copyArray(isnan(copyArray)) = [];
[... 198 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/LDR-public && for f in subspaceStatistics/predictOneComponentFromAnother.m subspaceStatistics/Analysis/oneComponentToAnother.m subspaceStatistics/predictRotationsFromOffset.m subspaceStatistics/Analysis/offsetToRotations.m utils/crossvalidation/cvConds.m utils/crossvalidation/splitTrials.m; do echo "=== $f"; grep -v -E '^\s*(%.*)?$' $f; done
```

```
=== subspaceStatistics/predictOneComponentFromAnother.m
function [groundTruthTensor,predictedData,reassambleTensor] = predictOneComponentFromAnother( ...
    data,leaveOut,L2,factorDim,svEnergy)
[train,test] = splitTrials([data().condNum],leaveOut);
for partition = 1:size(train,1)
    condInds = find(train(partition,:));
    [basisFxns,loadings,params] = eigTransform(data(train(partition,:)),factorDim);
    indices = [1 1+kron(1:floor(factorDim/2),[1 1])];
    for predictorIndex = 1:ceil(factorDim/2)
        for predictedIndex = 1:ceil(factorDim/2)
            predictor = (indices == predictorIndex);
            predicted = (indices == predictedIndex);
            predictedLoadings = loadings;
            predictorLoadings = loadings;
            for cond = 1:size(loadings,2)
                predictedLoadings(cond).matrix = ...
                    predictedLoadings(cond).matrix(:,predicted);
                predictedLoadings(cond).matrix = ...
                    predictedLoadings(cond).matrix(:);
                groundTruthTensor(predictedIndex,condInds(cond)).matrix ...
[... 259 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/LDR-public && grep -rn "function.*kinFuncEval" . ; cd neuralAndKinematicsInvestigation && for f in neuralFromKinematics/Analysis/kinToTBF.m neuralFromKinematics/predictDataUsingTBFandKinCondStructure.m kinematicsFromNeural/Analysis/kinFromTBFSingleTrial.m kinematicsFromNeural/predictKinUsingTBFandDataCondStructureSingletrial.m; do echo "=== $f"; grep -v -E '^\s*(%.*)?$' $f; done
```

```
=== neuralFromKinematics/Analysis/kinToTBF.m
function output = kinToTBF
kernelType = 'OU';
kernelScale = 10^3;
nonlinearL2 = 0;
linearL2 = 0.1;
holdOutNum = 6;
load('ShenoyMonkeyData');
ShenoyMonkeyData = ShenoyMonkeyData(1:2);
load('basisFxnNum');
for monkey = 1:size(ShenoyMonkeyData,2)
    output(monkey).M1 = prepForAnalysis(ShenoyMonkeyData(monkey).M1, ...
        ShenoyMonkeyData(monkey).Kinematics, ...
        kernelType,kernelScale,nonlinearL2,linearL2,holdOutNum, ...
        basisFxnNum(monkey).M1.maxDim);
    output(monkey).PMd = prepForAnalysis(ShenoyMonkeyData(monkey).PMd, ...
        ShenoyMonkeyData(monkey).Kinematics, ...
        kernelType,kernelScale,nonlinearL2,linearL2,holdOutNum, ...
        basisFxnNum(monkey).PMd.maxDim);
end
[... 199 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/LDR-public && for f in utils/evalFit/getVarExplainedKinematics.m utils/singleTrialDecoding/studyAroundMeanParams.m utils/TBFandCondSpecificDynamics/scrambleTrials.m utils/TBFandCondSpecificDynamics/warpTrials.m reconciliation/jPCAReconciliation/getRotations.m reconciliation/jPCAReconciliation/Analysis/getCorrOverlapWithjPCA.m utils/crossvalidation/generateTrials.m; do echo "=== $f"; grep -v -E '^\s*(%.*)?$' $f | head -70; done
```

```
=== utils/evalFit/getVarExplainedKinematics.m
function VE = getVarExplainedKinematics(kinematics,approx)
VE.pos.array = zeros(1,size(kinematics,2));
for cond = 1:size(kinematics,2)
    VE.pos.array(cond) = 1 -sum(var(kinematics(cond).matrix - approx(cond).position,0,1))/ ...
        sum(var(kinematics(cond).matrix,0,1));
end
VE.pos.array(VE.pos.array < 0) = 0;
VE.pos.mean = mean(VE.pos.array);
VE.pos.std = std(VE.pos.array);
VE.vel.array = zeros(1,size(kinematics,2));
for cond = 1:size(kinematics,2)
    VE.vel.array(cond) = 1 -sum(var(diff(kinematics(cond).matrix,1,1) - approx(cond).velocity(2:end,:),0,1))/ ...
        sum(var(diff(kinematics(cond).matrix,1,1),0,1));
end
VE.vel.array(VE.vel.array < 0) = 0;
VE.vel.mean = mean(VE.vel.array);
VE.vel.std = std(VE.vel.array);
end
=== utils/singleTrialDecoding/studyAroundMeanParams.m
[... 128 more lines not kept]
```

**Agent**

Code reading done. Checking the existing churchland-2012 claims (same dandiset) for how the data were described, and the check tool's usage.

**Agent calls Bash**

```bash
head -60 claims/churchland-2012.yaml; cat papers/datasets/churchland-2012.yaml; head -40 tools/claims_check.py; grep -n "^  [a-z_]*:" claims/*.yaml | awk -F: '{print $3}' | sort | uniq -c | sort -rn | head -30
```

```
# Claims for Churchland, Cunningham, Kaufman, Foster, Nuyujukian, Ryu & Shenoy (2012) on
# dandiset 000070.
# Source: the NIH author manuscript in PubMed Central (PMC3393826), full text, read from its
# Results, Methods and figure legends, and the Supplementary Information PDF from the
# publisher's site. Values marked "read from the figure" are readings of Figure 6, which the
# text does not give in numbers.
#
# When these criteria were written, the author had seen the data check only: the file list,
# metadata, trial tables, unit counts and firing rates, trial counts per condition after the
# Methods' selection, hand speed around movement onset, and the faults of the files (the
# wrapped first entry of spike_times_index, and the clock resets of the 2010 file). No jPCA
# or other claim analysis had been run on any file.
#
# The dandiset holds the paper's two array datasets, J-array (sub-Jenkins ses-20090918) and
# N-array (sub-Nitschke ses-20100923), each with 108 maze conditions. It does not hold the
# seven single-electrode datasets (monkeys A, B, J1 to J4 and N), the EMG, the leech or the
# walking-monkey data. It also holds eight further array sessions the paper does not use,
# one of which (sub-Nitschke ses-20090910, 108 conditions) is consistent with the
# "N-9-10-2010" dataset of Supplementary Figure 5 (see the notebook).
#
[... 105 more lines not kept]
```

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
python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1)); print(json.dumps({k:v for k,v in s['properties'].items() if k not in ('dataset','paper','claims')},indent=1)[:3000])"
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
[... 128 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -B2 -A8 "widened" claims/*.yaml | head -60
```

```
claims/amjad-2025.yaml-162-    blocks, cut by the start and end of the file, are reported but not judged. Reproduced when
claims/amjad-2025.yaml-163-    the forced share is within tolerance and every complete block is 45 to 330 trials long (the
claims/amjad-2025.yaml:164:    reported range widened by 10% of each bound); partially reproduced when only one of the two
claims/amjad-2025.yaml-165-    holds.
claims/amjad-2025.yaml-166-- id: zenodo-link
claims/amjad-2025.yaml-167-  kind: link
claims/amjad-2025.yaml-168-  statement: The dandiset reproduces the processed data the paper deposited on Zenodo; the trial
claims/amjad-2025.yaml-169-    selections and the beta power of the paper's example trial computed from the dandiset agree
claims/amjad-2025.yaml-170-    with the paper's own files.
claims/amjad-2025.yaml-171-  source: Data Availability Statement (doi:10.5281/zenodo.14826579)
claims/amjad-2025.yaml-172-  quote: Data used in this study are available at zenodo
--
claims/andrews-2024.yaml-570-    comment gives Holm-adjusted p < 0.05 over the step's trials. Reproduced when, under one
claims/andrews-2024.yaml-571-    reading, the threshold of at least two of the three slices lies in 23.6 to 34.3 mW/mm2 (the
claims/andrews-2024.yaml:572:    range widened by 10% of each bound).
claims/andrews-2024.yaml-573-- id: chr2-increase
claims/andrews-2024.yaml-574-  statement: In a ChR2-transduced slice (4C), 470 nm light increased unit firing; the rate after
claims/andrews-2024.yaml-575-    light-OFF did not differ significantly from pre, and spike amplitude did not change
claims/andrews-2024.yaml-576-    significantly between pre and light-ON.
claims/andrews-2024.yaml-577-  source: Results, Optical HcKCR1-mediated inhibition of network activity, paragraph 1; Extended
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/LDR-public && grep -v -E '^\s*(%.*)?$' reconciliation/jPCAReconciliation/Analysis/getRotationalProjCompare.m | head -60; echo ====; grep -v -E '^\s*(%.*)?$' neuralAndKinematicsInvestigation/kinematicsFromNeural/removePotent.m | head -50; echo ===; grep -rln -i "offset\|location" --include=*.m . | head; grep -rn "kinFuncEval\|skew" --include=*.m . | grep -v "kinFuncEval(-350" | head
```

```
function output = getRotationalProjCompare
load('TBFResults');
for monkey = 1:size(TBFResults,2)
    [~,~,~,output(monkey).M1.R2s] ...
        = getRotations(TBFResults(monkey).M1.loadings, ...
        TBFResults(monkey).M1.basisFxns,2);
    [~,~,~,output(monkey).M1.R2sStraight] ...
        = getRotations(TBFResults(monkey).M1.loadings(1:2:end), ...
        TBFResults(monkey).M1.basisFxns,2);
    [~,~,~,output(monkey).M1.R2sCurved] ...
        = getRotations(TBFResults(monkey).M1.loadings(2:2:end), ...
        TBFResults(monkey).M1.basisFxns,2);
    [~,~,~,output(monkey).PMd.R2s] ...
        = getRotations(TBFResults(monkey).PMd.loadings, ...
        TBFResults(monkey).PMd.basisFxns,2);
    [~,~,~,output(monkey).PMd.R2sStraight] ...
        = getRotations(TBFResults(monkey).PMd.loadings(1:2:end), ...
        TBFResults(monkey).PMd.basisFxns,2);
    [~,~,~,output(monkey).PMd.R2sCurved] ...
        = getRotations(TBFResults(monkey).PMd.loadings(2:2:end), ...
[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
ls -t claims/*.yaml | head -3; f=$(ls -t claims/*.yaml | head -1); head -45 $f
```

```
claims/zhuang-2025.yaml
claims/zhu-2022.yaml
claims/zhong-2026.yaml
# Claims for Zhuang, Lemak, Sridhar & Nelson (2025), Brain 149:238-251, on dandiset 001177.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-28,
# protocol pilot-12 as stated in docs/protocol.md. The writer did not look at the dandiset's data or
# files; only its title and description on the archive were read. Claim fig1fg-delay-discounting
# was added by the check of 2026-10-28.
#
# Text read: the version of record (open access, CC BY), full text as served by Europe PMC
# (PMC12597312), with its one supplement, awaf312_supplementary_data.pdf (Figures S1 to S8 and
# legends, Supplementary Materials and methods, and Table 1, "Experimental analysis and
# statistics"). Figure panels of the main paper were not available as images; values in the main
# figure legends were read from the text. The pie-chart percentages of Figures S5D and S8A-B were
# read from the supplement PDF (pages 7 and 10), as the text holds only the legends.
#
# Code read. The paper links (1) UCSF-Nelson-Lab/ICD-Cognitive-Analysis, tag ICD, commit 5528e22
# (Zenodo doi:10.5281/zenodo.10703139, record 10703140): Python scripts that count task events per
# block of the delay discounting task (delay_discounting_task.py, phase2.py, phase3.py) and
# Summary_Cognitive.m, which averages each mouse's sessions within a condition, fits
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 45,140p claims/zhuang-2025.yaml
```

```
#   Claims on them have data elsewhere. Delay discounting cohorts: PPX Ctrl 16 and Park 31 mice;
#   A77636 Ctrl 10 and Park 16; DREADD mCherry 15, hM4Di 12, hM3Dq 12. Each session has four blocks
#   (delays 0, 3, 6, 9 s) of 5 forced delayed/large, 5 forced immediate/small and 20 free choice
#   trials; the measure is the percentage of free choice trials, omissions excluded, on which the
#   delayed/large reward was chosen.
#
# Method shared by the electrophysiology claims, from the Supplementary Materials and methods
# ("In vivo electrophysiology" and "Experimental design & statistical analysis, In vivo
# electrophysiology"): firing rates in 1 min bins; baseline -30 to 0 min; the post-drug epoch
# 240 to 300 min, split into 241-270 and 271-300 min; a unit is 'increase' type when a Wilcoxon
# signed-rank test (p < 0.01) finds a significant increase against baseline in both 30 min post
# epochs, 'decrease' when a significant decrease in both, 'no change' when neither; optical
# identification by a PSTH around laser onset, the rate
# exceeding the 99% confidence interval of baseline within 15 ms of onset and staying above it for
# at least 15 ms, with light-evoked waveforms not distinguishable from spontaneous ones.
# Details these sources leave open, with the readings allowed, used by several claims:
# - Putative MSN classification: the thresholds are not given; readings are (a) a classification
#   deposited with the units by the authors, (b) the criteria of the cited papers (Berke et al.
#   2004, Neuron 43:883; Gage et al. 2010, Neuron 67:466) applied to peak to valley and peak width.
# - Optical identification: the PSTH bin width, the baseline window for the 99% interval and the
[... 76 more lines not kept]
```

**Agent calls Bash**

```bash
grep -L "^dataset:" claims/*.yaml | head;
```

```
claims/alasfour-2024.yaml
claims/andrews-2024.yaml
claims/asari-2009.yaml
claims/brinke-2017.yaml
claims/brudner-2026.yaml
claims/burman-2023.yaml
claims/dana-2016.yaml
claims/danish-2017.yaml
claims/dijk-2018.yaml
claims/drieu-2018.yaml
```

**Agent calls Bash**

```bash
cd $TMPDIR/LDR-public && grep -rn -i "gpfa\|xDim\|lambda\|L2 =\|kernelScale =\|holdOutNum =\|smooth" neuralAndKinematicsInvestigation/kinematicsFromNeural/Analysis/*.m neuralAndKinematicsInvestigation/neuralFromKinematics/Analysis/*.m | head -40; grep -v -E '^\s*(%.*)?$' TBF/analysis/modelComp.m | head -40
```

```
neuralAndKinematicsInvestigation/kinematicsFromNeural/Analysis/kinFromTBF.m:16:kernelScale = 10^3;
neuralAndKinematicsInvestigation/kinematicsFromNeural/Analysis/kinFromTBF.m:19:nonlinearL2 = 0;
neuralAndKinematicsInvestigation/kinematicsFromNeural/Analysis/kinFromTBF.m:25:linearL2 = 1;
neuralAndKinematicsInvestigation/kinematicsFromNeural/Analysis/kinFromTBF.m:28:holdOutNum = 2;
neuralAndKinematicsInvestigation/kinematicsFromNeural/Analysis/kinFromTBF.m:43:        basisFxnNum(monkey).M1.maxDim,decodeDim);
neuralAndKinematicsInvestigation/kinematicsFromNeural/Analysis/kinFromTBF.m:48:        basisFxnNum(monkey).PMd.maxDim,decodeDim);
neuralAndKinematicsInvestigation/kinematicsFromNeural/Analysis/kinFromTBFNoPotent.m:17:kernelScale = 10^3;
neuralAndKinematicsInvestigation/kinematicsFromNeural/Analysis/kinFromTBFNoPotent.m:20:nonlinearL2 = 0;
neuralAndKinematicsInvestigation/kinematicsFromNeural/Analysis/kinFromTBFNoPotent.m:26:linearL2 = 1;
neuralAndKinematicsInvestigation/kinematicsFromNeural/Analysis/kinFromTBFNoPotent.m:29:holdOutNum = 2;
neuralAndKinematicsInvestigation/kinematicsFromNeural/Analysis/kinFromTBFNoPotent.m:49:        basisFxnNum(monkey).M1.maxDim,decodeDim, ...
neuralAndKinematicsInvestigation/kinematicsFromNeural/Analysis/kinFromTBFNoPotent.m:59:        basisFxnNum(monkey).PMd.maxDim,decodeDim, ...
neuralAndKinematicsInvestigation/kinematicsFromNeural/Analysis/kinFromTBFSingleTrial.m:16:kernelScale = 10^3;
neuralAndKinematicsInvestigation/kinematicsFromNeural/Analysis/kinFromTBFSingleTrial.m:19:nonlinearL2 = 10^-5;
neuralAndKinematicsInvestigation/kinematicsFromNeural/Analysis/kinFromTBFSingleTrial.m:25:linearL2 = 10;
neuralAndKinematicsInvestigation/kinematicsFromNeural/Analysis/kinFromTBFSingleTrial.m:28:holdOutNum = 2;
neuralAndKinematicsInvestigation/kinematicsFromNeural/Analysis/kinFromTBFSingleTrial.m:46:        basisFxnNum(monkey).M1.maxDim,decodeDim);
neuralAndKinematicsInvestigation/kinematicsFromNeural/Analysis/kinFromTBFSingleTrial.m:53:
[... 41 more lines not kept]
```

**Agent**

I have what I need. Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/sabatini-2024.yaml",
 "content": "# Claims for Sabatini & Kaufman (2024), Nat. Commun. 15:7007, \"Reach-dependent reorientation of\n# rotational dynamics in motor cortex\", tested on dandiset 000070 (relation reuses).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-20,\n# protocol pilot-18 as stated in docs/protocol.md. The writer did not look at the dandiset's data\n# or files.\n#\n# Text read: the version of record (open access, CC BY-NC-ND), full text from PubMed Central\n# (PMC11325044) with Methods, figure legends and Data and Code availability, and its one\n# supplement, 41467_2024_51308_MOESM1_ESM.pdf (Supplementary Figures 1 to 8 with legends and the\n# derivation of the basis function representation of a linear dynamical system). The Peer Review\n# File and Reporting Summary were not read; no result rests on them. The supplement PDF was not\n# opened beyond its extracted text.\n#\n# Code read: github.com/kaufmanlab/LDR-public at commit b65f28d (2024-08-02), the MATLAB code the\n# Code availability statement links. It holds the analysis functions (TBF, single-condition LDS,\n# alignment index, subspace excursion angles, rotation and location prediction, LDR encoding and\n# decoding, jPCA reconciliation). It loads preprocessed .mat files that are not in the repository\n# (ShenoyMonkeyData, ShenoyMonkeyDataSingleTrial, basisFxnNum, TBFResults and others; the paper\n# says \"Code-compatible data are available upon request\"), and lacks kinFuncEval (the kinematic\n# basis functions), the jPCA codepack, GPFA, and code for the location-from-kinematics regression\n# (Figure 6e) and the eigenvalue Poisson null. Where the Methods are silent and the code settles a\n# detail, the claim says so; where they differ, the Methods decide and the code's choice is a\n# variant.\n#\n# Data the paper used. Reanalysed data of earlier studies (refs 19, 27, 40; Churchland et al. 2010\n# and 2012, Kaufman et al. 2016): two adult male rhesus macaques, J and N, performing the \"maze\"\n# delayed center-out reach task with a 0 to 1000 ms delay; 72 conditions (36 straight, 36 curved\n# around virtual barriers); two 96-electrode Utah arrays per monkey, one in PMd and one in M1;\n# single units and stable multi-units, 79 to 118 units per array; 1469 trials for J and 2014 for N\n# (Figure 7 legend). Four datasets, each analysed separately: M1-J, PMd-J, M1-N, PMd-N. Hand\n# position over time is the kinematic variable; Supplementary Figure 8 and the code also use\n# muscle activity (EMG). The Data availability statement names the dandiset files\n# sub-Jenkins_ses-20090918_behavior+ecephys.nwb and sub-Nitschke_ses-20100923_behavior+ecephys.nwb.\n#\n# Method shared by the claims, from the Methods unless marked.\n# - Spikes binned at 1 ms, smoothed with a Gaussian of 20 ms s.d., trial-averaged per condition,\n#   down-sampled to 10 ms, aligned to movement onset (Methods, Subjects, behavior and data\n#   pre-processing; code preprocessTrials.m, kernel width 111 samples, symmetric padding).\n# - Time base. The code's condition data are on a -350 to +850 ms grid every 10 ms (121 bins;\n#   kinFuncEval(-350:10:850), generateTrials.m). Dynamics are fitted from bin 20 on, which the\n#   Methods give as 150 ms before movement onset to 850 ms after (Fitting dynamics to single\n#   conditions; De-mixing temporal basis functions). Kinematic summaries use the whole -350 to\n#   +850 ms window (code).\n# - The 72 conditions. The source data hold 108 maze conditions; the code drops every third one\n#   (pruneRepeats.m, data(3:3:end) = [], \"conditions that involve a visual distractor ... but are\n#   essentially repeats of curved conditions\"). In the code's order, odd conditions are straight\n#   and even ones curved (getRotationalProjCompare.m). The order of the code's .mat files is not\n#   public. Readings for selecting the 72: (a) drop the conditions whose maze condition number is\n#   a multiple of 3; (b) drop the conditions identified from the maze geometry as repeating a\n#   curved condition's target and barrier with a distractor added. The author reports how many of\n#   36 straight and 36 curved each gives.\n# - Trials. The paper gives no trial selection beyond the task; readings are (a) all successful\n#   trials of the 72 conditions, (b) successful trials with a delay above 400 ms as in the original\n#   studies. The counts are compared with 1469 and 2014.\n# - Temporal basis factorization (TBF). SVD of the (neurons x conditions)-by-time matrix of\n#   condition-averaged rates; top k temporal singular vectors are the basis functions, k by\n#   cross-validation over two halves of the trials, 100 folds, maximising held-out variance\n#   explained (code crossValidateDimensionalityBasisFxns.m tests k = 1 to 20 and raises an even k\n#   by one); de-mixed by fitting an LDS to the basis functions and projecting onto its\n#   eigenvectors (code eigTransform.m, which then replaces the basis by damped sinusoids of the\n#   fitted frequencies and half-lives). getBasisFxns.m computes max-normalised rates but runs the\n#   SVD on the unnormalised ones; the unnormalised SVD is the code's choice.\n# - Population variance explained, per condition, is 1 minus the summed variance over neurons of\n#   the residual over the summed variance of the data, negative values set to 0 (code\n#   getVarExplained.m). Reported means and s.d. are across conditions.\n# - Alignment index of condition 1's rotation onto condition 2's plane is the fraction of the\n#   variance of condition 1's rotation (its loading columns times the basis functions) captured by\n#   projection onto the span of condition 2's loading columns (code getAlignmentIndex.m and\n#   quantifyProjectedVarianceSingleFrequency.m).\n# - ROC-AUC between an observed and a null distribution is folded to at least 0.5 (code\n#   compareTrialSimilarity.m, 0.5 + |AUC - 0.5|).\n# Rule for ranges. A value reported as a range over the four datasets (\"0.64-0.73\") is reproduced\n# when each dataset's value lies inside the range widened by 10% of each bound, and partially\n# reproduced when two or three of the four do. Where the paper's text, Methods and code name\n# different tests for the same comparison (Wilcoxon rank-sum against signed-rank), the Methods'\n# or Results' test decides and the other is shown as a variant.\nschema_version: 2\npaper: doi:10.1038/s41467-024-51308-7\nclaims:\n- id: data-composition\n  statement: Two monkeys (J and N) performed the maze task with 72 conditions (36 straight, 36\n    curved); a PMd and an M1 array in each monkey gave 79 to 118 units per array; 1469 trials for\n    monkey J and 2014 for monkey N.\n  source: Results, paragraph 1; Methods, Subjects, behavior and data pre-processing; Figure 7 legend\n  quote: We refer to the 72 unique combinations of target and virtual barrier positions as\n    \"conditions\". Simultaneous single- and multi-unit electrophysiological recordings were made\n    with a pair of 96-electrode Utah arrays in each monkey, implanted in PMd and in M1, yielding\n    79–118 units per array.\n  expected:\n  - quantity: conditions per monkey\n    value: 72\n    tolerance: 0\n  - quantity: trials, monkey J\n    value: 1469\n    tolerance: 146.9\n  - quantity: trials, monkey N\n    value: 2014\n    tolerance: 201.4\n  criterion: Conditions and trials under the readings of the shared method. Reproduced when, under\n    one reading, each monkey has 72 conditions (36 straight, 36 curved), each trial count is\n    within tolerance, and each of the four arrays has 71 to 130 units (79 to 118 widened by 10%),\n    counting single units and multi-units the dataset marks as such.\n- id: jpca-fit-r2\n  statement: Rotational dynamics found by jPCA fit activity within the jPCA planes with R2 of 0.64\n    to 0.73, higher on straight reaches (0.73 to 0.88) than on curved reaches (0.56 to 0.70).\n  source: Results, Rotational dynamics incompletely describe motor cortex activity, paragraph 1;\n    Supplementary Figure 1b\n  quote: Rotational dynamics fit neural activity within the identified plane reasonably well ( R 2\n    = 0.64–0.73). ... rotational dynamics fit neural activity on straight reaches more strongly ( R\n    2 = 0.73–0.88), but fit curved reaches less closely ( R 2 = 0.56–0.70; Supplementary Fig. 1 )\n  statistics:\n  - about: straight against curved jPCA fit\n    test: Wilcoxon signed-rank\n    p: 0.001\n    p_relation: \"<\"\n  criterion: jPCA as in Methods, Explaining variability in jPCA-identified rotations (mean\n    subtraction, soft normalisation constant 5, applied to activity reconstructed from the\n    temporal basis functions); fitted on bins 20 to 40 of the -350 to +850 ms grid, about -160 to\n    +40 ms, and with the codepack's default of 6 PCs (code getRotations.m; jPCA() called with\n    default parameters). The straight and curved fits refit jPCA on the 36 straight and the 36\n    curved conditions alone (code getRotationalProjCompare.m). The R2 is open between (a) the fit\n    of the skew-symmetric matrix in the top plane (summary.R2_Mskew_2D, the first the code\n    stores) and (b) the unconstrained fit in that plane (R2_Mbest_2D). Ranges judged by the rule\n    for ranges (0.576 to 0.803 all, 0.657 to 0.968 straight, 0.504 to 0.77 curved) under one\n    reading. The signed-rank test of Supplementary Figure 1b is not described; its pairing is\n    open, reading per-condition R2 of each condition's projected trajectory, straight against\n    curved conditions paired by target. It is reported, not decisive.\n- id: jpca-variance-explained\n  statement: Activity within the jPCA rotational planes explained only 7 to 12% of the population\n    variance in peri-movement firing rates.\n  source: Results, Rotational dynamics incompletely describe motor cortex activity, paragraph 1;\n    Figure 2c\n  quote: activity within the jPCA-identified rotational planes explained only 7–12% (s.d. <13%\n    across conditions; Supplementary Fig. 1 ) of the total variance in peri-movement firing rates\n  criterion: Per condition, the population variance of the activity reconstructed from the\n    retained jPCA planes (two planes for M1, one for PMd, Methods), as the fraction of total\n    variance (code getRotations.m, which reconstructs soft-normalised, mean-subtracted activity in\n    the planes, un-normalises it and compares it with the activity not mean-subtracted). Mean over\n    conditions judged by the rule for ranges (6.3 to 13.2%); the s.d. across conditions is\n    reported.\n  depends_on:\n  - jpca-fit-r2\n- id: single-lds-variance\n  statement: A single linear dynamical system fitted to all conditions captured on average 46 to\n    66% of the population variance.\n  source: Results, Rotational dynamics incompletely describe motor cortex activity, paragraph 2\n  quote: A single LDS on these data only captured an average of 46–66% of the population variance\n    (s.d. <16%)\n  criterion: Following the code fitSingleLDS.m, as the Methods do not describe this fit. One\n    full-rank matrix M fitted by least squares from each bin to the next over all conditions, from\n    bin 20 (about -150 ms) to the end; each condition simulated forward from its state at bin 20;\n    population variance explained per condition. The comparison window is open between (a)\n    -150 to +850 ms (bins 20 to 121), (b) the whole -350 to +850 ms matrix as the code computes\n    it with the bins before 20 copied from the data. Mean over conditions judged by the rule for\n    ranges (41.4 to 72.6%) under one reading.\n- id: fig2c-condition-lds-variance\n  statement: Activity on each single condition was low-dimensional and approximated by an LDS of\n    5 to 9 dimensions, which explained 71 to 93% of the population variance.\n  source: Results, Rotational dynamics incompletely describe motor cortex activity, paragraph 3;\n    Figure 2c\n  quote: 'Motor cortex activity for each single condition was low-dimensional and could be\n    approximated as an LDS: 5–9 dimensional LDSs explained 71–93% (Fig. 2c ; s.d. <10% across\n    conditions) of the population variance.'\n  criterion: Methods, Fitting dynamics to single conditions. Per condition a discrete-time LDS by\n    reduced-rank regression from -150 to +850 ms, eigenvalue half-lives above 10 s cut to 10 s,\n    simulated forward from the state at -150 ms; dimensionality by cross-validation over two\n    trial partitions, 100 repeats, one k for all conditions of a dataset. The code\n    (crossValidateDimensionalityConditions.m) tests odd k from 1 to 21 and splits trials 3/4 to\n    1/4; the Methods' even split is the main reading and the code's is a variant. Reproduced when\n    every dataset's chosen dimensionality is 5 to 9 and its mean variance explained lies in 63.9\n    to 100% (rule for ranges).\n- id: fig3a-eigenvalue-clusters\n  statement: Eigenvalues of the single-condition LDSs formed distinct clusters, corresponding to\n    rotations at about 0.5, 1.5, 2.5 and 4 Hz on every condition, along with an offset.\n  source: Results, Rotation frequencies are conserved across reaches in motor cortex activity,\n    paragraph 2; Figure 3a\n  quote: These clusters corresponded to the presence of rotations on every condition with\n    frequencies of approximately 0.5, 1.5, 2.5, and 4 Hz, along with an offset in the firing rates.\n  depends_on:\n  - fig2c-condition-lds-variance\n  criterion: Frequencies of the eigenvalues of each condition's LDS (angle of the eigenvalue over\n    2 pi times the 100 Hz sampling rate, as in the code's extractParams.m). Reproduced when, in\n    each dataset, the median frequencies of the complex eigenvalue pairs, sorted by frequency,\n    lie within 10% of 0.5, 1.5, 2.5 and 4 Hz for the pairs present (at least three) and at least\n    one real eigenvalue is present on most conditions.\n- id: fig3c-eigenvalue-distance-auc\n  statement: Eigenvalues differed between conditions only slightly more than expected from\n    estimation noise, with ROC-AUC 0.51 to 0.58 between the between-condition distances and the\n    noise distribution.\n  source: Results, Rotation frequencies are conserved across reaches in motor cortex activity,\n    paragraph 2; Figure 3b, c\n  quote: 'The rotational frequencies (specified by the eigenvalues) were nearly identical between\n    conditions: the variation in eigenvalues between conditions was only slightly larger than the\n    floor due to estimation noise (ROC-AUC = 0.51–0.58; Fig. 3b, c ).'\n  depends_on:\n  - fig2c-condition-lds-variance\n  criterion: Distance between two conditions is the norm of the difference of their\n    frequency-sorted eigenvalue vectors (code eigValDistance.m; the legend of Figure 3b says\n    averaging over corresponding eigenvalues, and the mean of the absolute differences is shown as\n    a variant). The null is open between the two the Methods give, (a) two sets of 20 Poisson\n    trials simulated from each condition's rates, smoothed, averaged and fitted, 500 repeats per\n    condition (Methods, main control); (b) random halves of the real trials, 500 repeats (the\n    Methods' additional control and the code's compareTrialSimilarity.m). AUC folded to at least\n    0.5. Reproduced when, under one reading, every dataset's AUC lies in 0.459 to 0.638.\n- id: suppfig2-eigenvalues-from-kinematics\n  statement: Kinematic parameters predicted the eigenvalues poorly (mean R2 = 0.1, leave-one-out\n    cross-validation), so the small variation in eigenvalues carried little information about the\n    reach.\n  source: Results, Rotation frequencies are conserved across reaches in motor cortex activity,\n    paragraph 2; Supplementary Figure 2e\n  quote: 'kinematic parameters performed poorly as predictors of eigenvalues (mean R 2 = 0.1,\n    leave-one-out cross-validation; Supplementary Fig. 2 )'\n  expected:\n    quantity: mean R2 of eigenvalue components predicted from reach parameters\n    value: 0.1\n    tolerance: 0.05\n  depends_on:\n  - fig2c-condition-lds-variance\n  - fig6e-kinematics-predict-location\n  criterion: Following the code getCorrelationsWithFrequency.m, as the Methods do not describe it.\n    Predictors are the four reach parameters (see fig6e) plus reach duration and a constant;\n    targets are the real and imaginary parts of each eigenvalue; ordinary least squares with\n    leave-one-condition-out; R2 per component as 1 minus residual over total variance, negatives\n    set to 0; mean over components pooled across the four datasets (Supplementary Figure 2e\n    pools them). Reach duration as in fig3i. The tolerance is 0.05, as a mean of 0.1 printed to\n    one figure covers 0.05 to 0.15.\n- id: fig3g-basis-frequencies\n  statement: The cross-validated temporal basis functions contained 3 to 4 rotations at 0.5, 1.5,\n    2.5 and 4 Hz, along with an offset.\n  source: Results, Identifying rotations with varying planes, paragraph 4; Figure 3g;\n    Supplementary Figure 4\n  quote: In agreement with our fits to single conditions, the optimal temporal basis functions\n    contained 3–4 rotations at 0.5, 1.5, 2.5, and 4 Hz, along with an offset (Fig. 3g ; optimal\n    number determined by cross-validation).\n  criterion: TBF as in the shared method, k by cross-validation, the last basis function dropped\n    when unpaired (Methods, Cross-validating the number of temporal basis functions; the visual\n    screen is replaced by checking for a conjugate partner). Frequencies from the de-mixing LDS.\n    Reproduced when every dataset has 3 or 4 rotation pairs plus one real (offset) mode, and each\n    rotation's frequency lies within 10% of one of 0.5, 1.5, 2.5 and 4 Hz, the lowest three always\n    present.\n- id: tbf-variance-explained\n  statement: The shared rotations of the temporal basis factorization explained 90 to 96% of the\n    population variance.\n  source: Results, Identifying rotations with varying planes, paragraph 4\n  quote: These rotations explained 90–96% of the population variance (s.d. <2% across conditions).\n  depends_on:\n  - fig3g-basis-frequencies\n  criterion: Per condition, population variance explained by the condition's loading matrix times\n    the shared basis functions (Methods, Factorizing neural activity using temporal basis\n    functions), mean over conditions, judged by the rule for ranges (81 to 100%). The window is\n    open between (a) -150 to +850 ms, the window of the de-mixed basis, and (b) the whole -350 to\n    +850 ms with the raw SVD basis, as the code's quantifyTBFStats.m computes it.\n- id: tbf-shuffle-control\n  statement: Shuffling time bins within each trial before smoothing lowered the variance explained\n    by the factorization to 35 to 46%, significantly below the real data.\n  source: Results, Identifying rotations with varying planes, paragraph 4; Methods, Control for\n    data smoothing\n  quote: This shuffle significantly lowered the variance explained by this method (35–46%; Wilcoxon\n    rank sum test, p < 0.001).\n  statistics:\n  - test: Wilcoxon rank sum test\n    p: 0.001\n    p_relation: \"<\"\n  depends_on:\n  - tbf-variance-explained\n  criterion: Per trial, 1 ms bins permuted in time before smoothing and averaging (code\n    scrambleTrials.m), then TBF with k matched to the real data and variance explained per\n    condition. The Results name a rank-sum test (and the code uses ranksum); the Methods name a\n    signed-rank test, shown as a variant. Reproduced when every dataset's shuffled mean lies in\n    31.5 to 50.6% and the rank-sum test against the real per-condition values gives p < 0.001\n    with real higher; partially by the rule for ranges.\n- id: fig3h-recoverability\n  statement: Projections of each condition's activity recovered the temporal basis functions\n    almost perfectly (91 to 95% variance explained, chance 63 to 80%), so the factorization found\n    rotations and not a frequency decomposition.\n  source: Results, Identifying rotations with varying planes, paragraph 5; Figure 3h; Methods,\n    Quantifying the recoverability of temporal basis functions\n  quote: The projections from each condition's motor cortex activity recovered the temporal basis\n    functions almost perfectly (91–95% variance explained; s.d. <2.5% across conditions; chance,\n    63–80%; Wilcoxon rank sum test, p < 0.001)\n  statistics:\n  - test: Wilcoxon rank sum test\n    p: 0.001\n    p_relation: \"<\"\n  depends_on:\n  - tbf-shuffle-control\n  criterion: Recoverability per condition is the variance of the basis functions explained by the\n    pseudo-inverse of the condition's loading matrix times its activity (Methods, Eq. 6; code\n    getRecoverability.m). Chance is the recoverability on the time-shuffled data of\n    tbf-shuffle-control (code quantifyTBFStats.m). Reproduced when every dataset's mean lies in\n    81.9 to 100%, its chance mean in 56.7 to 88%, and the rank-sum test gives p < 0.001 with real\n    higher; partially by the rule for ranges.\n- id: fig3i-duration-warping\n  statement: Before warping, rotation fits were unrelated or weakly related to reach duration\n    (M1-N rho = -0.26, p = 0.023; others -0.18 to 0.21, p > 0.067); warping reaches to equal\n    duration induced a negative correlation (rho -0.63 to -0.52, p < 0.001).\n  source: Results, Identifying rotations with varying planes, paragraph 6; Figure 3i; Methods,\n    Control for stereotyped time course of behavior\n  quote: 'Prior to warping, the frequencies of the rotations were unrelated or weakly related to\n    reach duration (M1-N, Pearson''s Rho = −0.26, p = 0.023; other datasets, Pearson''s Rho =\n    −0.18–0.21, p > 0.067). Warping to equalize reach duration induced a negative correlation'\n  statistics:\n  - about: M1-N, unwarped\n    test: Pearson correlation\n    statistic: rho = -0.26\n    p: 0.023\n  - about: other datasets, unwarped\n    test: Pearson correlation\n    p: 0.067\n    p_relation: \">\"\n  - about: warped data\n    test: Pearson correlation\n    p: 0.001\n    p_relation: \"<\"\n  expected:\n    quantity: M1-N unwarped correlation\n    value: -0.26\n    tolerance: 0.026\n  criterion: Methods and code quantifyTBFStats.m. Per condition, the Pearson correlation of the\n    absolute difference of its mean reach duration from the mean over conditions with its\n    recoverability. Reach duration per trial is the time from movement onset to the last bin\n    where hand speed is at least a tenth of its peak (code warpTrials.m); warping is linear to 600\n    ms with post-reach activity truncated at 850 ms after onset (the variant shown in Figure 3i;\n    the 250 ms post-reach warp is shown as a variant), TBF with the original k. Reproduced when the\n    M1-N unwarped rho is within tolerance with p < 0.05, the other three unwarped rho lie in -0.198\n    to 0.231, and all four warped rho lie in -0.693 to -0.468 with p < 0.001; partially when the\n    warped correlations hold and an unwarped value does not.\n- id: suppfig3-model-comparison\n  statement: The model with shared eigenvalues and condition-specific planes (LDR) explained more\n    cross-validated variance than jPCA or condition-specific LDSs.\n  source: Results, Identifying rotations with varying planes, paragraph 4; Supplementary Figure 3\n  quote: Our method also explained greater variance than jPCA or even single-condition LDSs (due\n    to lower overfitting and differences in objective function; Supplementary Fig. 3 ).\n  depends_on:\n  - jpca-variance-explained\n  - fig2c-condition-lds-variance\n  - tbf-variance-explained\n  criterion: The per-condition variance explained of the three models as computed for\n    jpca-variance-explained, fig2c-condition-lds-variance and tbf-variance-explained (code\n    modelComp.m gathers these three). The legend says cross-validated; the cross-validated TBF\n    value is the held-out variance at the chosen k (crossValidateDimensionalityBasisFxns.m) and\n    the in-sample values are a variant. The paper reports no test; reproduced when, in every\n    dataset, the TBF mean exceeds both others.\n- id: fig4b-plane-alignment\n  statement: Same-frequency rotational planes on pairs of conditions were far less aligned than\n    expected from estimation noise (ROC-AUC 0.85 to 0.96).\n  source: Results, Rotational planes differed across reaches, paragraph 1; Figure 4b;\n    Supplementary Figure 4a\n  quote: We found that rotational planes were far less aligned than expected due to estimation\n    noise (ROC-AUC = 0.85–0.96; Wilcoxon signed-rank test, p < 0.001; Fig. 4b and Supplementary\n    Fig. 4a ).\n  statistics:\n  - test: Wilcoxon signed-rank test\n    p: 0.001\n    p_relation: \"<\"\n  depends_on:\n  - fig3g-basis-frequencies\n  criterion: Alignment index as in the shared method for each ordered pair of different conditions\n    and each rotation. Noise is the alignment index between loading matrices fitted by regression\n    on the fixed basis to two random halves of a condition's trials (Methods, Measuring the\n    across-condition alignment of rotations); repeats are open between 36 (Methods) and 200 (code\n    singleFrequencyOverlapControl.m). The paper's AUC is per rotation; the range covers rotations\n    and datasets. Reproduced when every rotation in every dataset has AUC in 0.765 to 1 with\n    observed alignment lower, and the test gives p < 0.001; partially when at least half of the\n    rotations do. The Results name a signed-rank test of unequal-size samples, so the code's\n    rank-sum test decides and the paper's name is recorded.\n- id: fig4c-subspace-excursion-angles\n  statement: Across conditions, each rotation's planes spanned 6 to 20 distinct dimensions with\n    angles above 45 degrees to each other, and more that varied above chance.\n  source: Results, Rotational planes differed across reaches, paragraph 2; Figure 4c;\n    Supplementary Figure 4b\n  quote: Across conditions for each rotational frequency, SEA identified 6–20 distinct dimensions\n    with angles >45° to each other in motor cortex activity, and far more that varied above chance\n  depends_on:\n  - fig4b-plane-alignment\n  criterion: Subspace excursion angles as in the Methods, computed to 25 dimensions (code\n    subspaceExcursionAngles.m called with 25, angles from subspacea.m), the seed and sequence\n    optimised as the code does. Per rotation and dataset, the count of excursion angles above 45\n    degrees. Reproduced when every count lies in 5.4 to 22 (the rule for ranges, over rotations and\n    datasets), and in each dataset the angles exceed the half-split noise angles (code\n    singleFrequencyOverlapControl.m, fraction of noise SEA above the data) for more dimensions than\n    the count above 45 degrees.\n- id: rotation-orientation-dimensionality\n  statement: Rotation orientations required 23 to 40 principal components to capture 80% of their\n    variance, had 7 to 33 dimensions with SNR above 1, and participation ratios of 16.7 to 36.8.\n  source: Results, Rotational planes differed across reaches, paragraph 2; Methods, Estimating the\n    dimensionality of each rotation's orientations\n  quote: Rotation orientations required 23–40 principal components to capture 80% of their total\n    variance, had 7–33 dimensions with an SNR > 1 45 , and had participation ratios 46 of\n    16.7–36.8.\n  depends_on:\n  - fig3g-basis-frequencies\n  criterion: Per rotation, PCA across conditions of the rotation's loading columns (the PCA input\n    is open between (a) the two columns of each condition stacked as observations, (b) the\n    rotation's activity, loading columns times basis functions). PCs to 80% and participation\n    ratio from that PCA; SNR dimensionality by the half-split procedure of the Methods (100 folds,\n    the dimensionality maximising the alignment index between partitions; code\n    crossValidateDimensionalityRotations.m). Each range judged by the rule for ranges, over\n    rotations and datasets (20.7 to 44; 6.3 to 36.3; 15.03 to 40.48), under one reading.\n- id: fig4d-jpca-variance-correlation\n  statement: Variance in the jPCA planes was only moderately correlated with the total rotational\n    variance of a condition (rho 0.39 to 0.46; 66% of jPCA planes correlated at p < 0.05).\n  source: Results, Rotational planes differed across reaches, paragraph 3; Figure 4d\n  quote: 'variance in the jPCA planes was only moderately correlated with the variance in the\n    rotations we identified (Fig. 4d ; Pearson''s Rho = 0.39–0.46, 66% of jPCA planes correlated at\n    p < 0.05)'\n  expected:\n    quantity: share of retained jPCA planes correlated at p < 0.05\n    value: 66\n    tolerance: 6.6\n    unit: percent\n  depends_on:\n  - jpca-fit-r2\n  - tbf-variance-explained\n  criterion: Methods, Explaining variability in jPCA-identified rotations. Per condition, the\n    variance due to the rotational basis functions after the same soft normalisation and mean\n    subtraction as jPCA, against the variance in each retained jPCA plane (six planes in all, two\n    per M1 dataset and one per PMd dataset); Pearson correlation per plane. Reproduced when every\n    plane's rho lies in 0.351 to 0.506 and the share with p < 0.05 is within tolerance (4 of 6\n    planes is 67%); partially when the rho range holds for at least half.\n- id: fig4f-plane-alignment-explains-jpca\n  statement: Conditions without clear rotations in the jPCA planes had rotations misaligned with\n    those planes; the alignment index with the jPCA plane correlated strongly with the variance\n    jPCA captured (rho 0.82 to 0.97).\n  source: Results, Rotational planes differed across reaches, paragraph 3; Figure 4e, f\n  quote: Instead, for conditions that did not exhibit clear rotations in the jPCA planes, the\n    rotations our model discovered were misaligned with the jPCA planes (Fig. 4e, f ; Pearson's Rho\n    = 0.82–0.97 between plane alignment and variance explained by jPCA, p < 0.001).\n  statistics:\n  - test: Pearson correlation\n    p: 0.001\n    p_relation: \"<\"\n  depends_on:\n  - jpca-fit-r2\n  criterion: Per condition, the alignment index of the condition's total rotational activity onto\n    each retained jPCA plane, correlated across conditions with the variance in that plane\n    (Methods; code corrOverlapWithjPCA.m). Reproduced when every plane's rho lies in 0.738 to 1\n    with p < 0.001; partially when at least half do.\n- id: fig5a-frequencies-segregated\n  statement: Different-frequency rotational planes on pairs of conditions were nearly orthogonal,\n    and same-frequency planes were better aligned.\n  source: Results, Different-frequency rotations occupied distinct yet coordinated subspaces,\n    paragraph 1; Figure 5a; Supplementary Figure 5\n  quote: the different-frequency pairs were consistently nearly-orthogonal, and the corresponding\n    rotations were better aligned (Fig. 5a ; Wilcoxon signed-rank test, p < 0.001; Supplementary\n    Fig. 5 )\n  statistics:\n  - test: Wilcoxon signed-rank test\n    p: 0.001\n    p_relation: \"<\"\n  depends_on:\n  - fig4b-plane-alignment\n  criterion: Alignment indices of each rotation on one condition onto the same rotation and onto\n    each other rotation on a different condition (Methods; code\n    quantifyProjectedVarianceDifferentFrequencies.m). The pairing of the signed-rank test is open,\n    reading (a) the same ordered condition pairs, same against different frequency; the code's\n    rank-sum test of the two distributions is reading (b). Reproduced when, under one reading, for\n    every rotation and every other rotation in every dataset, same-frequency alignment is higher\n    with p < 0.001; partially when at least 80% of the comparisons do.\n- id: fig5c-rotations-predict-rotations\n  statement: Each rotation's parameters on a condition predicted 43 to 94% of the variance of a\n    different-frequency rotation, with one model for all conditions, above chance.\n  source: Results, Different-frequency rotations occupied distinct yet coordinated subspaces,\n    paragraph 2; Figure 5c\n  quote: Each rotation predicted an average of 43–94% of the variance in other rotations (s.d.\n    <25%, 6-fold cross-validation), significantly greater than expected by chance (Fig. 5c ;\n    Wilcoxon signed-rank test, p < 0.001).\n  statistics:\n  - test: Wilcoxon signed-rank test\n    p: 0.001\n    p_relation: \"<\"\n  depends_on:\n  - fig3g-basis-frequencies\n  criterion: Methods, Predicting rotations from other rotations or the state space location, with\n    code predictOneComponentFromAnother.m and oneComponentToAnother.m. Six folds over conditions;\n    TBF, loadings and a ridge map (lambda 0.1, with intercept) fitted on 5/6; the predictor's\n    vectorised columns reduced to the singular vectors holding 80% of the summed singular values\n    (code); test loadings by projecting the held-out condition on the training basis; variance of\n    the true rotation explained per condition. Null as in the code, each rotation taken from a\n    random condition. Mean per predictor and predicted pair (off the diagonal), judged by the rule\n    for ranges over pairs and datasets (38.7 to 100%), and every pair above its null at p < 0.001\n    by a signed-rank test (the code's rank-sum test a variant).\n- id: suppfig6a-location-alignment\n  statement: The state space location occupied different dimensions across conditions, less\n    aligned than expected from estimation noise (ROC-AUC 0.88 to 0.95).\n  source: Results, Motor cortex rotations were location-dependent, paragraph 1; Supplementary\n    Figure 6a\n  quote: 'The state space location subspace was multi-dimensional: the dimensions occupied across\n    conditions were less aligned than expected due to estimation noise (ROC-AUC = 0.88–0.95;\n    Wilcoxon signed-rank test, p < 0.001; Supplementary Fig. 6a ).'\n  statistics:\n  - test: Wilcoxon signed-rank test\n    p: 0.001\n    p_relation: \"<\"\n  depends_on:\n  - fig4b-plane-alignment\n  criterion: As fig4b-plane-alignment, with the single offset column in place of a plane (Methods).\n    Reproduced when every dataset's AUC lies in 0.792 to 1 with observed alignment lower and p <\n    0.001.\n- id: suppfig6b-location-dimensionality\n  statement: SEA found 4 to 5 state space location dimensions with angles above 15 degrees; the\n    locations needed 21 to 30 PCs for 80% of their variance, had 5 to 12 dimensions with SNR above\n    1, and participation ratios of 15.1 to 26.4.\n  source: Results, Motor cortex rotations were location-dependent, paragraph 1; Supplementary\n    Figure 6b\n  quote: SEA identified 4–5 state space location dimensions with angles >15° (Supplementary Fig. 6b\n    ). ... The state space location required 21–30 principal components to capture 80% of the total\n    variance, had 5–12 dimensions with an SNR > 1, and had participation ratios of 15.1–26.4.\n  depends_on:\n  - rotation-orientation-dimensionality\n  criterion: As fig4c-subspace-excursion-angles and rotation-orientation-dimensionality, on the\n    offset column. Rule for ranges (3.6 to 5.5 SEA dimensions above 15 degrees; 18.9 to 33 PCs; 4.5\n    to 13.2 SNR dimensions; participation ratio 13.59 to 29.04), each judged separately;\n    reproduced when all four hold.\n- id: suppfig6c-location-distinct-from-rotations\n  statement: State space location dimensions were distinct from those of the rotations.\n  source: Results, Motor cortex rotations were location-dependent, paragraph 1; Supplementary\n    Figure 6c\n  quote: Moreover, the state space location dimensions were distinct from those of rotations (same\n    analysis as Fig. 5a ; Wilcoxon signed-rank test, p < 0.001; Supplementary Fig. 6c ).\n  statistics:\n  - test: Wilcoxon signed-rank test\n    p: 0.001\n    p_relation: \"<\"\n  depends_on:\n  - fig5a-frequencies-segregated\n  criterion: As fig5a-frequencies-segregated, location against location compared with location\n    against each rotation. Reproduced when location-to-location alignment is higher with p < 0.001\n    in every dataset.\n- id: fig6b-location-predicts-rotations\n  statement: The state space location linearly predicted the rotations' parameters, explaining on\n    average 67 to 80% of the population variance, above chance.\n  source: Results, Motor cortex rotations were location-dependent, paragraph 2; Figure 6b\n  quote: The state space locations predicted an average of 67–80% of the total population variance\n    (Fig. 6b ; s.d. <15%, 6-fold cross-validation), significantly greater than expected by chance\n    (Wilcoxon signed-rank test, p < 0.001).\n  statistics:\n  - test: Wilcoxon signed-rank test\n    p: 0.001\n    p_relation: \"<\"\n  depends_on:\n  - fig3g-basis-frequencies\n  criterion: Methods, Predicting rotations from other rotations or the state space location. The\n    offset column predicts the vectorised remaining columns by ridge regression (lambda 0.1), 6\n    folds over conditions; the observed offset column joined to the prediction, times the basis\n    functions, gives the predicted activity; population variance explained per condition. Null,\n    offsets and rotations shuffled between conditions, signed-rank test. The code\n    (offsetToRotations.m) uses 2 folds, lambda 0.01 and an SVD reduction of the predictor to 90% of\n    the summed singular values with an intercept; it is shown as a variant. Reproduced when every\n    dataset's mean lies in 60.3 to 88% and p < 0.001 against the null.\n- id: fig6c-location-tracks-direction\n  statement: In a PCA of the state space locations across conditions, location related to the\n    overall reach direction, from starting point to target, in a continuous manner.\n  source: Results, Reach kinematics correlate with state space location, paragraph 1; Figure 6c\n  quote: Qualitatively, state space location related to the overall direction from starting point\n    to target in a continuous manner (Fig. 6c ).\n  depends_on:\n  - fig3g-basis-frequencies\n  criterion: The paper reports this qualitatively and gives no measure. PCA of the offset columns\n    across the 72 conditions; conditions plotted on PCs 1 and 2 coloured by target angle, as in\n    Figure 6c. The measure is open; the reading named here is the circular correlation between\n    target angle and the angle of each condition in the PC 1 to 2 plane, with neighbours in target\n    angle neighbours in the plane. Reproduced when that correlation is positive with p < 0.05 in\n    every dataset (or all four after a sign flip of a PC); the plots are shown.\n- id: fig6e-kinematics-predict-location\n  statement: Four reach parameters linearly predicted 37 to 71% of the variance in state space\n    location, and kernel regression 69 to 81%, both above chance.\n  source: Results, Reach kinematics correlate with state space location, paragraph 1; Figure 6d, e\n  quote: Reach parameters linearly predicted 37–71% of the variance in state space location (6-fold\n    cross-validation), greater than expected by chance (shuffle, p < 0.001). Allowing nonlinearities\n    via kernel regression raised the variance explained to 69–81% of the variance in state space\n    (6-fold cross-validation; shuffle, p < 0.001).\n  statistics:\n  - about: linear regression against shuffle\n    test: shuffle\n    p: 0.001\n    p_relation: \"<\"\n  - about: kernel regression against shuffle\n    test: shuffle\n    p: 0.001\n    p_relation: \"<\"\n  depends_on:\n  - fig3g-basis-frequencies\n  criterion: Reach parameters per condition are the least-squares coefficients of hand x and y\n    position over -350 to +850 ms on two kinematic basis functions (Methods, Extracting kinematic\n    basis functions; code predictDataUsingTBFandKinCondStructure.m). The basis functions\n    (kinFuncEval) are not in the code; readings are (a) the top two velocity singular vectors of\n    an SVD over all conditions of the datasets, integrated to position; (b) their skew-normal and\n    skew-normal-derivative fits (the Methods say the results were essentially identical). The\n    code for this regression is not published; following LDR encoding, ridge regression (lambda\n    0.1) with intercept from the four parameters to the offset column, 6 folds over conditions,\n    variance explained in the offset column over held-out conditions. The kernel is open between\n    (a) the Ornstein-Uhlenbeck kernel, length scale 10^3, of the LDR encoder and (b) the Gaussian\n    kernel, length scale 400, lambda 0.1, of the rotation predictions (Methods). Shuffle, reach\n    parameters permuted across conditions, 1000 permutations. Reproduced when, under one reading,\n    every dataset's linear value lies in 33.3 to 78.1% and kernel value in 62.1 to 89.1%, both\n    above all permutations.\n- id: fig7c-ldr-encoding\n  statement: Predicting each condition's loading matrix from four reach parameters and multiplying\n    by the shared basis functions explained 60 to 78% of the population variance with a linear\n    model and 71 to 87% with kernel regression, above chance.\n  source: Results, Reach kinematics correlate with the dynamics of motor cortex activity, paragraphs\n    3 and 4; Figure 7b, c\n  quote: 'This linear LDR-encoding model explained most of the population variance: 60–78% (s.d.\n    <22%, 6-fold cross-validation), greater than expected by chance (Wilcoxon signed-rank test, p <\n    0.001). ... This nonlinear LDR encoding model explained 71–87% of the population variance (s.d.\n    <17%, 6-fold cross-validation)'\n  statistics:\n  - about: linear LDR encoding against shuffle\n    test: Wilcoxon signed-rank test\n    p: 0.001\n    p_relation: \"<\"\n  - about: nonlinear LDR encoding against shuffle and memorization\n    test: Wilcoxon signed-rank test\n    p: 0.01\n    p_relation: \"<\"\n  depends_on:\n  - fig6e-kinematics-predict-location\n  criterion: Methods, LDR encoding, and code kinToTBF.m. Reach parameters as in fig6e (both\n    readings); ridge regression (lambda 0.1) with intercept to the vectorised loading matrix; 6\n    folds over conditions with TBF and loadings refitted on 5/6; kernel regression with the\n    Ornstein-Uhlenbeck kernel, length scale 10^3, no penalty (code); population variance explained\n    per held-out condition. Null, neural activity permuted across conditions, signed-rank test.\n    Reproduced when, under one kinematic reading, every dataset's linear mean lies in 54 to 85.8%\n    and nonlinear mean in 63.9 to 95.7%, with p < 0.001 and p < 0.01 against the nulls.\n- id: suppfig7a-not-memorization\n  statement: With targets held out by sextant, kernel-regression LDR encoding outperformed\n    nearest-neighbour regression, so it was not memorization of the training set.\n  source: Supplementary Figure 7a; Methods, Controlling for nonlinear LDR encoding\n  quote: The higher performance of kernel regression indicates that nonlinear LDR encoding was not\n    merely memorization of the training set.\n  depends_on:\n  - fig7c-ldr-encoding\n  criterion: Conditions divided into six sextants of target angle; nonlinear LDR encoding and the\n    same model with nearest-neighbour regression trained on five sextants and tested on the sixth;\n    per-condition variance explained compared by a Wilcoxon signed-rank test (Methods; code\n    predictDataUsingTBFandKinNN.m). Reproduced when kernel regression is higher with p < 0.01 in\n    every dataset.\n- id: fig7c-standard-encoding-worse\n  statement: Standard instantaneous encoding models (linear multi-parameter, kernel regression on\n    position, kernel regression on velocity) were substantially outperformed by both linear and\n    nonlinear LDR encoding.\n  source: Results, Reach kinematics correlate with the dynamics of motor cortex activity, paragraph\n    5; Figure 7b, c; Methods, Comparing the LDR encoding with standard instantaneous encoding models\n  quote: We quantified the performance of various linear and nonlinear standard encoding models and\n    found they were substantially outperformed by both linear and nonlinear LDR encoding models (Fig.\n    7b, c ; Wilcoxon signed-rank test, p < 0.001).\n  statistics:\n  - test: Wilcoxon signed-rank test\n    p: 0.001\n    p_relation: \"<\"\n  depends_on:\n  - fig7c-ldr-encoding\n  criterion: The three standard models of the Methods with a 100 ms causal lag, ridge lambda 0.1\n    for the linear model, Ornstein-Uhlenbeck kernels with length scales 10^12 (position) and 10^11\n    (velocity); per-condition variance explained, cross-validated over the same 6 folds of\n    conditions (the code's linearControls.m and nonlinearControls.m decide where the Methods are\n    silent). Reproduced when both LDR models exceed each standard model with p < 0.001 in every\n    dataset; partially when they do in at least half of the 24 comparisons.\n- id: fig7f-ldr-decoding\n  statement: A linear LDR-based decoder applied to single-trial spiking explained on average 84 to\n    92% of the variance in hand position over time.\n  source: Results, LDR allows linear decoding of single-trial kinematics, paragraph 2; Figure 7d-f;\n    Methods, LDR-based decoding\n  quote: Despite using only linear operations on spiking activity, this LDR-based decoder on average\n    explained 84–92% of the variance in the hand's position over time (s.d. <15% across trials;\n    2-fold cross-validation across conditions).\n  depends_on:\n  - fig6e-kinematics-predict-location\n  criterion: Two folds over conditions (Results and code kinFromTBFSingleTrial.m; the Methods say\n    6-fold but describe halves). On the training half, TBF on trial averages (raw SVD basis, code\n    predictKinUsingTBFandDataCondStructureSingletrial.m) and a ridge map with intercept from\n    vectorised loadings to the four reach parameters; the penalty is not in the Methods and is 10\n    in the code. Single-trial loadings of the held-out half are 1 ms spike counts summed in 10 ms\n    bins, scaled to spikes/s, times the pseudo-inverse of the basis; predicted parameters times the\n    kinematic basis functions give hand position; variance explained per trial (code\n    getVarExplainedKinematics.m, negatives set to 0). Kinematic readings as in fig6e. Reproduced\n    when, under one reading, every dataset's mean over trials lies in 75.6 to 100% and exceeds a\n    condition-shuffled null with p < 0.001.\n- id: fig7f-decoder-beats-standard\n  statement: The LDR-based decoder outperformed every other offline decoder tested, including GPFA\n    denoising followed by nonlinear decoders.\n  source: Results, LDR allows linear decoding of single-trial kinematics, paragraph 2; Figure 7f\n    legend; Methods, Comparing LDR-based decoding to instantaneous decoding methods\n  quote: This decoder outperformed every other standard offline decoder we tested, including\n    combining acausal de-noising methods such as Gaussian Process Factor Analysis 45 with nonlinear\n    decoders (Fig. 7d–f ; Wilcoxon signed-rank test, p < 0.001 vs. every other tested decoder for\n    all datasets).\n  statistics:\n  - test: two-sided Wilcoxon signed-rank test\n    p: 0.001\n    p_relation: \"<\"\n    n: 1469 trials for monkey J, 2014 trials for monkey N\n  depends_on:\n  - fig7f-ldr-decoding\n  criterion: The comparison decoders of the Methods, 100 ms lag; linear (ridge lambda 1) and\n    Ornstein-Uhlenbeck kernel regression (length scale 10^2, L2 0.1) on spikes smoothed with 20 or\n    100 ms Gaussians, trained on single trials or on trial averages, and on GPFA trajectories. GPFA\n    latent dimensionality and bin size are not given and not in the code; readings are 8 and 15\n    latents, 20 ms bins. Per-trial variance explained of position compared by two-sided signed-rank\n    tests on the same trials. Reproduced when LDR decoding is higher with p < 0.001 against every\n    decoder in every dataset; partially when it is against all but the GPFA decoders.\n- id: suppfig8-no-output-potent-dependence\n  statement: Removing dimensions that encoded hand position, hand velocity and muscle activity\n    produced no substantial degradation in LDR decoding.\n  source: Results, LDR allows linear decoding of single-trial kinematics, paragraph 3;\n    Supplementary Figure 8\n  quote: Identifying and removing dimensions that encoded hand position, hand velocity, and muscle\n    activity produced no substantial degradation in decoding quality (Supplementary Fig. 8 ;\n    Wilcoxon signed-rank test, p = 0.04–0.96).\n  statistics:\n  - test: Wilcoxon signed-rank test\n    p: 0.04\n    p_relation: \">\"\n  depends_on:\n  - fig7f-ldr-decoding\n  criterion: A claim of absence. Output-potent dimensions as in the code removePotent.m (the\n    Methods do not describe them), the row space of least-squares maps from activity to hand\n    position and velocity and to EMG, projected out of each condition's activity before decoding\n    (code kinFromTBFNoPotent.m, ridge 1, 2 folds). Variance explained per condition with and without\n    the potent dimensions, two-sided signed-rank test. The paper reports p from 0.04 to 0.96 and\n    calls none a substantial degradation, so no fixed threshold applies; reproduced when every\n    dataset's p is at least 0.036 (the lowest reported, less 10%), not reproduced otherwise. The\n    mean drop is reported either way. If the dataset holds no EMG, the kinematic dimensions alone\n    are removed and the outcome rests on that.\n- id: trial-curvature-decoding\n  statement: The LDR decoder followed trial-by-trial variation in reach curvature within a\n    condition (rho 0.16 to 0.41).\n  source: Results, LDR allows linear decoding of single-trial kinematics, paragraph 4; Methods,\n    Quantifying the trial-to-trial fidelity of decoding within condition\n  quote: Using an LDR-based decoder, however, we were able to decode trial-by-trial variations in\n    reach curvature (Pearson's rho, 0.16–0.41; p < 0.001), indicating that our model decoded fine\n    variations in movement.\n  statistics:\n  - test: Pearson correlation\n    p: 0.001\n    p_relation: \"<\"\n  depends_on:\n  - fig7f-ldr-decoding\n  criterion: The third and fourth reach parameters (x and y curvature) of each decoded trial and of\n    the trial's own hand path, each minus its condition mean (code studyAroundMeanParams.m);\n    Pearson correlation over all held-out trials of a dataset, per parameter. Reproduced when the\n    eight correlations (two parameters, four datasets) lie in 0.144 to 0.451 with p < 0.001 (rule\n    for ranges over the eight).\n"
}
```

```
File created successfully at: claims/sabatini-2024.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/sabatini-2024.yaml paper/10.1038-s41467-024-51308-7.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -e "—" -e "rather" claims/sabatini-2024.yaml; python3 - <<'E'
import yaml
d=yaml.safe_load(open('claims/sabatini-2024.yaml'))
c=d['claims']
print(len(c), sum('quote' in x for x in c), sum('statistics' in x for x in c), sum('criterion' in x for x in c), sum('expected' in x for x in c))
for x in c:
    for k in ('statement','criterion'):
        if ': ' in x.get(k,''): print(x['id'],k)
E
```

```
34 34 17 34 4
```

**Agent**

I wrote `claims/sabatini-2024.yaml`, and the quote checker passes it: 34 claims, 34 quotes, 21 statistical values, 0 problems. Nothing is committed.

**Text read**
- **Paper:** the version of record (Nat. Commun. 15:7007), full text from PMC11325044, including the Methods, figure legends and the data and code availability statements.
- **Supplement:** the extracted text of 41467_2024_51308_MOESM1_ESM.pdf (Supplementary Figures 1 to 8 and the basis-function derivation). I didn't need to open the PDF itself.
- **Code:** github.com/kaufmanlab/LDR-public at commit b65f28d.

**Counts**
- 34 claims, all with quotes and none `inferred`.
- 17 have `statistics`, 4 have `expected`, and all 34 have a `criterion`.
- Most numbers are ranges over the four datasets (M1-J, PMd-J, M1-N, PMd-N). One rule in the opening comment covers them: each dataset's value must fall inside the range widened by 10% of each bound.

**Details the paper leaves open, and the readings named**
- **Which 72 of the 108 conditions:** the code drops every third condition of a file order that isn't public. Readings: (a) condition number a multiple of 3; (b) distractor repeats identified from the maze geometry.
- **Trial selection:** (a) all successful trials; (b) delay above 400 ms. Both are compared against the paper's 1469 and 2014 trials.
- **Kinematic basis functions:** the function that builds them (`kinFuncEval`) isn't in the repo. Readings: (a) the raw velocity singular vectors integrated to position; (b) their skew-normal fits.
- **jPCA R2:** R2_Mskew_2D or R2_Mbest_2D. The pairing for the straight-against-curved test is also open.
- **Comparison windows for variance explained:** -150 to +850 ms, or the code's full -350 to +850 ms.
- **Eigenvalue noise null:** Poisson resampling (the Methods' main control) or trial half-splits (their second control, and what the code does).
- **Alignment noise repeats:** 36 (Methods) or 200 (code).
- **Tests named differently in the Results, Methods and code** (rank-sum against signed-rank): the Results' or Methods' test decides and the code's is a variant. The pairing for Fig. 5a is open.
- **Fig. 6b:** the Methods say 6 folds and lambda 0.1; the code uses 2 folds, lambda 0.01 and an SVD-reduced predictor. The code's version is a variant.
- **Fig. 6e location-from-kinematics regression:** there's no code for it. The kernel is either the Ornstein-Uhlenbeck kernel with length scale 10^3 or the Gaussian kernel with length scale 400.
- **Fig. 6c (location follows reach direction):** the paper states this only qualitatively. I named a circular correlation as the reading.
- **Decoder:** the Methods say "6-fold" but describe halves; the Results and code use 2 folds. The ridge penalty appears only in the code (10). GPFA latent count and bin size are given nowhere; I named 8 or 15 latents with 20 ms bins.
- **Rotation dimensionality:** what goes into the PCA is open (the loading columns, or the rotation's activity).
- **Supp. Fig. 8 absence claim:** the paper reports p = 0.04 to 0.96 and calls none of it a substantial drop, so it sets no threshold. The claim holds when every p is at least 0.036.

**Missing from the paper and its code**
- **Preprocessed data:** the code loads `.mat` files that aren't public; the paper says "code-compatible data" are available on request.
- **Code pieces:** `kinFuncEval`, GPFA, the location regression and the Poisson eigenvalue null aren't in the repo.
- **EMG:** Supp. Fig. 8 needs EMG to find the muscle-related dimensions, and I don't know whether the dandiset holds it. If it doesn't, only the hand dimensions are removed and the claim's outcome rests on that.
- **Output-potent dimensions:** the Methods don't say how they are found; only the code (`removePotent.m`) does.

## End of run

35 turns, 6 minutes, $2.63 at API prices, result: success.
