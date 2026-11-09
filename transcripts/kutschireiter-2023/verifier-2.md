# 000289 · verifier-2 · run 40983955184

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null | head; cat round-1-report.md
```

```
total 236
drwxr-xr-x 6 runner runner    4096 Oct 30 01:18 .
drwxr-xr-x 7 runner runner    4096 Oct 30 01:18 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 30 01:07 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 30 01:07 .bashrc
drwxr-xr-x 5 runner runner    4096 Oct 30 01:18 .claude
-rw-r--r-- 1 runner runner       0 Oct 30 01:18 .env
-rw-r--r-- 1 runner runner       0 Oct 30 01:18 .env.development
-rw-r--r-- 1 runner runner       0 Oct 30 01:18 .env.development.local
-rw-r--r-- 1 runner runner       0 Oct 30 01:18 .env.local
-rw-r--r-- 1 runner runner       0 Oct 30 01:18 .env.production
-rw-r--r-- 1 runner runner       0 Oct 30 01:18 .env.production.local
-rw-r--r-- 1 runner runner       0 Oct 30 01:18 .env.test
-rw-r--r-- 1 runner runner       0 Oct 30 01:18 .env.test.local
drwx------ 2 runner runner    4096 Oct 30 01:18 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 30 01:07 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 30 01:07 .github
-rw-r--r-- 1 runner runner       0 Oct 30 01:18 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 30 01:07 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 30 01:07 .mcp.json
[... 73 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; echo ======; cat 000289-kutschireiter-2023-01.yaml
```

```
<persisted-output>
Output too large (31.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/9a6c3ac9-126b-4529-bc65-ce4fb3e541db/tool-results/b0jjlb1qo.txt

Preview (first 2KB):
# Kutschireiter, Basnak, Wilson & Drugowitsch (2023) with dandiset 000289

Tests the findings of [Kutschireiter et al. (2023)](https://doi.org/10.1073/pnas.2210622120),
"Bayesian inference in ring attractor networks", a theory paper. The dandiset it is linked to,
[DANDI:000289](https://dandiarchive.org/dandiset/000289/0.240801.1040), holds two-photon imaging of
EPG neurons from a separate study of the same lab (Basnak et al.), which this paper does not analyse.

- Twelve claims are simulation or connectome results. They are tested on the paper's released code
  and processed outputs ([Zenodo 7615975](https://doi.org/10.5281/zenodo.7615975)) and on the public
  hemibrain v1.2 connectome export, not on the dandiset.
- One claim, the Discussion's prediction that bump amplitude is higher with a reliable cue, is
  tested on the dandiset's cue-contrast experiment (15 flies, visual cue at zero, low and high
  contrast).

| Claim | Outcome |
|---|---|
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md
```

```
# Kutschireiter, Basnak, Wilson & Drugowitsch (2023) with dandiset 000289

Tests the findings of [Kutschireiter et al. (2023)](https://doi.org/10.1073/pnas.2210622120),
"Bayesian inference in ring attractor networks", a theory paper. The dandiset it is linked to,
[DANDI:000289](https://dandiarchive.org/dandiset/000289/0.240801.1040), holds two-photon imaging of
EPG neurons from a separate study of the same lab (Basnak et al.), which this paper does not analyse.

- Twelve claims are simulation or connectome results. They are tested on the paper's released code
  and processed outputs ([Zenodo 7615975](https://doi.org/10.5281/zenodo.7615975)) and on the public
  hemibrain v1.2 connectome export, not on the dandiset.
- One claim, the Discussion's prediction that bump amplitude is higher with a reliable cue, is
  tested on the dandiset's cue-contrast experiment (15 flies, visual cue at zero, low and high
  contrast).

| Claim | Outcome |
|---|---|
| A conflicting HD observation lowers the circKF's certainty, a confirming one raises it | Reproduced |
| An 80-neuron Bayesian ring attractor tracks the circKF, and its amplitude decays in darkness | Reproduced |
| The attractor matches the circKF's accuracy for reliable cues, not for unreliable ones | Reproduced |
| The Bayesian attractor beats the optimized conventional one at every reliability | Reproduced |
[... 22 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "000289-kutschireiter-2023-01.yaml"
}
```

```
1	schema_version: 2
2	id: 000289-kutschireiter-2023-01
3	dataset:
4	  archive: dandi
5	  id: "000289"
6	  version: 0.240801.1040
7	  doi: 10.48324/dandi.000289/0.240801.1040
8	paper: doi:10.1073/pnas.2210622120
9	date: 2026-10-29
10	entry: 000289-kutschireiter-2023
11	provenance:
12	  kind: agent
13	  accountable:
14	    name: CatalystNeuro
15	  agent:
16	    harness: Claude Code
17	    model: claude-opus-5-5
18	    protocol: pilot-12
19	  runner:
20	    platform: GitHub Actions
[... 454 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF' > $TMPDIR/nb.txt
import json
nb=json.load(open('reproduce_kutschireiter_2023.ipynb'))
for i,c in enumerate(nb['cells']):
    print(f"\n######## CELL {i} [{c['cell_type']}]")
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--- OUT:'); print(''.join(o['text']))
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--- OUT data:'); print(''.join(d['text/plain'])[:3000])
        elif o.get('output_type')=='error': print('--- ERROR', o.get('ename'), o.get('evalue'))
EOF
wc -l $TMPDIR/nb.txt; grep -c "" 10.1073-pnas.2210622120.yaml
```

```
1428 /tmp/claude-1001/nb.txt
416
```

**Agent calls Read**

```json
{
 "file_path": "10.1073-pnas.2210622120.yaml"
}
```

```
1	# Claims for Kutschireiter, Basnak, Wilson & Drugowitsch (2023), "Bayesian inference in ring
2	# attractor networks", PNAS 120, e2210622120, on dandiset 000289.
3	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
4	# protocol pilot-10 as stated in docs/protocol.md.
5	#
6	# Text read: the version of record as served by Europe PMC (PMC9992764, CC BY-NC-ND), main text,
7	# figure legends and Materials and Methods, with the SI Appendix (Appendix 01, PDF, extracted to
8	# text in the same file): SI sections 1 to 6 and Figs. S1 to S5. The bioRxiv preprint version 1
9	# (10.1101/2021.12.17.473253v1) is also under paper/; it was not used for the claims.
10	#
11	# Code read: Zenodo doi:10.5281/zenodo.7615975, "DrugowitschLab/BayesianRingAttractor: Code as used
12	# in 2023 PNAS paper" v1.0 (GitHub DrugowitschLab/BayesianRingAttractor, tag v1.0, commit a9db6f9),
13	# the deposit the Data Availability statement names. It holds the filters and the
14	# single-population network (circularFiltering.py: generateData, vM_Projection_Run for the circKF,
15	# vM_Projection_quad_Run for its quadratic approximation, no_uncertainty_filter_Run for the
16	# conventional (fixed kappa*) attractor, RNN_filter_Run, PF_run), the Drosophila-like network
17	# (network_filter.py), the scan scripts (performance_scan_figure2i, 3d, 3f, 4g, S2), one notebook
18	# per figure, and the processed scan outputs the figures are drawn from (data_processed/
19	# figure2i.npz, figure3d.npz, figure3f/sigma=*.npz, figure4g.npz, figureS2.npz,
20	# vonMises_q_stats.npz). data_raw/ is empty. The code holds no imaging analysis and no
[... 397 more lines not kept]
```

**Agent**

Claims file and attempt record both list 13 claims and 13 outcomes. Next I'm reading the notebook's outputs.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "limit": 500
}
```

```
1	
2	######## CELL 0 [markdown]
3	# Testing Kutschireiter et al. (2023) with dandiset 000289
4	
5	Paper. Kutschireiter A, Basnak MA, Wilson RI, Drugowitsch J (2023). Bayesian inference in ring
6	attractor networks. *PNAS* 120, e2210622120.
7	[doi:10.1073/pnas.2210622120](https://doi.org/10.1073/pnas.2210622120). The claims file was written
8	from the version of record (Europe PMC, PMC9992764) with its SI Appendix.
9	
10	Dandiset. [DANDI:000289](https://dandiarchive.org/dandiset/000289/0.240801.1040), version
11	0.240801.1040, "Two-photon calcium imaging of EPG cells in Drosophila Melanogaster presented with
12	cues of varying reliability" (Basnak and Wilson). The paper cites no dandiset version. This is the
13	only published version and the most recent; the draft has the same 221 assets and size, so the
14	published version is pinned.
15	
16	What the dandiset holds, and what the paper uses. The paper is a theory paper: every result is
17	a simulation, apart from a connectome comparison and one prediction. The dandiset holds two-photon
18	imaging of EPG neurons in the protocerebral bridge, with the cue position and trial tables, from a
19	separate study (Basnak et al., "Uncertainty and learning in a biological ring attractor", named in
20	the dandiset's description). So, as the claims file sets out:
[... 480 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 500,
 "limit": 450
}
```

```
500	print(pd.DataFrame(f2h).T.to_string())
501	--- OUT:
502	   net_vs_kf    kf_err   net_err     r_cue amp_dark_start amp_dark_end kf_dark_start kf_dark_end      amp_range     a     b decay
503	15  0.016266  0.483045  0.487024  0.993624       7.214148     1.220141      7.270836    0.881076  1.22 to 10.37  True  True  True
504	10   0.02131  0.490626  0.488095   0.99313         5.8882     1.211796      5.955798     0.86244  0.55 to 10.00  True  True  True
505	
506	
507	######## CELL 17 [markdown]
508	**Result: reproduced.** Under both cue strengths the network's position differs from the circKF's by
509	a mean of 0.016 to 0.021 rad, against a circKF error to the true HD of 0.48 to 0.49 rad. Bump
510	amplitude and circKF certainty correlate at r = 0.99 over the cue periods. In darkness the amplitude
511	falls from 7.2 (rate 15) or 5.9 (rate 10) to 1.22 or 1.21, near the baseline of 1.
512	
513	######## CELL 18 [markdown]
514	## fig2i-accuracy-and-certainty-vs-reliability
515	
516	> The Bayesian ring attractor tracks HD with the same accuracy as the circular Kalman filter when HD
517	> observations are reliable and with slightly lower accuracy when they are unreliable; in the
518	> unreliable regime its certainty stays near its baseline and overestimates the filter's certainty.
519	
[... 430 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; ls -la; grep -n -i "S10[5-9]\|S11[0-9]\|S12[0-9]\|positive drift\|neural noise" 10.1073-pnas.2210622120.txt | head -60
```

```
<persisted-output>
Output too large (78.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/9a6c3ac9-126b-4529-bc65-ce4fb3e541db/tool-results/b0a7i5esg.txt

Preview (first 2KB):
total 1580
drwxr-xr-x 2 runner runner    4096 Oct 30 01:18 .
drwxr-xr-x 6 runner runner    4096 Oct 30 01:19 ..
-rw-r--r-- 1 runner runner 1319580 Oct 30 01:18 10.1073-pnas.2210622120.supp.pdf
-rw-r--r-- 1 runner runner  196214 Oct 30 01:18 10.1073-pnas.2210622120.txt
-rw-r--r-- 1 runner runner   89965 Oct 30 01:18 10.1101-2021.12.17.473253.txt
8:02115 1 To whom correspondence may be addressed. Email: [removed: an e-mail address] or [removed: an e-mail address] . Edited by Terrence Sejnowski, Salk Institute for Biological Studies, La Jolla, CA; received June 20, 2022; accepted January 12, 2023 22 2 2023 120 9 e2210622120 e2210622120 22 8 2023 Copyright © 2023 the Author(s). Published by PNAS. This article is distributed under Creative Commons Attribution-NonCommercial-NoDerivatives License 4.0 (CC BY-NC-ND) . Significance Data from human subjects as well as animals show that working memories are associated with a sense of uncertainty. Indeed, a sense of uncertainty is what allows an observer to properly weigh new evidence against their current memory. However, we do not understand how the brain tracks uncertainty. Here, we describe a simple and biologically plausible network model that can track the uncertainty associated with working memory. The representation of uncertainty in this model improves the accuracy of its working memory, as compared to conventional models, because it assigns proper weight to new conflicting evidence. Our model provides an interpretation of observed fluctuations in brain activity, and it makes testable predictions. Keywords: working memory, ring attractor networks, head direction neurons, Bayesian inference, Kalman filter Abstract Working memories are thought to be held in attractor networks in the brain. These attractors sho
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -o -i ".\{300\}positive drift.\{300\}" 10.1073-pnas.2210622120.txt | head; echo ====; grep -o "Neural noise.\{0,40\}" 10.1073-pnas.2210622120.txt | head; grep -c "" 10.1073-pnas.2210622120.txt
```

```
nty κ t ( SI Appendix ). The derivations revealed that, irrespective of the form of the neural noise (additive, multiplicative, etc.), this noise has two effects. First, it causes an unbiased random diffusion of μ t and, thus, an increasingly imprecise memory of the HD estimate. Second, it causes a positive drift and random diffusion of κ t , which, if the drift is not accounted for, results in an overestimation of one’s certainty and thus overconfidence in the HD estimate. These results mirror previous work that has shown a diffusion of μ t in ring attractors close to the attractor state ( 41 ). We here sh
n our simulations in Fig. 3 , we explored network dynamics with a range of κ * and β values by adjusting network parameters accordingly. Assessing the Impact of Neural Noise on Inference Accuracy. In SI Appendix , we show that neural noise results in an unbiased diffusion of μ t and a diffusion and positive drift of κ t . We assessed the impact of this noise on inference accuracy by simulating a network with N = 64 neurons and κ * and β tuned to maximize noise-free inference accuracy (“Best network model” in Fig. 3 D ) and by adding Gaussian zero-mean white noise with variance σ n n 2 δ t in each time step 
====
Neural noise models
Neural noise models. To get a better understanding o
Neural noise changes the optimal fixed point amplitu
3519
```

**Agent calls Bash**

```bash
cd paper; grep -n "Neural noise models\|Neural noise changes" 10.1073-pnas.2210622120.txt;
```

```
595:Neural noise models
2891:B.3. Neural noise models. To get a better understanding of the resulting μ and κ dynamics, we will now consider different noise
3393:Fig. S4. Neural noise changes the optimal fixed point amplitude and decay speed. We simulated a network of N = 64 neurons with different levels of additive Gaussian noise
```

**Agent calls Bash**

```bash
cd paper; sed -n 2800,2990p 10.1073-pnas.2210622120.txt
```

```
2Tr �
GT HxμG�
dt + (∇xμ)T GdW
=
4
κ4N 2
��
c2T h2 −s2T h2�
x1x2 + cT diag �
h2�
s �
x2
2 −x2
1
��
dt
+
2
κ2N
√
[... 171 more lines not kept]
```

**Agent**

Notebook figures so far match the record. Checking how the "inhibition held" diagnostic is implemented in `bra.py`.

**Agent calls Bash**

```bash
cd  grep -n "def rnn_batch" -A60 bra.py; grep -n "def RNN_filter_Run" -A5 bra.py | head
```

```
181:def rnn_batch(rng, runs, T, N, sigma_N, w_even, w_quad, tau=1.0, kappa_0=1.0, phi_0=0.0, dt=0.01,
182-              noise=None, inh_fixed=None, traces=None):
183-    """RNN_filter_Run (circularFiltering.py) for `runs` independent runs at once, with no angular
184-    velocity input (w_odd = 0, dy = 0), no HD input (I_ext = 0) and stoch_corr = 0 (claims file).
185-    Same update, term by term: decay, even recurrence (2/N w_even cos), quadratic inhibition
186-    (pi/N sum of rectified rates), additive noise sigma_N sqrt(dt) N(0,1). `noise` may pass the
187-    standard normal draws (steps x runs x N) to reproduce a given run.
188-
189-    Diagnostics for the noise claim (not in RNN_filter_Run): `inh_fixed`, if given, replaces the
190-    global inhibition w_quad pi/N sum max(r, 0) by that constant, so that the noise acts only
191-    through the linear terms, as in the SI derivation (section 5, Eqs. S107 to S109, where the
192-    noise is one more input and the other dynamics are unchanged). `traces`, a dict, receives the
193-    run-mean global inhibition and zero mode (population mean rate) at every step."""
194-    steps = int(T / dt)
195-    phi_r = np.linspace(-np.pi, np.pi - 2 * np.pi / N, N)
196-    W = 2 / N * w_even * np.cos(phi_r[:, None] - phi_r[None, :])
197-    A = np.array([np.cos(phi_r), np.sin(phi_r)])
198-    r = np.tile(kappa_0 * np.cos(phi_r - phi_0), (runs, 1))
199-    mu = np.zeros((steps, runs))
200-    kappa = np.zeros((steps, runs))
[... 41 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 949,
 "limit": 480
}
```

```
949	The diagnostics show why. The noise raises the rectified sum that drives the global inhibition,
950	from 0.5 without noise to 0.52 to 0.59 at 0.1 s and 0.57 to 0.76 at 1 s, and that extra inhibition
951	shrinks the bump; the zero mode stays near 0 (at most 0.014 in size). With the inhibition held at
952	its noise-free level, so that the noise is only one more input to otherwise unchanged dynamics as in
953	SI section 5, the mean amplitude rises: 1.08, 1.33, 1.01 and 1.07 after 5 s, against 1.08, 1.35, 1.02
954	and 1.08 from the Rice mean that SI Eq. S124 implies, each within 1.5 standard errors. So the
955	upward drift the SI derives is present in the noise's direct effect, and in the released network it
956	is outweighed by the noise's effect on the global inhibition. The criterion tests the full network;
957	whether that is what the paper claims is asked of a reader (questions/000289.yaml).
958	
959	
960	######## CELL 39 [markdown]
961	## fig4b-connectome-motifs
962	
963	> The connectivity among EPG, Delta7 and PEN1 neurons in the hemibrain connectome resembles the
964	> connectivity of a network that implements the approximate circular Kalman filter, with shifted
965	> PEN1 to EPG projections and broad EPG to Delta7 to EPG inhibition.
966	
967	Total synapse count per pair, from the public hemibrain v1.2 export (the paper used v1.2.1 in
968	neuPrint, which now needs a personal token). Neurons are sorted by the PB glomerulus in their
[... 460 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i "pixel\|mask" $TMPDIR/nb.txt | head -30; grep -n -i "mask" bra.py | head
```

```
371:def contrast_mask(s, c, shift_blocks=0):
386:        m = contrast_mask(s, c)
394:true = [np.abs(np.mean(np.exp(1j * (bra.fourier(s["dff"])[0] - s["cue"]))[contrast_mask(s, 3)])) for s in sessions]
395:shift = [np.abs(np.mean(np.exp(1j * (bra.fourier(s["dff"])[0] - s["cue"]))[contrast_mask(s, 3, 1)])) for s in sessions]
1209:TwoPhotonSeries averaged over planes, smoothed in the plane (Gaussian SD 4 pixels) and averaged in
1210:each ROI mask, minus each ROI's 10th percentile over the session, read in blocks of 25 volumes every
1223:    F = bra.raw_roi_fluorescence(f1, blocks, s1["masks"], proj, sm)
1260:    F = bra.raw_roi_fluorescence(f, blocks, s["masks"], "mean", (0, 2, 4))
1378:contrast is not above zero contrast (7 of 15 flies with either signal). Across 18 variants of the raw signal (smoothing 0, 2 or 4 pixels;
1421:ROI masks are 5 to 9 pixels on the PB midline, and the stored dF/F agrees with the raw imaging
280:        "masks": f["processing/ophys/ImageSegmentation/PlaneSegmentation/image_mask"][:],
312:def raw_roi_fluorescence(f, frames, masks, projection="mean", smooth=4.0):
316:        return _raw_roi(f, frames, masks, projection, smooth)
317:    return _raw_roi(f, frames, masks, projection, (smooth,))[smooth]
320:def _raw_roi(f, frames, masks, projection, smooths):
323:    pixels, and averaged over each ROI's 2D mask (5 to 9 pixels on the PB midline). Neither the
328:    m = masks.reshape(masks.shape[0], -1).astype(float)
```

**Agent calls Bash**

```bash
cd  grep -n "def resultant_se\|def objective_se\|def objective\b\|def objective(" -A22 bra.py | head -80
```

```
121:def objective(values, mu=0.5, sigma=1.0, rates=RATES):
122-    """Prior-weighted average over log rate, trapezoidal rule; objective() of the figure notebooks
123-    with mu_perf = 0.5 and sig_perf = 1 (Methods, Performance measures; claims file)."""
124-    x = np.log(rates)
125-    f = np.asarray(values) * norm.pdf(x, loc=mu, scale=sigma)
126-    return np.sum(0.5 * (f[1:] + f[:-1]) * np.diff(x))
127-
128-
129:def resultant_se(R, n=10000):
130-    """Monte Carlo standard error of an accuracy |m1| = |mean exp(i error)| over n independent runs
131-    (n = 10,000 in every performance_scan_*.py). Delta method with the mean error at 0, so that
132-    |m1| is about the mean of cos(error): SE = sd(cos error) / sqrt(n). Two values are returned:
133-    under von Mises errors with resultant R (var cos = (1 + A2) / 2 - R^2, A2 = I2/I0), and the
134-    distribution-free upper bound sqrt((1 - R^2) / n). A standard choice; it sets only how a
135-    difference is read, not a criterion."""
136-    R = np.atleast_1d(np.asarray(R, float))
137-    vm = np.empty_like(R)
138-    for k, r in enumerate(R):
139-        r = min(max(r, 1e-6), 1 - 1e-9)
140-        kap = brentq(lambda x: i1e(x) / i0e(x) - r, 1e-9, 1e6)
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 3390,3402p 10.1073-pnas.2210622120.txt; grep -o ".\{400\}reduced the drop in inference accuracy.\{300\}" 10.1073-pnas.2210622120.txt | head -2
```

```
w/o retuning
w/ retuning
Best network
Fig. S4. Neural noise changes the optimal fixed point amplitude and decay speed. We simulated a network of N = 64 neurons with different levels of additive Gaussian noise
with variance σ2
nnδt to each neuron within each time step δt, for different fixed point amplitudes κ∗and decay speeds β. As in main text Fig. 3D, the performance of each
network was assessed by its average inference accuracy over different HD observation information rates, weighted by a prior over these information rates (see Methods for
simulation details and parameters). Each panel shows this performance, relative to the best performance of a noise-free network, for a grid over values of κ∗and β. As can be
seen, the optimal κ∗and β that maximizes relative performance changes with σnn (purple dot), and differs from the best κ∗and β for the noise-free network (light blue dot).
In particular, larger noise requires re-tuning the network to use a larger κ∗and β.
28 of 30
Anna Kutschireiter, Melanie A. Basnak, Rachel I. Wilson and Jan Drugowitsch

 attractors close to the attractor state ( 41 ). We here show that such a diffusion persists even if the network operates far away from the attractor state, as is the case in our Bayesian ring attractor. While it is impossible to completely suppress the impact of neural noise, the derivations revealed that we can lessen its impact by retuning the network’s connectivity strengths. Indeed, doing so reduced the drop in inference accuracy by about 35% when compared to the network tuned to optimize noise-free performance ( Fig. 3 D and F ) and also boosted the network’s signal-to-noise ratio ( Fig. 3 F ). Lastly, our derivations show that the impact of noise vanishes once the network’s population size becomes sufficiently large, in l
```

**Agent**

# Round 2 verification: Kutschireiter et al. 2023 with DANDI:000289

I agree with all 13 outcomes. The notebook's printed outputs support every number in the conclusions, the summary, the README and the record's notes, except four sentences: one swapped pair of ratios, one value that is never printed, one unproven independence claim, and one wrong description of the noise diagnostic. The record states my round-1 reasons faithfully. One new point bears on the noise claim's explanation, but not on its outcome.

## 1. Outcomes and assumptions

The claims file and the attempt record each have 13 claims and 13 outcomes, with matching ids. Notebook cell numbers have shifted by about one since round 1.

| Claim | Record | Agree? |
|---|---|---|
| fig1-conflict-decreases-certainty | reproduced | Yes (cell 13: 6 of 6 under (a) and (b)) |
| fig2h-bump-tracks-circkf | reproduced | Yes (cell 16) |
| fig2i-accuracy-and-certainty-vs-reliability | reproduced | Yes (cell 19) |
| fig3b-bayesian-beats-conventional | reproduced | Yes (cell 22) |
| fig3c-update-weights | reproduced | Yes (cell 25) |
| fig3d-best-network-slow-decay | partially_reproduced | Yes. Condition 4 fails as written (cell 28). |
| fig3f-noise-drop-below-70 | reproduced | Yes (cell 31) |
| fig3f-retuning-reduces-drop | reproduced, measured 34.64 | Yes. 3 of 6 readings fall in 31.5 to 38.5%, and the SNR ratio is 1.05 to 3.00 (cell 34). |
| noise-effects-on-mu-and-kappa | partially_reproduced | Yes, as the criterion is written. Condition (2) fails in all 4 settings (cell 37). |
| fig4b-connectome-motifs | partially_reproduced, assumed | Yes. The criterion needs two sorts and only reading (a) can be formed (cells 6 and 40). |
| fig4gh-drosophila-network-matches | partially_reproduced | Yes. Reading (a) fails at 0.1, 0.2 and 0.3/s (cell 43). |
| figs2-performance-independent-of-n | not_reproduced | Yes. N = 16 at 0.1/s is 0.0414 off, both readings fail (cell 46). |
| prediction-bump-amplitude-cue-reliability | blocked (methods_underspecified) | Yes. dF/F with reading (b) gives p = 0.138; the other three combinations hold (cell 50). |

**Assumptions.** Only fig4b is marked `assumed: true`. Both of its assumptions are stated in the deviations and are reasonable:
- **Any synapse counts as a connection.** This is the legend's "total number of synaptic connections". The 3- and 5-synapse counts are shown alongside.
- **Offset measure.** The offset is the synapse-weighted circular mean of EPG targets minus that of EPG inputs (period 8 glomeruli). The paper gives no measure.

The raw-signal choices for the prediction claim are also the author's own, and they are listed as deviations. They cannot change that outcome, because the dF/F readings already disagree.

**Places where the claims file misreads or over-tightens the paper** (reported, not corrected):
- **Noise claim, criterion (2).** It tests the drift on the full network. SI §5 (Eqs. S121–S124) derives only the noise term's own contribution to dκ ("if the drift is not accounted for"). This is my round-1 B1; the record forwards it to a question for a reader.
- **fig4b, reading (b).** The criterion offers an ellipsoid-body or gall sort "in the name" that hemibrain names cannot provide, then requires both sorts. So the partial outcome comes from how the criterion is written, not from the connectome.
- **figs2.** The paper says "mostly independent", but the criterion requires every one of the 161 cells to be within 0.02. The not_reproduced outcome rests on one cell.

## 2. Sentences the numbers do not support

**Cell 51.** "p = 0.021 with raw fluorescence but p = 0.138 with dF/F (median high/low ratio 1.12 and 1.11)". Read in order, this gives raw 1.12 and dF/F 1.11. Cell 50 prints dF/F 1.120 and raw 1.112, so the ratios are swapped. The record's notes have them the right way round.

**Cells 38 and 37, and the record (noise notes and the code_mismatch finding).** Three related sentences go beyond what the diagnostic shows:
- Cell 38 says the run holds the inhibition "so that the noise is only one more input to otherwise unchanged dynamics as in SI section 5".
- The `bra.rnn_batch` docstring says "the other dynamics are unchanged".
- The record says "the fall comes from the noise raising the rectified sum".

`inh_fixed` replaces the whole term `w_quad·π/N·Σmax(r,0)` with a constant. That term is the only one that depends on amplitude: it is the decay that pulls the bump back to κ* = 1. Holding it fixed turns the first mode neutral (1.5 − 1 − 0.5 = 0), leaving a free 2-D random walk. That is why the end amplitude matches the Rice mean.

So the control changes two things at once: it removes the noise's effect on the inhibition, and it removes the restoring force. It shows that the SI's noise term is correct. It does not show that the noise's effect on the inhibition is what outweighs the drift in the full network. The numbers themselves (1.08, 1.33, 1.01 and 1.07, each within 1.5 SE of the Rice means) are correct.

**Cell 52, Summary.** "The ROI masks are 5 to 9 pixels on the PB midline". No cell prints the mask sizes; the figure appears only in a `bra.py` docstring.

**Cell 28 comment and cell 29.** "each cell is its own scan" is used to compute the SE of a difference between two grid cells (0.0026), which gives the "0.32 and 0.52 SE, within sampling error" verdict. Nothing printed shows that the grid cells use independent trajectories. If the scan reuses trajectories, that SE is too large.

**Minor imprecisions:**
- **Cell 11.** "lag 0 or 5 frames (0 to 0.55 s)". Sub-10 peaks at lag 5 and is imaged at 7.87 Hz, which is 0.64 s.
- **README.** "Not reproduced (one value of 161)". There are 161 cells, but only 160 values: one is NaN (cell 46).
- **Record, figs2 notes.** "about 1.2 values … expected" leaves out that the expectation covers N ≥ 8 only. The notebook says so.

**Checked and supported.** Everything else in the conclusions, the summary, the README and the record's notes matches the printed outputs. That covers fig1, fig2h, fig2i, fig3b, fig3c, fig3d, both fig3f claims, fig4b, fig4gh, figs2 and the prediction claim's counts, p-values and variant ranges. It also covers the README's run time (6.9 min, cell 53) and the description of the data.

**My round-1 reasons in the record.** The `verifications` block gives each of my 13 round-1 outcomes and reasons faithfully, including the B-points and the things I could not check. It correctly marks fig4b and figs2 as `agrees: false` against the original record.

## 3. Round-1 points

**Resolved:**
- **B2, MC error for fig4gh and figs2.** The SE is now shown. figs2 is 4.3 SE off, so it is not noise. fig4gh's differences are 1.16 to 1.95 SE. Both outcomes rest on the criterion's bounds, and the record says so.
- **B3, fig3d rises.** Resolved, subject to the independence caveat above.
- **B4, fig4b threshold.** The outcome was changed to partial, and the threshold dependence is stated.
- **B5, raw-signal variants.** 18 variants were added; the split follows division by F0.
- **B6, bump decoder.** The phase sign is now stated, and the spectral peak is at frequency 2 in all 15 flies (cell 49).
- **B7, weak comparison (a) in fig1.** Stated.
- **B8, NaN cell.** Printed as N = 128 at 100/s.
- **B9, "No claim is blocked" in cell 0.** Corrected.
- **C, unchecked code details.** The kappa_z = γ_z comment, the stats columns and the axis order are settled by the printed source lines and the array shapes.

**Remaining:**
- **B1 / noise claim, partly resolved.** The diagnostic was added, but it does not isolate the cause (section 2). This bears on the explanation in the noise conclusion and the code_mismatch finding, not on the outcome, which follows the criterion. A cleaner control would keep the inhibition at the value implied by the decoded amplitude alone.
- **New, on the fig3d SE.** The independence of the grid cells is assumed, not shown. This affects only the "within sampling error" reading; condition 4 fails as written either way.
- **B10, not changed.** The retuned performance is still a maximum over noisy grid cells, which biases it upward; the reduction values (34.64%) depend on it. The record keeps it because the paper's notebook does the same, which is acceptable.
- **Claims-file points.** The three in section 1 (noise criterion (2), fig4b reading (b), figs2 "mostly") are for the claims file's authors.

## End of run

18 turns, 3 minutes, result: success.
