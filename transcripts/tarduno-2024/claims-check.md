# figshare-24639285 · claims-check · run 40571469263

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/figshare-24639285/ paper/; grep -n "Reader" -A40 docs/protocol.md | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 80,200p docs/protocol.md; python tools/claims_check.py claims/figshare-24639285/10.1038-s41597-024-03626-0.yaml paper/10.1038-s41597-024-03626-0.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/figshare-24639285/10.1038-s41597-024-03626-0.yaml; wc -l paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/figshare-24639285/10.1038-s41597-024-03626-0.yaml",
 "limit": 5
}
```

```
1	# Claims for Tarduno, Cottrell & Zhou (2024), Scientific Data, doi:10.1038/s41597-024-03626-0,
2	# on Figshare dataset 24639285 (doi:10.6084/m9.figshare.24639285.v1).
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-27,
4	# protocol pilot-12 as stated in docs/protocol.md (Reader).
5	#
```

**Agent calls Bash**

```bash
python3 -c "
for n,m,t in [('12021g2',7.011,.23),('12021g3',6.292,.26),('12040g1',8.002,.20),('12040g2',6.021,.27),('12053g1',5.283,.31),('12053g2',7.982,.20),('14053g1',3.203,.51),('14053g2',5.294,.31),('14053g3',4.523,.36),('71055g1',3.883,.42),('71055g3',4.202,.39)]:
  v=0.08/m*20; print(n,round(v,4),round((t/v-1)*100,1))"
```

```
12021g2 0.2282 0.8
12021g3 0.2543 2.2
12040g1 0.2 0.0
12040g2 0.2657 1.6
12053g1 0.3029 2.4
12053g2 0.2005 -0.2
14053g1 0.4995 2.1
14053g2 0.3022 2.6
14053g3 0.3537 1.8
71055g1 0.4121 1.9
71055g3 0.3808 2.4
```

**Agent**

The checker passed with no problems. On reading the claims against the paper I found several wrong paragraph references and some loose wording, which I'm fixing now.

**Agent calls Bash**

```bash
cd claims/figshare-24639285 && python3 - <<'EOF'
p='10.1038-s41597-024-03626-0.yaml'
s=open(p).read()
def r(a,b,count=1):
    global s
    assert s.count(a)==count,(a,s.count(a))
    s=s.replace(a,b)
r("Text errors noted. The Results cite Figure 3","Text errors noted. The Single crystal measurements section cites Figure 3")
r("# are those of 12040g1 in Table 1 (8.002E-09 emu, 0.20 uT). Table 1 values are 1 to 3% above\n# 8e-11 / M590 x 20 uT computed from its own M590 column.",
  "# are those of 12040g1 in Table 1 (8.002E-09 emu, 0.20 uT). Table 1 max intensities are 0 to 3%\n# above 8e-11 / M590 x 20 uT computed from its own M590 column (12053g2 0.2% below).")
r("Results, Single crystal measurements","Background & Summary, Single crystal measurements",5)
r("""  source: Background & Summary, paragraph 6
  quote: they nevertheless""","""  source: Background & Summary, paragraph 7
  quote: they nevertheless""")
r("  source: Background & Summary, paragraphs 2 and 6\n","  source: Abstract; Background & Summary, paragraphs 2 and 7\n")
r("""    differences are as in Table 2, and the failure criteria listed follow from them.""",
  """    differences are as in Table 2, which lists the criteria each failed.""")
r("""    The counts under each reading are reported.""",
  """    The counts under each reading are reported. The pTRM check comparison is reported and does
    not decide the outcome.""")
r("""    crystal inconsistent. Reproduced when both hold under one reading.""",
  """    crystal inconsistent; or (b), where 400 C was measured once, the 400 C direction lies within the
    alpha95 of the Fisher mean of the NRM replicates. Reproduced when the 590.0 replicates are
    inconsistent and (a) or (b) holds.""")
r("""    is no more than about twice the 590.1 TRM (20 uT), as linear recording predicts. Reproduced""",
  """    is no more than about twice the 590.1 TRM (20 uT), as linear recording predicts; the paper
    gives no bound for "far above 100%", so the ratios are reported and a ratio of the 590.4 TRM
    to twice the 590.1 TRM above 2 is taken as failing, a choice not from the paper. Reproduced""")
s=s.rstrip('\n')+"""
checks:
- date: 2026-10-27
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - table1-max-intensity, fig3-nrm-consistent, fig3-590-inconsistent, fig3-alteration-check-inconsistent, crystal-14053g1-400c-stable; source said "Results, Single crystal measurements", but the paper has no Results section and that subsection sits under Background & Summary. Opening comment changed to match.
  - baseline-range; source paragraph 6 changed to 7, the paragraph that holds the quoted sentence.
  - interpretation-impact-no-dynamo; source changed to the Abstract and Background & Summary paragraphs 2 and 7, where the paper states the impact and null-field reading. Paragraph 6 is about replicate measurement.
  - table2-fit-statistics; statement no longer says the failure criteria follow from the values, since the criterion only reports this and the paper does not claim it.
  - table2-no-fit; criterion now says the pTRM check comparison does not decide the outcome, since no expected values or rule were given for it.
  - crystal-14053g1-400c-stable; added reading (b), the 400 C direction compared with the NRM mean, because replicate 400 C measurements may not exist and the paper does not define "stable".
  - no-alteration-recording-efficiency; reading (b) named a bound ("about twice") without a cutoff. A cutoff is now stated and marked as not from the paper.
  - Opening comment; Table 1 max intensities are 0 to 3% above the formula value from its own M590 column (12053g2 is 0.2% below), not 1 to 3%.
  - Open, glass-directions-not-random and glass-af-no-change; the paper names no test or threshold. The readings and counting rules in the criteria are not from the paper and are labelled as such.
  - Open, M590 in Table 1 and the MAD and pTRM check definitions remain open, with readings named in the opening comment. Table 1 gives the same M590 (6.292E-09) for 12021g3 and 12040g3, which may be a copying error in the paper.
  - Open, Figure 1 and 2 nominal paleointensities and arrow ranges could not be read because no PDF was supplied.
"""
open(p,'w').write(s)
EOF
cd ../.. && python tools/claims_check.py claims/figshare-24639285/10.1038-s41597-024-03626-0.yaml paper/10.1038-s41597-024-03626-0.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

I checked the claims file for FIGSHARE:24639285 and corrected it. It is ready for an attempt.

**Checker result:** `17 claims, 17 quotes, 0 statistical values, 0 problems`. It said the same before and after my edits.

**What I checked against the paper:** all of Table 1 (24 values) and Table 2 (n, temperature range, MAD and R2 for nine specimens), the counts of failed glass specimens (22, of which 12 have no AF pre-treatment and 10 do), and the 3 of 25 success rate. All the recorded numbers are right.

**Changes, by claim:**
- **Five crystal claims** (table1-max-intensity, fig3-nrm-consistent, fig3-590-inconsistent, fig3-alteration-check-inconsistent, crystal-14053g1-400c-stable): the source said "Results, Single crystal measurements". The paper has no Results section; that subsection sits under Background & Summary. I changed the sources and the opening comment.
- **baseline-range:** the quoted sentence is in Background & Summary paragraph 7, not 6.
- **interpretation-impact-no-dynamo:** the source now points to the Abstract and Background & Summary paragraphs 2 and 7. Paragraph 6 is about the replicate measurements.
- **table2-fit-statistics:** the statement claimed the listed failure criteria "follow from" the values. The paper doesn't say that, and the criterion doesn't test it, so I removed it.
- **table2-no-fit:** the criterion now says the pTRM check comparison is only reported and does not decide the outcome. It had no expected values or rule.
- **crystal-14053g1-400c-stable:** the existing reading compares replicate 400 C directions, but there may be only one 400 C measurement. I added a second reading: the 400 C direction lies within the alpha95 of the mean NRM replicate direction.
- **no-alteration-recording-efficiency:** reading (b) said "about twice" with no cutoff. It now uses a ratio above 2 as failing, marked as a choice not taken from the paper.
- **Opening comment:** Table 1's max intensities are 0 to 3% above what the formula gives from its own M590 column, not 1 to 3%. 12053g2 is 0.2% below.

**Still open (recorded in the check entry):**
- For glass-directions-not-random and glass-af-no-change the paper names no test or threshold. The readings in those criteria are labelled as not from the paper.
- The definitions of M590, MAD and the pTRM check percentage remain open. The possible readings are listed in the opening comment.
- Table 1 gives the same M590 value (6.292E-09) for 12021g3 and 12040g3, which may be a copying error in the paper.
- No PDF was supplied, so the nominal paleointensities and arrow ranges in Figures 1 and 2 are not recorded.

**Ready:** yes. The check entry is at the end of the file with `ready: true`. Nothing is committed.

## End of run

8 turns, 2 minutes, result: success.
