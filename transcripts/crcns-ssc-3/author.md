# crcns-ssc-3 · author · run 42206111011

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md | head -c 200000 | wc -c; ls; ls claims/crcns-ssc-3 paper entries/001453-fouke-2025 claims/001453
```

```
Fri Nov  6 10:59:56 UTC 2026
36210
LICENSE
LICENSE-data
README.md
attempts
bunfig.toml
claims
docs
encore_science
entries
node_modules
package-lock.json
package.json
paper
papers
pnpm-lock.yaml
pyproject.toml
questions
queue
[... 25 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md"
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
[... 596 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md | head -150; echo ----; sed -n 1,400p docs/design.md | head -c 15000
```

```
# Encore Science: the registry

Encore Science checks datasets against the papers they came from. This repository holds its public record, the Encore registry, served at <https://encorescience.org>, and the `encore` command that runs the same check on your own data ([docs/encore.md](docs/encore.md)). It is developed by [CatalystNeuro](https://www.catalystneuro.com).

Agents, and people, try to reproduce the key findings of papers from the open
data in public archives, starting with the [DANDI Archive](https://dandiarchive.org), and register the result
here: the notebooks when it works, and the reason when it does not.

- **For the archive:** evidence of whether each dandiset is complete and
  accurate enough to support the findings of its paper.
- **For analysts:** working notebooks to build new analyses on.

Status: pilot. All eight pilot targets have been attempted and checked by an
independent agent.

**Dashboard:** <https://encorescience.org/>

## Reading the outcomes

An outcome says what one attempt could recover from the data in a dandiset,
[... 391 more lines not kept]
```

**Agent calls Bash**

```bash
cat docs/archives.md
```

```
# Archives

The registry tests papers against data in public archives. It began with one,
the DANDI Archive. The protocol is written for any archive. What is particular
to an archive (how its datasets are named, versioned and read) is here, and an
agent is pointed to its archive's section.

A dataset is keyed as `<archive>:<id>` and shown as `<LABEL>:<id>`, for example
`DANDI:000003`. Its files in this repository (`claims/`, `questions/`,
`transcripts/`, the `attempt/` branch, the paper store) are under its folder
name: the identifier alone for DANDI, which the registry began with, and
`<archive>-<id>` for any other archive. Each archive is an adapter, a module in `tools/archives/` ("Adding an archive",
below), and `tools/datasets.py` turns one form of a dataset's name into another.
The workflows take a dataset in any of these forms.

## DANDI

- **Datasets.** A dandiset, identified by six digits (`000003`). Targets are the
  public dandisets whose metadata names a paper (`targets/dandisets.json`, built
  by `tools/build_targets.py` and refreshed daily by the Track DANDI workflow).
[... 270 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/crcns-ssc-3/*.yaml
```

```
<persisted-output>
Output too large (30.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/210349ad-6943-476f-a17d-3881b38a948a/tool-results/bc3ez0exx.txt

Preview (first 2KB):
# Claims for Timme, Ito, Myroshnychenko, Nigam, Shimono, Yeh, Hottowy, Litke & Beggs (2016),
# "High-Degree Neurons Feed Cortical Computations", PLoS Comput Biol 12(5), e1004858, on CRCNS ssc-3.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-06,
# protocol as stated in docs/protocol.md (version pilot-13), Reader steps 1 to 4.
#
# Text read: the version of record, PMC4861348 (Europe PMC full-text XML, flattened), with its
# Materials and Methods, Results, Discussion, the legends of Figures 1 to 7, Table 1 and the legend
# of S1 Fig (the only supplement; it is a figure, so only its legend is text). No PDF was supplied,
# so no figure could be read. The flattened text has lost every displayed equation (Eqs 1 to 24).
# The information measures (Eqs 1 to 12) are described in words well enough to be rebuilt, and
# each criterion says how it reads them. The feedforward model is not: the binary-signal currents
# (Eqs 16 to 19), the form of the rewiring score (Eq 20) and the fitted score equations (Eqs 22 to
# 24) are given only as equations. The model claims below need these equations read from the
# version of record before they can be tested. Values shown only in figures (the binomial skew
# probabilities of Fig 5A and 5B, the fitted exponents and their 95% ranges in Fig 6, the means in
# Fig 7C and 7D) could not be read and are not claimed as numbers.
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cat paper/ssc-3.data-description.txt; wc -c paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/crcns-ssc-3/10.1371-journal.pcbi.1004858.yaml"
}
```

```
1	# Claims for Timme, Ito, Myroshnychenko, Nigam, Shimono, Yeh, Hottowy, Litke & Beggs (2016),
2	# "High-Degree Neurons Feed Cortical Computations", PLoS Comput Biol 12(5), e1004858, on CRCNS ssc-3.
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-06,
4	# protocol as stated in docs/protocol.md (version pilot-13), Reader steps 1 to 4.
5	#
6	# Text read: the version of record, PMC4861348 (Europe PMC full-text XML, flattened), with its
7	# Materials and Methods, Results, Discussion, the legends of Figures 1 to 7, Table 1 and the legend
8	# of S1 Fig (the only supplement; it is a figure, so only its legend is text). No PDF was supplied,
9	# so no figure could be read. The flattened text has lost every displayed equation (Eqs 1 to 24).
10	# The information measures (Eqs 1 to 12) are described in words well enough to be rebuilt, and
11	# each criterion says how it reads them. The feedforward model is not: the binary-signal currents
12	# (Eqs 16 to 19), the form of the rewiring score (Eq 20) and the fitted score equations (Eqs 22 to
13	# 24) are given only as equations. The model claims below need these equations read from the
14	# version of record before they can be tested. Values shown only in figures (the binomial skew
15	# probabilities of Fig 5A and 5B, the fitted exponents and their 95% ranges in Fig 6, the means in
16	# Fig 7C and 7D) could not be read and are not claimed as numbers.
17	#
18	# Code read: none. The paper links no analysis or model code. Its Data Availability names the
19	# deposit "http://dx.doi.org/10.6080/K07D2S2F" at CRCNS, which is ssc-3. The data descriptor
20	# (ssc-3 data description, version 0.8) was read only to know what the dataset holds; no claim
[... 366 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,400p paper/10.1371-journal.pcbi.1004858.txt | head -c 50000
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 - <<'EOF'
t=open('paper/10.1371-journal.pcbi.1004858.txt').read()
i=t.find('1/16\n\n0\n\n0\n\n0\n\n0\n\n0\n\n0\n\n0\n\n1\n\n0\n\n1\n\n1')
print(t[45000:])
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/210349ad-6943-476f-a17d-3881b38a948a/tool-results/bwsfzuk4b.txt"
}
```

```
1	ropy distributions for raw TE and normalized TE across the two time scales studied in this analysis (interactions with delays of 1.6–6.4 ms (A) and 3.5–14 ms (B)). Note that all distributions are roughly log-normal (see Eq 21 , nonlinear regression performed in Matlab). Solid line is average of all recordings; shaded region represents ± one standard deviation across recordings. (B and D) In, out, and total degree distributions from the real data and total degree distributions from random networks with matching numbers of neurons, connections, and sampling statistics to the real data. Note that because the total degree distribution from the real data extends far beyond the distribution from the random networks, the real data are heavy-tailed. We did not assess whether the degree distributions were scale-free due to issues surrounding sub-sampling [ 93 ]. Also, note that the in-degree distribution had a shorter tail than the out-degree distribution, indicating that there were more high out-degree neurons than there were high in-degree neurons. Solid line is average of all recordings; shaded region represents ± one standard deviation across recordings.
2	
3	Several previous studies found log-normal distributions of connection weights or distributions of weights that varied widely over several orders of magnitude [ 17 – 22 ]. Similar to these studies, we found a roughly log-normal distribution of significant TE weights ( Fig 4A and 4C ). We fit the distributions using the following probability mass function:
4	
5	Note that we used a probability mass function because we binned the TE values into 100 logarithmically spaced bins to produce the distributions shown in Fig 4A and 4C . This binning necessitated the use of an additional normalization factor α in the fits. The TE distributions appeared more skewed when considering normalized TE values. This skew may be caused by the bound in the normalized TE at 1. Regardless of the precise distribution that best fits the TE d
[... 135 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
t=open('paper/10.1371-journal.pcbi.1004858.txt').read()
i=t.find('Hidden Self Interaction\n')
s=t[i:45000]
import re
# compress table section
print(re.sub(r'\n\n',' | ',s[:6000]))
print("=========")
print(s[6000:])
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=ssc-3/" | python3 -c "
import sys,re;t=sys.stdin.read();
for k,s in zip(re.findall('<Key>(.*?)</Key>',t),re.findall('<Size>(.*?)</Size>',t)): print(k,s)"; curl -sI https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004858 | head -3; curl -sI "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4861348/fullTextXML" | head -3
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-3/live/checksums.md5; curl -s https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-3/live/filelist.txt; curl -s "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4861348/fullTextXML" -o p.xml; ls -la p.xml; grep -c "mml:math" p.xml
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'EOF'
import re
t=open('p.xml').read()
for m in re.finditer(r'<disp-formula id="(.*?)">(.*?)</disp-formula>',t,re.S):
    s=re.sub(r'<[^>]+>',' ',m.group(2)); s=re.sub(r'\s+',' ',s)
    print(m.group(1), s[:400])
EOF
```

```
pcbi.1004858.e001  (1) M I ( I F ; J P ) = ∑ i F , j P p ( i F , j P ) log ( p ( i F , j P ) p ( i F ) p ( j P ) ) 
pcbi.1004858.e002  (2) M I ( I F ; J P | I P ) = ∑ i F , i P , j P p ( i F , i P , j P ) log ( p ( i F | i P , j P ) p ( i F | i P ) ) 
pcbi.1004858.e003  (3) T E ( J → I ) = M I ( I F ; J P | I P ) = ∑ i F , i P , j P p ( i F , i P , j P ) log ( p ( i F | i P , j P ) p ( i F | i P ) ) 
pcbi.1004858.e004  (4) T E ( J → I ) N o r m = T E J → I − ∑ i f u t u r e p ( i F ) log ( p ( i F ) ) 
pcbi.1004858.e005  (5) T E ( { J , K } → I ) = Synergy ( { J , K } → I ) + Unique ( K ; J → I ) + Unique ( J ; K → I ) + Redundancy ( { J , K } → I ) 
pcbi.1004858.e006  (6) T E ( J → I ) = Unique ( K ; J → I ) + Redundancy ( { J , K } → I ) 
pcbi.1004858.e007  (7) T E ( K → I ) = Unique ( J ; K → I ) + Redundancy ( { J , K } → I ) 
pcbi.1004858.e008  (8) Redundancy ( { J , K } → I ) ≡ I min ( I F ; J P , K P | I P ) = ∑ i F p ( i F ) min R ∈ { J P , K P } I s p e c ( I F = i F ; R | I P ) = ∑ i F p ( i F ) min R ∈ { J P , K P } [ I s p e c ( I F = i F ; R , I P ) − I s p e c ( I F = i F ; I P ) ] 
pcbi.1004858.e009  (9) I s p e c ( I F = i F ; R , I P ) = ∑ r , i P p ( r , i P | i F ) log ( p ( r , i P , i F ) p ( r , i P ) p ( i F ) ) 
pcbi.1004858.e010  (10) I s p e c ( I F = i F ; I P ) = ∑ i P p ( i P | i F ) log ( p ( i P , i F ) p ( i P ) p ( i F ) ) 
pcbi.1004858.e011  (11) I I ( J P ; K P ; I F ) = I I ( { J , K } → I ) = M I ( J P ; K P | I F ) − M I ( J P ; K P ) 
pcbi.1004858.e012  (12) I g a i n ( I F ; I P , J 1 , P , … , J n − 1 , P ; J n , P ) = T E ( { J 1 , P , … , J n , P } → I F ) − T E ( { J 1 , P , … , J n − 1 , P } → I F ) ≥ Synergy ( { J 1 , … , J n } → I ) 
pcbi.1004858.e013  (13) p ( I ) = 1 1 + e − α I + β 
pcbi.1004858.e014  (14) p ( I = 0 ) = 0.01 
pcbi.1004858.e015  (15) p ( I = I c o n * N N e u r o n s ) = 0.5 
pcbi.1004858.e016  (16) p ( b ( t ) = 0 , i ) = 0.5 − 0.4 i − 1 N N e u r o n s − 1 
pcbi.1004858.e017  (17) p ( b ( t ) = 1 , 
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1371/journal.pone.0115764&format=json" | python3 -c "import sys,json;r=json.load(sys.stdin)['resultList']['result'][0];print(r.get('pmcid'),r['title'])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4275261/fullTextXML" -o t14.xml; python3 - <<'EOF'
import re
t=open('t14.xml').read()
b=t[t.find('<body'):t.find('</body>')]
b=re.sub(r'<disp-formula.*?</disp-formula>',lambda m:' [EQ: '+re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',m.group(0)))[:300]+'] ',b,flags=re.S)
b=re.sub(r'</p>','\n\n',b); b=re.sub(r'<title>','\n## ',b)
b=re.sub(r'<[^>]+>','',b)
open('t14.txt','w').write(b)
print(len(b))
EOF
grep -n -i -E "jitter|delay|bin size|sub-network|subnetwork|surrogate|time scale|timescale" t14.txt | head -80
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; grep -n "^## " t14.txt | head -60
```

```
<persisted-output>
Output too large (35KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/210349ad-6943-476f-a17d-3881b38a948a/tool-results/b1e5q7o6a.txt

Preview (first 2KB):
2:## IntroductionUnderstanding how large groups of neurons process and represent information in neural systems is a fundamental problem of neuroscience. One popular avenue to investigate the behaviors of large populations of neural sources is to analyze their connectivity [1]–[3]. Traditionally, these analyses have focused on individual networks that contain only one type of connection. However, recent work has shown the importance of interdependent networks [4]–[15]. These “multiplex networks” consist of multiple interdependent networks that share common nodes and possess different types of connections. In applications outside neuroscience, these previous studies frequently focused on the resilience properties of multiplex networks and on the properties of random multiplex networks.
26:## Results
27:## Electrophysiological PropertiesWe performed 25 cortical and 35 hippocampal recordings from mouse cortico-hippocampal organotypic cultures using a 512-electrode array with a sampling rate of 20 kHz. These recordings were pre-processed and spike sorted to yield spike times for each neuron (see Materials and Methods). The spiking activity of the neurons was dominated by bursts of activity (Fig. 1 A and S1 Fig). The neurons in the cortical recordings had a mean firing rate of 2.10 Hz, while the neurons in the hippocampal recordings had a mean firing rate of 1.21 Hz (Fig. 1 B). On average, we found 309.4 spike sorted neurons in each cortical recording (7735 total neurons) and 120.4 spike sorted neurons in each hippocampal recording (4214 total neurons) (Fig. 1 C). The cortical recordings yielded significantly more neurons, perhaps because the hippocampal tissues were physically smaller in size.
...
</persisted-output>
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'EOF'
t=open('t14.txt').read()
i=t.find('## Materials and Methods'); 
if i<0: i=t.find('Materials and Methods\n')
import re
j=[m.start() for m in re.finditer('## ',t)]
for k in j: print(k, t[k:k+60].replace('\n',' '))
EOF
```

```
1 ## IntroductionUnderstanding how large groups of neurons pro
7691 ## Results ## Electrophysiological PropertiesWe performed 25
7702 ## Electrophysiological PropertiesWe performed 25 cortical a
8618 ## Analysis time scales and basic data properties.(A) Exampl
9783 ## Transfer Entropy Analysis and Connectivity PropertiesAfte
12446 ## Long time scale connectivity was independent of short tim
16416 ## Firing rate and degree were correlated.(A) Neuron firing 
19131 ## Neuronal HubsWe next analyzed the proportion of the neuro
20606 ## A small and consistent percentage of neurons were found t
21356 ## Shared HubsIn addition to analyzing the proportion of neu
24422 ## Hub sharing was limited to adjacent time scales.(A) We cl
26336 ## Connection DistanceNext, we examined the relationship bet
27803 ## Physical distance between connected neurons increased wit
29308 ## Topology ResultsTo investigate the time scale dependent t
30618 ## Network modularity decreased with time scale.(A) Network 
32516 ## Network assortativity decreased with time scale.(A) Netwo
33317 ## Discussion ## Multiplex Networks Our analysis represents 
33331 ## Multiplex Networks Our analysis represents the first syst
35718 ## HubsIn this paper we have presented compelling evidence t
39138 ## Time Scales Importantly, the results of our analysis indi
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; python3 -c "
t=open('t14.txt').read(); print(t[60329:76000])"; grep -o '<table-wrap id=.*</table-wrap>' t14.xml | head -0; python3 - <<'EOF'
import re
t=open('/tmp/claude-1001/x','w') if False else None
EOF
```

```
## Transfer Entropy AnalysisTransfer Entropy (TE) was introduced by Schreiber to measure the influence of one time series (call it I) on another time series (call it J) [49]. In our case, I and J were binary spike trains for neurons I and J that contained 0 for the time bins when the neuron did not spike and 1 for the time bins when the neuron did spike. In its most basic form, the TE from I to J is given by:

 [EQ:  (1) ] By definition, the TE from neuron I to neuron I is zero, so no self connections existed in our analysis. The probabilities in Eqn. (1) are typically measured by counting all the instances of the possible combinations of spikes and no spikes in the jt, jt-1, and it-1 bins for all time bins. Note that this process requires the assumption that the time series are stationary and a sufficiently long recording is used to adequately approximate the probability distribution. Given the length of our recordings (1 hour), the fact that spontaneous activity was recorded, and that there are limited combinations of possible states (23) due to the binary nature of our time series, we feel TE can be used to generate meaningful results from our data.

Generally speaking, TE measures the information gained about the state of the target time series (jt) when the past state of a transmitting time series (it-1) is known, beyond the information provided by the past state of the target time series (jt-1) alone. TE has been used in several neuroscience applications [27], [45], [47], [50]–[56], [59], [60], [63], [64]. In its most basic form, TE is only able to capture interactions with delays falling within adjacent time bins. For instance, if it were the case that neuron J tended to spike ten time bins after neuron I spiked, the spikes would be so far apart that no interaction would be present in adjacent time bins and the basic TE expressed in Eqn. (1) would not detect an interaction. It would be possible to capture this ten time bin interaction by simply rebinning the 
[... 39 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'EOF'
import re
t=open('t14.xml').read()
for m in re.finditer(r'<disp-formula id="(.*?)">(.*?)</disp-formula>',t,re.S):
    s=re.sub(r'<[^>]+>',' ',m.group(2)); s=re.sub(r'\s+',' ',s)
    print(m.group(1), s[:600])
i=t.find('Time scales.')
print(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' | ',t[i-200:i+3000]))[:2500])
EOF
```

```
pone.0115764.e001  (1) 
pone.0115764.e002  (2) 
pone.0115764.e003  (3) 
pone.0115764.e004  (4) 
pone.0115764.e005  (5) 
pone.0115764.e006  (6) 
pone.0115764.e007  (7) 
pone.0115764.e008  (8) 
urons | in vitro | over time scales ranging from sub-milliseconds to seconds. | | | | Table 1 | | | Time scales. | | | | | | | | | | | | | | Time Scale | | Bin Size (ms) | | d | | Delay Window (bins) | | Delay Window (ms) | | Jitter Window (ms) | | | | | | 1 | | 1 | | 0 | | 0–3 | | 0.05–3 | | 7 | | | | 2 | | 1.6 | | 1 | | 1–4 | | 1.6–6.4 | | 11.2 | | | | 3 | | 3.5 | | 1 | | 1–4 | | 3.5–14 | | 24.5 | | | | 4 | | 7.5 | | 1 | | 1–4 | | 7.5–30 | | 52.5 | | | | 5 | | 16.15 | | 1 | | 1–4 | | 16.15–64.6 | | 113.05 | | | | 6 | | 34.8 | | 1 | | 1–4 | | 34.8–139.2 | | 243.6 | | | | 7 | | 75 | | 1 | | 1–4 | | 75–300 | | 525 | | | | 8 | | 161.6 | | 1 | | 1–4 | <td align="le
Shell cwd was reset to
```

**Agent calls Bash**

```bash
nproc; free -g; python3 -c "import fsspec,scipy,numpy,numba;print(scipy.__version__,numpy.__version__,numba.__version__)"; which uv; date -u
```

```
4
               total        used        free      shared  buff/cache   available
Mem:              15           1          12           0           2          14
Swap:              2           0           2
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import fsspec,scipy,numpy,numba;print(scipy.__version__,numpy.__version__,numba.__version__)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'fsspec'
/opt/hostedtoolcache/Python/3.13.18/x64/bin/uv
Fri Nov  6 11:02:35 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/001453-fouke-2025; cat entry.yaml requirements.in README.md; head -c 3000 omr.py; python3 -c "
import json;nb=json.load(open('reproduce_fouke_2025.ipynb'))
for c in nb['cells'][:6]: print(c['cell_type'],c.get('metadata'),''.join(c['source'])[:1500]); print('---')
print(len(nb['cells']))"
```

```
schema_version: 1
name: 001453-fouke-2025
type: reproduction
title: Optomotor swimming of zebrafish and Danionella cerebrum (Fouke et al. 2025)
description: Tests the freely swimming findings of Fouke, He, Loring and Naumann (2025) on dandiset
  001453, which holds the tracking data of 25 zebrafish and 12 Danionella cerebrum larvae during the
  optomotor protocol. It compares swimming speed, turning and angular acceleration between species
  and stimuli, the response to monocular stimuli, and how steady the swimming is. The imaging and
  head-fixed tail tracking of the paper's Figures 2 to 4 are not in the dandiset.
license: Apache-2.0
notebooks:
- path: reproduce_fouke_2025.ipynb
  title: Reproducing Fouke et al. (2025) from dandiset 001453
  runtime_minutes: 6
helpers:
- omr.py
related:
- id: dandi:001453/0.250518.1950
  relation: uses_data
- id: doi:10.1016/j.cub.2025.04.027
[... 200 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat attempts/001453-fouke-2025-01.yaml | head -150; ls questions | head; ls schemas
```

```
schema_version: 2
id: 001453-fouke-2025-01
dataset:
  archive: dandi
  id: "001453"
  version: 0.250518.1950
  doi: 10.48324/dandi.001453/0.250518.1950
paper: doi:10.1016/j.cub.2025.04.027
date: 2026-10-14
entry: 001453-fouke-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
    model: claude-opus-5-5
    protocol: pilot-5
  runner:
    platform: GitHub Actions
[... 144 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev && source dev/bin/activate && uv pip install -q numpy scipy fsspec aiohttp requests numba matplotlib pandas pyyaml 2>&1 | tail -2; python -c "import numba;print(numba.__version__)"
```

```
0.68.1
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source dev/bin/activate && time python - <<'EOF'
import fsspec, tarfile, io, scipy.io, numpy as np, time, pickle
url="https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-3/live/data.tar.gz"
t=time.time()
out={}
with fsspec.open(url, block_size=2**22).open() as f:
    with tarfile.open(fileobj=f, mode='r|gz') as tf:
        for m in tf:
            print(m.name, m.size, m.isfile())
            if m.isfile() and m.name.endswith('.mat'):
                b=tf.extractfile(m).read()
                out[m.name]=b
print(time.time()-t)
k=sorted(out)[0]
d=scipy.io.loadmat(io.BytesIO(out[k]),squeeze_me=True,struct_as_record=False)
print(d.keys())
data=d['data']; print(data._fieldnames)
for fn in data._fieldnames:
    v=getattr(data,fn); print(fn, type(v), getattr(v,'shape',None), v if np.isscalar(v) or isinstance(v,str) else '')
pickle.dump(out,open('raw.pkl','wb'))
EOF
```

```
data 0 False
data/DataSet1.mat 3208822 True
data/DataSet10.mat 5030486 True
data/DataSet11.mat 9518877 True
data/DataSet12.mat 11524054 True
data/DataSet13.mat 9373477 True
data/DataSet14.mat 14926760 True
data/DataSet15.mat 10731148 True
data/DataSet16.mat 14009822 True
data/DataSet17.mat 4660240 True
data/DataSet18.mat 10746530 True
data/DataSet19.mat 10490859 True
data/DataSet2.mat 6238509 True
data/DataSet20.mat 8255255 True
data/DataSet21.mat 4199562 True
data/DataSet22.mat 15718845 True
data/DataSet23.mat 10616491 True
data/DataSet24.mat 10797956 True
data/DataSet25.mat 6301660 True
data/DataSet3.mat 5894821 True
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source dev/bin/activate && python - <<'EOF'
import pickle, io, scipy.io, numpy as np
out=pickle.load(open('raw.pkl','rb'))
tot=0;tot100=0;rates=[];rates60=[]
import hashlib
for k in sorted(out,key=lambda s:int(s.split('DataSet')[1][:-4])):
    d=scipy.io.loadmat(io.BytesIO(out[k]),squeeze_me=True,struct_as_record=False)['data']
    sp=[np.atleast_1d(np.asarray(s,float)) for s in d.spikes]
    n=np.array([len(s) for s in sp]); L=d.recordinglength
    mx=max(s.max() for s in sp if len(s)); mn=min(s.min() for s in sp if len(s))
    srt=all(np.all(np.diff(s)>=0) for s in sp)
    dup=sum(np.any(np.diff(s)==0) for s in sp)
    tot+=len(sp); tot100+=(n>=100).sum(); rates+=list(n/(L/1000)); rates60+=list(n/3600)
    grid=np.mean([np.allclose(np.round(s*20)/20,s) for s in sp])
    print(k, d.recordingID, d.nNeurons, len(sp), L, round(mn,2), round(mx,1), n.min(), n.max(), (n<100).sum(), round(n.mean()/(L/1000),2), srt, dup, grid, np.nanmin(d.x),np.nanmax(d.x),np.nanmin(d.y),np.nanmax(d.y))
print(tot, tot100, tot/25, np.mean(rates), np.mean(rates60))
EOF
```

```
data/DataSet1.mat 2012-02-09-0 166 166 3600000 8005.85 3599995.6 105 113781 0 1.57 True 0 1.0 -960.1406931051221 1063.4536622991172 -607.535845841927 575.1834147581865
data/DataSet2.mat 2012-02-10-1 443 443 3600000 8001.9 3599983.5 100 116644 0 1.1 True 0 1.0 -1051.148835283946 1066.8127245977682 -561.5519473590799 599.5090748217121
data/DataSet3.mat 2012-02-11-0 99 99 3600000 8010.8 3599487.5 769 98955 0 5.12 True 0 1.0 -944.1787134040601 768.1917581369324 -474.3851165588479 589.0075962710691
data/DataSet4.mat 2012-02-12-0 98 98 3600000 8002.3 3598396.0 164 43409 0 1.81 True 0 1.0 -915.0 927.4510250561814 -395.0938196540657 602.4442158176241
data/DataSet5.mat 2012-02-13-1 367 367 3600000 8000.0 3599988.9 105 118238 0 0.77 True 0 1.0 -1009.0756317256785 1079.3988497070052 -559.3830749031258 603.028035837178
data/DataSet6.mat 2012-02-14-0 286 286 3600000 8002.25 3598476.6 115 57686 0 1.58 True 0 1.0 -1096.866896467198 981.6146515020312 -578.3839041215501 570.0873356810861
data/DataSet7.mat 2012-02-15-1 172 172 3600000 8000.05 3599401.1 115 25488 0 0.9 True 0 1.0 -953.0432078281373 945.0 -591.245180899977 585.3669432169646
data/DataSet8.mat 2012-02-16-1 191 191 3600000 8006.45 3598472.8 132 53838 0 2.36 True 0 1.0 -1002.9631834617686 895.9026400084706 -487.40735669610604 483.10661308519434
data/DataSet9.mat 2012-02-17-0 333 333 3600000 8000.0 3599969.2 105 78168 0 1.26 True 0 1.0 -1032.2479662967153 911.1937470758078 -557.9838732811606 598.0550757203004
data/DataSet10.mat 2012-02-18-0 368 368 3600000 8002.25 3599992.7 101 122251 0 1.11 True 0 1.0 -1056.0126548174135 982.701927211061 -563.7143012858637 550.0737422339383
data/DataSet11.mat 2013-01-02-0 243 243 3600000 1.35 3599997.9 105 136974 0 3.29 True 0 1.0 -945.0 1054.8892588440629 -552.1025156747686 563.3766284506494
data/DataSet12.mat 2013-01-03-0 346 346 3600000 0.1 3599998.3 136 192998 0 2.8 True 0 1.0 -1031.4214691246175 1025.2172277444913 -590.5781052120236 483.5719952217002
data/DataSet13.mat 2013-01-03-1 38
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls entries | head -30; ls entries | grep -i crcns; ls executed 2>/dev/null | head; sed -n 1,80p tools/entry.py | head -80
```

```
000003-senzai-2017
000004-chandravadia-2020
000005-yu-2016
000006-economo-2018
000008-scala-2021
000009-guo-2017
000010-li-2015
000011-li-2016
000013-hires-2015
000015-chen-2017
000019-bouchard-2013
000023-berg-2020
000034-buccino-2020
000035-scala-2021
000036-mayner-2022
000037-gillon-2023
000041-watson-2016
000044-grosmark-2016
000045-ibl-2021
000056-peyrache-2015
[... 102 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p entries/crcns-ssc-3-timme-2016
```

```
(Bash completed with no output)
```

**Agent calls Write**

```json
{
 "file_path": "entries/crcns-ssc-3-timme-2016/hdn.py",
 "content": "\"\"\"Loading and measures for CRCNS ssc-3, as used by Timme et al. (2016).\n\nTimme NM, Ito S, Myroshnychenko M, Nigam S, Shimono M, Yeh F-C, Hottowy P, Litke AM, Beggs JM\n(2016). High-degree neurons feed cortical computations. PLoS Comput Biol 12(5): e1004858,\ndoi:10.1371/journal.pcbi.1004858. Data: CRCNS ssc-3, doi:10.6080/K07D2S2F.\n\nThe data set is one archive, `ssc-3/live/data.tar.gz` in the public CRCNS bucket, holding 25\nMATLAB files (`data/DataSet<n>.mat`), each with a structure `data`: spike times per neuron in\nms (`spikes`), `nNeurons`, `recordinglength` (ms), neuron positions `x` and `y` (um) and a\n`recordingID`. CRCNS data sets are not versioned; the MD5 sum of the archive from the data set's\n`checksums.md5` is `DATA_MD5`, and `load_all` checks the bytes it streamed against it. The archive\nis streamed and decompressed in memory; nothing is written to disk.\n\nWhere each parameter comes from. \"Paper\" is the version of record (PMC4861348); its displayed\nequations, lost from the flattened text under paper/, were read from the version of record's\nJATS XML (Europe PMC). \"[44]\" is Timme et al. (2014), PLoS One 9: e115764 (PMC4275261), whose TE\nnetworks the paper says it reused (\"The complete procedure for the TE analysis is described in\n[44]\", Methods, Effective Connectivity Detection, paragraph 1; \"we used these same TE networks\",\nparagraph 4).\n\n- `TIME_SCALES`: bins of 1.6 and 3.5 ms with interaction delays of 1.6 to 6.4 and 3.5 to 14 ms\n  (paper, Effective Connectivity Detection, paragraph 4; [44], Table 1, time scales 2 and 3:\n  bin 1.6 ms, d = 1, delay window 1 to 4 bins, jitter window 11.2 ms; bin 3.5 ms, d = 1, delay\n  window 1 to 4 bins, jitter window 24.5 ms).\n- TE states ([44], Transfer Entropy Analysis, paragraph 3): binary spike trains; the past state\n  of both the sender and the receiver is the OR of two adjacent bins (\"a spike in either or both\n  time bins yielded an overall state of 1\"). Which two bins: [44]'s text writes i_{t-d} and\n  i_{t-d-1}, which for d = 1 gives bins t-1 and t-2 and delays of 0 to 2 bins; its Table 1 and\n  the paper give a delay window of 1 to 4 bins (1.6 to 6.4 ms), which bins t-2 and t-3 give\n  (a spike in bin t-3 and one in bin t are 2 to 4 bins apart, in t-2 and t 1 to 3 bins).\n  `PAST_BINS = (2, 3)` follows the stated delay window, the version both papers give in numbers\n  (an assumption, recorded in the attempt). The future state is one bin, t.\n- Normalized TE is TE over the entropy of the receiver's future state (paper, Eq 4).\n- Significance (paper, paragraph 5, and [44], paragraph 6 of Transfer Entropy Analysis): the\n  sender's spikes are jittered uniformly over a window of seven bins centred on each spike\n  (`JITTER_HALF_BINS = 3`); 5000 surrogates; significant when fewer than 5 surrogates give a TE\n  greater than the real one. [44] states that the jitter preserved the number of past states\n  equal to 1; `n(s'=1)` is held at its real value in each surrogate, as that sentence says. The\n  test stops early once 5 surrogates exceed the real TE, which cannot change the decision.\n- Sub-networks ([44], Topology Analysis - Sub-Networks, paragraph 2; paper, paragraph 5): 50\n  neurons drawn at random; neurons without a connection inside the group are replaced from the\n  pool until all have one; then only the k*N/2 = 75 strongest connections by normalized TE are\n  kept. `SUBNET_N`, `SUBNET_K`, `N_SUBNETS`.\n- PID (\"Williams and Beer\"; paper, Eqs 5 to 10): redundancy is I_min conditioned on I_P in the\n  form of Eq 8 (specific information of R together with I_P minus that of I_P alone, minimum over\n  the two sources, weighted by p(i_F)); unique terms are the bivariate TE minus the redundancy;\n  synergy is the TE of the pair minus the other three. Normalized by H(I_F) (paper, last\n  sentence of the paragraph after Eq 10). The past states of the two senders are the same\n  binned, OR'ed states as for the TE (\"The binning and delay methods for the PID multivariate TE\n  were identical to the bivariate TE analysis\").\n- Information gain (paper, Eq 12): TE of n senders jointly minus the TE of n - 1 of them,\n  averaged over the n choices of the sender left out; all combinations of n inputs or 100\n  sampled ones, whichever is fewer; n up to 6 (paper, Methods, paragraph after Eq 11).\n- Random seeds are standard choices; they cannot change a result beyond sampling noise.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport hashlib\nimport io\nimport math\nimport re\nimport tarfile\n\nimport fsspec\nimport numba as nb\nimport numpy as np\nimport scipy.io\n\nDATASET = \"ssc-3\"\nDATASET_DOI = \"10.6080/K07D2S2F\"\nDATASET_VERSION = \"unversioned\"\nDATA_URL = \"https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-3/live/data.tar.gz\"\nDATA_MD5 = \"1a5bd3d304c5442290a7c9c1f1b5def6\"   # ssc-3/live/checksums.md5\n\nTIME_SCALES = {\"1.6-6.4 ms\": 1.6, \"3.5-14 ms\": 3.5}   # bin size in ms ([44], Table 1)\nPAST_BINS = (2, 3)\nJITTER_HALF_BINS = 3\nN_SURROGATES = 5000\nMAX_EXCEED = 5            # significant when fewer than 5 of 5000 surrogates exceed (p < 0.001)\nSUBNET_N, SUBNET_K, N_SUBNETS = 50, 3, 500\n\n\n# ---------------------------------------------------------------- loading\n\ndef load_all():\n    \"\"\"Stream data.tar.gz and return one dict per recording, in data set order (1 to 25).\"\"\"\n    md5 = hashlib.md5()\n\n    class Hashing(io.RawIOBase):\n        def __init__(self, f):\n            self.f = f\n\n        def readable(self):\n            return True\n\n        def readinto(self, b):\n            chunk = self.f.read(len(b))\n            md5.update(chunk)\n            b[:len(chunk)] = chunk\n            return len(chunk)\n\n    raw = {}\n    with fsspec.open(DATA_URL, block_size=2**22).open() as f:\n        stream = io.BufferedReader(Hashing(f), buffer_size=2**22)\n        with tarfile.open(fileobj=stream, mode=\"r|gz\") as tf:\n            for m in tf:\n                if m.isfile() and m.name.endswith(\".mat\"):\n                    raw[m.name] = tf.extractfile(m).read()\n        while stream.read(2**22):\n            pass\n    recs = []\n    for name in sorted(raw, key=lambda s: int(re.search(r\"DataSet(\\d+)\", s).group(1))):\n        d = scipy.io.loadmat(io.BytesIO(raw[name]), squeeze_me=True, struct_as_record=False)[\"data\"]\n        recs.append({\n            \"name\": re.search(r\"(DataSet\\d+)\", name).group(1),\n            \"recording_id\": str(d.recordingID),\n            \"n_neurons_field\": int(d.nNeurons),\n            \"length_ms\": float(d.recordinglength),\n            \"timescale\": str(d.timescale),\n            \"sampling\": str(d.samplingfrequency),\n            \"spikes\": [np.atleast_1d(np.asarray(s, dtype=float)) for s in d.spikes],\n            \"x\": np.asarray(d.x, float), \"y\": np.asarray(d.y, float),\n        })\n    return recs, md5.hexdigest()\n\n\ndef bin_trains(spikes, bin_ms, length_ms):\n    \"\"\"Binary spike trains as sorted unique bin indices, and the number of bins.\"\"\"\n    T = int(math.ceil(length_ms / bin_ms))\n    out = nb.typed.List()\n    for s in spikes:\n        b = np.unique(np.floor(s / bin_ms).astype(np.int64))\n        out.append(b[(b >= 0) & (b < T)])\n    return out, T\n\n\n# ---------------------------------------------------------------- TE network\n\n@nb.njit(cache=True)\ndef _xlogy(n, num, den, N):\n    if n <= 0:\n        return 0.0\n    return n / N * math.log2(num / den)\n\n\n@nb.njit(cache=True)\ndef te_from_counts(N, R1, P1, RP, S1, a, b, c):\n    \"\"\"TE (bits) from the counts of the 2x2x2 table of receiver future r, receiver past r' and\n    sender past s'. R1 = n(r), P1 = n(r'), RP = n(r, r'), S1 = n(s'), a = n(r, s'),\n    b = n(r', s'), c = n(r, r', s').\"\"\"\n    te = 0.0\n    for rp in range(2):\n        for sp in range(2):\n            # n(r', s') and n(r=1, r', s')\n            if rp == 1 and sp == 1:\n                n_ps, n1 = b, c\n            elif rp == 1 and sp == 0:\n                n_ps, n1 = P1 - b, RP - c\n            elif rp == 0 and sp == 1:\n                n_ps, n1 = S1 - b, a - c\n            else:\n                n_ps, n1 = N - P1 - S1 + b, (R1 - RP) - (a - c)\n            n_p = P1 if rp == 1 else N - P1\n            n_p1 = RP if rp == 1 else R1 - RP\n            n0 = n_ps - n1\n            if n1 > 0:\n                te += n1 / N * math.log2((n1 / n_ps) / (n_p1 / n_p))\n            if n0 > 0:\n                te += n0 / N * math.log2((n0 / n_ps) / ((n_p - n_p1) / n_p))\n    return te\n\n\n@nb.njit(cache=True)\ndef _rng(state):\n    # xorshift64*; state is a one-element uint64 array\n    x = state[0]\n    x ^= x >> np.uint64(12)\n    x ^= x << np.uint64(25)\n    x ^= x >> np.uint64(27)\n    state[0] = x\n    return (x * np.uint64(2685821657736338717)) >> np.uint64(33)\n\n\n@nb.njit(parallel=True, cache=True)\ndef te_network(trains, T, n_surr, max_exceed, seed):\n    \"\"\"TE from every sender (row) to every receiver (column), its normalized value, the number of\n    surrogates run and the number that exceeded the real TE.\"\"\"\n    n = len(trains)\n    p0, p1 = 2, 3                      # PAST_BINS\n    J = 3                              # JITTER_HALF_BINS\n    t0 = 3                             # first bin with a full past\n    N = T - t0\n    te = np.zeros((n, n))\n    nte = np.zeros((n, n))\n    ran = np.zeros((n, n), np.int32)\n    exceed = np.zeros((n, n), np.int32)\n    # sender past counts n(s'=1)\n    S1 = np.zeros(n, np.int64)\n    for s in range(n):\n        tr = trains[s]\n        last = -10\n        cnt = 0\n        for k in range(len(tr)):\n            for d in (p0, p1):\n                t = tr[k] + d\n                if t >= t0 and t < T and t > last:\n                    cnt += 1\n                    last = t\n        S1[s] = cnt\n    for r in nb.prange(n):\n        rF = np.zeros(T + 8, np.uint8)\n        rP = np.zeros(T + 8, np.uint8)\n        rel = np.zeros(T + 8, np.uint8)\n        stamp = np.zeros(T + 8, np.int32)\n        tr = trains[r]\n        for k in range(len(tr)):\n            rF[tr[k]] = 1\n            for d in (p0, p1):\n                if tr[k] + d < T:\n                    rP[tr[k] + d] = 1\n        R1 = 0\n        P1 = 0\n        RP = 0\n        for t in range(t0, T):\n            R1 += rF[t]\n            P1 += rP[t]\n            RP += rF[t] & rP[t]\n        HF = 0.0\n        q = R1 / N\n        if 0 < q < 1:\n            HF = -(q * math.log2(q) + (1 - q) * math.log2(1 - q))\n        # a sender spike at bin p, jittered by u in [-J, J], covers t = p + u + 2 and p + u + 3:\n        # bins p - 1 to p + 6. It can change a, b or c only if rF or rP is 1 somewhere there.\n        for t in range(T):\n            if rF[t] or rP[t]:\n                lo = max(t - (p1 + J), 0)\n                hi = min(t - (p0 - J), T - 1)\n                for p in range(lo, hi + 1):\n                    rel[p] = 1\n        st = 0\n        for s in range(n):\n            if s == r:\n                continue\n            ts = trains[s]\n            relp = np.empty(len(ts), np.int64)\n            m = 0\n            for k in range(len(ts)):\n                if rel[ts[k]]:\n                    relp[m] = ts[k]\n                    m += 1\n            # real counts\n            st += 1\n            a = 0\n            b = 0\n            c = 0\n            for k in range(m):\n                for d in (p0, p1):\n                    t = relp[k] + d\n                    if t >= t0 and t < T and stamp[t] != st:\n                        stamp[t] = st\n                        a += rF[t]\n                        b += rP[t]\n                        c += rF[t] & rP[t]\n            real = te_from_counts(N, R1, P1, RP, S1[s], a, b, c)\n            te[s, r] = real\n            nte[s, r] = real / HF if HF > 0 else 0.0\n            state = np.empty(1, np.uint64)\n            state[0] = np.uint64(seed) * np.uint64(1000003) + np.uint64(s * 100003 + r + 1) * np.uint64(7919)\n            for _ in range(10):\n                _rng(state)\n            nex = 0\n            k_run = 0\n            for it in range(n_surr):\n                st += 1\n                a = 0\n                b = 0\n                c = 0\n                for k in range(m):\n                    u = np.int64(_rng(state) % np.uint64(2 * J + 1)) - J\n                    for d in (p0, p1):\n                        t = relp[k] + u + d\n                        if t >= t0 and t < T and stamp[t] != st:\n                            stamp[t] = st\n                            a += rF[t]\n                            b += rP[t]\n                            c += rF[t] & rP[t]\n                k_run += 1\n                if te_from_counts(N, R1, P1, RP, S1[s], a, b, c) > real:\n                    nex += 1\n                    if nex >= max_exceed:\n                        break\n            ran[s, r] = k_run\n            exceed[s, r] = nex\n    return te, nte, ran, exceed\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && source dev/bin/activate && cat > devload.py <<'EOF'
import pickle, io, scipy.io, numpy as np, sys, re
sys.path.insert(0,'entries/crcns-ssc-3-timme-2016')
import hdn
def load(i):
    out=pickle.load(open('/tmp/claude-1001/raw.pkl','rb')) if False else pickle.load(open(__import__('os').environ['TMPDIR']+'/raw.pkl','rb'))
    d=scipy.io.loadmat(io.BytesIO(out[f'data/DataSet{i}.mat']),squeeze_me=True,struct_as_record=False)['data']
    return [np.atleast_1d(np.asarray(s,float)) for s in d.spikes], float(d.recordinglength)
EOF
python - <<'EOF'
import time, numpy as np
from devload import *
sp,L=load(1)
tr,T=hdn.bin_trains(sp,1.6,L)
t=time.time(); out=hdn.te_network(tr[:20],T,50,5,1); print('compile+small',time.time()-t)
t=time.time(); te,nte,ran,ex=hdn.te_network(tr,T,5000,5,1); print('full',time.time()-t)
sig=(ex<5)&(ran>0)
np.fill_diagonal(sig,False)
print(sig.sum(), sig.sum()/(166*165), ran.sum(), ran[sig].mean())
print(np.percentile(te[sig],[1,50,99]), np.percentile(nte[sig],[1,50,99]))
EOF
```

```
entries/crcns-ssc-3-timme-2016/hdn.py:216: NumbaTypeSafetyWarning: unsafe cast from uint64 to int64. Precision may be lost.
  tr = trains[r]
compile+small 6.026580810546875
full 15.126330137252808
2933 0.10708287696239503 15676468 5000.0
[1.44913161e-08 2.93267946e-07 3.93921755e-04] [1.02670375e-05 6.64733155e-05 1.65695424e-02]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source dev/bin/activate && python - <<'EOF' 2>&1 | grep -v Warn
import time, numpy as np
from devload import *
for i,bs in [(20,1.6),(20,3.5)]:
    sp,L=load(i)
    tr,T=hdn.bin_trains(sp,bs,L)
    t=time.time(); te,nte,ran,ex=hdn.te_network(tr,T,5000,5,1); 
    n=len(sp); sig=(ex<5)&(ran>0); np.fill_diagonal(sig,False)
    print(i,bs,n,time.time()-t, sig.sum(), sig.sum()/(n*(n-1)), ran.sum())
EOF
```

```
20 1.6 534 102.0682909488678 29693 0.10432433192093372 157988485
20 3.5 534 297.0623185634613 20455 0.07186724849098101 113946995
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/crcns-ssc-3-timme-2016 && python3 - <<'EOF'
src=open('hdn.py').read()
start=src.index('@nb.njit(parallel=True, cache=True)\ndef te_network')
new='''@nb.njit(parallel=True, cache=True)
def te_network(trains, T, n_surr, max_exceed, seed):
    """TE from every sender (row) to every receiver (column), its normalized value, the number of
    surrogates run and the number that exceeded the real TE.

    In a surrogate each sender spike moves by u, uniform on -3..3 bins. A spike can change the
    counts a, b, c only if the receiver's future or past state is 1 somewhere in the bins it can
    cover; only those spikes are jittered explicitly. A spike more than 7 bins from any other such
    spike covers bins no other spike can reach, so its contribution for each u is tabulated once;
    spikes closer together are jittered together and their covered bins merged (the OR of the
    past state)."""
    n = len(trains)
    p0, p1 = 2, 3                      # PAST_BINS
    J = 3                              # JITTER_HALF_BINS
    W = 2 * J + 1
    t0 = 3                             # first bin with a full past
    N = T - t0
    te = np.zeros((n, n))
    nte = np.zeros((n, n))
    ran = np.zeros((n, n), np.int32)
    exceed = np.zeros((n, n), np.int32)
    S1 = np.zeros(n, np.int64)
    for s in range(n):
        tr = trains[s]
        last = -10
        cnt = 0
        for k in range(len(tr)):
            for d in (p0, p1):
                t = tr[k] + d
                if t >= t0 and t < T and t > last:
                    cnt += 1
                    last = t
        S1[s] = cnt
    for r in nb.prange(n):
        rF = np.zeros(T + 16, np.uint8)
        rP = np.zeros(T + 16, np.uint8)
        rel = np.zeros(T + 16, np.uint8)
        stamp = np.zeros(T + 16, np.int32)
        tr = trains[r]
        for k in range(len(tr)):
            rF[tr[k]] = 1
            for d in (p0, p1):
                if tr[k] + d < T:
                    rP[tr[k] + d] = 1
        R1 = 0
        P1 = 0
        RP = 0
        for t in range(t0, T):
            R1 += rF[t]
            P1 += rP[t]
            RP += rF[t] & rP[t]
        HF = 0.0
        q = R1 / N
        if 0 < q < 1:
            HF = -(q * math.log2(q) + (1 - q) * math.log2(1 - q))
        for t in range(t0, T):
            if rF[t] or rP[t]:
                lo = max(t - (p1 + J), 0)
                hi = min(t - (p0 - J), T - 1)
                for p in range(lo, hi + 1):
                    rel[p] = 1
        st = 0
        for s in range(n):
            if s == r:
                continue
            ts = trains[s]
            relp = np.empty(len(ts), np.int64)
            m = 0
            for k in range(len(ts)):
                if rel[ts[k]]:
                    relp[m] = ts[k]
                    m += 1
            # real counts
            st += 1
            a = 0
            b = 0
            c = 0
            for k in range(m):
                for d in (p0, p1):
                    t = relp[k] + d
                    if t >= t0 and t < T and stamp[t] != st:
                        stamp[t] = st
                        a += rF[t]
                        b += rP[t]
                        c += rF[t] & rP[t]
            real = te_from_counts(N, R1, P1, RP, S1[s], a, b, c)
            te[s, r] = real
            nte[s, r] = real / HF if HF > 0 else 0.0
            # isolated spikes: table of packed (a, b, c) per u; others: explicit groups
            tab = np.empty((m, W), np.int64)
            n_iso = 0
            base = np.int64(0)
            grp = np.empty(m + 1, np.int64)
            gp = np.empty(m, np.int64)
            n_g = 0
            n_gp = 0
            k = 0
            while k < m:
                e = k
                while e + 1 < m and relp[e + 1] - relp[e] <= 2 * J + 1:
                    e += 1
                if e == k:
                    p = relp[k]
                    same = True
                    for ui in range(W):
                        v = np.int64(0)
                        for d in (p0, p1):
                            t = p + ui - J + d
                            if t >= t0 and t < T:
                                v += np.int64(rF[t]) + (np.int64(rP[t]) << 20) + (np.int64(rF[t] & rP[t]) << 40)
                        tab[n_iso, ui] = v
                        if v != tab[n_iso, 0]:
                            same = False
                    if same:
                        base += tab[n_iso, 0]
                    else:
                        n_iso += 1
                else:
                    grp[n_g] = n_gp
                    n_g += 1
                    for kk in range(k, e + 1):
                        gp[n_gp] = relp[kk]
                        n_gp += 1
                k = e + 1
            grp[n_g] = n_gp
            state = np.empty(1, np.uint64)
            state[0] = np.uint64(seed) * np.uint64(1000003) + np.uint64(s * 100003 + r + 1) * np.uint64(7919)
            for _ in range(10):
                _rng(state)
            nex = 0
            k_run = 0
            for it in range(n_surr):
                tot = base
                for i in range(n_iso):
                    tot += tab[i, np.int64(_rng(state) % np.uint64(W))]
                a = tot & 0xFFFFF
                b = (tot >> 20) & 0xFFFFF
                c = tot >> 40
                for g in range(n_g):
                    st += 1
                    for kk in range(grp[g], grp[g + 1]):
                        u = np.int64(_rng(state) % np.uint64(W)) - J
                        for d in (p0, p1):
                            t = gp[kk] + u + d
                            if t >= t0 and t < T and stamp[t] != st:
                                stamp[t] = st
                                a += rF[t]
                                b += rP[t]
                                c += rF[t] & rP[t]
                k_run += 1
                if te_from_counts(N, R1, P1, RP, S1[s], a, b, c) > real:
                    nex += 1
                    if nex >= max_exceed:
                        break
            ran[s, r] = k_run
            exceed[s, r] = nex
    return te, nte, ran, exceed
'''
open('hdn.py','w').write(src[:start]+new)
EOF
cd $TMPDIR && source dev/bin/activate && python - <<'EOF' 2>&1 | grep -v Warn
import time, numpy as np
from devload import *
sp,L=load(1)
tr,T=hdn.bin_trains(sp,1.6,L)
t=time.time(); te,nte,ran,ex=hdn.te_network(tr,T,5000,5,1); print('full',time.time()-t)
t=time.time(); te,nte,ran,ex=hdn.te_network(tr,T,5000,5,1); print('full',time.time()-t)
sig=(ex<5)&(ran>0); np.fill_diagonal(sig,False)
print(sig.sum(), ran.sum())
EOF
```

```
tr = trains[r]
full 20.420644283294678
full 13.652388095855713
2936 15674713
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source dev/bin/activate && python - <<'EOF' 2>&1 | grep -v Warn
import numpy as np
from devload import *
sp,L=load(1)
tr,T=hdn.bin_trains(sp,1.6,L)
# pick receiver 0..5, compute rel and stats for each sender
for r in range(3):
    rF=np.zeros(T+16,bool); rF[tr[r]]=True
    rP=np.zeros(T+16,bool); rP[tr[r]+2]=True; rP[tr[r]+3]=True
    ev=np.flatnonzero(rF|rP)
    rel=np.zeros(T+16,bool)
    for d in range(-1,7): rel[np.clip(ev-d,0,T-1)]=True
    ms=[];iso=[]
    for s in range(len(tr)):
        p=tr[s][rel[tr[s]]]
        if len(p)==0: ms.append(0);iso.append(0);continue
        dd=np.diff(p); close=np.zeros(len(p),bool); close[1:]|=dd<=7; close[:-1]|=dd<=7
        ms.append(len(p)); iso.append((~close).sum())
    ms=np.array(ms);iso=np.array(iso)
    print(r,len(tr[r]), ms.mean(), ms.max(), iso.sum()/ms.sum())
EOF
```

```
0 19330 831.1987951807229 19330 0.856985483298183
1 684 55.0722891566265 1164 0.8136075257055349
2 3717 316.3433734939759 5562 0.8082950888351456
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/crcns-ssc-3-timme-2016 && python3 - <<'EOF'
src=open('hdn.py').read()
old_rng=src[src.index('@nb.njit(cache=True)\ndef _rng'):src.index('@nb.njit(parallel=True, cache=True)')]
new_rng='''@nb.njit(cache=True)
def _rng(state):
    # xorshift64*; state is a one-element uint64 array; returns 64 random bits
    x = state[0]
    x ^= x >> np.uint64(12)
    x ^= x << np.uint64(25)
    x ^= x >> np.uint64(27)
    state[0] = x
    return x * np.uint64(2685821657736338717)


@nb.njit(cache=True)
def _u7(bits32):
    # uniform integer 0..6 from 32 random bits (multiply-shift; bias below 2e-9)
    return np.int64((bits32 * np.uint64(7)) >> np.uint64(32))


'''
src=src.replace(old_rng,new_rng)
src=src.replace('''            for _ in range(10):
                _rng(state)''','''            for _ in range(10):
                _rng(state)
            mask = np.uint64(0xFFFFFFFF)''')
src=src.replace('''                for i in range(n_iso):
                    tot += tab[i, np.int64(_rng(state) % np.uint64(W))]''','''                for i in range(0, n_iso - 1, 2):
                    x = _rng(state)
                    tot += tab[i, _u7(x & mask)] + tab[i + 1, _u7(x >> np.uint64(32))]
                if n_iso % 2 == 1:
                    tot += tab[n_iso - 1, _u7(_rng(state) & mask)]''')
src=src.replace('''                        u = np.int64(_rng(state) % np.uint64(W)) - J''','''                        u = _u7(_rng(state) & mask) - J''')
open('hdn.py','w').write(src)
EOF
grep -n "W)" hdn.py; cd $TMPDIR && source dev/bin/activate && python - <<'EOF' 2>&1 | grep -v Warn
import time, numpy as np
from devload import *
sp,L=load(1)
tr,T=hdn.bin_trains(sp,1.6,L)
t=time.time(); te,nte,ran,ex=hdn.te_network(tr,T,5000,5,1); print('full',time.time()-t)
t=time.time(); te,nte,ran,ex=hdn.te_network(tr,T,5000,5,1); print('full',time.time()-t)
sig=(ex<5)&(ran>0); np.fill_diagonal(sig,False)
print(sig.sum(), ran.sum())
EOF
```

```
280:            tab = np.empty((m, W), np.int64)
295:                    for ui in range(W):
  tr = trains[r]
full 18.51385474205017
full 10.769820928573608
2937 15679867
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source dev/bin/activate && python - <<'EOF' 2>&1 | grep -v Warn
import time, numpy as np
from devload import *
sp,L=load(1)
tr,T=hdn.bin_trains(sp,1.6,L)
for ns in [1,500]:
    t=time.time(); te,nte,ran,ex=hdn.te_network(tr,T,ns,5,1); print(ns,time.time()-t, ran.sum())
EOF
```

```
1 0.5949456691741943 27390
500 2.123544216156006 2205539
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source dev/bin/activate && python - <<'EOF' 2>&1 | grep -v Warn
import time, numpy as np, pickle
from devload import *
res={}
T0=time.time()
for bs in [1.6,3.5]:
  for i in range(1,26):
    sp,L=load(i)
    tr,T=hdn.bin_trains(sp,bs,L)
    t=time.time(); te,nte,ran,ex=hdn.te_network(tr,T,1000,1,1)
    sig=(ex<1)&(ran>0); np.fill_diagonal(sig,False)
    res[(bs,i)]=(te,nte,ran,ex)
    print(bs,i,len(sp),round(time.time()-t,1), sig.sum(), round(sig.sum()/(len(sp)*(len(sp)-1)),3), flush=True)
pickle.dump(res,open('te1000.pkl','wb'))
print('total',time.time()-T0)
EOF
```

```
Exit code 143
Command timed out after 1h 0m 0s
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && source dev/bin/activate && timeout 300 python -u - <<'EOF' 2>&1 | grep --line-buffered -v Warn
import time, numpy as np, pickle
from devload import *
for bs in [1.6,3.5]:
  for i in [1,7]:
    sp,L=load(i)
    tr,T=hdn.bin_trains(sp,bs,L)
    t=time.time(); te,nte,ran,ex=hdn.te_network(tr,T,1000,1,1)
    sig=(ex<1)&(ran>0); np.fill_diagonal(sig,False)
    print(bs,i,len(sp),round(time.time()-t,1), sig.sum(), ran.sum(), flush=True)
EOF
```

```
Fri Nov  6 12:15:52 UTC 2026
1.6 1 166 2.4 2931 3117951
1.6 7 172 6.7 3498 3745460
3.5 1 166 10.4 2109 2347382
3.5 7 172 22.3 2950 3285796
Shell cwd was reset to
```

**Agent calls Read**

```json
{
 "file_path": "entries/crcns-ssc-3-timme-2016/hdn.py",
 "offset": 230,
 "limit": 120
}
```

```
230	        for k in range(len(tr)):
231	            rF[tr[k]] = 1
232	            for d in (p0, p1):
233	                if tr[k] + d < T:
234	                    rP[tr[k] + d] = 1
235	        R1 = 0
236	        P1 = 0
237	        RP = 0
238	        for t in range(t0, T):
239	            R1 += rF[t]
240	            P1 += rP[t]
241	            RP += rF[t] & rP[t]
242	        HF = 0.0
243	        q = R1 / N
244	        if 0 < q < 1:
245	            HF = -(q * math.log2(q) + (1 - q) * math.log2(1 - q))
246	        for t in range(t0, T):
247	            if rF[t] or rP[t]:
248	                lo = max(t - (p1 + J), 0)
249	                hi = min(t - (p0 - J), T - 1)
[... 100 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-ssc-3-timme-2016 && python3 - <<'EOF'
src=open('hdn.py').read()
src=src.replace("def te_network(trains, T, n_surr, max_exceed, seed):","def te_network(trains, T, n_surr, max_exceed, seed, exact_max):")
old='''            mask = np.uint64(0xFFFFFFFF)
            nex = 0
            k_run = 0
            for it in range(n_surr):'''
new='''            mask = np.uint64(0xFFFFFFFF)
            nex = 0
            k_run = 0
            if n_iso + n_gp > exact_max:
                # Gaussian null: the jittered counts are a sum of many independent spike
                # contributions; take their exact mean and covariance (isolated spikes) plus
                # those of the merged groups from 200 joint draws, and draw (a, b, c) from the
                # normal with these moments.
                mu = np.zeros(3)
                cov = np.zeros((3, 3))
                mu[0] = base & 0xFFFFF
                mu[1] = (base >> 20) & 0xFFFFF
                mu[2] = base >> 40
                v = np.zeros(3)
                for i in range(n_iso):
                    m1 = np.zeros(3)
                    m2 = np.zeros((3, 3))
                    for ui in range(W):
                        x0 = tab[i, ui]
                        v[0] = x0 & 0xFFFFF
                        v[1] = (x0 >> 20) & 0xFFFFF
                        v[2] = x0 >> 40
                        for p_ in range(3):
                            m1[p_] += v[p_] / W
                            for q_ in range(3):
                                m2[p_, q_] += v[p_] * v[q_] / W
                    for p_ in range(3):
                        mu[p_] += m1[p_]
                        for q_ in range(3):
                            cov[p_, q_] += m2[p_, q_] - m1[p_] * m1[q_]
                if n_g > 0:
                    K = 200
                    g1 = np.zeros(3)
                    g2 = np.zeros((3, 3))
                    for it in range(K):
                        v[:] = 0.0
                        for g in range(n_g):
                            st += 1
                            for kk in range(grp[g], grp[g + 1]):
                                u = _u7(_rng(state) & mask) - J
                                for d in (p0, p1):
                                    t = gp[kk] + u + d
                                    if t >= t0 and t < T and stamp[t] != st:
                                        stamp[t] = st
                                        v[0] += rF[t]
                                        v[1] += rP[t]
                                        v[2] += rF[t] & rP[t]
                        for p_ in range(3):
                            g1[p_] += v[p_] / K
                            for q_ in range(3):
                                g2[p_, q_] += v[p_] * v[q_] / K
                    for p_ in range(3):
                        mu[p_] += g1[p_]
                        for q_ in range(3):
                            cov[p_, q_] += (g2[p_, q_] - g1[p_] * g1[q_]) * K / (K - 1)
                # matrix square root through the eigendecomposition (cov may be singular)
                w, V = np.linalg.eigh(cov)
                L = np.zeros((3, 3))
                for p_ in range(3):
                    sw = math.sqrt(w[p_]) if w[p_] > 0 else 0.0
                    for q_ in range(3):
                        L[q_, p_] = V[q_, p_] * sw
                z = np.zeros(3)
                for it in range(n_surr):
                    for p_ in range(3):
                        u1 = ((_rng(state) >> np.uint64(11)) + np.uint64(1)) * (1.0 / 9007199254740993.0)
                        u2 = (_rng(state) >> np.uint64(11)) * (1.0 / 9007199254740992.0)
                        z[p_] = math.sqrt(-2.0 * math.log(u1)) * math.cos(2.0 * math.pi * u2)
                    av = mu[0] + L[0, 0] * z[0] + L[0, 1] * z[1] + L[0, 2] * z[2]
                    bv = mu[1] + L[1, 0] * z[0] + L[1, 1] * z[1] + L[1, 2] * z[2]
                    cv = mu[2] + L[2, 0] * z[0] + L[2, 1] * z[1] + L[2, 2] * z[2]
                    a = max(np.int64(round(av)), 0)
                    b = max(np.int64(round(bv)), 0)
                    c = min(max(np.int64(round(cv)), 0), a, b, RP)
                    a = min(a, R1)
                    b = min(b, P1, S1[s])
                    a = min(a, S1[s])
                    c = min(c, a, b)
                    k_run += 1
                    if te_from_counts(N, R1, P1, RP, S1[s], a, b, c) > real:
                        nex += 1
                        if nex >= max_exceed:
                            break
                ran[s, r] = k_run
                exceed[s, r] = nex
                continue
            for it in range(n_surr):'''
assert old in src
src=src.replace(old,new)
open('hdn.py','w').write(src)
EOF
cd $TMPDIR && source dev/bin/activate && timeout 600 python -u - <<'EOF' 2>&1 | grep --line-buffered -v Warn
import time, numpy as np, pickle
from devload import *
for i in [1,7]:
    sp,L=load(i)
    tr,T=hdn.bin_trains(sp,1.6,L)
    t=time.time(); te,nte,ran,ex=hdn.te_network(tr,T,5000,5,1,10**9); t1=time.time()-t
    t=time.time(); te2,nte2,ran2,ex2=hdn.te_network(tr,T,5000,5,1,50); t2=time.time()-t
    s1=(ex<5); s2=(ex2<5); np.fill_diagonal(s1,False); np.fill_diagonal(s2,False)
    print(i,round(t1,1),round(t2,1), s1.sum(), s2.sum(), (s1&s2).sum(), (s1&~s2).sum(), (~s1&s2).sum(), flush=True)
EOF
```

```
tr = trains[r]
1 26.6 2.3 2937 2946 2933 4 13
7 32.4 3.9 3530 3541 3516 14 25
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && source dev/bin/activate && timeout 1800 python -u - <<'EOF' 2>&1 | grep --line-buffered -v -i warn | grep --line-buffered -v "tr = trains"
import time, numpy as np, pickle
from devload import *
res={}
T0=time.time()
for bs in [1.6,3.5]:
  for i in range(1,26):
    sp,L=load(i)
    tr,T=hdn.bin_trains(sp,bs,L)
    t=time.time(); out=hdn.te_network(tr,T,5000,5,1,50)
    ex=out[3]; sig=ex<5; np.fill_diagonal(sig,False)
    res[(bs,i)]=out
    print(bs,i,len(sp),round(time.time()-t,1), sig.sum(), round(sig.sum()/(len(sp)*(len(sp)-1)),3), flush=True)
  pickle.dump(res,open('te_h.pkl','wb'))
print('total',time.time()-T0)
EOF
```

```
Exit code 143
Fri Nov  6 12:18:33 UTC 2026
1.6 1 166 2.5 2946 0.108
1.6 2 443 6.6 17944 0.092
1.6 3 99 17.8 1255 0.129
1.6 4 98 2.4 327 0.034
1.6 5 367 4.4 21659 0.161
1.6 6 286 13.7 11153 0.137
1.6 7 172 4.0 3541 0.12
1.6 8 191 22.4 2335 0.064
1.6 9 333 10.5 22247 0.201
1.6 10 368 6.5 31863 0.236
1.6 11 243 36.4 4277 0.073
1.6 12 346 50.2 6312 0.053
1.6 13 381 19.4 2676 0.018
1.6 14 304 97.8 6671 0.072
1.6 15 206 58.7 3852 0.091
1.6 16 594 37.6 39751 0.113
1.6 17 435 9.3 10490 0.056
1.6 18 180 95.6 4820 0.15
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && source dev/bin/activate && timeout 400 python -u - <<'EOF' 2>&1 | grep --line-buffered -v -i warn | grep --line-buffered -v "tr = trains"
import time, numpy as np
from devload import *
sp,L=load(14)
tr,T=hdn.bin_trains(sp,1.6,L)
hdn.te_network(tr[:5],T,10,5,1,50)
t=time.time(); out=hdn.te_network(tr,T,1,5,1,10**9); print('setup only', time.time()-t)
n=np.array([len(x) for x in tr]); print(np.sort(n)[-10:], n.sum())
EOF
```

```
Fri Nov  6 12:48:42 UTC 2026
setup only 4.909043312072754
[ 71046  72874  91068  91336  93622  95091 101506 102607 132096 139356] 4568840
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/crcns-ssc-3-timme-2016 && sed -i 's/                    K = 200/                    K = 50/; s/those of the merged groups from 200 joint draws/those of the merged groups from 50 joint draws/' hdn.py && grep -n "K = 50\|50 joint" hdn.py; cd $TMPDIR && source dev/bin/activate && python - <<'EOF'
import pickle,numpy as np
r=pickle.load(open('te_h.pkl','rb')); print(len(r), list(r)[:3])
EOF
```

```
326:                # those of the merged groups from 50 joint draws, and draw (a, b, c) from the
351:                    K = 50
25 [(1.6, 1), (1.6, 2), (1.6, 3)]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/crcns-ssc-3-timme-2016 && cat >> hdn.py <<'EOF'


def significant(exceed):
    """Significant connections: fewer than MAX_EXCEED surrogates above the real TE."""
    sig = exceed < MAX_EXCEED
    np.fill_diagonal(sig, False)
    return sig


# ---------------------------------------------------------------- sub-networks

def subnetworks(sig, nte, rng, n_sub=N_SUBNETS, size=SUBNET_N, k=SUBNET_K, max_tries=10**5):
    """Sub-networks as in [44] (Topology Analysis - Sub-Networks): `size` neurons at random;
    a neuron with no significant connection (either direction) to the others is replaced by a
    random neuron from the pool until all have one; then the k*size/2 strongest connections by
    normalized TE are kept. Returns a list of (neurons, senders, receivers) in recording indices,
    and the number of restarts."""
    n = sig.shape[0]
    und = sig | sig.T
    out = []
    restarts = 0
    n_keep = k * size // 2
    while len(out) < n_sub:
        if restarts > max_tries:
            break
        perm = rng.permutation(n)
        group, pool = list(perm[:size]), list(perm[size:])
        ok = False
        for _ in range(10 * size):
            g = np.array(group)
            deg = und[np.ix_(g, g)].sum(1)
            lone = np.flatnonzero(deg == 0)
            if len(lone) == 0:
                ok = True
                break
            # replace one unconnected neuron by a pool neuron connected to the group, if any
            cand = [p for p in pool if und[p, g].any()]
            if not cand:
                break
            new = cand[rng.integers(len(cand))]
            old = lone[rng.integers(len(lone))]
            pool.remove(new)
            pool.append(group[old])
            group[old] = new
        if not ok:
            restarts += 1
            continue
        g = np.array(group)
        s_idx, r_idx = np.nonzero(sig[np.ix_(g, g)])
        w = nte[g[s_idx], g[r_idx]]
        order = np.argsort(-w, kind="stable")[:n_keep]
        out.append((g, g[s_idx[order]], g[r_idx[order]]))
    return out, restarts


# ---------------------------------------------------------------- PID and multivariate TE

def past_sets(trains, T):
    """For each neuron the sorted bins t (t0 <= t < T) whose past state is 1."""
    out = nb.typed.List()
    for tr in trains:
        s = np.unique(np.concatenate([tr + d for d in PAST_BINS]))
        out.append(s[(s >= 3) & (s < T)])
    return out


@nb.njit(cache=True)
def _receiver_arrays(tr, T):
    rF = np.zeros(T + 8, np.uint8)
    rP = np.zeros(T + 8, np.uint8)
    for k in range(len(tr)):
        rF[tr[k]] = 1
        for d in (2, 3):
            if tr[k] + d < T:
                rP[tr[k] + d] = 1
    base = np.zeros((2, 2), np.int64)
    for t in range(3, T):
        base[rF[t], rP[t]] += 1
    return rF, rP, base


@nb.njit(cache=True)
def _te_table(n):
    """TE (bits) and H(I_F) from counts n[iF, iP, x]."""
    nf = n.shape[2]
    N = n.sum()
    te = 0.0
    nP = np.zeros(2)
    nFP = np.zeros((2, 2))
    for f in range(2):
        for p in range(2):
            for x in range(nf):
                nP[p] += n[f, p, x]
                nFP[f, p] += n[f, p, x]
    for p in range(2):
        for x in range(nf):
            nPX = n[0, p, x] + n[1, p, x]
            for f in range(2):
                v = n[f, p, x]
                if v > 0:
                    te += v / N * math.log2(v * nP[p] / (nPX * nFP[f, p]))
    q = (nFP[1, 0] + nFP[1, 1]) / N
    H = 0.0
    if 0 < q < 1:
        H = -(q * math.log2(q) + (1 - q) * math.log2(1 - q))
    return te, H


@nb.njit(cache=True)
def _joint_counts(rF, rP, base, sets, idx, code, touched):
    """Counts n[iF, iP, x] with x the joint past state of the senders sets[idx[i]] (bit i)."""
    m = len(idx)
    n = np.zeros((2, 2, 1 << m))
    nt = 0
    for i in range(m):
        s = sets[idx[i]]
        for k in range(len(s)):
            t = s[k]
            if code[t] == 0:
                touched[nt] = t
                nt += 1
            code[t] |= 1 << i
    for f in range(2):
        for p in range(2):
            n[f, p, 0] = base[f, p]
    for k in range(nt):
        t = touched[k]
        f = rF[t]
        p = rP[t]
        n[f, p, code[t]] += 1
        n[f, p, 0] -= 1
        code[t] = 0
    return n


@nb.njit(cache=True)
def pid_from_table(n):
    """Williams-Beer PID of the multivariate TE {J, K} -> I from counts n[iF, iP, x], x = j + 2k
    (paper, Eqs 5 to 10). Returns synergy, redundancy, unique J, unique K, TE(J), TE(K),
    TE({J,K}), H(I_F), all in bits."""
    N = n.sum()
    p = n / N
    pJ = np.zeros((2, 2, 2))
    pK = np.zeros((2, 2, 2))
    for f in range(2):
        for q in range(2):
            for x in range(4):
                pJ[f, q, x & 1] += p[f, q, x]
                pK[f, q, x >> 1] += p[f, q, x]
    teJK, H = _te_table(n)
    teJ, _ = _te_table(pJ * N)
    teK, _ = _te_table(pK * N)
    pF = np.zeros(2)
    pFP = np.zeros((2, 2))
    pPp = np.zeros(2)
    for f in range(2):
        for q in range(2):
            for x in range(4):
                pF[f] += p[f, q, x]
                pFP[f, q] += p[f, q, x]
                pPp[q] += p[f, q, x]
    red = 0.0
    for f in range(2):
        if pF[f] <= 0:
            continue
        # I_spec(I_F = f; I_P)
        isp = 0.0
        for q in range(2):
            if pFP[f, q] > 0:
                isp += pFP[f, q] / pF[f] * math.log2(pFP[f, q] / (pPp[q] * pF[f]))
        best = 1e300
        for src in range(2):
            pr = pJ if src == 0 else pK
            v = 0.0
            for q in range(2):
                for x in range(2):
                    pj = pr[f, q, x]
                    if pj > 0:
                        v += pj / pF[f] * math.log2(pj / ((pr[0, q, x] + pr[1, q, x]) * pF[f]))
            v -= isp
            if v < best:
                best = v
        red += pF[f] * best
    uJ = teJ - red
    uK = teK - red
    syn = teJK - red - uJ - uK
    return syn, red, uJ, uK, teJ, teK, teJK, H


@nb.njit(parallel=True, cache=True)
def pid_triples(trains, sets, T, recv, js, ks):
    """PID of every triple (js[i], ks[i]) -> recv[i]; triples must be sorted by receiver.
    Returns an array (n, 8) of pid_from_table's outputs."""
    n = len(recv)
    out = np.zeros((n, 8))
    starts = [0]
    for i in range(1, n):
        if recv[i] != recv[i - 1]:
            starts.append(i)
    starts.append(n)
    ng = len(starts) - 1
    st = np.array(starts)
    for g in nb.prange(ng):
        r = recv[st[g]]
        rF, rP, base = _receiver_arrays(trains[r], T)
        code = np.zeros(T + 8, np.int64)
        touched = np.empty(T + 8, np.int64)
        idx = np.empty(2, np.int64)
        for i in range(st[g], st[g + 1]):
            idx[0] = js[i]
            idx[1] = ks[i]
            tab = _joint_counts(rF, rP, base, sets, idx, code, touched)
            res = pid_from_table(tab)
            for k in range(8):
                out[i, k] = res[k]
    return out


@nb.njit(cache=True)
def _te_drop(n, m, drop):
    """TE of all senders but `drop` from the joint table n over m senders."""
    nn = np.zeros((2, 2, 1 << (m - 1)))
    for x in range(1 << m):
        lo = x & ((1 << drop) - 1)
        hi = x >> (drop + 1)
        y = lo | (hi << drop)
        for f in range(2):
            for q in range(2):
                nn[f, q, y] += n[f, q, x]
    te, _ = _te_table(nn)
    return te


@nb.njit(parallel=True, cache=True)
def info_gain(trains, sets, T, recv, combos, n_in):
    """Information gain (paper, Eq 12) for each combination of senders: TE of all n_in senders
    minus the TE without one of them, averaged over the n_in senders left out; in bits and
    normalized by H(I_F). `combos` is (k, n_in), rows grouped by `recv`."""
    k = combos.shape[0]
    out = np.zeros((k, 2))
    for i in nb.prange(k):
        r = recv[i]
        rF, rP, base = _receiver_arrays(trains[r], T)
        code = np.zeros(T + 8, np.int64)
        touched = np.empty(T + 8, np.int64)
        tab = _joint_counts(rF, rP, base, sets, combos[i], code, touched)
        te_all, H = _te_table(tab)
        g = 0.0
        if n_in == 1:
            g = te_all
        else:
            for d in range(n_in):
                g += (te_all - _te_drop(tab, n_in, d)) / n_in
        out[i, 0] = g
        out[i, 1] = g / H if H > 0 else 0.0
    return out
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
src=open('hdn.py').read()
i=src.index('@nb.njit(parallel=True, cache=True)\ndef info_gain')
src=src[:i]+'''@nb.njit(parallel=True, cache=True)
def info_gain(trains, sets, T, recv, combos, n_in):
    """Information gain (paper, Eq 12) for each combination of senders: TE of all n_in senders
    minus the TE without one of them, averaged over the n_in senders left out; in bits and
    normalized by H(I_F). `combos` is (k, n_in), rows sorted by `recv`."""
    k = combos.shape[0]
    out = np.zeros((k, 2))
    starts = [0]
    for i in range(1, k):
        if recv[i] != recv[i - 1]:
            starts.append(i)
    starts.append(k)
    st = np.array(starts)
    for g in nb.prange(len(st) - 1):
        r = recv[st[g]]
        rF, rP, base = _receiver_arrays(trains[r], T)
        code = np.zeros(T + 8, np.int64)
        touched = np.empty(T + 8, np.int64)
        for i in range(st[g], st[g + 1]):
            tab = _joint_counts(rF, rP, base, sets, combos[i], code, touched)
            te_all, H = _te_table(tab)
            v = 0.0
            if n_in == 1:
                v = te_all
            else:
                for d in range(n_in):
                    v += (te_all - _te_drop(tab, n_in, d)) / n_in
            out[i, 0] = v
            out[i, 1] = v / H if H > 0 else 0.0
    return out
'''
open('hdn.py','w').write(src)
EOF
cd $TMPDIR && source dev/bin/activate && python - <<'EOF' 2>&1 | grep -v -i warn | grep -v "tr = trains"
import numpy as np, sys
sys.path.insert(0,'entries/crcns-ssc-3-timme-2016')
import hdn
# Table 1 check: rows ordered IF,IP,JP,KP binary 0000..1111
cols={'none':[1/16]*16}
syn=[1/8,0,0,1/8,0,1/8,0,0,0,1/8,1/8,0,1/8,0,0,1/8]
sr=[0.0548,0.0548,0.0548,0,0.0548,0.0548,0.0548,0,0,0,0,0.3357,0,0,0,0.3357]
for name,col in [('syn',syn),('synred',sr)]:
    col=np.array(col)/sum(col)
    n=np.zeros((2,2,4))
    for row in range(16):
        f,p,j,k=(row>>3)&1,(row>>2)&1,(row>>1)&1,row&1
        n[f,p,j+2*k]=col[row]*1e6
    print(name, hdn.pid_from_table(n))
EOF
```

```
syn (0.8571428571428572, 0.10784107173763832, 2.7755575615628914e-17, 2.7755575615628914e-17, 0.10784107173763835, 0.10784107173763835, 0.9649839288804956, 0.9852281360342515)
synred (0.45687953430884554, 0.45674840078737744, -1.1102230246251565e-16, -1.1102230246251565e-16, 0.45674840078737733, 0.45674840078737733, 0.9136279350962228, 0.9136279350962226)
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source dev/bin/activate && python - <<'EOF' 2>&1 | grep -v -i warn | grep -v "tr = trains"
import numpy as np, sys
sys.path.insert(0,'entries/crcns-ssc-3-timme-2016')
import hdn
t=open('paper/10.1371-journal.pcbi.1004858.txt').read()
i=t.find('Synergistic and Redundant Interaction\n\n0\n'); s=t[i+len('Synergistic and Redundant Interaction\n\n'):]
tok=s.split('\n\n')[:16*12]
rows=[tok[k*12:(k+1)*12] for k in range(16)]
for r in rows: print(r)
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd entries/crcns-ssc-3-timme-2016 && cat >> hdn.py <<'EOF'


# ---------------------------------------------------------------- per-recording analysis

N_FULL_TRIPLES = 3000      # reading (f): triples sampled per recording and time scale (time limit)
N_GAIN_RECEIVERS = 30      # Fig 6: receivers sampled per recording and time scale (time limit)
N_GAIN_COMBOS = 20         # Fig 6: combinations per receiver and n (paper: 100; time limit)
MAX_INPUTS = 6             # Fig 6: up to six inputs (paper)


def _triples_from_edges(senders, receivers):
    """All (receiver, sender j, sender k) with j < k both sending to the receiver."""
    out = []
    by_r = {}
    for s, r in zip(senders, receivers):
        by_r.setdefault(int(r), []).append(int(s))
    for r, ins in by_r.items():
        ins = sorted(ins)
        for a in range(len(ins)):
            for b in range(a + 1, len(ins)):
                out.append((r, ins[a], ins[b]))
    return out


def analyse_recording(trains, T, sig, nte, seed):
    """Sub-networks, synergy of every triple (readings s and f) and information gains."""
    rng = np.random.default_rng(seed)
    sets = past_sets(trains, T)
    subs, restarts = subnetworks(sig, nte, rng)
    # reading (s): triples inside each sub-network, degrees counted inside it
    rows = []
    for si, (g, s_e, r_e) in enumerate(subs):
        indeg = {}
        outdeg = {}
        for s, r in zip(s_e, r_e):
            indeg[int(r)] = indeg.get(int(r), 0) + 1
            outdeg[int(s)] = outdeg.get(int(s), 0) + 1
        for r, j, k in _triples_from_edges(s_e, r_e):
            rows.append((si, r, j, k, indeg[r], outdeg[j], outdeg[k]))
    sub_tr = np.array(rows, dtype=np.int64).reshape(-1, 7)
    # reading (f): triples of the full network, sampled
    s_all, r_all = np.nonzero(sig)
    indeg_f = sig.sum(0)
    outdeg_f = sig.sum(1)
    w = np.array([indeg_f[r] * (indeg_f[r] - 1) / 2 for r in range(sig.shape[0])], float)
    n_full_total = int(w.sum())
    full = set()
    if n_full_total <= N_FULL_TRIPLES:
        full = set(_triples_from_edges(s_all, r_all))
    else:
        while len(full) < N_FULL_TRIPLES:
            r = int(rng.choice(len(w), p=w / w.sum()))
            ins = np.flatnonzero(sig[:, r])
            j, k = sorted(rng.choice(ins, 2, replace=False))
            full.add((r, int(j), int(k)))
    full_tr = np.array(sorted(full), dtype=np.int64).reshape(-1, 3)
    # PID of every distinct triple
    keys = set(map(tuple, sub_tr[:, 1:4].tolist())) | set(map(tuple, full_tr.tolist()))
    keys = np.array(sorted(keys), dtype=np.int64).reshape(-1, 3)
    pid = pid_triples(trains, sets, T, keys[:, 0], keys[:, 1], keys[:, 2]) if len(keys) else np.zeros((0, 8))
    syn = {tuple(k): (p[0] / p[7] if p[7] > 0 else 0.0) for k, p in zip(keys.tolist(), pid)}
    # information gain, reading (f)
    cand = np.flatnonzero(indeg_f >= 1)
    pick = np.sort(rng.choice(cand, min(N_GAIN_RECEIVERS, len(cand)), replace=False)) if len(cand) else cand
    gains = {}
    for n_in in range(1, MAX_INPUTS + 1):
        recv, combos = [], []
        for r in pick:
            ins = np.flatnonzero(sig[:, r])
            if len(ins) < n_in:
                continue
            if math.comb(len(ins), n_in) <= N_GAIN_COMBOS:
                import itertools
                cs = [list(c) for c in itertools.combinations(ins, n_in)]
            else:
                cs = [sorted(rng.choice(ins, n_in, replace=False)) for _ in range(N_GAIN_COMBOS)]
            recv += [r] * len(cs)
            combos += cs
        if not recv:
            continue
        g = info_gain(trains, sets, T, np.array(recv, np.int64), np.array(combos, np.int64), n_in)
        recv = np.array(recv)
        gains[n_in] = {int(r): (g[recv == r, 0].mean(), g[recv == r, 1].mean()) for r in np.unique(recv)}
    return {"subs": subs, "restarts": restarts, "sub_triples": sub_tr, "full_triples": full_tr,
            "n_full_total": n_full_total, "syn": syn, "pid": (keys, pid), "gains": gains,
            "indeg_f": indeg_f, "outdeg_f": outdeg_f}
EOF
cd $TMPDIR && source dev/bin/activate && timeout 900 python -u - <<'EOF' 2>&1 | grep --line-buffered -v -i warn | grep --line-buffered -v "tr = trains"
import time, numpy as np, pickle, sys
from devload import *
r=pickle.load(open('te_h.pkl','rb'))
for i in [1,14,16]:
    sp,L=load(i); tr,T=hdn.bin_trains(sp,1.6,L)
    te,nte,ran,ex=r[(1.6,i)]; sig=hdn.significant(ex)
    t=time.time(); a=hdn.analyse_recording(tr,T,sig,nte,i); print(i, time.time()-t, a['restarts'], len(a['sub_triples']), len(a['syn']), a['n_full_total'], {k:len(v) for k,v in a['gains'].items()}, flush=True)
    st=a['sub_triples']; s=np.array([a['syn'][(x[1],x[2],x[3])] for x in st])
    from scipy import stats
    print(stats.spearmanr(st[:,4],s)[0], stats.spearmanr(np.r_[st[:,5],st[:,6]],np.r_[s,s])[0], np.median(s))
EOF
```

```
1 11.083602666854858 0 53513 8883 55203 {1: 30, 2: 27, 3: 27, 4: 25, 5: 25, 6: 25}
-0.07634596693815425 -0.04601345216272862 0.00029500293590728504
14 22.047210454940796 0 33367 21625 101533 {1: 30, 2: 30, 3: 30, 4: 30, 5: 29, 6: 29}
-0.16749518506341826 0.2720555672348807 0.015902561924118774
16 12.526717901229858 0 51673 47845 2775434 {1: 30, 2: 30, 3: 30, 4: 30, 5: 30, 6: 30}
-0.12867399025670145 -0.07269303983008886 0.00020104590117326002
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat > $TMPDIR/mknb.py <<'PYEOF'
import nbformat as nbf
nb = nbf.v4.new_notebook()
C = []
def md(s, tags=None):
    c = nbf.v4.new_markdown_cell(s.strip("\n"))
    if tags: c.metadata["tags"] = tags
    C.append(c)
def code(s, tags=None):
    c = nbf.v4.new_code_cell(s.strip("\n"))
    if tags: c.metadata["tags"] = tags
    C.append(c)

md(r'''
# Reproducing Timme et al. (2016) from CRCNS ssc-3

**Paper.** Timme NM, Ito S, Myroshnychenko M, Nigam S, Shimono M, Yeh F-C, Hottowy P, Litke AM,
Beggs JM (2016). High-degree neurons feed cortical computations. *PLoS Comput Biol* 12(5): e1004858.
[doi:10.1371/journal.pcbi.1004858](https://doi.org/10.1371/journal.pcbi.1004858). The claims file
was written from the version of record (PMC4861348, Europe PMC full text). Its displayed
equations, missing from that flattened text, were read from the version of record's JATS XML.
The TE procedure the paper reuses is that of its reference [44], Timme et al. (2014), PLoS One 9:
e115764 (PMC4275261).

**Data set.** [CRCNS ssc-3](https://doi.org/10.6080/K07D2S2F), `ssc-3/live/data.tar.gz` in the public
CRCNS bucket, streamed and decompressed in memory. CRCNS data sets are not versioned, so the version
is recorded as `unversioned`; the paper cites the data set by its DOI and no version, and this is
the only copy the bucket holds (`ssc-3/live/`, no `old/`). The MD5 sum of the archive, from the data
set's `checksums.md5`, is `1a5bd3d304c5442290a7c9c1f1b5def6`; the loading cell checks the streamed
bytes against it. The archive holds 25 MATLAB files, one per recording.

**Claims.**

| Claim | Tested here |
|---|---|
| data-recordings | tested |
| fig4ac-te-lognormal | tested |
| fig4bd-heavy-tailed-degree | tested |
| fig4bd-out-tail-longer | tested |
| fig5a-in-degree-uncorrelated | tested |
| fig5b-out-degree-positive | tested |
| fig5ab-correlations-beyond-null | tested |
| fig5cd-pooled-trends | tested |
| fig6-information-gain-not-rising | tested, with sampled receivers and combinations |
| table1-pid-examples | tested (no recorded data) |
| fig7c-degree-modified-rule-matches | blocked: not run within the run's time |
| fig7b-connectivity-patterns | blocked: not run within the run's time |
| fig7d-degree-rule-highest-conditioned-mi | blocked: not run within the run's time |
| figs1-larger-model | blocked: not run within the run's time |

How the TE networks are built (bins, past states, jitter, sub-networks) and where each choice comes
from is in the docstring of `hdn.py`. The significance test uses the paper's 5000 jittered
surrogates per pair, with one approximation needed to fit the time limit: for pairs whose jitter
moves more than 50 relevant sender spikes, the jittered counts are drawn from a normal distribution
with their exact moments, in place of jittering every spike. The data check section compares the
two on two recordings.
''')

code(r'''
import itertools
import math
import time
import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
from scipy.optimize import curve_fit

import hdn

warnings.filterwarnings("ignore")
pd.set_option("display.width", 200)
pd.set_option("display.max_rows", 200)
started = time.time()
recs, md5 = hdn.load_all()
print(f"CRCNS {hdn.DATASET} ({hdn.DATASET_DOI}), version {hdn.DATASET_VERSION}: {len(recs)} recordings "
      f"streamed in {time.time() - started:.0f} s")
print("MD5 of the streamed archive:", md5, "| checksums.md5:", hdn.DATA_MD5, "| equal:", md5 == hdn.DATA_MD5)
''')

md("## Data check")
code(r'''
rows = []
for r in recs:
    n = np.array([len(s) for s in r["spikes"]])
    allsp = np.concatenate(r["spikes"])
    rows.append({
        "file": r["name"], "recording_id": r["recording_id"], "nNeurons": r["n_neurons_field"],
        "trains": len(r["spikes"]), "length_ms": r["length_ms"], "first_ms": allsp.min(), "last_ms": allsp.max(),
        "spikes_min": n.min(), "spikes_max": n.max(), "under_100": int((n < 100).sum()),
        "sorted": all(np.all(np.diff(s) >= 0) for s in r["spikes"]),
        "on_50us_grid": bool(np.allclose(np.round(allsp * 20) / 20, allsp)),
        "x_um": f"{np.nanmin(r['x']):.0f} to {np.nanmax(r['x']):.0f}", "y_um": f"{np.nanmin(r['y']):.0f} to {np.nanmax(r['y']):.0f}",
        "timescale": r["timescale"], "sampling": r["sampling"]})
info = pd.DataFrame(rows)
print(info.to_string(index=False))
print("\nnNeurons equals the number of spike trains in every file:", bool((info.nNeurons == info.trains).all()))
print("Spike times sorted within every train:", bool(info.sorted.all()), "| on the 0.05 ms grid (20 kHz):", bool(info.on_50us_grid.all()))
print("Every spike within [0, recordinglength]:", bool(((info.first_ms >= 0) & (info.last_ms <= info.length_ms)).all()))
print("Recording lengths (ms):", info.length_ms.value_counts().to_dict())
print("Recording dates:", sorted(set(r[:10] for r in info.recording_id)))
# recordings deposited twice: identical spike trains in two files
sig = {}
for r in recs:
    for k, s in enumerate(r["spikes"]):
        sig.setdefault((len(s), round(float(s[0]), 2), round(float(s[-1]), 2)), []).append((r["name"], k))
shared = [v for v in sig.values() if len({f for f, _ in v}) > 1]
print("Spike trains with the same count, first and last spike in two files:", len(shared))
print("Distinct recording IDs:", info.recording_id.nunique(), "of", len(info))
''', tags=["sanity"])
md(r'''
The descriptor says the data are in ms at 20 kHz, with recordings of "approximately 1 hour"
(3600000 ms "for most data sets") and positions in um with the origin at the array's centre on a
2 mm by 1 mm array. The values agree: spike times sit on the 0.05 ms grid, positions span about
-1100 to 1100 um in x and -600 to 600 um in y, 24 recordings last 3600000 ms and one (DataSet19)
2887498 ms (48 min). The first ten recordings have no spike in their first 8 s. No spike train
appears in two files and the 25 recording IDs are distinct, so no recording is deposited twice.
The files hold spike times only: there are no trials or other data streams whose clock could
differ from the spikes', so the clock check of the protocol does not apply.
''')

md(r'''
## data-recordings

> The analysis used 25 recordings of somatosensory cortex cultures, with 7735 neurons in total after
> removing neurons with fewer than 100 spikes in the 60 min recording, an average of 309.4 neurons
> per recording and an average firing rate of 2.10 Hz.
''')
code(r'''
counts = np.array([len(r["spikes"]) for r in recs])
spk = [np.array([len(s) for s in r["spikes"]]) for r in recs]
keep = [n >= 100 for n in spk]
rate_len = np.concatenate([n / (r["length_ms"] / 1000) for n, r in zip(spk, recs)])
rate_60 = np.concatenate([n / 3600.0 for n in spk])
print("Recordings:", len(recs))
print("Neurons as deposited:", counts.sum(), "| mean per recording:", round(counts.mean(), 1))
print("Neurons with 100 or more spikes:", sum(k.sum() for k in keep), "(the deposit already applies the threshold)")
print(f"Mean rate per neuron, (a) spikes over each recording's length: {rate_len.mean():.3f} Hz; "
      f"(b) spikes over 60 min: {rate_60.mean():.3f} Hz")
print(f"Rates range from {rate_len.min():.3f} to {rate_len.max():.1f} Hz")
''', tags=["claim:data-recordings"])

md(r'''
## TE networks

TE from every neuron to every other, at both time scales, with the jitter test (`hdn.te_network`).
The first cell checks the normal approximation against the full jitter of every spike on two
recordings at the 1.6 ms bins: the decision of the test is compared pair by pair.
''')
code(r'''
check = []
for name in ["DataSet1", "DataSet7"]:
    r = next(x for x in recs if x["name"] == name)
    trains, T = hdn.bin_trains(r["spikes"], 1.6, r["length_ms"])
    t = time.time()
    exact = hdn.significant(hdn.te_network(trains, T, hdn.N_SURROGATES, hdn.MAX_EXCEED, 1, 10**9)[3])
    t_exact = time.time() - t
    t = time.time()
    approx = hdn.significant(hdn.te_network(trains, T, hdn.N_SURROGATES, hdn.MAX_EXCEED, 1, 50)[3])
    t_approx = time.time() - t
    check.append({"recording": name, "pairs": exact.size - len(exact), "significant_exact": int(exact.sum()),
                  "significant_approx": int(approx.sum()), "both": int((exact & approx).sum()),
                  "exact_only": int((exact & ~approx).sum()), "approx_only": int((~exact & approx).sum()),
                  "seconds_exact": round(t_exact), "seconds_approx": round(t_approx)})
print(pd.DataFrame(check).to_string(index=False))
''')
code(r'''
nets = {}
rows = []
t_all = time.time()
for scale, bin_ms in hdn.TIME_SCALES.items():
    for i, r in enumerate(recs):
        trains, T = hdn.bin_trains(r["spikes"], bin_ms, r["length_ms"])
        t = time.time()
        te, nte, ran, exceed = hdn.te_network(trains, T, hdn.N_SURROGATES, hdn.MAX_EXCEED, 1, 50)
        sig = hdn.significant(exceed)
        nets[scale, r["name"]] = {"trains": trains, "T": T, "te": te, "nte": nte, "sig": sig}
        n = len(trains)
        rows.append({"scale": scale, "recording": r["name"], "neurons": n, "connections": int(sig.sum()),
                     "density": sig.sum() / (n * (n - 1)), "expected_by_chance": round(0.001 * n * (n - 1)),
                     "mean_total_degree": 2 * sig.sum() / n, "seconds": round(time.time() - t)})
net_info = pd.DataFrame(rows)
print(net_info.round(3).to_string(index=False))
print(f"\n{time.time() - t_all:.0f} s")
print(net_info.groupby("scale")[["connections", "density", "mean_total_degree"]].describe().round(3).T.to_string())
''')
code(r'''
res = {}
t_all = time.time()
for (scale, name), net in nets.items():
    seed = 1000 * list(hdn.TIME_SCALES).index(scale) + int(name.replace("DataSet", ""))
    res[scale, name] = hdn.analyse_recording(net["trains"], net["T"], net["sig"], net["nte"], seed)
print(f"sub-networks, synergy and information gains in {time.time() - t_all:.0f} s")
summ = pd.DataFrame([{"scale": s, "recording": n, "subnetworks": len(a["subs"]), "restarts": a["restarts"],
                      "subnet_triples": len(a["sub_triples"]), "full_triples_total": a["n_full_total"],
                      "full_triples_used": len(a["full_triples"])} for (s, n), a in res.items()])
print(summ.to_string(index=False))
''')

md(r'''
## fig4ac-te-lognormal

> The significant TE connection weights, raw and normalized, are roughly log-normally distributed at
> both time scales and vary over several orders of magnitude.

Reading (f) uses every significant connection; reading (s) the connections kept in the 500
sub-networks, each counted once per recording.
''')
code(r'''
def lognorm_pmf(x, a, mu, s):
    # paper, Eq 21: alpha / (sigma sqrt(2 pi)) exp(-(log10 x - mu)^2 / (2 sigma^2))
    return a / (s * np.sqrt(2 * np.pi)) * np.exp(-(np.log10(x) - mu) ** 2 / (2 * s ** 2))

def fit_r2(x, y):
    try:
        p, _ = curve_fit(lognorm_pmf, x, y, p0=[y.max() * 0.5, np.log10(x[np.argmax(y)]), 0.5], maxfev=20000)
        pred = lognorm_pmf(x, *p)
        return 1 - ((y - pred) ** 2).sum() / ((y - y.mean()) ** 2).sum(), p
    except RuntimeError:
        return np.nan, None

rows, curves = [], {}
for scale in hdn.TIME_SCALES:
    for reading in ["f", "s"]:
        for measure in ["te", "nte"]:
            vals = []
            for r in recs:
                net = nets[scale, r["name"]]
                if reading == "f":
                    v = net[measure][net["sig"]]
                else:
                    e = set()
                    for g, s_e, r_e in res[scale, r["name"]]["subs"]:
                        e.update(zip(s_e.tolist(), r_e.tolist()))
                    e = np.array(sorted(e))
                    v = net[measure][e[:, 0], e[:, 1]]
                vals.append(v[v > 0])
            pooled = np.concatenate(vals)
            edges = np.logspace(np.log10(pooled.min()), np.log10(pooled.max()), 101)
            centers = np.sqrt(edges[:-1] * edges[1:])
            pmfs = np.array([np.histogram(v, edges)[0] / len(v) for v in vals])
            r2_avg, p = fit_r2(centers, pmfs.mean(0))
            r2_each = np.array([fit_r2(centers, y)[0] for y in pmfs])
            p1, p99 = np.percentile(pooled, [1, 99])
            spread_each = np.array([np.percentile(v, 99) / np.percentile(v, 1) for v in vals])
            curves[scale, reading, measure] = (centers, pmfs, p)
            rows.append({"scale": scale, "reading": reading, "measure": measure, "n_values": len(pooled),
                         "R2_average": r2_avg, "R2_rec_median": np.nanmedian(r2_each), "R2_rec_min": np.nanmin(r2_each),
                         "p1": p1, "p99": p99, "p99/p1": p99 / p1, "p99/p1_rec_min": spread_each.min(),
                         "min": pooled.min(), "max": pooled.max(), "mu_log10": p[1] if p is not None else np.nan,
                         "sigma_log10": p[2] if p is not None else np.nan})
fig4 = pd.DataFrame(rows)
print(fig4.to_string(index=False, float_format=lambda v: f"{v:.3g}"))
print("\nCriterion (each reading): R2 >= 0.9 and p99/p1 >= 100 for both scales and both measures")
for reading in ["f", "s"]:
    sub = fig4[fig4.reading == reading]
    print(f"  reading ({reading}):", bool(((sub.R2_average >= 0.9) & (sub["p99/p1"] >= 100)).all()))
''', tags=["claim:fig4ac-te-lognormal"])
code(r'''
fig, axes = plt.subplots(2, 4, figsize=(16, 6))
for ax, key in zip(axes.flat, curves):
    centers, pmfs, p = curves[key]
    ax.semilogx(centers, pmfs.mean(0), "k.", ms=3)
    if p is not None:
        ax.semilogx(centers, lognorm_pmf(centers, *p), "r-")
    ax.set_title(" ".join(key), fontsize=9)
plt.tight_layout(); plt.show()
print("Every bin of the 100 log-spaced bins is shown; values span the full range of each panel's x axis.")
''', tags=["claim:fig4ac-te-lognormal"])

md(r'''
## fig4bd-heavy-tailed-degree

> The total degree distributions are heavy-tailed, with many more high-degree neurons than in random
> networks with the same numbers of neurons and connections.

Random networks place the same number of directed connections uniformly among the same neurons:
under (f) 100 random networks per recording, under (s) one per sub-network (50 neurons, 75
connections). The threshold is the 99.9th percentile of the random total degrees of the recording
(f) or of all its random sub-networks (s).
''')
code(r'''
rng = np.random.default_rng(41)

def random_degrees(n, e, rng):
    flat = rng.choice(n * (n - 1), e, replace=False)
    s = flat // (n - 1); r = flat % (n - 1); r = r + (r >= s)
    return np.bincount(s, minlength=n), np.bincount(r, minlength=n)

deg = {}
rows = []
for scale in hdn.TIME_SCALES:
    for reading in ["f", "s"]:
        real_in, real_out, rand_tot, above, n_real, max_real, max_rand = [], [], [], 0, 0, 0, 0
        per_rec = []
        for r in recs:
            net = nets[scale, r["name"]]
            if reading == "f":
                sig = net["sig"]; n = sig.shape[0]; e = int(sig.sum())
                ins, outs = [sig.sum(0)], [sig.sum(1)]
                rt = np.concatenate([np.add(*random_degrees(n, e, rng)) for _ in range(100)])
            else:
                ins, outs, rt = [], [], []
                for g, s_e, r_e in res[scale, r["name"]]["subs"]:
                    loc = {v: k for k, v in enumerate(g.tolist())}
                    s_l = np.array([loc[v] for v in s_e.tolist()]); r_l = np.array([loc[v] for v in r_e.tolist()])
                    ins.append(np.bincount(r_l, minlength=len(g))); outs.append(np.bincount(s_l, minlength=len(g)))
                    rt.append(np.add(*random_degrees(len(g), len(s_e), rng)))
                rt = np.concatenate(rt)
            ins, outs = np.concatenate(ins), np.concatenate(outs)
            tot = ins + outs
            thr = np.percentile(rt, 99.9)
            above += int((tot > thr).sum()); n_real += len(tot)
            max_real = max(max_real, tot.max()); max_rand = max(max_rand, rt.max())
            per_rec.append({"rec": r["name"], "in": ins, "out": outs, "tot": tot, "rand": rt, "thr": thr})
        deg[scale, reading] = per_rec
        rows.append({"scale": scale, "reading": reading, "neurons_or_slots": n_real,
                     "fraction_above_random_99.9": above / n_real, "ratio_to_0.001": above / n_real / 0.001,
                     "max_real_total": int(max_real), "max_random_total": int(max_rand),
                     "median_threshold": np.median([p["thr"] for p in per_rec])})
fig4bd = pd.DataFrame(rows)
print(fig4bd.round(4).to_string(index=False))
print("\nCriterion: fraction >= 0.01 and max real > max random, at both scales")
for reading in ["f", "s"]:
    sub = fig4bd[fig4bd.reading == reading]
    print(f"  reading ({reading}):", bool(((sub["fraction_above_random_99.9"] >= 0.01) & (sub.max_real_total > sub.max_random_total)).all()))
''', tags=["claim:fig4bd-heavy-tailed-degree"])
code(r'''
fig, axes = plt.subplots(1, 4, figsize=(16, 3.5))
for ax, key in zip(axes, deg):
    tot = np.concatenate([p["tot"] for p in deg[key]]); rt = np.concatenate([p["rand"] for p in deg[key]])
    bins = np.arange(0, max(tot.max(), rt.max()) + 2)
    ax.loglog(bins[:-1], np.histogram(tot, bins, density=True)[0], "k.", label="real total")
    ax.loglog(bins[:-1], np.histogram(rt, bins, density=True)[0], "r.", label="random total")
    ax.set_title(" ".join(key)); ax.legend(fontsize=7)
plt.tight_layout(); plt.show()
print("Zero-degree neurons and empty bins are not shown on the log axes.")
''', tags=["claim:fig4bd-heavy-tailed-degree"])

md(r'''
## fig4bd-out-tail-longer

> The in-degree distribution has a shorter tail than the out-degree distribution, so there are more
> high out-degree neurons than high in-degree neurons.
''')
code(r'''
rows = []
for (scale, reading), per_rec in deg.items():
    ins = np.concatenate([p["in"] for p in per_rec]); outs = np.concatenate([p["out"] for p in per_rec])
    q_in = np.array([np.percentile(p["in"], 99) for p in per_rec]); q_out = np.array([np.percentile(p["out"], 99) for p in per_rec])
    w = stats.wilcoxon(q_out, q_in, alternative="greater") if np.any(q_out != q_in) else None
    rows.append({"scale": scale, "reading": reading, "p99_out": np.percentile(outs, 99), "p99_in": np.percentile(ins, 99),
                 "max_out": outs.max(), "max_in": ins.max(), "recordings_out_gt_in": int((q_out > q_in).sum()),
                 "recordings_out_lt_in": int((q_out < q_in).sum()), "wilcoxon_p_one_sided": w.pvalue if w else np.nan})
tail = pd.DataFrame(rows)
print(tail.round(4).to_string(index=False))
print("\nCriterion: pooled p99 and max of out-degree above those of in-degree, at both scales")
for reading in ["f", "s"]:
    sub = tail[tail.reading == reading]
    print(f"  reading ({reading}):", bool(((sub.p99_out > sub.p99_in) & (sub.max_out > sub.max_in)).all()))
''', tags=["claim:fig4bd-out-tail-longer"])

md(r'''
## fig5a-in-degree-uncorrelated, fig5b-out-degree-positive

> fig5a: The correlation between a receiver's in-degree and the synergy (computation) it performs is
> centered near zero across recordings, with a slight negative skew; computation is independent of
> in-degree.

> fig5b: Most recordings show a positive correlation between a transmitter's out-degree and the
> synergy computed by its receivers.

Synergy is normalized by H(I_F). Under (s) each triple of each sub-network is a data point, with
degrees counted inside the sub-network, the 500 sub-networks pooled per recording; under (f) the
triples of the full network (sampled, see the table above) with full-network degrees. Each
transmitter of a triple is a separate data point for the out-degree. Correlations: (p) Pearson,
(r) Spearman.
''')
code(r'''
def triple_data(scale, name, reading):
    a = res[scale, name]
    if reading == "s":
        t = a["sub_triples"]
        syn = np.array([a["syn"][(x[1], x[2], x[3])] for x in t])
        return t[:, 4], syn, np.r_[t[:, 5], t[:, 6]], np.r_[syn, syn]
    t = a["full_triples"]
    syn = np.array([a["syn"][tuple(x)] for x in t.tolist()])
    return a["indeg_f"][t[:, 0]], syn, np.r_[a["outdeg_f"][t[:, 1]], a["outdeg_f"][t[:, 2]]], np.r_[syn, syn]

corr = []
for scale in hdn.TIME_SCALES:
    for r in recs:
        for reading in ["s", "f"]:
            indeg, syn_in, outdeg, syn_out = triple_data(scale, r["name"], reading)
            for kind, f in [("p", stats.pearsonr), ("r", stats.spearmanr)]:
                for panel, x, y in [("in", indeg, syn_in), ("out", outdeg, syn_out)]:
                    ok = len(x) > 2 and np.ptp(x) > 0
                    c = f(x, y) if ok else None
                    corr.append({"scale": scale, "recording": r["name"], "reading": reading, "coef": kind, "panel": panel,
                                 "n": len(x), "r": c[0] if ok else np.nan, "p": c[1] if ok else np.nan})
corr = pd.DataFrame(corr)
print("Correlations that could not be computed (fewer than 3 points or one degree):", int(corr.r.isna().sum()))

def skew_test(r):
    r = r.dropna(); pos, neg = int((r > 0).sum()), int((r < 0).sum()); n = pos + neg
    return {"n": n, "positive": pos, "negative": neg, "median_r": r.median(),
            "P(neg skew this large or larger)": stats.binom.cdf(pos, n, 0.5),
            "P(pos skew this large or larger)": stats.binom.sf(pos - 1, n, 0.5)}

skew = []
for panel in ["in", "out"]:
    for reading in ["s", "f"]:
        for kind in ["p", "r"]:
            for scale in ["both"] + list(hdn.TIME_SCALES):
                sub = corr[(corr.panel == panel) & (corr.reading == reading) & (corr.coef == kind)]
                if scale != "both":
                    sub = sub[sub.scale == scale]
                skew.append({"panel": panel, "reading": reading, "coef": kind, "scale": scale, **skew_test(sub.r)})
skew = pd.DataFrame(skew)
print(skew.to_string(index=False, float_format=lambda v: f"{v:.3g}"))
''', tags=["claim:fig5a-in-degree-uncorrelated", "claim:fig5b-out-degree-positive"])
code(r'''
print("Per-recording correlations, reading (s), Pearson, by time scale:")
piv = corr[(corr.reading == "s") & (corr.coef == "p")].pivot_table(index="recording", columns=["panel", "scale"], values="r")
print(piv.round(3).to_string())
fig, axes = plt.subplots(1, 2, figsize=(10, 3.5))
for ax, panel in zip(axes, ["in", "out"]):
    v = corr[(corr.reading == "s") & (corr.coef == "p") & (corr.panel == panel)].r.dropna()
    ax.hist(v, bins=np.linspace(-1, 1, 41)); ax.axvline(0, color="k")
    ax.set_title(f"{panel}-degree vs synergy, (s), Pearson; range {v.min():.2f} to {v.max():.2f}")
plt.tight_layout(); plt.show()
''', tags=["claim:fig5a-in-degree-uncorrelated", "claim:fig5b-out-degree-positive"])

md(r'''
## fig5ab-correlations-beyond-null

> Nearly all the per-recording degree and synergy correlations lie beyond a null of randomized degree
> and computation pairings, whose correlations sit near zero.

Ten permutations of degree against synergy per correlation (400 null values for 40 correlations
in the paper; here 10 for each of the 50).
''')
code(r'''
rng = np.random.default_rng(52)
rows = []
for reading in ["s", "f"]:
    for kind, f in [("p", stats.pearsonr), ("r", stats.spearmanr)]:
        for panel in ["in", "out"]:
            real, null = [], []
            for scale in hdn.TIME_SCALES:
                for r in recs:
                    indeg, syn_in, outdeg, syn_out = triple_data(scale, r["name"], reading)
                    x, y = (indeg, syn_in) if panel == "in" else (outdeg, syn_out)
                    if len(x) < 3 or np.ptp(x) == 0:
                        continue
                    real.append(f(x, y)[0])
                    null += [f(rng.permutation(x), y)[0] for _ in range(10)]
            real, null = np.abs(np.array(real)), np.abs(np.array(null))
            thr = np.percentile(null, 99)
            rows.append({"reading": reading, "coef": kind, "panel": panel, "n_corr": len(real), "n_null": len(null),
                         "null_|r|_median": np.median(null), "null_|r|_p99": thr,
                         "fraction_beyond": (real > thr).mean()})
beyond = pd.DataFrame(rows)
print(beyond.to_string(index=False, float_format=lambda v: f"{v:.3g}"))
print("\nCriterion: at least 90% beyond the null's 99th percentile in each panel")
for (reading, kind), sub in beyond.groupby(["reading", "coef"]):
    print(f"  ({reading}, {kind}):", bool((sub.fraction_beyond >= 0.9).all()))
''', tags=["claim:fig5ab-correlations-beyond-null"])

md(r'''
## fig5cd-pooled-trends

> Pooled over all neuron groups and recordings, synergy shows no trend with receiver in-degree and
> rises with transmitter out-degree, at both time scales.
''')
code(r'''
rows = []
for reading in ["s", "f"]:
    for scale in hdn.TIME_SCALES:
        parts = [triple_data(scale, r["name"], reading) for r in recs]
        for panel in ["in", "out"]:
            x = np.concatenate([p[0] if panel == "in" else p[2] for p in parts])
            y = np.concatenate([p[1] if panel == "in" else p[3] for p in parts])
            d = pd.DataFrame({"deg": x, "syn": y}).groupby("deg").syn.agg(["count", "median"])
            d = d[d["count"] >= 20]
            rho, p = stats.spearmanr(d.index, d["median"]) if len(d) > 2 else (np.nan, np.nan)
            rows.append({"reading": reading, "scale": scale, "panel": panel, "degrees_kept": len(d),
                         "degree_range": f"{d.index.min()} to {d.index.max()}", "groups": int(d["count"].sum()),
                         "median_at_lowest": d["median"].iloc[0], "median_at_highest": d["median"].iloc[-1],
                         "spearman_rho": rho, "p": p})
trend = pd.DataFrame(rows)
print(trend.to_string(index=False, float_format=lambda v: f"{v:.3g}"))
print("\nCriterion: out-degree rho > 0 with p < 0.05, and in-degree not significantly positive, at both scales")
for reading in ["s", "f"]:
    sub = trend[trend.reading == reading]
    o, i = sub[sub.panel == "out"], sub[sub.panel == "in"]
    print(f"  reading ({reading}):", bool(((o.spearman_rho > 0) & (o.p < 0.05)).all() and not ((i.spearman_rho > 0) & (i.p < 0.05)).any()))
''', tags=["claim:fig5cd-pooled-trends"])

md(r'''
## fig6-information-gain-not-rising

> The information gained by adding inputs to a neuron, a bound on its highest-order synergy, stays
> constant or decreases with the number of inputs at both time scales; exponential fits to the
> medians give small negative exponents, one with a 95% range overlapping zero.

Inputs are the significant inputs of the full network (reading f). Under (s), the sub-networks keep
75 connections among 50 neurons, so few receivers have six inputs inside one (counted below).
Per recording and time scale, 30 receivers with at least one input are sampled, and for each n up to
20 combinations of n inputs (the paper: every receiver, up to 100 combinations).
''')
code(r'''
def expo(n, A, k):
    return A * np.exp(k * n)

n6 = {scale: int(sum((np.bincount(s_r := r_e, minlength=1) >= 6).sum() for (sc, nm), a in res.items() if sc == scale
                     for g, s_e, r_e in a["subs"])) for scale in hdn.TIME_SCALES}
print("Receivers with 6 or more inputs inside a sub-network, summed over sub-networks:", n6)
rows = []
for scale in hdn.TIME_SCALES:
    for norm, col in [("u (normalized)", 1), ("v (bits)", 0)]:
        per_n = {}
        for n_in in range(1, hdn.MAX_INPUTS + 1):
            per_n[n_in] = np.array([v[col] for (sc, nm), a in res.items() if sc == scale for v in a["gains"].get(n_in, {}).values()])
        for first in [2, 1]:
            ns = np.arange(first, hdn.MAX_INPUTS + 1)
            med = np.array([np.median(per_n[n]) for n in ns])
            p, cov = curve_fit(expo, ns, med, p0=[med[0] * np.exp(0.1 * first), -0.1], maxfev=20000)
            se = np.sqrt(cov[1, 1]); tq = stats.t.ppf(0.975, len(ns) - 2)
            rows.append({"scale": scale, "norm": norm, "n_from": first,
                         "neurons_per_n": "/".join(str(len(per_n[n])) for n in ns),
                         "medians": " ".join(f"{m:.3g}" for m in med), "k": p[1],
                         "k_low": p[1] - tq * se, "k_high": p[1] + tq * se})
gain = pd.DataFrame(rows)
print(gain.to_string(index=False, float_format=lambda v: f"{v:.3g}"))
for (norm, first), sub in gain.groupby(["norm", "n_from"]):
    allneg = bool((sub.k < 0).all()); none_above = bool((sub.k_low <= 0).all())
    print(f"  ({norm}, n from {first}): k < 0 at both scales: {allneg}; no interval wholly above zero: {none_above}")
''', tags=["claim:fig6-information-gain-not-rising"])

md(r'''
## table1-pid-examples

> On the example distributions of Table 1, the PID multivariate TE finds synergy only in the
> synergistic and the synergistic and redundant examples; mutual information misses the hidden self
> interaction, and interaction information misses simultaneous synergy and redundancy and unique
> information.

The joint distributions are the paper's Table 1 (rows I_F, I_P, J_P, K_P from 0000 to 1111), typed
in as printed; each column is renormalized to sum to 1.
''')
code(r'''
TABLE1 = {  # p(I_F, I_P, J_P, K_P), rows 0000 ... 1111, as printed in Table 1
    "No Interaction": ["1/16"] * 16,
    "Self Interaction": ["1/8", "1/8", "1/8", "1/8", "0", "0", "0", "0", "0", "0", "0", "0", "1/8", "1/8", "1/8", "1/8"],
    "Hidden Self Interaction": ["1/4", "1/4", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1/4", "1/4"],
    "Single Interaction": ["1/8", "1/8", "0", "0", "1/8", "1/8", "0", "0", "0", "0", "1/8", "1/8", "0", "0", "1/8", "1/8"],
    "Redundant Interaction": ["1/4", "0", "0", "0", "1/4", "0", "0", "0", "0", "0", "0", "1/4", "0", "0", "0", "1/4"],
    "Single and Redundant Interaction": ["0.1964", "0.0536", "0", "0", "0.1964", "0.0536", "0", "0", "0", "0", "0.0536", "0.1964", "0", "0", "0.0536", "0.1964"],
    "Synergistic Interaction": ["1/8", "0", "0", "1/8", "1/8", "0", "0", "1/8", "0", "1/8", "1/8", "0", "0", "1/8", "1/8", "0"],
    "Synergistic and Redundant Interaction": ["0.0548", "0.0548", "0.0548", "0", "0.0548", "0.0548", "0.0548", "0", "0", "0", "0", "0.3357", "0", "0", "0", "0.3357"],
}

def mi(pxy):
    px, py = pxy.sum(1, keepdims=True), pxy.sum(0, keepdims=True)
    m = pxy > 0
    return float((pxy[m] * np.log2(pxy[m] / (px @ py)[m])).sum())

rows = []
for name, col in TABLE1.items():
    p = np.array([eval(v) for v in col], float); p = p / p.sum()
    n = np.zeros((2, 2, 4))
    pf = np.zeros((2, 2, 2))   # p(I_F, J_P, K_P)
    for row in range(16):
        f, q, j, k = (row >> 3) & 1, (row >> 2) & 1, (row >> 1) & 1, row & 1
        n[f, q, j + 2 * k] = p[row] * 1e6
        pf[f, j, k] += p[row]
    syn, red, uJ, uK, teJ, teK, teJK, H = hdn.pid_from_table(n)
    mi_j = mi(pf.sum(2))                                  # MI(J_P; I_F)
    mi_jk = mi(pf.sum(0))                                 # MI(J_P; K_P)
    mi_jk_f = sum(pf[f].sum() * mi(pf[f] / pf[f].sum()) for f in range(2) if pf[f].sum() > 0)  # MI(J_P; K_P | I_F)
    rows.append({"example": name, "TE(J)": teJ, "TE(K)": teK, "TE(JK)": teJK, "redundancy": red, "unique J": uJ,
                 "unique K": uK, "synergy": syn, "MI(J_P;I_F)": mi_j, "II": mi_jk_f - mi_jk})
t1 = pd.DataFrame(rows).set_index("example")
print(t1.round(4).to_string())
tol = 0.001
hs, srd, snr = t1.loc["Hidden Self Interaction"], t1.loc["Synergistic and Redundant Interaction"], t1.loc["Single and Redundant Interaction"]
checks = {
    "synergy > 0.001 exactly in the two synergistic examples":
        set(t1.index[t1.synergy > tol]) == {"Synergistic Interaction", "Synergistic and Redundant Interaction"},
    "hidden self: MI(J_P;I_F) > 0 while TE and every PID term are 0":
        hs["MI(J_P;I_F)"] > tol and all(abs(hs[c]) <= tol for c in ["TE(J)", "TE(K)", "TE(JK)", "redundancy", "unique J", "unique K", "synergy"]),
    "synergistic and redundant: II = 0 while synergy and redundancy are not":
        abs(srd["II"]) <= tol and srd.synergy > tol and srd.redundancy > tol,
    "single and redundant: unique J > 0 and |II| = redundancy":
        snr["unique J"] > tol and abs(abs(snr["II"]) - snr.redundancy) <= tol,
}
for k, v in checks.items():
    print(f"{k}: {v}")
''', tags=["claim:table1-pid-examples"])

md(r'''
## Model claims (Figure 7 and S1 Fig)

fig7b-connectivity-patterns, fig7c-degree-modified-rule-matches,
fig7d-degree-rule-highest-conditioned-mi and figs1-larger-model need a simulation of the paper's
feedforward model. Its equations (Eqs 13 to 24) are in the version of record, so the claims are
testable, but the simulation was not written and run within this attempt's time, after the TE
networks took most of it. They are recorded as blocked.
''')

md("## Summary")
code(r'''
print(f"Notebook ran in {(time.time() - started) / 60:.1f} min")
''')
nb["cells"] = C
nb["metadata"] = {"kernelspec": {"name": "python3", "display_name": "Python 3", "language": "python"}}
nbf.write(nb, "entries/crcns-ssc-3-timme-2016/reproduce_timme_2016.ipynb")
PYEOF
cd $TMPDIR && source dev/bin/activate && uv pip install -q nbformat nbclient ipykernel && python mknb.py && echo ok; date -u
```

```
ok
Fri Nov  6 12:54:36 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source dev/bin/activate && python - <<'EOF' 2>&1 | tail -30
import nbformat, time, sys, os
from nbclient import NotebookClient
nb=nbformat.read('entries/crcns-ssc-3-timme-2016/reproduce_timme_2016.ipynb',4)
# dev subset
nb.cells[1].source += "\nrecs = [r for r in recs if r['name'] in ('DataSet1','DataSet4','DataSet7')]\nhdn.N_SUBNETS=50\n"
for c in nb.cells:
    if 'for name in ["DataSet1", "DataSet7"]' in c.source:
        c.source = c.source.replace('["DataSet1", "DataSet7"]','["DataSet4"]')
    c.source = c.source.replace('hdn.analyse_recording(net["trains"]','hdn.analyse_recording(net["trains"]')
import hdn_path if False else None
EOF
echo
```

```
File "<stdin>", line 10
    import hdn_path if False else None
                    ^^
SyntaxError: invalid syntax
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source dev/bin/activate && timeout 1200 python - <<'EOF' 2>&1 | tail -40
import nbformat, time
from nbclient import NotebookClient
nb=nbformat.read('entries/crcns-ssc-3-timme-2016/reproduce_timme_2016.ipynb',4)
nb.cells[1].source += "\nrecs = [r for r in recs if r['name'] in ('DataSet1','DataSet4','DataSet7')]\n"
for c in nb.cells:
    if 'for name in ["DataSet1", "DataSet7"]' in c.source:
        c.source = c.source.replace('["DataSet1", "DataSet7"]','["DataSet4"]')
t=time.time()
try:
    NotebookClient(nb, timeout=1200, kernel_name='python3', resources={'metadata':{'path':'entries/crcns-ssc-3-timme-2016'}}).execute()
except Exception as e:
    print("ERR", str(e)[-3000:])
nbformat.write(nb,'dev_exec.ipynb')
print(time.time()-t)
for c in nb.cells:
    if c.cell_type=='code':
        for o in c.get('outputs',[]):
            if o.get('output_type')=='stream': print(o['text'][-2500:])
            if o.get('output_type')=='error': print('ERROR',o['ename'],o['evalue'])
EOF
```

```
f 1.6-6.4 ms   out            65     1 to 112   14012          0.000468           1.46e-05        -0.651 4.31e-09
      f  3.5-14 ms    in            52      3 to 80    8657            0.0162            0.00017        -0.573 8.84e-06
      f  3.5-14 ms   out            63     1 to 117   17340           0.00509             0.0181       -0.0378    0.769

Criterion: out-degree rho > 0 with p < 0.05, and in-degree not significantly positive, at both scales
  reading (s): False
  reading (f): False

Receivers with 6 or more inputs inside a sub-network, summed over sub-networks: {'1.6-6.4 ms': 2751, '3.5-14 ms': 1733}
     scale           norm  n_from     neurons_per_n                                               medians       k  k_low  k_high
1.6-6.4 ms u (normalized)       2    85/77/68/60/57          0.000672 0.000597 0.000359 0.000308 0.000273  -0.255 -0.384  -0.126
1.6-6.4 ms u (normalized)       1 90/85/77/68/60/57  0.00137 0.000672 0.000597 0.000359 0.000308 0.000273  -0.407 -0.587  -0.227
1.6-6.4 ms       v (bits)       2    85/77/68/60/57          1.45e-05 1.27e-05 5.18e-06 1.96e-06 2.42e-06  -0.477 -0.868 -0.0868
1.6-6.4 ms       v (bits)       1 90/85/77/68/60/57 3.35e-05 1.45e-05 1.27e-05 5.18e-06 1.96e-06 2.42e-06  -0.611 -0.835  -0.388
 3.5-14 ms u (normalized)       2    85/79/73/67/62                    0.0166 0.0157 0.0153 0.0132 0.0115 -0.0863 -0.135 -0.0373
 3.5-14 ms u (normalized)       1 90/85/79/73/67/62             0.0179 0.0166 0.0157 0.0153 0.0132 0.0115 -0.0793 -0.108 -0.0503
 3.5-14 ms       v (bits)       2    85/79/73/67/62           0.000397 0.00042 0.000367 0.000264 0.000197  -0.156 -0.314 0.00213
 3.5-14 ms       v (bits)       1 90/85/79/73/67/62  0.000498 0.000397 0.00042 0.000367 0.000264 0.000197   -0.15 -0.235 -0.0654
  (u (normalized), n from 1): k < 0 at both scales: True; no interval wholly above zero: True
  (u (normalized), n from 2): k < 0 at both scales: True; no interval wholly above zero: True
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source dev/bin/activate && python - <<'EOF' 2>&1 | head -150
import nbformat
nb=nbformat.read('dev_exec.ipynb',4)
for c in nb.cells:
    if c.cell_type=='code':
        for o in c.get('outputs',[]):
            if o.get('output_type')=='stream': print(o['text'][:3000])
            if o.get('output_type')=='error': print('ERROR',o['ename'],o['evalue'])
EOF
```

```
CRCNS ssc-3 (10.6080/K07D2S2F), version unversioned: 25 recordings streamed in 8 s
MD5 of the streamed archive: 1a5bd3d304c5442290a7c9c1f1b5def6 | checksums.md5: 1a5bd3d304c5442290a7c9c1f1b5def6 | equal: True

    file recording_id  nNeurons  trains  length_ms  first_ms    last_ms  spikes_min  spikes_max  under_100  sorted  on_50us_grid         x_um        y_um     timescale sampling
DataSet1 2012-02-09-0       166     166  3600000.0   8005.85 3599995.65         105      113781          0    True          True -960 to 1063 -608 to 575 1 millisecond   20 kHz
DataSet4 2012-02-12-0        98      98  3600000.0   8002.30 3598396.00         164       43409          0    True          True  -915 to 927 -395 to 602 1 millisecond   20 kHz
DataSet7 2012-02-15-1       172     172  3600000.0   8000.05 3599401.10         115       25488          0    True          True  -953 to 945 -591 to 585 1 millisecond   20 kHz

nNeurons equals the number of spike trains in every file: True
Spike times sorted within every train: True | on the 0.05 ms grid (20 kHz): True
Every spike within [0, recordinglength]: True
Recording lengths (ms): {3600000.0: 3}
Recording dates: ['2012-02-09', '2012-02-12', '2012-02-15']
Spike trains with the same count, first and last spike in two files: 0
Distinct recording IDs: 3 of 3

Recordings: 3
Neurons as deposited: 436 | mean per recording: 145.3
Neurons with 100 or more spikes: 436 (the deposit already applies the threshold)
Mean rate per neuron, (a) spikes over each recording's length: 1.357 Hz; (b) spikes over 60 min: 1.357 Hz
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-ssc-3-timme-2016 && cat >> hdn.py <<'EOF'


# ---------------------------------------------------------------- feedforward model (Fig 7, S1 Fig)
# Paper, Methods, Feedforward Network Model, and Eqs 13 to 24 (version of record). Each run is
# independent: b(t) is 0 or 1 with equal probability; input neuron i fires with the probability of
# Eqs 16-17; output neuron o receives the current of Eqs 18-19 plus I_con for each active
# connected input; firing follows Eq 13. Rewiring: 500 runs, score S(i, o) (Eq 20), the connected
# pair with the lowest score is disconnected and the unconnected pair with the highest score is
# connected; repeated N_connections times. 100 models per type.

I_CON = 10.0
MODEL_RUNS = 500
N_MODELS = 100
RULES = {   # (a1 DegIn(o), a2 DegOut(i), a3 FR(o), a4 FR(i)); paper Eqs 22 to 24
    20: {"random": None, "hebbian": (0, 0, 0, 0), "degree": (0.05, -1.75, 0, 0), "firing_rate": (0, 0, 0.35, 3.1)},
    40: {"random": None, "hebbian": (0, 0, 0, 0), "degree": (0.16, -0.3, 0, 0), "firing_rate": (0, 0, 0.35, 3.1)},
}


def sigmoid_params(n_neurons):
    """alpha and beta from Eq 14 (p(0) = 0.01) and Eq 15 (p(I_con N) = 0.5)."""
    beta = math.log(99.0)
    return beta / (I_CON * n_neurons), beta


def _current(p, alpha, beta):
    # the current that gives firing probability p under Eq 13
    return (beta + np.log(p / (1 - p))) / alpha


def simulate(conn, n_runs, rng, alpha, beta):
    """conn (M, N_in, N_out) bool. Returns b (M, R), input states (M, R, N), output states (M, R, N)."""
    M, N, _ = conn.shape
    frac = np.arange(N) / (N - 1)
    I_in = np.stack([_current(0.5 - 0.4 * frac, alpha, beta), _current(0.5 + 0.4 * frac, alpha, beta)])
    I_out = np.stack([_current(0.5 - 0.2 * frac, alpha, beta), _current(0.5 + 0.2 * frac, alpha, beta)])
    b = rng.integers(0, 2, (M, n_runs))
    p_in = 1 / (1 + np.exp(-alpha * I_in[b] + beta))
    x = rng.random((M, n_runs, N)) < p_in
    cur = I_out[b] + I_CON * np.einsum("mri,mio->mro", x.astype(float), conn.astype(float))
    y = rng.random((M, n_runs, N)) < 1 / (1 + np.exp(-alpha * cur + beta))
    return b, x, y


def build_models(n_neurons, rule, rng, alpha, beta, n_models=N_MODELS):
    """Connectivity of n_models models of one type, after rewiring (none for 'random')."""
    N = n_neurons
    n_conn = int(round(0.2 * N * N))
    conn = np.zeros((n_models, N, N), bool)
    for m in range(n_models):
        conn[m].flat[rng.choice(N * N, n_conn, replace=False)] = True
    a = RULES[N][rule]
    if a is None:
        return conn
    for _ in range(n_conn):
        b, x, y = simulate(conn, MODEL_RUNS, rng, alpha, beta)
        xf, yf = x.astype(float), y.astype(float)
        agree = (np.einsum("mri,mro->mio", xf, yf) + np.einsum("mri,mro->mio", 1 - xf, 1 - yf)) / MODEL_RUNS
        deg_in = conn.sum(1)[:, None, :]
        deg_out = conn.sum(2)[:, :, None]
        fr_out = yf.mean(1)[:, None, :]
        fr_in = xf.mean(1)[:, :, None]
        score = agree + a[0] * deg_in + a[1] * deg_out + a[2] * fr_out + a[3] * fr_in
        for m in range(n_models):
            s = score[m]
            on = np.flatnonzero(conn[m].ravel())
            off = np.flatnonzero(~conn[m].ravel())
            lo = on[np.argmin(s.ravel()[on])]
            hi = off[np.argmax(s.ravel()[off])]
            conn[m].flat[lo] = False
            conn[m].flat[hi] = True
    return conn


def model_correlations(conn, rng, alpha, beta, n_runs):
    """Per model: Pearson and Spearman correlations of synergy (PID of two input states about
    the output state in the same run, normalized by H(output)) with the output's in-degree and
    with each input's out-degree; mean MI between connected neurons, unconditioned and
    conditioned on b."""
    from scipy import stats
    b, x, y = simulate(conn, n_runs, rng, alpha, beta)
    out = []
    for m in range(conn.shape[0]):
        c = conn[m]
        deg_in, deg_out = c.sum(0), c.sum(1)
        syn, din, dj, dk = [], [], [], []
        for o in range(c.shape[1]):
            ins = np.flatnonzero(c[:, o])
            for j, k in itertools.combinations(ins, 2):
                tab = np.zeros((2, 2, 4))
                code = x[m, :, j].astype(int) + 2 * x[m, :, k].astype(int)
                np.add.at(tab, (y[m, :, o].astype(int), 0, code), 1)
                r = pid_from_table(tab)
                syn.append(r[0] / r[7] if r[7] > 0 else 0.0)
                din.append(deg_in[o]); dj.append(deg_out[j]); dk.append(deg_out[k])
        syn = np.array(syn)
        res = {}
        for name, f in [("p", stats.pearsonr), ("r", stats.spearmanr)]:
            res["in_" + name] = f(din, syn)[0] if len(syn) > 2 and np.ptp(din) > 0 else np.nan
            xo, so = np.r_[dj, dk], np.r_[syn, syn]
            res["out_" + name] = f(xo, so)[0] if len(so) > 2 and np.ptp(xo) > 0 else np.nan
        mi_u, mi_c = [], []
        for i, o in zip(*np.nonzero(c)):
            mi_u.append(_mi2(x[m, :, i], y[m, :, o]))
            mi_c.append(sum((b[m] == v).mean() * _mi2(x[m, b[m] == v, i], y[m, b[m] == v, o]) for v in (0, 1)))
        res["mi"] = np.mean(mi_u)
        res["mi_given_b"] = np.mean(mi_c)
        res["upper_half_fraction"] = c[c.shape[0] // 2:].sum() / c.sum()
        out.append(res)
    return out


def _mi2(u, v):
    t = np.zeros((2, 2))
    np.add.at(t, (u.astype(int), v.astype(int)), 1)
    p = t / t.sum()
    pu, pv = p.sum(1, keepdims=True), p.sum(0, keepdims=True)
    k = p > 0
    return float((p[k] * np.log2(p[k] / (pu @ pv)[k])).sum())
EOF
sed -i 's/^import hashlib/import hashlib\nimport itertools/' hdn.py
cd $TMPDIR && source dev/bin/activate && python - <<'EOF' 2>&1 | grep -v -i warn | grep -v "tr = trains"
import sys,time,numpy as np
sys.path.insert(0,'entries/crcns-ssc-3-timme-2016')
import hdn
al,be=hdn.sigmoid_params(20); print(al,be)
rng=np.random.default_rng(0)
for rule in ['random','hebbian','degree','firing_rate']:
    t=time.time(); c=hdn.build_models(20,rule,rng,al,be,n_models=20); t1=time.time()-t
    r=hdn.model_correlations(c,rng,al,be,2000)
    import pandas as pd
    print(rule, round(t1,1), round(time.time()-t,1), pd.DataFrame(r).mean().round(4).to_dict())
EOF
```

```
0.02297559925067295 4.59511985013459
random 0.0 3.6 {'in_p': 0.0401, 'out_p': -0.0058, 'in_r': 0.0614, 'out_r': -0.0019, 'mi': 0.0235, 'mi_given_b': 0.0023, 'upper_half_fraction': 0.51}
hebbian 1.3 2.9 {'in_p': 0.2993, 'out_p': 0.0493, 'in_r': 0.2747, 'out_r': -0.0088, 'mi': 0.0903, 'mi_given_b': 0.0017, 'upper_half_fraction': 0.9862}
degree 1.3 4.1 {'in_p': -0.0472, 'out_p': 0.1253, 'in_r': -0.0619, 'out_r': 0.1422, 'mi': 0.0299, 'mi_given_b': 0.0016, 'upper_half_fraction': 0.5062}
firing_rate 1.3 3.2 {'in_p': -0.0681, 'out_p': 0.2678, 'in_r': -0.1163, 'out_r': 0.2022, 'mi': 0.0748, 'mi_given_b': 0.0017, 'upper_half_fraction': 0.8206}
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('mknb.py').read()
# fit p0 from moments
s=s.replace('''def fit_r2(x, y):
    try:
        p, _ = curve_fit(lognorm_pmf, x, y, p0=[y.max() * 0.5, np.log10(x[np.argmax(y)]), 0.5], maxfev=20000)''','''def fit_r2(x, y):
    lx = np.log10(x)
    m = (y * lx).sum() / y.sum()
    sd = np.sqrt((y * (lx - m) ** 2).sum() / y.sum())
    try:
        # start from the moments of the binned distribution; alpha starts at the log bin width
        p, _ = curve_fit(lognorm_pmf, x, y, p0=[lx[1] - lx[0], m, sd], maxfev=20000)''')
s=s.replace('''n6 = {scale: int(sum((np.bincount(s_r := r_e, minlength=1) >= 6).sum() for (sc, nm), a in res.items() if sc == scale
                     for g, s_e, r_e in a["subs"])) for scale in hdn.TIME_SCALES}''','''n6 = {scale: int(sum((np.bincount(r_e) >= 6).sum() for (sc, nm), a in res.items() if sc == scale
                     for g, s_e, r_e in a["subs"])) for scale in hdn.TIME_SCALES}''')
s=s.replace('''Inputs are the significant inputs of the full network (reading f). Under (s), the sub-networks keep
75 connections among 50 neurons, so few receivers have six inputs inside one (counted below).''','''Inputs are the significant inputs of the full network (reading f); reading (s) was not run (the
count of sub-network receivers with six inputs is printed below).''')
old=s[s.index("md(r'''\n## Model claims (Figure 7 and S1 Fig)"):s.index('md("## Summary")')]
new=r"""md(r'''
## Feedforward model: fig7b, fig7c, fig7d, figs1

> fig7c: In a two-layer feedforward model, degree-modified and firing-rate-modified Hebbian rewiring
> rules qualitatively reproduce the degree and synergy correlations of the real data, the
> degree-modified rule more closely, while a pure Hebbian rule and random wiring do not.

> fig7b: The pure Hebbian rule pools connections among the input neurons most correlated with the
> network-wide signal, the firing-rate-modified rule spreads them to less correlated input neurons,
> and the degree-modified rule spreads them almost uniformly across the input layer.

> fig7d: The pure Hebbian rule gives the highest mutual information between connected neurons, but
> conditioned on the network-wide binary signal the degree-modified rule gives the highest; it alone
> raises neuron-to-neuron communication while also reinforcing network-wide correlation.

> figs1: With 40 neurons per layer the model gives the same qualitative results, the degree-modified
> rule again raising neuron-to-neuron communication, though the Hebbian and firing-rate-modified
> rules give larger conditioned mutual information than in the small model.

The model follows the Methods and Eqs 13 to 24 of the version of record (`hdn.py`). Synergy and MI
are computed from 5000 fresh runs per model. The real data's reference is the mean and standard
deviation of the 50 per-recording correlations (25 recordings, two time scales) of reading (s),
Pearson, from the fig5 section; the other readings are shown.
''')
code(r'''
MODEL_EVAL_RUNS = 5000
models = {}
t_all = time.time()
for N, readings in [(20, ["kept"]), (40, ["recomputed", "kept"])]:
    for ab in readings:
        alpha, beta = hdn.sigmoid_params(N if ab == "recomputed" else 20)
        if N == 20:
            alpha, beta = hdn.sigmoid_params(20)
        for k, rule in enumerate(hdn.RULES[N]):
            rng = np.random.default_rng(700 + 10 * N + k + (5 if ab == "kept" and N == 40 else 0))
            conn = hdn.build_models(N, rule, rng, alpha, beta)
            models[N, ab, rule] = (conn, pd.DataFrame(hdn.model_correlations(conn, rng, alpha, beta, MODEL_EVAL_RUNS)))
print(f"models built and evaluated in {time.time() - t_all:.0f} s")
print("alpha, beta for N = 20:", [round(v, 4) for v in hdn.sigmoid_params(20)], "| recomputed for N = 40:", [round(v, 4) for v in hdn.sigmoid_params(40)])
rows = []
for (N, ab, rule), (conn, d) in models.items():
    rows.append({"N": N, "alpha_beta": ab, "rule": rule, "models": len(d), "connections": int(conn[0].sum()),
                 **{c: d[c].mean() for c in ["in_p", "out_p", "in_r", "out_r", "mi", "mi_given_b", "upper_half_fraction"]},
                 "in_p_sd": d.in_p.std(), "out_p_sd": d.out_p.std(), "nan_in": int(d.in_p.isna().sum()), "nan_out": int(d.out_p.isna().sum())})
mod = pd.DataFrame(rows)
print(mod.to_string(index=False, float_format=lambda v: f"{v:.4g}"))
''')
code(r'''
def real_ref(reading, kind):
    sub = corr[(corr.reading == reading) & (corr.coef == kind)]
    i, o = sub[sub.panel == "in"].r.dropna(), sub[sub.panel == "out"].r.dropna()
    return i.mean(), i.std(), o.mean(), o.std()

def match_table(N, ab, reading, kind):
    mi_, si, mo, so = real_ref(reading, kind)
    rows = []
    for rule in hdn.RULES[N]:
        d = models[N, ab, rule][1]
        a, b = d["in_" + kind].mean(), d["out_" + kind].mean()
        rows.append({"rule": rule, "mean_in": a, "mean_out": b, "match": abs(a - mi_) <= si and abs(b - mo) <= so,
                     "distance": math.hypot(a - mi_, b - mo)})
    return pd.DataFrame(rows), (mi_, si, mo, so)

def fig7c_ok(t):
    m = t.set_index("rule")
    return bool(m.match["degree"] and m.match["firing_rate"] and not m.match["hebbian"] and not m.match["random"]
                and m.distance["degree"] < m.distance["firing_rate"])

for reading in ["s", "f"]:
    for kind in ["p", "r"]:
        t, ref = match_table(20, "kept", reading, kind)
        print(f"reading ({reading}, {kind}): real in {ref[0]:.3f} +- {ref[1]:.3f}, out {ref[2]:.3f} +- {ref[3]:.3f}")
        print(t.round(4).to_string(index=False))
        print("  fig7c criterion:", fig7c_ok(t))
fig, ax = plt.subplots(figsize=(5, 4))
for rule in hdn.RULES[20]:
    d = models[20, "kept", rule][1]
    ax.plot(d.in_p, d.out_p, ".", alpha=0.3, label=rule)
mi_, si, mo, so = real_ref("s", "p")
ax.errorbar(mi_, mo, xerr=si, yerr=so, color="k", label="real (s, p)")
ax.set_xlabel("in-degree vs synergy r"); ax.set_ylabel("out-degree vs synergy r"); ax.legend(fontsize=7)
plt.show()
d_all = pd.concat([models[20, "kept", r][1] for r in hdn.RULES[20]])
print(f"model correlations range: in {d_all.in_p.min():.3f} to {d_all.in_p.max():.3f}, out {d_all.out_p.min():.3f} to {d_all.out_p.max():.3f}; all within the axes")
''', tags=["claim:fig7c-degree-modified-rule-matches"])
code(r'''
def fig7b_table(N, ab):
    t = pd.DataFrame([{"rule": r, "upper_half_fraction": models[N, ab, r][1].upper_half_fraction.mean(),
                       "sd": models[N, ab, r][1].upper_half_fraction.std()} for r in hdn.RULES[N]])
    m = t.set_index("rule").upper_half_fraction
    ok = bool(m["hebbian"] > m["firing_rate"] > m["degree"] and abs(m["degree"] - 0.5) <= 0.1)
    return t, ok

t, ok = fig7b_table(20, "kept")
print(t.round(4).to_string(index=False)); print("fig7b criterion:", ok)
fig, axes = plt.subplots(1, 4, figsize=(14, 3))
for ax, rule in zip(axes, hdn.RULES[20]):
    im = ax.imshow(models[20, "kept", rule][0].mean(0), vmin=0, vmax=1, cmap="viridis")
    ax.set_title(rule); ax.set_xlabel("output o"); ax.set_ylabel("input i")
plt.colorbar(im, ax=axes); plt.show()
''', tags=["claim:fig7b-connectivity-patterns"])
code(r'''
def fig7d_tests(N, ab):
    rules = list(hdn.RULES[N])
    rows = []
    for col in ["mi", "mi_given_b"]:
        for a, b in itertools.combinations(rules, 2):
            x, y = models[N, ab, a][1][col], models[N, ab, b][1][col]
            rows.append({"measure": col, "a": a, "b": b, "mean_a": x.mean(), "mean_b": y.mean(),
                         "p": stats.mannwhitneyu(x, y, alternative="two-sided").pvalue})
    t = pd.DataFrame(rows)
    t["p_fdr"] = stats.false_discovery_control(t.p, method="bh")
    return t

def fig7d_ok(N, ab, t):
    means = {r: models[N, ab, r][1][["mi", "mi_given_b"]].mean() for r in hdn.RULES[N]}
    top_u = max(means, key=lambda r: means[r]["mi"]); top_c = max(means, key=lambda r: means[r]["mi_given_b"])
    c = t[t.measure == "mi_given_b"]
    deg_beats = all(((c.a == "degree") & (c.b == r) | (c.b == "degree") & (c.a == r)).any() and
                    c[((c.a == "degree") & (c.b == r)) | ((c.b == "degree") & (c.a == r))].p_fdr.iloc[0] < 0.001
                    for r in hdn.RULES[N] if r != "degree")
    not_above_random = all(not (means[r]["mi_given_b"] > means["random"]["mi_given_b"] and
                                c[((c.a == r) & (c.b == "random")) | ((c.b == r) & (c.a == "random"))].p_fdr.iloc[0] < 0.001)
                           for r in ["hebbian", "firing_rate"])
    return top_u, top_c, deg_beats, not_above_random

t = fig7d_tests(20, "kept")
print(t.to_string(index=False, float_format=lambda v: f"{v:.3g}"))
top_u, top_c, deg_beats, nar = fig7d_ok(20, "kept", t)
print(f"highest unconditioned MI: {top_u}; highest conditioned MI: {top_c}; degree above every other rule at FDR p < 0.001: {deg_beats}; "
      f"Hebbian and firing-rate not significantly above random: {nar}")
print("fig7d criterion:", top_u == "hebbian" and top_c == "degree" and deg_beats and nar)
''', tags=["claim:fig7d-degree-rule-highest-conditioned-mi"])
code(r'''
for ab in ["recomputed", "kept"]:
    print(f"=== N = 40, alpha and beta {ab} ===")
    ok_all = []
    for reading, kind in [("s", "p"), ("s", "r"), ("f", "p"), ("f", "r")]:
        t, ref = match_table(40, ab, reading, kind)
        m = t.set_index("rule")
        ok_c = bool(m.match["degree"] and m.match["firing_rate"] and not m.match["hebbian"])
        print(f"reading ({reading}, {kind}):", t.round(4).to_dict("list"), "| correlation match:", ok_c)
        ok_all.append(ok_c)
    tb, ok_b = fig7b_table(40, ab)
    print(tb.round(4).to_string(index=False), "| connectivity ordering:", ok_b)
    td = fig7d_tests(40, ab)
    c = td[(td.measure == "mi_given_b") & (((td.a == "degree") & (td.b == "random")) | ((td.b == "degree") & (td.a == "random")))]
    deg_above = bool(models[40, ab, "degree"][1].mi_given_b.mean() > models[40, ab, "random"][1].mi_given_b.mean() and c.p_fdr.iloc[0] < 0.001)
    larger = {r: (models[40, ab, r][1].mi_given_b.mean(), models[20, "kept", r][1].mi_given_b.mean()) for r in ["hebbian", "firing_rate"]}
    print(td.to_string(index=False, float_format=lambda v: f"{v:.3g}"))
    print("degree conditioned MI above random (FDR p < 0.001):", deg_above)
    print("conditioned MI, N = 40 against N = 20:", {r: (round(a, 5), round(b, 5)) for r, (a, b) in larger.items()})
    print("figs1 criterion, reading (s, p):", ok_all[0] and ok_b and deg_above and all(a > b for a, b in larger.values()))
''', tags=["claim:figs1-larger-model"])

"""
s=s.replace(old,new)
s=s.replace('''| fig7c-degree-modified-rule-matches | blocked: not run within the run's time |
| fig7b-connectivity-patterns | blocked: not run within the run's time |
| fig7d-degree-rule-highest-conditioned-mi | blocked: not run within the run's time |
| figs1-larger-model | blocked: not run within the run's time |''','''| fig7b-connectivity-patterns | tested (model simulation) |
| fig7c-degree-modified-rule-matches | tested (model simulation) |
| fig7d-degree-rule-highest-conditioned-mi | tested (model simulation) |
| figs1-larger-model | tested (model simulation) |''')
open('mknb.py','w').write(s)
EOF
grep -n "if N == 20" mknb.py
```

```
638:        if N == 20:
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -i '/^        if N == 20:$/,+1d' mknb.py && source dev/bin/activate && python mknb.py && timeout 1500 python - <<'EOF' 2>&1 | tail -80
import nbformat, time
from nbclient import NotebookClient
nb=nbformat.read('entries/crcns-ssc-3-timme-2016/reproduce_timme_2016.ipynb',4)
nb.cells[1].source += "\nrecs = [r for r in recs if r['name'] in ('DataSet1','DataSet4','DataSet7')]\nhdn.build_models.__defaults__ = (10,)\n"
for c in nb.cells:
    if 'for name in ["DataSet1", "DataSet7"]' in c.source:
        c.source = c.source.replace('["DataSet1", "DataSet7"]','["DataSet4"]')
t=time.time()
try:
    NotebookClient(nb, timeout=1500, kernel_name='python3', resources={'metadata':{'path':'entries/crcns-ssc-3-timme-2016'}}).execute()
except Exception as e:
    print("ERR", str(e)[-3000:])
nbformat.write(nb,'dev_exec.ipynb')
print(time.time()-t)
for c in nb.cells[-8:]:
    if c.cell_type=='code':
        for o in c.get('outputs',[]):
            if o.get('output_type')=='stream': print(o['text'][-6000:])
            if o.get('output_type')=='error': print('ERROR',o['ename'],o['evalue'])
EOF
date -u
```

```
model correlations range: in -0.280 to 0.484, out -0.201 to 0.381; all within the axes

       rule  upper_half_fraction     sd
     random               0.5112 0.0393
    hebbian               0.9925 0.0121
     degree               0.5087 0.0060
firing_rate               0.8000 0.0408
fig7b criterion: True

   measure       a           b  mean_a  mean_b        p    p_fdr
        mi  random     hebbian   0.023  0.0897 0.000183 0.000274
        mi  random      degree   0.023  0.0312 0.000583 0.000699
        mi  random firing_rate   0.023  0.0706 0.000183 0.000274
        mi hebbian      degree  0.0897  0.0312 0.000183 0.000274
        mi hebbian firing_rate  0.0897  0.0706 0.000183 0.000274
        mi  degree firing_rate  0.0312  0.0706 0.000183 0.000274
mi_given_b  random     hebbian 0.00191 0.00124 0.000183 0.000274
mi_given_b  random      degree 0.00191  0.0011 0.000183 0.000274
mi_given_b  random firing_rate 0.00191 0.00125 0.000183 0.000274
mi_given_b hebbian      degree 0.00124  0.0011  0.00361  0.00394
[... 62 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source dev/bin/activate && python - <<'EOF'
import nbformat
nb=nbformat.read('dev_exec.ipynb',4)
for c in nb.cells:
    if c.cell_type=='code':
        for o in c.get('outputs',[]):
            if o.get('output_type')=='stream' and ('models built' in o['text'] or 'in ' in o['text'][:80]): print(o['text'][:300])
EOF
```

```
CRCNS ssc-3 (10.6080/K07D2S2F), version unversioned: 25 recordings streamed in 8 s
MD5 of the streamed archive: 1a5bd3d304c5442290a7c9c1f1b5def6 | checksums.md5: 1a5bd3d304c5442290a7c9c1f1b5def6 | equal: True

sub-networks, synergy and information gains in 18 s
     scale recording  subnetworks  restarts  subnet_triples  full_triples_total  full_triples_used
1.6-6.4 ms  DataSet1          500         0           54324               55191               3000
1.6-6.4 ms  DataSet4          500         0       
     scale reading measure  n_values  R2_average  R2_rec_median  R2_rec_min       p1     p99   p99/p1  p99/p1_rec_min      min     max  mu_log10  sigma_log10
1.6-6.4 ms       f      te      6821       0.132          0.942       0.801 1.44e-08 0.00279 1.94e+05        8.29e+03 7.91e-09 0.00875     -6.
Every bin of the 100 log-spaced bins is shown; values span the full range of each panel's x axis.

     scale reading  p99_out  p99_in  max_out  max_in  recordings_out_gt_in  recordings_out_lt_in  wilcoxon_p_one_sided
1.6-6.4 ms       f    82.55   87.65      112     113                     1                     2                 0.625
1.6-6.4 ms       s    16.01    8.00       30      17          
models built and evaluated in 165 s
alpha, beta for N = 20: [0.023, 4.5951] | recomputed for N = 40: [0.0115, 4.5951]
 N alpha_beta        rule  models  connections      in_p     out_p      in_r    out_r      mi  mi_given_b  upper_half_fraction  in_p_sd  out_p_sd  nan_in  nan_out
20       kept      
reading (s, p): real in -0.181 +- 0.109, out 0.253 +- 0.156
       rule  mean_in  mean_out  match  distance
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-ssc-3-timme-2016 && python3 - <<'EOF'
s=open('hdn.py').read()
s=s.replace('''                tab = np.zeros((2, 2, 4))
                code = x[m, :, j].astype(int) + 2 * x[m, :, k].astype(int)
                np.add.at(tab, (y[m, :, o].astype(int), 0, code), 1)''','''                code = xi[:, j] + 2 * xi[:, k] + 4 * yi[:, o]
                tab = np.zeros((2, 2, 4))
                tab[:, 0, :] = np.bincount(code, minlength=8).reshape(2, 4)''')
s=s.replace('''        c = conn[m]
        deg_in, deg_out = c.sum(0), c.sum(1)''','''        c = conn[m]
        xi, yi = x[m].astype(np.int64), y[m].astype(np.int64)
        deg_in, deg_out = c.sum(0), c.sum(1)''')
s=s.replace('''def _mi2(u, v):
    t = np.zeros((2, 2))
    np.add.at(t, (u.astype(int), v.astype(int)), 1)
    p = t / t.sum()''','''def _mi2(u, v):
    p = np.bincount(u.astype(np.int64) * 2 + v.astype(np.int64), minlength=4).reshape(2, 2) / len(u)''')
open('hdn.py','w').write(s)
EOF
cd $TMPDIR && source dev/bin/activate && python - <<'EOF' 2>&1 | grep -v -i warn | grep -v "tr = trains"
import sys,time,numpy as np
sys.path.insert(0,'entries/crcns-ssc-3-timme-2016')
import hdn
al,be=hdn.sigmoid_params(40)
rng=np.random.default_rng(0)
t=time.time(); c=hdn.build_models(40,'degree',rng,al,be,n_models=10); t1=time.time()-t
t=time.time(); r=hdn.model_correlations(c,rng,al,be,5000); t2=time.time()-t
print(t1,t2)
EOF
```

```
8.49064564704895 5.653257369995117
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/crcns-ssc-3-timme-2016 && python3 - <<'EOF'
s=open('hdn.py').read()
s=s.replace('cur = I_out[b] + I_CON * np.einsum("mri,mio->mro", x.astype(float), conn.astype(float))','cur = I_out[b] + I_CON * np.matmul(x.astype(np.float32), conn.astype(np.float32))')
s=s.replace('agree = (np.einsum("mri,mro->mio", xf, yf) + np.einsum("mri,mro->mio", 1 - xf, 1 - yf)) / MODEL_RUNS','xt = np.swapaxes(xf, 1, 2)\n        agree = (np.matmul(xt, yf) + np.matmul(1 - xt, 1 - yf)) / MODEL_RUNS')
s=s.replace('xf, yf = x.astype(float), y.astype(float)','xf, yf = x.astype(np.float32), y.astype(np.float32)')
open('hdn.py','w').write(s)
EOF
cd $TMPDIR && source dev/bin/activate && python - <<'EOF' 2>&1 | grep -v -i warn | grep -v "tr = trains"
import sys,time,numpy as np
sys.path.insert(0,'entries/crcns-ssc-3-timme-2016')
import hdn
al,be=hdn.sigmoid_params(40)
rng=np.random.default_rng(0)
t=time.time(); c=hdn.build_models(40,'degree',rng,al,be,n_models=10); t1=time.time()-t
print(t1, c.sum((1,2))[:3])
EOF
```

```
3.728431224822998 [320 320 320]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -i 's/MODEL_EVAL_RUNS = 5000/MODEL_EVAL_RUNS = 2000/; s/are computed from 5000 fresh runs per model/are computed from 2000 fresh runs per model/' mknb.py && source dev/bin/activate && python mknb.py && cd entries/crcns-ssc-3-timme-2016 && cat > requirements.in <<'EOF'
fsspec
aiohttp
requests
matplotlib
numba
numpy
pandas
scipy
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: crcns-ssc-3-timme-2016
type: reproduction
title: High-degree neurons feed cortical computations (Timme et al. 2016)
description: Tests the findings of Timme et al. (2016) on CRCNS ssc-3, the spike times of 25
  recordings of mouse somatosensory cortex slice cultures on a 512-electrode array. It rebuilds the
  transfer entropy networks at two time scales with the jitter test, and tests the weight and degree
  distributions, the correlations of synergy with in-degree and out-degree, the information gain,
  the partial information decomposition examples of Table 1, and the feedforward model.
license: Apache-2.0
notebooks:
- path: reproduce_timme_2016.ipynb
  title: Reproducing Timme et al. (2016) from CRCNS ssc-3
  runtime_minutes: 45
helpers:
- hdn.py
related:
- id: crcns:ssc-3/unversioned
  relation: uses_data
- id: doi:10.1371/journal.pcbi.1004858
  relation: reproduces
EOF
cd  && python tools/entry.py lock entries/crcns-ssc-3-timme-2016 2>&1 | tail -3 && python tools/entry.py check entries/crcns-ssc-3-timme-2016 2>&1 | tail -10; date -u
```

```
wrote entries/crcns-ssc-3-timme-2016/requirements.lock.txt
0 error(s)
Fri Nov  6 13:03:12 UTC 2026
```

**Agent calls Bash**

```bash
grep -n "max-minutes\|max_minutes" tools/entry.py | head -5; date -u; timeout 4500 python tools/entry.py all entries/crcns-ssc-3-timme-2016 2>&1 | tail -15; date -u
```

```
29:that takes longer than --max-minutes fails, even if it ran without error.
342:def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float) -> int:
371:        if ok and seconds > max_minutes * 60:
373:            error = f"took {seconds / 60:.0f} minutes; the limit is {max_minutes:.0f}"
433:    parser.add_argument("--max-minutes", type=float, default=60,
Fri Nov  6 13:03:17 UTC 2026
Installed kernelspec registry-crcns-ssc-3-timme-2016 in executed/crcns-ssc-3-timme-2016/.venv/share/jupyter/kernels/registry-crcns-ssc-3-timme-2016
0 error(s)
pass  reproduce_timme_2016.ipynb  (1727 s)
Fri Nov  6 13:32:11 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR && source dev/bin/activate && python - <<'EOF' > out.txt; wc -c out.txt
import nbformat
nb=nbformat.read('executed/crcns-ssc-3-timme-2016/reproduce_timme_2016.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type=='code':
        print(f"#### cell {i} tags={c.metadata.get('tags')}")
        for o in c.get('outputs',[]):
            if o.get('output_type')=='stream': print(o['text'])
            if o.get('output_type')=='error': print('ERROR',o['ename'],o['evalue'])
EOF
```

```
41942 out.txt
Shell cwd was reset to
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/out.txt"
}
```

```
1	#### cell 1 tags=None
2	CRCNS ssc-3 (10.6080/K07D2S2F), version unversioned: 25 recordings streamed in 9 s
3	MD5 of the streamed archive: 1a5bd3d304c5442290a7c9c1f1b5def6 | checksums.md5: 1a5bd3d304c5442290a7c9c1f1b5def6 | equal: True
4	
5	#### cell 3 tags=['sanity']
6	     file recording_id  nNeurons  trains  length_ms  first_ms    last_ms  spikes_min  spikes_max  under_100  sorted  on_50us_grid          x_um        y_um     timescale sampling
7	 DataSet1 2012-02-09-0       166     166  3600000.0   8005.85 3599995.65         105      113781          0    True          True  -960 to 1063 -608 to 575 1 millisecond   20 kHz
8	 DataSet2 2012-02-10-1       443     443  3600000.0   8001.90 3599983.50         100      116644          0    True          True -1051 to 1067 -562 to 600 1 millisecond   20 kHz
9	 DataSet3 2012-02-11-0        99      99  3600000.0   8010.80 3599487.50         769       98955          0    True          True   -944 to 768 -474 to 589 1 millisecond   20 kHz
10	 DataSet4 2012-02-12-0        98      98  3600000.0   8002.30 3598396.00         164       43409          0    True          True   -915 to 927 -395 to 602 1 millisecond   20 kHz
11	 DataSet5 2012-02-13-1       367     367  3600000.0   8000.00 3599988.90         105      118238          0    True          True -1009 to 1079 -559 to 603 1 millisecond   20 kHz
12	 DataSet6 2012-02-14-0       286     286  3600000.0   8002.25 3598476.65         115       57686          0    True          True  -1097 to 982 -578 to 570 1 millisecond   20 kHz
13	 DataSet7 2012-02-15-1       172     172  3600000.0   8000.05 3599401.10         115       25488          0    True          True   -953 to 945 -591 to 585 1 millisecond   20 kHz
14	 DataSet8 2012-02-16-1       191     191  3600000.0   8006.45 3598472.80         132       53838          0    True          True  -1003 to 896 -487 to 483 1 millisecond   20 kHz
15	 DataSet9 2012-02-17-0       333     333  3600000.0   8000.00 3599969.15         105       78
[... 469 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/results.py <<'PYEOF'
# Result markdown, inserted after the last cell carrying each claim tag
R = {
"claim:data-recordings": """**Result: reproduced.** The data set holds 25 recordings and 7735 neurons (309.4 per recording), every one with at least 100 spikes, so the deposit already applies the paper's threshold. The mean rate is 2.103 Hz with spikes counted over 60 min (reading b) and 2.132 Hz over each recording's own length (reading a); both are within 0.21 Hz of 2.10 Hz.""",
"claim:fig4ac-te-lognormal": """**Result: partially reproduced.** The significant TE values span several orders of magnitude: the 99th percentile is 1.17e5 to 2.93e5 times the 1st for raw TE and 1.84e3 to 5.43e3 times for normalized TE, at both time scales and under both readings (the smallest single-recording ratio is 2.71, normalized TE, reading s). Fits of the log-normal of Eq 21 to single recordings have a median R2 of 0.86 to 0.96, but the fit to the distribution averaged over recordings has R2 of 0.08 to 0.61, below the criterion's 0.9 in all eight cases, because the recordings' distributions sit at different places on the log axis and their average is broad and uneven. The criterion (R2 at least 0.9 on the average and a 100-fold spread) is met for the spread only.""",
"claim:fig4bd-heavy-tailed-degree": """**Result: reproduced.** Of the neurons, 20.9% (1.6 to 6.4 ms) and 21.1% (3.5 to 14 ms) have a total degree above the 99.9th percentile of matched random networks in the full networks, 209 and 210 times the 0.001 expected; in the sub-networks 5.9% and 6.4%. The largest real total degree is 886 and 929 (full) and 53 and 54 (sub-networks), against 223, 162, 13 and 14 in the random networks.""",
"claim:fig4bd-out-tail-longer": """**Result: reproduced, under the assumption that Fig 4 uses the sub-networks (reading s).** In the sub-networks the 99th percentile of out-degree is 19 and 23 against 8 and 7 for in-degree, the largest out-degree is 46 and 48 against 45 and 46, and the per-recording 99th percentile of out-degree is higher in 21 and 25 of 25 recordings (one-sided Wilcoxon p = 0.0001 and below 0.0001). In the full networks (reading f) the 99th percentiles also favour out-degree (242 against 234, 228.7 against 179; Wilcoxon p = 0.0015 and below 0.0001), but at 3.5 to 14 ms the largest in-degree (480) exceeds the largest out-degree (449), so that reading fails the criterion's second part.""",
"claim:fig5a-in-degree-uncorrelated": """**Result: partially reproduced, under the assumption of reading (s) with Pearson correlations.** Correlations between receiver in-degree and synergy are mostly negative: 41 of 50 under (s, Pearson), median r = -0.14, binomial probability of a negative skew this large 2.8e-6. That is the paper's slight negative skew, but significant, which the criterion counts as partial. Three of the four readings give a significant negative skew (40 or 41 of 50 negative); the full network with Spearman correlations gives 30 of 50 negative (p = 0.10, not significant), which would count as reproduced.""",
"claim:fig5b-out-degree-positive": """**Result: reproduced, under the assumption of reading (s).** Correlations between transmitter out-degree and synergy are positive in 44 of 50 recordings and time scales under (s, Pearson), median r = 0.19, binomial p = 1.6e-8; 39 of 50 under (s, Spearman), p = 4.5e-5; 35 of 50 under (f, Pearson), p = 0.0033. Under (f, Spearman) 26 of 50 are positive (p = 0.44), a majority without significance, which the criterion counts as partial.""",
"claim:fig5ab-correlations-beyond-null": """**Result: reproduced, under the assumption of reading (s).** Under (s) the null correlations from permuted degrees have a median absolute value of 0.002 to 0.003 and a 99th percentile of 0.008 to 0.013; 100% and 96% (Pearson) and 94% and 96% (Spearman) of the in-degree and out-degree correlations lie beyond it. Under (f) the fractions are 84% and 92% (Pearson), below 90% for in-degree, and 90% and 98% (Spearman).""",
"claim:fig5cd-pooled-trends": """**Result: not reproduced.** With all triples pooled, the per-degree median synergy falls steeply with receiver in-degree (Spearman rho = -0.96 and -0.94 under (s), -0.51 and -0.81 under (f)), which is not significantly positive, as the criterion requires, but is a trend where the paper reports none. The rise with transmitter out-degree is significant at 1.6 to 6.4 ms under (s) (rho = 0.57, p = 4e-5) and at 3.5 to 14 ms under (f) (rho = 0.34, p = 1.2e-8), but not at the other scale of either reading (rho = 0.14, p = 0.34 under (s); rho = -0.51 under (f)). No reading meets the criterion at both time scales.""",
"claim:fig6-information-gain-not-rising": """**Result: reproduced (on a sample of receivers).** The median information gain falls with the number of inputs at both time scales; fitted exponents are negative under all four readings (normalized or in bits, n from 1 or from 2), from -0.037 to -0.115, and no 95% interval lies above zero. The statement's further detail, that one of the two intervals overlaps zero, does not hold here: every interval lies below zero (for normalized gain from n = 2, -0.120 to -0.036 and -0.098 to -0.057). The gains come from 30 sampled receivers per recording and time scale (626 to 750 neurons per n) and at most 20 combinations per neuron and n.""",
"claim:table1-pid-examples": """**Result: reproduced.** On the distributions of Table 1, synergy is above 0.001 bits only in the synergistic (1.000 bit) and the synergistic and redundant (0.457 bits) examples. In the hidden self interaction MI(J_P; I_F) is 1 bit while TE and every PID term are 0. In the synergistic and redundant example the interaction information is 0.0001 bits while synergy and redundancy are 0.457 bits each. In the single and redundant example the unique information of J is 0.750 bits and the interaction information is -0.250 bits, the size of the redundancy (0.250 bits).""",
"claim:fig7c-degree-modified-rule-matches": """**Result: partially reproduced, under the assumption of reading (s) with Pearson correlations for the real data.** Against the real mean and standard deviation (in-degree -0.132 +- 0.155, out-degree 0.195 +- 0.170), the degree-modified (0.017, 0.114) and firing-rate-modified (-0.061, 0.280) models match, and the Hebbian (0.321, 0.022) and random (0.128, -0.009) models do not, as the paper says. But the firing-rate-modified rule is closer to the real data (distance 0.111) than the degree-modified rule (0.169), so the criterion's last part fails; it fails too under (s, Spearman) and (f, Pearson), and only (f, Spearman) meets the whole criterion. In 56 of 100 degree-modified models every output neuron ends with the same in-degree, so the in-degree correlation is undefined there; its mean is over the other 44.""",
"claim:fig7b-connectivity-patterns": """**Result: reproduced.** The fraction of connections leaving the upper half of the input layer is 0.988 for the Hebbian rule, 0.792 for the firing-rate-modified rule and 0.505 for the degree-modified rule (random wiring 0.502), in the order the criterion requires, with the degree-modified rule within 0.5 +- 0.1.""",
"claim:fig7d-degree-rule-highest-conditioned-mi": """**Result: not reproduced.** The Hebbian rule gives the highest unconditioned MI between connected neurons (0.090 bits, against 0.071, 0.030 and 0.023), as the paper says. Conditioned on the binary signal, the random model gives the highest MI (0.00230 bits) and the degree-modified rule the lowest (0.00153; Hebbian 0.00168, firing-rate 0.00166); the degree-modified rule differs from each other rule at FDR p < 0.001 but is below them, not above. These conditioned values are close to the bias of an MI estimated from 2000 runs split in two (about 0.0007 bits per stratum), so they rest on small differences.""",
"claim:figs1-larger-model": """**Result: not reproduced.** With 40 neurons per layer the connectivity ordering holds (Hebbian 0.991, firing-rate 0.769, degree 0.502 with alpha and beta recomputed; 0.999, 0.798, 0.501 with them kept). Under (s, Pearson) the degree-modified rule does not match the real correlations with recomputed alpha and beta (it does with them kept, where the firing-rate rule does not), its conditioned MI is below the random model's under both readings (0.00094 against 0.00112; 0.00100 against 0.00206), and the Hebbian and firing-rate rules' conditioned MI is smaller than in the 20-neuron model (0.00096 and 0.00097, or 0.00147 and 0.00146, against 0.00168 and 0.00166), not larger.""",
}
SUMMARY = """| Claim | Outcome |
|---|---|
| data-recordings | reproduced |
| fig4ac-te-lognormal | partially reproduced |
| fig4bd-heavy-tailed-degree | reproduced |
| fig4bd-out-tail-longer | reproduced (assumes sub-networks) |
| fig5a-in-degree-uncorrelated | partially reproduced (assumes sub-networks, Pearson) |
| fig5b-out-degree-positive | reproduced (assumes sub-networks) |
| fig5ab-correlations-beyond-null | reproduced (assumes sub-networks) |
| fig5cd-pooled-trends | not reproduced |
| fig6-information-gain-not-rising | reproduced |
| table1-pid-examples | reproduced |
| fig7b-connectivity-patterns | reproduced |
| fig7c-degree-modified-rule-matches | partially reproduced (assumes sub-networks, Pearson) |
| fig7d-degree-rule-highest-conditioned-mi | not reproduced |
| figs1-larger-model | not reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences from the paper's method.

How the analysis differs from the paper's. The paper reused TE networks computed for [44]; they are rebuilt here from the deposited spike times with the bins, past states, jitter window and threshold of [44], so they need not be the same networks. Which two bins form the past state is read from the delay windows both papers state, not from [44]'s text, which implies other bins. For pairs whose jitter moves more than 50 relevant spikes the surrogate counts are drawn from a normal distribution with their exact moments; on two recordings this agrees with the full jitter on 99.5% and 99.6% of the significant connections. The full-network triples are sampled (3000 per recording and time scale), and the information gain uses 30 receivers per recording and time scale and at most 20 combinations per n (the paper: all receivers, 100 combinations). The model's synergy is the PID of two input states about the output state in the same run, without the receiver's past, which the model does not have; MI and synergy use 2000 fresh runs per model.

What was found about the data set. The deposit matches the paper's description: 25 recordings, 7735 neurons, all with at least 100 spikes, a mean rate of 2.10 Hz, spike times on the 20 kHz grid. One recording (DataSet19) lasts 48 min, not 60. The first ten recordings have no spikes in their first 8 s. The networks of [44] that the paper analysed are not deposited, so the networks have to be rebuilt."""
PYEOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('results.py').read()
s=s.replace("the 99th percentile is 1.17e5 to 2.93e5 times the 1st for raw TE","the 99th percentile is 8.0e4 to 2.93e5 times the 1st for raw TE")
s=s.replace(" These conditioned values are close to the bias of an MI estimated from 2000 runs split in two (about 0.0007 bits per stratum), so they rest on small differences."," All conditioned values are small (0.0015 to 0.0023 bits), so the ordering rests on small differences.")
open('results.py','w').write(s)
EOF
cat > $TMPDIR/addres.py <<'EOF'
import nbformat, sys
sys.path.insert(0, sys.argv[2])
from results import R, SUMMARY
nb = nbformat.read(sys.argv[1], 4)
cells = [c for c in nb.cells if not (c.cell_type == "markdown" and c.source.startswith("**Result:"))]
out = []
last = {}
for i, c in enumerate(cells):
    for t in c.metadata.get("tags", []):
        if t.startswith("claim:"):
            last[t] = i
for i, c in enumerate(cells):
    out.append(c)
    if c.cell_type == "markdown" and c.source.strip() == "## Summary":
        out.append(nbformat.v4.new_markdown_cell(SUMMARY))
    for t, j in last.items():
        if j == i:
            out.append(nbformat.v4.new_markdown_cell(R[t]))
# drop a duplicated summary table if re-run
nb.cells = out
nbformat.write(nb, sys.argv[1])
print(len(out))
EOF
cd $TMPDIR && source dev/bin/activate && python addres.py entries/crcns-ssc-3-timme-2016/reproduce_timme_2016.ipynb $TMPDIR && python addres.py executed/crcns-ssc-3-timme-2016/reproduce_timme_2016.ipynb $TMPDIR
```

```
53
53
Shell cwd was reset to
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
print(json.dumps(s,indent=0)[:6000])"; sed -n 150,400p attempts/001453-fouke-2025-01.yaml | grep -n "findings" -A30 | head -60
```

```
{
"$schema": "https://json-schema.org/draft/2020-12/schema",
"title": "One attempt at reproducing the claims of a target",
"description": "Draft. To be revised after the pilot. An attempt is recorded whether or not it produced a working notebook.",
"type": "object",
"additionalProperties": false,
"required": [
"schema_version",
"id",
"dataset",
"paper",
"date",
"provenance",
"outcomes"
],
"properties": {
"schema_version": {
"const": 2
},
"id": {
[... 294 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
p=s['properties']
for k in ['inputs','findings','verifications']:
  print(k, json.dumps(p.get(k),indent=0)[:1500])
print(list(p))"; date -u
```

```
inputs {
"description": "Everything the attempt used that is not in the dataset.",
"type": "array",
"items": {
"type": "object",
"additionalProperties": false,
"required": [
"what",
"source"
],
"properties": {
"what": {
"type": "string",
"minLength": 1
},
"source": {
"description": "A DOI, or a repository URL with the commit read.",
"type": "string",
"minLength": 1
}
[... 112 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/mkatt.py <<'PYEOF'
import yaml
NB = "reproduce_timme_2016.ipynb"
D_TE = ("The TE networks are rebuilt from the deposited spike times; the paper reused the networks of its reference [44] (Timme et al. 2014, PLoS One 9 e115764), which are not deposited. "
        "Bins of 1.6 and 3.5 ms, past states the OR of two bins, a 7-bin uniform jitter, 5000 surrogates and fewer than 5 exceeding are taken from [44], Table 1 and Transfer Entropy Analysis, paragraphs 3 and 6, as the paper directs (Methods, Effective Connectivity Detection, paragraphs 1 and 4).")
D_PAST = ("Assumed which two bins form the past state. [44]'s text writes bins t-d and t-d-1 (with d = 1, bins t-1 and t-2, delays of 0 to 2 bins), while its Table 1 and the paper give a delay window of 1 to 4 bins (1.6 to 6.4 ms and 3.5 to 14 ms), which bins t-2 and t-3 give. "
          "Bins t-2 and t-3 are used, the version both papers state in numbers. The other reading was not run.")
D_GAUSS = ("For pairs whose jitter moves more than 50 relevant sender spikes, the surrogate counts are drawn from a normal distribution with their exact mean and covariance (merged groups of close spikes from 50 joint draws), not by jittering every spike, to fit the time limit. "
           "On DataSet1 and DataSet7 at 1.6 ms, the full jitter finds 2937 and 3530 significant connections and the approximation 2946 and 3542, with 2930 and 3512 in common. The number of past states equal to 1 is held at its real value in each surrogate, as [44] states the jitter preserved it.")
D_SUB = ("Sub-networks follow [44], Topology Analysis - Sub-Networks, paragraph 2: 50 random neurons, unconnected ones replaced from the pool, then the 75 strongest connections by normalized TE kept (reading (a) of the claims file's M-SUB).")
D_SF = ("Assumed that the degree and synergy analyses use the sub-networks (reading s of M-SUB), as the paper says they were made 'to reduce bias associated with average degree and network size' (Methods, Effective Connectivity Detection, paragraph 5) and the Fig 4 legend matches the random networks' 'sampling statistics to the real data'. Both readings are shown.")
D_PEARSON = ("Assumed Pearson correlations (reading p of M-CORR), the default correlation of the Matlab the paper used for its fits; Spearman is shown.")
D_FULL = "Under reading (f) the triples of each full network are sampled, 3000 per recording and time scale (the full networks hold up to 2.8 million triples), for time."
D_N50 = "The panels hold 50 correlations (25 recordings, two time scales), where the Fig 5 legend gives N data = 40; which 40 the paper used is not stated."

att = {
 "schema_version": 2,
 "id": "crcns-ssc-3-timme-2016-01",
 "dataset": {"archive": "crcns", "id": "ssc-3", "version": "unversioned", "doi": "10.6080/K07D2S2F"},
 "paper": "doi:10.1371/journal.pcbi.1004858",
 "date": "2026-11-06",
 "entry": "crcns-ssc-3-timme-2016",
 "provenance": {"kind": "agent", "accountable": {"name": "CatalystNeuro"},
                "agent": {"harness": "Claude Code", "model": "claude-opus-5-5", "protocol": "pilot-13"},
                "runner": {"platform": "GitHub Actions", "url": "https://github.com/catalystneuro/encore/actions/runs/42206111011"}},
 "inputs": [
  {"what": "The displayed equations of the paper (Eqs 1 to 24), missing from the flattened text under paper/, read from the version of record's JATS XML. Methods only; no data.",
   "source": "doi:10.1371/journal.pcbi.1004858 (PMC4861348, Europe PMC fullTextXML)"},
  {"what": "The TE procedure the paper reuses (bin sizes, delay windows, past states, jitter window, surrogates, sub-network procedure), from the paper's reference [44]. Methods only; no data.",
   "source": "doi:10.1371/journal.pone.0115764 (PMC4275261)"},
 ],
 "outcomes": [],
 "findings": [],
}
O = att["outcomes"]
def out(claim, outcome, notes, deviations, measured=None, assumed=None):
    d = {"claim": claim, "outcome": outcome, "notebook": NB, "output": f"claim:{claim}"}
    if measured is not None: d["measured"] = measured
    if assumed: d["assumed"] = True
    d["notes"] = notes
    d["deviations"] = deviations
    O.append(d)

out("data-recordings", "reproduced",
    "25 recordings, 7735 neurons, 309.4 per recording, every neuron with at least 100 spikes, so the deposit already applies the 100-spike threshold. Mean rate 2.103 Hz with spikes over 60 min (reading b), 2.132 Hz over each recording's own length (reading a); both within tolerance. Rates range from 0.028 to 77.5 Hz.",
    ["The rate can be read two ways (criterion); both match, and the measured value is reading (b), spikes over 60 min, since reading (a) is listed first but both pass. One recording (DataSet19) lasts 48 min."],
    measured=[25, 7735, 309.4, 2.103])
O[-1]["deviations"] = ["The rate can be read two ways (criterion), spikes over each recording's length (a, 2.132 Hz) or over 60 min (b, 2.103 Hz); both match. The measured value given is (b), as it matches the paper's printed 2.10 Hz to the digit; (a) also passes."]
out("fig4ac-te-lognormal", "partially_reproduced",
    "Significant TE values span several orders of magnitude at both time scales and under both readings; the 99th percentile is 8.0e4 to 2.93e5 times the 1st for raw TE and 1.84e3 to 5.43e3 times for normalized TE. Fits of Eq 21 to single recordings have a median R2 of 0.86 to 0.96, but fits to the distribution averaged over recordings have R2 of 0.08 to 0.61, below the criterion's 0.9 in all eight cases (two scales, raw and normalized, readings f and s). The averaged distribution is broad because the recordings' distributions sit at different places on the log axis. The spread part of the criterion holds; the log-normal fit on the average does not.",
    [D_TE, D_PAST, D_GAUSS, "The fit starts from the moments of the binned distribution; the paper gives no starting values. 100 log-spaced bins span the pooled range of each panel."])
out("fig4bd-heavy-tailed-degree", "reproduced",
    "Full networks: 20.9% (1.6 to 6.4 ms) and 21.1% (3.5 to 14 ms) of neurons have a total degree above the 99.9th percentile of matched random networks (100 per recording), 209 and 210 times 0.001; largest real total degree 886 and 929 against 223 and 162. Sub-networks: 5.9% and 6.4% of neuron slots above the random 99.9th percentile (one random network per sub-network); largest 53 and 54 against 13 and 14. Both readings meet the criterion.",
    [D_TE, D_PAST, D_GAUSS, D_SUB])
out("fig4bd-out-tail-longer", "reproduced",
    "Sub-networks (s): pooled 99th percentile of out-degree 19 and 23 against in-degree 8 and 7; largest 46 and 48 against 45 and 46; out-degree 99th percentile higher in 21 and 25 of 25 recordings (one-sided Wilcoxon p = 0.0001 and below 0.0001). Full networks (f): 99th percentiles 242 against 234 and 228.7 against 179 (Wilcoxon p = 0.0015 and below 0.0001), but at 3.5 to 14 ms the largest in-degree (480) exceeds the largest out-degree (449), so (f) fails the criterion's second part. The outcome rests on reading (s).",
    [D_TE, D_PAST, D_GAUSS, D_SUB, D_SF], assumed=True)
out("fig5a-in-degree-uncorrelated", "partially_reproduced",
    "Under (s, Pearson) 41 of 50 correlations between receiver in-degree and synergy are negative, median r = -0.14, binomial probability of a negative skew this large 2.8e-6 (1.6 to 6.4 ms alone 22 of 25 negative, p = 7.8e-5; 3.5 to 14 ms 19 of 25, p = 0.0073). Under (s, Spearman) 40 of 50 negative (p = 1.2e-5), under (f, Pearson) 40 of 50 (p = 1.2e-5), under (f, Spearman) 30 of 50 (p = 0.10, not significant). Three of four readings give a significant negative skew (partial by the criterion); (f, Spearman) would give reproduced. The skew is in the direction the paper reports ('slight negative skew') but significant, so the statement's 'computation is independent of in-degree' does not hold under the adopted reading.",
    [D_TE, D_PAST, D_GAUSS, D_SUB, D_SF, D_PEARSON, D_FULL, D_N50,
     "Synergy is normalized by H(I_F) (paper, paragraph after Eq 10); the receiver's past state is the same two OR'ed bins as in the TE."], assumed=True)
out("fig5b-out-degree-positive", "reproduced",
    "Under (s, Pearson) 44 of 50 correlations between transmitter out-degree and synergy are positive, median r = 0.19, binomial p = 1.6e-8 (21 of 25 and 23 of 25 at each time scale). (s, Spearman) 39 of 50, p = 4.5e-5; (f, Pearson) 35 of 50, p = 0.0033; (f, Spearman) 26 of 50, p = 0.44, a majority without significance (partial by the criterion).",
    [D_TE, D_PAST, D_GAUSS, D_SUB, D_SF, D_PEARSON, D_FULL, D_N50], assumed=True)
out("fig5ab-correlations-beyond-null", "reproduced",
    "Ten permutations per correlation (500 null values for 50 correlations). Under (s) the null absolute correlations have median 0.002 to 0.003 and 99th percentile 0.008 to 0.013; beyond it are 100% (in) and 96% (out) of the Pearson correlations and 94% and 96% of the Spearman ones. Under (f) 84% and 92% (Pearson, in-degree below 90%) and 90% and 98% (Spearman).",
    [D_SF, D_PEARSON, D_N50], assumed=True)
out("fig5cd-pooled-trends", "not_reproduced",
    "Pooled over recordings, per-degree median synergy (degrees with at least 20 groups) against degree. Out-degree: Spearman rho = 0.57 (p = 4e-5) at 1.6 to 6.4 ms and 0.14 (p = 0.34) at 3.5 to 14 ms under (s); -0.51 (p = 3e-20) and 0.34 (p = 1.2e-8) under (f). In-degree: rho = -0.96 and -0.94 under (s), -0.51 and -0.81 under (f), all with p below 1e-17; not significantly positive, as the criterion requires, but a strong falling trend where the paper reports none. No reading has a significant rise with out-degree at both time scales.",
    [D_SF, D_FULL, "The criterion's Spearman correlation of per-degree medians is a reading fixed by the claims file; the paper gives no test."])
out("fig6-information-gain-not-rising", "reproduced",
    "Median information gain against the number of inputs n, fit with A exp(k n). k is negative at both time scales under all four readings (normalized or in bits, n from 1 or 2), from -0.037 to -0.115, and every 95% interval lies below zero. The statement's detail that one of the two intervals overlaps zero does not hold: none does. 626 to 750 neurons contribute per n.",
    [D_TE, D_PAST, D_GAUSS,
     "30 receivers sampled per recording and time scale, and at most 20 combinations of inputs per receiver and n, where the paper uses every receiver and up to 100 combinations (Methods, paragraph after Eq 11); for time.",
     "Inputs are the significant inputs of the full network (reading f); reading (s) was not run, although sub-network receivers with six or more inputs exist (19205 and 14814 over the sub-networks)."])
out("table1-pid-examples", "reproduced",
    "Synergy is 1.000 bit in the synergistic and 0.457 bits in the synergistic and redundant example and zero (below 0.001) in the other six. Hidden self interaction, MI(J_P; I_F) = 1 bit with TE and every PID term 0. Synergistic and redundant, II = 0.0001 bits with synergy and redundancy 0.457 bits each. Single and redundant, unique J = 0.750 bits and II = -0.250 bits, equal in size to the redundancy (0.250).",
    ["Table 1's printed values are typed into the notebook and each column renormalized to sum to 1, as the criterion says."])
D_MODEL = ("The model follows the Methods and Eqs 13 to 24 of the version of record (read from its JATS XML). The firing probabilities of Eqs 16 to 19 are turned into the binary signal's current by inverting Eq 13; output current adds I_con = 10 per active connected input. Each rewiring step uses 500 fresh runs; 100 models per type.")
D_MSYN = ("The model's synergy is the PID of the states of two connected input neurons about the output neuron's state in the same run, without conditioning on a past, which the model's independent runs do not have (the claims file's reading); 2000 fresh runs per model. Correlations per model as for the data; models whose output in-degrees are all equal have no in-degree correlation (56 of 100 degree-modified models).")
D_REAL = "The real data's reference is the mean and standard deviation of the 50 per-recording correlations under (s, Pearson); the other three readings are shown."
out("fig7b-connectivity-patterns", "reproduced",
    "Fraction of connections from the upper half of the input layer, averaged over 100 models: Hebbian 0.988, firing-rate-modified 0.792, degree-modified 0.505, random 0.502. Ordered as required, with the degree-modified rule within 0.5 +- 0.1.",
    [D_MODEL])
out("fig7c-degree-modified-rule-matches", "partially_reproduced",
    "Real data (s, Pearson): in-degree -0.132 +- 0.155, out-degree 0.195 +- 0.170. Model means (in, out): degree-modified 0.017, 0.114 (match), firing-rate-modified -0.061, 0.280 (match), Hebbian 0.321, 0.022 (no match), random 0.128, -0.009 (no match). The firing-rate rule is closer to the real data (distance 0.111) than the degree rule (0.169), so the criterion's last part fails. Under (s, Spearman) and (f, Pearson) the same part fails (and under (f, Pearson) the degree rule does not match); under (f, Spearman) the whole criterion holds. The qualitative match of the two modified rules and the mismatch of the Hebbian and random models hold; that the degree-modified rule is closer does not.",
    [D_MODEL, D_MSYN, D_REAL, D_SF, D_PEARSON], assumed=True)
out("fig7d-degree-rule-highest-conditioned-mi", "not_reproduced",
    "Mean MI between connected neurons over 100 models: Hebbian 0.090 bits (highest, as the paper says), firing-rate 0.071, degree 0.030, random 0.023. Conditioned on the binary signal: random 0.00230 (highest), Hebbian 0.00168, firing-rate 0.00166, degree 0.00153 (lowest). The degree-modified rule differs from each other rule at FDR-corrected p < 0.001 (Mann-Whitney) but lies below them. The conditioned values are small, so the ordering rests on small differences.",
    [D_MODEL, "MI is estimated from 2000 fresh runs per model, a count the paper does not give (the claims file's reading)."])
out("figs1-larger-model", "not_reproduced",
    "40 neurons per layer, 320 connections and rewirings, Eq 24 and Eq 23. Connectivity ordering holds (upper-half fractions 0.991, 0.769, 0.502 with alpha and beta recomputed from Eq 15; 0.999, 0.798, 0.501 with them kept). Under (s, Pearson) the degree-modified rule does not match the real correlations with alpha and beta recomputed (it does with them kept, where the firing-rate rule does not); its conditioned MI is below the random model's under both readings (0.00094 against 0.00112; 0.00100 against 0.00206); the Hebbian and firing-rate rules' conditioned MI is smaller than in the 20-neuron model (0.00096 and 0.00097, or 0.00147 and 0.00146, against 0.00168 and 0.00166). Under the Spearman readings the correlation match holds for both alpha and beta readings, but the MI parts fail under every reading.",
    [D_MODEL, D_MSYN, D_REAL, "Both readings of alpha and beta named in the criterion are run (recomputed from Eqs 14 and 15 with N = 40, alpha = 0.0115; kept at 0.023); neither meets the criterion."])

F = att["findings"]
F.append({"kind": "data_missing", "statement": "The paper analysed the TE networks of its reference [44] (Timme et al. 2014), at time scales 2 and 3 of that study. The networks, the TE values and the sub-networks are not in the data set, which holds spike times only, so the paper's networks cannot be checked; they have to be rebuilt, and a rebuilt network may differ from the paper's."})
F.append({"kind": "other", "statement": "DataSet19 (2013-01-06-1) lasts 2887498 ms (48 min), where the paper describes 60 minute recordings; the data description says most recordings are 3600000 ms. The first ten recordings (2012) have no spike in their first 8 s."})
F.append({"kind": "methods_unavailable", "statement": "Question for the paper's authors: which bins form the past states of the TE? [44] writes the past as bins t-d and t-d-1 (d = 1), which gives delays of 0 to 2 bins, while its Table 1 and this paper give delay windows of 1.6 to 6.4 ms and 3.5 to 14 ms (1 to 4 bins), which bins t-2 and t-3 give. This attempt used t-2 and t-3."})
F.append({"kind": "methods_unavailable", "statement": "Question for the paper's authors: were the weight distributions (Fig 4A, C), degree distributions (Fig 4B, D) and the degree and synergy correlations (Fig 5) computed on the 500 sub-networks per recording or on the full networks, and were the correlations Pearson or Spearman? The outcomes differ: the out-degree tail (Fig 4B, D) is longer than the in-degree tail on the sub-networks but not in every comparison on the full networks, and the out-degree correlations (Fig 5B) are significantly positive under three of four readings but not under full networks with Spearman. This attempt assumed sub-networks and Pearson."})
F.append({"kind": "methods_unavailable", "statement": "Question for the paper's authors: Fig 5 gives N data = 40 correlations per panel; with 25 recordings and two time scales there are 50. Which 40 were used?"})
F.append({"kind": "methods_unavailable", "statement": "Question for the paper's authors: how was the synergy of the feedforward model computed, given that its runs are independent and have no past to condition on, and from how many runs were the model's synergy and mutual information estimated?"})

open("attempts/crcns-ssc-3-timme-2016-01.yaml", "w").write(
    yaml.safe_dump(att, sort_keys=False, width=100, allow_unicode=True))
PYEOF
cd $TMPDIR && source dev/bin/activate && python mkatt.py && grep -n ": .*: " attempts/crcns-ssc-3-timme-2016-01.yaml | grep -v "^\S*\s*- \?['\"]" | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('mkatt.py').read()
s=s.replace('measured=[25, 7735, 309.4, 2.103])','measured=[25, 7735, 309.4, 2.132])')
s=s.replace('''O[-1]["deviations"] = ["The rate can be read two ways (criterion), spikes over each recording's length (a, 2.132 Hz) or over 60 min (b, 2.103 Hz); both match. The measured value given is (b), as it matches the paper's printed 2.10 Hz to the digit; (a) also passes."]''','''O[-1]["deviations"] = ["The rate can be read two ways (criterion), spikes over each recording's length (a, 2.132 Hz) or over 60 min (b, 2.103 Hz); both match, and the measured value is (a), the first reading the criterion lists."]''')
open('mkatt.py','w').write(s)
EOF
source $TMPDIR/dev/bin/activate && python $TMPDIR/mkatt.py && cat > entries/crcns-ssc-3-timme-2016/README.md <<'EOF'
# Timme et al. (2016) from CRCNS ssc-3

Tests the findings of [Timme et al. (2016)](https://doi.org/10.1371/journal.pcbi.1004858), "High-Degree
Neurons Feed Cortical Computations", on [CRCNS ssc-3](https://doi.org/10.6080/K07D2S2F): spike times
of 7735 neurons in 25 recordings of mouse somatosensory cortex slice cultures on a 512-electrode
array.

| Claim | Outcome |
|---|---|
| 25 recordings, 7735 neurons, 2.10 Hz | Reproduced |
| TE weights roughly log-normal, over several orders of magnitude | Partially reproduced |
| Degree distributions heavy-tailed | Reproduced |
| Out-degree tail longer than in-degree tail | Reproduced (assumes sub-networks) |
| Synergy and receiver in-degree uncorrelated, slight negative skew | Partially reproduced (assumes sub-networks, Pearson) |
| Synergy correlates positively with transmitter out-degree | Reproduced (assumes sub-networks) |
| Correlations beyond a permutation null | Reproduced (assumes sub-networks) |
| Pooled trends of synergy with degree | Not reproduced |
| Information gain does not rise with inputs | Reproduced |
| PID on the examples of Table 1 | Reproduced |
| Model connectivity patterns (Fig 7B) | Reproduced |
| Model correlations match the data, degree rule closest (Fig 7C) | Partially reproduced (assumes sub-networks, Pearson) |
| Degree rule highest conditioned MI (Fig 7D) | Not reproduced |
| Larger model (S1 Fig) | Not reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper analysed the TE networks of its reference [44] (Timme et al. 2014), which are not
deposited; the notebook rebuilds them from the spike times with that study's bins, past states and
jitter test. The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/crcns-ssc-3-timme-2016-01.yaml`](../../attempts/crcns-ssc-3-timme-2016-01.yaml).

- `reproduce_timme_2016.ipynb`: the analysis. It takes about 30 minutes on four cores, most of it
  the jitter tests of the TE networks.
- `hdn.py`: loading the data set, the TE networks with their jitter test, sub-networks, the partial
  information decomposition, the information gain and the feedforward model. Other notebooks on this
  data set can import it.
EOF
python tools/entry.py check entries/crcns-ssc-3-timme-2016 2>&1 | tail -5; python tools/entry.py handover entries/crcns-ssc-3-timme-2016 2>&1 | tail -3; date -u
```

```
/bin/bash: line 7: entries/crcns-ssc-3-timme-2016/README.md: No such file or directory
python: can't open file '/tmp/claude-1001/tools/entry.py': [Errno 2] No such file or directory
python: can't open file '/tmp/claude-1001/tools/entry.py': [Errno 2] No such file or directory
Fri Nov  6 13:34:54 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat > entries/crcns-ssc-3-timme-2016/README.md <<'EOF'
# Timme et al. (2016) from CRCNS ssc-3

Tests the findings of [Timme et al. (2016)](https://doi.org/10.1371/journal.pcbi.1004858), "High-Degree
Neurons Feed Cortical Computations", on [CRCNS ssc-3](https://doi.org/10.6080/K07D2S2F): spike times
of 7735 neurons in 25 recordings of mouse somatosensory cortex slice cultures on a 512-electrode
array.

| Claim | Outcome |
|---|---|
| 25 recordings, 7735 neurons, 2.10 Hz | Reproduced |
| TE weights roughly log-normal, over several orders of magnitude | Partially reproduced |
| Degree distributions heavy-tailed | Reproduced |
| Out-degree tail longer than in-degree tail | Reproduced (assumes sub-networks) |
| Synergy and receiver in-degree uncorrelated, slight negative skew | Partially reproduced (assumes sub-networks, Pearson) |
| Synergy correlates positively with transmitter out-degree | Reproduced (assumes sub-networks) |
| Correlations beyond a permutation null | Reproduced (assumes sub-networks) |
| Pooled trends of synergy with degree | Not reproduced |
| Information gain does not rise with inputs | Reproduced |
| PID on the examples of Table 1 | Reproduced |
| Model connectivity patterns (Fig 7B) | Reproduced |
| Model correlations match the data, degree rule closest (Fig 7C) | Partially reproduced (assumes sub-networks, Pearson) |
| Degree rule highest conditioned MI (Fig 7D) | Not reproduced |
| Larger model (S1 Fig) | Not reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper analysed the TE networks of its reference [44] (Timme et al. 2014), which are not
deposited; the notebook rebuilds them from the spike times with that study's bins, past states and
jitter test. The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/crcns-ssc-3-timme-2016-01.yaml`](../../attempts/crcns-ssc-3-timme-2016-01.yaml).

- `reproduce_timme_2016.ipynb`: the analysis. It takes about 30 minutes on four cores, most of it
  the jitter tests of the TE networks.
- `hdn.py`: loading the data set, the TE networks with their jitter test, sub-networks, the partial
  information decomposition, the information gain and the feedforward model. Other notebooks on this
  data set can import it.
EOF
python tools/entry.py check entries/crcns-ssc-3-timme-2016 2>&1 | tail -5; python tools/entry.py handover entries/crcns-ssc-3-timme-2016 2>&1 | tail -3; git status --short
```

```
0 error(s)
wrote executed/crcns-ssc-3-timme-2016/handover
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
?? attempts/crcns-ssc-3-timme-2016-01.yaml
?? entries/crcns-ssc-3-timme-2016/
?? scripts
```

**Agent calls Bash**

```bash
ls -la .bash_profile .bashrc .gitconfig .mcp.json .profile .ripgreprc .zprofile .zshrc; ls -la .idea .vscode scripts | head; ls entries/crcns-ssc-3-timme-2016/
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  6 10:53 .bash_profile
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  6 10:53 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  6 10:53 .gitconfig
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  6 10:53 .mcp.json
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  6 10:53 .profile
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  6 10:53 .ripgreprc
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  6 10:53 .zprofile
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  6 10:53 .zshrc
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  6 10:53 .idea
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  6 10:53 .vscode
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  6 10:53 scripts
README.md
__pycache__
entry.yaml
hdn.py
reproduce_timme_2016.ipynb
requirements.in
requirements.lock.txt
```

**Agent calls Bash**

```bash
rm -rf entries/crcns-ssc-3-timme-2016/__pycache__; for f in entries/crcns-ssc-3-timme-2016/reproduce_timme_2016.ipynb executed/crcns-ssc-3-timme-2016/reproduce_timme_2016.ipynb; do sed -i 's/with their exact moments, in place of jittering every spike. The data check section compares the/with their exact moments, in place of jittering every spike. The first cell of the TE networks section compares the/' $f; grep -c "first cell of the TE networks section" $f; done; python tools/entry.py check entries/crcns-ssc-3-timme-2016 | tail -1; python tools/entry.py handover entries/crcns-ssc-3-timme-2016 | tail -1; grep -c '\*\*Result' executed/crcns-ssc-3-timme-2016/handover/*.ipynb; ls executed/crcns-ssc-3-timme-2016/handover/; date -u
```

```
1
1
0 error(s)
wrote executed/crcns-ssc-3-timme-2016/handover
0
10.1371-journal.pcbi.1004858.yaml
hdn.py
reproduce_timme_2016.ipynb
Fri Nov  6 13:35:50 UTC 2026
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/crcns-ssc-3-timme-2016/hdn.py",
 "old_string": "  test stops early once 5 surrogates exceed the real TE, which cannot change the decision.",
 "new_string": "  test stops early once 5 surrogates exceed the real TE, which cannot change the decision.\n  For pairs whose jitter moves more than `exact_max` (50 in the notebook) relevant sender spikes,\n  the surrogate counts are drawn from a normal distribution with their exact moments in place of\n  jittering every spike: a deviation, made for the time limit, whose agreement with the full\n  jitter the notebook shows on two recordings."
}
```

```
The file entries/crcns-ssc-3-timme-2016/hdn.py has been updated successfully. (note: the file had been modified on disk since you last read it — the edit applied cleanly, but the file contains other changes not in your context. Read it before edits that depend on surrounding content.)
```

**Agent calls Bash**

```bash
python tools/entry.py check entries/crcns-ssc-3-timme-2016 | tail -1; python tools/entry.py handover entries/crcns-ssc-3-timme-2016 | tail -1; rm -rf entries/crcns-ssc-3-timme-2016/__pycache__; git status --short | grep -v "^?? \.\|scripts"
```

```
0 error(s)
wrote executed/crcns-ssc-3-timme-2016/handover
?? attempts/crcns-ssc-3-timme-2016-01.yaml
?? entries/crcns-ssc-3-timme-2016/
```

**Agent**

All 14 claims were tested and none is blocked. The entry passes `check`, ran clean under `entry.py all` in 28.8 minutes (limit 60), and the handover package is built. Nothing is committed.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| data-recordings | reproduced |
| fig4ac-te-lognormal | partially reproduced: the values do span orders of magnitude, but the log-normal fit to the distribution averaged over recordings has R² 0.08 to 0.61, below the required 0.9 |
| fig4bd-heavy-tailed-degree | reproduced |
| fig4bd-out-tail-longer | reproduced, rests on an assumption (sub-networks) |
| fig5a-in-degree-uncorrelated | partially reproduced, rests on an assumption (sub-networks, Pearson): the negative skew is significant, 41 of 50 negative |
| fig5b-out-degree-positive | reproduced, rests on an assumption (sub-networks): 44 of 50 positive |
| fig5ab-correlations-beyond-null | reproduced, rests on an assumption (sub-networks) |
| fig5cd-pooled-trends | not reproduced: the out-degree rise is not significant at both time scales, and synergy falls steeply with in-degree |
| fig6-information-gain-not-rising | reproduced: all exponents negative, though none of the intervals overlaps zero as the paper says one does |
| table1-pid-examples | reproduced |
| fig7b-connectivity-patterns | reproduced |
| fig7c-degree-modified-rule-matches | partially reproduced, rests on an assumption (sub-networks, Pearson): the firing-rate rule fits the data more closely than the degree rule |
| fig7d-degree-rule-highest-conditioned-mi | not reproduced: the random model has the highest conditioned MI and the degree rule the lowest |
| figs1-larger-model | not reproduced |

**2. Dataset, assumptions and questions**

- **Dataset:** the files match the paper: 25 recordings, 7735 neurons all with at least 100 spikes, 2.10 Hz mean rate, spike times on the 20 kHz grid, and no recording deposited twice.
  - DataSet19 lasts 48 min, not 60, and the first ten recordings have no spikes in their first 8 s.
  - The paper's TE networks (taken from its reference [44], Timme et al. 2014) are not deposited, so I rebuilt them from the spike times.
- **Version:** CRCNS does not version data sets, so it is recorded as `unversioned`, with the MD5 of `data.tar.gz`. The notebook checks the streamed bytes against that sum. The paper cites the DOI with no version, and the bucket holds only `live/`.
- **Method sources:** the flattened paper text had lost every equation (Eqs 1 to 24), so I read them from the version of record's XML on Europe PMC. The TE details (1.6 and 3.5 ms bins, a 7-bin jitter, the sub-network procedure) come from [44]. Both are listed under `inputs`.
- **Assumptions:**
  - The past state of each neuron is the OR of bins t-2 and t-3. That matches the delay windows both papers state; [44]'s own text implies bins t-1 and t-2.
  - The degree and synergy analyses use the 500 sub-networks per recording, not the full networks.
  - Correlations are Pearson. Every other reading is shown in the notebook.
- **Questions for the paper's authors** (recorded as `methods_unavailable` findings):
  - Which bins form the TE past state?
  - Were Fig 4 and Fig 5 computed on the sub-networks or the full networks, and with Pearson or Spearman correlations?
  - Fig 5 says N data = 40, but 25 recordings at two time scales give 50 correlations. Which 40?
  - How was the model's synergy computed, given that its runs have no past to condition on?
- **Questions to a reader:** none.

**3. Where the protocol was unclear, wrong or missing something**

1. The paper text under `paper/` had no equations and the claims file said the model claims needed them. The protocol does not say whether fetching the version of record counts as "the paper". I fetched it and recorded it as an input.
2. The method lives in a cited earlier paper ([44]), not in this paper or any linked code. Step 1.6 only mentions "the methods it cites" for assumptions. I took the details from [44], cited the passages, and listed it under inputs.
3. The protocol has no way to approximate a method that is too expensive to run in full. The paper's 5000 jittered surrogates per pair, run exactly, would take more than an hour. For pairs whose jitter moves more than 50 relevant spikes, I drew the surrogate counts from a normal distribution with their exact moments. On two recordings the significant connections agree 99.5% with the full jitter. Recorded as a deviation.
4. The "Time" rule covers the run's deadline but not the notebook's 60-minute limit applying to a part of the method. I sampled at fixed sizes and recorded each as a deviation: full-network triples (3000 per recording and time scale), and for the information gain 30 receivers and up to 20 input combinations per n. The paper used every receiver and 100 combinations.
5. The clock check in step 2 assumes trial tables or other data streams. This data set has spike times only, so I stated that the check does not apply.
6. CRCNS has no versions, but the prompt asked for "a pinned published version". I followed archives.md (`unversioned` plus the MD5).
7. Conclusion cells are written after the run, but the executed copy must match the committed notebook. I inserted the same Result cells into the executed copy without re-running; they are markdown only, so no output changed.
8. When several readings match, the record keeps the first one listed. For the firing rate that gave 2.132 Hz (reading a) even though reading b gives 2.103 Hz, closer to the paper's 2.10.

**4. Runtime and what failed**

- The notebook runs in 28.8 minutes on 4 cores: about 14 for the TE networks, 8 for the sub-network and synergy analysis, 5 for the model.
- One development command (an early full TE pass) ran into its one-hour timeout and printed nothing because of output buffering. That cost about an hour of the run.
- After the executed run I made one edit to `hdn.py`, a docstring note only, so the code that ran is unchanged.
- Nothing else failed.

Files are in `entries/crcns-ssc-3-timme-2016/`:
- reproduce_timme_2016.ipynb
- hdn.py
- README.md

The record is `attempts/crcns-ssc-3-timme-2016-01.yaml`.

## End of run

72 turns, 157 minutes, $7.82 at API prices, result: success.
