# crcns-pfc-6 · verifier-1 · run 41962745919

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; wc -c *
```

```
Exit code 1
total 388
drwxr-xr-x 6 runner runner    4096 Nov  5 03:42 .
drwxr-xr-x 7 runner runner    4096 Nov  5 03:42 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  5 03:36 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  5 03:36 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov  5 03:42 .claude
-rw-r--r-- 1 runner runner       0 Nov  5 03:42 .env
-rw-r--r-- 1 runner runner       0 Nov  5 03:42 .env.development
-rw-r--r-- 1 runner runner       0 Nov  5 03:42 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov  5 03:42 .env.local
-rw-r--r-- 1 runner runner       0 Nov  5 03:42 .env.production
-rw-r--r-- 1 runner runner       0 Nov  5 03:42 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov  5 03:42 .env.test
-rw-r--r-- 1 runner runner       0 Nov  5 03:42 .env.test.local
drwx------ 2 runner runner    4096 Nov  5 03:42 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  5 03:36 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  5 03:36 .github
-rw-r--r-- 1 runner runner       0 Nov  5 03:42 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  5 03:36 .idea
[... 40 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "10.1038-nn.2337.yaml"
}
```

```
1	# Claims for Peyrache, Khamassi, Benchenane, Wiener & Battaglia (2009), Nat Neurosci 12:919-926,
2	# on CRCNS data set pfc-6 (doi:10.6080/K0KH0KH5).
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-05,
4	# protocol as stated in docs/protocol.md (Reader), version pilot-13.
5	#
6	# Text read: the version of record, as supplied under paper/ (PyMuPDF text of the journal PDF),
7	# with its Results, Discussion, figure legends and Online Methods, and the supplement
8	# (41593_2009_BFnn2337_MOESM12_ESM.pdf), from which the Supplementary Discussion, the legends of
9	# Supplementary Figures 2 to 13 and Supplementary Table 1 were read. The legend of
10	# Supplementary Figure 1 (histology) is not in the extracted text; no claim rests on it. The PDF
11	# pages could not be rendered here, so no figure was read from the image. The extracted text
12	# prints some signs as other glyphs. "P o" is P <, "P 4" is P >, "n 1⁄4" is n =, "B" before a
13	# number is "about", and "10�30" is 10 to the power -30. Quotes keep these glyphs as printed,
14	# and the p-values below are read from them; the quote checker cannot find p-values printed as
15	# powers of ten, which were confirmed by reading. The paper links no analysis code, so none was
16	# read; every method below is from the Online Methods, the figure legends or the supplement.
17	#
18	# Data the paper used. Four male Long-Evans rats (rats 15, 18, 19 and 20), a drive of six
19	# recording tetrodes in the right prelimbic cortex (mPFC) and three tetrodes for LFP in ventral
20	# CA1. 63 sessions (rat 15, 16; rat 18, 11; rat 19, 12; rat 20, 24), 1,692 mPFC cells. Only
[... 737 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat pfc6.py
```

```
"""Loading and reactivation measures for CRCNS pfc-6 (Peyrache et al. 2009, Nat Neurosci 12:919).

The data set is one tar.gz on the public CRCNS bucket. It is streamed once, in order, and each
session's text files are parsed in memory; nothing is written to disk.

Where parameters come from:

- 100 ms bins, z-transform per cell within an epoch, C = QQ'/B, projectors p p', and
  R_l(t) = sum over i != j of Q_it P_ij Q_jt: Online Methods, "Computational methods", and
  Supplementary Figure 3 (cited in the claims file's opening comment).
- lambda_max/min = (1 +- sqrt(1/q))^2, q = B/n, Phi = lambda/lambda_max: Online Methods,
  "Signal and nonsignal components".
- Inclusion rule (at least ten cells, at least 4 min of SWS in each rest epoch): Results,
  paragraph 2, as the claims file quotes it.
- A bin counts as SWS when it lies wholly inside an SWS interval: standard choice named in the
  claims file's opening comment.
- Rest epochs: the data set gives SWS intervals and the awake epoch only. The pre epoch is taken
  as the time before the awake epoch and the post epoch as the time after it, each bounded by the
  first and last spike of the session (an assumption; the claims file's supp5 criterion says the
  rest epochs are taken from the data set's epoch times).
[... 292 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_peyrache_2009.ipynb'))
for i,c in enumerate(nb['cells']):
    print(f'=== [{i}] {c[\"cell_type\"]}')
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: t=''.join(o['text'])
        elif 'data' in o: t=''.join(o['data'].get('text/plain',''))
        else: t=str(o.get('ename'))+str(o.get('evalue'))
        print('--- out:'); print(t[:6000])
" > $TMPDIR/nb.txt; wc -l $TMPDIR/nb.txt
```

```
1273 /tmp/claude-1001/nb.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt"
}
```

```
1	=== [0] markdown
2	# Reproducing Peyrache et al. (2009) from CRCNS pfc-6
3	
4	**Paper.** Peyrache A, Khamassi M, Benchenane K, Wiener SI, Battaglia FP (2009). Replay of
5	rule-learning related neural patterns in the prefrontal cortex during sleep. *Nature
6	Neuroscience* 12(7):919-926. [doi:10.1038/nn.2337](https://doi.org/10.1038/nn.2337)
7	
8	**Dataset.** CRCNS pfc-6, "Activity of neurons in rat medial prefrontal cortex during learning
9	and sleep" ([doi:10.6080/K0KH0KH5](https://doi.org/10.6080/K0KH0KH5)), read anonymously from the
10	public bucket at `https://crcnsarchive.s3-us-west-2.amazonaws.com/pfc-6/live/`. The data set holds
11	one archive, `mPFC_Data.tar.gz`, with seven text files per session (spikes, cell types, behaviour,
12	position, awake and SWS intervals), described by `docs/crcns_pfc-6_data_description.pdf`
13	(version 0.7, March 12, 2018).
14	
15	**Version.** CRCNS data sets are not versioned (docs/archives.md), so the version is recorded as
16	`unversioned`, and the file read is pinned by its MD5 from the data set's `checksums.md5`:
17	`mPFC_Data.tar.gz` 2c255b44209ece01326dd09efaabd92a, checked below against the bucket's ETag.
18	The data set's description is checksummed too (pdf 3464d68562a83bb15d843999ec3227c8, docx
19	c536d32bb1a791ac00a9a7d1056f57a6); the learning sessions are read from the docx. This is the
20	only published version (`live/`; there is no `old/` folder), and the paper cites none.
[... 693 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 713,
 "limit": 600
}
```

```
713	SWS    post  0.1469 0.0090    285
714	       pre   0.1005 0.0076    285
715	nonSWS post  0.1088 0.0079    285
716	       pre   0.0985 0.0078    285
717	
718	non-SWS, post against pre over signal components: mean diff 0.0103, paired t p = 0.0416, Wilcoxon p = 0.0179
719	SWS, post against pre over the same components: mean diff 0.0464, paired t p = 5.83e-09
720	  group >1.8: n=9, non-SWS post-pre 0.0183 (t p = 0.49), SWS post-pre 0.2714
721	  group 1.4-1.8: n=35, non-SWS post-pre 0.0234 (t p = 0.21), SWS post-pre 0.1439
722	  group 1-1.4: n=241, non-SWS post-pre 0.0081 (t p = 0.13), SWS post-pre 0.0238
723	
724	variant, 30 min rest epochs (285 components): state p = 0.0178, epoch p = 0.000472, interaction p = 0.0261; means SWS pre 0.1010 post 0.1487, non-SWS pre 0.0998 post 0.1104; non-SWS post-pre paired t p = 0.0438, Wilcoxon p = 0.0207
725	non-SWS minutes per session: pre 10.0 to 46.3, post 10.0 to 50.1
726	
727	=== [22] markdown
728	## supp6-pre-post-sws-alike
729	
730	> Pre and post epoch SWS do not differ in average SWS duration, average firing rates, rates of
731	> SPWRs and delta waves, or LFP power in the delta and spindle bands.
732	
[... 542 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_peyrache_2009.ipynb'))
c=nb['cells'][3]
for o in c['outputs']:
    t=''.join(o.get('text',''))
    print(t[5500:])
" ; grep -n -i -E "lfp|tetrode|ripple|eeg|channel|learning|Trials during" paper/pfc-6.data-description.txt | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  cat paper/pfc-6.data-description.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=pfc-6/" | python3 -c "import sys,re; x=sys.stdin.read(); print(x[:300]); [print(k,s) for k,s in re.findall(r'<Key>(.*?)</Key>.*?<Size>(\d+)</Size>',x)]"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; for f in filelist.txt checksums.md5 Load_And_View_Data_Examples.m; do echo "== $f"; curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/pfc-6/live/$f"; done; echo; curl -s -r 0-2000000 "https://crcnsarchive.s3-us-west-2.amazonaws.com/pfc-6/live/mPFC_Data.tar.gz" -o part.gz; python3 -c "
import zlib
d=zlib.decompressobj(31); raw=d.decompress(open('part.gz','rb').read())
import re
names=[raw[i:i+100].split(b'\0')[0].decode(errors='replace') for i in range(0,len(raw)-512,512) if raw[i+257:i+262]==b'ustar']
print(names)"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  python3 -c "
import numpy as np, pfc6
rng=np.random.default_rng(0)
# reactivation vs brute force
q=rng.normal(size=(6,50)); vec=np.linalg.qr(rng.normal(size=(6,6)))[0]
R=pfc6.reactivation(q,vec)
l=2;P=np.outer(vec[:,l],vec[:,l]);np.fill_diagonal(P,0)
print('react ok', np.allclose(R[l], np.einsum('it,ij,jt->t',q,P,q)))
# shuffle closed form vs brute force exact over all perms (n=5)
import itertools
q=rng.normal(size=(5,3)); v=vec[:5,:1]
ex=pfc6.shuffle_expected_R(q,v)[0]
bf=np.mean([pfc6.reactivation(q[list(p)],v)[0] for p in itertools.permutations(range(5))],axis=0)
print('shuffle ok', np.allclose(ex,bf))
# criterion
print(pfc6.reached_criterion([1]*10), pfc6.reached_criterion([1]*9), pfc6.reached_criterion([1]*5+[0]+[1]*6), pfc6.reached_criterion([1]*5+[0]+[1]*5))
# learning point: perfect block to end
for c in ([0,0,1,1,1,1,1],[0,1,0,1,1,1,1,1,1],[0,0,1,1,1,0,1,1,1,1]):
    print(c, pfc6.learning_point(c,True), pfc6.learning_point(c,False))
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import numpy as np, pfc6
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
cd  (pip install -q numpy fsspec 2>&1 || python3 -m pip install --user -q numpy fsspec 2>&1) | tail -2; python3 -c "import numpy; print(numpy.__version__)"
```

```
[notice] A new release of pip is available: 26.2.2 -> 26.3
[notice] To update, run: pip install --upgrade pip
2.5.4
```

**Agent calls Bash**

```bash
cd  python3 -c "
import numpy as np, pfc6
rng=np.random.default_rng(0)
q=rng.normal(size=(6,50)); vec=np.linalg.qr(rng.normal(size=(6,6)))[0]
R=pfc6.reactivation(q,vec)
l=2;P=np.outer(vec[:,l],vec[:,l]);np.fill_diagonal(P,0)
print('react ok', np.allclose(R[l], np.einsum('it,ij,jt->t',q,P,q)))
import itertools
q=rng.normal(size=(5,3)); v=vec[:5,:1]
ex=pfc6.shuffle_expected_R(q,v)[0]
bf=np.mean([pfc6.reactivation(q[list(p)],v)[0] for p in itertools.permutations(range(5))],axis=0)
print('shuffle ok', np.allclose(ex,bf))
print(pfc6.reached_criterion([1]*10), pfc6.reached_criterion([1]*9), pfc6.reached_criterion([1]*5+[0]+[1]*6), pfc6.reached_criterion([1]*5+[0]+[1]*5))
for c in ([0,0,1,1,1,1,1],[0,1,0,1,1,1,1,1,1],[0,0,1,1,1,0,1,1,1,1]):
    print(c, pfc6.learning_point(c,True), pfc6.learning_point(c,False))
x=rng.normal(size=200); y=np.r_[0,x[:-1]]
print('xcorr lag+1', np.round(pfc6.xcorr_runs(x,y,[0],[200],2),2))
e=np.arange(0,1001,100.); print(pfc6.in_intervals(e,np.array([[150,450]])))
"
```

```
react ok True
shuffle ok True
True False True False
[0, 0, 1, 1, 1, 1, 1] 3 None
[0, 1, 0, 1, 1, 1, 1, 1, 1] 4 None
[0, 0, 1, 1, 1, 0, 1, 1, 1, 1] 3 None
xcorr lag+1 [-0.07 -0.03 -0.05  1.   -0.05]
[False False  True  True False False False False False False]
```

**Agent calls Bash**

```bash
cd  grep -c "^- id:" 10.1038-nn.2337.yaml
```

```
29
```

**Agent calls Bash**

```bash
cd  grep -n -E "r2|0\.61|99th|skewness|n 1⁄4 10, 40|Supplementary Fig. 5" paper/10.1038-nn.2337.txt | head; grep -n -i -E "ANOVA|Fig(ure)? ?5|SWS vs" paper/10.1038-nn.2337.supp.pdf 2>/dev/null | head -2; ls paper
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 240,300p paper/10.1038-nn.2337.txt; sed -n 420,460p paper/10.1038-nn.2337.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

**A. Outcomes** (29 claims in the claims file: 15 tested in the notebook, 14 treated as blocked)

| Claim | Outcome | Reason |
|---|---|---|
| sessions-and-cells | not_reproduced | Neither reading falls within tolerance. All sessions gives 86 sessions and 2155 cells; the inclusion rule gives 56 and 1499 (need 57–69 and 1523–1861). Per rat under the rule: 10/11/11/24, against the paper's 16/11/12/24 (cell 9). |
| rules-learned | not_reproduced | Both readings give right 3, lit 4, left 3, dark 1, against 4/4/2/1. Rat 18 never reaches the criterion under the right-arm rule (cell 11). |
| learning-sessions | not_reproduced | No reading gives 9–11 sessions over four rats: (a)(i) 34, (a)(ii) 16, (b)(i) 9 over 3 rats, (b)(ii) 4 (cell 13). Reading (b) is computed wrongly (problem 1), so this result is not final. |
| fig1b-signal-components | partially_reproduced | Signal total is 285, outside 291–355. Nonsignal is 730, exactly at the lower bound. 45 of 56 sessions have 1–6 signal components. Per session the rates match the paper (5.09 and 13.04 against 5.13 and 12.87) (cell 17). |
| fig2b-post-greater-than-pre | reproduced | Post exceeds pre in all three groups with p < 0.005 under both tests and both z readings (epochz t: 0.0015, 1.4e-4, 2.3e-4). Group sizes are 9/35/241, so two of the three expected counts are outside tolerance. That shortfall comes from fig1b (cell 19). |
| supp5-sws-only | not_reproduced | The state main effect has p = 0.0138, above the required 0.01. In non-SWS bins post exceeds pre significantly (paired t p = 0.042, Wilcoxon p = 0.018). The 30-min variant gives the same result (cell 21). |
| supp6-pre-post-sws-alike | partially_reproduced | No difference by paired t-test in total SWS (p = 0.87), episode duration (0.41), session-mean rate (0.93) or cell rate (0.65). SPWR rate, delta waves and LFP power are blocked (data_missing) (cell 23). |
| fig2b-encoding-correlation | not_reproduced | r² is 0.384 (epochz) or 0.417 (swsz), outside 0.549–0.671. p < 1e-30 and r > 0 do hold. r itself is 0.620, close to the paper's "r² = 0.61", which the claims file cannot settle (cell 25). |
| fig2b-pre-weaker | partially_reproduced | The pre slope and correlation are lower in both z readings. The correlation test passes 1e-5 (Steiger p = 6e-13). The best slope p is 3e-13, which misses 1e-20, so this falls under the criterion's partial clause (cell 27). |
| supp8-other-tetrode-pairs | blocked (data_missing) | There is no tetrode per cell; confirmed against the archive (section C). |
| fig2e-skewness | not_reproduced | Only the 1.4–1.8 group is significant (p = 0.009). The >1.8 group has a negative mean difference (−1.19, p = 0.62), and there is no rise with Phi under either z reading (cell 29). |
| fig2f-tail-contribution | partially_reproduced | At best, 2 of 3 groups fall in 36–55%: swsz (a) gives 51.0, 60.6 and 36.6%; swsz (b) gives 46.3, 45.8 and 5459%. The epochz readings give 1 and 0 of 3 (cell 31). |
| supp10-no-coactivation | reproduced | Reading (a): the post-SWS zero lag is below 0 and below the 200–500 ms mean, with its minimum at 0 ms, in both z readings. The awake zero lag is 0.033, above chance with p = 8.5e-16 (cell 33). |
| supp11-shuffle-control | partially_reproduced | Shuffled values are about 1/20 of actual in every group, so the magnitude part holds. They differ between pre and post in the >1.8 group (t p = 0.031, Wilcoxon p = 0.012) and in 1.4–1.8 by Wilcoxon (p = 0.023), so the absence part fails (cell 35). |
| fig5a-spwr-bins, fig5b-spwr-triggered, fig5c-peak-40ms, fig5d-population-asymmetric, fig5e-autocorrelogram | blocked (data_missing) | No ripple times or hippocampal LFP in the archive. |
| replay-in-delta-spindle-periods, fig6a-delta-waves, fig6c-spindles | blocked (data_missing) | No prefrontal LFP in the archive. |
| fig6b-down-up | partially_reproduced | Post signal components have significant bins at −0.5 to −0.3 s, nonsignal components have none, and pre is lower in that window (0.063 against 0.107). Pre's peak is higher than post's (0.145 against 0.132), and the per-component post-minus-pre difference is not significant (p = 0.15). The SPWR part is blocked (cell 37). |
| fig6d-reactivation-spwr-correlation | blocked (data_missing) | Needs ripple times. |
| fig7b-post-spwr-after-learning, fig7b-controls, fig7c-choice-point, fig7d-two-factors | blocked (data_missing) | All templates come from SPWR or inter-SPWR bins, and there are no ripple times. |
| supp12-behavior-unchanged | reproduced | Trial length shows no difference: (b) paired p = 0.158, (a) p = 0.278. The test has little power (+2.7 s, n = 10), and the sessions come from the data set's description, not from learning-sessions (problem 3) (cell 39). |

**B. Problems**

1. [affects a conclusion] `pfc6.learning_point` with `include_block=False` returns None when the qualifying block of correct trials runs to the end of the session, because an empty remainder fails `len(rest)`. I confirmed this on a synthetic input: `[0,0,1,1,1,1,1]` gives 3 under (a) and None under (b). So reading (b) drops exactly the sessions that end in a clean run: 7 of the description's 10 learning sessions are NaN under (b) in cell 13. Counting the empty remainder as passing could move (b)(i) or (b)(ii) into 9–11 sessions over four rats, so learning-sessions is not settled under reading (b).
2. [does not affect a conclusion] In cell 37 (`down_up_times`), readings (a) and (b) give identical outputs. With 10 ms bins the mean count per bin is below 5, so "below a fifth of the mean" means a count of zero, and reading (b) is the same as (a). The notebook does not say so.
3. [does not affect a conclusion] Cell 39 (supp12) takes its learning sessions and trials from the data set's description, not from a reading of learning-sessions, which this claim depends on and which did not reproduce. The cell does say this. The description's points also disagree with every computed reading for 181020, 201222 and 201227 (cell 13).
4. [does not affect a conclusion] The module docstring of `pfc6.py` says rest epochs are bounded by the first and last spike. `rest_epochs` actually uses 0 and the end of the position record. That bound changes only the epochz values and supp5's non-SWS bins. supp5 fails under the 30-min variant too, and swsz results do not depend on it.
5. [does not affect a conclusion] Cell 21 (supp5) runs an ordinary two-way ANOVA on four non-independent means per component. A repeated-measures form could bring the state effect below 0.01, but the significant post > pre result in non-SWS bins still fails the claim.
6. [does not affect a conclusion] fig2f reading (b) and supp10 reading (b) divide by near-zero means, giving values like 5459% and a zero-lag ratio of −337 with s.e.m. 430. The cell 33 printout calls supp10 (b) "below chance: True", which is meaningless here. The supp10 outcome rests on reading (a), and the fig2f count rests on values that are well defined.
7. [does not affect a conclusion] `session_reactivation`/`template` count the 12 cells that are silent in the awake epoch in n. That lowers q and raises λmax slightly, which biases the signal count in fig1b down a little.
8. [does not affect a conclusion] Cell 9's 3.5-min SWS variant gives 63 sessions and 1682 cells, matching the paper's totals but not its per-rat counts. fig1b was not run under it; at about 5.09 signal components per session it would likely land inside tolerance. Two of the description's learning sessions (201227 with 2.2 min of pre SWS, 201229 with 3.3 min of post SWS) fail the 4-min rule, although the paper's Figure 7 uses them. This suggests the deposited SWS intervals or the inclusion rule differ from the paper's. The notebook does not mention it.
9. [does not affect a conclusion] Cell 39 shows a speed difference in path bin 0 (p = 0.034, uncorrected) without comment. Its path-fraction bins are not the paper's linearized maze.

Helper checks on synthetic inputs all passed: `reactivation` against a brute-force sum, `shuffle_expected_R` against an exact average over all permutations, `reached_criterion`, the lag sign of `xcorr_runs`, and `in_intervals`. The awake template is applied only to pre and post data, so there is no train/test leakage.

**C. Not checked, and what would settle it**

- **Blocked claims:** the S3 listing for pfc-6 has only `mPFC_Data.tar.gz`, the description (.pdf, .docx), `Load_And_View_Data_Examples.m`, `filelist.txt` and `checksums.md5`. The tarball's first entry is `SpikeData.dat`, and `load_sessions` would raise a KeyError on any file outside the seven kinds, so there is no LFP, ripple, delta or spindle data and no tetrode map. None of the blocked claims can be tested in part.
- **learning-sessions:** cell 13 rerun with an empty post-block remainder counted as passing under (b).
- **fig1b and fig2b:** signal and nonsignal totals and group sizes under the 3.5-min variant.
- **rules-learned:** for each rat and rule, the longest correct run and the best 12-trial window, to show whether a missing session or the criterion causes the mismatch.
- **supp5:** a repeated-measures ANOVA.
- **fig6b:** the lag of the one significant pre bin and the full pre profile.
- **Figures:** the plots were not viewable as images, so the plotted ranges were the only figure output I checked.

## End of run

17 turns, 4 minutes, $1.51 at API prices, result: success.
