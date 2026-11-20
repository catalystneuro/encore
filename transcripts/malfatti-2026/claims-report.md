I'm stopping without writing any claims. The supplement this paper's results depend on is missing, and the protocol (Reader, step 1) says to write no claims in that case. `claims/malfatti-2026.yaml` was not created and nothing else in the repository was changed.

**What I read.** `paper/10.7554-elife.109286.txt`, which is the eLife Reviewed Preprint v3 (2026-11-02), "revised by the authors", taken from a supplied PDF. It has 38 pages:
- Main text: Methods, Results, the legends for Figures 1 to 6, and the Discussion.
- The reviews and author responses (pages 31 to 38).

It does not include the paper's supplement. Page 25 lists it only as "Additional files: Supplemental material", and neither the text nor the PDF contains it.

**Why the supplement matters.** Almost every result in the Results points to it for its support:
- **Supplemental Tables 1 to 6:** the paper's statistics are all here. That covers behaviour (Table 1 A to P), PC amplitude and the baseline and planning/execution analyses (Table 2 A to P), peak latency (3), peak width (4), assembly salience, area and resilience (5), and LFP power (6 A to P). The main text names the effects but gives no test statistics or p-values. Without these tables, the claims would have no statistics, and expected values could only come from reading figures.
- **Supplemental Figures 1 to 7:**
  - c-Fos validation (Figure 1)
  - the lower baseline PC activity in Chrna2-Cre+ mice (Figure 2I) and the planning/execution amplitudes (Figure 2J)
  - trial-interference baselines (Figure 3)
  - the execution/planning ratio (Figure 4)
  - latency (Figure 5) and peak width (Figure 6)
  - pre-injection training and the LFP outside prehensions (Figure 7)

  Several findings, such as the baseline decrease and the LFP session effects, are shown only in these figures.

**What is needed.** The eLife supplementary file(s) for RP109286 v3, with Supplemental Tables 1 to 6 and the legends and panels of Supplemental Figures 1 to 7, placed under `paper/`. The reader run can then be repeated.

Because I stopped at step 1, I didn't read the paper's code (https://gitlab.com/malfatti/M1MartinottiOnMovement), didn't run the quote checker, and listed no open method details.
